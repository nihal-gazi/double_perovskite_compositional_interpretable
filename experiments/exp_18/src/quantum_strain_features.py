"""
src/quantum_strain_features.py
==============================
Feature engine for Experiment 18:
1. Harrison's Solid State Tight-Binding Quantum Gap Proxy E_gap_QM.
2. Birch-Murnaghan Thermodynamic Elastic Strain Engine (Tolerance strain, Octahedral strain, Packing strain).
3. Sub-linear Radical & Fractional Power Laws ((x_i * x_j)^(1/3), (x_i * x_j)^(2/3)).
4. 100% Pure Compositional & 0D Quantum Features.
"""

import numpy as np
import pandas as pd
from .mendeleev_tightbinding_features_data import PETTIFOR_MENDELEEV, FIRST_IONIZATION_ENERGY_EV, ELECTRON_AFFINITY_EV, EA_OXYGEN

R_OXYGEN_SHANNON = 1.40  # Shannon Ionic Radius of O2- in Angstroms

def generate_exp18_features(df: pd.DataFrame, base_feature_cols: list) -> tuple[np.ndarray, list]:
    """
    Constructs Exp 18 features:
    - Harrison Quantum Gap E_gap_QM
    - Birch-Murnaghan Strain Engine
    - Fractional power laws
    - Mendeleev, IE, EA, VEC, Mismatches
    """
    feat_df = df[base_feature_cols].copy()
    feat_cols = list(base_feature_cols)

    # 1. HOMO-LUMO & Tight-Binding Proxies
    if 'B_site' in df.columns and 'Bprime_site' in df.columns:
        ie_b = df['B_site'].map(FIRST_IONIZATION_ENERGY_EV).fillna(7.5)
        ie_bp = df['Bprime_site'].map(FIRST_IONIZATION_ENERGY_EV).fillna(7.5)
        ea_b = df['B_site'].map(ELECTRON_AFFINITY_EV).fillna(0.5)
        ea_bp = df['Bprime_site'].map(ELECTRON_AFFINITY_EV).fillna(0.5)

        feat_df['IE_B_eV'] = ie_b
        feat_df['IE_Bprime_eV'] = ie_bp
        feat_cols.extend(['IE_B_eV', 'IE_Bprime_eV'])

        # Tight-Binding Gap Proxy: Delta E_gap = min(IE_B, IE_B') - EA_O
        min_ie_b = np.minimum(ie_b, ie_bp)
        delta_e_gap = min_ie_b - EA_OXYGEN
        feat_df['Tight_Binding_Gap_Proxy_eV'] = delta_e_gap
        feat_cols.append('Tight_Binding_Gap_Proxy_eV')

        # Harrison Tight-Binding Quantum Gap Proxy: E_gap_QM = sqrt((Delta E_gap)^2 + (r_B + r_O)^-4)
        if 'Shannon_B' in df.columns and 'Shannon_Bprime' in df.columns:
            r_b_avg = (df['Shannon_B'] + df['Shannon_Bprime']) / 2.0
            v_transfer_sq = ((r_b_avg + R_OXYGEN_SHANNON).abs() + 1e-4) ** -4
            feat_df['Harrison_Quantum_Gap_eV'] = np.sqrt(np.maximum(0.0, delta_e_gap**2) + v_transfer_sq)
            feat_cols.append('Harrison_Quantum_Gap_eV')

    # 2. Mendeleev Number / Pettifor Scale (M)
    if 'B_site' in df.columns and 'Bprime_site' in df.columns:
        m_b = df['B_site'].map(PETTIFOR_MENDELEEV).fillna(30.0)
        m_bp = df['Bprime_site'].map(PETTIFOR_MENDELEEV).fillna(30.0)
        feat_df['Delta_Mendeleev_B'] = (m_b - m_bp).abs()
        feat_cols.append('Delta_Mendeleev_B')

    # 3. Valence Electron Concentration (VEC)
    val_a = df['Val_A'] if 'Val_A' in df.columns else 2.0
    val_ap = df['Val_Aprime'] if 'Val_Aprime' in df.columns else 2.0
    val_b = df['Val_B'] if 'Val_B' in df.columns else 3.0
    val_bp = df['Val_Bprime'] if 'Val_Bprime' in df.columns else 3.0

    feat_df['VEC'] = (val_a + val_ap + val_b + val_bp + 36.0) / 10.0
    feat_cols.append('VEC')

    # 4. Birch-Murnaghan Thermodynamic Strain Proxies
    if 'Tolerance_Factor' in df.columns:
        feat_df['E_tolerance_strain'] = (df['Tolerance_Factor'] - 1.0) ** 2
        feat_cols.append('E_tolerance_strain')

    if 'Octahedral_Mismatch' in df.columns and 'Density_g_cm3' in df.columns:
        feat_df['E_oct_distortion_strain'] = (df['Octahedral_Mismatch'] ** 2) * df['Density_g_cm3']
        feat_cols.append('E_oct_distortion_strain')

    if 'Shannon_A' in df.columns and 'Shannon_B' in df.columns and 'Volume_A3' in df.columns:
        r_a = df['Shannon_A']
        r_ap = df['Shannon_Aprime'] if 'Shannon_Aprime' in df.columns else r_a
        r_b = df['Shannon_B']
        r_bp = df['Shannon_Bprime'] if 'Shannon_Bprime' in df.columns else r_b
        
        v_ideal_spheres = (4.0 / 3.0) * np.pi * (2.0*(r_a**3) + r_b**3 + r_bp**3 + 6.0*(R_OXYGEN_SHANNON**3))
        feat_df['Delta_V_packing_strain'] = ((df['Volume_A3'] - v_ideal_spheres) / (v_ideal_spheres + 1e-4)) ** 2
        feat_cols.append('Delta_V_packing_strain')

    # 5. Pure Compositional Mismatch Metrics
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

    # 6. Fractional Power Laws (x_i * x_j)^(1/3)
    fractional_pairs = [
        ('Harrison_Quantum_Gap_eV', 'Phillips_Ionicity_Proxy'),
        ('E_tolerance_strain', 'Delta_Mendeleev_B'),
        ('VEC', 'Total_HS_FiM')
    ]

    for c1, c2 in fractional_pairs:
        if c1 in feat_df.columns and c2 in feat_df.columns:
            new_c = f"({c1}_x_{c2})^(1/3)"
            feat_df[new_c] = np.cbrt(np.abs(feat_df[c1] * feat_df[c2]))
            feat_cols.append(new_c)

    # 7. Sub-linear square root terms
    key_root_cols = ['Tolerance_Factor', 'EN_avg', 'Volume_A3', 'Density_g_cm3', 'Total_HS_FiM', 'Total_d_electrons', 'Harrison_Quantum_Gap_eV', 'E_tolerance_strain']
    for col in key_root_cols:
        if col in feat_df.columns:
            new_c = f"sqrt({col})"
            feat_df[new_c] = np.sqrt(np.abs(feat_df[col]))
            feat_cols.append(new_c)

    # 8. Logarithmic scale terms
    key_log_cols = ['Volume_A3', 'Density_g_cm3', 'Total_HS_FiM', 'Total_d_electrons', 'Spin_Proxy_Distance', 'Harrison_Quantum_Gap_eV', 'Delta_Mendeleev_B']
    for col in key_log_cols:
        if col in feat_df.columns:
            new_c = f"log({col}+1)"
            feat_df[new_c] = np.log(np.abs(feat_df[col]) + 1.0)
            feat_cols.append(new_c)

    # 9. Squared terms
    key_sq_cols = ['Tolerance_Factor', 'Octahedral_Mismatch', 'EN_avg', 'Total_HS_FiM', 'Volume_A3', 'Density_g_cm3', 'Harrison_Quantum_Gap_eV', 'VEC']
    for col in key_sq_cols:
        if col in feat_df.columns:
            new_c = f"({col})^2"
            feat_df[new_c] = feat_df[col] ** 2
            feat_cols.append(new_c)

    # 10. 2nd-order multiplication interactions
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
        ('VEC', 'Total_HS_FiM')
    ]

    for c1, c2 in interaction_pairs:
        if c1 in feat_df.columns and c2 in feat_df.columns:
            new_c = f"{c1}_x_{c2}"
            feat_df[new_c] = feat_df[c1] * feat_df[c2]
            feat_cols.append(new_c)

    # 11. Physical ratio terms
    ratio_pairs = [
        ('EN_B', 'EN_A'),
        ('EN_Bprime', 'EN_B'),
        ('Shannon_B', 'Shannon_A'),
        ('Shannon_Bprime', 'Shannon_B'),
        ('d_BO', 'd_AO'),
        ('d_BprimeO', 'd_BO'),
        ('Group_B', 'Val_B'),
        ('d_electrons_B', 'Group_B'),
        ('Harrison_Quantum_Gap_eV', 'EN_avg')
    ]

    for num, den in ratio_pairs:
        if num in feat_df.columns and den in feat_df.columns:
            new_c = f"({num}_/_({den}))"
            feat_df[new_c] = feat_df[num] / (feat_df[den].abs() + 1e-4)
            feat_cols.append(new_c)

    # 12. 3rd-order physical triplet terms
    triplet_tuples = [
        ('Tolerance_Factor', 'Octahedral_Mismatch', 'EN_avg'),
        ('Val_avg', 'EN_avg', 'Volume_A3'),
        ('Total_HS_FiM', 'Total_d_electrons', 'Spin_Proxy_Distance'),
        ('EN_B', 'EN_Bprime', 'Volume_A3'),
        ('Tolerance_Factor', 'Density_g_cm3', 'Octahedral_Mismatch'),
        ('Harrison_Quantum_Gap_eV', 'Delta_EN_AB', 'Tolerance_Factor'),
        ('Delta_Mendeleev_B', 'E_tolerance_strain', 'VEC')
    ]

    for c1, c2, c3 in triplet_tuples:
        if c1 in feat_df.columns and c2 in feat_df.columns and c3 in feat_df.columns:
            new_c = f"{c1}_x_{c2}_x_{c3}"
            feat_df[new_c] = feat_df[c1] * feat_df[c2] * feat_df[c3]
            feat_cols.append(new_c)

    X_expanded = feat_df[feat_cols].values
    return X_expanded, feat_cols
