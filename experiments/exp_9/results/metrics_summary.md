# Experiment 9: Extended Dual Symbolic Regression Hurdle Architecture (19 Operators) Summary Report (Clean Physical Descriptors)

**Dataset:** `exp_v2/data/data_24_7_2026/double_perovskite_dataset.csv` (2,000 double perovskites)  
**Data Leakage Audit:** Removed `E_GNN`, `M_net`, `M_abs`. Evaluated on 33 pure physical/chemical descriptors.  
**Theoretical Limit References (Literature):** Formation Energy ($R^2_{\text{limit}} = 65.0\%$), Magnetization ($R^2_{\text{limit}} = 60.0\%$), Band Gap ($R^2_{\text{limit}} = 50.0\%$), Hull Energy ($R^2_{\text{limit}} = 25.0\%$).  

---

## Performance Summary Table

| Target Property | Stage 1 Cls Acc (%) | Stage 1 F1 | Stage 2 Sub R² (%) | **Final Pipeline R² (%)** | **Theoretical Limit (%)** | Final MSE | Final MAE |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Band Gap (eV)** | 63.80% | 0.7736 | 27.82% | **-8.61%** | **0.00%** | 1.692378 | 1.0628 |
| **Total Magnetization (uB)** | 63.00% | 0.6463 | 35.44% | **-4.27%** | **0.00%** | 98.796864 | 4.7329 |
| **Energy Above Hull (eV)** | 72.20% | 0.8305 | -5.27% | **-1.39%** | **0.00%** | 0.074519 | 0.0853 |
| **Formation Energy (eV/atom)** | 100.00% | 1.0000 | 28.56% | **28.56%** | **43.94%** | 0.249223 | 0.3543 |

---
