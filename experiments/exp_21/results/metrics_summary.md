# Experiment 21: Log-Transformed Target Space & Gibbs Phase Separation Engine Report

**Dataset:** `exp_v2/data/data_24_7_2026/double_perovskite_dataset.csv` (2,000 double perovskites)  
**Data Leakage & 3D Audit Compliance:** 100% Pure Compositional Descriptors (Zero 3D atomic coordinates, zero GNN proxies `E_GNN`, `M_net`, `M_abs`).  
**New Physical Descriptors Added:** Gibbs Phase Separation Energy Index ($\Xi_{\text{hull}}$), Entropic Driving Force Proxy ($\Delta G_{\text{decomp\_proxy}}$), Log-Transformed Target Space Regression ($z = \log(y + 1.0)$).  
**Theoretical Limit References (Literature):** Formation Energy ($R^2_{\text{limit}} = 65.0\%$), Magnetization ($R^2_{\text{limit}} = 60.0\%$), Band Gap ($R^2_{\text{limit}} = 50.0\%$), Hull Energy ($R^2_{\text{limit}} = 25.0\%$).  

---

## Performance Summary Table Across Target Properties

| Target Property | Optimal Architecture | Stage 1 Acc (%) | Stage 2 Sub R² (%) | **Sub R² Limit (%)** | **Final Pipeline R² (%)** | **Theoretical Limit (%)** | Final MSE | Final MAE |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Formation Energy (eV/atom)** | direct_multi_operator | 100.00% | 71.26% | **109.62%** | **71.26%** | **109.62%** | 0.100281 | 0.1870 |
| **Total Magnetization (uB)** | hard_margin_hurdle | 92.80% | 61.75% | **102.92%** | **62.23%** | **103.72%** | 35.788531 | 3.0011 |
| **Band Gap (eV)** | soft_gated_regressor | 88.20% | 41.04% | **82.09%** | **50.71%** | **101.42%** | 0.768051 | 0.7062 |
| **Energy Above Hull (eV)** | log_target_hurdle | 94.60% | 10.73% | **42.91%** | **15.10%** | **60.42%** | 0.062395 | 0.0664 |

---

