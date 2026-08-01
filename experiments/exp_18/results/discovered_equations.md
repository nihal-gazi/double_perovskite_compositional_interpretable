# Experiment 18: Discovered Quantum & Strain Physical Equations Report

This document presents the pure compositional analytical physical equations discovered across all 4 target properties in Experiment 18.

---

## Target Property: Formation Energy (eV/atom)

- **Optimal Architecture:** `direct_multi_operator`  
- **Final Pipeline $R^2$:** **71.09%**  
- **Stage 2 Non-Zero Sub $R^2$:** **71.09%**  
- **Relative Theoretical Limit Achieved:** **109.37%**  

### Discovered Physical Equation (Top 15 Terms)

```text
Formation Energy (eV/atom) = +2.688682
     + 0.745731 * EN_B_x_EN_Bprime
     + 0.031252 * d_electrons_B_x_d_electrons_Bprime
     - 0.657303 * (EN_avg)^2
     - 0.120358 * (VEC)^2
     - 2.102993 * sqrt(Tolerance_Factor)
     + 1.126619 * (EN_Bprime_/_(EN_B))
     - 0.064623 * VEC_x_Total_HS_FiM
     + 0.080708 * Val_avg_x_EN_avg
     + 0.853197 * EN_A
     + 0.853197 * EN_Aprime
     - 0.966874 * EN_Bprime
     - 0.290770 * sqrt(E_tolerance_strain)
     + 0.563776 * log(Total_HS_FiM+1)
     + 0.789569 * EN_B
     - 0.006749 * Group_B_x_Group_Bprime
```

---

## Target Property: Total Magnetization (uB)

- **Optimal Architecture:** `hard_margin_hurdle`  
- **Final Pipeline $R^2$:** **59.69%**  
- **Stage 2 Non-Zero Sub $R^2$:** **61.19%**  
- **Relative Theoretical Limit Achieved:** **99.49%**  

### Discovered Physical Equation (Top 15 Terms)

```text
Total Magnetization (uB) = -173.289430
     + 0.001261 * Tolerance_Factor_x_Density_g_cm3_x_Octahedral_Mismatch
     + 0.004400 * Tolerance_Factor_x_Octahedral_Mismatch
     - 0.001708 * Tolerance_Factor_x_Octahedral_Mismatch_x_EN_avg
     + 0.000062 * (Volume_A3)^2
     - 0.065766 * Volume_A3
     + 17.719236 * log(Volume_A3+1)
     - 11.130419 * (EN_avg)^2
     + 3.233314 * Delta_Shannon_B
     + 0.027500 * EN_avg_x_Volume_A3
     - 10.233310 * EN_B_x_EN_Bprime
     + 1.410065 * (Shannon_Bprime_/_(Shannon_B))
     + 84.317702 * sqrt(EN_avg)
     - 2.737803 * d_electrons_B
     - 26.375383 * Phillips_Ionicity_Proxy
     + 1.678666 * Val_avg_x_EN_avg
```

---

## Target Property: Band Gap (eV)

- **Optimal Architecture:** `direct_multi_operator`  
- **Final Pipeline $R^2$:** **30.98%**  
- **Stage 2 Non-Zero Sub $R^2$:** **30.98%**  
- **Relative Theoretical Limit Achieved:** **61.96%**  

### Discovered Physical Equation (Top 15 Terms)

```text
Band Gap (eV) = -6.893069
     + 2.839817 * sqrt(Total_d_electrons)
     - 1.935317 * log(Total_d_electrons+1)
     + 0.128048 * Total_HS_FiM_x_Total_d_electrons
     + 1.485478 * (EN_avg)^2
     + 5.899125 * sqrt(Tolerance_Factor)
     + 0.240512 * VEC_x_Total_HS_FiM
     - 0.312787 * Val_avg_x_EN_avg
     + 0.365396 * Spin_Proxy_Distance
     + 0.638863 * (d_BprimeO_/_(d_BO))
     - 0.025913 * Group_B_x_Group_Bprime
     - 0.009292 * Total_HS_FiM_x_Total_d_electrons_x_Spin_Proxy_Distance
     - 0.046964 * d_electrons_B_x_d_electrons_Bprime
     - 3.401310 * (d_electrons_B_/_(Group_B))
     + 0.220659 * (VEC)^2
     - 0.000111 * Tolerance_Factor_x_Octahedral_Mismatch_x_EN_avg
```

---

## Target Property: Energy Above Hull (eV)

- **Optimal Architecture:** `hard_margin_hurdle`  
- **Final Pipeline $R^2$:** **15.92%**  
- **Stage 2 Non-Zero Sub $R^2$:** **11.97%**  
- **Relative Theoretical Limit Achieved:** **63.69%**  

### Discovered Physical Equation (Top 15 Terms)

```text
Energy Above Hull (eV) = +3.803588
     - 0.058938 * (VEC)^2
     - 0.000000 * (Octahedral_Mismatch)^2
     - 0.000006 * Octahedral_Mismatch
     - 0.037729 * VEC_x_Total_HS_FiM
     + 0.064441 * Spin_Proxy_Distance
     - 0.000000 * E_oct_distortion_strain
     + 0.413110 * (EN_B_/_(EN_A))
     + 0.133063 * sqrt(Total_d_electrons)
     - 0.100239 * (d_BprimeO_/_(d_BO))
     - 0.723084 * sqrt(Tolerance_Factor)
     + 0.317565 * log(Total_HS_FiM+1)
     + 0.420318 * Delta_EN_B
     + 0.012822 * Total_HS_FiM_x_Total_d_electrons
     - 0.181650 * (Group_B_/_(Val_B))
     - 0.619592 * log(Density_g_cm3+1)
```

---

