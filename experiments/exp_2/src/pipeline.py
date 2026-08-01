"""
src/pipeline.py
===============
Pipeline for Experiment 2:
Multi-descriptor 1D Fourier Transform distillation and top-K ensemble averaging across depths D = {3, 5, 10, 50, 100}.
"""

import os
import json
import numpy as np
import pandas as pd
from .fourier_fitter import FourierSeries1DFitter

def run_exp2_pipeline(
    dataset_path: str,
    results_dir: str,
    top_k: int = 5,
    depths: list = [3, 5, 10, 50, 100]
):
    """
    Executes Experiment 2 pipeline across all targets and depths D.

    Parameters
    ----------
    dataset_path : str
        Path to compiled double perovskite CSV dataset.
    results_dir : str
        Directory to save results logs and summary metrics.
    top_k : int
        Number of top Fourier transforms to select and ensemble average (default: 5).
    depths : list
        List of Fourier series depths D to evaluate (default: [3, 5, 10, 50, 100]).

    Returns
    -------
    dict
        Dictionary containing all evaluation results.
    """
    df = pd.read_csv(dataset_path)
    print(f"Loaded dataset from: {dataset_path}")
    print(f"Dataset shape: {df.shape}")

    # Define target properties
    target_configs = {
        "Formation Energy (eV/atom)": "Formation_Energy_eV_atom",
        "Band Gap (eV)": "Band_Gap_eV",
        "Total Magnetization (uB)": "Total_Magnetization_uB",
        "Energy Above Hull (eV)": "Energy_Above_Hull_eV"
    }

    # Define input descriptor feature columns (N features)
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

    # Filter out features that might be missing
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
    log("EXPERIMENT 2: Sequential Fourier Distillation & Top-K Ensemble Averaging")
    log("======================================================================")
    log(f"Dataset Size : {len(df)} materials")
    log(f"Input Features N : {len(feature_cols)}")
    log(f"Top-K Ensemble : K = {top_k}")
    log(f"Depths Evaluated D : {depths}")
    log("")

    for target_name, target_col in target_configs.items():
        log("=" * 70)
        log(f"TARGET PROPERTY: {target_name}")
        log("=" * 70)

        # Drop NaN for target and features
        d_clean = df.dropna(subset=[target_col] + feature_cols).copy()
        y_target = d_clean[target_col].values

        target_results = {}

        for D in depths:
            log(f"\n--- Evaluating Depth D = {D} ---")

            # Fit 1D Fourier Transform for each feature I[i] -> T
            feature_fits = []

            for feat in feature_cols:
                x_feat = d_clean[feat].values
                fitter = FourierSeries1DFitter(depth=D)
                fitter.fit(x_feat, y_target)
                metrics = fitter.evaluate(x_feat, y_target)

                feature_fits.append({
                    'feature': feat,
                    'r2': metrics['r2'],
                    'mse': metrics['mse'],
                    'mae': metrics['mae'],
                    'fitter': fitter
                })

            # Sort features by R2 accuracy descending
            feature_fits.sort(key=lambda item: item['r2'], reverse=True)

            # Pick top K=5 features
            top_k_fits = feature_fits[:top_k]

            log(f"Top {top_k} Individual Fourier Transforms for D={D}:")
            top_preds = []
            for rank, fit_item in enumerate(top_k_fits, start=1):
                f_name = fit_item['feature']
                f_r2 = fit_item['r2']
                f_mse = fit_item['mse']
                log(f"  Rank {rank}: Feature '{f_name}' -> R2 = {f_r2*100:.2f}% | MSE = {f_mse:.6f}")
                pred_i = fit_item['fitter'].predict(d_clean[f_name].values)
                top_preds.append(pred_i)

            # Compute ensemble average F_final = (f0 + f1 + ... + f4) / 5
            F_final = np.mean(np.column_stack(top_preds), axis=1)

            # Final ensemble accuracy calculation
            ss_tot = np.sum((y_target - np.mean(y_target)) ** 2)
            ss_res = np.sum((y_target - F_final) ** 2)
            final_r2 = float(1.0 - (ss_res / (ss_tot + 1e-10)))
            final_mse = float(np.mean((y_target - F_final) ** 2))
            final_mae = float(np.mean(np.abs(y_target - F_final)))

            log(f"\n>>> FINAL ENSEMBLE ACCURACY (D={D}):")
            log(f"    F_final = ({' + '.join([item['feature'] for item in top_k_fits])}) / {top_k}")
            log(f"    - Final R2 Accuracy : {final_r2 * 100:.2f}% ({final_r2:.6f})")
            log(f"    - Final MSE         : {final_mse:.6e}")
            log(f"    - Final MAE         : {final_mae:.6f}")

            target_results[D] = {
                'depth': D,
                'final_r2': final_r2,
                'final_mse': final_mse,
                'final_mae': final_mae,
                'top_features': [item['feature'] for item in top_k_fits],
                'top_individual_r2': [item['r2'] for item in top_k_fits]
            }

        all_results[target_name] = target_results
        log("")

    # Save metrics_summary.txt
    with open(txt_log_path, "w", encoding="utf-8") as f:
        f.write("\n".join(log_lines))
    print(f"\nLog saved to: {txt_log_path}")

    # Save json raw results
    json_export = {
        target: {str(D): res for D, res in res_dict.items()}
        for target, res_dict in all_results.items()
    }
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(json_export, f, indent=2)
    print(f"Raw JSON saved to: {json_path}")

    # Generate Markdown Summary Report
    with open(md_report_path, "w", encoding="utf-8") as f:
        f.write("# Experiment 2: Multi-Descriptor Fourier Transform Ensemble Distillation Report\n\n")
        f.write("**Dataset:** `exp_v2/data/data_24_7_2026/double_perovskite_dataset.csv` (2,000 double perovskites)  \n")
        f.write(f"**Ensemble Strategy:** Top K = {top_k} Fourier Transforms Average  \n")
        f.write(f"**Evaluated Fourier Depths (num_freq D):** `{depths}`  \n\n")
        f.write("---\n\n")

        for target_name, target_dict in all_results.items():
            f.write(f"## Target Property: {target_name}\n\n")
            f.write("| Fourier Depth (D) | Final Ensemble R² (%) | Final MSE | Final MAE | Top-5 Input Features Included |\n")
            f.write("| :---: | :---: | :---: | :---: | :--- |\n")

            for D, res in target_dict.items():
                r2_str = f"**{res['final_r2']*100:.2f}%**"
                mse_str = f"{res['final_mse']:.6f}"
                mae_str = f"{res['final_mae']:.4f}"
                feats_str = ", ".join([f"`{feat}`" for feat in res['top_features']])
                f.write(f"| D = {D} | {r2_str} | {mse_str} | {mae_str} | {feats_str} |\n")

            f.write("\n")

    print(f"Markdown summary report saved to: {md_report_path}")

    return all_results
