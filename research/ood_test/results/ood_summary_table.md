# 80/20 Train-Test Benchmark Report (5,000 Double Perovskites)

**Dataset:** `exp_v2/data/data_28_7_2026/double_perovskite_dataset_5000.csv` (5,000 double perovskites)  
**Data Split:** 80% Training Set (4,000 samples) / 20% Held-Out Test Set (1,000 samples)  
**Data Source Citation:** [`citation.md`](../../data/data_28_7_2026/citation.md) (Materials Project API key `gWJXczH9PXlsJ4tByN7ilvwJGv0TMnsY`).  
**Data Leakage & 3D Audit:** 100% Pure Compositional Descriptors (Zero 3D atomic coordinates, zero GNN surrogates).  

---

## 80/20 Train vs. Test Performance Summary Table

| Target Property | Architecture | 80% Train Acc (%) | **80% Train R² (%)** | **Train Limit (%)** | 20% Test Acc (%) | **20% Test R² (%)** | **Test Limit (%)** | Test MSE | Test MAE |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Formation Energy (eV/atom)** | direct_multi_operator | 100.00% | **70.95%** | **109.16%** | 100.00% | **65.16%** | **100.25%** | 0.127321 | 0.2133 |
| **Total Magnetization (uB)** | hard_margin_hurdle | 93.53% | **48.78%** | **81.29%** | 75.00% | **-3.89%** | **0.00%** | 55.420880 | 4.3735 |
| **Band Gap (eV)** | soft_gated_regressor | 90.28% | **41.17%** | **82.35%** | 79.40% | **40.37%** | **80.73%** | 0.973627 | 0.8088 |
| **Energy Above Hull (eV)** | hard_margin_hurdle | 94.35% | **17.43%** | **69.72%** | 78.70% | **11.03%** | **44.14%** | 0.076343 | 0.1029 |

---

