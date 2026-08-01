# Experiment 14: 100% Fully Interpretable Multi-Operator Hurdle Model Summary Report

**Dataset:** `exp_v2/data/data_24_7_2026/double_perovskite_dataset.csv` (2,000 double perovskites)  
**Data Leakage Audit:** Removed `E_GNN`, `M_net`, `M_abs`. Evaluated on 33 pure physical descriptors expanded with multi-operator terms (roots, logs, squares, interactions, ratios, 3rd-order triplets).  
**Stage 1 Decision Boundary Classifier:** 100% Analytical Log-Odds Decision Boundary ($S_{\text{cls}}(\mathbf{x}) > \tau^*$) with F1-Threshold Tuning  
**Stage 2 Regressor:** 100% Analytical Physical Interaction Regressor (RIDGE)  
**Theoretical Limit References (Literature):** Formation Energy ($R^2_{\text{limit}} = 65.0\%$), Magnetization ($R^2_{\text{limit}} = 60.0\%$), Band Gap ($R^2_{\text{limit}} = 50.0\%$), Hull Energy ($R^2_{\text{limit}} = 25.0\%$).  

---

## Performance Summary Table

| Target Property | Stage 1 Analytical Acc (%) | Stage 1 F1 | Stage 2 Sub R² (%) | Direct Interaction R² (%) | **Hurdle Pipeline R² (%)** | **Hurdle Theoretical Limit (%)** | Hurdle MSE | Hurdle MAE |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Band Gap (eV)** | **68.20%** | 0.7870 | 36.70% | 28.84% | **8.11%** | **16.21%** | 1.431863 | 0.9479 |
| **Total Magnetization (uB)** | **72.30%** | 0.7795 | 58.83% | 37.23% | **28.40%** | **47.33%** | 67.847699 | 4.6111 |
| **Energy Above Hull (eV)** | **80.30%** | 0.8680 | 10.49% | 11.72% | **11.96%** | **47.83%** | 0.064709 | 0.0897 |
| **Formation Energy (eV/atom)** | **100.00%** | 1.0000 | 69.61% | 69.61% | **69.61%** | **107.10%** | 0.106012 | 0.1914 |

---

