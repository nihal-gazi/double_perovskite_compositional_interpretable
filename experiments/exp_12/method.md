# Experiment 12: Physical Interaction & Polynomial-Linear Hybrid Model (Clean Physical Descriptors)

## 1. Executive Summary & Data Leakage Audit

Following the data leakage audit, **3 leaked GNN-derived structural proxies were removed** from the candidate feature pool:
- **`M_net` & `M_abs`**: Pre-computed CHGNet magnetic moments ($r = 1.0000$ correlation with target `Total_Magnetization_uB`).
- **`E_GNN`**: Pre-computed CHGNet DFT energy surrogate ($r = 0.9994$ correlation with target `Formation_Energy_eV_atom`).

All evaluations in **Experiment 12** are performed on **33 pure physical and chemical descriptors** expanded with **2nd-order physical interaction terms and dimensionless ratios**:
- **Multiplication Interactions**: $x_i \cdot x_j$ (e.g., $\text{Tolerance\_Factor} \cdot \text{Octahedral\_Mismatch}$, $\text{EN\_avg} \cdot \text{Volume\_A3}$, $\text{Total\_HS\_FiM} \cdot \text{Total\_d\_electrons}$).
- **Dimensionless Ratios**: $x_i / (x_j + \epsilon)$ (e.g., $\text{EN\_B} / \text{EN\_A}$, $\text{Shannon\_B} / \text{Shannon\_A}$, $d_{\text{BO}} / d_{\text{AO}}$).
- **Polynomial Squares**: $x_i^2$.

---

## 2. Method Architecture & Mathematical Formulation

Experiment 12 constructs a **Physical Interaction & Polynomial-Linear Hybrid Model** ($y = w_0 + \sum w_i x_i + \sum w_{ij} x_i x_j + \sum w_{k} \frac{x_i}{x_j}$) regularized via Ridge/Lasso feature selection:

1. **Physical Feature Expansion & Standard Normalization**:
   $$\mathbf{\Phi}(\mathbf{x}) = \left[ \mathbf{x}, \; \mathbf{x}^2, \; \{ x_i \cdot x_j \}_{i < j}, \; \left\{ \frac{x_i}{x_j + \epsilon} \right\} \right]$$

2. **Direct Regularized Polynomial-Linear Regression**:
   $$\widehat{y}(\mathbf{x}) = w_0 + \mathbf{w}^T \mathbf{\Phi}(\mathbf{x})$$
   Objective: $\min_{\mathbf{w}} \|\mathbf{y} - \mathbf{\Phi X} \mathbf{w}\|_2^2 + \alpha \|\mathbf{w}\|_2^2 + \lambda \|\mathbf{w}\|_1$.

3. **Two-Stage Hurdle Architecture (for Zero-Inflated Targets)**:
   - **Stage 1 (Logistic Classifier with Interactions)**: Predicts non-zero state binary probability $\widehat{y}_{\text{bin}} = 1$ if $\sigma(\mathbf{w}_{\text{cls}}^T \mathbf{\Phi}(\mathbf{x}) + b) > 0.5$.
   - **Stage 2 (Interaction Regressor on Non-Zeros)**: Fits regularized polynomial-linear model on active non-zero samples ($y > \text{threshold}$).
   - **Stage 3 (Combined Pipeline Inference)**: $\widehat{y}_{\text{pipeline}}(\mathbf{x}) = \begin{cases} 0.0 & \text{if } \widehat{y}_{\text{bin}} == 0 \\ \max(0.0, \mathbf{w}_{\text{reg}}^T \mathbf{\Phi}(\mathbf{x}) + b) & \text{if } \widehat{y}_{\text{bin}} == 1 \end{cases}$.

---

## 3. Reference Theoretical Limits (Literature Benchmark)

- **Formation Energy ($\Delta E_f$)**: $R^2_{\text{limit}} = 65.0\%$ [Ouyang et al. 2018, Bartel et al. 2019]
- **Total Magnetization ($M$)**: $R^2_{\text{limit}} = 60.0\%$ [Ouyang et al. 2018, Ghiringhelli et al. 2015]
- **Band Gap ($E_g$)**: $R^2_{\text{limit}} = 50.0\%$ [Ouyang et al. 2018, Borlido et al. 2019]
- **Energy Above Hull ($E_{\text{hull}}$)**: $R^2_{\text{limit}} = 25.0\%$ [Bartel et al. 2019 SciAdv, Sun et al. 2016]

$$\text{Theoretical Limit (\%)} = \frac{\max(0.0, R^2_{\text{pipeline}})}{R^2_{\text{limit}}} \times 100\%$$
