# Experiment 21: Discovered Physical Equations Report

This document presents the pure compositional analytical physical equations discovered across all 4 target properties in Experiment 21.

---

## Target Property: Formation Energy (eV/atom)

- **Optimal Architecture:** `direct_multi_operator`  
- **Final Pipeline $R^2$:** **71.26%**  
- **Stage 2 Non-Zero Sub $R^2$:** **71.26%**  
- **Relative Theoretical Limit Achieved:** **109.62%**  

### Discovered Physical Equation (Top 15 Terms)

```text
Formation Energy (eV/atom) = +1.676609
     + 0.739904 * EN_B_x_EN_Bprime
     + 0.028943 * d_electrons_B_x_d_electrons_Bprime
     - 0.637325 * (EN_avg)^2
     - 0.083065 * VEC_x_Total_HS_FiM
     - 0.106577 * (VEC)^2
     + 1.109092 * (EN_Bprime_/_(EN_B))
     + 0.423454 * log(Total_d_electrons+1)
     - 1.729635 * sqrt(Tolerance_Factor)
     + 0.867137 * EN_A
     + 0.867137 * EN_Aprime
     - 0.118475 * d_electrons_B
     - 0.964664 * EN_Bprime
     + 0.079401 * Val_avg_x_EN_avg
     - 0.323705 * sqrt(E_tolerance_strain)
     - 0.007797 * Group_B_x_Group_Bprime
```

---

## Target Property: Total Magnetization (uB)

- **Optimal Architecture:** `hard_margin_hurdle`  
- **Final Pipeline $R^2$:** **62.23%**  
- **Stage 2 Non-Zero Sub $R^2$:** **61.75%**  
- **Relative Theoretical Limit Achieved:** **103.72%**  

### Discovered Physical Equation (Top 15 Terms)

```text
Total Magnetization (uB) = -174.949745
     + 0.001294 * Tolerance_Factor_x_Density_g_cm3_x_Octahedral_Mismatch
     + 0.004366 * Tolerance_Factor_x_Octahedral_Mismatch
     - 0.076902 * Volume_A3
     + 0.000064 * (Volume_A3)^2
     - 0.001684 * Tolerance_Factor_x_Octahedral_Mismatch_x_EN_avg
     + 20.209179 * log(Volume_A3+1)
     - 11.208474 * EN_B_x_EN_Bprime
     + 1.586669 * (Shannon_Bprime_/_(Shannon_B))
     + 0.025786 * EN_avg_x_Volume_A3
     - 8.683213 * (EN_avg)^2
     + 1.944030 * Val_avg_x_EN_avg
     + 71.808434 * sqrt(EN_avg)
     + 2.273254 * Delta_Shannon_B
     + 20.050236 * EN_Bprime
     - 23.106567 * Phillips_Ionicity_Proxy
```

---

## Target Property: Band Gap (eV)

- **Optimal Architecture:** `soft_gated_regressor`  
- **Final Pipeline $R^2$:** **50.71%**  
- **Stage 2 Non-Zero Sub $R^2$:** **41.04%**  
- **Relative Theoretical Limit Achieved:** **101.42%**  

### Discovered Physical Equation (Top 15 Terms)

```text
Band Gap (eV) = +0.806034
     + 1.953233 * (EN_avg)^2
     + 0.375023 * Group_Bprime
     + 0.514475 * d_electrons_B
     + 0.115964 * Total_HS_FiM_x_Total_d_electrons
     - 0.063532 * d_electrons_B_x_d_electrons_Bprime
     + 0.366100 * Spin_Proxy_Distance
     - 0.010033 * Total_HS_FiM_x_Total_d_electrons_x_Spin_Proxy_Distance
     - 0.000122 * Tolerance_Factor_x_Octahedral_Mismatch_x_EN_avg
     - 0.963911 * Total_HS_FiM
     - 0.963911 * Delta_HS_B
     + 0.286944 * Delta_Shannon_B
     - 0.021634 * Group_B_x_Group_Bprime
     + 2.032160 * (EN_Bprime_/_(EN_B))
     - 0.834583 * log(Total_d_electrons+1)
     - 2.749130 * (d_electrons_B_/_(Group_B))
```

---

## Target Property: Energy Above Hull (eV)

- **Optimal Architecture:** `log_target_hurdle`  
- **Final Pipeline $R^2$:** **15.10%**  
- **Stage 2 Non-Zero Sub $R^2$:** **10.73%**  
- **Relative Theoretical Limit Achieved:** **60.42%**  

### Discovered Physical Equation (Top 15 Terms)

```text
log(Energy Above Hull (eV) + 1.0) = 
    +2.390922
     - 0.037239 * VEC_x_Total_HS_FiM
     - 0.037628 * (VEC)^2
     + 0.290961 * (EN_B_/_(EN_A))
     - 0.000000 * E_oct_distortion_strain
     - 0.494809 * sqrt(Tolerance_Factor)
     + 0.034746 * Spin_Proxy_Distance
     + 0.212002 * log(Total_HS_FiM+1)
     + 0.000493 * Volume_A3
     - 0.090101 * t_ABO3
     - 0.027878 * Delta_Shannon_B
     - 0.408662 * log(Density_g_cm3+1)
     - 0.142669 * log(Volume_A3+1)
     + 0.225930 * Delta_EN_B
     + 0.020836 * Val_avg_x_EN_avg
     - 0.049818 * (d_BprimeO_/_(d_BO))
```

---

