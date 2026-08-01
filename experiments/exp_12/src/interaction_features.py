"""
src/interaction_features.py
============================
Module to generate 2nd-order physical interaction features, polynomial terms,
and dimensionless ratios between key physical descriptors.
"""

import numpy as np
import pandas as pd

def generate_physical_interactions(df: pd.DataFrame, base_feature_cols: list) -> tuple[np.ndarray, list]:
    """
    Expands the base physical descriptor set with:
    1. Base features (33 features)
    2. Squared terms (x_i^2)
    3. Pairwise multiplication interactions (x_i * x_j) for key physical pairs
    4. Physical ratio terms (x_i / (x_j + eps))
    """
    X_base = df[base_feature_cols].copy()
    
    expanded_df = X_base.copy()
    expanded_cols = list(base_feature_cols)

    # 1. Add squared terms for key non-linear descriptors
    key_sq_cols = ['Tolerance_Factor', 'Octahedral_Mismatch', 'EN_avg', 'Total_HS_FiM', 'Volume_A3', 'Density_g_cm3']
    for col in key_sq_cols:
        if col in df.columns:
            new_c = f"({col})^2"
            expanded_df[new_c] = df[col] ** 2
            expanded_cols.append(new_c)

    # 2. Add domain-specific physical multiplication interactions
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

    # 3. Add physical scale-invariant ratio terms
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

    X_expanded = expanded_df[expanded_cols].values
    return X_expanded, expanded_cols
