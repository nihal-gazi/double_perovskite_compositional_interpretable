# Experiment 5: Hybrid Symbolic Decision Boundary Classifier + Optimal Top-K* Fourier Ensemble Regressor Report (Clean Physical Descriptors)

**Dataset:** `exp_v2/data/data_24_7_2026/double_perovskite_dataset.csv` (2,000 double perovskites)  
**Data Leakage Audit:** Removed `E_GNN`, `M_net`, `M_abs`. Evaluated on 33 pure physical/chemical descriptors.  
**Theoretical Limit References (Literature):** Formation Energy ($R^2_{\text{limit}} = 65.0\%$), Magnetization ($R^2_{\text{limit}} = 60.0\%$), Band Gap ($R^2_{\text{limit}} = 50.0\%$), Hull Energy ($R^2_{\text{limit}} = 25.0\%$).  

---

## Target Property: Band Gap (eV)

**Discovered Symbolic Decision Boundary Formula S(x):**  
```text
S(x) = log(add(add(d_AO, Density_g_cm3), neg(Total_HS_FM)))
```  
**Stage 1 Classification Metrics:** Accuracy = **63.25%** | F1-Score = **0.7637** | Precision = **0.6384** | Recall = **0.9504**

| Fourier Depth (D) | Stage 1 Symbolic Acc (%) | Stage 1 F1 | **Optimal Best K*** | Stage 2 Sub R² (%) | **Final Pipeline R² (%)** | **Theoretical Limit (%)** | Final MSE | Final MAE | Top Fourier Features (K*) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| D = 3 | 63.25% | 0.7637 | **K* = 6** | 21.27% | **-8.87%** | **0.00%** | 1.696331 | 1.1021 | `Spin_Proxy_Distance`, `Val_avg`, `Total_d_electrons` |
| D = 5 | 63.25% | 0.7637 | **K* = 7** | 24.49% | **-6.24%** | **0.00%** | 1.655439 | 1.0878 | `Spin_Proxy_Distance`, `Total_d_electrons`, `d_electrons_Bprime` |
| D = 10 | 63.25% | 0.7637 | **K* = 7** | 27.53% | **-3.38%** | **0.00%** | 1.610914 | 1.0697 | `Total_d_electrons`, `d_electrons_Bprime`, `Spin_Proxy_Distance` |
| D = 50 | 63.25% | 0.7637 | **K* = 6** | 33.33% | **-3.75%** | **0.00%** | 1.616618 | 1.0608 | `d_electrons_Bprime`, `Total_d_electrons`, `EN_Bprime` |
| D = 100 | 63.25% | 0.7637 | **K* = 4** | 37.54% | **-2.00%** | **0.00%** | 1.589310 | 1.0446 | `EN_avg`, `d_electrons_Bprime`, `Total_d_electrons` |

---

## Target Property: Total Magnetization (uB)

**Discovered Symbolic Decision Boundary Formula S(x):**  
```text
S(x) = sub(sub(log(neg(Group_Bprime)), add(neg(Shannon_Aprime), sub(d_BO, EN_Aprime))), neg(mul(abs(Group_B), sub(Group_B, Spin_Proxy_Distance))))
```  
**Stage 1 Classification Metrics:** Accuracy = **62.80%** | F1-Score = **0.7062** | Precision = **0.6358** | Recall = **0.7940**

| Fourier Depth (D) | Stage 1 Symbolic Acc (%) | Stage 1 F1 | **Optimal Best K*** | Stage 2 Sub R² (%) | **Final Pipeline R² (%)** | **Theoretical Limit (%)** | Final MSE | Final MAE | Top Fourier Features (K*) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| D = 3 | 62.80% | 0.7062 | **K* = 2** | 27.71% | **6.25%** | **10.42%** | 88.832252 | 5.7667 | `Volume_A3`, `EN_A` |
| D = 5 | 62.80% | 0.7062 | **K* = 2** | 31.52% | **8.84%** | **14.73%** | 86.382029 | 5.5930 | `Volume_A3`, `EN_A` |
| D = 10 | 62.80% | 0.7062 | **K* = 2** | 39.43% | **12.71%** | **21.18%** | 82.710911 | 5.3986 | `Volume_A3`, `EN_A` |
| D = 50 | 62.80% | 0.7062 | **K* = 3** | 51.41% | **23.16%** | **38.60%** | 72.808894 | 4.8194 | `Volume_A3`, `EN_A`, `EN_Aprime` |
| D = 100 | 62.80% | 0.7062 | **K* = 3** | 53.63% | **21.36%** | **35.59%** | 74.518183 | 4.7632 | `Volume_A3`, `EN_A`, `EN_Aprime` |

---

## Target Property: Energy Above Hull (eV)

**Discovered Symbolic Decision Boundary Formula S(x):**  
```text
S(x) = div(add(div(log(add(log(Spin_Proxy_Distance), log(Group_Bprime))), div(abs(abs(EN_avg)), neg(mul(EN_B, Group_B)))), abs(sub(abs(neg(EN_Bprime)), sub(abs(Val_B), div(Group_B, EN_A))))), neg(div(neg(neg(sub(d_AO, Tolerance_Factor))), abs(log(div(-0.536, Total_d_electrons))))))
```  
**Stage 1 Classification Metrics:** Accuracy = **72.45%** | F1-Score = **0.8328** | Precision = **0.7225** | Recall = **0.9828**

| Fourier Depth (D) | Stage 1 Symbolic Acc (%) | Stage 1 F1 | **Optimal Best K*** | Stage 2 Sub R² (%) | **Final Pipeline R² (%)** | **Theoretical Limit (%)** | Final MSE | Final MAE | Top Fourier Features (K*) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| D = 3 | 72.45% | 0.8328 | **K* = 2** | 3.47% | **1.69%** | **6.76%** | 0.072254 | 0.1094 | `EN_B`, `Volume_A3` |
| D = 5 | 72.45% | 0.8328 | **K* = 3** | 4.23% | **2.65%** | **10.62%** | 0.071546 | 0.1092 | `EN_B`, `Group_B`, `Volume_A3` |
| D = 10 | 72.45% | 0.8328 | **K* = 7** | 5.17% | **3.20%** | **12.79%** | 0.071146 | 0.1086 | `EN_B`, `Volume_A3`, `Group_B` |
| D = 50 | 72.45% | 0.8328 | **K* = 2** | 9.45% | **7.60%** | **30.39%** | 0.067913 | 0.1087 | `EN_B`, `Density_g_cm3` |
| D = 100 | 72.45% | 0.8328 | **K* = 10** | 9.91% | **2.89%** | **11.56%** | 0.071372 | 0.1084 | `Density_g_cm3`, `EN_avg`, `Volume_A3` |

---

## Target Property: Formation Energy (eV/atom)

**Discovered Symbolic Decision Boundary Formula S(x):**  
```text
S(x) = N/A (Continuous Baseline)
```  
**Stage 1 Classification Metrics:** Accuracy = **100.00%** | F1-Score = **1.0000** | Precision = **1.0000** | Recall = **1.0000**

| Fourier Depth (D) | Stage 1 Symbolic Acc (%) | Stage 1 F1 | **Optimal Best K*** | Stage 2 Sub R² (%) | **Final Pipeline R² (%)** | **Theoretical Limit (%)** | Final MSE | Final MAE | Top Fourier Features (K*) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| D = 3 | 100.00% | 1.0000 | **K* = 3** | 46.00% | **46.00%** | **70.77%** | 0.188390 | 0.2940 | `EN_avg`, `EN_B`, `EN_A` |
| D = 5 | 100.00% | 1.0000 | **K* = 4** | 48.32% | **48.32%** | **74.34%** | 0.180294 | 0.2817 | `EN_avg`, `EN_B`, `EN_A` |
| D = 10 | 100.00% | 1.0000 | **K* = 4** | 52.03% | **52.03%** | **80.04%** | 0.167367 | 0.2684 | `EN_A`, `EN_Aprime`, `EN_avg` |
| D = 50 | 100.00% | 1.0000 | **K* = 4** | 56.94% | **56.94%** | **87.59%** | 0.150237 | 0.2484 | `EN_avg`, `EN_A`, `EN_Aprime` |
| D = 100 | 100.00% | 1.0000 | **K* = 2** | 58.03% | **58.03%** | **89.27%** | 0.146437 | 0.2450 | `EN_avg`, `EN_A` |

---
