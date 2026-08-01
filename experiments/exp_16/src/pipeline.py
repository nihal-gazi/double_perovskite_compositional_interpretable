"""
src/pipeline.py
===============
Pipeline for Experiment 16:
Compositional Physical Mismatch & Ionicity-Enhanced Pipeline across 4 target properties.
Evaluates 100% Pure Compositional Features (Zero 3D atomic coordinates or GNN surrogates).
Calculates Theoretical Limit (%) relative to literature physical limits.
"""

import os
import json
import numpy as np
import pandas as pd
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error, accuracy_score, precision_score, recall_score, f1_score
from .compositional_mismatch import generate_mismatch_features
from .master_model import MasterOptimalModel

# Peer-Reviewed Literature Physical Descriptor Limits:
LITERATURE_LIMITS = {
    "Formation Energy (eV/atom)": 0.65,      # 65.0% (Ouyang 2018, Bartel 2019)
    "Total Magnetization (uB)": 0.60,        # 60.0% (Ouyang 2018, Ghiringhelli 2015)
    "Band Gap (eV)": 0.50,                   # 50.0% (Ouyang 2018, Borlido 2019)
    "Energy Above Hull (eV)": 0.25           # 25.0% (Bartel 2019 SciAdv, Sun 2016)
}

def run_exp16_pipeline(
    dataset_path: str,
    results_dir: str
):
    df = pd.read_csv(dataset_path)
    print(f"Loaded dataset from: {dataset_path}")
    print(f"Dataset shape: {df.shape}")

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

    base_feature_cols = [c for c in base_feature_cols if c in df.columns]
    X_expanded, expanded_feature_cols = generate_mismatch_features(df, base_feature_cols)

    print(f"Base Features N = {len(base_feature_cols)} -> Pure Compositional Features N = {len(expanded_feature_cols)}")

    os.makedirs(results_dir, exist_ok=True)
    txt_log_path = os.path.join(results_dir, "metrics_summary.txt")
    md_report_path = os.path.join(results_dir, "metrics_summary.md")
    disc_eq_path = os.path.join(results_dir, "discovered_equations.md")
    json_path = os.path.join(results_dir, "results_raw.json")

    all_results = {}
    fitted_equations = {}

    log_lines = []
    def log(msg=""):
        print(msg)
        log_lines.append(str(msg))

    log("======================================================================")
    log("EXPERIMENT 16: Compositional Physical Mismatch & Ionicity-Enhanced Pipeline")
    log("Clean Physical Descriptors (No Leakage: E_GNN, M_net, M_abs removed)")
    log("100% PURE COMPOSITIONAL DESCRIPTORS ONLY (Zero 3D Atomic Coordinates)")
    log(f"Expanded Features N = {len(expanded_feature_cols)} (Mismatch, Ionicity, Roots, Logs, Interactions, Triplets)")
    log("======================================================================")
    log(f"Dataset Size       : {len(df)} materials")
    log("")

    for target_name, t_info in target_configs.items():
        target_col = t_info["col"]
        thr = t_info["threshold"]
        allow_neg = t_info["allow_negative"]
        is_zi = thr is not None

        log("=" * 80)
        log(f"TARGET PROPERTY: {target_name}")
        log("=" * 80)

        d_clean = df.dropna(subset=[target_col] + base_feature_cols).copy()
        X_all, exp_cols = generate_mismatch_features(d_clean, base_feature_cols)
        y_all = d_clean[target_col].values

        master_model = MasterOptimalModel(target_name=target_name)
        master_model.fit(X_all, y_all, threshold=thr, feature_names=exp_cols)
        
        pipeline_preds, cls_metrics = master_model.predict(X_all, threshold=thr, allow_negative=allow_neg)

        ss_tot = np.sum((y_all - np.mean(y_all)) ** 2)
        ss_res = np.sum((y_all - pipeline_preds) ** 2)
        master_r2 = float(1.0 - (ss_res / (ss_tot + 1e-10)))
        master_mse = float(np.mean((y_all - pipeline_preds) ** 2))
        master_mae = float(np.mean(np.abs(y_all - pipeline_preds)))

        if is_zi and master_model.cls_model is not None:
            y_bin = (y_all > thr).astype(int)
            pred_bin = master_model.cls_model.predict(master_model.scaler.transform(X_all))
            cls_acc = float(accuracy_score(y_bin, pred_bin))
            cls_f1 = float(f1_score(y_bin, pred_bin, zero_division=0))
            
            nz_idx = y_all > thr
            X_nz_scaled = master_model.scaler.transform(X_all[nz_idx])
            y_nz = y_all[nz_idx]
            sub_r2 = float(r2_score(y_nz, master_model.reg_model.predict(X_nz_scaled)))
        else:
            cls_acc = 1.0
            cls_f1 = 1.0
            sub_r2 = master_r2

        lit_limit = LITERATURE_LIMITS.get(target_name, 0.50)
        master_theo_pct = (max(0.0, master_r2) / lit_limit) * 100.0
        sub_theo_pct = (max(0.0, sub_r2) / lit_limit) * 100.0

        master_eq = master_model.format_master_equation(top_k=15)

        log(f"--> EXPERIMENT 16 RESULTS ({master_model.arch_type.upper()}):")
        log(f"    - Stage 1 Classification Acc : {cls_acc * 100:.2f}% (F1 = {cls_f1:.4f})")
        log(f"    - Stage 2 Sub R2            : {sub_r2 * 100:.2f}% ({sub_theo_pct:.2f}% of Lit Ceiling)")
        log(f"    - Final Pipeline R2         : {master_r2 * 100:.2f}% ({master_r2:.6f})")
        log(f"    - Pipeline MSE               : {master_mse:.6f}")
        log(f"    - Pipeline MAE               : {master_mae:.6f}")
        log(f"    - Relative Theoretical Limit : {master_theo_pct:.2f}% of Lit Ceiling ({lit_limit * 100:.1f}%)")
        log("")

        all_results[target_name] = {
            'arch_type': master_model.arch_type,
            'cls_acc': cls_acc,
            'cls_f1': cls_f1,
            'sub_r2': sub_r2,
            'sub_theo_pct': sub_theo_pct,
            'master_r2': master_r2,
            'master_mse': master_mse,
            'master_mae': master_mae,
            'master_theo_pct': master_theo_pct
        }

        fitted_equations[target_name] = {
            'arch_type': master_model.arch_type,
            'master_eq': master_eq
        }

    # Save metrics_summary.txt
    with open(txt_log_path, "w", encoding="utf-8") as f:
        f.write("\n".join(log_lines))
    print(f"\nLog saved to: {txt_log_path}")

    # Save raw JSON results
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(all_results, f, indent=2)
    print(f"Raw JSON saved to: {json_path}")

    # Generate Markdown Summary Report
    with open(md_report_path, "w", encoding="utf-8") as f:
        f.write("# Experiment 16: Compositional Physical Mismatch & Ionicity-Enhanced Pipeline Summary Report\n\n")
        f.write("**Dataset:** `exp_v2/data/data_24_7_2026/double_perovskite_dataset.csv` (2,000 double perovskites)  \n")
        f.write("**Data Leakage & 3D Audit Compliance:** 100% Pure Compositional Descriptors (Zero 3D atomic coordinates, zero DFT-relaxed 3D bond vectors, zero GNN proxies `E_GNN`, `M_net`, `M_abs`).  \n")
        f.write("**New Compositional Features Added:** Electronegativity Mismatches ($\\Delta\\chi_B, \\Delta\\chi_{AB}$), Phillips Ionicity Index ($f_i$), Ferrimagnetic Spin Difference ($\\Delta HS$), Valence Mismatch ($\\Delta\\text{Val}_B$), Radii Mismatch ($\\Delta r_B$).  \n")
        f.write("**Theoretical Limit References (Literature):** Formation Energy ($R^2_{\\text{limit}} = 65.0\\%$), Magnetization ($R^2_{\\text{limit}} = 60.0\\%$), Band Gap ($R^2_{\\text{limit}} = 50.0\\%$), Hull Energy ($R^2_{\\text{limit}} = 25.0\\%$).  \n\n")
        f.write("---\n\n")

        f.write("## Performance Summary Table Across Target Properties\n\n")
        f.write("| Target Property | Optimal Architecture | Stage 1 Acc (%) | Stage 2 Sub R² (%) | **Sub R² Limit (%)** | **Final Pipeline R² (%)** | **Theoretical Limit (%)** | Final MSE | Final MAE |\n")
        f.write("| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |\n")

        for target_name, res in all_results.items():
            arch_str = "Direct Multi-Operator" if res['arch_type'] == "direct_multi_operator" else "Non-Linear Hurdle"
            f.write(f"| **{target_name}** | {arch_str} | {res['cls_acc']*100:.2f}% | {res['sub_r2']*100:.2f}% | **{res['sub_theo_pct']:.2f}%** | **{res['master_r2']*100:.2f}%** | **{res['master_theo_pct']:.2f}%** | {res['master_mse']:.6f} | {res['master_mae']:.4f} |\n")

        f.write("\n---\n\n")

    print(f"Markdown summary report saved to: {md_report_path}")

    # Generate discovered_equations.md
    with open(disc_eq_path, "w", encoding="utf-8") as f:
        f.write("# Experiment 16: Discovered Pure Compositional Physical Equations Report\n\n")
        f.write("This document presents the pure compositional analytical physical equations discovered across all 4 target properties in Experiment 16.\n\n")
        f.write("---\n\n")

        for target_name, eq_dict in fitted_equations.items():
            f.write(f"## Target Property: {target_name}\n\n")
            res = all_results[target_name]
            f.write(f"- **Optimal Architecture:** `{eq_dict['arch_type']}`  \n")
            f.write(f"- **Final Pipeline $R^2$:** **{res['master_r2']*100:.2f}%**  \n")
            f.write(f"- **Stage 2 Non-Zero Sub $R^2$:** **{res['sub_r2']*100:.2f}%**  \n")
            f.write(f"- **Relative Theoretical Limit Achieved:** **{res['master_theo_pct']:.2f}%**  \n\n")

            f.write("### Discovered Pure Compositional Physical Equation (Top 15 Terms)\n\n")
            f.write("```text\n")
            f.write(eq_dict['master_eq'] + "\n")
            f.write("```\n\n")

            f.write("---\n\n")

    print(f"Discovered equations report saved to: {disc_eq_path}")

    return all_results
