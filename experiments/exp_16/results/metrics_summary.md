# Experiment 16: Compositional Physical Mismatch & Ionicity-Enhanced Pipeline Summary Report

**Dataset:** `exp_v2/data/data_24_7_2026/double_perovskite_dataset.csv` (2,000 double perovskites)  
**Data Leakage & 3D Audit Compliance:** 100% Pure Compositional Descriptors (Zero 3D atomic coordinates, zero DFT-relaxed 3D bond vectors, zero GNN proxies `E_GNN`, `M_net`, `M_abs`).  
**New Compositional Features Added:** Electronegativity Mismatches ($\Delta\chi_B, \Delta\chi_{AB}$), Phillips Ionicity Index ($f_i$), Ferrimagnetic Spin Difference ($\Delta HS$), Valence Mismatch ($\Delta\text{Val}_B$), Radii Mismatch ($\Delta r_B$).  
**Theoretical Limit References (Literature):** Formation Energy ($R^2_{\text{limit}} = 65.0\%$), Magnetization ($R^2_{\text{limit}} = 60.0\%$), Band Gap ($R^2_{\text{limit}} = 50.0\%$), Hull Energy ($R^2_{\text{limit}} = 25.0\%$).  

---

## Performance Summary Table Across Target Properties

| Target Property | Optimal Architecture | Stage 1 Acc (%) | Stage 2 Sub R² (%) | **Sub R² Limit (%)** | **Final Pipeline R² (%)** | **Theoretical Limit (%)** | Final MSE | Final MAE |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Formation Energy (eV/atom)** | Direct Multi-Operator | 100.00% | 71.24% | **109.60%** | **71.24%** | **109.60%** | 0.100330 | 0.1849 |
| **Total Magnetization (uB)** | Non-Linear Hurdle | 84.50% | 61.93% | **103.21%** | **53.23%** | **88.72%** | 44.316210 | 3.4740 |
| **Band Gap (eV)** | Direct Multi-Operator | 100.00% | 31.23% | **62.47%** | **31.23%** | **62.47%** | 1.071488 | 0.8596 |
| **Energy Above Hull (eV)** | Non-Linear Hurdle | 85.75% | 11.83% | **47.32%** | **14.96%** | **59.85%** | 0.062500 | 0.0828 |

---

