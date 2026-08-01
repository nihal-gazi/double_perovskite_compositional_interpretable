"""
src/mendeleev_tightbinding_features.py
======================================
Feature engine for Experiment 17:
1. HOMO-LUMO Energy Proxies: First Ionization Energy (IE), Electron Affinity (EA), Tight-Binding Gap Proxy Delta E_gap.
2. Mendeleev Number / Pettifor Scale (M) & Mendeleev Mismatch Delta M_B.
3. Valence Electron Concentration (VEC).
4. Pure Compositional Mismatches & Multi-Operator Expansions.
"""

import numpy as np
import pandas as pd

# Pettifor / Mendeleev Number Lookup Table (Continuous 1D Scale 1..103)
PETTIFOR_MENDELEEV = {
    'H': 1, 'Cs': 2, 'Rb': 3, 'K': 4, 'Na': 5, 'Li': 6, 'Fr': 2,
    'Ba': 7, 'Sr': 8, 'Ca': 9, 'Mg': 10, 'Be': 11, 'Ra': 7,
    'La': 12, 'Ce': 13, 'Pr': 14, 'Nd': 15, 'Pm': 16, 'Sm': 17, 'Eu': 18, 'Gd': 19, 'Tb': 20, 'Dy': 21, 'Ho': 22, 'Er': 23, 'Tm': 24, 'Yb': 25, 'Lu': 26,
    'Ac': 12, 'Th': 13, 'Pa': 14, 'U': 15, 'Np': 16, 'Pu': 17,
    'Y': 17, 'Sc': 18, 'Zr': 20, 'Hf': 21, 'Ti': 22, 'Ta': 25, 'Nb': 24, 'V': 26,
    'Mo': 28, 'W': 29, 'Cr': 30, 'Tc': 33, 'Re': 34, 'Mn': 35,
    'Fe': 38, 'Ru': 39, 'Os': 40, 'Co': 44, 'Rh': 45, 'Ir': 46,
    'Ni': 50, 'Pd': 51, 'Pt': 52, 'Cu': 55, 'Ag': 56, 'Au': 57,
    'Zn': 60, 'Cd': 61, 'Hg': 62, 'Al': 74, 'Ga': 75, 'In': 76, 'Tl': 77,
    'Si': 80, 'Ge': 81, 'Sn': 82, 'Pb': 83, 'P': 86, 'As': 87, 'Sb': 88, 'Bi': 89,
    'S': 94, 'Se': 95, 'Te': 96, 'F': 100, 'Cl': 101, 'Br': 102, 'I': 103, 'O': 93, 'N': 85, 'C': 79, 'B': 73
}

# First Ionization Energy (IE, in eV) Lookup Table
FIRST_IONIZATION_ENERGY_EV = {
    'H': 13.598, 'Li': 5.392, 'Na': 5.139, 'K': 4.341, 'Rb': 4.177, 'Cs': 3.894,
    'Be': 9.323, 'Mg': 7.646, 'Ca': 6.113, 'Sr': 5.695, 'Ba': 5.212,
    'Sc': 6.561, 'Y': 6.217, 'La': 5.577, 'Ti': 6.828, 'Zr': 6.634, 'Hf': 6.825,
    'V': 6.746, 'Nb': 6.759, 'Ta': 7.550, 'Cr': 6.767, 'Mo': 7.092, 'W': 7.864,
    'Mn': 7.434, 'Tc': 7.280, 'Re': 7.834, 'Fe': 7.902, 'Ru': 7.361, 'Os': 8.438,
    'Co': 7.881, 'Rh': 7.459, 'Ir': 8.967, 'Ni': 7.639, 'Pd': 8.337, 'Pt': 8.958,
    'Cu': 7.726, 'Ag': 7.576, 'Au': 9.226, 'Zn': 9.394, 'Cd': 8.994, 'Hg': 10.438,
    'Al': 5.986, 'Ga': 5.999, 'In': 5.786, 'Tl': 6.108, 'Si': 8.152, 'Ge': 7.900,
    'Sn': 7.344, 'Pb': 7.417, 'Bi': 7.289, 'O': 13.618
}

# Electron Affinity (EA, in eV) Lookup Table
ELECTRON_AFFINITY_EV = {
    'H': 0.754, 'Li': 0.618, 'Na': 0.548, 'K': 0.501, 'Rb': 0.486, 'Cs': 0.472,
    'Be': 0.0, 'Mg': 0.0, 'Ca': 0.025, 'Sr': 0.052, 'Ba': 0.145,
    'Sc': 0.188, 'Y': 0.307, 'La': 0.470, 'Ti': 0.079, 'Zr': 0.426, 'Hf': 0.178,
    'V': 0.525, 'Nb': 0.893, 'Ta': 0.322, 'Cr': 0.666, 'Mo': 0.746, 'W': 0.816,
    'Mn': 0.0, 'Tc': 0.550, 'Re': 0.150, 'Fe': 0.151, 'Ru': 1.050, 'Os': 1.100,
    'Co': 0.661, 'Rh': 1.137, 'Ir': 1.565, 'Ni': 1.156, 'Pd': 0.557, 'Pt': 2.128,
    'Cu': 1.228, 'Ag': 1.302, 'Au': 2.309, 'Zn': 0.0, 'Cd': 0.0, 'Hg': 0.0,
    'Al': 0.441, 'Ga': 0.430, 'In': 0.300, 'Tl': 0.377, 'Si': 1.385, 'Ge': 1.233,
    'Sn': 1.112, 'Pb': 1.056, 'Bi': 0.942, 'O': 1.461
}

EA_OXYGEN = 1.461  # Electron Affinity of Oxygen in eV

def generate_exp17_features(df: pd.DataFrame, base_feature_cols: list) -> tuple[np.ndarray, list]:
    """
    Constructs Exp 17 features:
    1. HOMO-LUMO Energy Proxies: IE_B, IE_Bprime, EA_B, EA_Bprime, Delta E_gap = min(IE_B, IE_B') - EA_O.
    2. Mendeleev Number & Mismatch: Mendeleev_B, Mendeleev_Bprime, Delta_Mendeleev_B = |M_B - M_B'|.
    3. Valence Electron Concentration (VEC).
    4. Pure compositional mismatches & multi-operator terms.
    """
    feat_df = df[base_feature_cols].copy()
    feat_cols = list(base_feature_cols)

    # 1. HOMO-LUMO Energy Proxies (in eV)
    if 'B_site' in df.columns and 'Bprime_site' in df.columns:
        ie_b = df['B_site'].map(FIRST_IONIZATION_ENERGY_EV).fillna(7.5)
        ie_bp = df['Bprime_site'].map(FIRST_IONIZATION_ENERGY_EV).fillna(7.5)
        ea_b = df['B_site'].map(ELECTRON_AFFINITY_EV).fillna(0.5)
        ea_bp = df['Bprime_site'].map(ELECTRON_AFFINITY_EV).fillna(0.5)

        feat_df['IE_B_eV'] = ie_b
        feat_df['IE_Bprime_eV'] = ie_bp
        feat_df['EA_B_eV'] = ea_b
        feat_df['EA_Bprime_eV'] = ea_bp
        feat_cols.extend(['IE_B_eV', 'IE_Bprime_eV', 'EA_B_eV', 'EA_Bprime_eV'])

        # Tight-Binding Gap Proxy: Delta E_gap = min(IE_B, IE_B') - EA_Oxygen
        min_ie_b = np.minimum(ie_b, ie_bp)
        feat_df['Tight_Binding_Gap_Proxy_eV'] = min_ie_b - EA_OXYGEN
        feat_cols.append('Tight_Binding_Gap_Proxy_eV')

        feat_df['IE_avg_eV'] = (ie_b + ie_bp) / 2.0
        feat_df['Delta_IE_B_eV'] = (ie_b - ie_bp).abs()
        feat_cols.extend(['IE_avg_eV', 'Delta_IE_B_eV'])

    # 2. Mendeleev Number / Pettifor Scale (M)
    if 'B_site' in df.columns and 'Bprime_site' in df.columns:
        m_b = df['B_site'].map(PETTIFOR_MENDELEEV).fillna(30.0)
        m_bp = df['Bprime_site'].map(PETTIFOR_MENDELEEV).fillna(30.0)
        feat_df['Mendeleev_B'] = m_b
        feat_df['Mendeleev_Bprime'] = m_bp
        feat_df['Delta_Mendeleev_B'] = (m_b - m_bp).abs()
        feat_cols.extend(['Mendeleev_B', 'Mendeleev_Bprime', 'Delta_Mendeleev_B'])

    # 3. Valence Electron Concentration (VEC)
    # VEC = sum(Valence Electrons of all 10 atoms) / 10
    val_a = df['Val_A'] if 'Val_A' in df.columns else 2.0
    val_ap = df['Val_Aprime'] if 'Val_Aprime' in df.columns else 2.0
    val_b = df['Val_B'] if 'Val_B' in df.columns else 3.0
    val_bp = df['Val_Bprime'] if 'Val_Bprime' in df.columns else 3.0

    feat_df['VEC'] = (val_a + val_ap + val_b + val_bp + 6.0 * 6.0) / 10.0
    feat_cols.append('VEC')

    # 4. Pure Compositional Mismatch Metrics
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

    if 'Group_B' in df.columns and 'Group_Bprime' in df.columns:
        feat_df['Delta_Group_B'] = (df['Group_B'] - df['Group_Bprime']).abs()
        feat_cols.append('Delta_Group_B')

    if 'Delta_EN_AB' in feat_df.columns and 'd_BO' in df.columns:
        den = (feat_df['Delta_EN_AB'] ** 2) + ((df['d_BO'].abs() + 1e-4) ** -2)
        feat_df['Phillips_Ionicity_Proxy'] = (feat_df['Delta_EN_AB'] ** 2) / (den + 1e-6)
        feat_cols.append('Phillips_Ionicity_Proxy')

    # 5. Sub-linear square root terms
    key_root_cols = ['Tolerance_Factor', 'EN_avg', 'Volume_A3', 'Density_g_cm3', 'Total_HS_FiM', 'Total_d_electrons', 'Delta_EN_AB', 'Tight_Binding_Gap_Proxy_eV', 'VEC']
    for col in key_root_cols:
        if col in feat_df.columns:
            new_c = f"sqrt({col})"
            feat_df[new_c] = np.sqrt(np.abs(feat_df[col]))
            feat_cols.append(new_c)

    # 6. Logarithmic scale terms
    key_log_cols = ['Volume_A3', 'Density_g_cm3', 'Total_HS_FiM', 'Total_d_electrons', 'Spin_Proxy_Distance', 'Delta_EN_B', 'Tight_Binding_Gap_Proxy_eV', 'Delta_Mendeleev_B']
    for col in key_log_cols:
        if col in feat_df.columns:
            new_c = f"log({col}+1)"
            feat_df[new_c] = np.log(np.abs(feat_df[col]) + 1.0)
            feat_cols.append(new_c)

    # 7. Squared terms
    key_sq_cols = ['Tolerance_Factor', 'Octahedral_Mismatch', 'EN_avg', 'Total_HS_FiM', 'Volume_A3', 'Density_g_cm3', 'Tight_Binding_Gap_Proxy_eV', 'Delta_Mendeleev_B', 'VEC']
    for col in key_sq_cols:
        if col in feat_df.columns:
            new_c = f"({col})^2"
            feat_df[new_c] = feat_df[col] ** 2
            feat_cols.append(new_c)

    # 8. 2nd-order multiplication interactions
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
        ('Tolerance_Factor', 'Volume_A3'),
        ('Octahedral_Mismatch', 'Density_g_cm3'),
        ('Tight_Binding_Gap_Proxy_eV', 'Phillips_Ionicity_Proxy'),
        ('Delta_Mendeleev_B', 'Tolerance_Factor'),
        ('VEC', 'Total_HS_FiM')
    ]

    for c1, c2 in interaction_pairs:
        if c1 in feat_df.columns and c2 in feat_df.columns:
            new_c = f"{c1}_x_{c2}"
            feat_df[new_c] = feat_df[c1] * feat_df[c2]
            feat_cols.append(new_c)

    # 9. Physical ratio terms
    ratio_pairs = [
        ('EN_B', 'EN_A'),
        ('EN_Bprime', 'EN_B'),
        ('Shannon_B', 'Shannon_A'),
        ('Shannon_Bprime', 'Shannon_B'),
        ('d_BO', 'd_AO'),
        ('d_BprimeO', 'd_BO'),
        ('Group_B', 'Val_B'),
        ('d_electrons_B', 'Group_B'),
        ('Tight_Binding_Gap_Proxy_eV', 'EN_avg')
    ]

    for num, den in ratio_pairs:
        if num in feat_df.columns and den in feat_df.columns:
            new_c = f"({num}_/_({den}))"
            feat_df[new_c] = feat_df[num] / (feat_df[den].abs() + 1e-4)
            feat_cols.append(new_c)

    # 10. 3rd-order physical triplet terms
    triplet_tuples = [
        ('Tolerance_Factor', 'Octahedral_Mismatch', 'EN_avg'),
        ('Val_avg', 'EN_avg', 'Volume_A3'),
        ('Total_HS_FiM', 'Total_d_electrons', 'Spin_Proxy_Distance'),
        ('EN_B', 'EN_Bprime', 'Volume_A3'),
        ('Tolerance_Factor', 'Density_g_cm3', 'Octahedral_Mismatch'),
        ('Tight_Binding_Gap_Proxy_eV', 'Delta_EN_AB', 'Tolerance_Factor'),
        ('Delta_Mendeleev_B', 'VEC', 'Tolerance_Factor')
    ]

    for c1, c2, c3 in triplet_tuples:
        if c1 in feat_df.columns and c2 in feat_df.columns and c3 in feat_df.columns:
            new_c = f"{c1}_x_{c2}_x_{c3}"
            feat_df[new_c] = feat_df[c1] * feat_df[c2] * feat_df[c3]
            feat_cols.append(new_c)

    X_expanded = feat_df[feat_cols].values
    return X_expanded, feat_cols
