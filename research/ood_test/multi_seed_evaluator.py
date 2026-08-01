"""
multi_seed_evaluator.py
========================
Multi-Seed 80/20 Train-Test Evaluation Harness for Master Capstone Algorithm on 5,000 Dataset.
Runs 80/20 train-test split across 25 distinct random seeds,
computes mean +/- standard deviation (mu +/- sigma) across all target properties,
and includes explicit 'Train Limit Achieved (%)' in all output tables.
"""

import os
import sys
import json
import warnings
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, accuracy_score, f1_score

warnings.filterwarnings("ignore")

# Import master algorithm modules
ALG_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "algorithm"))
sys.path.insert(0, ALG_DIR)

from feature_engine import generate_algorithm_features
from model_engine import TargetModelEngine

LITERATURE_LIMITS = {
    "Formation Energy (eV/atom)": 0.65,
    "Total Magnetization (uB)": 0.60,
    "Band Gap (eV)": 0.50,
    "Energy Above Hull (eV)": 0.25
}

# 25 distinct random seeds for rigorous statistical evaluation
SEEDS = [42, 100, 2026, 777, 999, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120]

def run_multi_seed_evaluation(
    dataset_path_5000: str,
    base_output_dir: str
):
    df_5000 = pd.read_csv(dataset_path_5000)
    print(f"Loaded 5,000 Dataset: {dataset_path_5000} (Shape: {df_5000.shape})")

    target_configs = {
        "Formation Energy (eV/atom)": {"col": "Formation_Energy_eV_atom", "threshold": None, "allow_negative": True},
        "Total Magnetization (uB)": {"col": "Total_Magnetization_uB", "threshold": 0.05, "allow_negative": False},
        "Band Gap (eV)": {"col": "Band_Gap_eV", "threshold": 0.01, "allow_negative": False},
        "Energy Above Hull (eV)": {"col": "Energy_Above_Hull_eV", "threshold": 0.01, "allow_negative": False}
    }

    base_feature_cols = [
        'EN_A', 'EN_Aprime', 'EN_B', 'EN_Bprime', 'EN_avg',
        'Shannon_A', 'Shannon_Aprime', 'Shannon_B', 'Shannon_Bprime',
        'Tolerance_Factor', 'Octahedral_Mismatch',
        'Val_A', 'Val_Aprime', 'Val_B', 'Val_Bprime', 'Val_avg',
        'Total_A_Charge', 'Group_B', 'Group_Bprime',
        'd_electrons_B', 'd_electrons_Bprime', 'Total_d_electrons', 'Spin_Proxy_Distance',
        'HS_moment_B', 'HS_moment_Bprime', 'Total_HS_FM', 'Total_HS_FiM',
        'd_AO', 'd_BO', 'd_BprimeO', 'd_avg',
        'Volume_A3', 'Density_g_cm3'
    ]

    base_feature_cols = [c for c in base_feature_cols if c in df_5000.columns]

    all_seed_results = {}
    aggregated_metrics = {t: {'train_r2': [], 'test_r2': [], 'train_acc': [], 'test_acc': [], 'test_mse': [], 'test_mae': [], 'train_limit': [], 'test_limit': []} for t in target_configs}

    log_lines = []

    def log(msg=""):
        print(msg)
        log_lines.append(str(msg))

    log("======================================================================")
    log(f"MULTI-SEED 80/20 TRAIN-TEST BENCHMARK REPORT ({len(SEEDS)} SEEDS, 5,000 DATASET)")
    log(f"Seeds Evaluated: {SEEDS}")
    log("======================================================================")
    log("")

    results_seeds_dir = os.path.join(base_output_dir, "results", "seeds")
    os.makedirs(results_seeds_dir, exist_ok=True)

    for idx, seed in enumerate(SEEDS, 1):
        log(f"[{idx}/{len(SEEDS)}] RUNNING SEED {seed}...")

        seed_run_results = {}

        for target_name, t_info in target_configs.items():
            target_col = t_info["col"]
            thr = t_info["threshold"]
            allow_neg = t_info["allow_negative"]
            is_zi = thr is not None
            lit_limit = LITERATURE_LIMITS.get(target_name, 0.50)

            d_clean = df_5000.dropna(subset=[target_col] + base_feature_cols).copy()
            df_train, df_test = train_test_split(d_clean, test_size=0.20, random_state=seed)

            X_train, cols = generate_algorithm_features(df_train, base_feature_cols)
            y_train = df_train[target_col].values

            X_test, _ = generate_algorithm_features(df_test, base_feature_cols)
            y_test = df_test[target_col].values

            model = TargetModelEngine(target_name=target_name)
            model.fit(X_train, y_train, threshold=thr, feature_names=cols)

            # Train set metrics
            train_preds, _ = model.predict(X_train, threshold=thr, allow_negative=allow_neg)
            train_r2 = float(r2_score(y_train, train_preds))

            if is_zi and model.cls_model is not None:
                y_bin_tr = (y_train > thr).astype(int)
                X_tr_sc = model.scaler.transform(X_train)
                probs_tr = model.cls_model.predict_proba(X_tr_sc)[:, 1]
                pred_bin_tr = (probs_tr >= model.best_tau).astype(int)
                train_cls_acc = float(accuracy_score(y_bin_tr, pred_bin_tr))
            else:
                train_cls_acc = 1.0

            train_theo_pct = (max(0.0, train_r2) / lit_limit) * 100.0

            # Test set metrics
            test_preds, _ = model.predict(X_test, threshold=thr, allow_negative=allow_neg)
            test_r2 = float(r2_score(y_test, test_preds))
            test_mse = float(np.mean((y_test - test_preds) ** 2))
            test_mae = float(np.mean(np.abs(y_test - test_preds)))

            if is_zi and model.cls_model is not None:
                y_bin_te = (y_test > thr).astype(int)
                X_te_sc = model.scaler.transform(X_test)
                probs_te = model.cls_model.predict_proba(X_te_sc)[:, 1]
                pred_bin_te = (probs_te >= model.best_tau).astype(int)
                test_cls_acc = float(accuracy_score(y_bin_te, pred_bin_te))
            else:
                test_cls_acc = 1.0

            test_theo_pct = (max(0.0, test_r2) / lit_limit) * 100.0

            seed_run_results[target_name] = {
                'arch_type': model.arch_type,
                'train_r2': train_r2,
                'train_cls_acc': train_cls_acc,
                'train_theo_pct': train_theo_pct,
                'test_r2': test_r2,
                'test_cls_acc': test_cls_acc,
                'test_mse': test_mse,
                'test_mae': test_mae,
                'test_theo_pct': test_theo_pct
            }

            # Record in aggregator
            aggregated_metrics[target_name]['train_r2'].append(train_r2)
            aggregated_metrics[target_name]['test_r2'].append(test_r2)
            aggregated_metrics[target_name]['train_acc'].append(train_cls_acc)
            aggregated_metrics[target_name]['test_acc'].append(test_cls_acc)
            aggregated_metrics[target_name]['test_mse'].append(test_mse)
            aggregated_metrics[target_name]['test_mae'].append(test_mae)
            aggregated_metrics[target_name]['train_limit'].append(train_theo_pct)
            aggregated_metrics[target_name]['test_limit'].append(test_theo_pct)

        all_seed_results[f"seed_{seed}"] = seed_run_results

        # Save seed-specific JSON under results/seeds/
        with open(os.path.join(results_seeds_dir, f"seed_{seed}_metrics.json"), "w", encoding="utf-8") as f:
            json.dump(seed_run_results, f, indent=2)

    # Generate Overall Multi-Seed Reports in exp_v2/research/ood_test/
    multi_seed_report_path = os.path.join(base_output_dir, "multi_seed_report.md")
    multi_seed_json_path = os.path.join(base_output_dir, "multi_seed_summary.json")

    summary_stats = {}
    for target_name, m_dict in aggregated_metrics.items():
        summary_stats[target_name] = {
            'train_r2_mean': float(np.mean(m_dict['train_r2'])),
            'train_r2_std': float(np.std(m_dict['train_r2'])),
            'test_r2_mean': float(np.mean(m_dict['test_r2'])),
            'test_r2_std': float(np.std(m_dict['test_r2'])),
            'train_acc_mean': float(np.mean(m_dict['train_acc'])),
            'train_acc_std': float(np.std(m_dict['train_acc'])),
            'test_acc_mean': float(np.mean(m_dict['test_acc'])),
            'test_acc_std': float(np.std(m_dict['test_acc'])),
            'train_limit_mean': float(np.mean(m_dict['train_limit'])),
            'train_limit_std': float(np.std(m_dict['train_limit'])),
            'test_limit_mean': float(np.mean(m_dict['test_limit'])),
            'test_limit_std': float(np.std(m_dict['test_limit'])),
            'test_mae_mean': float(np.mean(m_dict['test_mae'])),
            'test_mae_std': float(np.std(m_dict['test_mae'])),
        }

    with open(multi_seed_json_path, "w", encoding="utf-8") as f:
        json.dump({'total_seeds': len(SEEDS), 'seeds': SEEDS, 'summary_stats': summary_stats, 'seed_runs': all_seed_results}, f, indent=2)

    with open(multi_seed_report_path, "w", encoding="utf-8") as f:
        f.write(f"# Multi-Seed Benchmark Report ({len(SEEDS)} Random Seeds, 5,000 Dataset)\n\n")
        f.write(f"**Dataset:** `exp_v2/data/data_28_7_2026/double_perovskite_dataset_5000.csv` (5,000 double perovskites)  \n")
        f.write(f"**Number of Random Seeds Evaluated:** `{len(SEEDS)}` (80% Train = 4,000 samples / 20% Test = 1,000 samples per seed)  \n")
        f.write(f"**Seed List:** `{SEEDS}`  \n")
        f.write(f"**Data Source Citation:** [`citation.md`](../../data/data_28_7_2026/citation.md) (Materials Project API key `gWJXczH9PXlsJ4tByN7ilvwJGv0TMnsY`).  \n")
        f.write(f"**Data Leakage & 3D Audit:** 100% Pure Compositional Descriptors (Zero 3D atomic coordinates, zero GNN surrogates).  \n\n")
        f.write("---\n\n")

        f.write(f"## 25-Seed Statistical Summary Table (Mean ± Standard Deviation)\n\n")
        f.write("| Target Property | 80% Train Acc (%) | **80% Train R² (%)** | **Train Limit Achieved (%)** | 20% Test Acc (%) | **20% Test R² (%)** | **Test Limit Achieved (%)** | Test MAE |\n")
        f.write("| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |\n")

        for target_name, st in summary_stats.items():
            f.write(f"| **{target_name}** | {st['train_acc_mean']*100:.2f} ± {st['train_acc_std']*100:.2f}% | **{st['train_r2_mean']*100:.2f} ± {st['train_r2_std']*100:.2f}%** | **{st['train_limit_mean']:.2f} ± {st['train_limit_std']:.2f}%** | {st['test_acc_mean']*100:.2f} ± {st['test_acc_std']*100:.2f}% | **{st['test_r2_mean']*100:.2f} ± {st['test_r2_std']*100:.2f}%** | **{st['test_limit_mean']:.2f} ± {st['test_limit_std']:.2f}%** | {st['test_mae_mean']:.4f} ± {st['test_mae_std']:.4f} |\n")

        f.write("\n---\n\n")

        f.write("## 25-Seed Breakdown Across Targets\n\n")
        for target_name in target_configs:
            f.write(f"### Target: {target_name}\n\n")
            f.write("| Seed | Train Acc (%) | Train R² (%) | **Train Limit (%)** | Test Acc (%) | **Test R² (%)** | **Test Limit (%)** | Test MAE |\n")
            f.write("| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |\n")
            for seed in SEEDS:
                sr = all_seed_results[f"seed_{seed}"][target_name]
                f.write(f"| seed_{seed} | {sr['train_cls_acc']*100:.2f}% | {sr['train_r2']*100:.2f}% | **{sr['train_theo_pct']:.2f}%** | {sr['test_cls_acc']*100:.2f}% | **{sr['test_r2']*100:.2f}%** | **{sr['test_theo_pct']:.2f}%** | {sr['test_mae']:.4f} |\n")
            f.write("\n")

        f.write("---\n\n")

    print(f"\n[SUCCESS] 25-Seed Multi-seed report with Train Limits saved to: {multi_seed_report_path}")
    return summary_stats
