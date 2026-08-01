# Experiment 13: Non-Linear Decision Boundary Hurdle Model Summary Report

**Dataset:** `exp_v2/data/data_24_7_2026/double_perovskite_dataset.csv` (2,000 double perovskites)  
**Data Leakage Audit:** Removed `E_GNN`, `M_net`, `M_abs`. Evaluated on 33 pure physical descriptors expanded with 2nd-order interaction terms ($x_i x_j$, $x_i/x_j$, $x_i^2$).  
**Stage 1 Decision Boundary Classifier:** Non-Linear RBF_SVC Classifier  
**Stage 2 Regressor:** Regularized Physical Interaction Regressor (RIDGE)  
**Theoretical Limit References (Literature):** Formation Energy ($R^2_{\text{limit}} = 65.0\%$), Magnetization ($R^2_{\text{limit}} = 60.0\%$), Band Gap ($R^2_{\text{limit}} = 50.0\%$), Hull Energy ($R^2_{\text{limit}} = 25.0\%$).  

---

## Performance Summary Table

| Target Property | Stage 1 Non-Linear Acc (%) | Stage 1 F1 | Stage 2 Sub R² (%) | Direct Interaction R² (%) | **Hurdle Pipeline R² (%)** | **Hurdle Theoretical Limit (%)** | Hurdle MSE | Hurdle MAE |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Band Gap (eV)** | **78.25%** | 0.8405 | 33.23% | 25.03% | **27.19%** | **54.37%** | 1.134573 | 0.7792 |
| **Total Magnetization (uB)** | **81.90%** | 0.8391 | 56.23% | 35.15% | **49.87%** | **83.12%** | 47.497219 | 3.6167 |
| **Energy Above Hull (eV)** | **84.50%** | 0.8930 | 9.49% | 10.47% | **12.34%** | **49.37%** | 0.064425 | 0.0854 |
| **Formation Energy (eV/atom)** | **100.00%** | 1.0000 | 68.20% | 68.20% | **68.20%** | **104.92%** | 0.110958 | 0.1979 |

---

