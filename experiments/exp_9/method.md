# Experiment 9: Dual Symbolic Regression Hurdle Architecture with Extended Mathematical Operators (Clean Physical Descriptors)

## 1. Executive Summary & Data Leakage Audit

Following a rigorous feature audit, **3 leaked GNN-derived structural proxies were removed** from the candidate feature pool to guarantee zero data leakage and ensure 100% genuine physical interpretability:
- **`M_net` & `M_abs`**: Pre-computed CHGNet magnetic moments ($r = 1.0000$ correlation with target `Total_Magnetization_uB`).
- **`E_GNN`**: Pre-computed CHGNet DFT energy surrogate ($r = 0.9994$ correlation with target `Formation_Energy_eV_atom`).

All evaluations in **Experiment 9** are performed on **33 pure physical and chemical descriptors** (electronegativities, ionic radii, Goldschmidt tolerance factor, octahedral mismatch, valence charges, Hund's rule spin moments, bond lengths, unit cell volume, and mass density).

---

## 2. Extended Mathematical Primitive Function Set (19 Operators)

Experiment 9 expands the Genetic Programming function set for **BOTH** the Stage 1 Classifier and Stage 2 Regressor by adding **11 advanced mathematical operators** to the base arithmetic, logarithmic, and power set:

1. **Base Operators (8)**: `add`, `sub`, `mul`, `div`, `neg`, `abs`, `log`, `pow`
2. **Trigonometric & Reciprocal Primitives (5)**:
   - **`sin(x)`**: Standard sine function.
   - **`cos(x)`**: Standard cosine function.
   - **`tan(x)`**: Protected tangent function (overflow-safe).
   - **`cosec(x)`**: Protected cosecant $\csc(x) = \frac{1}{\sin(x)}$.
   - **`sec(x)`**: Protected secant $\sec(x) = \frac{1}{\cos(x)}$.
3. **Exponential & Special Primitives (3)**:
   - **`exp(x)`**: Protected exponential function $\exp(\text{clip}(x, -10, 10))$.
   - **`gaussian_function(x)`**: Protected 1D Gaussian basis $\exp(-x^2)$.
   - **`sign(x)`**: Signum function $\text{sgn}(x) \in \{-1, 0, 1\}$.
4. **Step, Modular & Root Primitives (3)**:
   - **`mod(x1, x2)`**: Protected floating-point modulo $x_1 \pmod{x_2}$.
   - **`ceil(x)`**: Ceiling step function $\lceil x \rceil$.
   - **`nth_root(x1, x2)`**: Protected $n$-th root $\sqrt[|x_2|]{|x_1|}$.

$$\mathcal{F}_{\text{exp9}} = \{\text{add, sub, mul, div, neg, abs, log, pow, sin, cos, exp, tan, cosec, sec, mod, ceil, sign, nth\_root, gaussian\_function}\}$$

---

## 3. Method Architecture & Mathematical Formulation

1. **Stage 1 (Symbolic Boundary Classifier with Extended Operators)**:
   - Evaluates Genetic Programming Symbolic Regression using `gplearn` with a **custom classification fitness metric**:
     $$\text{Fitness} = \sum_{i=1}^{M} \text{score}_i, \quad \text{where } \text{score}_i = \begin{cases} +1 & \text{if } (S_{\text{cls}}(\mathbf{x}_i) > 0.0) == y_{\text{bin}, i} \\ -1 & \text{if } (S_{\text{cls}}(\mathbf{x}_i) > 0.0) \neq y_{\text{bin}, i} \end{cases}$$
   - **Decision Rule**: $\widehat{y}_{\text{bin}} = 1\ (\text{Non-Zero})$ if $S_{\text{cls}}(\mathbf{x}) > 0.0$, else $0\ (\text{Zero})$.

2. **Stage 2 (Symbolic Non-Zero Regressor with Extended Operators)**:
   - For active non-zero samples ($y > \text{threshold}$), runs standard Symbolic Regression (`gplearn` `SymbolicRegressor`) using the Mean Absolute Error / MSE fitness metric with all 19 operators enabled.

3. **Stage 3 (Combined Dual-SR Hurdle Pipeline Inference)**:
   $$\widehat{y}_{\text{pipeline}}(\mathbf{x}) = \begin{cases} 0.0 & \text{if } S_{\text{cls}}(\mathbf{x}) \le 0.0 \\ \max\left(0.0, S_{\text{reg}}(\mathbf{x})\right) & \text{if } S_{\text{cls}}(\mathbf{x}) > 0.0 \end{cases}$$

---

## 4. Hyperparameters

| Parameter | Setting | Description |
| :--- | :--- | :--- |
| **GP Function Set** | `19 mathematical primitives` | Includes sin, cos, exp, tan, cosec, sec, mod, ceil, sign, nth_root, gaussian |
| **Candidate Features** | `33` pure physical descriptors | `E_GNN`, `M_net`, `M_abs` removed |
| **Stage 1 Population Size** | `1500` | Candidate expressions per generation for classifier |
| **Stage 1 Generations** | `15` | Short genetic programming evolution for boundary |
| **Stage 1 Fitness Metric** | `+1` (correct), `-1` (wrong) | Maximizes classification accuracy score |
| **Stage 2 Population Size** | `2000` | Candidate expressions per generation for regressor |
| **Stage 2 Generations** | `25` | Genetic programming evolution for non-zero regression |
| **Stage 2 Fitness Metric** | `mean absolute error` / `mse` | Minimizes non-zero prediction error |
| **Random Seed** | `42` | PyTorch, NumPy & GP random seed |
| **Dataset Location** | `exp_v2/data/data_24_7_2026/double_perovskite_dataset.csv` | 2,000 double perovskite materials |
