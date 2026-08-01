# Experiment 15: Master Registry of Discovered Physical Equations Report

This document presents the final master registry of optimal analytical physical equations discovered across all 4 target properties.

---

## Target Property: Formation Energy (eV/atom)

- **Optimal Architecture:** `direct_multi_operator`  
- **Final Master Pipeline $R^2$:** **69.61%**  
- **Stage 2 Non-Zero Sub $R^2$:** **69.61%**  
- **Relative Theoretical Limit Achieved:** **107.10%**  

### Discovered Physical Master Equation (Top 15 Terms)

```text
Formation Energy (eV/atom) = +2.845942
     + 0.028739 * d_electrons_B_x_d_electrons_Bprime
     + 0.154460 * Val_avg_x_EN_avg
     - 4.973541 * sqrt(EN_avg)
     + 1.306099 * (EN_Bprime_/_(EN_B))
     - 1.976812 * sqrt(Tolerance_Factor)
     + 1.040317 * (EN_B_/_(EN_A))
     + 0.437830 * log(Total_d_electrons+1)
     - 0.143003 * Val_B
     + 0.949618 * EN_A
     + 0.949618 * EN_Aprime
     - 0.549364 * sqrt(Total_HS_FiM)
     + 0.100988 * Group_B
     - 0.182308 * Val_avg
     + 0.635015 * log(Total_HS_FiM+1)
     + 0.801250 * EN_B
```

---

## Target Property: Total Magnetization (uB)

- **Optimal Architecture:** `nonlinear_hurdle`  
- **Final Master Pipeline $R^2$:** **50.80%**  
- **Stage 2 Non-Zero Sub $R^2$:** **58.79%**  
- **Relative Theoretical Limit Achieved:** **84.66%**  

### Discovered Physical Master Equation (Top 15 Terms)

```text
Total Magnetization (uB) = -178.533413
     + 0.001281 * Tolerance_Factor_x_Density_g_cm3_x_Octahedral_Mismatch
     + 0.004054 * Tolerance_Factor_x_Octahedral_Mismatch
     - 0.001867 * Tolerance_Factor_x_Octahedral_Mismatch_x_EN_avg
     - 14.284434 * (EN_avg)^2
     + 0.000054 * (Volume_A3)^2
     + 0.029488 * EN_avg_x_Volume_A3
     + 103.001826 * sqrt(EN_avg)
     - 0.052512 * Volume_A3
     + 14.452901 * log(Volume_A3+1)
     - 2.967438 * d_electrons_B
     - 1.348024 * Total_d_electrons
     - 0.600461 * Total_HS_FiM_x_Total_d_electrons
     + 1.073573 * (Shannon_Bprime_/_(Shannon_B))
     + 23.340396 * (d_electrons_B_/_(Group_B))
     - 0.008548 * EN_B_x_EN_Bprime_x_Volume_A3
```

---

## Target Property: Band Gap (eV)

- **Optimal Architecture:** `direct_multi_operator`  
- **Final Master Pipeline $R^2$:** **29.10%**  
- **Stage 2 Non-Zero Sub $R^2$:** **29.10%**  
- **Relative Theoretical Limit Achieved:** **58.19%**  

### Discovered Physical Master Equation (Top 15 Terms)

```text
Band Gap (eV) = -13.225284
     + 3.110437 * sqrt(Total_d_electrons)
     - 2.603690 * log(Total_d_electrons+1)
     - 0.498567 * Val_avg_x_EN_avg
     + 0.129919 * Total_HS_FiM_x_Total_d_electrons
     + 6.785353 * sqrt(Tolerance_Factor)
     + 0.823145 * (d_BprimeO_/_(d_BO))
     - 0.049506 * d_electrons_B_x_d_electrons_Bprime
     - 0.000128 * Tolerance_Factor_x_Octahedral_Mismatch_x_EN_avg
     + 0.283788 * Spin_Proxy_Distance
     - 2.741937 * EN_Bprime
     + 0.948604 * (EN_avg)^2
     - 0.022214 * Group_B_x_Group_Bprime
     + 0.316203 * d_electrons_B
     + 0.329757 * Val_B
     + 0.456806 * Val_avg
```

---

## Target Property: Energy Above Hull (eV)

- **Optimal Architecture:** `nonlinear_hurdle`  
- **Final Master Pipeline $R^2$:** **13.58%**  
- **Stage 2 Non-Zero Sub $R^2$:** **10.44%**  
- **Relative Theoretical Limit Achieved:** **54.32%**  

### Discovered Physical Master Equation (Top 15 Terms)

```text
Energy Above Hull (eV) = +2.866668
     - 0.000000 * (Octahedral_Mismatch)^2
     - 0.000007 * Octahedral_Mismatch
     - 0.000002 * Octahedral_Mismatch_x_Density_g_cm3
     - 0.235975 * EN_B_x_EN_Bprime
     + 0.065486 * Spin_Proxy_Distance
     + 0.198220 * (EN_avg)^2
     - 0.216206 * (Group_B_/_(Val_B))
     + 0.119534 * sqrt(Total_d_electrons)
     + 0.045729 * Group_B
     - 0.059420 * Val_B
     - 0.237821 * sqrt(Total_HS_FiM)
     - 0.073498 * Shannon_B_x_Shannon_Bprime
     + 0.280622 * log(Total_HS_FiM+1)
     - 0.082536 * (d_BprimeO_/_(d_BO))
     - 0.003339 * Group_B_x_Group_Bprime
```

---

