# SOTA Baseline Benchmark Report (5000 Dataset)

**Exact Target Property Tested:** `Energy Above Hull (eV)`  
**Paper Reference:** A new tolerance factor for the prediction of perovskite oxides and halides (Christopher J. Bartel, Christopher Sutton, Bryan R. Goldsmith, Runhai Ouyang, Charles B. Musgrave, Luca M. Ghiringhelli, and Matthias Scheffler)  
**Publication:** Nature Communications 10, Article No. 831 (2019) | DOI: [10.1038/s41467-019-08682-f](https://doi.org/10.1038/s41467-019-08682-f)  
**Dataset File:** `double_perovskite_dataset_5000.csv` (5000 materials)  

---

## Table 1: In-Distribution (Full Dataset Fit) Performance

| Target Property Tested | SOTA Paper Algorithm | Dataset Size | In-Sample $R^2$ (%) | Theoretical Limit ($R^2_\text{limit}$) | **Limit Achieved (%)** | Classification Acc (%) | MSE | MAE |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Energy Above Hull (eV)** | `bartel_2019_tau` | 5000 | **0.61%** | 25.0% | **2.45%** | 59.54% | 0.081020 | 0.0976 |

---

## Table 2: Out-of-Distribution (80/20 Train/Test Split, 10 Seeds) Performance

| Target Property Tested | SOTA Paper Algorithm | Dataset | 80% Train $R^2$ | Train Limit Achieved (%) | 20% Test $R^2$ | **Test Limit Achieved (%)** | Test Class. Acc (%) | Test MSE | Test MAE |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Energy Above Hull (eV)** | `bartel_2019_tau` | 5000 | 0.61 $\pm$ 0.09% | **2.43%** | 0.64 $\pm$ 0.63% | **2.54%** | 56.01 $\pm$ 4.29% | 0.073092 | 0.0959 |

---

## Scientific Observations & Evaluation

1. **Exact Property Tested**: **`Energy Above Hull (eV)`**
2. **SOTA Feature Vector**: Extracted physical descriptors (tau_bartel, t_goldschmidt, den_B).
3. **In-Distribution vs. OOD Generalization**:
   - In-Distribution fit yields an $R^2$ of **0.61%** (2.45% of limit).
   - 80/20 Out-of-Distribution evaluation yields a test $R^2$ of **0.64 $\pm$ 0.63%** (2.54% of limit).
