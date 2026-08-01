"""
src/pipeline.py
===============
Pipeline for Experiment 9:
Dual Symbolic Regression Hurdle Architecture with 19 extended mathematical operators in BOTH Stage 1 Classifier and Stage 2 Regressor.
Uses strict physical chemical descriptors (EXCLUDING leaked GNN proxies E_GNN, M_net, M_abs).
"""

import os
import json
import numpy as np
import pandas as pd
from sklearn.metrics import precision_score, recall_score, f1_score
from .symbolic_classifier import SymbolicBoundaryClassifier
from .symbolic_regressor import SymbolicNonZeroRegressor

def run_exp9_pipeline(
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

    # Pure physical chemical candidate descriptor columns (EXCLUDING E_GNN, M_net, M_abs to prevent leakage)
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

    log_lines = []
    def log(msg=""):
        print(msg)
        log_lines.append(str(msg))

    log("======================================================================")
    log("EXPERIMENT 9: Extended Dual Symbolic Regression Hurdle Architecture")
    log("Includes 19 Operators: add, sub, mul, div, neg, abs, log, pow, sin, cos, exp, tan, cosec, sec, mod, ceil, sign, nth_root, gaussian_function")
    log("Clean Physical Descriptors (No Leakage: E_GNN, M_net, M_abs removed)")
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

        # ─── STAGE 1: Symbolic Boundary Classifier with 19 Extended Operators ───
        if is_zi:
            y_bin = (y_all > thr).astype(int)
            zero_pct = (1.0 - y_bin.mean()) * 100.0
            log(f"Zero-Inflation Rate: {zero_pct:.1f}% ({np.sum(y_bin == 0)} zeros, {np.sum(y_bin == 1)} non-zeros)")
            log("Running Stage 1 Symbolic Boundary Classifier S_cls(x) > 0 (19 Operators)...")

            sym_cls = SymbolicBoundaryClassifier(population_size=1500, generations=15, random_state=42)
            sym_cls.fit(X_all, y_bin, feature_names=feature_cols)
            cls_eval = sym_cls.evaluate(X_all, y_bin)

            pred_bin = sym_cls.predict(X_all)
            cls_acc = cls_eval['accuracy']
            cls_prec = cls_eval['precision']
            cls_rec = cls_eval['recall']
            cls_f1 = cls_eval['f1']
            cls_formula = cls_eval['program']

            log("--> STAGE 1 DISCOVERED SYMBOLIC DECISION BOUNDARY S_cls(x):")
            log(f"    S_cls(x) = {cls_formula}")
            log("--> Stage 1 Symbolic Classifier Metrics:")
            log(f"    - Classification Accuracy : {cls_acc * 100:.2f}%")
            log(f"    - F1-Score               : {cls_f1:.4f}")
            log(f"    - Precision              : {cls_prec:.4f}")
            log(f"    - Recall                 : {cls_rec:.4f}")

        else:
            pred_bin = np.ones(len(y_all), dtype=int)
            cls_acc, cls_prec, cls_rec, cls_f1 = 1.0, 1.0, 1.0, 1.0
            cls_formula = "N/A (Continuous Baseline)"
            zero_pct = 0.0

        # ─── STAGE 2: Symbolic Non-Zero Regressor with 19 Extended Operators ───
        if is_zi:
            nz_idx = y_all > thr
        else:
            nz_idx = np.ones(len(y_all), dtype=bool)

        X_nz = d_clean.iloc[nz_idx][feature_cols].values
        y_nz = y_all[nz_idx]

        log(f"\nRunning Stage 2 Symbolic Non-Zero Regressor S_reg(x) (19 Operators) on {len(y_nz)} active samples...")
        sym_reg = SymbolicNonZeroRegressor(population_size=2000, generations=25, random_state=42)
        sym_reg.fit(X_nz, y_nz, feature_names=feature_cols)
        reg_eval = sym_reg.evaluate(X_nz, y_nz)

        reg_sub_r2 = reg_eval['r2']
        reg_sub_mse = reg_eval['mse']
        reg_sub_mae = reg_eval['mae']
        reg_formula = reg_eval['program']

        log("--> STAGE 2 DISCOVERED SYMBOLIC NON-ZERO REGRESSION FORMULA S_reg(x):")
        log(f"    S_reg(x) = {reg_formula}")
        log("--> Stage 2 Non-Zero Subset Regression Metrics:")
        log(f"    - Subset R2  : {reg_sub_r2 * 100:.2f}%")
        log(f"    - Subset MSE : {reg_sub_mse:.6f}")
        log(f"    - Subset MAE : {reg_sub_mae:.6f}")

        # ─── STAGE 3: Combined Dual Symbolic Hurdle System Inference ───
        S_reg_all = sym_reg.predict(X_all)
        if allow_neg:
            S_reg_clean = S_reg_all
        else:
            S_reg_clean = np.maximum(0.0, S_reg_all)

        if is_zi:
            y_pipeline = np.where(pred_bin == 0, 0.0, S_reg_clean)
        else:
            y_pipeline = S_reg_clean

        ss_tot_all = np.sum((y_all - np.mean(y_all)) ** 2)
        ss_res_all = np.sum((y_all - y_pipeline) ** 2)
        pipe_r2 = float(1.0 - (ss_res_all / (ss_tot_all + 1e-10)))
        pipe_mse = float(np.mean((y_all - y_pipeline) ** 2))
        pipe_mae = float(np.mean(np.abs(y_all - y_pipeline)))

        log(f"\n>>> COMBINED DUAL SYMBOLIC REGRESSION PIPELINE RESULT:")
        log(f"    - Final Pipeline R2  : {pipe_r2 * 100:.2f}% ({pipe_r2:.6f})")
        log(f"    - Final Pipeline MSE : {pipe_mse:.6e}")
        log(f"    - Final Pipeline MAE : {pipe_mae:.6f}")
        log("")

        all_results[target_name] = {
            'zero_pct': zero_pct,
            'cls_acc': cls_acc,
            'cls_f1': cls_f1,
            'cls_prec': cls_prec,
            'cls_rec': cls_rec,
            'cls_formula': cls_formula,
            'reg_sub_r2': reg_sub_r2,
            'reg_sub_mse': reg_sub_mse,
            'reg_sub_mae': reg_sub_mae,
            'reg_formula': reg_formula,
            'pipe_r2': pipe_r2,
            'pipe_mse': pipe_mse,
            'pipe_mae': pipe_mae
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
        f.write("# Experiment 9: Extended Dual Symbolic Regression Hurdle Architecture Summary Report\n\n")
        f.write("**Dataset:** `exp_v2/data/data_24_7_2026/double_perovskite_dataset.csv` (2,000 double perovskites)  \n")
        f.write("**Data Leakage Audit:** Removed `E_GNN`, `M_net`, `M_abs`. Evaluated on 33 pure physical/chemical descriptors.  \n")
        f.write("**Stage 1 Classifier:** Short Symbolic Regression with 19 extended operators (`gplearn` custom +1/-1 classification fitness)  \n")
        f.write("**Stage 2 Regressor:** Standard Symbolic Regression with 19 extended operators (`gplearn` `SymbolicRegressor` with MAE fitness)  \n")
        f.write("**Operator Set (19 Primitives):** `add, sub, mul, div, neg, abs, log, pow, sin, cos, exp, tan, cosec, sec, mod, ceil, sign, nth_root, gaussian_function`  \n\n")
        f.write("---\n\n")

        f.write("## Performance Summary Table\n\n")
        f.write("| Target Property | Stage 1 Cls Acc (%) | Stage 1 F1 | Stage 2 Sub R² (%) | **Final Pipeline R² (%)** | Final MSE | Final MAE |\n")
        f.write("| :--- | :---: | :---: | :---: | :---: | :---: | :---: |\n")

        for target_name, res in all_results.items():
            f.write(f"| **{target_name}** | {res['cls_acc']*100:.2f}% | {res['cls_f1']:.4f} | {res['reg_sub_r2']*100:.2f}% | **{res['pipe_r2']*100:.2f}%** | {res['pipe_mse']:.6f} | {res['pipe_mae']:.4f} |\n")

        f.write("\n---\n\n")

    print(f"Markdown summary report saved to: {md_report_path}")

    # Generate discovered_equations.md
    with open(disc_eq_path, "w", encoding="utf-8") as f:
        f.write("# Experiment 9: Discovered Analytical Dual Symbolic Equations Report (19 Extended Operators)\n\n")
        f.write("This document presents the complete 100% interpretable analytical symbolic equations discovered by Genetic Programming (using 19 extended mathematical operators) on 33 pure physical chemical descriptors (with leaked GNN proxies `E_GNN`, `M_net`, `M_abs` removed).\n\n")
        f.write("---\n\n")

        for target_name, res in all_results.items():
            f.write(f"## Target Property: {target_name}\n\n")
            f.write(f"- **Stage 1 Classification Accuracy:** **{res['cls_acc']*100:.2f}%** (F1 = {res['cls_f1']:.4f})  \n")
            f.write(f"- **Stage 2 Non-Zero Subset $R^2$:** **{res['reg_sub_r2']*100:.2f}%**  \n")
            f.write(f"- **Final Combined Dual-SR Pipeline $R^2$:** **{res['pipe_r2']*100:.2f}%** (MSE = {res['pipe_mse']:.6f}, MAE = {res['pipe_mae']:.4f})  \n\n")

            f.write("### 1. Stage 1 Discovered Symbolic Decision Boundary Classifier Formula $S_{\\text{cls}}(\\mathbf{x})$\n\n")
            f.write("$$\\widehat{y}_{\\text{bin}} = 1 \\quad \\text{if } S_{\\text{cls}}(\\mathbf{x}) > 0.0 \\quad \\text{else } 0$$\n\n")
            f.write("```text\n")
            f.write(f"S_cls(x) = {res['cls_formula']}\n")
            f.write("```\n\n")

            f.write("### 2. Stage 2 Discovered Symbolic Non-Zero Regressor Formula $S_{\\text{reg}}(\\mathbf{x})$\n\n")
            f.write("```text\n")
            f.write(f"S_reg(x) = {res['reg_formula']}\n")
            f.write("```\n\n")

            f.write("### 3. Combined Dual-SR Hurdle System Analytical Formula\n\n")
            f.write("$$\\widehat{y}_{\\text{pipeline}}(\\mathbf{x}) = \\begin{cases} 0.0 & \\text{if } S_{\\text{cls}}(\\mathbf{x}) \\le 0.0 \\\\ \\max\\left(0.0, S_{\\text{reg}}(\\mathbf{x})\\right) & \\text{if } S_{\\text{cls}}(\\mathbf{x}) > 0.0 \\end{cases}$$\n\n")
            f.write("---\n\n")

    print(f"Discovered equations report saved to: {disc_eq_path}")

    return all_results
