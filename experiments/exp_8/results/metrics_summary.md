# Experiment 8: Dual Symbolic Regression Hurdle Architecture with Power Operator (pow) Summary Report (Clean Physical Descriptors)

**Dataset:** `exp_v2/data/data_24_7_2026/double_perovskite_dataset.csv` (2,000 double perovskites)  
**Data Leakage Audit:** Removed `E_GNN`, `M_net`, `M_abs`. Evaluated on 33 pure physical/chemical descriptors.  
**Theoretical Limit References (Literature):** Formation Energy ($R^2_{\text{limit}} = 65.0\%$), Magnetization ($R^2_{\text{limit}} = 60.0\%$), Band Gap ($R^2_{\text{limit}} = 50.0\%$), Hull Energy ($R^2_{\text{limit}} = 25.0\%$).  

---

## Performance Summary Table

| Target Property | Stage 1 Cls Acc (%) | Stage 1 F1 | Stage 2 Sub R² (%) | **Final Pipeline R² (%)** | **Theoretical Limit (%)** | Final MSE | Final MAE |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Band Gap (eV)** | 64.15% | 0.7583 | 15.14% | **-13.18%** | **0.00%** | 1.763539 | 1.0838 |
| **Total Magnetization (uB)** | 63.90% | 0.7255 | 6.89% | **4.83%** | **8.06%** | 90.172784 | 4.8052 |
| **Energy Above Hull (eV)** | 71.45% | 0.8167 | -1.37% | **0.09%** | **0.37%** | 0.073429 | 0.0927 |
| **Formation Energy (eV/atom)** | 100.00% | 1.0000 | 16.55% | **16.55%** | **25.46%** | 0.291136 | 0.3522 |

---
