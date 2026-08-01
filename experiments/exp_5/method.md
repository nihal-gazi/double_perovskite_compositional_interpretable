# Experiment 5: Hybrid Symbolic Regression Decision Boundary Classifier + Optimal Top-K* Fourier Ensemble Regressor (Clean Physical Descriptors)

## 1. Executive Summary & Data Leakage Audit

Following a rigorous feature audit, **3 leaked GNN-derived structural proxies were removed** from the candidate feature pool to guarantee zero data leakage and ensure 100% genuine physical interpretability:
- **`M_net` & `M_abs`**: Pre-computed CHGNet magnetic moments ($r = 1.0000$ correlation with target `Total_Magnetization_uB`).
- **`E_GNN`**: Pre-computed CHGNet DFT energy surrogate ($r = 0.9994$ correlation with target `Formation_Energy_eV_atom`).

All evaluations in **Experiment 5** are performed on **33 pure physical and chemical descriptors** (electronegativities, ionic radii, Goldschmidt tolerance factor, octahedral mismatch, valence charges, Hund's rule spin moments, bond lengths, unit cell volume, and mass density).

---

## 2. Method Architecture

- **Stage 1 (Pure Symbolic Regression Classifier)**: Runs a short Genetic Programming Symbolic Regression using `gplearn` with a **custom classification fitness metric**.
  - **Decision Rule**:
    $$\widehat{y}_{\text{bin}} = \begin{cases} 1\ (\text{Non-Zero}) & \text{if } S_{\text{sym}}(\mathbf{x}) > 0.0 \\ 0\ (\text{Zero}) & \text{if } S_{\text{sym}}(\mathbf{x}) \le 0.0 \end{cases}$$
  - **Custom Fitness Scoring Metric**:
    $$\text{Fitness} = \sum_{i=1}^{M} \text{score}_i, \quad \text{where } \text{score}_i = \begin{cases} +1 & \text{if } \widehat{y}_{\text{bin}, i} == y_{\text{bin}, i} \\ -1 & \text{if } \widehat{y}_{\text{bin}, i} \neq y_{\text{bin}, i} \end{cases}$$
  - Discovers a 100% human-readable analytical hypersurface $S_{\text{sym}}(\mathbf{x}) = 0$ separating zero from non-zero states.

- **Stage 2 (Optimal Top-K* Fourier Ensemble Non-Zero Regressor)**:
  - Takes active non-zero samples ($y > \text{threshold}$) and fits 1D Fourier Series Regressors across Fourier depths $D \in \{3, 5, 10, 50, 100\}$.
  - **Dynamic $K^*$ Selection**: For each depth $D$, we perform a Top-$K$ ensemble sweep across $K \in \{1, 2, \dots, 10\}$ and select the **optimal ensemble capacity $K^*(D)$** that maximizes the combined pipeline $R^2$:
    $$K^*(D) = \arg\max_{K \in \{1, \dots, 10\}} R^2_{\text{pipeline}}(K, D)$$
    $$F_{\text{reg}}^{(K^*)}(\mathbf{x}) = \frac{1}{K^*} \sum_{j=0}^{K^*-1} f^{\text{reg}}_{(j)}\left(I_{(j)}\right)$$

- **Stage 3 (Combined Hurdle Pipeline Inference)**:
  $$\widehat{y}_{\text{pipeline}} = \begin{cases} 0.0 & \text{if } \widehat{y}_{\text{bin}} == 0 \\ F_{\text{reg}}^{(K^*)}(\mathbf{x}) & \text{if } \widehat{y}_{\text{bin}} == 1 \end{cases}$$

---

## 3. Selection Priority Rule for Best Fourier Depth $D^*$

To select the representative **Best Fourier Depth $D^*$** for final analytical expression export in `discovered_equations.md`, we strictly enforce the following hierarchical priority rule:

1. **Priority 1 (High-Accuracy Threshold $\ge 90\%$)**:
   - If any evaluated Fourier depth $D \in \{3, 5, 10, 50, 100\}$ achieves a Final Pipeline $R^2 \ge 90.0\%$, select the smallest parsimonious depth $D^*$ among those exceeding $90\%$.
2. **Priority 2 (Moderate-Accuracy Fallback among $D=5$ and $D=10$)**:
   - If no evaluated depth achieves a Final Pipeline $R^2 \ge 90.0\%$, select the depth $D^* \in \{5, 10\}$ that yields the highest Final Pipeline $R^2$:
     $$D^* = \arg\max_{D \in \{5, 10\}} R^2_{\text{pipeline}}(D)$$

---

## 4. Hyperparameters & Settings

| Parameter | Value / Setting | Description |
| :--- | :--- | :--- |
| **Random Seed** | `42` | PyTorch & NumPy random seed |
| **Dataset Location** | `exp_v2/data/data_24_7_2026/double_perovskite_dataset.csv` | 2,000 double perovskites |
| **Candidate Features** | `33` pure physical descriptors | `E_GNN`, `M_net`, `M_abs` removed |
| **GP Population Size** | `1500` | Number of candidate symbolic expressions per generation |
| **GP Generations** | `15` | Short genetic programming evolution steps |
| **GP Custom Fitness** | `+1` (correct), `-1` (wrong) | Maximizes classification accuracy score |
| **GP Function Set** | `['add', 'sub', 'mul', 'div', 'neg', 'abs', 'log']` | Parsimonious base mathematical operators |
| **Fourier Depths ($D$)** | `[3, 5, 10, 50, 100]` | Frequency harmonics evaluated |
| **Selection Priority** | Priority 1: $R^2 \ge 90\%$; Priority 2: $\max(R^2(D=5), R^2(D=10))$ | Hierarchical selection rule for $D^*$ |
