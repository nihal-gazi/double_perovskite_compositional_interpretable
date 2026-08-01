# SOTA Baseline Benchmark Report (2000 Dataset)

**Exact Target Property Tested:** `Total Magnetization (uB)`  
**Paper Reference:** Big Data of Materials Science: Critical Role of the Compressed Sensing Feature Selection for Classification of Crystal Structures (Luca M. Ghiringhelli, Jan Vybiral, Sergey V. Levchenko, Claudia Draxl, and Matthias Scheffler)  
**Publication:** Physical Review Letters 114, 105503 (2015) | DOI: [10.1103/PhysRevLett.114.105503](https://doi.org/10.1103/PhysRevLett.114.105503)  
**Dataset File:** `double_perovskite_dataset.csv` (2000 materials)  

---

## Table 1: In-Distribution (Full Dataset Fit) Performance

| Target Property Tested | SOTA Paper Algorithm | Dataset Size | In-Sample $R^2$ (%) | Theoretical Limit ($R^2_\text{limit}$) | **Limit Achieved (%)** | Classification Acc (%) | MSE | MAE |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Total Magnetization (uB)** | `ghiringhelli_2015_lasso` | 2000 | **1.70%** | 60.0% | **2.84%** | 68.50% | 93.141243 | 5.6535 |

---

## Table 2: Out-of-Distribution (80/20 Train/Test Split, 10 Seeds) Performance

| Target Property Tested | SOTA Paper Algorithm | Dataset | 80% Train $R^2$ | Train Limit Achieved (%) | 20% Test $R^2$ | **Test Limit Achieved (%)** | Test Class. Acc (%) | Test MSE | Test MAE |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Total Magnetization (uB)** | `ghiringhelli_2015_lasso` | 2000 | 3.71 $\pm$ 0.69% | **6.18%** | 1.89 $\pm$ 2.18% | **3.15%** | 67.58 $\pm$ 1.21% | 100.143381 | 5.6287 |

---

## Scientific Observations & Evaluation

1. **Exact Property Tested**: **`Total Magnetization (uB)`**
2. **SOTA Feature Vector**: Extracted physical descriptors (hs_B, hs_Bprime, total_fim, vec, den_B, fim_x_vec, fim_x_den_B, vec_sq, fim_sq, sqrt_fim, log_fim).
3. **In-Distribution vs. OOD Generalization**:
   - In-Distribution fit yields an $R^2$ of **1.70%** (2.84% of limit).
   - 80/20 Out-of-Distribution evaluation yields a test $R^2$ of **1.89 $\pm$ 2.18%** (3.15% of limit).
