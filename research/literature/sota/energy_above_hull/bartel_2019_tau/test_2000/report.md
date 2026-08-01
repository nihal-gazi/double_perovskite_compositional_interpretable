# SOTA Baseline Benchmark Report (2000 Dataset)

**Exact Target Property Tested:** `Energy Above Hull (eV)`  
**Paper Reference:** A new tolerance factor for the prediction of perovskite oxides and halides (Christopher J. Bartel, Christopher Sutton, Bryan R. Goldsmith, Runhai Ouyang, Charles B. Musgrave, Luca M. Ghiringhelli, and Matthias Scheffler)  
**Publication:** Nature Communications 10, Article No. 831 (2019) | DOI: [10.1038/s41467-019-08682-f](https://doi.org/10.1038/s41467-019-08682-f)  
**Dataset File:** `double_perovskite_dataset.csv` (2000 materials)  

---

## Table 1: In-Distribution (Full Dataset Fit) Performance

| Target Property Tested | SOTA Paper Algorithm | Dataset Size | In-Sample $R^2$ (%) | Theoretical Limit ($R^2_\text{limit}$) | **Limit Achieved (%)** | Classification Acc (%) | MSE | MAE |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Energy Above Hull (eV)** | `bartel_2019_tau` | 2000 | **0.41%** | 25.0% | **1.66%** | 60.30% | 0.073192 | 0.0962 |

---

## Table 2: Out-of-Distribution (80/20 Train/Test Split, 10 Seeds) Performance

| Target Property Tested | SOTA Paper Algorithm | Dataset | 80% Train $R^2$ | Train Limit Achieved (%) | 20% Test $R^2$ | **Test Limit Achieved (%)** | Test Class. Acc (%) | Test MSE | Test MAE |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Energy Above Hull (eV)** | `bartel_2019_tau` | 2000 | 0.44 $\pm$ 0.11% | **1.75%** | 0.23 $\pm$ 0.49% | **0.93%** | 62.10 $\pm$ 3.62% | 0.073505 | 0.0969 |

---

## Scientific Observations & Evaluation

1. **Exact Property Tested**: **`Energy Above Hull (eV)`**
2. **SOTA Feature Vector**: Extracted physical descriptors (tau_bartel, t_goldschmidt, den_B).
3. **In-Distribution vs. OOD Generalization**:
   - In-Distribution fit yields an $R^2$ of **0.41%** (1.66% of limit).
   - 80/20 Out-of-Distribution evaluation yields a test $R^2$ of **0.23 $\pm$ 0.49%** (0.93% of limit).
