# SOTA Baseline Benchmark Report (5000 Dataset)

**Exact Target Property Tested:** `Band Gap (eV)`  
**Paper Reference:** Large-Scale Benchmark of Exchange-Correlation Functionals for the Determination of Electronic Band Gaps of Solids (Pedro Borlido, Tilak Aull, Antonio W. H. Da Silva, Silvana Botti, and Miguel A. L. Marques)  
**Publication:** Journal of Chemical Theory and Computation 15, 5069-5793 (2019) | DOI: [10.1021/acs.jctc.9b00322](https://doi.org/10.1021/acs.jctc.9b00322)  
**Dataset File:** `double_perovskite_dataset_5000.csv` (5000 materials)  

---

## Table 1: In-Distribution (Full Dataset Fit) Performance

| Target Property Tested | SOTA Paper Algorithm | Dataset Size | In-Sample $R^2$ (%) | Theoretical Limit ($R^2_\text{limit}$) | **Limit Achieved (%)** | Classification Acc (%) | MSE | MAE |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Band Gap (eV)** | `borlido_2019_sisso` | 5000 | **0.89%** | 50.0% | **1.79%** | 78.22% | 1.591818 | 1.0577 |

---

## Table 2: Out-of-Distribution (80/20 Train/Test Split, 10 Seeds) Performance

| Target Property Tested | SOTA Paper Algorithm | Dataset | 80% Train $R^2$ | Train Limit Achieved (%) | 20% Test $R^2$ | **Test Limit Achieved (%)** | Test Class. Acc (%) | Test MSE | Test MAE |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Band Gap (eV)** | `borlido_2019_sisso` | 5000 | 0.77 $\pm$ 0.24% | **1.54%** | 0.40 $\pm$ 1.19% | **0.80%** | 78.47 $\pm$ 0.76% | 1.612913 | 1.0647 |

---

## Scientific Observations & Evaluation

1. **Exact Property Tested**: **`Band Gap (eV)`**
2. **SOTA Feature Vector**: Extracted physical descriptors (den_BO_pow, d_elec_pow, en_avg_sq, log_d_elec).
3. **In-Distribution vs. OOD Generalization**:
   - In-Distribution fit yields an $R^2$ of **0.89%** (1.79% of limit).
   - 80/20 Out-of-Distribution evaluation yields a test $R^2$ of **0.40 $\pm$ 1.19%** (0.80% of limit).
