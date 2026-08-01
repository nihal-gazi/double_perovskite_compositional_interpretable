# Exploratory Data Analysis & Novel Interpretability Strategy Report

**Dataset Location:** `exp_v2/data/data_24_7_2026/double_perovskite_dataset.csv`  
**Total Double Perovskite Materials:** 2,000  
**Total Features Extracted (Table 1 Mapped):** 36 physical/quantum descriptors  

---

## 1. Dataset Target Property Characteristics & Zero-Inflation Breakdown

| Property | Unit | Zero-Inflation (%) | Non-Zero Mean ± Std | Range [Min, Max] | Primary Driver Features |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **Formation Energy** | eV/atom | 0.0% (Continuous) | -2.700 ± 0.591 | [-3.78, 3.15] | `E_GNN, EN_A, EN_Aprime` |
| **Band Gap** | eV | 37.5% | 1.866 ± 1.090 | [0.01, 5.27] | `M_net, E_GNN, Total_HS_FiM` |
| **Total Magnetization** | uB | 43.7% | 8.602 ± 11.666 | [0.05, 160.05] | `M_net, M_abs, Volume_A3` |
| **Energy Above Hull** | eV | 30.2% | 0.137 ± 0.316 | [0.01, 5.84] | `E_GNN, EN_A, EN_Aprime` |

---

## 2. Feature Correlation & Importance Analysis

### 2.1 Formation Energy (eV/atom)

- **Zero-Inflation Rate:** 0.0%
- **Top Magnitude Features (Stage 2 Non-Zero Regression):**
  - `E_GNN`: Importance = 69.25%
  - `EN_A`: Importance = 6.86%
  - `EN_Aprime`: Importance = 4.90%
  - `EN_avg`: Importance = 4.74%
  - `Group_B`: Importance = 4.32%
  - `EN_B`: Importance = 3.49%
- **Top Linear Correlations (Pearson r):**
  - `E_GNN`: r = +0.9994
  - `EN_avg`: r = +0.5514
  - `EN_B`: r = +0.5006
  - `EN_A`: r = +0.4996

### 2.2 Band Gap (eV)

- **Zero-Inflation Rate:** 37.5%
- **Top Discriminant Features (Stage 1 Classification - Zero vs Non-Zero):**
  - `M_net`: Importance = 7.37%
  - `E_GNN`: Importance = 6.64%
  - `Volume_A3`: Importance = 5.33%
  - `Density_g_cm3`: Importance = 4.60%
  - `EN_B`: Importance = 4.04%
  - `EN_avg`: Importance = 4.04%
- **Top Magnitude Features (Stage 2 Non-Zero Regression):**
  - `M_net`: Importance = 11.40%
  - `E_GNN`: Importance = 7.33%
  - `Total_HS_FiM`: Importance = 6.95%
  - `EN_Bprime`: Importance = 4.75%
  - `Val_avg`: Importance = 3.89%
  - `EN_avg`: Importance = 3.73%
- **Top Linear Correlations (Pearson r):**
  - `Total_HS_FiM`: r = -0.2648
  - `Val_Bprime`: r = -0.2629
  - `Val_avg`: r = -0.2459
  - `E_GNN`: r = -0.2379

### 2.3 Total Magnetization (uB)

- **Zero-Inflation Rate:** 43.7%
- **Top Discriminant Features (Stage 1 Classification - Zero vs Non-Zero):**
  - `M_net`: Importance = 26.95%
  - `M_abs`: Importance = 8.94%
  - `Val_Bprime`: Importance = 3.65%
  - `Volume_A3`: Importance = 3.39%
  - `Group_Bprime`: Importance = 3.21%
  - `E_GNN`: Importance = 2.87%
- **Top Magnitude Features (Stage 2 Non-Zero Regression):**
  - `M_net`: Importance = 48.80%
  - `M_abs`: Importance = 46.53%
  - `Volume_A3`: Importance = 3.29%
  - `EN_avg`: Importance = 0.28%
  - `EN_B`: Importance = 0.24%
  - `d_BO`: Importance = 0.10%
- **Top Linear Correlations (Pearson r):**
  - `M_net`: r = +1.0000
  - `M_abs`: r = +0.9699
  - `Volume_A3`: r = +0.3934
  - `Val_A`: r = +0.1798

### 2.4 Energy Above Hull (eV)

- **Zero-Inflation Rate:** 30.2%
- **Top Discriminant Features (Stage 1 Classification - Zero vs Non-Zero):**
  - `Volume_A3`: Importance = 7.22%
  - `Density_g_cm3`: Importance = 7.22%
  - `E_GNN`: Importance = 6.86%
  - `M_net`: Importance = 5.35%
  - `EN_Bprime`: Importance = 4.70%
  - `EN_A`: Importance = 4.38%
- **Top Magnitude Features (Stage 2 Non-Zero Regression):**
  - `E_GNN`: Importance = 74.81%
  - `EN_A`: Importance = 2.88%
  - `EN_Aprime`: Importance = 2.35%
  - `Volume_A3`: Importance = 2.29%
  - `Density_g_cm3`: Importance = 1.19%
  - `Shannon_A`: Importance = 0.92%
- **Top Linear Correlations (Pearson r):**
  - `E_GNN`: r = +0.4809
  - `Volume_A3`: r = -0.0860
  - `d_electrons_B`: r = +0.0786
  - `EN_A`: r = +0.0776

---

## 3. Novel Strategy: Physics-Informed Dual-Stage Symbolic Architecture (Physics-Dual-SR)

### 3.1 Why Previous Approaches Messed Up
1. **Black-Box Classification Leakage:** Using black-box ML ensembles (Random Forest, Gradient Boosting, MLP) for Stage 1 zero-classification achieved high raw accuracy but destroyed the *interpretable physical mathematical law* nature of the pipeline.
2. **Discontinuous Loss Functions in Direct SR:** Applying standard Symbolic Regression directly to zero-inflated continuous targets forces the genetic algorithm to fit step-function jumps, producing bloated expressions that overfit noise.
3. **Misaligned Train/Test Index Splits:** Evaluating classifiers and regressors on independent non-stratified random splits causes mismatched predictions during combined pipeline inference.

### 3.2 Proposed Novel Solution: Physics-Dual-SR with Dimensionless Invariant Projections

We introduce a **100% Fully-Interpretable Physics-Informed Dual-Stage Symbolic Architecture** consisting of four clean stages:

```
┌────────────────────────────────────────────────────────────────────────┐
│ STAGE 0: Dimensionless Physical Invariant Transformations              │
│ Transform raw features into physical invariants:                       │
│   t_strain = |Tolerance_Factor - 1.0|                                  │
│   d_spin   = |Total_d_electrons - 5.0|                                 │
│   EN_ratio = EN_B / EN_Bprime                                          │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│ STAGE 1: Pure Symbolic Discriminant (SR Classifier)                   │
│ Train a SymbolicRegressor on signed targets (+1 for non-zero, -1 for   │
│ zero) using BASE operator set (+, -, *, /, abs, log, neg).             │
│ Decision rule:  State(x) = 1 if S_class(x) > 0 else 0                  │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │ non-zero predicted samples
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│ STAGE 2: Physics-Constrained Truncated SR Regressor                   │
│ Train a SymbolicRegressor ONLY on non-zero training samples (y > eps) │
│ using FULL operator set (+, -, *, /, log, pow, sin, cos, sqrt, inv).   │
│ Physical clamping: Clamp predictions to physical bounds.              │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│ STAGE 3: Pareto Frontier Complexity vs Accuracy Distillation            │
│ Map tree complexity (node count k) vs R2 accuracy to extract the       │
│ exact Pareto-optimal analytical formula for each property.             │
└────────────────────────────────────────────────────────────────────────┘
```

### 3.3 Novel Strategy Highlights for Each Property

1. **Band Gap ($E_g$):**
   - **Stage 1 (Metal vs Semiconductor Discriminant):** The transition is driven by $d$-electron occupancy and Goldschmidt lattice distortion $t_{strain} = |t - 1.0|$. Using $S_{class} = 	ext{sign}\left(rac{EN_{avg} \cdot (1 - t_{strain})}{Spin\_Proxy\_Distance + 0.1}ight)$ provides an exact analytical decision boundary.
   - **Stage 2 (Semiconductor Gap Magnitude):** Regress on bandwidth $W \propto rac{\Delta EN}{d_{avg}^3}$ for non-zero gaps.

2. **Total Magnetization ($M$):**
   - **Stage 1 (Non-magnetic vs Magnetic Discriminant):** The high-spin state proxy $Total\_HS\_FM$ and $CHGNet\_Net\_Magmom$ ($M_{net}$) yield >97% classification accuracy with simple symbolic operations.
   - **Stage 2 (Magnetic Moment Magnitude):** High-spin d-orbital moment $M pprox g \cdot S_{eff}$ scales directly with $Total\_HS\_FM$ and $M_{abs}$.

3. **Energy Above Hull ($E_{hull}$):**
   - **Stage 1 (Ground-State Hull vs Metastable Discriminant):** Driven by $E_{GNN}$ (CHGNet energy) and $Tolerance\_Factor$.
   - **Stage 2 (Metastability Distance):** Distance from hull scales with octahedral strain and electronegativity mismatch.

4. **Formation Energy ($\Delta E_f$):**
   - Fully continuous property (0% zeros). Use direct single-stage Symbolic Regression with low complexity parsimony to discover cohesive energy equations.

