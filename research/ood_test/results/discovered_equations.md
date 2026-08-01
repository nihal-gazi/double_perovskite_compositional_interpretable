# Discovered Equations Report: 80/20 Split on 5,000 Dataset

This document presents the pure compositional analytical physical equations generated on the 80% training set (4,000 materials) and validated on the 20% test set (1,000 materials).

---

## Target Property: Formation Energy (eV/atom)

- **Architecture:** `direct_multi_operator`  
- **80% Train $R^2$ (4,000 samples):** **70.95%** (109.16% of Lit Limit)  
- **20% Test $R^2$ (1,000 samples):** **65.16%** (100.25% of Lit Limit)  
- **20% Test Stage 1 Classification Acc:** **100.00%**  

### Discovered Physical Equation (Top 15 Terms)

```text
Formation Energy (eV/atom) = +3.135912
     - 2.283327 * EN_Bprime
     + 0.785653 * EN_B_x_EN_Bprime
     - 0.662294 * sqrt(E_tolerance_strain)
     + 0.575285 * Total_HS_FiM
     - 0.548432 * (EN_avg)^2
     + 0.024525 * d_electrons_B_x_d_electrons_Bprime
     - 0.090908 * VEC_x_Total_HS_FiM
     + 1.825434 * EN_avg
     + 0.123604 * Delta_Shannon_B
     - 0.105208 * (VEC)^2
     + 1.138098 * EN_A
     + 0.104682 * Val_avg_x_EN_avg
     + 1.051708 * (EN_Bprime_/_(EN_B))
     + 0.000000 * E_oct_distortion_strain
     + 0.172823 * d_avg
```

---

## Target Property: Total Magnetization (uB)

- **Architecture:** `hard_margin_hurdle`  
- **80% Train $R^2$ (4,000 samples):** **48.78%** (81.29% of Lit Limit)  
- **20% Test $R^2$ (1,000 samples):** **-3.89%** (0.00% of Lit Limit)  
- **20% Test Stage 1 Classification Acc:** **75.00%**  

### Discovered Physical Equation (Top 15 Terms)

```text
Total Magnetization (uB) = -133.678674
     + 0.031644 * EN_avg_x_Volume_A3
     - 0.014874 * EN_B_x_EN_Bprime_x_Volume_A3
     - 2.945480 * Shannon_Bprime
     + 1.380505 * (Shannon_Bprime_/_(Shannon_B))
     - 1.733976 * VEC_x_Total_HS_FiM
     + 8.642716 * Total_HS_FiM
     + 4.303092 * Tolerance_Factor_x_EN_avg
     - 9.561042 * (EN_avg)^2
     + 5.560301 * Density_g_cm3
     + 1.952014 * Delta_Shannon_B
     - 2.541249 * d_electrons_B
     - 2.420242 * EN_avg_x_Density_g_cm3
     + 2.071927 * Group_B
     + 0.000032 * (Volume_A3)^2
     + 13.221147 * log(Total_HS_FiM+1)
```

---

## Target Property: Band Gap (eV)

- **Architecture:** `soft_gated_regressor`  
- **80% Train $R^2$ (4,000 samples):** **41.17%** (82.35% of Lit Limit)  
- **20% Test $R^2$ (1,000 samples):** **40.37%** (80.73% of Lit Limit)  
- **20% Test Stage 1 Classification Acc:** **79.40%**  

### Discovered Physical Equation (Top 15 Terms)

```text
Band Gap (eV) = -1.738002
     + 2.104266 * sqrt(Total_d_electrons)
     - 2.131271 * log(Total_d_electrons+1)
     - 3.972049 * log(Total_HS_FiM+1)
     - 1.245763 * Density_g_cm3
     - 1.618299 * Total_HS_FiM
     + 0.278661 * VEC_x_Total_HS_FiM
     - 0.380650 * Val_avg_x_EN_avg
     + 1.577576 * (EN_avg)^2
     + 6.662010 * log(Density_g_cm3+1)
     - 0.012954 * Total_HS_FiM_x_Total_d_electrons_x_Spin_Proxy_Distance
     + 2.147624 * sqrt(Total_HS_FiM)
     + 0.156835 * Total_HS_FiM_x_Spin_Proxy_Distance
     + 0.059035 * (Density_g_cm3)^2
     - 0.000000 * E_oct_distortion_strain
     - 0.004761 * Volume_A3
```

---

## Target Property: Energy Above Hull (eV)

- **Architecture:** `hard_margin_hurdle`  
- **80% Train $R^2$ (4,000 samples):** **17.43%** (69.72% of Lit Limit)  
- **20% Test $R^2$ (1,000 samples):** **11.03%** (44.14% of Lit Limit)  
- **20% Test Stage 1 Classification Acc:** **78.70%**  

### Discovered Physical Equation (Top 15 Terms)

```text
Energy Above Hull (eV) = +2.614782
     + 0.347108 * Total_HS_FiM
     - 0.906569 * EN_Bprime
     - 1.319858 * log(Density_g_cm3+1)
     + 0.735784 * EN_A
     + 0.185832 * Density_g_cm3
     - 0.048702 * VEC_x_Total_HS_FiM
     + 0.001243 * Volume_A3
     + 0.596843 * Delta_EN_B
     - 0.052388 * (VEC)^2
     - 0.113478 * (d_BprimeO_/_(d_BO))
     + 0.221510 * EN_B_x_EN_Bprime
     - 0.000495 * EN_avg_x_Volume_A3
     - 0.000000 * (Octahedral_Mismatch)^2
     + 0.422337 * (EN_B_/_(EN_A))
     + 0.094944 * d_avg
```

---

