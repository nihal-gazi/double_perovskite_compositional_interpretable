# Experiment 8: Discovered Analytical Dual Symbolic Equations Report (with 'pow' operator)

This document presents the complete 100% interpretable analytical symbolic equations discovered by Genetic Programming (using primitive set with `pow`) on 33 pure physical chemical descriptors (with leaked GNN proxies `E_GNN`, `M_net`, `M_abs` removed).

---

## Target Property: Band Gap (eV)

- **Stage 1 Classification Accuracy:** **64.15%** (F1 = 0.7583)  
- **Stage 2 Non-Zero Subset $R^2$:** **15.14%**  
- **Final Combined Dual-SR Pipeline $R^2$:** **-13.18%** (MSE = 1.763539, MAE = 1.0838)  

### 1. Stage 1 Discovered Symbolic Decision Boundary Classifier Formula $S_{\text{cls}}(\mathbf{x})$

$$\widehat{y}_{\text{bin}} = 1 \quad \text{if } S_{\text{cls}}(\mathbf{x}) > 0.0 \quad \text{else } 0$$

```text
S_cls(x) = sub(abs(abs(sub(div(neg(Val_Aprime), log(Volume_A3)), mul(mul(EN_Bprime, Total_HS_FM), pow(EN_A, EN_Bprime))))), abs(neg(mul(sub(mul(Shannon_Bprime, Total_HS_FiM), neg(Tolerance_Factor)), sub(div(HS_moment_B, Shannon_Aprime), mul(Total_HS_FiM, HS_moment_Bprime))))))
```

### 2. Stage 2 Discovered Symbolic Non-Zero Regressor Formula $S_{\text{reg}}(\mathbf{x})$

```text
S_reg(x) = sub(log(div(div(log(div(-0.102, abs(EN_B))), -0.102), abs(EN_B))), sub(log(add(log(Density_g_cm3), Total_A_Charge)), pow(log(div(pow(log(-0.102), neg(abs(Total_HS_FiM))), abs(EN_B))), neg(abs(Total_HS_FiM)))))
```

### 3. Combined Dual-SR Hurdle System Analytical Formula

$$\widehat{y}_{\text{pipeline}}(\mathbf{x}) = \begin{cases} 0.0 & \text{if } S_{\text{cls}}(\mathbf{x}) \le 0.0 \\ \max\left(0.0, S_{\text{reg}}(\mathbf{x})\right) & \text{if } S_{\text{cls}}(\mathbf{x}) > 0.0 \end{cases}$$

---

## Target Property: Total Magnetization (uB)

- **Stage 1 Classification Accuracy:** **63.90%** (F1 = 0.7255)  
- **Stage 2 Non-Zero Subset $R^2$:** **6.89%**  
- **Final Combined Dual-SR Pipeline $R^2$:** **4.83%** (MSE = 90.172784, MAE = 4.8052)  

### 1. Stage 1 Discovered Symbolic Decision Boundary Classifier Formula $S_{\text{cls}}(\mathbf{x})$

$$\widehat{y}_{\text{bin}} = 1 \quad \text{if } S_{\text{cls}}(\mathbf{x}) > 0.0 \quad \text{else } 0$$

```text
S_cls(x) = log(pow(add(HS_moment_B, Total_HS_FiM), mul(Val_A, Group_Bprime)))
```

### 2. Stage 2 Discovered Symbolic Non-Zero Regressor Formula $S_{\text{reg}}(\mathbf{x})$

```text
S_reg(x) = pow(log(pow(div(div(div(div(pow(Volume_A3, EN_Aprime), log(add(neg(sub(Density_g_cm3, EN_Aprime)), EN_B))), log(add(neg(sub(Density_g_cm3, EN_Aprime)), EN_B))), log(add(neg(neg(div(neg(sub(Shannon_A, Total_HS_FM)), sub(pow(d_electrons_B, Shannon_Aprime), log(Total_HS_FiM))))), EN_B))), log(add(neg(sub(sub(Density_g_cm3, EN_Aprime), EN_Aprime)), EN_B))), EN_Aprime)), log(Val_A))
```

### 3. Combined Dual-SR Hurdle System Analytical Formula

$$\widehat{y}_{\text{pipeline}}(\mathbf{x}) = \begin{cases} 0.0 & \text{if } S_{\text{cls}}(\mathbf{x}) \le 0.0 \\ \max\left(0.0, S_{\text{reg}}(\mathbf{x})\right) & \text{if } S_{\text{cls}}(\mathbf{x}) > 0.0 \end{cases}$$

---

## Target Property: Energy Above Hull (eV)

- **Stage 1 Classification Accuracy:** **71.45%** (F1 = 0.8167)  
- **Stage 2 Non-Zero Subset $R^2$:** **-1.37%**  
- **Final Combined Dual-SR Pipeline $R^2$:** **0.09%** (MSE = 0.073429, MAE = 0.0927)  

### 1. Stage 1 Discovered Symbolic Decision Boundary Classifier Formula $S_{\text{cls}}(\mathbf{x})$

$$\widehat{y}_{\text{bin}} = 1 \quad \text{if } S_{\text{cls}}(\mathbf{x}) > 0.0 \quad \text{else } 0$$

```text
S_cls(x) = log(add(pow(sub(add(d_BprimeO, Shannon_Bprime), abs(Total_HS_FM)), log(log(Total_d_electrons))), add(neg(abs(Shannon_Aprime)), log(mul(EN_Aprime, Val_B)))))
```

### 2. Stage 2 Discovered Symbolic Non-Zero Regressor Formula $S_{\text{reg}}(\mathbf{x})$

```text
S_reg(x) = 0.100
```

### 3. Combined Dual-SR Hurdle System Analytical Formula

$$\widehat{y}_{\text{pipeline}}(\mathbf{x}) = \begin{cases} 0.0 & \text{if } S_{\text{cls}}(\mathbf{x}) \le 0.0 \\ \max\left(0.0, S_{\text{reg}}(\mathbf{x})\right) & \text{if } S_{\text{cls}}(\mathbf{x}) > 0.0 \end{cases}$$

---

## Target Property: Formation Energy (eV/atom)

- **Stage 1 Classification Accuracy:** **100.00%** (F1 = 1.0000)  
- **Stage 2 Non-Zero Subset $R^2$:** **16.55%**  
- **Final Combined Dual-SR Pipeline $R^2$:** **16.55%** (MSE = 0.291136, MAE = 0.3522)  

### 1. Stage 1 Discovered Symbolic Decision Boundary Classifier Formula $S_{\text{cls}}(\mathbf{x})$

$$\widehat{y}_{\text{bin}} = 1 \quad \text{if } S_{\text{cls}}(\mathbf{x}) > 0.0 \quad \text{else } 0$$

```text
S_cls(x) = N/A (Continuous Baseline)
```

### 2. Stage 2 Discovered Symbolic Non-Zero Regressor Formula $S_{\text{reg}}(\mathbf{x})$

```text
S_reg(x) = neg(log(sub(sub(sub(sub(sub(div(Total_A_Charge, EN_Bprime), div(neg(Shannon_B), div(0.167, d_BO))), neg(sub(Total_A_Charge, d_electrons_B))), neg(abs(div(sub(Total_A_Charge, EN_Bprime), EN_Bprime)))), neg(div(0.948, d_electrons_B))), neg(neg(Shannon_B)))))
```

### 3. Combined Dual-SR Hurdle System Analytical Formula

$$\widehat{y}_{\text{pipeline}}(\mathbf{x}) = \begin{cases} 0.0 & \text{if } S_{\text{cls}}(\mathbf{x}) \le 0.0 \\ \max\left(0.0, S_{\text{reg}}(\mathbf{x})\right) & \text{if } S_{\text{cls}}(\mathbf{x}) > 0.0 \end{cases}$$

---

