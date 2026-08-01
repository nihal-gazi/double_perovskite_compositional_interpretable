# Experiment 7: Dual Symbolic Regression Hurdle Architecture Summary Report (Clean Physical Descriptors)

**Dataset:** `exp_v2/data/data_24_7_2026/double_perovskite_dataset.csv` (2,000 double perovskites)  
**Data Leakage Audit:** Removed `E_GNN`, `M_net`, `M_abs`. Evaluated on 33 pure physical/chemical descriptors.  
**Theoretical Limit References (Literature):** Formation Energy ($R^2_{\text{limit}} = 65.0\%$), Magnetization ($R^2_{\text{limit}} = 60.0\%$), Band Gap ($R^2_{\text{limit}} = 50.0\%$), Hull Energy ($R^2_{\text{limit}} = 25.0\%$).  

---

## Performance Summary Table

| Target Property | Stage 1 Cls Acc (%) | Stage 1 F1 | Stage 2 Sub R² (%) | **Final Pipeline R² (%)** | **Theoretical Limit (%)** | Final MSE | Final MAE |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Band Gap (eV)** | 63.25% | 0.7637 | 7.29% | **-18.59%** | **0.00%** | 1.847809 | 1.1493 |
| **Total Magnetization (uB)** | 62.80% | 0.7062 | -0.29% | **0.16%** | **0.26%** | 94.603435 | 5.0762 |
| **Energy Above Hull (eV)** | 72.45% | 0.8328 | -1.37% | **0.15%** | **0.59%** | 0.073389 | 0.0953 |
| **Formation Energy (eV/atom)** | 100.00% | 1.0000 | 3.02% | **3.02%** | **4.65%** | 0.338330 | 0.4168 |

---
