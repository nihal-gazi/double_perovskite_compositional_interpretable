# Discovered Equations Report: ood_test_2 (2,000 Dataset, Seed = 42)

This document presents the pure compositional analytical physical equations generated on the 80% training set (1,600 materials) and validated on the 20% test set (400 materials).

---

## Target Property: Formation Energy (eV/atom)

- **Architecture:** `direct_multi_operator`  
- **80% Train $R^2$ (1,600 samples):** **69.96%** (107.64% of Lit Limit)  
- **20% Test $R^2$ (400 samples):** **75.01%** (115.40% of Lit Limit)  
- **20% Test Stage 1 Classification Acc:** **100.00%**  

### Discovered Physical Equation (Top 15 Terms)

```text
Formation Energy (eV/atom) = +1.221492
     + 0.751125 * EN_B_x_EN_Bprime
     - 0.627359 * (EN_avg)^2
     + 0.026471 * d_electrons_B_x_d_electrons_Bprime
     + 1.134418 * (EN_Bprime_/_(EN_B))
     - 0.072038 * VEC_x_Total_HS_FiM
     - 1.749535 * sqrt(Tolerance_Factor)
     - 1.077485 * EN_Bprime
     + 0.898216 * EN_Aprime
     + 0.898216 * EN_A
     - 0.075817 * (VEC)^2
     + 0.696146 * (EN_B_/_(EN_A))
     - 0.107302 * d_electrons_B
     + 0.310635 * log(Total_d_electrons+1)
     + 0.071398 * Val_avg_x_EN_avg
     + 0.341019 * (Delta_t_sub_perov_/_(Tolerance_Factor))
```

---

## Target Property: Total Magnetization (uB)

- **Architecture:** `hard_margin_hurdle`  
- **80% Train $R^2$ (1,600 samples):** **62.60%** (104.33% of Lit Limit)  
- **20% Test $R^2$ (400 samples):** **30.31%** (50.51% of Lit Limit)  
- **20% Test Stage 1 Classification Acc:** **76.25%**  

### Discovered Physical Equation (Top 15 Terms)

```text
Total Magnetization (uB) = -166.574530
     + 0.001261 * Tolerance_Factor_x_Density_g_cm3_x_Octahedral_Mismatch
     + 0.003833 * Tolerance_Factor_x_Octahedral_Mismatch
     + 0.000064 * (Volume_A3)^2
     - 0.069411 * Volume_A3
     + 19.808233 * log(Volume_A3+1)
     - 0.001250 * Tolerance_Factor_x_Octahedral_Mismatch_x_EN_avg
     + 0.025832 * EN_avg_x_Volume_A3
     + 2.247240 * Val_avg_x_EN_avg
     - 8.853584 * EN_B_x_EN_Bprime
     - 7.164386 * (EN_avg)^2
     - 0.565823 * Total_HS_FiM_x_Total_d_electrons
     + 64.428506 * sqrt(EN_avg)
     + 1.011789 * (Shannon_Bprime_/_(Shannon_B))
     + 18.681438 * EN_Bprime
     + 1.774634 * Spin_Proxy_Distance
```

---

## Target Property: Band Gap (eV)

- **Architecture:** `soft_gated_regressor`  
- **80% Train $R^2$ (1,600 samples):** **50.18%** (100.36% of Lit Limit)  
- **20% Test $R^2$ (400 samples):** **41.07%** (82.14% of Lit Limit)  
- **20% Test Stage 1 Classification Acc:** **74.75%**  

### Discovered Physical Equation (Top 15 Terms)

```text
Band Gap (eV) = +1.433067
     + 1.728714 * (EN_avg)^2
     + 0.388906 * Group_Bprime
     - 0.069430 * d_electrons_B_x_d_electrons_Bprime
     + 0.116461 * Total_HS_FiM_x_Total_d_electrons
     + 0.481193 * d_electrons_B
     + 0.397929 * Spin_Proxy_Distance
     - 0.008526 * Total_HS_FiM_x_Total_d_electrons_x_Spin_Proxy_Distance
     - 0.869495 * Total_HS_FiM
     - 0.869495 * Delta_HS_B
     - 3.175804 * (d_electrons_B_/_(Group_B))
     - 0.846063 * log(Total_d_electrons+1)
     - 0.270183 * EN_avg_x_Density_g_cm3
     - 0.018959 * Group_B_x_Group_Bprime
     + 0.221740 * Delta_Shannon_B
     - 0.168459 * Val_avg_x_EN_avg
```

---

## Target Property: Energy Above Hull (eV)

- **Architecture:** `hard_margin_hurdle`  
- **80% Train $R^2$ (1,600 samples):** **16.71%** (66.83% of Lit Limit)  
- **20% Test $R^2$ (400 samples):** **7.30%** (29.21% of Lit Limit)  
- **20% Test Stage 1 Classification Acc:** **84.00%**  

### Discovered Physical Equation (Top 15 Terms)

```text
Energy Above Hull (eV) = +3.587800
     - 0.047800 * VEC_x_Total_HS_FiM
     + 0.563925 * Delta_EN_B
     + 0.060265 * Spin_Proxy_Distance
     + 0.401090 * (EN_B_/_(EN_A))
     - 0.039477 * (VEC)^2
     - 0.157077 * t_ABO3
     - 0.738425 * sqrt(Tolerance_Factor)
     - 0.476742 * EN_Bprime
     - 0.000000 * E_oct_distortion_strain
     - 0.216870 * log(Spin_Proxy_Distance+1)
     + 0.265228 * log(Total_HS_FiM+1)
     - 0.003350 * Group_B_x_Group_Bprime
     - 0.203334 * sqrt(Total_HS_FiM)
     - 0.039153 * Delta_Shannon_B
     + 0.000591 * Volume_A3
```

---

