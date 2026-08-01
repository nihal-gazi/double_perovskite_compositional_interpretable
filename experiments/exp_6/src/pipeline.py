"""
src/pipeline.py
===============
Pipeline for Experiment 6:
Symbolic Regression Decision Boundary Classifier (+1/-1 fitness, including protected 'pow' operator)
+ Optimal Top-K* Fourier Ensemble Regressor dynamically selected per depth D in {3, 5, 10, 50, 100}.
Uses strict physical chemical descriptors (EXCLUDING leaked GNN proxies E_GNN, M_net, M_abs).
Generates discovered_equations.md containing full expanded Fourier formulas with substituted fitted coefficients.
"""

import os
import json
import numpy as np
import pandas as pd
from sklearn.metrics import precision_score, recall_score, f1_score
from .symbolic_classifier import SymbolicBoundaryClassifier
from .fourier_regressor import FourierSeriesRegressor

def format_expanded_fourier_equation(fitter, feature_name: str) -> str:
    w = fitter.weights
    x_min = fitter.x_min
    x_max = fitter.x_max
    depth = fitter.depth
    range_x = x_max - x_min if (x_max - x_min) > 1e-8 else 1.0

    lines = []
    lines.append(f"f_{{{feature_name}}}(x) = {w[0]:+.6f}")
    for m in range(1, depth + 1):
        a_m = w[2 * m - 1]
        b_m = w[2 * m]
        sign_a = "+" if a_m >= 0 else "-"
        sign_b = "+" if b_m >= 0 else "-"
        lines.append(f"    {sign_a} {abs(a_m):.6f} * cos({m} * (2*pi*(x - {x_min:.6f}) / {range_x:.6f} - pi))")
        lines.append(f"    {sign_b} {abs(b_m):.6f} * sin({m} * (2*pi*(x - {x_min:.6f}) / {range_x:.6f} - pi))")
    return "\n".join(lines)

def run_exp6_pipeline(
    dataset_path: str,
    results_dir: str,
    k_range: list = list(range(1, 11)),
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
    priority_selected_equations = {}

    log_lines = []
    def log(msg=""):
        print(msg)
        log_lines.append(str(msg))

    log("======================================================================")
    log("EXPERIMENT 6: Hybrid Symbolic-Fourier Hurdle Architecture Pipeline")
    log("Clean Physical Descriptors (No Leakage: E_GNN, M_net, M_abs removed)")
    log("Stage 1: Symbolic Regression Classifier with 'pow' primitive (+1/-1 fitness)")
    log("Stage 2: Top-K* Fourier Ensemble Non-Zero Regressor (Sweeping K=1..10 per D)")
    log("======================================================================")
    log(f"Dataset Size       : {len(df)} materials")
    log(f"Input Features N   : {len(feature_cols)}")
    log(f"K Sweep Range      : K = {k_range}")
    log(f"Depths Evaluated D : {depths}")
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

        if is_zi:
            y_bin = (y_all > thr).astype(int)
            zero_pct = (1.0 - y_bin.mean()) * 100.0
            log(f"Zero-Inflation Rate: {zero_pct:.1f}% ({np.sum(y_bin == 0)} zeros, {np.sum(y_bin == 1)} non-zeros)")
            log("Running Symbolic Regression (with 'pow') for Decision Boundary S(x) > 0...")

            sym_cls = SymbolicBoundaryClassifier(population_size=1500, generations=15, random_state=42)
            sym_cls.fit(X_all, y_bin, feature_names=feature_cols)
            cls_eval = sym_cls.evaluate(X_all, y_bin)

            pred_bin = sym_cls.predict(X_all)
            cls_acc = cls_eval['accuracy']
            cls_prec = cls_eval['precision']
            cls_rec = cls_eval['recall']
            cls_f1 = cls_eval['f1']
            discovered_formula = cls_eval['program']

            log("--> STAGE 1 DISCOVERED SYMBOLIC DECISION BOUNDARY FORMULA S(x):")
            log(f"    S(x) = {discovered_formula}")
            log("--> Stage 1 Symbolic Classifier Metrics:")
            log(f"    - Classification Accuracy : {cls_acc * 100:.2f}%")
            log(f"    - F1-Score               : {cls_f1:.4f}")
            log(f"    - Precision              : {cls_prec:.4f}")
            log(f"    - Recall                 : {cls_rec:.4f}")

        else:
            pred_bin = np.ones(len(y_all), dtype=int)
            cls_acc, cls_prec, cls_rec, cls_f1 = 1.0, 1.0, 1.0, 1.0
            discovered_formula = "N/A (Continuous Baseline)"
            zero_pct = 0.0

        if is_zi:
            nz_idx = y_all > thr
        else:
            nz_idx = np.ones(len(y_all), dtype=bool)

        x_nz = d_clean.iloc[nz_idx]
        y_nz = y_all[nz_idx]

        target_depth_results = {}
        depth_fitters = {}

        for D in depths:
            log(f"\n--- Evaluating Stage 2 & Pipeline at Fourier Depth D = {D} ---")

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
                    'fitter': f_reg,
                    'all_preds': f_reg.predict(d_clean[feat].values),
                    'nz_preds': f_reg.predict(x_feat_nz)
                })

            reg_fits.sort(key=lambda item: item['r2'], reverse=True)
            depth_fitters[D] = reg_fits

            best_k_star = 1
            best_pipe_r2 = -float('inf')
            best_pipe_metrics = {}

            for K in k_range:
                top_k_reg = reg_fits[:K]
                nz_reg_matrix = np.column_stack([item['nz_preds'] for item in top_k_reg])
                F_reg_nz_k = np.mean(nz_reg_matrix, axis=1)

                ss_tot_nz = np.sum((y_nz - np.mean(y_nz)) ** 2)
                ss_res_nz = np.sum((y_nz - F_reg_nz_k) ** 2)
                reg_sub_r2_k = float(1.0 - (ss_res_nz / (ss_tot_nz + 1e-10)))

                all_reg_matrix = np.column_stack([item['all_preds'] for item in top_k_reg])
                raw_ensemble_all = np.mean(all_reg_matrix, axis=1)

                if allow_neg:
                    F_reg_all_k = raw_ensemble_all
                else:
                    F_reg_all_k = np.maximum(0.0, raw_ensemble_all)

                if is_zi:
                    y_pipe_k = np.where(pred_bin == 0, 0.0, F_reg_all_k)
                else:
                    y_pipe_k = F_reg_all_k

                ss_tot_all = np.sum((y_all - np.mean(y_all)) ** 2)
                ss_res_all = np.sum((y_all - y_pipe_k) ** 2)
                pipe_r2_k = float(1.0 - (ss_res_all / (ss_tot_all + 1e-10)))
                pipe_mse_k = float(np.mean((y_all - y_pipe_k) ** 2))
                pipe_mae_k = float(np.mean(np.abs(y_all - y_pipe_k)))

                if pipe_r2_k > best_pipe_r2:
                    best_pipe_r2 = pipe_r2_k
                    best_k_star = K
                    best_pipe_metrics = {
                        'best_k': K,
                        'reg_sub_r2': reg_sub_r2_k,
                        'reg_sub_mse': float(np.mean((y_nz - F_reg_nz_k) ** 2)),
                        'reg_sub_mae': float(np.mean(np.abs(y_nz - F_reg_nz_k))),
                        'top_reg_fits': top_k_reg,
                        'top_reg_features': [item['feature'] for item in top_k_reg],
                        'pipe_r2': pipe_r2_k,
                        'pipe_mse': pipe_mse_k,
                        'pipe_mae': pipe_mae_k
                    }

            log(f"--> OPTIMAL K ENSEMBLE CAPACITY AT D={D}: K* = {best_k_star}")
            log(f"    - Stage 2 Non-Zero Subset R2 : {best_pipe_metrics['reg_sub_r2']*100:.2f}%")
            log(f"    - Final Pipeline R2         : {best_pipe_metrics['pipe_r2']*100:.2f}% ({best_pipe_metrics['pipe_r2']:.6f})")

            target_depth_results[D] = {
                'depth': D,
                'zero_pct': zero_pct,
                'cls_acc': cls_acc,
                'cls_f1': cls_f1,
                'cls_prec': cls_prec,
                'cls_rec': cls_rec,
                'symbolic_formula': discovered_formula,
                'best_k': best_k_star,
                'reg_sub_r2': best_pipe_metrics['reg_sub_r2'],
                'reg_sub_mse': best_pipe_metrics['reg_sub_mse'],
                'reg_sub_mae': best_pipe_metrics['reg_sub_mae'],
                'top_reg_fits': best_pipe_metrics['top_reg_fits'],
                'top_reg_features': best_pipe_metrics['top_reg_features'],
                'pipe_r2': best_pipe_metrics['pipe_r2'],
                'pipe_mse': best_pipe_metrics['pipe_mse'],
                'pipe_mae': best_pipe_metrics['pipe_mae']
            }

        all_results[target_name] = target_depth_results

        # Selection Priority Rule for Best D*
        high_acc_depths = [D for D in depths if target_depth_results[D]['pipe_r2'] >= 0.90]
        if len(high_acc_depths) > 0:
            best_D_star = high_acc_depths[0]
            priority_used = "Priority 1 (Pipeline R2 >= 90%)"
        else:
            r2_d5 = target_depth_results[5]['pipe_r2']
            r2_d10 = target_depth_results[10]['pipe_r2']
            best_D_star = 5 if r2_d5 >= r2_d10 else 10
            priority_used = "Priority 2 (Max R2 between D=5 and D=10)"

        selected_res = target_depth_results[best_D_star]
        log(f"\n>>> PRIORITY SELECTED BEST FOURIER DEPTH FOR '{target_name}': D* = {best_D_star} via {priority_used}")
        log(f"    Final Pipeline R2 = {selected_res['pipe_r2']*100:.2f}% | Best K* = {selected_res['best_k']}")

        priority_selected_equations[target_name] = {
            'D_star': best_D_star,
            'priority_used': priority_used,
            'selected_res': selected_res
        }
        log("")

    # Save metrics_summary.txt
    with open(txt_log_path, "w", encoding="utf-8") as f:
        f.write("\n".join(log_lines))
    print(f"\nLog saved to: {txt_log_path}")

    # Save raw JSON results
    json_export = {
        target: {
            str(D): {
                k: v for k, v in res.items() if k != 'top_reg_fits'
            } for D, res in res_dict.items()
        } for target, res_dict in all_results.items()
    }
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(json_export, f, indent=2)
    print(f"Raw JSON saved to: {json_path}")

    # Generate Markdown Summary Report
    with open(md_report_path, "w", encoding="utf-8") as f:
        f.write("# Experiment 6: Hybrid Symbolic Decision Boundary Classifier (with 'pow') + Optimal Top-K* Fourier Ensemble Regressor Report (Clean Physical Descriptors)\n\n")
        f.write("**Dataset:** `exp_v2/data/data_24_7_2026/double_perovskite_dataset.csv` (2,000 double perovskites)  \n")
        f.write("**Data Leakage Audit:** Removed `E_GNN`, `M_net`, `M_abs`. Evaluated on 33 pure physical/chemical descriptors.  \n")
        f.write("**Stage 1 Classifier:** Short Symbolic Regression with `pow` operator (`gplearn` custom +1/-1 classification fitness)  \n")
        f.write("**Stage 2 Regressor:** Dynamically Selected Optimal Top-K* Fourier Ensemble Average per Depth D  \n")
        f.write(f"**Evaluated Fourier Depths (num_freq D):** `{depths}`  \n\n")
        f.write("---\n\n")

        for target_name, target_dict in all_results.items():
            f.write(f"## Target Property: {target_name}\n\n")
            first_res = list(target_dict.values())[0]
            f.write("**Discovered Symbolic Decision Boundary Formula S(x) (with 'pow'):**  \n")
            f.write(f"```text\nS(x) = {first_res['symbolic_formula']}\n```  \n")
            f.write(f"**Stage 1 Classification Metrics:** Accuracy = **{first_res['cls_acc']*100:.2f}%** | F1-Score = **{first_res['cls_f1']:.4f}** | Precision = **{first_res['cls_prec']:.4f}** | Recall = **{first_res['cls_rec']:.4f}**\n\n")

            f.write("| Fourier Depth (D) | Stage 1 Symbolic Acc (%) | Stage 1 F1 | **Optimal Best K*** | Stage 2 Sub R² (%) | **Final Pipeline R² (%)** | Final MSE | Final MAE | Top Fourier Features (K*) |\n")
            f.write("| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |\n")

            for D, res in target_dict.items():
                cls_acc_str = f"{res['cls_acc']*100:.2f}%"
                cls_f1_str = f"{res['cls_f1']:.4f}"
                best_k_str = f"**K* = {res['best_k']}**"
                sub_r2_str = f"{res['reg_sub_r2']*100:.2f}%"
                pipe_r2_str = f"**{res['pipe_r2']*100:.2f}%**"
                mse_str = f"{res['pipe_mse']:.6f}"
                mae_str = f"{res['pipe_mae']:.4f}"
                reg_feats = ", ".join([f"`{feat}`" for feat in res['top_reg_features'][:3]])

                f.write(f"| D = {D} | {cls_acc_str} | {cls_f1_str} | {best_k_str} | {sub_r2_str} | {pipe_r2_str} | {mse_str} | {mae_str} | {reg_feats} |\n")

            f.write("\n---\n\n")

    print(f"Markdown summary report saved to: {md_report_path}")

    # Generate discovered_equations.md
    with open(disc_eq_path, "w", encoding="utf-8") as f:
        f.write("# Experiment 6: Discovered Symbolic & Expanded Fourier Analytical Equations Report (Clean Physical Descriptors)\n\n")
        f.write("This document contains the complete, fully expanded analytical formulas for both **Stage 1 (Symbolic Boundary Classifier with 'pow')** and **Stage 2 (Fitted 1D Fourier Regressors)** on pure physical chemical descriptors (with leaked GNN proxies `E_GNN`, `M_net`, `M_abs` removed).\n\n")
        f.write("### Selection Priority Rules Enforced for Best Fourier Depth $D^*$:\n")
        f.write("1. **Priority 1**: If any depth $D \\in \\{3, 5, 10, 50, 100\\}$ achieves Final Pipeline $R^2 \\ge 90.0\\%$, select that depth $D^*$.\n")
        f.write("2. **Priority 2**: If no depth achieves $\\ge 90.0\\%$, select the depth $D^* \\in \\{5, 10\\}$ with the highest Final Pipeline $R^2$.\n\n")
        f.write("---\n\n")

        for target_name, sel_info in priority_selected_equations.items():
            D_star = sel_info['D_star']
            p_used = sel_info['priority_used']
            res = sel_info['selected_res']
            best_k = res['best_k']

            f.write(f"## Target Property: {target_name}\n\n")
            f.write(f"- **Selection Rule Applied:** {p_used}  \n")
            f.write(f"- **Selected Best Fourier Depth $D^*$:** **{D_star}**  \n")
            f.write(f"- **Optimal Ensemble Size $K^*$:** **{best_k}**  \n")
            f.write(f"- **Stage 1 Classification Accuracy:** **{res['cls_acc']*100:.2f}%**  \n")
            f.write(f"- **Stage 2 Subset $R^2$:** **{res['reg_sub_r2']*100:.2f}%**  \n")
            f.write(f"- **Final Combined Pipeline $R^2$:** **{res['pipe_r2']*100:.2f}%**  \n\n")

            f.write("### 1. Stage 1 Symbolic Decision Boundary Classifier Formula\n\n")
            f.write("$$\\widehat{y}_{\\text{bin}} = 1 \\quad \\text{if } S_{\\text{sym}}(\\mathbf{x}) > 0.0 \\quad \\text{else } 0$$\n\n")
            f.write("```text\n")
            f.write(f"S(x) = {res['symbolic_formula']}\n")
            f.write("```\n\n")

            f.write(f"### 2. Stage 2 Full Expanded 1D Fourier Series Regressor Equations ($D^* = {D_star}, K^* = {best_k}$)\n\n")
            f.write(f"The Stage 2 prediction is the average of the top $K^* = {best_k}$ descriptor Fourier series:\n\n")
            f.write("$$F_{\\text{reg}}(\\mathbf{x}) = \\frac{1}{" + str(best_k) + "} \\sum_{j=1}^{" + str(best_k) + "} f_{I_{(j)}}(x_{(j)})$$\n\n")

            for rank, item in enumerate(res['top_reg_fits'], start=1):
                feat_name = item['feature']
                fitter = item['fitter']
                f.write(f"#### Descriptor Rank #{rank}: `{feat_name}` (Subset $R^2 = {item['r2']*100:.2f}\\%$)\n\n")
                f.write("```text\n")
                eq_text = format_expanded_fourier_equation(fitter, feat_name)
                f.write(eq_text + "\n")
                f.write("```\n\n")

            f.write("### 3. Complete Two-Stage Hurdle System Equation\n\n")
            f.write("$$\\widehat{y}_{\\text{pipeline}}(\\mathbf{x}) = \\begin{cases} 0.0 & \\text{if } S_{\\text{sym}}(\\mathbf{x}) \\le 0.0 \\\\ \\frac{1}{" + str(best_k) + "} \\sum_{j=1}^{" + str(best_k) + "} f_{I_{(j)}}(x_{(j)}) & \\text{if } S_{\\text{sym}}(\\mathbf{x}) > 0.0 \\end{cases}$$\n\n")
            f.write("---\n\n")

    print(f"Discovered equations report saved to: {disc_eq_path}")

    return all_results, priority_selected_equations
