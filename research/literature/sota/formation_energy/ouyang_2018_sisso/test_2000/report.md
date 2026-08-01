# SOTA Baseline Benchmark Report (2000 Dataset)

**Exact Target Property Tested:** `Formation Energy (eV/atom)`  
**Paper Reference:** SISSO: A compressed-sensing method for identifying the best low-dimensional features in machine learning of materials properties (Runhai Ouyang, Stefano Curtarolo, Emre Ahmetcik, Matthias Scheffler, and Luca M. Ghiringhelli)  
**Publication:** Physical Review Materials 2, 083802 (2018) | DOI: [10.1103/PhysRevMaterials.2.083802](https://doi.org/10.1103/PhysRevMaterials.2.083802)  
**Dataset File:** `double_perovskite_dataset.csv` (2000 materials)  

---

## Table 1: In-Distribution (Full Dataset Fit) Performance

| Target Property Tested | SOTA Paper Algorithm | Dataset Size | In-Sample $R^2$ (%) | Theoretical Limit ($R^2_\text{limit}$) | **Limit Achieved (%)** | Classification Acc (%) | MSE | MAE |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Formation Energy (eV/atom)** | `ouyang_2018_sisso` | 2000 | **48.31%** | 65.0% | **74.32%** | 100.00% | 0.180349 | 0.2850 |

---

## Table 2: Out-of-Distribution (80/20 Train/Test Split, 10 Seeds) Performance

| Target Property Tested | SOTA Paper Algorithm | Dataset | 80% Train $R^2$ | Train Limit Achieved (%) | 20% Test $R^2$ | **Test Limit Achieved (%)** | Test Class. Acc (%) | Test MSE | Test MAE |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Formation Energy (eV/atom)** | `ouyang_2018_sisso` | 2000 | 48.33 $\pm$ 1.48% | **74.35%** | 48.26 $\pm$ 6.67% | **74.24%** | 100.00 $\pm$ 0.00% | 0.181802 | 0.2859 |

---

## Scientific Observations & Evaluation

1. **Exact Property Tested**: **`Formation Energy (eV/atom)`**
2. **SOTA Feature Vector**: Extracted physical descriptors (en_avg, den_B, dr_B, t_goldschmidt, en_B_ratio, t_g_sq, den_B_sq, sqrt_t_g, sqrt_den_B, t_g_x_en_avg, den_B_x_t_g, dr_B_x_t_g, log_t_g, log_en_avg).
3. **In-Distribution vs. OOD Generalization**:
   - In-Distribution fit yields an $R^2$ of **48.31%** (74.32% of limit).
   - 80/20 Out-of-Distribution evaluation yields a test $R^2$ of **48.26 $\pm$ 6.67%** (74.24% of limit).
