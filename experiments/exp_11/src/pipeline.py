"""
src/pipeline.py
===============
Pipeline for Experiment 11:
Standard Linear Regression Baseline across the 4 target properties.
Evaluates both Direct Single-Stage Linear Regression and Two-Stage Linear Hurdle Architecture.
Calculates Theoretical Limit (%) relative to literature physical limits.
"""

import os
import json
import numpy as np
import pandas as pd
from .linear_model import StandardLinearModel

# Peer-Reviewed Literature Physical Descriptor Limits:
LITERATURE_LIMITS = {
    "Formation Energy (eV/atom)": 0.65,      # 65.0% (Ouyang 2018, Bartel 2019)
    "Total Magnetization (uB)": 0.60,        # 60.0% (Ouyang 2018, Ghiringhelli 2015)
    "Band Gap (eV)": 0.50,                   # 50.0% (Ouyang 2018, Borlido 2019)
    "Energy Above Hull (eV)": 0.25           # 25.0% (Bartel 2019 SciAdv, Sun 2016)
}

def run_exp11_pipeline(
    dataset_path: str,
    results_dir: str
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

    # 33 pure physical chemical descriptors (EXCLUDING leaked GNN proxies E_GNN, M_net, M_abs)
    feature_cols = [
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

    feature_cols = [c for c in feature_cols if c in df.columns]
    print(f"Total pure physical input features N = {len(feature_cols)} (Leaked proxies E_GNN, M_net, M_abs removed)")

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
    log("EXPERIMENT 11: Standard Linear Regression Baseline Pipeline")
    log("Clean Physical Descriptors (No Leakage: E_GNN, M_net, M_abs removed)")
    log("Evaluates Direct OLS Linear Regression & Two-Stage Linear Hurdle System")
    log("======================================================================")
    log(f"Dataset Size       : {len(df)} materials")
    log(f"Input Features N   : {len(feature_cols)}")
    log("")

    for target_name, t_info in target_configs.items():
        target_col = t_info["col"]
        thr = t_info["threshold"]
        allow_neg = t_info["allow_negative"]
        is_zi = thr is not None

        log("=" * 80)
        log(f"TARGET PROPERTY: {target_name} (Threshold = {thr})")
        log("=" * 80)

        d_clean = df.dropna(subset=[target_col] + feature_cols).copy()
        X_all = d_clean[feature_cols].values
        y_all = d_clean[target_col].values

        # ─── 1. DIRECT SINGLE-STAGE LINEAR REGRESSION ───
        direct_model = StandardLinearModel(use_ridge=False)
        direct_model.fit_regressor(X_all, y_all, feature_names=feature_cols)
        direct_eval = direct_model.evaluate_regressor(X_all, y_all)

        direct_r2 = direct_eval['r2']
        direct_mse = direct_eval['mse']
        direct_mae = direct_eval['mae']
        direct_eq = direct_model.format_linear_equation(target_name)

        log("--> 1. DIRECT SINGLE-STAGE OLS LINEAR REGRESSION RESULT:")
        log(f"    - Direct R2  : {direct_r2 * 100:.2f}% ({direct_r2:.6f})")
        log(f"    - Direct MSE : {direct_mse:.6f}")
        log(f"    - Direct MAE : {direct_mae:.6f}")

        # ─── 2. TWO-STAGE LINEAR HURDLE ARCHITECTURE ───
        if is_zi:
            y_bin = (y_all > thr).astype(int)
            zero_pct = (1.0 - y_bin.mean()) * 100.0
            log(f"Zero-Inflation Rate: {zero_pct:.1f}% ({np.sum(y_bin == 0)} zeros, {np.sum(y_bin == 1)} non-zeros)")

            # Stage 1: Linear Logistic Classifier
            cls_model = StandardLinearModel()
            cls_model.fit_classifier(X_all, y_bin, feature_names=feature_cols)
            cls_eval = cls_model.evaluate_classifier(X_all, y_bin)
            pred_bin = cls_eval['preds']

            log("--> STAGE 1 LINEAR LOGISTIC CLASSIFIER METRICS:")
            log(f"    - Classification Accuracy : {cls_eval['accuracy'] * 100:.2f}%")
            log(f"    - F1-Score               : {cls_eval['f1']:.4f}")

            # Stage 2: Linear Regressor on Non-Zeros
            nz_idx = y_all > thr
            X_nz = d_clean.iloc[nz_idx][feature_cols].values
            y_nz = y_all[nz_idx]

            hurdle_reg = StandardLinearModel(use_ridge=False)
            hurdle_reg.fit_regressor(X_nz, y_nz, feature_names=feature_cols)
            reg_nz_eval = hurdle_reg.evaluate_regressor(X_nz, y_nz)
            hurdle_nz_eq = hurdle_reg.format_linear_equation(f"{target_name} (Non-Zero)")

            log("--> STAGE 2 LINEAR REGRESSOR (NON-ZERO SUBSET) METRICS:")
            log(f"    - Subset R2  : {reg_nz_eval['r2'] * 100:.2f}%")
            log(f"    - Subset MSE : {reg_nz_eval['mse']:.6f}")
            log(f"    - Subset MAE : {reg_nz_eval['mae']:.6f}")

            # Stage 3: Hurdle Combined Pipeline Inference
            y_nz_pred_all = hurdle_reg.predict_regressor(X_all)
            if not allow_neg:
                y_nz_pred_clean = np.maximum(0.0, y_nz_pred_all)
            else:
                y_nz_pred_clean = y_nz_pred_all

            y_pipeline = np.where(pred_bin == 0, 0.0, y_nz_pred_clean)

            ss_tot = np.sum((y_all - np.mean(y_all)) ** 2)
            ss_res = np.sum((y_all - y_pipeline) ** 2)
            hurdle_r2 = float(1.0 - (ss_res / (ss_tot + 1e-10)))
            hurdle_mse = float(np.mean((y_all - y_pipeline) ** 2))
            hurdle_mae = float(np.mean(np.abs(y_all - y_pipeline)))

            cls_acc = cls_eval['accuracy']
            cls_f1 = cls_eval['f1']
            sub_r2 = reg_nz_eval['r2']

        else:
            zero_pct = 0.0
            cls_acc, cls_f1 = 1.0, 1.0
            sub_r2 = direct_r2
            hurdle_r2 = direct_r2
            hurdle_mse = direct_mse
            hurdle_mae = direct_mae
            hurdle_nz_eq = direct_eq

        # Calculate Relative Theoretical Limit Percentage Achieved
        lit_limit = LITERATURE_LIMITS.get(target_name, 0.50)
        direct_theo_pct = (max(0.0, direct_r2) / lit_limit) * 100.0
        hurdle_theo_pct = (max(0.0, hurdle_r2) / lit_limit) * 100.0

        log(f"\n>>> COMBINED HURDLE SYSTEM RESULT:")
        log(f"    - Hurdle Pipeline R2        : {hurdle_r2 * 100:.2f}% ({hurdle_r2:.6f})")
        log(f"    - Hurdle Pipeline MSE       : {hurdle_mse:.6f}")
        log(f"    - Hurdle Pipeline MAE       : {hurdle_mae:.6f}")
        log(f"    - Relative Theoretical Limit: {hurdle_theo_pct:.2f}% of Lit Ceiling ({lit_limit * 100:.1f}%)")
        log("")

        all_results[target_name] = {
            'zero_pct': zero_pct,
            'direct_r2': direct_r2,
            'direct_mse': direct_mse,
            'direct_mae': direct_mae,
            'direct_theo_pct': direct_theo_pct,
            'cls_acc': cls_acc,
            'cls_f1': cls_f1,
            'sub_r2': sub_r2,
            'hurdle_r2': hurdle_r2,
            'hurdle_mse': hurdle_mse,
            'hurdle_mae': hurdle_mae,
            'hurdle_theo_pct': hurdle_theo_pct
        }

        fitted_equations[target_name] = {
            'direct_eq': direct_eq,
            'hurdle_nz_eq': hurdle_nz_eq
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
        f.write("# Experiment 11: Standard Linear Regression Baseline Summary Report\n\n")
        f.write("**Dataset:** `exp_v2/data/data_24_7_2026/double_perovskite_dataset.csv` (2,000 double perovskites)  \n")
        f.write("**Data Leakage Audit:** Removed `E_GNN`, `M_net`, `M_abs`. Evaluated on 33 pure physical/chemical descriptors.  \n")
        f.write("**Theoretical Limit References (Literature):** Formation Energy ($R^2_{\\text{limit}} = 65.0\\%$), Magnetization ($R^2_{\\text{limit}} = 60.0\\%$), Band Gap ($R^2_{\\text{limit}} = 50.0\\%$), Hull Energy ($R^2_{\\text{limit}} = 25.0\\%$).  \n\n")
        f.write("---\n\n")

        f.write("## Performance Summary Table\n\n")
        f.write("| Target Property | Direct OLS R² (%) | **Direct Theoretical Limit (%)** | Stage 1 Cls Acc (%) | Stage 2 Sub R² (%) | **Hurdle Pipeline R² (%)** | **Hurdle Theoretical Limit (%)** | Hurdle MSE | Hurdle MAE |\n")
        f.write("| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |\n")

        for target_name, res in all_results.items():
            f.write(f"| **{target_name}** | {res['direct_r2']*100:.2f}% | **{res['direct_theo_pct']:.2f}%** | {res['cls_acc']*100:.2f}% | {res['sub_r2']*100:.2f}% | **{res['hurdle_r2']*100:.2f}%** | **{res['hurdle_theo_pct']:.2f}%** | {res['hurdle_mse']:.6f} | {res['hurdle_mae']:.4f} |\n")

        f.write("\n---\n\n")

    print(f"Markdown summary report saved to: {md_report_path}")

    # Generate discovered_equations.md
    with open(disc_eq_path, "w", encoding="utf-8") as f:
        f.write("# Experiment 11: Discovered Fitted Linear Regression Equations Report\n\n")
        f.write("This document contains the exact unscaled analytical linear regression equations fitted across all 4 target properties on 33 pure physical descriptors (with leaked GNN proxies `E_GNN`, `M_net`, `M_abs` removed).\n\n")
        f.write("---\n\n")

        for target_name, eq_dict in fitted_equations.items():
            f.write(f"## Target Property: {target_name}\n\n")
            res = all_results[target_name]
            f.write(f"- **Direct OLS $R^2$:** **{res['direct_r2']*100:.2f}%**  \n")
            f.write(f"- **Two-Stage Hurdle Pipeline $R^2$:** **{res['hurdle_r2']*100:.2f}%**  \n")
            f.write(f"- **Relative Theoretical Limit Achieved:** **{res['hurdle_theo_pct']:.2f}%**  \n\n")

            f.write("### 1. Direct Single-Stage Linear Regression Formula\n\n")
            f.write("```text\n")
            f.write(eq_dict['direct_eq'] + "\n")
            f.write("```\n\n")

            if target_name != "Formation Energy (eV/atom)":
                f.write("### 2. Stage 2 Hurdle Non-Zero Linear Regressor Formula\n\n")
                f.write("```text\n")
                f.write(eq_dict['hurdle_nz_eq'] + "\n")
                f.write("```\n\n")

            f.write("---\n\n")

    print(f"Discovered equations report saved to: {disc_eq_path}")

    return all_results
