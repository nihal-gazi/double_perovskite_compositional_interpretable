# Ablation Study Methodology: Master Algorithm Component Isolation

## 1. Executive Summary

This document specifies the experimental design for the **Systematic Ablation Study** of the Master Capstone Double Perovskite Machine Learning Algorithm (`exp_v2/research/ablation_study/`).

To prove the statistical necessity and independent contribution of every novel physical descriptor engine and model architecture component, we define **8 distinct experimental ablation conditions (C0 to C7)**:

---

## 2. Formal Specification of Ablation Conditions (C0 – C7)

| Code | Condition Name | Feature Engines Included | Architecture Model Engine | Objective & Hypothesis |
| :--- | :--- | :--- | :--- | :--- |
| **C0** | `Baseline_Classical` | Classical 0D Features Only ($t, r, \chi, \text{Val}, d\text{-count}$) | Target-Specific Default | Establishes classical baseline performance before physical engine additions. |
| **C1** | `+Harrison_Quantum_Gap` | C0 + $E_{\text{gap, QM}}$ ($IE_B, EA_O, V_{\text{transfer}}$) | Target-Specific Default | Tests contribution of Harrison's tight-binding quantum gap. |
| **C2** | `+Birch_Murnaghan_Strain` | C1 + $E_{\text{tolerance\_strain}}, E_{\text{oct\_distortion\_strain}}$ | Target-Specific Default | Tests contribution of thermodynamic elastic strain proxies. |
| **C3** | `+Octahedral_d0_d10` | C2 + `Is_d0_B`, `Is_d10_B`, `Is_Closed_Shell_both` | Target-Specific Default | Tests contribution of closed-shell crystal field indicators. |
| **C4** | `+Single_Perov_TieLines` | C3 + $D_{\text{hull\_proxy}}, \Delta t_{\text{sub\_perov}}, \Delta H_{\text{sub\_perov\_mismatch}}$ | Target-Specific Default | Tests contribution of single-perovskite competing phase tie-lines. |
| **C5** | `Direct_Linear_No_Hurdle` | All Features (C4) | Single-Stage Ridge Regression Only | Proves necessity of two-stage hurdle/gating decomposition. |
| **C6** | `Hard_Step_Hurdle` | All Features (C4) | Hard Step Hurdle Model $\mathbb{I}(S \ge \tau^*)$ | Proves necessity of Soft-Sigmoidal Gated continuous transitions. |
| **C7** | **`Master_Capstone_Full`** | **All Feature Engines (C4)** | **Full Master Architecture Engine** | **Represents complete Master Capstone Algorithm performance.** |

---

## 3. Evaluated Performance Metrics

For each target property ($\Delta E_f, M, E_g, E_{\text{hull}}$) under each condition (C0–C7):
1. **Stage 1 Classification Accuracy (%)** & **F1-Score**
2. **Stage 2 Non-Zero Sub $R^2$ (%)**
3. **Final Pipeline $R^2$ (%)**
4. **Pipeline Mean Squared Error (MSE)** & **Mean Absolute Error (MAE)**
5. **Relative Theoretical Limit Achieved (%)**:
   $$\text{Theoretical Limit (\%)} = \frac{\max(0.0, R^2_{\text{pipeline}})}{R^2_{\text{limit}}} \times 100\%$$
