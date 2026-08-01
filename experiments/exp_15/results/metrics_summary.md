# Experiment 15: Target-Specific Optimal Interpretable Master Model Report

**Dataset:** `exp_v2/data/data_24_7_2026/double_perovskite_dataset.csv` (2,000 double perovskites)  
**Data Leakage Audit:** Removed `E_GNN`, `M_net`, `M_abs`. Evaluated on 33 pure physical descriptors expanded with multi-operator terms.  
**Theoretical Limit References (Literature):** Formation Energy ($R^2_{\text{limit}} = 65.0\%$), Magnetization ($R^2_{\text{limit}} = 60.0\%$), Band Gap ($R^2_{\text{limit}} = 50.0\%$), Hull Energy ($R^2_{\text{limit}} = 25.0\%$).  

---

## Master Performance Benchmark Table Across Target Properties

| Target Property | Master Optimal Architecture | Stage 1 Acc (%) | Stage 2 Sub R² (%) | **Sub R² Limit (%)** | **Final Master R² (%)** | **Master Theoretical Limit (%)** | Master MSE | Master MAE |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Formation Energy (eV/atom)** | Direct Multi-Operator | 100.00% | 69.61% | **107.10%** | **69.61%** | **107.10%** | 0.106012 | 0.1914 |
| **Total Magnetization (uB)** | Non-Linear Hurdle | 83.00% | 58.79% | **97.98%** | **50.80%** | **84.66%** | 46.620004 | 3.5750 |
| **Band Gap (eV)** | Direct Multi-Operator | 100.00% | 29.10% | **58.19%** | **29.10%** | **58.19%** | 1.104798 | 0.8786 |
| **Energy Above Hull (eV)** | Non-Linear Hurdle | 85.20% | 10.44% | **41.76%** | **13.58%** | **54.32%** | 0.063516 | 0.0832 |

---

