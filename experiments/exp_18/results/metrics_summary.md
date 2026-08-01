# Experiment 18: Quantum Power Laws & Birch-Murnaghan Strain Engine Summary Report

**Dataset:** `exp_v2/data/data_24_7_2026/double_perovskite_dataset.csv` (2,000 double perovskites)  
**Data Leakage & 3D Audit Compliance:** 100% Pure Compositional Descriptors (Zero 3D atomic coordinates, zero GNN proxies `E_GNN`, `M_net`, `M_abs`).  
**New Physical Descriptors Added:** Harrison Quantum Gap ($E_{\text{gap, QM}} = \sqrt{\Delta E_{\text{gap}}^2 + d_{\text{ideal}}^{-4}}$), Birch-Murnaghan Strain Proxies ($E_{\text{tolerance\_strain}}, E_{\text{oct\_distortion\_strain}}, \Delta V_{\text{packing\_strain}}$), Fractional Power Laws.  
**Algorithmic Upgrade:** High-C ($C=50.0$) Hard-Margin Stage 1 Classifier with F1 Threshold Tuning ($\tau^*$).  
**Theoretical Limit References (Literature):** Formation Energy ($R^2_{\text{limit}} = 65.0\%$), Magnetization ($R^2_{\text{limit}} = 60.0\%$), Band Gap ($R^2_{\text{limit}} = 50.0\%$), Hull Energy ($R^2_{\text{limit}} = 25.0\%$).  

---

## Performance Summary Table Across Target Properties

| Target Property | Optimal Architecture | Stage 1 Acc (%) | Stage 2 Sub R² (%) | **Sub R² Limit (%)** | **Final Pipeline R² (%)** | **Theoretical Limit (%)** | Final MSE | Final MAE |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Formation Energy (eV/atom)** | Direct Multi-Operator | 100.00% | 71.09% | **109.37%** | **71.09%** | **109.37%** | 0.100865 | 0.1880 |
| **Total Magnetization (uB)** | Hard-Margin Hurdle | 89.75% | 61.19% | **101.99%** | **59.69%** | **99.49%** | 38.191558 | 3.1995 |
| **Band Gap (eV)** | Direct Multi-Operator | 100.00% | 30.98% | **61.96%** | **30.98%** | **61.96%** | 1.075492 | 0.8596 |
| **Energy Above Hull (eV)** | Hard-Margin Hurdle | 91.40% | 11.97% | **47.88%** | **15.92%** | **63.69%** | 0.061794 | 0.0792 |

---

