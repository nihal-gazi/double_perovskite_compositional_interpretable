"""
ablation_matrix.py
==================
Feature and Model Architecture Isolation Engine for Master Algorithm Ablation Study.
Implements Conditions C0 through C7.
"""

import os
import sys
import numpy as np
import pandas as pd

# Import from master algorithm package
ALG_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "algorithm"))
sys.path.insert(0, ALG_DIR)

from data_lookup import (
    PETTIFOR_MENDELEEV,
    FIRST_IONIZATION_ENERGY_EV,
    ELECTRON_AFFINITY_EV,
    BINARY_OXIDE_FORMATION_ENTHALPY_EV_ATOM,
    EA_OXYGEN,
    R_OXYGEN_SHANNON
)

def get_ablation_features(df: pd.DataFrame, base_feature_cols: list, condition_code: str) -> tuple[np.ndarray, list]:
    """
    Returns feature matrix X and feature names list for specific ablation condition C0-C7.
    """
    feat_df = df[base_feature_cols].copy()
    feat_cols = list(base_feature_cols)

    # Base classical features for C0
    val_a = df['Val_A'] if 'Val_A' in df.columns else 2.0
    val_ap = df['Val_Aprime'] if 'Val_Aprime' in df.columns else 2.0
    val_b = df['Val_B'] if 'Val_B' in df.columns else 3.0
    val_bp = df['Val_Bprime'] if 'Val_Bprime' in df.columns else 3.0

    d_b = df['d_electrons_B'] if 'd_electrons_B' in df.columns else pd.Series(0, index=df.index)
    d_bp = df['d_electrons_Bprime'] if 'd_electrons_Bprime' in df.columns else pd.Series(0, index=df.index)

    if 'EN_B' in df.columns and 'EN_Bprime' in df.columns:
        feat_df['Delta_EN_B'] = (df['EN_B'] - df['EN_Bprime']).abs()
        feat_cols.append('Delta_EN_B')

    if 'Shannon_B' in df.columns and 'Shannon_Bprime' in df.columns:
        feat_df['Delta_Shannon_B'] = (df['Shannon_B'] - df['Shannon_Bprime']).abs()
        feat_cols.append('Delta_Shannon_B')

    # C1+: Add Harrison Quantum Tight-Binding Gap
    if condition_code != "C0":
        if 'B_site' in df.columns and 'Bprime_site' in df.columns:
            ie_b = df['B_site'].map(FIRST_IONIZATION_ENERGY_EV).fillna(7.5)
            ie_bp = df['Bprime_site'].map(FIRST_IONIZATION_ENERGY_EV).fillna(7.5)

            feat_df['IE_B_eV'] = ie_b
            feat_df['IE_Bprime_eV'] = ie_bp
            feat_cols.extend(['IE_B_eV', 'IE_Bprime_eV'])

            min_ie_b = np.minimum(ie_b, ie_bp)
            delta_e_gap = min_ie_b - EA_OXYGEN
            feat_df['Tight_Binding_Gap_Proxy_eV'] = delta_e_gap
            feat_cols.append('Tight_Binding_Gap_Proxy_eV')

            if 'Shannon_B' in df.columns and 'Shannon_Bprime' in df.columns:
                r_b_avg = (df['Shannon_B'] + df['Shannon_Bprime']) / 2.0
                v_transfer_sq = ((r_b_avg + R_OXYGEN_SHANNON).abs() + 1e-4) ** -4
                feat_df['Harrison_Quantum_Gap_eV'] = np.sqrt(np.maximum(0.0, delta_e_gap**2) + v_transfer_sq)
                feat_cols.append('Harrison_Quantum_Gap_eV')

    # C2+: Add Birch-Murnaghan Strain Engine
    if condition_code not in ["C0", "C1"]:
        if 'Tolerance_Factor' in df.columns:
            feat_df['E_tolerance_strain'] = (df['Tolerance_Factor'] - 1.0) ** 2
            feat_cols.append('E_tolerance_strain')

        if 'Octahedral_Mismatch' in df.columns and 'Density_g_cm3' in df.columns:
            feat_df['E_oct_distortion_strain'] = (df['Octahedral_Mismatch'] ** 2) * df['Density_g_cm3']
            feat_cols.append('E_oct_distortion_strain')

    # C3+: Add Octahedral d0/d10 Closed-Shell Engine
    if condition_code not in ["C0", "C1", "C2"]:
        feat_df['Is_d0_B'] = (d_b == 0).astype(float)
        feat_df['Is_d10_B'] = (d_b == 10).astype(float)
        feat_df['Is_d0_Bprime'] = (d_bp == 0).astype(float)
        feat_df['Is_d10_Bprime'] = (d_bp == 10).astype(float)

        is_cs_b = (d_b == 0) | (d_b == 10)
        is_cs_bp = (d_bp == 0) | (d_bp == 10)
        feat_df['Is_Closed_Shell_both'] = (is_cs_b & is_cs_bp).astype(float)
        feat_df['Open_Shell_d_fraction'] = (d_b + d_bp) / 20.0
        feat_cols.extend(['Is_d0_B', 'Is_d10_B', 'Is_d0_Bprime', 'Is_d10_Bprime', 'Is_Closed_Shell_both', 'Open_Shell_d_fraction'])

    # C4+: Add Single-Perovskite Competing Phase Tie-Line Engine
    if condition_code not in ["C0", "C1", "C2", "C3"]:
        r_a = df['Shannon_A'] if 'Shannon_A' in df.columns else pd.Series(1.35, index=df.index)
        r_ap = df['Shannon_Aprime'] if 'Shannon_Aprime' in df.columns else r_a
        r_b = df['Shannon_B'] if 'Shannon_B' in df.columns else pd.Series(0.65, index=df.index)
        r_bp = df['Shannon_Bprime'] if 'Shannon_Bprime' in df.columns else r_b

        t_abo3 = (r_a + R_OXYGEN_SHANNON) / (np.sqrt(2.0) * (r_b + R_OXYGEN_SHANNON))
        t_apbpO3 = (r_ap + R_OXYGEN_SHANNON) / (np.sqrt(2.0) * (r_bp + R_OXYGEN_SHANNON))

        feat_df['t_ABO3'] = t_abo3
        feat_df['t_AprimeBprimeO3'] = t_apbpO3
        feat_df['Delta_t_sub_perov'] = (t_abo3 - t_apbpO3).abs()
        feat_cols.extend(['t_ABO3', 't_AprimeBprimeO3', 'Delta_t_sub_perov'])

        if 'B_site' in df.columns and 'Bprime_site' in df.columns:
            h_ox_b = df['B_site'].map(BINARY_OXIDE_FORMATION_ENTHALPY_EV_ATOM).fillna(-2.0)
            h_ox_bp = df['Bprime_site'].map(BINARY_OXIDE_FORMATION_ENTHALPY_EV_ATOM).fillna(-2.0)
            h_ox_a = df['A_site'].map(BINARY_OXIDE_FORMATION_ENTHALPY_EV_ATOM).fillna(-3.0) if 'A_site' in df.columns else -3.0
            h_ox_ap = df['Aprime_site'].map(BINARY_OXIDE_FORMATION_ENTHALPY_EV_ATOM).fillna(-3.0) if 'Aprime_site' in df.columns else h_ox_a

            feat_df['Delta_H_sub_perov_mismatch'] = (h_ox_b + h_ox_ap - h_ox_bp - h_ox_a).abs()
            feat_cols.append('Delta_H_sub_perov_mismatch')

            feat_df['D_hull_proxy'] = feat_df['Delta_t_sub_perov'] * feat_df['Delta_H_sub_perov_mismatch']
            feat_cols.append('D_hull_proxy')

            feat_df['Exp_D_hull_scale'] = np.exp(np.clip(feat_df['D_hull_proxy'] - 1.0, -5.0, 5.0))
            feat_cols.append('Exp_D_hull_scale')

    # Add Non-linear transformations for all conditions
    key_root_cols = ['Tolerance_Factor', 'EN_avg', 'Volume_A3', 'Density_g_cm3', 'Total_HS_FiM', 'Total_d_electrons']
    for col in key_root_cols:
        if col in feat_df.columns:
            new_c = f"sqrt({col})"
            feat_df[new_c] = np.sqrt(np.abs(feat_df[col]))
            feat_cols.append(new_c)

    key_log_cols = ['Volume_A3', 'Density_g_cm3', 'Total_HS_FiM', 'Total_d_electrons']
    for col in key_log_cols:
        if col in feat_df.columns:
            new_c = f"log({col}+1)"
            feat_df[new_c] = np.log(np.abs(feat_df[col]) + 1.0)
            feat_cols.append(new_c)

    key_sq_cols = ['Tolerance_Factor', 'Octahedral_Mismatch', 'EN_avg', 'Total_HS_FiM', 'Volume_A3', 'Density_g_cm3']
    for col in key_sq_cols:
        if col in feat_df.columns:
            new_c = f"({col})^2"
            feat_df[new_c] = feat_df[col] ** 2
            feat_cols.append(new_c)

    interaction_pairs = [
        ('Tolerance_Factor', 'Octahedral_Mismatch'),
        ('EN_avg', 'Volume_A3'),
        ('EN_avg', 'Density_g_cm3'),
        ('Total_HS_FiM', 'Total_d_electrons'),
        ('Val_avg', 'EN_avg'),
        ('EN_B', 'EN_Bprime')
    ]

    for c1, c2 in interaction_pairs:
        if c1 in feat_df.columns and c2 in feat_df.columns:
            new_c = f"{c1}_x_{c2}"
            feat_df[new_c] = feat_df[c1] * feat_df[c2]
            feat_cols.append(new_c)

    ratio_pairs = [
        ('EN_B', 'EN_A'),
        ('EN_Bprime', 'EN_B'),
        ('Shannon_B', 'Shannon_A'),
        ('Shannon_Bprime', 'Shannon_B')
    ]

    for num, den in ratio_pairs:
        if num in feat_df.columns and den in feat_df.columns:
            new_c = f"({num}_/_({den}))"
            feat_df[new_c] = feat_df[num] / (feat_df[den].abs() + 1e-4)
            feat_cols.append(new_c)

    X_expanded = feat_df[feat_cols].values
    return X_expanded, feat_cols
