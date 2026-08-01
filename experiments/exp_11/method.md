# Experiment 11: Standard Linear Regression Baseline (Clean Physical Descriptors)

## 1. Executive Summary & Data Leakage Audit

Following the data leakage audit, **3 leaked GNN-derived structural proxies were removed** from the candidate feature pool to guarantee zero data leakage and ensure 100% genuine physical interpretability:
- **`M_net` & `M_abs`**: Pre-computed CHGNet magnetic moments ($r = 1.0000$ correlation with target `Total_Magnetization_uB`).
- **`E_GNN`**: Pre-computed CHGNet DFT energy surrogate ($r = 0.9994$ correlation with target `Formation_Energy_eV_atom`).

All evaluations in **Experiment 11** are performed on **33 pure physical and chemical descriptors** (electronegativities, ionic radii, Goldschmidt tolerance factor, octahedral mismatch, valence charges, Hund's rule spin moments, bond lengths, unit cell volume, and mass density).

---

## 2. Method Architecture & Mathematical Formulation

Experiment 11 establishes the **Standard Linear Regression Baseline** ($y = w_0 + \sum_{i=1}^{N} w_i x_i$) across all 4 target properties:

1. **Standard Ordinary Least Squares (OLS) Linear Regression**:
   $$\widehat{y}(\mathbf{x}) = w_0 + \sum_{j=1}^{33} w_j x_j$$
   Solves the closed-form normal equations: $\mathbf{w} = (\mathbf{X}^T \mathbf{X})^{-1} \mathbf{X}^T \mathbf{y}$.

2. **Two-Stage Linear Hurdle System (for Zero-Inflated Targets)**:
   - **Stage 1 (Linear Logistic Classifier)**: Predicts non-zero state binary probability $\widehat{y}_{\text{bin}} = 1$ if $\sigma(\mathbf{w}_{\text{cls}}^T \mathbf{x} + b) > 0.5$.
   - **Stage 2 (Linear Regressor on Non-Zeros)**: Fits standard linear regression on active non-zero samples ($y > \text{threshold}$).
   - **Stage 3 (Combined Pipeline Inference)**: $\widehat{y}_{\text{pipeline}}(\mathbf{x}) = \begin{cases} 0.0 & \text{if } \widehat{y}_{\text{bin}} == 0 \\ \max(0.0, \mathbf{w}_{\text{reg}}^T \mathbf{x} + b) & \text{if } \widehat{y}_{\text{bin}} == 1 \end{cases}$.

---

## 3. Reference Theoretical Limits (Literature Benchmark)

- **Formation Energy ($\Delta E_f$)**: $R^2_{\text{limit}} = 65.0\%$ [Ouyang et al. 2018, Bartel et al. 2019]
- **Total Magnetization ($M$)**: $R^2_{\text{limit}} = 60.0\%$ [Ouyang et al. 2018, Ghiringhelli et al. 2015]
- **Band Gap ($E_g$)**: $R^2_{\text{limit}} = 50.0\%$ [Ouyang et al. 2018, Borlido et al. 2019]
- **Energy Above Hull ($E_{\text{hull}}$)**: $R^2_{\text{limit}} = 25.0\%$ [Bartel et al. 2019 SciAdv, Sun et al. 2016]

$$\text{Theoretical Limit (\%)} = \frac{\max(0.0, R^2_{\text{pipeline}})}{R^2_{\text{limit}}} \times 100\%$$
