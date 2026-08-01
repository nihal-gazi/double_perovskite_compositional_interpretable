# Experiment 17: Tight-Binding Proxies & Mendeleev Feature Engine Summary Report

**Dataset:** `exp_v2/data/data_24_7_2026/double_perovskite_dataset.csv` (2,000 double perovskites)  
**Data Leakage & 3D Audit Compliance:** 100% Pure Compositional Descriptors (Zero 3D atomic coordinates, zero GNN proxies `E_GNN`, `M_net`, `M_abs`).  
**New Quantum & Thermodynamic Descriptors Added:** Tight-Binding Gap Proxy ($\Delta E_{\text{gap}} = \min(IE_B, IE_{B'}) - EA_{\text{O}}$), Mendeleev Scale Number ($\mathcal{M}$) & Mismatch ($\Delta \mathcal{M}_B$), Valence Electron Concentration ($VEC$).  
**Algorithmic Upgrade:** Cost-Sensitive Stage 1 Classifier with Class Penalties and Precision-Recall Threshold Tuning ($\tau^*$).  
**Theoretical Limit References (Literature):** Formation Energy ($R^2_{\text{limit}} = 65.0\%$), Magnetization ($R^2_{\text{limit}} = 60.0\%$), Band Gap ($R^2_{\text{limit}} = 50.0\%$), Hull Energy ($R^2_{\text{limit}} = 25.0\%$).  

---

## Performance Summary Table Across Target Properties

| Target Property | Optimal Architecture | Stage 1 Acc (%) | Stage 2 Sub R² (%) | **Sub R² Limit (%)** | **Final Pipeline R² (%)** | **Theoretical Limit (%)** | Final MSE | Final MAE |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Formation Energy (eV/atom)** | Direct Multi-Operator | 100.00% | 71.24% | **109.59%** | **71.24%** | **109.59%** | 0.100352 | 0.1865 |
| **Total Magnetization (uB)** | Cost-Sensitive Hurdle | 86.90% | 61.38% | **102.30%** | **56.82%** | **94.70%** | 40.913123 | 3.2037 |
| **Band Gap (eV)** | Direct Multi-Operator | 100.00% | 31.23% | **62.46%** | **31.23%** | **62.46%** | 1.071546 | 0.8600 |
| **Energy Above Hull (eV)** | Cost-Sensitive Hurdle | 87.15% | 11.98% | **47.93%** | **14.98%** | **59.92%** | 0.062488 | 0.0838 |

---

