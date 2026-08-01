# ood_test_2 Benchmark Report: 80/20 Split on Original 2,000 Dataset (Seed = 42)

**Dataset:** `exp_v2/data/data_24_7_2026/double_perovskite_dataset.csv` (2,000 double perovskites)  
**Data Split:** 80% Training Set (1,600 samples) / 20% Held-Out Test Set (400 samples) | `seed=42`  
**Data Leakage & 3D Audit:** 100% Pure Compositional Descriptors (Zero 3D atomic coordinates, zero GNN surrogates).  

---

## 80/20 Train vs. Test Performance Summary Table

| Target Property | Architecture | 80% Train Acc (%) | **80% Train R² (%)** | **Train Limit (%)** | 20% Test Acc (%) | **20% Test R² (%)** | **Test Limit (%)** | Test MSE | Test MAE |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Formation Energy (eV/atom)** | direct_multi_operator | 100.00% | **69.96%** | **107.64%** | 100.00% | **75.01%** | **115.40%** | 0.087921 | 0.1956 |
| **Total Magnetization (uB)** | hard_margin_hurdle | 93.00% | **62.60%** | **104.33%** | 76.25% | **30.31%** | **50.51%** | 53.336908 | 3.9218 |
| **Band Gap (eV)** | soft_gated_regressor | 88.25% | **50.18%** | **100.36%** | 74.75% | **41.07%** | **82.14%** | 0.901101 | 0.7718 |
| **Energy Above Hull (eV)** | hard_margin_hurdle | 94.06% | **16.71%** | **66.83%** | 84.00% | **7.30%** | **29.21%** | 0.045380 | 0.0852 |

---

