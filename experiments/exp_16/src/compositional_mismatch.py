"""
src/compositional_mismatch.py
==============================
100% Pure Compositional Mismatch & Multi-Operator Feature Engine for Exp 16.
GUARANTEE: Uses ZERO 3D atomic coordinates or GNN surrogates!
Derived strictly from chemical formulas, Pauling electronegativities, Shannon radii lookup, and formal charges.
"""

import numpy as np
import pandas as pd

def generate_mismatch_features(df: pd.DataFrame, base_feature_cols: list) -> tuple[np.ndarray, list]:
    """
    Constructs pure compositional mismatch features and multi-operator terms.
    """
    comp_df = df[base_feature_cols].copy()
    comp_cols = list(base_feature_cols)

    # 1. Pure Compositional Mismatch Metrics
    if 'EN_B' in df.columns and 'EN_Bprime' in df.columns:
        comp_df['Delta_EN_B'] = (df['EN_B'] - df['EN_Bprime']).abs()
        comp_cols.append('Delta_EN_B')

    if 'EN_B' in df.columns and 'EN_Bprime' in df.columns and 'EN_A' in df.columns and 'EN_Aprime' in df.columns:
        comp_df['Delta_EN_AB'] = (((df['EN_B'] + df['EN_Bprime'])/2.0) - ((df['EN_A'] + df['EN_Aprime'])/2.0)).abs()
        comp_cols.append('Delta_EN_AB')

    if 'Val_B' in df.columns and 'Val_Bprime' in df.columns:
        comp_df['Delta_Val_B'] = (df['Val_B'] - df['Val_Bprime']).abs()
        comp_cols.append('Delta_Val_B')

    if 'HS_moment_B' in df.columns and 'HS_moment_Bprime' in df.columns:
        comp_df['Delta_HS_B'] = (df['HS_moment_B'] - df['HS_moment_Bprime']).abs()
        comp_cols.append('Delta_HS_B')

    if 'Shannon_B' in df.columns and 'Shannon_Bprime' in df.columns:
        comp_df['Delta_Shannon_B'] = (df['Shannon_B'] - df['Shannon_Bprime']).abs()
        comp_cols.append('Delta_Shannon_B')

    if 'Group_B' in df.columns and 'Group_Bprime' in df.columns:
        comp_df['Delta_Group_B'] = (df['Group_B'] - df['Group_Bprime']).abs()
        comp_cols.append('Delta_Group_B')

    # Phillips Scale Pure Compositional Ionicity Index Proxy: f_i = (Delta_EN_AB)^2 / ((Delta_EN_AB)^2 + (d_BO_ideal)^-2)
    if 'Delta_EN_AB' in comp_df.columns and 'd_BO' in df.columns:
        den = (comp_df['Delta_EN_AB'] ** 2) + ((df['d_BO'].abs() + 1e-4) ** -2)
        comp_df['Phillips_Ionicity_Proxy'] = (comp_df['Delta_EN_AB'] ** 2) / (den + 1e-6)
        comp_cols.append('Phillips_Ionicity_Proxy')

    # 2. Sub-linear square root terms
    key_root_cols = ['Tolerance_Factor', 'EN_avg', 'Volume_A3', 'Density_g_cm3', 'Total_HS_FiM', 'Total_d_electrons', 'Delta_EN_AB', 'Delta_HS_B']
    for col in key_root_cols:
        if col in comp_df.columns:
            new_c = f"sqrt({col})"
            comp_df[new_c] = np.sqrt(np.abs(comp_df[col]))
            comp_cols.append(new_c)

    # 3. Logarithmic scale terms
    key_log_cols = ['Volume_A3', 'Density_g_cm3', 'Total_HS_FiM', 'Total_d_electrons', 'Spin_Proxy_Distance', 'Delta_EN_B', 'Delta_HS_B']
    for col in key_log_cols:
        if col in comp_df.columns:
            new_c = f"log({col}+1)"
            comp_df[new_c] = np.log(np.abs(comp_df[col]) + 1.0)
            comp_cols.append(new_c)

    # 4. Squared terms
    key_sq_cols = ['Tolerance_Factor', 'Octahedral_Mismatch', 'EN_avg', 'Total_HS_FiM', 'Volume_A3', 'Density_g_cm3', 'Delta_EN_AB', 'Delta_Val_B']
    for col in key_sq_cols:
        if col in comp_df.columns:
            new_c = f"({col})^2"
            comp_df[new_c] = comp_df[col] ** 2
            comp_cols.append(new_c)

    # 5. 2nd-order multiplication interactions
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
        ('Total_A_Charge', 'Val_avg'),
        ('Delta_EN_AB', 'Tolerance_Factor'),
        ('Delta_HS_B', 'Total_d_electrons'),
        ('Delta_Val_B', 'EN_avg')
    ]

    for c1, c2 in interaction_pairs:
        if c1 in comp_df.columns and c2 in comp_df.columns:
            new_c = f"{c1}_x_{c2}"
            comp_df[new_c] = comp_df[c1] * comp_df[c2]
            comp_cols.append(new_c)

    # 6. Physical ratio terms
    ratio_pairs = [
        ('EN_B', 'EN_A'),
        ('EN_Bprime', 'EN_B'),
        ('Shannon_B', 'Shannon_A'),
        ('Shannon_Bprime', 'Shannon_B'),
        ('d_BO', 'd_AO'),
        ('d_BprimeO', 'd_BO'),
        ('Group_B', 'Val_B'),
        ('d_electrons_B', 'Group_B')
    ]

    for num, den in ratio_pairs:
        if num in comp_df.columns and den in comp_df.columns:
            new_c = f"({num}_/_({den}))"
            comp_df[new_c] = comp_df[num] / (comp_df[den].abs() + 1e-4)
            comp_cols.append(new_c)

    # 7. 3rd-order physical triplet terms
    triplet_tuples = [
        ('Tolerance_Factor', 'Octahedral_Mismatch', 'EN_avg'),
        ('Val_avg', 'EN_avg', 'Volume_A3'),
        ('Total_HS_FiM', 'Total_d_electrons', 'Spin_Proxy_Distance'),
        ('EN_B', 'EN_Bprime', 'Volume_A3'),
        ('Tolerance_Factor', 'Density_g_cm3', 'Octahedral_Mismatch'),
        ('Delta_EN_AB', 'Tolerance_Factor', 'Volume_A3')
    ]

    for c1, c2, c3 in triplet_tuples:
        if c1 in comp_df.columns and c2 in comp_df.columns and c3 in comp_df.columns:
            new_c = f"{c1}_x_{c2}_x_{c3}"
            comp_df[new_c] = comp_df[c1] * comp_df[c2] * comp_df[c3]
            comp_cols.append(new_c)

    X_expanded = comp_df[comp_cols].values
    return X_expanded, comp_cols
