# Experiment 11: Standard Linear Regression Baseline Summary Report

**Dataset:** `exp_v2/data/data_24_7_2026/double_perovskite_dataset.csv` (2,000 double perovskites)  
**Data Leakage Audit:** Removed `E_GNN`, `M_net`, `M_abs`. Evaluated on 33 pure physical/chemical descriptors.  
**Theoretical Limit References (Literature):** Formation Energy ($R^2_{\text{limit}} = 65.0\%$), Magnetization ($R^2_{\text{limit}} = 60.0\%$), Band Gap ($R^2_{\text{limit}} = 50.0\%$), Hull Energy ($R^2_{\text{limit}} = 25.0\%$).  

---

## Performance Summary Table

| Target Property | Direct OLS R² (%) | **Direct Theoretical Limit (%)** | Stage 1 Cls Acc (%) | Stage 2 Sub R² (%) | **Hurdle Pipeline R² (%)** | **Hurdle Theoretical Limit (%)** | Hurdle MSE | Hurdle MAE |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Band Gap (eV)** | 16.33% | **32.65%** | 65.40% | 23.07% | **-8.27%** | **0.00%** | 1.686980 | 1.0469 |
| **Total Magnetization (uB)** | 26.63% | **44.38%** | 69.70% | 46.85% | **15.50%** | **25.84%** | 80.062394 | 5.0366 |
| **Energy Above Hull (eV)** | 6.57% | **26.28%** | 76.35% | 5.04% | **5.41%** | **21.62%** | 0.069524 | 0.0968 |
| **Formation Energy (eV/atom)** | 61.41% | **94.48%** | 100.00% | 61.41% | **61.41%** | **94.48%** | 0.134622 | 0.2202 |

---

