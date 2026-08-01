"""
src/generate_graphs.py
======================
Modular python script to generate all 7 exploratory data analysis (EDA) plots
and save them cleanly in exp_v2/research/data/analysis_1/graphs/.
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from sklearn.preprocessing import StandardScaler

def generate_all_eda_graphs(dataset_path: str, output_graphs_dir: str):
    """
    Reads the double perovskite dataset, performs EDA calculations,
    and generates 7 publication-quality plots.
    """
    os.makedirs(output_graphs_dir, exist_ok=True)
    
    # Set plot styling
    plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
    plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
    plt.rcParams['axes.edgecolor'] = '#cccccc'
    plt.rcParams['axes.linewidth'] = 1.0

    df = pd.read_csv(dataset_path)
    targets = ['Formation_Energy_eV_atom', 'Energy_Above_Hull_eV', 'Band_Gap_eV', 'Total_Magnetization_uB']

    # 33 pure physical/chemical candidate descriptors
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

    clean_df = df.dropna(subset=targets + feature_cols).copy()
    X = clean_df[feature_cols].values
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    print(f"[EDA Engine] Data shape for analysis: {clean_df.shape}")

    # ─── 1. TARGET DISTRIBUTIONS ───
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    target_titles = {
        'Formation_Energy_eV_atom': 'Formation Energy (eV/atom)',
        'Energy_Above_Hull_eV': 'Energy Above Hull (eV)',
        'Band_Gap_eV': 'Band Gap (eV)',
        'Total_Magnetization_uB': 'Total Magnetization (uB)'
    }
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']

    for i, (t, col) in enumerate(zip(targets, colors)):
        ax = axes[i // 2, i % 2]
        sns.histplot(clean_df[t], kde=True, ax=ax, color=col, bins=35, edgecolor='black', alpha=0.6)
        ax.set_title(f"Distribution of {target_titles[t]}", fontsize=13, fontweight='bold')
        ax.set_xlabel(target_titles[t], fontsize=11)
        ax.set_ylabel("Frequency", fontsize=11)
        
        if t != 'Formation_Energy_eV_atom':
            thr = 0.01 if 'Energy' in t or 'Gap' in t else 0.05
            zero_cnt = (clean_df[t] <= thr).sum()
            zero_pct = (zero_cnt / len(clean_df)) * 100.0
            ax.text(0.65, 0.82, f"Zero-Inflation: {zero_pct:.1f}%\n({zero_cnt} zeros)", 
                    transform=ax.transAxes, fontsize=10, bbox=dict(boxstyle="round,pad=0.3", fc="yellow", ec="black", lw=1, alpha=0.8))

    plt.tight_layout()
    p1 = os.path.join(output_graphs_dir, "target_distributions.png")
    plt.savefig(p1, dpi=300)
    plt.close()
    print(f"--> Saved {p1}")

    # ─── 2. CORRELATION MATRIX HEATMAP ───
    fig, ax = plt.subplots(figsize=(16, 12))
    corr = clean_df[feature_cols + targets].corr()
    sns.heatmap(corr, cmap='coolwarm', vmin=-1.0, vmax=1.0, ax=ax, annot=False, cbar_kws={'label': 'Pearson Correlation Coefficient'})
    ax.set_title("Full Descriptor & Target Pearson Correlation Matrix Heatmap", fontsize=15, fontweight='bold', pad=15)
    plt.tight_layout()
    p2 = os.path.join(output_graphs_dir, "correlation_matrix_heatmap.png")
    plt.savefig(p2, dpi=300)
    plt.close()
    print(f"--> Saved {p2}")

    # ─── 3. PCA SCREE PLOT ───
    pca = PCA()
    X_pca = pca.fit_transform(X_scaled)
    var_exp = pca.explained_variance_ratio_ * 100
    cum_var = np.cumsum(var_exp)

    fig, ax1 = plt.subplots(figsize=(10, 6))
    ax1.bar(range(1, len(var_exp) + 1), var_exp, color='#3498db', alpha=0.7, label='Individual Variance (%)')
    ax1.set_xlabel('Principal Component Number', fontsize=12)
    ax1.set_ylabel('Individual Variance Explained (%)', fontsize=12, color='#2980b9')
    ax1.tick_params(axis='y', labelcolor='#2980b9')

    ax2 = ax1.twinx()
    ax2.plot(range(1, len(cum_var) + 1), cum_var, color='#e74c3c', marker='o', linewidth=2, label='Cumulative Variance (%)')
    ax2.set_ylabel('Cumulative Variance Explained (%)', fontsize=12, color='#c0392b')
    ax2.tick_params(axis='y', labelcolor='#c0392b')
    ax2.axhline(y=90.0, color='gray', linestyle='--', label='90% Variance Cutoff')

    n_90 = np.argmax(cum_var >= 90.0) + 1
    ax1.set_title(f"PCA Scree Plot: {n_90} Components Explain >90% Variance", fontsize=14, fontweight='bold')
    plt.tight_layout()
    p3 = os.path.join(output_graphs_dir, "pca_scree_variance.png")
    plt.savefig(p3, dpi=300)
    plt.close()
    print(f"--> Saved {p3}")

    # ─── 4. PCA 2D SCATTER PROJECTION COLOR-CODED BY TARGETS ───
    fig, axes = plt.subplots(2, 2, figsize=(14, 11))
    for i, t in enumerate(targets):
        ax = axes[i // 2, i % 2]
        sc = ax.scatter(X_pca[:, 0], X_pca[:, 1], c=clean_df[t], cmap='viridis' if i%2==0 else 'magma', alpha=0.8, s=15)
        cbar = plt.colorbar(sc, ax=ax)
        cbar.set_label(target_titles[t], fontsize=10)
        ax.set_title(f"PC1 vs PC2: Colored by {target_titles[t]}", fontsize=12, fontweight='bold')
        ax.set_xlabel(f"PC1 ({var_exp[0]:.1f}% var)", fontsize=10)
        ax.set_ylabel(f"PC2 ({var_exp[1]:.1f}% var)", fontsize=10)

    plt.tight_layout()
    p4 = os.path.join(output_graphs_dir, "pca_2d_scatter_targets.png")
    plt.savefig(p4, dpi=300)
    plt.close()
    print(f"--> Saved {p4}")

    # ─── 5. TOP DESCRIPTOR CORRELATIONS BAR CHART ───
    fig, axes = plt.subplots(2, 2, figsize=(15, 11))
    for i, t in enumerate(targets):
        ax = axes[i // 2, i % 2]
        corrs = clean_df[feature_cols].corrwith(clean_df[t]).abs().sort_values(ascending=False).head(10)
        ax.barh(corrs.index[::-1], corrs.values[::-1], color='#2980b9', alpha=0.85)
        ax.set_title(f"Top 10 Physical Feature Correlations with {target_titles[t]}", fontsize=12, fontweight='bold')
        ax.set_xlabel("|Pearson Correlation Coefficient|", fontsize=11)
        ax.set_ylabel("Physical Descriptor", fontsize=11)
        for p in ax.patches:
            ax.annotate(f"{p.get_width():.3f}", (p.get_width() + 0.005, p.get_y() + p.get_height() / 2.),
                        ha='left', va='center', fontsize=9)

    plt.tight_layout()
    p5 = os.path.join(output_graphs_dir, "feature_target_top_correlations.png")
    plt.savefig(p5, dpi=300)
    plt.close()
    print(f"--> Saved {p5}")

    # ─── 6. t-SNE MANIFOLD CLUSTER PROJECTION ───
    tsne = TSNE(n_components=2, perplexity=30, random_state=42)
    X_tsne = tsne.fit_transform(X_scaled)

    fig, ax = plt.subplots(figsize=(10, 8))
    sc = ax.scatter(X_tsne[:, 0], X_tsne[:, 1], c=clean_df['Energy_Above_Hull_eV'], cmap='plasma', alpha=0.8, s=20)
    cbar = plt.colorbar(sc, ax=ax)
    cbar.set_label("Energy Above Hull (eV)", fontsize=11)
    ax.set_title("t-SNE 2D Manifold Projection Colored by Stability (Energy Above Hull)", fontsize=14, fontweight='bold')
    ax.set_xlabel("t-SNE Dimension 1", fontsize=11)
    ax.set_ylabel("t-SNE Dimension 2", fontsize=11)
    plt.tight_layout()
    p6 = os.path.join(output_graphs_dir, "tsne_cluster_projection.png")
    plt.savefig(p6, dpi=300)
    plt.close()
    print(f"--> Saved {p6}")

    # ─── 7. KEY PHYSICAL DESCRIPTORS PAIRPLOT / SCATTER MATRIX ───
    key_phys_feats = ['Tolerance_Factor', 'Octahedral_Mismatch', 'Total_HS_FiM', 'Density_g_cm3']
    fig, axes = plt.subplots(4, 4, figsize=(13, 13))

    for i, f1 in enumerate(key_phys_feats):
        for j, f2 in enumerate(key_phys_feats):
            ax = axes[i, j]
            if i == j:
                ax.hist(clean_df[f1].dropna(), bins=30, color='#2c3e50', edgecolor='black', alpha=0.7)
                ax.set_title(f"{f1}", fontsize=10, fontweight='bold')
            else:
                ax.scatter(clean_df[f2], clean_df[f1], c=clean_df['Formation_Energy_eV_atom'], cmap='viridis', alpha=0.5, s=8)
            
            if i == 3:
                ax.set_xlabel(f2, fontsize=9)
            if j == 0:
                ax.set_ylabel(f1, fontsize=9)

    plt.suptitle("Pairwise Relationships of Key Physical Descriptors Colored by Formation Energy", fontsize=14, fontweight='bold', y=0.99)
    plt.tight_layout()
    p7 = os.path.join(output_graphs_dir, "feature_pairplot_phys.png")
    plt.savefig(p7, dpi=200)
    plt.close()
    print(f"--> Saved {p7}")

    print("[SUCCESS] All 7 EDA plots generated cleanly by src/generate_graphs.py!")
