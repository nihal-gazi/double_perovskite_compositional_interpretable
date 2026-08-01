"""
src/pipeline.py
===============
Pipeline for Experiment 3:
Two-Stage Fourier Ensemble Hurdle Architecture for Zero-Inflated Double Perovskite Properties.
Conducts Fourier binary classification (Zero vs Non-Zero), non-zero Fourier regression,
and combined two-stage pipeline evaluation across depths D = {3, 5, 10, 50, 100}.
"""

import os
import json
import numpy as np
import pandas as pd
from sklearn.metrics import precision_score, recall_score, f1_score
from .fourier_classifier import FourierSeriesClassifier
from .fourier_regressor import FourierSeriesRegressor

def run_exp3_pipeline(
    dataset_path: str,
    results_dir: str,
    top_k: int = 5,
    depths: list = [3, 5, 10, 50, 100]
):
    df = pd.read_csv(dataset_path)
    print(f"Loaded dataset from: {dataset_path}")
    print(f"Dataset shape: {df.shape}")

    # Define target properties with zero-inflation thresholds
    target_configs = {
        "Band Gap (eV)": {"col": "Band_Gap_eV", "threshold": 0.01, "allow_negative": False},
        "Total Magnetization (uB)": {"col": "Total_Magnetization_uB", "threshold": 0.05, "allow_negative": False},
        "Energy Above Hull (eV)": {"col": "Energy_Above_Hull_eV", "threshold": 0.01, "allow_negative": False},
        "Formation Energy (eV/atom)": {"col": "Formation_Energy_eV_atom", "threshold": None, "allow_negative": True}
    }

    # Define candidate input descriptor feature columns (N features)
    feature_cols = [
        'EN_A', 'EN_Aprime', 'EN_B', 'EN_Bprime', 'EN_avg',
        'Shannon_A', 'Shannon_Aprime', 'Shannon_B', 'Shannon_Bprime',
        'Tolerance_Factor', 'Octahedral_Mismatch',
        'Val_A', 'Val_Aprime', 'Val_B', 'Val_Bprime', 'Val_avg',
        'Total_A_Charge', 'Group_B', 'Group_Bprime',
        'd_electrons_B', 'd_electrons_Bprime', 'Total_d_electrons', 'Spin_Proxy_Distance',
        'HS_moment_B', 'HS_moment_Bprime', 'Total_HS_FM', 'Total_HS_FiM',
        'd_AO', 'd_BO', 'd_BprimeO', 'd_avg',
        'Volume_A3', 'Density_g_cm3', 'E_GNN', 'M_net', 'M_abs'
    ]

    feature_cols = [c for c in feature_cols if c in df.columns]
    print(f"Total candidate input features N = {len(feature_cols)}")

    os.makedirs(results_dir, exist_ok=True)
    txt_log_path = os.path.join(results_dir, "metrics_summary.txt")
    md_report_path = os.path.join(results_dir, "metrics_summary.md")
    json_path = os.path.join(results_dir, "results_raw.json")

    all_results = {}

    log_lines = []
    def log(msg=""):
        print(msg)
        log_lines.append(str(msg))

    log("======================================================================")
    log("EXPERIMENT 3: Two-Stage Fourier Ensemble Hurdle Architecture Pipeline")
    log("======================================================================")
    log(f"Dataset Size       : {len(df)} materials")
    log(f"Input Features N   : {len(feature_cols)}")
    log(f"Top-K Ensemble     : K = {top_k}")
    log(f"Depths Evaluated D : {depths}")
    log("")

    for target_name, t_info in target_configs.items():
        target_col = t_info["col"]
        thr = t_info["threshold"]
        allow_neg = t_info["allow_negative"]
        is_zi = thr is not None

        log("=" * 75)
        log(f"TARGET PROPERTY: {target_name} (Threshold = {thr})")
        log("=" * 75)

        d_clean = df.dropna(subset=[target_col] + feature_cols).copy()
        y_all = d_clean[target_col].values

        target_depth_results = {}

        for D in depths:
            log(f"\n--- Evaluating Depth D = {D} ---")

            if is_zi:
                # ─── STAGE 1: Fourier Ensemble Binary Classification (Zero vs Non-Zero) ───
                y_bin = (y_all > thr).astype(int)
                zero_pct = (1.0 - y_bin.mean()) * 100.0

                cls_fits = []
                for feat in feature_cols:
                    x_feat = d_clean[feat].values
                    f_cls = FourierSeriesClassifier(depth=D, alpha=1e-4)
                    f_cls.fit(x_feat, y_bin)
                    eval_res = f_cls.evaluate(x_feat, y_bin)

                    cls_fits.append({
                        'feature': feat,
                        'accuracy': eval_res['accuracy'],
                        'f1': eval_res['f1'],
                        'precision': eval_res['precision'],
                        'recall': eval_res['recall'],
                        'fitter': f_cls
                    })

                cls_fits.sort(key=lambda item: item['accuracy'], reverse=True)
                top_cls_fits = cls_fits[:top_k]

                log(f"Stage 1 Top {top_k} Fourier Classifiers (Zero vs Non-Zero):")
                cls_raw_preds = []
                for rank, item in enumerate(top_cls_fits, start=1):
                    f_name = item['feature']
                    log(f"  Rank {rank}: Feature '{f_name:<20}' -> Acc = {item['accuracy']*100:.2f}% | F1 = {item['f1']:.4f}")
                    raw_p = item['fitter'].predict_raw(d_clean[f_name].values)
                    cls_raw_preds.append(raw_p)

                F_class_raw = np.mean(np.column_stack(cls_raw_preds), axis=1)
                pred_bin = (F_class_raw > 0.5).astype(int)

                cls_acc = float(np.mean(pred_bin == y_bin))
                cls_prec = float(precision_score(y_bin, pred_bin, zero_division=0))
                cls_rec = float(recall_score(y_bin, pred_bin, zero_division=0))
                cls_f1 = float(f1_score(y_bin, pred_bin, zero_division=0))

                log(f"--> Stage 1 Ensemble Classifier Result (K={top_k}, D={D}):")
                log(f"    - Accuracy  : {cls_acc * 100:.2f}%")
                log(f"    - F1-Score  : {cls_f1:.4f}")
                log(f"    - Precision : {cls_prec:.4f}")
                log(f"    - Recall    : {cls_rec:.4f}")

            else:
                pred_bin = np.ones(len(y_all), dtype=int)
                cls_acc, cls_prec, cls_rec, cls_f1 = 1.0, 1.0, 1.0, 1.0
                top_cls_fits = [{'feature': 'N/A (Continuous)'}] * top_k
                zero_pct = 0.0

            # ─── STAGE 2: Fourier Ensemble Non-Zero Regression ───
            if is_zi:
                nz_idx = y_all > thr
            else:
                nz_idx = np.ones(len(y_all), dtype=bool)

            x_nz = d_clean.iloc[nz_idx]
            y_nz = y_all[nz_idx]

            reg_fits = []
            for feat in feature_cols:
                x_feat_nz = x_nz[feat].values
                f_reg = FourierSeriesRegressor(depth=D, alpha=1e-4)
                f_reg.fit(x_feat_nz, y_nz)
                eval_res = f_reg.evaluate(x_feat_nz, y_nz)

                reg_fits.append({
                    'feature': feat,
                    'r2': eval_res['r2'],
                    'mse': eval_res['mse'],
                    'mae': eval_res['mae'],
                    'fitter': f_reg
                })

            reg_fits.sort(key=lambda item: item['r2'], reverse=True)
            top_reg_fits = reg_fits[:top_k]

            log(f"\nStage 2 Top {top_k} Non-Zero Fourier Regressors (on {len(y_nz)} active samples):")
            reg_nz_preds = []
            for rank, item in enumerate(top_reg_fits, start=1):
                f_name = item['feature']
                log(f"  Rank {rank}: Feature '{f_name:<20}' -> Subset R2 = {item['r2']*100:.2f}% | MSE = {item['mse']:.6f}")
                pred_p = item['fitter'].predict(x_nz[f_name].values)
                reg_nz_preds.append(pred_p)

            F_reg_nz = np.mean(np.column_stack(reg_nz_preds), axis=1)

            ss_tot_nz = np.sum((y_nz - np.mean(y_nz)) ** 2)
            ss_res_nz = np.sum((y_nz - F_reg_nz) ** 2)
            reg_sub_r2 = float(1.0 - (ss_res_nz / (ss_tot_nz + 1e-10)))
            reg_sub_mse = float(np.mean((y_nz - F_reg_nz) ** 2))
            reg_sub_mae = float(np.mean(np.abs(y_nz - F_reg_nz)))

            log(f"--> Stage 2 Ensemble Regressor Subset Result (K={top_k}, D={D}):")
            log(f"    - Subset R2  : {reg_sub_r2 * 100:.2f}%")
            log(f"    - Subset MSE : {reg_sub_mse:.6f}")
            log(f"    - Subset MAE : {reg_sub_mae:.6f}")

            # ─── STAGE 3: Combined Two-Stage Hurdle Pipeline Inference ───
            all_reg_preds = []
            for item in top_reg_fits:
                f_name = item['feature']
                p_all = item['fitter'].predict(d_clean[f_name].values)
                all_reg_preds.append(p_all)

            raw_ensemble_all = np.mean(np.column_stack(all_reg_preds), axis=1)
            if allow_neg:
                F_reg_all = raw_ensemble_all
            else:
                F_reg_all = np.maximum(0.0, raw_ensemble_all)

            if is_zi:
                y_pipeline = np.where(pred_bin == 0, 0.0, F_reg_all)
            else:
                y_pipeline = F_reg_all

            ss_tot_all = np.sum((y_all - np.mean(y_all)) ** 2)
            ss_res_all = np.sum((y_all - y_pipeline) ** 2)
            pipe_r2 = float(1.0 - (ss_res_all / (ss_tot_all + 1e-10)))
            pipe_mse = float(np.mean((y_all - y_pipeline) ** 2))
            pipe_mae = float(np.mean(np.abs(y_all - y_pipeline)))

            log(f"\n>>> COMBINED TWO-STAGE PIPELINE RESULT (D={D}):")
            log(f"    - Final Pipeline R2  : {pipe_r2 * 100:.2f}% ({pipe_r2:.6f})")
            log(f"    - Final Pipeline MSE : {pipe_mse:.6e}")
            log(f"    - Final Pipeline MAE : {pipe_mae:.6f}")

            target_depth_results[D] = {
                'depth': D,
                'zero_pct': zero_pct,
                'cls_acc': cls_acc,
                'cls_f1': cls_f1,
                'cls_prec': cls_prec,
                'cls_rec': cls_rec,
                'top_cls_features': [item['feature'] for item in top_cls_fits],
                'reg_sub_r2': reg_sub_r2,
                'reg_sub_mse': reg_sub_mse,
                'reg_sub_mae': reg_sub_mae,
                'top_reg_features': [item['feature'] for item in top_reg_fits],
                'pipe_r2': pipe_r2,
                'pipe_mse': pipe_mse,
                'pipe_mae': pipe_mae
            }

        all_results[target_name] = target_depth_results
        log("")

    # Save metrics_summary.txt
    with open(txt_log_path, "w", encoding="utf-8") as f:
        f.write("\n".join(log_lines))
    print(f"\nLog saved to: {txt_log_path}")

    # Save raw JSON results
    json_export = {
        target: {str(D): res for D, res in res_dict.items()}
        for target, res_dict in all_results.items()
    }
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(json_export, f, indent=2)
    print(f"Raw JSON saved to: {json_path}")

    # Generate Markdown Summary Report
    with open(md_report_path, "w", encoding="utf-8") as f:
        f.write("# Experiment 3: Two-Stage Fourier Ensemble Hurdle Architecture Report\n\n")
        f.write("**Dataset:** `exp_v2/data/data_24_7_2026/double_perovskite_dataset.csv` (2,000 double perovskites)  \n")
        f.write(f"**Ensemble Strategy:** Top K = {top_k} Fourier Models Average  \n")
        f.write(f"**Evaluated Fourier Depths (num_freq D):** `{depths}`  \n\n")
        f.write("---\n\n")

        for target_name, target_dict in all_results.items():
            f.write(f"## Target Property: {target_name}\n\n")
            f.write("| Fourier Depth (D) | Stage 1 Cls Acc (%) | Stage 1 F1 | Stage 2 Sub R² (%) | **Final Pipeline R² (%)** | Final MSE | Final MAE | Top-5 Stage 1 Features | Top-5 Stage 2 Features |\n")
            f.write("| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- | :--- |\n")

            for D, res in target_dict.items():
                cls_acc_str = f"{res['cls_acc']*100:.2f}%"
                cls_f1_str = f"{res['cls_f1']:.4f}"
                sub_r2_str = f"{res['reg_sub_r2']*100:.2f}%"
                pipe_r2_str = f"**{res['pipe_r2']*100:.2f}%**"
                mse_str = f"{res['pipe_mse']:.6f}"
                mae_str = f"{res['pipe_mae']:.4f}"
                cls_feats = ", ".join([f"`{feat}`" for feat in res['top_cls_features'][:3]])
                reg_feats = ", ".join([f"`{feat}`" for feat in res['top_reg_features'][:3]])

                f.write(f"| D = {D} | {cls_acc_str} | {cls_f1_str} | {sub_r2_str} | {pipe_r2_str} | {mse_str} | {mae_str} | {cls_feats} | {reg_feats} |\n")

            f.write("\n")

    print(f"Markdown summary report saved to: {md_report_path}")

    return all_results
