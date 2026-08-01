# SOTA Baseline Benchmark Report (5000 Dataset)

**Exact Target Property Tested:** `Formation Energy (eV/atom)`  
**Paper Reference:** SISSO: A compressed-sensing method for identifying the best low-dimensional features in machine learning of materials properties (Runhai Ouyang, Stefano Curtarolo, Emre Ahmetcik, Matthias Scheffler, and Luca M. Ghiringhelli)  
**Publication:** Physical Review Materials 2, 083802 (2018) | DOI: [10.1103/PhysRevMaterials.2.083802](https://doi.org/10.1103/PhysRevMaterials.2.083802)  
**Dataset File:** `double_perovskite_dataset_5000.csv` (5000 materials)  

---

## Table 1: In-Distribution (Full Dataset Fit) Performance

| Target Property Tested | SOTA Paper Algorithm | Dataset Size | In-Sample $R^2$ (%) | Theoretical Limit ($R^2_\text{limit}$) | **Limit Achieved (%)** | Classification Acc (%) | MSE | MAE |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Formation Energy (eV/atom)** | `ouyang_2018_sisso` | 5000 | **48.70%** | 65.0% | **74.93%** | 100.00% | 0.188539 | 0.2871 |

---

## Table 2: Out-of-Distribution (80/20 Train/Test Split, 10 Seeds) Performance

| Target Property Tested | SOTA Paper Algorithm | Dataset | 80% Train $R^2$ | Train Limit Achieved (%) | 20% Test $R^2$ | **Test Limit Achieved (%)** | Test Class. Acc (%) | Test MSE | Test MAE |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Formation Energy (eV/atom)** | `ouyang_2018_sisso` | 5000 | 48.67 $\pm$ 1.10% | **74.87%** | 49.09 $\pm$ 4.59% | **75.53%** | 100.00 $\pm$ 0.00% | 0.181807 | 0.2872 |

---

## Scientific Observations & Evaluation

1. **Exact Property Tested**: **`Formation Energy (eV/atom)`**
2. **SOTA Feature Vector**: Extracted physical descriptors (en_avg, den_B, dr_B, t_goldschmidt, en_B_ratio, t_g_sq, den_B_sq, sqrt_t_g, sqrt_den_B, t_g_x_en_avg, den_B_x_t_g, dr_B_x_t_g, log_t_g, log_en_avg).
3. **In-Distribution vs. OOD Generalization**:
   - In-Distribution fit yields an $R^2$ of **48.70%** (74.93% of limit).
   - 80/20 Out-of-Distribution evaluation yields a test $R^2$ of **49.09 $\pm$ 4.59%** (75.53% of limit).
