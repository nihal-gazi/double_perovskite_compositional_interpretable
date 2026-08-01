# Experiment 14: Discovered 100% Analytical Physical Equations Report

This document contains the 100% fully interpretable analytical mathematical equations discovered for both Stage 1 Decision Boundaries and Stage 2 Magnitude Equations across all 4 target properties.

---

## Target Property: Band Gap (eV)

- **Stage 1 Analytical Classification Accuracy:** **68.20%**  
- **Stage 2 Non-Zero Sub $R^2$:** **36.70%**  
- **Direct Multi-Operator $R^2$:** **28.84%**  
- **Two-Stage Hurdle Pipeline $R^2$:** **8.11%**  
- **Relative Theoretical Limit Achieved:** **16.21%**  

### 1. Stage 1 Analytical Log-Odds Decision Boundary Formula

```text
S_cls(x) = -15.617326
     - 0.704201 * Val_avg_x_EN_avg
     + 2.160329 * sqrt(Total_d_electrons)
     + 0.158785 * Total_HS_FiM_x_Total_d_electrons
     - 1.581856 * log(Total_d_electrons+1)
     - 0.012520 * Total_HS_FiM_x_Total_d_electrons_x_Spin_Proxy_Distance
     + 9.963633 * sqrt(EN_avg)
     + 4.599708 * sqrt(Tolerance_Factor)
     - 0.005178 * Volume_A3
     + 0.397531 * Val_B
     + 0.453968 * Val_avg

Predict Active Non-Zero (Band Gap (eV) > 0) IF S_cls(x) > 0.4200
```

### 2. Stage 2 Hurdle Non-Zero Interaction Regressor Formula

```text
Band Gap (eV) (Non-Zero) = -2.823476
     + 1.718545 * sqrt(Total_d_electrons)
     + 0.489629 * Spin_Proxy_Distance
     - 0.393333 * Val_avg_x_EN_avg
     + 0.114483 * Total_HS_FiM_x_Total_d_electrons
     + 1.398599 * (EN_avg)^2
     - 0.000131 * Tolerance_Factor_x_Octahedral_Mismatch_x_EN_avg
     - 0.053575 * d_electrons_B_x_d_electrons_Bprime
     - 1.019088 * Total_HS_FiM
     + 0.239399 * Group_Bprime
     - 0.286781 * d_electrons_Bprime
     + 0.344968 * d_electrons_B
     - 3.143642 * (d_electrons_B_/_(Group_B))
     - 0.021279 * Group_B_x_Group_Bprime
     + 3.148294 * sqrt(Tolerance_Factor)
     - 2.413147 * EN_Bprime
```

---

## Target Property: Total Magnetization (uB)

- **Stage 1 Analytical Classification Accuracy:** **72.30%**  
- **Stage 2 Non-Zero Sub $R^2$:** **58.83%**  
- **Direct Multi-Operator $R^2$:** **37.23%**  
- **Two-Stage Hurdle Pipeline $R^2$:** **28.40%**  
- **Relative Theoretical Limit Achieved:** **47.33%**  

### 1. Stage 1 Analytical Log-Odds Decision Boundary Formula

```text
S_cls(x) = -0.833337
     - 3.628252 * sqrt(Total_d_electrons)
     - 0.246029 * Total_HS_FiM_x_Total_d_electrons
     + 0.499236 * Val_avg_x_EN_avg
     + 1.306545 * Density_g_cm3
     - 0.606928 * EN_avg_x_Density_g_cm3
     + 0.212416 * Total_HS_FiM_x_Spin_Proxy_Distance
     - 0.891831 * (d_BprimeO_/_(d_BO))
     + 1.537999 * log(Total_d_electrons+1)
     + 0.000168 * Tolerance_Factor_x_Octahedral_Mismatch_x_EN_avg
     + 0.411012 * d_electrons_Bprime

Predict Active Non-Zero (Total Magnetization (uB) > 0) IF S_cls(x) > 0.4300
```

### 2. Stage 2 Hurdle Non-Zero Interaction Regressor Formula

```text
Total Magnetization (uB) (Non-Zero) = -178.403534
     + 0.001276 * Tolerance_Factor_x_Density_g_cm3_x_Octahedral_Mismatch
     + 0.004120 * Tolerance_Factor_x_Octahedral_Mismatch
     - 0.001919 * Tolerance_Factor_x_Octahedral_Mismatch_x_EN_avg
     - 14.901271 * (EN_avg)^2
     + 0.000054 * (Volume_A3)^2
     + 0.027987 * EN_avg_x_Volume_A3
     - 0.049931 * Volume_A3
     + 105.067933 * sqrt(EN_avg)
     + 14.389328 * log(Volume_A3+1)
     - 2.933637 * d_electrons_B
     - 0.586884 * Total_HS_FiM_x_Total_d_electrons
     - 1.455678 * Total_d_electrons
     + 1.092467 * (Shannon_Bprime_/_(Shannon_B))
     + 24.059951 * (d_electrons_B_/_(Group_B))
     - 0.008125 * EN_B_x_EN_Bprime_x_Volume_A3
```

---

## Target Property: Energy Above Hull (eV)

- **Stage 1 Analytical Classification Accuracy:** **80.30%**  
- **Stage 2 Non-Zero Sub $R^2$:** **10.49%**  
- **Direct Multi-Operator $R^2$:** **11.72%**  
- **Two-Stage Hurdle Pipeline $R^2$:** **11.96%**  
- **Relative Theoretical Limit Achieved:** **47.83%**  

### 1. Stage 1 Analytical Log-Odds Decision Boundary Formula

```text
S_cls(x) = +46.974598
     + 0.930673 * Group_B
     - 4.593814 * log(Volume_A3+1)
     + 0.012796 * Volume_A3
     + 0.725809 * EN_avg_x_Density_g_cm3
     + 0.432549 * Group_Bprime
     - 0.554860 * d_electrons_B
     - 0.369098 * Val_avg_x_EN_avg
     + 1.267851 * (EN_avg)^2
     - 5.047171 * sqrt(Tolerance_Factor)
     - 10.647384 * sqrt(EN_avg)

Predict Active Non-Zero (Energy Above Hull (eV) > 0) IF S_cls(x) > 0.4700
```

### 2. Stage 2 Hurdle Non-Zero Interaction Regressor Formula

```text
Energy Above Hull (eV) (Non-Zero) = +3.131970
     - 0.000000 * (Octahedral_Mismatch)^2
     - 0.000008 * Octahedral_Mismatch
     - 0.000002 * Octahedral_Mismatch_x_Density_g_cm3
     + 0.065196 * Spin_Proxy_Distance
     - 0.228382 * EN_B_x_EN_Bprime
     + 0.194258 * (EN_avg)^2
     - 0.213426 * (Group_B_/_(Val_B))
     + 0.044040 * Group_B
     + 0.118247 * sqrt(Total_d_electrons)
     - 0.236924 * sqrt(Total_HS_FiM)
     - 0.099490 * (d_BprimeO_/_(d_BO))
     - 0.082081 * Shannon_B_x_Shannon_Bprime
     - 0.058672 * Val_B
     + 0.277115 * log(Total_HS_FiM+1)
     - 0.003253 * Group_B_x_Group_Bprime
```

---

## Target Property: Formation Energy (eV/atom)

- **Stage 1 Analytical Classification Accuracy:** **100.00%**  
- **Stage 2 Non-Zero Sub $R^2$:** **69.61%**  
- **Direct Multi-Operator $R^2$:** **69.61%**  
- **Two-Stage Hurdle Pipeline $R^2$:** **69.61%**  
- **Relative Theoretical Limit Achieved:** **107.10%**  

### 1. Direct Multi-Operator Interaction Formula

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

