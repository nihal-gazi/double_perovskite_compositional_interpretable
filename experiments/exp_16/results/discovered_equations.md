# Experiment 16: Discovered Pure Compositional Physical Equations Report

This document presents the pure compositional analytical physical equations discovered across all 4 target properties in Experiment 16.

---

## Target Property: Formation Energy (eV/atom)

- **Optimal Architecture:** `direct_multi_operator`  
- **Final Pipeline $R^2$:** **71.24%**  
- **Stage 2 Non-Zero Sub $R^2$:** **71.24%**  
- **Relative Theoretical Limit Achieved:** **109.60%**  

### Discovered Pure Compositional Physical Equation (Top 15 Terms)

```text
Formation Energy (eV/atom) = +2.002787
     + 1.172758 * (EN_Bprime_/_(EN_B))
     - 1.786427 * sqrt(Tolerance_Factor)
     + 1.073403 * EN_B
     + 0.016069 * d_electrons_B_x_d_electrons_Bprime
     - 3.296810 * sqrt(EN_avg)
     + 1.345877 * log(Delta_EN_B+1)
     + 0.848843 * EN_A
     + 0.848843 * EN_Aprime
     + 0.108218 * EN_avg_x_Density_g_cm3
     - 0.088683 * d_electrons_Bprime
     + 1.017096 * Phillips_Ionicity_Proxy
     - 0.817893 * EN_Bprime
     + 0.079827 * Group_B
     + 0.000061 * Tolerance_Factor_x_Octahedral_Mismatch
     - 0.398067 * log(Volume_A3+1)
```

---

## Target Property: Total Magnetization (uB)

- **Optimal Architecture:** `nonlinear_hurdle`  
- **Final Pipeline $R^2$:** **53.23%**  
- **Stage 2 Non-Zero Sub $R^2$:** **61.93%**  
- **Relative Theoretical Limit Achieved:** **88.72%**  

### Discovered Pure Compositional Physical Equation (Top 15 Terms)

```text
Total Magnetization (uB) = -200.701237
     + 0.001172 * Tolerance_Factor_x_Density_g_cm3_x_Octahedral_Mismatch
     + 0.004229 * Tolerance_Factor_x_Octahedral_Mismatch
     - 0.064868 * Volume_A3
     + 0.033049 * EN_avg_x_Volume_A3
     + 0.000055 * (Volume_A3)^2
     - 0.001453 * Tolerance_Factor_x_Octahedral_Mismatch_x_EN_avg
     - 11.291081 * EN_B_x_EN_Bprime
     + 17.664825 * log(Volume_A3+1)
     + 30.695154 * Delta_EN_AB
     + 8.765382 * Tolerance_Factor
     + 2.620085 * Delta_Shannon_B
     - 8.933034 * (EN_avg)^2
     - 4.190789 * Tolerance_Factor_x_EN_avg
     + 78.169592 * sqrt(EN_avg)
     - 26.801330 * Phillips_Ionicity_Proxy
```

---

## Target Property: Band Gap (eV)

- **Optimal Architecture:** `direct_multi_operator`  
- **Final Pipeline $R^2$:** **31.23%**  
- **Stage 2 Non-Zero Sub $R^2$:** **31.23%**  
- **Relative Theoretical Limit Achieved:** **62.47%**  

### Discovered Pure Compositional Physical Equation (Top 15 Terms)

```text
Band Gap (eV) = -9.607321
     + 2.680414 * sqrt(Total_d_electrons)
     + 7.336684 * sqrt(Tolerance_Factor)
     - 1.617171 * log(Total_d_electrons+1)
     - 0.012120 * Total_HS_FiM_x_Total_d_electrons_x_Spin_Proxy_Distance
     + 1.286948 * (EN_avg)^2
     + 0.714593 * (d_BprimeO_/_(d_BO))
     - 0.289991 * Val_avg_x_EN_avg
     - 3.758316 * (d_electrons_B_/_(Group_B))
     + 0.084394 * Delta_HS_B_x_Total_d_electrons
     + 0.084394 * Total_HS_FiM_x_Total_d_electrons
     + 1.025347 * Tolerance_Factor
     + 0.288252 * Spin_Proxy_Distance
     + 5.470868 * (d_BO_/_(d_AO))
     + 0.257921 * Delta_Shannon_B
     - 0.003960 * Volume_A3
```

---

## Target Property: Energy Above Hull (eV)

- **Optimal Architecture:** `nonlinear_hurdle`  
- **Final Pipeline $R^2$:** **14.96%**  
- **Stage 2 Non-Zero Sub $R^2$:** **11.83%**  
- **Relative Theoretical Limit Achieved:** **59.85%**  

### Discovered Pure Compositional Physical Equation (Top 15 Terms)

```text
Energy Above Hull (eV) = +3.463993
     + 0.068584 * Spin_Proxy_Distance
     - 0.000000 * (Octahedral_Mismatch)^2
     - 0.000006 * Octahedral_Mismatch
     - 0.000002 * Octahedral_Mismatch_x_Density_g_cm3
     - 0.811161 * sqrt(Tolerance_Factor)
     + 0.129190 * sqrt(Total_d_electrons)
     - 0.096493 * (d_BprimeO_/_(d_BO))
     + 0.356869 * (EN_B_/_(EN_A))
     - 0.225336 * log(Spin_Proxy_Distance+1)
     - 0.612859 * log(Density_g_cm3+1)
     - 0.176042 * (Group_B_/_(Val_B))
     - 0.372697 * EN_Bprime
     - 0.047149 * Val_B
     - 0.035986 * d_electrons_Bprime
     + 0.000542 * Volume_A3
```

---

