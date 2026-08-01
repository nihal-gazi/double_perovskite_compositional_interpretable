# Experiment 19: Discovered Physical Equations Report

This document presents the pure compositional analytical physical equations discovered across all 4 target properties in Experiment 19.

---

## Target Property: Formation Energy (eV/atom)

- **Optimal Architecture:** `direct_multi_operator`  
- **Final Pipeline $R^2$:** **71.24%**  
- **Stage 2 Non-Zero Sub $R^2$:** **71.24%**  
- **Relative Theoretical Limit Achieved:** **109.59%**  

### Discovered Physical Equation (Top 15 Terms)

```text
Formation Energy (eV/atom) = +1.904330
     + 0.744000 * EN_B_x_EN_Bprime
     + 0.029104 * d_electrons_B_x_d_electrons_Bprime
     - 0.651330 * (EN_avg)^2
     - 2.033459 * sqrt(Tolerance_Factor)
     - 0.083520 * VEC_x_Total_HS_FiM
     - 0.105896 * (VEC)^2
     + 1.113400 * (EN_Bprime_/_(EN_B))
     + 0.421490 * log(Total_d_electrons+1)
     - 0.118691 * d_electrons_B
     - 0.984131 * EN_Bprime
     + 0.861544 * EN_A
     + 0.861544 * EN_Aprime
     + 0.078752 * Val_avg_x_EN_avg
     - 0.007821 * Group_B_x_Group_Bprime
     + 0.091672 * Delta_Shannon_B
```

---

## Target Property: Total Magnetization (uB)

- **Optimal Architecture:** `hard_margin_hurdle`  
- **Final Pipeline $R^2$:** **61.16%**  
- **Stage 2 Non-Zero Sub $R^2$:** **61.67%**  
- **Relative Theoretical Limit Achieved:** **101.94%**  

### Discovered Physical Equation (Top 15 Terms)

```text
Total Magnetization (uB) = -182.135052
     + 0.001312 * Tolerance_Factor_x_Density_g_cm3_x_Octahedral_Mismatch
     + 0.004588 * Tolerance_Factor_x_Octahedral_Mismatch
     - 0.076360 * Volume_A3
     - 0.001725 * Tolerance_Factor_x_Octahedral_Mismatch_x_EN_avg
     + 0.000064 * (Volume_A3)^2
     + 20.170531 * log(Volume_A3+1)
     + 3.542454 * Delta_Shannon_B
     - 10.813383 * EN_B_x_EN_Bprime
     + 1.463966 * (Shannon_Bprime_/_(Shannon_B))
     + 0.024667 * EN_avg_x_Volume_A3
     - 9.077986 * (EN_avg)^2
     + 74.488400 * sqrt(EN_avg)
     + 1.826295 * Val_avg_x_EN_avg
     + 19.715423 * EN_Bprime
     - 23.494405 * Phillips_Ionicity_Proxy
```

---

## Target Property: Band Gap (eV)

- **Optimal Architecture:** `soft_gated_regressor`  
- **Final Pipeline $R^2$:** **50.82%**  
- **Stage 2 Non-Zero Sub $R^2$:** **41.03%**  
- **Relative Theoretical Limit Achieved:** **101.63%**  

### Discovered Physical Equation (Top 15 Terms)

```text
Band Gap (eV) = +0.987175
     + 1.924914 * (EN_avg)^2
     + 0.524095 * Delta_Shannon_B
     + 0.356598 * Group_Bprime
     + 0.115695 * Total_HS_FiM_x_Total_d_electrons
     + 0.509771 * d_electrons_B
     - 0.063696 * d_electrons_B_x_d_electrons_Bprime
     + 0.360965 * Spin_Proxy_Distance
     - 0.010118 * Total_HS_FiM_x_Total_d_electrons_x_Spin_Proxy_Distance
     - 0.000124 * Tolerance_Factor_x_Octahedral_Mismatch_x_EN_avg
     - 0.957691 * Delta_HS_B
     - 0.957691 * Total_HS_FiM
     - 0.021050 * Group_B_x_Group_Bprime
     + 3.667768 * sqrt(Tolerance_Factor)
     + 2.030594 * (EN_Bprime_/_(EN_B))
     - 0.834579 * log(Total_d_electrons+1)
```

---

## Target Property: Energy Above Hull (eV)

- **Optimal Architecture:** `hard_margin_hurdle`  
- **Final Pipeline $R^2$:** **16.29%**  
- **Stage 2 Non-Zero Sub $R^2$:** **12.25%**  
- **Relative Theoretical Limit Achieved:** **65.14%**  

### Discovered Physical Equation (Top 15 Terms)

```text
Energy Above Hull (eV) = +3.777106
     - 0.050888 * VEC_x_Total_HS_FiM
     + 0.069640 * Spin_Proxy_Distance
     - 0.000000 * (Octahedral_Mismatch)^2
     - 0.000006 * Octahedral_Mismatch
     - 0.047373 * (VEC)^2
     + 0.442203 * (EN_B_/_(EN_A))
     - 0.000000 * E_oct_distortion_strain
     + 0.455383 * Delta_EN_B
     + 0.331793 * log(Total_HS_FiM+1)
     - 0.097964 * (d_BprimeO_/_(d_BO))
     - 0.680468 * sqrt(Tolerance_Factor)
     - 0.214323 * sqrt(Total_HS_FiM)
     - 0.627617 * log(Density_g_cm3+1)
     + 0.000641 * Volume_A3
     - 0.385879 * EN_Bprime
```

---

