# Master Algorithm Systematic Ablation Study Report

**Dataset:** `exp_v2/data/data_24_7_2026/double_perovskite_dataset.csv` (2,000 double perovskites)  
**Data Leakage Audit:** 100% Pure Compositional Descriptors (Zero 3D atomic coordinates, zero GNN surrogates).  

---

## Target Property: Formation Energy (eV/atom)

**Literature Theoretical Ceiling ($R^2_{\text{limit}}$):** 65.0%

| Code | Condition Name | Description | Stage 1 Acc (%) | Stage 2 Sub R² (%) | **Final Pipeline R² (%)** | **Theoretical Limit (%)** | MSE | MAE |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| C0 | Baseline_Classical | Classical 0D Features Only | 100.00% | 67.93% | **67.93%** | **104.50%** | 0.111892 | 0.2049 |
| C1 | +Harrison_Quantum_Gap | C0 + Tight-Binding Quantum Gap (E_gap,QM) | 100.00% | 67.93% | **67.93%** | **104.50%** | 0.111892 | 0.2049 |
| C2 | +Birch_Murnaghan_Strain | C1 + Thermodynamic Strain Engine | 100.00% | 68.01% | **68.01%** | **104.63%** | 0.111616 | 0.2046 |
| C3 | +Octahedral_d0_d10 | C2 + Closed-Shell Crystal Field Engine | 100.00% | 68.49% | **68.49%** | **105.37%** | 0.109925 | 0.2026 |
| C4 | +Single_Perov_TieLines | C3 + Single-Perovskite Convex Hull Tie-Lines | 100.00% | 68.52% | **68.52%** | **105.41%** | 0.109836 | 0.2023 |
| C5 | Direct_Linear_No_Hurdle | All Features (C4) + Single-Stage Ridge Only | 100.00% | 68.52% | **68.52%** | **105.41%** | 0.109836 | 0.2023 |
| C6 | Hard_Step_Hurdle | All Features (C4) + Hard Binary Step Function | 100.00% | 68.52% | **68.52%** | **105.41%** | 0.109836 | 0.2023 |
| C7 | **Master_Capstone_Full** | Complete Master Capstone Algorithm | 100.00% | 71.26% | **71.26%** | **109.62%** | 0.100281 | 0.1870 |

---

## Target Property: Total Magnetization (uB)

**Literature Theoretical Ceiling ($R^2_{\text{limit}}$):** 60.0%

| Code | Condition Name | Description | Stage 1 Acc (%) | Stage 2 Sub R² (%) | **Final Pipeline R² (%)** | **Theoretical Limit (%)** | MSE | MAE |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| C0 | Baseline_Classical | Classical 0D Features Only | 90.10% | 57.03% | **56.14%** | **93.57%** | 41.555822 | 3.1758 |
| C1 | +Harrison_Quantum_Gap | C0 + Tight-Binding Quantum Gap (E_gap,QM) | 90.10% | 57.03% | **56.14%** | **93.57%** | 41.555822 | 3.1758 |
| C2 | +Birch_Murnaghan_Strain | C1 + Thermodynamic Strain Engine | 90.20% | 57.21% | **57.94%** | **96.57%** | 39.849585 | 3.1510 |
| C3 | +Octahedral_d0_d10 | C2 + Closed-Shell Crystal Field Engine | 89.85% | 57.93% | **58.22%** | **97.03%** | 39.589189 | 3.1441 |
| C4 | +Single_Perov_TieLines | C3 + Single-Perovskite Convex Hull Tie-Lines | 89.55% | 57.98% | **57.94%** | **96.56%** | 39.854423 | 3.1679 |
| C5 | Direct_Linear_No_Hurdle | All Features (C4) + Single-Stage Ridge Only | 100.00% | 36.53% | **36.53%** | **60.88%** | 60.144618 | 4.5356 |
| C6 | Hard_Step_Hurdle | All Features (C4) + Hard Binary Step Function | 89.55% | 57.98% | **57.94%** | **96.56%** | 39.854423 | 3.1679 |
| C7 | **Master_Capstone_Full** | Complete Master Capstone Algorithm | 92.80% | 61.75% | **62.23%** | **103.72%** | 35.788531 | 3.0011 |

---

## Target Property: Band Gap (eV)

**Literature Theoretical Ceiling ($R^2_{\text{limit}}$):** 50.0%

| Code | Condition Name | Description | Stage 1 Acc (%) | Stage 2 Sub R² (%) | **Final Pipeline R² (%)** | **Theoretical Limit (%)** | MSE | MAE |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| C0 | Baseline_Classical | Classical 0D Features Only | 88.90% | 31.08% | **47.09%** | **94.19%** | 0.824395 | 0.6094 |
| C1 | +Harrison_Quantum_Gap | C0 + Tight-Binding Quantum Gap (E_gap,QM) | 88.90% | 31.08% | **47.09%** | **94.19%** | 0.824395 | 0.6094 |
| C2 | +Birch_Murnaghan_Strain | C1 + Thermodynamic Strain Engine | 88.60% | 31.16% | **46.44%** | **92.87%** | 0.834621 | 0.6159 |
| C3 | +Octahedral_d0_d10 | C2 + Closed-Shell Crystal Field Engine | 88.10% | 32.96% | **47.60%** | **95.20%** | 0.816505 | 0.6035 |
| C4 | +Single_Perov_TieLines | C3 + Single-Perovskite Convex Hull Tie-Lines | 87.75% | 32.97% | **46.95%** | **93.90%** | 0.826614 | 0.6082 |
| C5 | Direct_Linear_No_Hurdle | All Features (C4) + Single-Stage Ridge Only | 100.00% | 25.46% | **25.46%** | **50.91%** | 1.161544 | 0.9038 |
| C6 | Hard_Step_Hurdle | All Features (C4) + Hard Binary Step Function | 87.75% | 32.97% | **46.95%** | **93.90%** | 0.826614 | 0.6082 |
| C7 | **Master_Capstone_Full** | Complete Master Capstone Algorithm | 88.20% | 41.04% | **50.71%** | **101.42%** | 0.768051 | 0.7062 |

---

## Target Property: Energy Above Hull (eV)

**Literature Theoretical Ceiling ($R^2_{\text{limit}}$):** 25.0%

| Code | Condition Name | Description | Stage 1 Acc (%) | Stage 2 Sub R² (%) | **Final Pipeline R² (%)** | **Theoretical Limit (%)** | MSE | MAE |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| C0 | Baseline_Classical | Classical 0D Features Only | 90.70% | 10.11% | **14.34%** | **57.37%** | 0.062956 | 0.0781 |
| C1 | +Harrison_Quantum_Gap | C0 + Tight-Binding Quantum Gap (E_gap,QM) | 90.70% | 10.11% | **14.34%** | **57.37%** | 0.062956 | 0.0781 |
| C2 | +Birch_Murnaghan_Strain | C1 + Thermodynamic Strain Engine | 90.50% | 10.20% | **14.39%** | **57.56%** | 0.062921 | 0.0780 |
| C3 | +Octahedral_d0_d10 | C2 + Closed-Shell Crystal Field Engine | 90.60% | 10.88% | **15.00%** | **59.98%** | 0.062475 | 0.0782 |
| C4 | +Single_Perov_TieLines | C3 + Single-Perovskite Convex Hull Tie-Lines | 90.55% | 10.92% | **15.03%** | **60.11%** | 0.062453 | 0.0782 |
| C5 | Direct_Linear_No_Hurdle | All Features (C4) + Single-Stage Ridge Only | 100.00% | 12.65% | **12.65%** | **50.61%** | 0.064197 | 0.0864 |
| C6 | Hard_Step_Hurdle | All Features (C4) + Hard Binary Step Function | 90.55% | 10.92% | **15.03%** | **60.11%** | 0.062453 | 0.0782 |
| C7 | **Master_Capstone_Full** | Complete Master Capstone Algorithm | 93.70% | 12.39% | **16.67%** | **66.66%** | 0.061248 | 0.0770 |

---

