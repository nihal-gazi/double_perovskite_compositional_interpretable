# Experiment 9: Discovered Analytical Dual Symbolic Equations Report (19 Extended Operators)

This document presents the complete 100% interpretable analytical symbolic equations discovered by Genetic Programming (using 19 extended mathematical operators) on 33 pure physical chemical descriptors (with leaked GNN proxies `E_GNN`, `M_net`, `M_abs` removed).

---

## Target Property: Band Gap (eV)

- **Stage 1 Classification Accuracy:** **63.80%** (F1 = 0.7736)  
- **Stage 2 Non-Zero Subset $R^2$:** **27.82%**  
- **Final Combined Dual-SR Pipeline $R^2$:** **-8.61%** (MSE = 1.692378, MAE = 1.0628)  

### 1. Stage 1 Discovered Symbolic Decision Boundary Classifier Formula $S_{\text{cls}}(\mathbf{x})$

$$\widehat{y}_{\text{bin}} = 1 \quad \text{if } S_{\text{cls}}(\mathbf{x}) > 0.0 \quad \text{else } 0$$

```text
S_cls(x) = mod(tan(nth_root(sec(Group_Bprime), mod(Spin_Proxy_Distance, Tolerance_Factor))), log(mod(sign(Val_B), pow(d_electrons_Bprime, EN_avg))))
```

### 2. Stage 2 Discovered Symbolic Non-Zero Regressor Formula $S_{\text{reg}}(\mathbf{x})$

```text
S_reg(x) = nth_root(ceil(nth_root(ceil(nth_root(ceil(nth_root(nth_root(exp(cos(log(EN_avg))), nth_root(Group_B, Density_g_cm3)), ceil(tan(Shannon_Bprime)))), div(abs(EN_A), sin(ceil(tan(Shannon_Bprime)))))), div(div(tan(Shannon_Bprime), nth_root(Total_HS_FM, Density_g_cm3)), sin(div(ceil(tan(Shannon_Bprime)), EN_A))))), sub(mod(Val_avg, d_AO), exp(Total_HS_FiM)))
```

### 3. Combined Dual-SR Hurdle System Analytical Formula

$$\widehat{y}_{\text{pipeline}}(\mathbf{x}) = \begin{cases} 0.0 & \text{if } S_{\text{cls}}(\mathbf{x}) \le 0.0 \\ \max\left(0.0, S_{\text{reg}}(\mathbf{x})\right) & \text{if } S_{\text{cls}}(\mathbf{x}) > 0.0 \end{cases}$$

---

## Target Property: Total Magnetization (uB)

- **Stage 1 Classification Accuracy:** **63.00%** (F1 = 0.6463)  
- **Stage 2 Non-Zero Subset $R^2$:** **35.44%**  
- **Final Combined Dual-SR Pipeline $R^2$:** **-4.27%** (MSE = 98.796864, MAE = 4.7329)  

### 1. Stage 1 Discovered Symbolic Decision Boundary Classifier Formula $S_{\text{cls}}(\mathbf{x})$

$$\widehat{y}_{\text{bin}} = 1 \quad \text{if } S_{\text{cls}}(\mathbf{x}) > 0.0 \quad \text{else } 0$$

```text
S_cls(x) = mul(sec(Val_avg), sign(Volume_A3))
```

### 2. Stage 2 Discovered Symbolic Non-Zero Regressor Formula $S_{\text{reg}}(\mathbf{x})$

```text
S_reg(x) = mul(EN_Aprime, add(sin(ceil(div(mul(EN_Aprime, Val_A), Shannon_Bprime))), add(sin(log(Volume_A3)), add(sin(mul(log(Volume_A3), add(div(EN_Aprime, Shannon_Bprime), cosec(Val_Aprime)))), add(sin(mul(EN_Aprime, add(div(EN_Aprime, Shannon_Bprime), cosec(Val_Aprime)))), add(sin(log(Volume_A3)), add(sin(add(sin(log(Volume_A3)), cosec(Val_Aprime))), add(sin(mul(EN_Aprime, add(sin(mul(EN_Aprime, add(sin(ceil(log(Volume_A3))), mul(div(EN_Aprime, Shannon_Bprime), Val_A)))), log(Volume_A3)))), add(sin(log(Volume_A3)), add(add(sin(sin(add(sin(log(Volume_A3)), add(sin(sin(add(sin(ceil(log(Volume_A3))), sin(ceil(log(Volume_A3)))))), add(sin(ceil(div(mul(EN_Aprime, Val_A), Shannon_Bprime))), add(div(mul(EN_Aprime, Val_A), Shannon_Bprime), sin(mul(log(Volume_A3), add(div(EN_Aprime, Shannon_Bprime), cosec(Val_Aprime)))))))))), add(sin(log(Volume_A3)), add(sin(log(Volume_A3)), add(add(sin(sin(sin(ceil(mul(EN_Aprime, Val_A))))), ceil(add(sin(log(Volume_A3)), add(add(sin(sin(log(Volume_A3))), ceil(add(div(EN_Aprime, Shannon_Bprime), cosec(Val_Aprime)))), cosec(Shannon_B))))), cosec(Shannon_B))))), cosec(Shannon_B)))))))))))
```

### 3. Combined Dual-SR Hurdle System Analytical Formula

$$\widehat{y}_{\text{pipeline}}(\mathbf{x}) = \begin{cases} 0.0 & \text{if } S_{\text{cls}}(\mathbf{x}) \le 0.0 \\ \max\left(0.0, S_{\text{reg}}(\mathbf{x})\right) & \text{if } S_{\text{cls}}(\mathbf{x}) > 0.0 \end{cases}$$

---

## Target Property: Energy Above Hull (eV)

- **Stage 1 Classification Accuracy:** **72.20%** (F1 = 0.8305)  
- **Stage 2 Non-Zero Subset $R^2$:** **-5.27%**  
- **Final Combined Dual-SR Pipeline $R^2$:** **-1.39%** (MSE = 0.074519, MAE = 0.0853)  

### 1. Stage 1 Discovered Symbolic Decision Boundary Classifier Formula $S_{\text{cls}}(\mathbf{x})$

$$\widehat{y}_{\text{bin}} = 1 \quad \text{if } S_{\text{cls}}(\mathbf{x}) > 0.0 \quad \text{else } 0$$

```text
S_cls(x) = mod(d_AO, d_electrons_B)
```

### 2. Stage 2 Discovered Symbolic Non-Zero Regressor Formula $S_{\text{reg}}(\mathbf{x})$

```text
S_reg(x) = 0.065
```

### 3. Combined Dual-SR Hurdle System Analytical Formula

$$\widehat{y}_{\text{pipeline}}(\mathbf{x}) = \begin{cases} 0.0 & \text{if } S_{\text{cls}}(\mathbf{x}) \le 0.0 \\ \max\left(0.0, S_{\text{reg}}(\mathbf{x})\right) & \text{if } S_{\text{cls}}(\mathbf{x}) > 0.0 \end{cases}$$

---

## Target Property: Formation Energy (eV/atom)

- **Stage 1 Classification Accuracy:** **100.00%** (F1 = 1.0000)  
- **Stage 2 Non-Zero Subset $R^2$:** **28.56%**  
- **Final Combined Dual-SR Pipeline $R^2$:** **28.56%** (MSE = 0.249223, MAE = 0.3543)  

### 1. Stage 1 Discovered Symbolic Decision Boundary Classifier Formula $S_{\text{cls}}(\mathbf{x})$

$$\widehat{y}_{\text{bin}} = 1 \quad \text{if } S_{\text{cls}}(\mathbf{x}) > 0.0 \quad \text{else } 0$$

```text
S_cls(x) = N/A (Continuous Baseline)
```

### 2. Stage 2 Discovered Symbolic Non-Zero Regressor Formula $S_{\text{reg}}(\mathbf{x})$

```text
S_reg(x) = sub(log(EN_Aprime), exp(sec(gaussian_function(sec(exp(sec(sin(EN_avg))))))))
```

### 3. Combined Dual-SR Hurdle System Analytical Formula

$$\widehat{y}_{\text{pipeline}}(\mathbf{x}) = \begin{cases} 0.0 & \text{if } S_{\text{cls}}(\mathbf{x}) \le 0.0 \\ \max\left(0.0, S_{\text{reg}}(\mathbf{x})\right) & \text{if } S_{\text{cls}}(\mathbf{x}) > 0.0 \end{cases}$$

---

