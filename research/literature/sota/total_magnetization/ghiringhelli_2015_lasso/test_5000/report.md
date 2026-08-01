# SOTA Baseline Benchmark Report (5000 Dataset)

**Exact Target Property Tested:** `Total Magnetization (uB)`  
**Paper Reference:** Big Data of Materials Science: Critical Role of the Compressed Sensing Feature Selection for Classification of Crystal Structures (Luca M. Ghiringhelli, Jan Vybiral, Sergey V. Levchenko, Claudia Draxl, and Matthias Scheffler)  
**Publication:** Physical Review Letters 114, 105503 (2015) | DOI: [10.1103/PhysRevLett.114.105503](https://doi.org/10.1103/PhysRevLett.114.105503)  
**Dataset File:** `double_perovskite_dataset_5000.csv` (5000 materials)  

---

## Table 1: In-Distribution (Full Dataset Fit) Performance

| Target Property Tested | SOTA Paper Algorithm | Dataset Size | In-Sample $R^2$ (%) | Theoretical Limit ($R^2_\text{limit}$) | **Limit Achieved (%)** | Classification Acc (%) | MSE | MAE |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Total Magnetization (uB)** | `ghiringhelli_2015_lasso` | 5000 | **3.12%** | 60.0% | **5.19%** | 74.38% | 80.543322 | 5.3970 |

---

## Table 2: Out-of-Distribution (80/20 Train/Test Split, 10 Seeds) Performance

| Target Property Tested | SOTA Paper Algorithm | Dataset | 80% Train $R^2$ | Train Limit Achieved (%) | 20% Test $R^2$ | **Test Limit Achieved (%)** | Test Class. Acc (%) | Test MSE | Test MAE |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Total Magnetization (uB)** | `ghiringhelli_2015_lasso` | 5000 | 3.23 $\pm$ 0.21% | **5.38%** | 2.24 $\pm$ 0.95% | **3.74%** | 73.96 $\pm$ 1.29% | 82.301836 | 5.4414 |

---

## Scientific Observations & Evaluation

1. **Exact Property Tested**: **`Total Magnetization (uB)`**
2. **SOTA Feature Vector**: Extracted physical descriptors (hs_B, hs_Bprime, total_fim, vec, den_B, fim_x_vec, fim_x_den_B, vec_sq, fim_sq, sqrt_fim, log_fim).
3. **In-Distribution vs. OOD Generalization**:
   - In-Distribution fit yields an $R^2$ of **3.12%** (5.19% of limit).
   - 80/20 Out-of-Distribution evaluation yields a test $R^2$ of **2.24 $\pm$ 0.95%** (3.74% of limit).
