# SOTA Literature Baseline Master Benchmark Summary

This report presents the exact replication and execution of SOTA literature baseline algorithms on both the **2,000 dataset** and **5,000 dataset** across all 4 target properties, evaluated under both **In-Distribution (Full Fit)** and **Out-of-Distribution (80/20 Train/Test Split over 10 Seeds)** protocols.

---

## Table 1: In-Distribution (Full Dataset Fit) SOTA Baseline Performance

| Target Property Tested | Paper Reference Algorithm | Dataset | In-Sample R² (%) | Literature Limit (R²_limit) | **Limit Achieved (%)** | Classification Acc (%) | MSE | MAE |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Formation Energy (eV/atom)** | `ouyang_2018_sisso` | 2000 | **48.31%** | 65.0% | **74.32%** | 100.00% | 0.180349 | 0.2850 |
| **Formation Energy (eV/atom)** | `ouyang_2018_sisso` | 5000 | **48.70%** | 65.0% | **74.93%** | 100.00% | 0.188539 | 0.2871 |
| **Total Magnetization (uB)** | `ghiringhelli_2015_lasso` | 2000 | **1.70%** | 60.0% | **2.84%** | 68.50% | 93.141243 | 5.6535 |
| **Total Magnetization (uB)** | `ghiringhelli_2015_lasso` | 5000 | **3.12%** | 60.0% | **5.19%** | 74.38% | 80.543322 | 5.3970 |
| **Band Gap (eV)** | `borlido_2019_sisso` | 2000 | **-6.77%** | 50.0% | **0.00%** | 62.50% | 1.663627 | 1.0480 |
| **Band Gap (eV)** | `borlido_2019_sisso` | 5000 | **0.89%** | 50.0% | **1.79%** | 78.22% | 1.591818 | 1.0577 |
| **Energy Above Hull (eV)** | `bartel_2019_tau` | 2000 | **0.41%** | 25.0% | **1.66%** | 60.30% | 0.073192 | 0.0962 |
| **Energy Above Hull (eV)** | `bartel_2019_tau` | 5000 | **0.61%** | 25.0% | **2.45%** | 59.54% | 0.081020 | 0.0976 |

---

## Table 2: Out-of-Distribution (80/20 Train/Test Split, 10 Seeds) SOTA Baseline Performance

| Target Property Tested | Paper Reference Algorithm | Dataset | 80% Train R² (%) | Train Limit Achieved (%) | 20% Test R² (%) | **Test Limit Achieved (%)** | Test Class. Acc (%) | Test MSE | Test MAE |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Formation Energy (eV/atom)** | `ouyang_2018_sisso` | 2000 | 48.33 ± 1.48% | **74.35%** | 48.26 ± 6.67% | **74.24%** | 100.00 ± 0.00% | 0.181802 | 0.2859 |
| **Formation Energy (eV/atom)** | `ouyang_2018_sisso` | 5000 | 48.67 ± 1.10% | **74.87%** | 49.09 ± 4.59% | **75.53%** | 100.00 ± 0.00% | 0.181807 | 0.2872 |
| **Total Magnetization (uB)** | `ghiringhelli_2015_lasso` | 2000 | 3.71 ± 0.69% | **6.18%** | 1.89 ± 2.18% | **3.15%** | 67.58 ± 1.21% | 100.143381 | 5.6287 |
| **Total Magnetization (uB)** | `ghiringhelli_2015_lasso` | 5000 | 3.23 ± 0.21% | **5.38%** | 2.24 ± 0.95% | **3.74%** | 73.96 ± 1.29% | 82.301836 | 5.4414 |
| **Band Gap (eV)** | `borlido_2019_sisso` | 2000 | -6.34 ± 0.48% | **0.00%** | -6.86 ± 3.54% | **0.00%** | 62.07 ± 2.33% | 1.620071 | 1.0403 |
| **Band Gap (eV)** | `borlido_2019_sisso` | 5000 | 0.77 ± 0.24% | **1.54%** | 0.40 ± 1.19% | **0.80%** | 78.47 ± 0.76% | 1.612913 | 1.0647 |
| **Energy Above Hull (eV)** | `bartel_2019_tau` | 2000 | 0.44 ± 0.11% | **1.75%** | 0.23 ± 0.49% | **0.93%** | 62.10 ± 3.62% | 0.073505 | 0.0969 |
| **Energy Above Hull (eV)** | `bartel_2019_tau` | 5000 | 0.61 ± 0.09% | **2.43%** | 0.64 ± 0.63% | **2.54%** | 56.01 ± 4.29% | 0.073092 | 0.0959 |

---

