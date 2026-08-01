"""
src/tieline_hull_features.py
============================
Feature engine for Experiment 20:
1. Single-Perovskite Convex Hull Tie-Line Engine (Delta_t_sub_perov, Delta_H_sub_perov_mismatch, D_hull_proxy).
2. Exponential Convex Hull Distance Scaling Features.
3. Octahedral d0/d10 Closed-Shell Engine, Binary Oxidation Enthalpy, Harrison Gap, Strain.
"""

import numpy as np
import pandas as pd
from .tieline_hull_data import (
    BINARY_OXIDE_FORMATION_ENTHALPY_EV_ATOM,
    PETTIFOR_MENDELEEV,
    FIRST_IONIZATION_ENERGY_EV,
    ELECTRON_AFFINITY_EV,
    EA_OXYGEN
)

R_OXYGEN_SHANNON = 1.40  # Shannon Ionic Radius of O2- in Angstroms

def generate_exp20_features(df: pd.DataFrame, base_feature_cols: list) -> tuple[np.ndarray, list]:
    """
    Constructs Exp 20 features:
    - Single-Perovskite Tie-Line Engine & Exponential Hull Distance Scaling
    - Octahedral d0/d10 Closed-Shell Engine
    - Binary Oxide Formation Enthalpy Mismatch Engine
    - Harrison Quantum Gap & Birch-Murnaghan Strain Engine
    """
    feat_df = df[base_feature_cols].copy()
    feat_cols = list(base_feature_cols)

    # 1. Single-Perovskite Convex Hull Tie-Line Engine
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

        # Exponential Convex Hull Distance Scaling
        feat_df['Exp_D_hull_scale'] = np.exp(np.clip(feat_df['D_hull_proxy'] - 1.0, -5.0, 5.0))
        feat_cols.append('Exp_D_hull_scale')

    # 2. Octahedral d0 / d10 Closed-Shell Engine
    d_b = df['d_electrons_B'] if 'd_electrons_B' in df.columns else pd.Series(0, index=df.index)
    d_bp = df['d_electrons_Bprime'] if 'd_electrons_Bprime' in df.columns else pd.Series(0, index=df.index)

    feat_df['Is_d0_B'] = (d_b == 0).astype(float)
    feat_df['Is_d10_B'] = (d_b == 10).astype(float)
    feat_df['Is_d0_Bprime'] = (d_bp == 0).astype(float)
    feat_df['Is_d10_Bprime'] = (d_bp == 10).astype(float)

    is_cs_b = (d_b == 0) | (d_b == 10)
    is_cs_bp = (d_bp == 0) | (d_bp == 10)
    feat_df['Is_Closed_Shell_both'] = (is_cs_b & is_cs_bp).astype(float)
    feat_df['Open_Shell_d_fraction'] = (d_b + d_bp) / 20.0

    feat_cols.extend(['Is_d0_B', 'Is_d10_B', 'Is_d0_Bprime', 'Is_d10_Bprime', 'Is_Closed_Shell_both', 'Open_Shell_d_fraction'])

    # 3. Binary Oxide Formation Enthalpy Mismatch Engine
    if 'B_site' in df.columns and 'Bprime_site' in df.columns:
        h_ox_b = df['B_site'].map(BINARY_OXIDE_FORMATION_ENTHALPY_EV_ATOM).fillna(-2.0)
        h_ox_bp = df['Bprime_site'].map(BINARY_OXIDE_FORMATION_ENTHALPY_EV_ATOM).fillna(-2.0)

        feat_df['H_oxide_B_eV'] = h_ox_b
        feat_df['H_oxide_Bprime_eV'] = h_ox_bp
        feat_df['Delta_H_ox_mismatch'] = (h_ox_b - h_ox_bp).abs()
        feat_df['Delta_H_ox_avg'] = (h_ox_b + h_ox_bp) / 2.0
        feat_cols.extend(['H_oxide_B_eV', 'H_oxide_Bprime_eV', 'Delta_H_ox_mismatch', 'Delta_H_ox_avg'])

    # 4. HOMO-LUMO & Tight-Binding Proxies
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

    # 5. Mendeleev Number / Pettifor Scale (M)
    if 'B_site' in df.columns and 'Bprime_site' in df.columns:
        m_b = df['B_site'].map(PETTIFOR_MENDELEEV).fillna(30.0)
        m_bp = df['Bprime_site'].map(PETTIFOR_MENDELEEV).fillna(30.0)
        feat_df['Delta_Mendeleev_B'] = (m_b - m_bp).abs()
        feat_cols.append('Delta_Mendeleev_B')

    # 6. Valence Electron Concentration (VEC)
    val_a = df['Val_A'] if 'Val_A' in df.columns else 2.0
    val_ap = df['Val_Aprime'] if 'Val_Aprime' in df.columns else 2.0
    val_b = df['Val_B'] if 'Val_B' in df.columns else 3.0
    val_bp = df['Val_Bprime'] if 'Val_Bprime' in df.columns else 3.0

    feat_df['VEC'] = (val_a + val_ap + val_b + val_bp + 36.0) / 10.0
    feat_cols.append('VEC')

    # 7. Birch-Murnaghan Thermodynamic Strain Proxies
    if 'Tolerance_Factor' in df.columns:
        feat_df['E_tolerance_strain'] = (df['Tolerance_Factor'] - 1.0) ** 2
        feat_cols.append('E_tolerance_strain')

    if 'Octahedral_Mismatch' in df.columns and 'Density_g_cm3' in df.columns:
        feat_df['E_oct_distortion_strain'] = (df['Octahedral_Mismatch'] ** 2) * df['Density_g_cm3']
        feat_cols.append('E_oct_distortion_strain')

    # 8. Pure Compositional Mismatch Metrics
    if 'EN_B' in df.columns and 'EN_Bprime' in df.columns:
        feat_df['Delta_EN_B'] = (df['EN_B'] - df['EN_Bprime']).abs()
        feat_cols.append('Delta_EN_B')

    if 'EN_B' in df.columns and 'EN_Bprime' in df.columns and 'EN_A' in df.columns and 'EN_Aprime' in df.columns:
        feat_df['Delta_EN_AB'] = (((df['EN_B'] + df['EN_Bprime'])/2.0) - ((df['EN_A'] + df['EN_Aprime'])/2.0)).abs()
        feat_cols.append('Delta_EN_AB')

    if 'Val_B' in df.columns and 'Val_Bprime' in df.columns:
        feat_df['Delta_Val_B'] = (df['Val_B'] - df['Val_Bprime']).abs()
        feat_cols.append('Delta_Val_B')

    if 'HS_moment_B' in df.columns and 'HS_moment_Bprime' in df.columns:
        feat_df['Delta_HS_B'] = (df['HS_moment_B'] - df['HS_moment_Bprime']).abs()
        feat_cols.append('Delta_HS_B')

    if 'Shannon_B' in df.columns and 'Shannon_Bprime' in df.columns:
        feat_df['Delta_Shannon_B'] = (df['Shannon_B'] - df['Shannon_Bprime']).abs()
        feat_cols.append('Delta_Shannon_B')

    if 'Delta_EN_AB' in feat_df.columns and 'd_BO' in df.columns:
        den = (feat_df['Delta_EN_AB'] ** 2) + ((df['d_BO'].abs() + 1e-4) ** -2)
        feat_df['Phillips_Ionicity_Proxy'] = (feat_df['Delta_EN_AB'] ** 2) / (den + 1e-6)
        feat_cols.append('Phillips_Ionicity_Proxy')

    # 9. Multi-Operator Closed-Shell & Tie-Line Interactions
    if 'Delta_t_sub_perov' in feat_df.columns and 'Exp_D_hull_scale' in feat_df.columns:
        feat_df['SubPerov_x_ExpHull'] = feat_df['Delta_t_sub_perov'] * feat_df['Exp_D_hull_scale']
        feat_cols.append('SubPerov_x_ExpHull')

    # 10. Sub-linear square root terms
    key_root_cols = ['Tolerance_Factor', 'EN_avg', 'Volume_A3', 'Density_g_cm3', 'Total_HS_FiM', 'Total_d_electrons', 'Harrison_Quantum_Gap_eV', 'E_tolerance_strain', 'Delta_H_ox_mismatch', 'D_hull_proxy']
    for col in key_root_cols:
        if col in feat_df.columns:
            new_c = f"sqrt({col})"
            feat_df[new_c] = np.sqrt(np.abs(feat_df[col]))
            feat_cols.append(new_c)

    # 11. Logarithmic scale terms
    key_log_cols = ['Volume_A3', 'Density_g_cm3', 'Total_HS_FiM', 'Total_d_electrons', 'Spin_Proxy_Distance', 'Harrison_Quantum_Gap_eV', 'Delta_Mendeleev_B', 'Delta_H_ox_mismatch', 'D_hull_proxy']
    for col in key_log_cols:
        if col in feat_df.columns:
            new_c = f"log({col}+1)"
            feat_df[new_c] = np.log(np.abs(feat_df[col]) + 1.0)
            feat_cols.append(new_c)

    # 12. Squared terms
    key_sq_cols = ['Tolerance_Factor', 'Octahedral_Mismatch', 'EN_avg', 'Total_HS_FiM', 'Volume_A3', 'Density_g_cm3', 'Harrison_Quantum_Gap_eV', 'VEC', 'Delta_H_ox_mismatch', 'Delta_t_sub_perov', 'D_hull_proxy']
    for col in key_sq_cols:
        if col in feat_df.columns:
            new_c = f"({col})^2"
            feat_df[new_c] = feat_df[col] ** 2
            feat_cols.append(new_c)

    # 13. 2nd-order multiplication interactions
    interaction_pairs = [
        ('Tolerance_Factor', 'Octahedral_Mismatch'),
        ('EN_avg', 'Volume_A3'),
        ('EN_avg', 'Density_g_cm3'),
        ('Total_HS_FiM', 'Total_d_electrons'),
        ('Total_HS_FiM', 'Spin_Proxy_Distance'),
        ('Val_avg', 'EN_avg'),
        ('Group_B', 'Group_Bprime'),
        ('d_electrons_B', 'd_electrons_Bprime'),
        ('Shannon_B', 'Shannon_Bprime'),
        ('EN_B', 'EN_Bprime'),
        ('d_BO', 'd_BprimeO'),
        ('Tolerance_Factor', 'EN_avg'),
        ('Harrison_Quantum_Gap_eV', 'Phillips_Ionicity_Proxy'),
        ('Delta_Mendeleev_B', 'E_tolerance_strain'),
        ('VEC', 'Total_HS_FiM'),
        ('Delta_H_ox_mismatch', 'E_tolerance_strain'),
        ('Delta_t_sub_perov', 'Delta_H_sub_perov_mismatch')
    ]

    for c1, c2 in interaction_pairs:
        if c1 in feat_df.columns and c2 in feat_df.columns:
            new_c = f"{c1}_x_{c2}"
            feat_df[new_c] = feat_df[c1] * feat_df[c2]
            feat_cols.append(new_c)

    # 14. Physical ratio terms
    ratio_pairs = [
        ('EN_B', 'EN_A'),
        ('EN_Bprime', 'EN_B'),
        ('Shannon_B', 'Shannon_A'),
        ('Shannon_Bprime', 'Shannon_B'),
        ('d_BO', 'd_AO'),
        ('d_BprimeO', 'd_BO'),
        ('Group_B', 'Val_B'),
        ('d_electrons_B', 'Group_B'),
        ('Harrison_Quantum_Gap_eV', 'EN_avg'),
        ('Delta_H_ox_mismatch', 'EN_avg'),
        ('Delta_t_sub_perov', 'Tolerance_Factor')
    ]

    for num, den in ratio_pairs:
        if num in feat_df.columns and den in feat_df.columns:
            new_c = f"({num}_/_({den}))"
            feat_df[new_c] = feat_df[num] / (feat_df[den].abs() + 1e-4)
            feat_cols.append(new_c)

    # 15. 3rd-order physical triplet terms
    triplet_tuples = [
        ('Tolerance_Factor', 'Octahedral_Mismatch', 'EN_avg'),
        ('Val_avg', 'EN_avg', 'Volume_A3'),
        ('Total_HS_FiM', 'Total_d_electrons', 'Spin_Proxy_Distance'),
        ('EN_B', 'EN_Bprime', 'Volume_A3'),
        ('Tolerance_Factor', 'Density_g_cm3', 'Octahedral_Mismatch'),
        ('Harrison_Quantum_Gap_eV', 'Delta_EN_AB', 'Tolerance_Factor'),
        ('Delta_Mendeleev_B', 'E_tolerance_strain', 'VEC'),
        ('Delta_H_ox_mismatch', 'E_tolerance_strain', 'Density_g_cm3'),
        ('Delta_t_sub_perov', 'Delta_H_sub_perov_mismatch', 'Exp_D_hull_scale')
    ]

    for c1, c2, c3 in triplet_tuples:
        if c1 in feat_df.columns and c2 in feat_df.columns and c3 in feat_df.columns:
            new_c = f"{c1}_x_{c2}_x_{c3}"
            feat_df[new_c] = feat_df[c1] * feat_df[c2] * feat_df[c3]
            feat_cols.append(new_c)

    X_expanded = feat_df[feat_cols].values
    return X_expanded, feat_cols
