# Experiment 7: Dual Symbolic Regression Hurdle Architecture Report (Clean Physical Descriptors)

## 1. Executive Summary & Data Leakage Audit

Following a rigorous feature audit, **3 leaked GNN-derived structural proxies were removed** from the candidate feature pool to guarantee zero data leakage and ensure 100% genuine physical interpretability:
- **`M_net` & `M_abs`**: Pre-computed CHGNet magnetic moments ($r = 1.0000$ correlation with target `Total_Magnetization_uB`).
- **`E_GNN`**: Pre-computed CHGNet DFT energy surrogate ($r = 0.9994$ correlation with target `Formation_Energy_eV_atom`).

All evaluations in **Experiment 7** are performed on **33 pure physical and chemical descriptors** (electronegativities, ionic radii, Goldschmidt tolerance factor, octahedral mismatch, valence charges, Hund's rule spin moments, bond lengths, unit cell volume, and mass density).

---

## 2. Method Architecture

1. **Stage 1 (Symbolic Boundary Classifier)**:
   - Evaluates a short Genetic Programming Symbolic Regression using `gplearn` with a **custom classification fitness metric**:
     $$\text{Fitness} = \sum_{i=1}^{M} \text{score}_i, \quad \text{where } \text{score}_i = \begin{cases} +1 & \text{if } (S_{\text{cls}}(\mathbf{x}_i) > 0.0) == y_{\text{bin}, i} \\ -1 & \text{if } (S_{\text{cls}}(\mathbf{x}_i) > 0.0) \neq y_{\text{bin}, i} \end{cases}$$
   - **Decision Rule**: $\widehat{y}_{\text{bin}} = 1\ (\text{Non-Zero})$ if $S_{\text{cls}}(\mathbf{x}) > 0.0$, else $0\ (\text{Zero})$.
   - Discovers an analytical hypersurface $S_{\text{cls}}(\mathbf{x}) = 0$ separating zero from non-zero states.

2. **Stage 2 (Symbolic Non-Zero Regressor)**:
   - For active non-zero samples ($y > \text{threshold}$), runs standard Symbolic Regression (`gplearn` `SymbolicRegressor`) using the Mean Absolute Error / MSE fitness metric to discover a single continuous analytical expression $S_{\text{reg}}(\mathbf{x})$ mapping physical descriptors to target magnitudes.

3. **Stage 3 (Combined Dual-SR Hurdle Pipeline Inference)**:
   $$\widehat{y}_{\text{pipeline}}(\mathbf{x}) = \begin{cases} 0.0 & \text{if } S_{\text{cls}}(\mathbf{x}) \le 0.0 \\ \max\left(0.0, S_{\text{reg}}(\mathbf{x})\right) & \text{if } S_{\text{cls}}(\mathbf{x}) > 0.0 \end{cases}$$
   *(For Formation Energy $\Delta E_f$, non-negative clipping is disabled as values are physically negative).*

---

## 3. Mathematical Function Set & Hyperparameters

Both Stage 1 Classifier and Stage 2 Regressor use the **exact same set of 7 parsimonious base mathematical operators** (matching Exp 5):

$$\mathcal{F} = \{\text{add}, \text{sub}, \text{mul}, \text{div}, \text{neg}, \text{abs}, \text{log}\}$$

| Parameter | Setting | Description |
| :--- | :--- | :--- |
| **GP Function Set** | `add, sub, mul, div, neg, abs, log` | Same 7 base operators as exp_5 |
| **Candidate Features** | `33` pure physical descriptors | `E_GNN`, `M_net`, `M_abs` removed |
| **Stage 1 Population Size** | `1500` | Candidate expressions per generation for classifier |
| **Stage 1 Generations** | `15` | Short genetic programming evolution for boundary |
| **Stage 1 Fitness Metric** | `+1` (correct), `-1` (wrong) | Maximizes classification accuracy score |
| **Stage 2 Population Size** | `2000` | Candidate expressions per generation for regressor |
| **Stage 2 Generations** | `25` | Genetic programming evolution for non-zero regression |
| **Stage 2 Fitness Metric** | `mean absolute error` / `mse` | Minimizes non-zero prediction error |
| **Random Seed** | `42` | PyTorch, NumPy & GP random seed |
| **Dataset Location** | `exp_v2/data/data_24_7_2026/double_perovskite_dataset.csv` | 2,000 double perovskite materials |
