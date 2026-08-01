# Experiment 19: Octahedral d0/d10 Closed-Shell Engine & Oxidation Enthalpy Mismatch Report

**Dataset:** `exp_v2/data/data_24_7_2026/double_perovskite_dataset.csv` (2,000 double perovskites)  
**Data Leakage & 3D Audit Compliance:** 100% Pure Compositional Descriptors (Zero 3D atomic coordinates, zero GNN proxies `E_GNN`, `M_net`, `M_abs`).  
**New Physical Descriptors Added:** Octahedral $d^0/d^{10}$ Closed-Shell Indicators (`Is_d0_B`, `Is_d10_B`, `Is_Closed_Shell_both`), Binary Oxidation Enthalpy Mismatch ($\Delta H_{\text{ox\_mismatch}}$), Soft-Sigmoidal Gated Regressor.  
**Theoretical Limit References (Literature):** Formation Energy ($R^2_{\text{limit}} = 65.0\%$), Magnetization ($R^2_{\text{limit}} = 60.0\%$), Band Gap ($R^2_{\text{limit}} = 50.0\%$), Hull Energy ($R^2_{\text{limit}} = 25.0\%$).  

---

## Performance Summary Table Across Target Properties

| Target Property | Optimal Architecture | Stage 1 Acc (%) | Stage 2 Sub R² (%) | **Sub R² Limit (%)** | **Final Pipeline R² (%)** | **Theoretical Limit (%)** | Final MSE | Final MAE |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Formation Energy (eV/atom)** | direct_multi_operator | 100.00% | 71.24% | **109.59%** | **71.24%** | **109.59%** | 0.100353 | 0.1870 |
| **Total Magnetization (uB)** | hard_margin_hurdle | 91.35% | 61.67% | **102.78%** | **61.16%** | **101.94%** | 36.798237 | 3.0962 |
| **Band Gap (eV)** | soft_gated_regressor | 88.65% | 41.03% | **82.06%** | **50.82%** | **101.63%** | 0.766382 | 0.7052 |
| **Energy Above Hull (eV)** | hard_margin_hurdle | 92.70% | 12.25% | **49.00%** | **16.29%** | **65.14%** | 0.061527 | 0.0780 |

---

