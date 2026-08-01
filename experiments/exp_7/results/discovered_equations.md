# Experiment 7: Discovered Analytical Dual Symbolic Equations Report (Clean Physical Descriptors)

This document presents the complete 100% interpretable analytical symbolic equations discovered by Genetic Programming on 33 pure physical chemical descriptors (with leaked GNN proxies `E_GNN`, `M_net`, `M_abs` removed).

---

## Target Property: Band Gap (eV)

- **Stage 1 Classification Accuracy:** **63.25%** (F1 = 0.7637)  
- **Stage 2 Non-Zero Subset $R^2$:** **7.29%**  
- **Final Combined Dual-SR Pipeline $R^2$:** **-18.59%** (MSE = 1.847809, MAE = 1.1493)  

### 1. Stage 1 Discovered Symbolic Decision Boundary Classifier Formula $S_{\text{cls}}(\mathbf{x})$

$$\widehat{y}_{\text{bin}} = 1 \quad \text{if } S_{\text{cls}}(\mathbf{x}) > 0.0 \quad \text{else } 0$$

```text
S_cls(x) = log(add(add(d_AO, Density_g_cm3), neg(Total_HS_FM)))
```

### 2. Stage 2 Discovered Symbolic Non-Zero Regressor Formula $S_{\text{reg}}(\mathbf{x})$

```text
S_reg(x) = add(div(Spin_Proxy_Distance, Group_B), div(EN_A, EN_Aprime))
```

### 3. Combined Dual-SR Hurdle System Analytical Formula

$$\widehat{y}_{\text{pipeline}}(\mathbf{x}) = \begin{cases} 0.0 & \text{if } S_{\text{cls}}(\mathbf{x}) \le 0.0 \\ \max\left(0.0, S_{\text{reg}}(\mathbf{x})\right) & \text{if } S_{\text{cls}}(\mathbf{x}) > 0.0 \end{cases}$$

---

## Target Property: Total Magnetization (uB)

- **Stage 1 Classification Accuracy:** **62.80%** (F1 = 0.7062)  
- **Stage 2 Non-Zero Subset $R^2$:** **-0.29%**  
- **Final Combined Dual-SR Pipeline $R^2$:** **0.16%** (MSE = 94.603435, MAE = 5.0762)  

### 1. Stage 1 Discovered Symbolic Decision Boundary Classifier Formula $S_{\text{cls}}(\mathbf{x})$

$$\widehat{y}_{\text{bin}} = 1 \quad \text{if } S_{\text{cls}}(\mathbf{x}) > 0.0 \quad \text{else } 0$$

```text
S_cls(x) = sub(sub(log(neg(Group_Bprime)), add(neg(Shannon_Aprime), sub(d_BO, EN_Aprime))), neg(mul(abs(Group_B), sub(Group_B, Spin_Proxy_Distance))))
```

### 2. Stage 2 Discovered Symbolic Non-Zero Regressor Formula $S_{\text{reg}}(\mathbf{x})$

```text
S_reg(x) = mul(Total_A_Charge, EN_Aprime)
```

### 3. Combined Dual-SR Hurdle System Analytical Formula

$$\widehat{y}_{\text{pipeline}}(\mathbf{x}) = \begin{cases} 0.0 & \text{if } S_{\text{cls}}(\mathbf{x}) \le 0.0 \\ \max\left(0.0, S_{\text{reg}}(\mathbf{x})\right) & \text{if } S_{\text{cls}}(\mathbf{x}) > 0.0 \end{cases}$$

---

## Target Property: Energy Above Hull (eV)

- **Stage 1 Classification Accuracy:** **72.45%** (F1 = 0.8328)  
- **Stage 2 Non-Zero Subset $R^2$:** **-1.37%**  
- **Final Combined Dual-SR Pipeline $R^2$:** **0.15%** (MSE = 0.073389, MAE = 0.0953)  

### 1. Stage 1 Discovered Symbolic Decision Boundary Classifier Formula $S_{\text{cls}}(\mathbf{x})$

$$\widehat{y}_{\text{bin}} = 1 \quad \text{if } S_{\text{cls}}(\mathbf{x}) > 0.0 \quad \text{else } 0$$

```text
S_cls(x) = div(add(div(log(add(log(Spin_Proxy_Distance), log(Group_Bprime))), div(abs(abs(EN_avg)), neg(mul(EN_B, Group_B)))), abs(sub(abs(neg(EN_Bprime)), sub(abs(Val_B), div(Group_B, EN_A))))), neg(div(neg(neg(sub(d_AO, Tolerance_Factor))), abs(log(div(-0.536, Total_d_electrons))))))
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
- **Stage 2 Non-Zero Subset $R^2$:** **3.02%**  
- **Final Combined Dual-SR Pipeline $R^2$:** **3.02%** (MSE = 0.338330, MAE = 0.4168)  

### 1. Stage 1 Discovered Symbolic Decision Boundary Classifier Formula $S_{\text{cls}}(\mathbf{x})$

$$\widehat{y}_{\text{bin}} = 1 \quad \text{if } S_{\text{cls}}(\mathbf{x}) > 0.0 \quad \text{else } 0$$

```text
S_cls(x) = N/A (Continuous Baseline)
```

### 2. Stage 2 Discovered Symbolic Non-Zero Regressor Formula $S_{\text{reg}}(\mathbf{x})$

```text
S_reg(x) = sub(-0.411, d_BO)
```

### 3. Combined Dual-SR Hurdle System Analytical Formula

$$\widehat{y}_{\text{pipeline}}(\mathbf{x}) = \begin{cases} 0.0 & \text{if } S_{\text{cls}}(\mathbf{x}) \le 0.0 \\ \max\left(0.0, S_{\text{reg}}(\mathbf{x})\right) & \text{if } S_{\text{cls}}(\mathbf{x}) > 0.0 \end{cases}$$

---

