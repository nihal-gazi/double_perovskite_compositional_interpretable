# Experiment 12: Physical Interaction & Polynomial-Linear Hybrid Model Summary Report

**Dataset:** `exp_v2/data/data_24_7_2026/double_perovskite_dataset.csv` (2,000 double perovskites)  
**Data Leakage Audit:** Removed `E_GNN`, `M_net`, `M_abs`. Evaluated on 33 pure physical descriptors expanded with 2nd-order interaction terms ($x_i x_j$, $x_i/x_j$, $x_i^2$).  
**Theoretical Limit References (Literature):** Formation Energy ($R^2_{\text{limit}} = 65.0\%$), Magnetization ($R^2_{\text{limit}} = 60.0\%$), Band Gap ($R^2_{\text{limit}} = 50.0\%$), Hull Energy ($R^2_{\text{limit}} = 25.0\%$).  

---

## Performance Summary Table

| Target Property | Direct Interaction R² (%) | **Direct Theoretical Limit (%)** | Stage 1 Cls Acc (%) | Stage 2 Sub R² (%) | **Hurdle Pipeline R² (%)** | **Hurdle Theoretical Limit (%)** | Hurdle MSE | Hurdle MAE |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Band Gap (eV)** | 25.03% | **50.06%** | 68.45% | 33.23% | **7.68%** | **15.37%** | 1.438472 | 0.9300 |
| **Total Magnetization (uB)** | 35.15% | **58.58%** | 70.75% | 56.23% | **20.53%** | **34.22%** | 75.297068 | 4.6825 |
| **Energy Above Hull (eV)** | 10.47% | **41.86%** | 79.25% | 9.49% | **10.83%** | **43.30%** | 0.065541 | 0.0907 |
| **Formation Energy (eV/atom)** | 68.20% | **104.92%** | 100.00% | 68.20% | **68.20%** | **104.92%** | 0.110958 | 0.1979 |

---

