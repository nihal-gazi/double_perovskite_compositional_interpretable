"""
src/expanded_features.py
=========================
Engine for multi-operator physical feature expansion:
Includes square roots, logarithms, squares, 2nd-order interactions, ratios, and 3rd-order physical triplets.
"""

import numpy as np
import pandas as pd

def generate_multi_operator_features(df: pd.DataFrame, base_feature_cols: list) -> tuple[np.ndarray, list]:
    """
    Generates a 100% interpretable multi-operator feature matrix:
    - Base features (33)
    - Sub-linear sqrt terms (sqrt(|x_i|))
    - Logarithmic terms (log(|x_i| + 1.0))
    - Squared terms (x_i^2)
    - 2nd-order multiplication terms (x_i * x_j)
    - Scale-invariant ratios (x_i / (x_j + eps))
    - 3rd-order physical triplets (x_i * x_j * x_k)
    """
    expanded_df = df[base_feature_cols].copy()
    expanded_cols = list(base_feature_cols)

    # 1. Sub-linear square root terms for positive physical magnitudes
    key_root_cols = ['Tolerance_Factor', 'EN_avg', 'Volume_A3', 'Density_g_cm3', 'Total_HS_FiM', 'Total_d_electrons']
    for col in key_root_cols:
        if col in df.columns:
            new_c = f"sqrt({col})"
            expanded_df[new_c] = np.sqrt(np.abs(df[col]))
            expanded_cols.append(new_c)

    # 2. Logarithmic scale terms
    key_log_cols = ['Volume_A3', 'Density_g_cm3', 'Total_HS_FiM', 'Total_d_electrons', 'Spin_Proxy_Distance']
    for col in key_log_cols:
        if col in df.columns:
            new_c = f"log({col}+1)"
            expanded_df[new_c] = np.log(np.abs(df[col]) + 1.0)
            expanded_cols.append(new_c)

    # 3. Squared terms
    key_sq_cols = ['Tolerance_Factor', 'Octahedral_Mismatch', 'EN_avg', 'Total_HS_FiM', 'Volume_A3', 'Density_g_cm3']
    for col in key_sq_cols:
        if col in df.columns:
            new_c = f"({col})^2"
            expanded_df[new_c] = df[col] ** 2
            expanded_cols.append(new_c)

    # 4. 2nd-order multiplication interactions
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
        ('Total_A_Charge', 'Val_avg')
    ]

    for c1, c2 in interaction_pairs:
        if c1 in df.columns and c2 in df.columns:
            new_c = f"{c1}_x_{c2}"
            expanded_df[new_c] = df[c1] * df[c2]
            expanded_cols.append(new_c)

    # 5. Physical ratio terms
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
        if num in df.columns and den in df.columns:
            new_c = f"({num}_/_({den}))"
            expanded_df[new_c] = df[num] / (df[den].abs() + 1e-4)
            expanded_cols.append(new_c)

    # 6. 3rd-order physical triplet terms
    triplet_tuples = [
        ('Tolerance_Factor', 'Octahedral_Mismatch', 'EN_avg'),
        ('Val_avg', 'EN_avg', 'Volume_A3'),
        ('Total_HS_FiM', 'Total_d_electrons', 'Spin_Proxy_Distance'),
        ('EN_B', 'EN_Bprime', 'Volume_A3'),
        ('Tolerance_Factor', 'Density_g_cm3', 'Octahedral_Mismatch')
    ]

    for c1, c2, c3 in triplet_tuples:
        if c1 in df.columns and c2 in df.columns and c3 in df.columns:
            new_c = f"{c1}_x_{c2}_x_{c3}"
            expanded_df[new_c] = df[c1] * df[c2] * df[c3]
            expanded_cols.append(new_c)

    X_expanded = expanded_df[expanded_cols].values
    return X_expanded, expanded_cols
