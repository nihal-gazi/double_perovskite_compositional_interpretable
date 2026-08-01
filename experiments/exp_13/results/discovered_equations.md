# Experiment 13: Discovered Physical Interaction Equations Report

This document contains the top 15 most influential physical interaction terms ($x_i x_j$, $x_i/x_j$, $x_i^2$) and their fitted coefficients across all 4 target properties under the Non-Linear Decision Boundary Hurdle Architecture.

---

## Target Property: Band Gap (eV)

- **Stage 1 Non-Linear Classification Accuracy:** **78.25%**  
- **Stage 2 Non-Zero Sub $R^2$:** **33.23%**  
- **Direct Interaction $R^2$:** **25.03%**  
- **Two-Stage Hurdle Pipeline $R^2$:** **27.19%**  
- **Relative Theoretical Limit Achieved:** **54.37%**  

### 1. Direct Physical Interaction Formula (Top 15 Terms)

```text
Band Gap (eV) = +1.049218
     + 0.726145 * d_electrons_B
     - 0.452939 * Val_avg_x_EN_avg
     - 0.069300 * d_electrons_B_x_d_electrons_Bprime
     + 1.316943 * Tolerance_Factor
     + 0.734764 * (d_BprimeO_/_(d_BO))
     - 0.263650 * Group_B
     + 0.154991 * Total_d_electrons
     + 0.445738 * Val_avg
     + 0.307928 * Val_B
     + 0.002045 * EN_avg_x_Volume_A3
     - 0.113286 * (Shannon_Bprime_/_(Shannon_B))
     + 0.158848 * Group_Bprime
     - 0.000154 * Tolerance_Factor_x_Octahedral_Mismatch
     - 1.805980 * EN_Bprime
     + 0.086017 * (Tolerance_Factor)^2
```

### 2. Stage 2 Hurdle Non-Zero Interaction Regressor Formula

```text
Band Gap (eV) (Non-Zero) = +3.521799
     + 0.692900 * d_electrons_B
     - 0.377746 * Val_avg_x_EN_avg
     + 0.326122 * Group_Bprime
     + 1.383800 * (EN_avg)^2
     - 0.060866 * d_electrons_B_x_d_electrons_Bprime
     - 2.735675 * EN_Bprime
     - 2.797903 * (d_electrons_B_/_(Group_B))
     - 0.219663 * d_electrons_Bprime
     + 0.378538 * Val_avg
     + 1.591815 * (EN_Bprime_/_(EN_B))
     + 0.235172 * Val_B
     + 0.001366 * EN_avg_x_Volume_A3
     - 0.014002 * Group_B_x_Group_Bprime
     + 0.479105 * Tolerance_Factor
     + 0.167512 * Spin_Proxy_Distance
```

---

## Target Property: Total Magnetization (uB)

- **Stage 1 Non-Linear Classification Accuracy:** **81.90%**  
- **Stage 2 Non-Zero Sub $R^2$:** **56.23%**  
- **Direct Interaction $R^2$:** **35.15%**  
- **Two-Stage Hurdle Pipeline $R^2$:** **49.87%**  
- **Relative Theoretical Limit Achieved:** **83.12%**  

### 1. Direct Physical Interaction Formula (Top 15 Terms)

```text
Total Magnetization (uB) = -56.158716
     + 0.004207 * Tolerance_Factor_x_Octahedral_Mismatch
     - 15.276606 * (EN_avg)^2
     - 3.453970 * d_electrons_B
     - 1.439346 * Total_d_electrons
     + 28.738735 * EN_avg
     + 0.351100 * d_electrons_B_x_d_electrons_Bprime
     + 0.000000 * (Octahedral_Mismatch)^2
     + 1.103954 * (Shannon_Bprime_/_(Shannon_B))
     + 21.003685 * EN_Bprime
     + 0.000207 * Octahedral_Mismatch
     - 3.701429 * (d_BprimeO_/_(d_BO))
     + 1.843425 * Group_B
     + 21.726763 * (d_electrons_B_/_(Group_B))
     + 15.857515 * EN_B
     - 1.590745 * d_electrons_Bprime
```

### 2. Stage 2 Hurdle Non-Zero Interaction Regressor Formula

```text
Total Magnetization (uB) (Non-Zero) = -59.929080
     + 0.005796 * Tolerance_Factor_x_Octahedral_Mismatch
     - 18.217703 * (EN_avg)^2
     + 1.452440 * (Shannon_Bprime_/_(Shannon_B))
     + 32.196389 * EN_avg
     + 27.059752 * EN_Bprime
     + 1.963132 * Val_avg_x_EN_avg
     + 0.000245 * Octahedral_Mismatch
     - 0.000063 * Octahedral_Mismatch_x_Density_g_cm3
     + 0.000000 * (Octahedral_Mismatch)^2
     - 4.311678 * (d_BprimeO_/_(d_BO))
     - 2.581926 * d_electrons_B
     - 0.516390 * Total_HS_FiM_x_Total_d_electrons
     - 2.034379 * d_BprimeO
     - 2.034379 * Shannon_Bprime
     - 3.932387 * d_avg
```

---

## Target Property: Energy Above Hull (eV)

- **Stage 1 Non-Linear Classification Accuracy:** **84.50%**  
- **Stage 2 Non-Zero Sub $R^2$:** **9.49%**  
- **Direct Interaction $R^2$:** **10.47%**  
- **Two-Stage Hurdle Pipeline $R^2$:** **12.34%**  
- **Relative Theoretical Limit Achieved:** **49.37%**  

### 1. Direct Physical Interaction Formula (Top 15 Terms)

```text
Energy Above Hull (eV) = +0.595590
     + 0.077133 * Group_B
     - 0.166419 * Density_g_cm3
     + 0.196807 * (EN_avg)^2
     - 0.000045 * Tolerance_Factor_x_Octahedral_Mismatch
     - 0.000000 * (Octahedral_Mismatch)^2
     - 0.103343 * (d_BprimeO_/_(d_BO))
     - 0.226663 * (Group_B_/_(Val_B))
     - 0.000005 * Octahedral_Mismatch
     - 0.157798 * Tolerance_Factor
     - 0.159285 * EN_B_x_EN_Bprime
     + 0.007881 * (Density_g_cm3)^2
     - 0.052014 * Val_B
     - 0.014412 * (Tolerance_Factor)^2
     - 0.000001 * Octahedral_Mismatch_x_Density_g_cm3
     - 0.002457 * Group_B_x_Group_Bprime
```

### 2. Stage 2 Hurdle Non-Zero Interaction Regressor Formula

```text
Energy Above Hull (eV) (Non-Zero) = +0.751137
     - 0.000068 * Tolerance_Factor_x_Octahedral_Mismatch
     - 0.000000 * (Octahedral_Mismatch)^2
     - 0.000008 * Octahedral_Mismatch
     - 0.151655 * Density_g_cm3
     + 0.219388 * (EN_avg)^2
     + 0.053934 * Group_B
     - 0.190015 * EN_B_x_EN_Bprime
     - 0.328222 * Tolerance_Factor
     - 0.224835 * (Group_B_/_(Val_B))
     - 0.000001 * Octahedral_Mismatch_x_Density_g_cm3
     - 0.099635 * (d_BprimeO_/_(d_BO))
     - 0.059060 * Val_B
     + 0.314766 * (EN_B_/_(EN_A))
     - 0.069983 * Shannon_B_x_Shannon_Bprime
     + 0.006859 * (Density_g_cm3)^2
```

---

## Target Property: Formation Energy (eV/atom)

- **Stage 1 Non-Linear Classification Accuracy:** **100.00%**  
- **Stage 2 Non-Zero Sub $R^2$:** **68.20%**  
- **Direct Interaction $R^2$:** **68.20%**  
- **Two-Stage Hurdle Pipeline $R^2$:** **68.20%**  
- **Relative Theoretical Limit Achieved:** **104.92%**  

### 1. Direct Physical Interaction Formula (Top 15 Terms)

```text
Formation Energy (eV/atom) = -3.590251
     + 0.030259 * d_electrons_B_x_d_electrons_Bprime
     + 0.143303 * Val_avg_x_EN_avg
     + 1.323970 * (EN_Bprime_/_(EN_B))
     + 1.051072 * (EN_B_/_(EN_A))
     + 0.119255 * Group_B
     - 1.175591 * EN_Bprime
     - 0.117044 * Spin_Proxy_Distance
     - 0.143156 * Val_B
     + 0.944518 * EN_A
     + 0.944518 * EN_Aprime
     - 0.190487 * Val_avg
     + 0.000011 * Octahedral_Mismatch
     - 0.349449 * Tolerance_Factor
     + 0.000000 * (Octahedral_Mismatch)^2
     - 0.023980 * Total_HS_FiM_x_Total_d_electrons
```

---

