# Experiment 11: Discovered Fitted Linear Regression Equations Report

This document contains the exact unscaled analytical linear regression equations fitted across all 4 target properties on 33 pure physical descriptors (with leaked GNN proxies `E_GNN`, `M_net`, `M_abs` removed).

---

## Target Property: Band Gap (eV)

- **Direct OLS $R^2$:** **16.33%**  
- **Two-Stage Hurdle Pipeline $R^2$:** **-8.27%**  
- **Relative Theoretical Limit Achieved:** **0.00%**  

### 1. Direct Single-Stage Linear Regression Formula

```text
Band Gap (eV) = +7.652122
     - 0.050215 * EN_A
     - 0.050215 * EN_Aprime
     - 0.556853 * EN_B
     + 0.071082 * EN_Bprime
     - 0.415430 * EN_avg
     - 0.006417 * Shannon_A
     - 0.006417 * Shannon_Aprime
     - 0.045424 * Shannon_B
     + 0.004240 * Shannon_Bprime
     - 0.108353 * Tolerance_Factor
     + 0.000004 * Octahedral_Mismatch
     - 0.286646 * Val_A
     - 0.286646 * Val_Aprime
     + 0.007021 * Val_B
     - 0.083042 * Val_Bprime
     - 0.065318 * Val_avg
     - 0.143323 * Total_A_Charge
     - 0.416086 * Group_B
     - 0.159290 * Group_Bprime
     + 0.472674 * d_electrons_B
     - 0.032080 * d_electrons_Bprime
     + 0.108237 * Total_d_electrons
     - 0.004485 * Spin_Proxy_Distance
     + 0.025532 * HS_moment_B
     + 0.019455 * HS_moment_Bprime
     + 0.014596 * Total_HS_FM
     - 0.322458 * Total_HS_FiM
     - 0.006417 * d_AO
     - 0.045424 * d_BO
     + 0.004240 * d_BprimeO
     + 0.007839 * d_avg
     + 0.000269 * Volume_A3
     - 0.002848 * Density_g_cm3
```

### 2. Stage 2 Hurdle Non-Zero Linear Regressor Formula

```text
Band Gap (eV) (Non-Zero) = +4.275097
     - 0.125344 * EN_A
     - 0.125344 * EN_Aprime
     - 0.363882 * EN_B
     - 0.041196 * EN_Bprime
     - 0.341328 * EN_avg
     - 0.028640 * Shannon_A
     - 0.028640 * Shannon_Aprime
     + 0.077131 * Shannon_B
     + 0.015553 * Shannon_Bprime
     + 0.108355 * Tolerance_Factor
     + 0.000007 * Octahedral_Mismatch
     - 0.107438 * Val_A
     - 0.107438 * Val_Aprime
     + 0.012847 * Val_B
     - 0.081432 * Val_Bprime
     - 0.054761 * Val_avg
     - 0.053719 * Total_A_Charge
     - 0.431676 * Group_B
     + 0.372721 * Group_Bprime
     + 0.819396 * d_electrons_B
     - 0.714063 * d_electrons_Bprime
     - 0.069280 * Total_d_electrons
     + 0.093622 * Spin_Proxy_Distance
     + 0.059463 * HS_moment_B
     + 0.120669 * HS_moment_Bprime
     + 0.058293 * Total_HS_FM
     - 0.372704 * Total_HS_FiM
     - 0.028640 * d_AO
     + 0.077131 * d_BO
     + 0.015553 * d_BprimeO
     + 0.030942 * d_avg
     + 0.000088 * Volume_A3
     - 0.008540 * Density_g_cm3
```

---

## Target Property: Total Magnetization (uB)

- **Direct OLS $R^2$:** **26.63%**  
- **Two-Stage Hurdle Pipeline $R^2$:** **15.50%**  
- **Relative Theoretical Limit Achieved:** **25.84%**  

### 1. Direct Single-Stage Linear Regression Formula

```text
Total Magnetization (uB) = -32.386523
     + 1.615566 * EN_A
     + 1.615566 * EN_Aprime
     + 2.070333 * EN_B
     + 0.438667 * EN_Bprime
     + 2.060680 * EN_avg
     + 0.039639 * Shannon_A
     + 0.039639 * Shannon_Aprime
     + 0.256900 * Shannon_B
     - 1.173003 * Shannon_Bprime
     + 0.627120 * Tolerance_Factor
     - 0.000349 * Octahedral_Mismatch
     + 2.669228 * Val_A
     + 2.669228 * Val_Aprime
     - 0.272235 * Val_B
     + 0.164000 * Val_Bprime
     - 0.124041 * Val_avg
     + 1.334614 * Total_A_Charge
     + 2.253803 * Group_B
     + 1.106529 * Group_Bprime
     - 2.382754 * d_electrons_B
     - 0.332339 * d_electrons_Bprime
     - 0.721148 * Total_d_electrons
     + 0.056329 * Spin_Proxy_Distance
     + 1.201891 * HS_moment_B
     - 0.803945 * HS_moment_Bprime
     + 0.113621 * Total_HS_FM
     + 0.930787 * Total_HS_FiM
     + 0.039639 * d_AO
     + 0.256900 * d_BO
     - 1.173003 * d_BprimeO
     - 2.284301 * d_avg
     + 0.020662 * Volume_A3
     - 0.168907 * Density_g_cm3
```

### 2. Stage 2 Hurdle Non-Zero Linear Regressor Formula

```text
Total Magnetization (uB) (Non-Zero) = -54.046121
     + 2.249979 * EN_A
     + 2.249979 * EN_Aprime
     + 1.130148 * EN_B
     + 1.863211 * EN_Bprime
     + 2.364333 * EN_avg
     + 0.054161 * Shannon_A
     + 0.054161 * Shannon_Aprime
     + 1.259710 * Shannon_B
     - 1.956422 * Shannon_Bprime
     + 0.174864 * Tolerance_Factor
     - 0.000558 * Octahedral_Mismatch
     + 4.032181 * Val_A
     + 4.032181 * Val_Aprime
     - 0.487450 * Val_B
     + 0.074545 * Val_Bprime
     - 0.409694 * Val_avg
     + 2.016091 * Total_A_Charge
     + 3.887633 * Group_B
     + 3.140496 * Group_Bprime
     - 2.768815 * d_electrons_B
     - 1.726061 * d_electrons_Bprime
     - 1.333026 * Total_d_electrons
     - 0.324279 * Spin_Proxy_Distance
     + 1.868734 * HS_moment_B
     - 1.706120 * HS_moment_Bprime
     + 0.014453 * Total_HS_FM
     + 0.459988 * Total_HS_FiM
     + 0.054161 * d_AO
     + 1.259710 * d_BO
     - 1.956422 * d_BprimeO
     - 3.814440 * d_avg
     + 0.034436 * Volume_A3
     + 0.182395 * Density_g_cm3
```

---

## Target Property: Energy Above Hull (eV)

- **Direct OLS $R^2$:** **6.57%**  
- **Two-Stage Hurdle Pipeline $R^2$:** **5.41%**  
- **Relative Theoretical Limit Achieved:** **21.62%**  

### 1. Direct Single-Stage Linear Regression Formula

```text
Energy Above Hull (eV) = -0.250145
     + 0.048101 * EN_A
     + 0.048101 * EN_Aprime
     + 0.097209 * EN_B
     - 0.051864 * EN_Bprime
     + 0.043550 * EN_avg
     + 0.000410 * Shannon_A
     + 0.000410 * Shannon_Aprime
     + 0.072692 * Shannon_B
     - 0.010440 * Shannon_Bprime
     + 0.025535 * Tolerance_Factor
     - 0.000003 * Octahedral_Mismatch
     + 0.031637 * Val_A
     + 0.031637 * Val_Aprime
     - 0.005898 * Val_B
     - 0.002838 * Val_Bprime
     - 0.008244 * Val_avg
     + 0.015819 * Total_A_Charge
     + 0.037229 * Group_B
     - 0.003639 * Group_Bprime
     - 0.040199 * d_electrons_B
     + 0.028707 * d_electrons_Bprime
     + 0.000024 * Total_d_electrons
     - 0.010256 * Spin_Proxy_Distance
     - 0.007756 * HS_moment_B
     - 0.006443 * HS_moment_Bprime
     - 0.004612 * Total_HS_FM
     - 0.005319 * Total_HS_FiM
     + 0.000410 * d_AO
     + 0.072692 * d_BO
     - 0.010440 * d_BprimeO
     - 0.019671 * d_avg
     - 0.000160 * Volume_A3
     - 0.034367 * Density_g_cm3
```

### 2. Stage 2 Hurdle Non-Zero Linear Regressor Formula

```text
Energy Above Hull (eV) (Non-Zero) = -0.047599
     + 0.035763 * EN_A
     + 0.035763 * EN_Aprime
     + 0.094178 * EN_B
     - 0.033385 * EN_Bprime
     + 0.051750 * EN_avg
     + 0.005093 * Shannon_A
     + 0.005093 * Shannon_Aprime
     + 0.076346 * Shannon_B
     - 0.016515 * Shannon_Bprime
     - 0.030049 * Tolerance_Factor
     - 0.000005 * Octahedral_Mismatch
     + 0.025459 * Val_A
     + 0.025459 * Val_Aprime
     - 0.008408 * Val_B
     - 0.002021 * Val_Bprime
     - 0.010111 * Val_avg
     + 0.012729 * Total_A_Charge
     + 0.016884 * Group_B
     - 0.000202 * Group_Bprime
     - 0.004383 * d_electrons_B
     + 0.010925 * d_electrons_Bprime
     + 0.002684 * Total_d_electrons
     - 0.014712 * Spin_Proxy_Distance
     - 0.006242 * HS_moment_B
     - 0.009543 * HS_moment_Bprime
     - 0.005201 * Total_HS_FM
     - 0.010254 * Total_HS_FiM
     + 0.005093 * d_AO
     + 0.076346 * d_BO
     - 0.016515 * d_BprimeO
     - 0.031293 * d_avg
     - 0.000189 * Volume_A3
     - 0.033096 * Density_g_cm3
```

---

## Target Property: Formation Energy (eV/atom)

- **Direct OLS $R^2$:** **61.41%**  
- **Two-Stage Hurdle Pipeline $R^2$:** **61.41%**  
- **Relative Theoretical Limit Achieved:** **94.48%**  

### 1. Direct Single-Stage Linear Regression Formula

```text
Formation Energy (eV/atom) = -5.095832
     + 0.421190 * EN_A
     + 0.421190 * EN_Aprime
     + 0.157028 * EN_B
     + 0.186432 * EN_Bprime
     + 0.268756 * EN_avg
     + 0.010798 * Shannon_A
     + 0.010798 * Shannon_Aprime
     + 0.149406 * Shannon_B
     + 0.076855 * Shannon_Bprime
     - 0.050848 * Tolerance_Factor
     + 0.000024 * Octahedral_Mismatch
     - 0.134252 * Val_A
     - 0.134252 * Val_Aprime
     + 0.006371 * Val_B
     + 0.010079 * Val_Bprime
     + 0.015002 * Val_avg
     - 0.067126 * Total_A_Charge
     + 0.030306 * Group_B
     + 0.002315 * Group_Bprime
     + 0.024144 * d_electrons_B
     + 0.016942 * d_electrons_Bprime
     + 0.012130 * Total_d_electrons
     - 0.045219 * Spin_Proxy_Distance
     + 0.010425 * HS_moment_B
     - 0.016076 * HS_moment_Bprime
     - 0.002050 * Total_HS_FM
     + 0.020861 * Total_HS_FiM
     + 0.010798 * d_AO
     + 0.149406 * d_BO
     + 0.076855 * d_BprimeO
     + 0.151225 * d_avg
     - 0.000269 * Volume_A3
     - 0.011271 * Density_g_cm3
```

---

