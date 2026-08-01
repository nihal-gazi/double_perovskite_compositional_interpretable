# Experiment 17: Discovered Tight-Binding & Mendeleev Physical Equations Report

This document presents the pure compositional analytical physical equations discovered across all 4 target properties in Experiment 17.

---

## Target Property: Formation Energy (eV/atom)

- **Optimal Architecture:** `direct_multi_operator`  
- **Final Pipeline $R^2$:** **71.24%**  
- **Stage 2 Non-Zero Sub $R^2$:** **71.24%**  
- **Relative Theoretical Limit Achieved:** **109.59%**  

### Discovered Physical Equation (Top 15 Terms)

```text
Formation Energy (eV/atom) = -2.253472
     + 1.263274 * (EN_Bprime_/_(EN_B))
     + 0.022127 * d_electrons_B_x_d_electrons_Bprime
     - 0.111559 * (VEC)^2
     - 1.997480 * sqrt(Tolerance_Factor)
     + 1.031085 * EN_B
     - 0.061504 * VEC_x_Total_HS_FiM
     - 0.008318 * Group_B_x_Group_Bprime
     - 3.143963 * sqrt(EN_avg)
     + 1.383717 * log(Delta_EN_B+1)
     - 0.962981 * EN_Bprime
     + 0.826316 * EN_A
     + 0.826316 * EN_Aprime
     - 0.479571 * sqrt(Total_HS_FiM)
     + 0.566010 * log(Total_HS_FiM+1)
     + 0.097893 * EN_avg_x_Density_g_cm3
```

---

## Target Property: Total Magnetization (uB)

- **Optimal Architecture:** `cost_sensitive_hurdle`  
- **Final Pipeline $R^2$:** **56.82%**  
- **Stage 2 Non-Zero Sub $R^2$:** **61.38%**  
- **Relative Theoretical Limit Achieved:** **94.70%**  

### Discovered Physical Equation (Top 15 Terms)

```text
Total Magnetization (uB) = -213.900296
     + 0.001270 * Tolerance_Factor_x_Density_g_cm3_x_Octahedral_Mismatch
     + 0.004413 * Tolerance_Factor_x_Octahedral_Mismatch
     - 0.001761 * Tolerance_Factor_x_Octahedral_Mismatch_x_EN_avg
     - 0.063004 * Volume_A3
     + 0.000058 * (Volume_A3)^2
     + 0.031403 * EN_avg_x_Volume_A3
     - 11.403415 * EN_B_x_EN_Bprime
     + 17.984184 * log(Volume_A3+1)
     + 3.187155 * Delta_Shannon_B
     - 8.724601 * (EN_avg)^2
     + 1.245128 * (Shannon_Bprime_/_(Shannon_B))
     + 73.629243 * sqrt(EN_avg)
     - 2.824659 * d_electrons_B
     + 1.803697 * Val_avg_x_EN_avg
     - 0.563966 * Total_HS_FiM_x_Total_d_electrons
```

---

## Target Property: Band Gap (eV)

- **Optimal Architecture:** `direct_multi_operator`  
- **Final Pipeline $R^2$:** **31.23%**  
- **Stage 2 Non-Zero Sub $R^2$:** **31.23%**  
- **Relative Theoretical Limit Achieved:** **62.46%**  

### Discovered Physical Equation (Top 15 Terms)

```text
Band Gap (eV) = -2.946233
     + 2.730433 * sqrt(Total_d_electrons)
     + 0.137097 * Total_HS_FiM_x_Total_d_electrons
     + 6.823415 * sqrt(Tolerance_Factor)
     - 1.622404 * log(Total_d_electrons+1)
     + 0.219981 * VEC_x_Total_HS_FiM
     + 0.706353 * (d_BprimeO_/_(d_BO))
     + 1.204123 * (EN_avg)^2
     - 0.010064 * Total_HS_FiM_x_Total_d_electrons_x_Spin_Proxy_Distance
     + 0.331456 * Spin_Proxy_Distance
     - 0.000120 * Tolerance_Factor_x_Octahedral_Mismatch_x_EN_avg
     - 3.447529 * (d_electrons_B_/_(Group_B))
     - 0.233782 * Val_avg_x_EN_avg
     - 2.831266 * Delta_EN_AB
     - 1.737205 * log(Total_HS_FiM+1)
     - 0.832633 * Delta_HS_B
```

---

## Target Property: Energy Above Hull (eV)

- **Optimal Architecture:** `cost_sensitive_hurdle`  
- **Final Pipeline $R^2$:** **14.98%**  
- **Stage 2 Non-Zero Sub $R^2$:** **11.98%**  
- **Relative Theoretical Limit Achieved:** **59.92%**  

### Discovered Physical Equation (Top 15 Terms)

```text
Energy Above Hull (eV) = +1.486400
     - 0.060638 * (VEC)^2
     - 0.039258 * VEC_x_Total_HS_FiM
     - 0.000000 * (Octahedral_Mismatch)^2
     - 0.000006 * Octahedral_Mismatch
     + 0.064291 * Spin_Proxy_Distance
     - 0.000002 * Octahedral_Mismatch_x_Density_g_cm3
     - 0.733299 * sqrt(Tolerance_Factor)
     - 0.099429 * (d_BprimeO_/_(d_BO))
     + 0.393906 * (EN_B_/_(EN_A))
     + 0.012894 * Total_HS_FiM_x_Total_d_electrons
     + 0.307497 * log(Total_HS_FiM+1)
     + 0.120511 * sqrt(Total_d_electrons)
     - 0.227731 * sqrt(Total_HS_FiM)
     - 0.612539 * log(Density_g_cm3+1)
     - 0.383180 * EN_Bprime
```

---

