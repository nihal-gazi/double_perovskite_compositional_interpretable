# Experiment 6: Hybrid Symbolic Decision Boundary Classifier (with 'pow') + Optimal Top-K* Fourier Ensemble Regressor Report (Clean Physical Descriptors)

**Dataset:** `exp_v2/data/data_24_7_2026/double_perovskite_dataset.csv` (2,000 double perovskites)  
**Data Leakage Audit:** Removed `E_GNN`, `M_net`, `M_abs`. Evaluated on 33 pure physical/chemical descriptors.  
**Theoretical Limit References (Literature):** Formation Energy ($R^2_{\text{limit}} = 65.0\%$), Magnetization ($R^2_{\text{limit}} = 60.0\%$), Band Gap ($R^2_{\text{limit}} = 50.0\%$), Hull Energy ($R^2_{\text{limit}} = 25.0\%$).  

---

## Target Property: Band Gap (eV)

**Discovered Symbolic Decision Boundary Formula S(x):**  
```text
S(x) = sub(abs(abs(sub(div(neg(Val_Aprime), log(Volume_A3)), mul(mul(EN_Bprime, Total_HS_FM), pow(EN_A, EN_Bprime))))), abs(neg(mul(sub(mul(Shannon_Bprime, Total_HS_FiM), neg(Tolerance_Factor)), sub(div(HS_moment_B, Shannon_Aprime), mul(Total_HS_FiM, HS_moment_Bprime))))))
```  
**Stage 1 Classification Metrics:** Accuracy = **64.15%** | F1-Score = **0.7583** | Precision = **0.6552** | Recall = **0.9000**

| Fourier Depth (D) | Stage 1 Symbolic Acc (%) | Stage 1 F1 | **Optimal Best K*** | Stage 2 Sub R² (%) | **Final Pipeline R² (%)** | **Theoretical Limit (%)** | Final MSE | Final MAE | Top Fourier Features (K*) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| D = 3 | 64.15% | 0.7583 | **K* = 6** | 21.27% | **-7.70%** | **0.00%** | 1.678238 | 1.0707 | `Spin_Proxy_Distance`, `Val_avg`, `Total_d_electrons` |
| D = 5 | 64.15% | 0.7583 | **K* = 8** | 24.59% | **-3.98%** | **0.00%** | 1.620188 | 1.0507 | `Spin_Proxy_Distance`, `Total_d_electrons`, `d_electrons_Bprime` |
| D = 10 | 64.15% | 0.7583 | **K* = 6** | 28.55% | **-1.22%** | **0.00%** | 1.577126 | 1.0315 | `Total_d_electrons`, `d_electrons_Bprime`, `Spin_Proxy_Distance` |
| D = 50 | 64.15% | 0.7583 | **K* = 10** | 31.17% | **1.51%** | **3.02%** | 1.534667 | 1.0125 | `d_electrons_Bprime`, `Total_d_electrons`, `EN_Bprime` |
| D = 100 | 64.15% | 0.7583 | **K* = 9** | 33.30% | **2.16%** | **4.33%** | 1.524487 | 1.0076 | `EN_avg`, `d_electrons_Bprime`, `Total_d_electrons` |

---

## Target Property: Total Magnetization (uB)

**Discovered Symbolic Decision Boundary Formula S(x):**  
```text
S(x) = log(pow(add(HS_moment_B, Total_HS_FiM), mul(Val_A, Group_Bprime)))
```  
**Stage 1 Classification Metrics:** Accuracy = **63.90%** | F1-Score = **0.7255** | Precision = **0.6343** | Recall = **0.8472**

| Fourier Depth (D) | Stage 1 Symbolic Acc (%) | Stage 1 F1 | **Optimal Best K*** | Stage 2 Sub R² (%) | **Final Pipeline R² (%)** | **Theoretical Limit (%)** | Final MSE | Final MAE | Top Fourier Features (K*) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| D = 3 | 63.90% | 0.7255 | **K* = 2** | 27.71% | **8.38%** | **13.96%** | 86.816290 | 5.8186 | `Volume_A3`, `EN_A` |
| D = 5 | 63.90% | 0.7255 | **K* = 2** | 31.52% | **12.41%** | **20.68%** | 82.994424 | 5.5863 | `Volume_A3`, `EN_A` |
| D = 10 | 63.90% | 0.7255 | **K* = 2** | 39.43% | **16.50%** | **27.50%** | 79.116649 | 5.3692 | `Volume_A3`, `EN_A` |
| D = 50 | 63.90% | 0.7255 | **K* = 3** | 51.41% | **23.84%** | **39.73%** | 72.168082 | 4.7598 | `Volume_A3`, `EN_A`, `EN_Aprime` |
| D = 100 | 63.90% | 0.7255 | **K* = 3** | 53.63% | **25.58%** | **42.63%** | 70.517146 | 4.6791 | `Volume_A3`, `EN_A`, `EN_Aprime` |

---

## Target Property: Energy Above Hull (eV)

**Discovered Symbolic Decision Boundary Formula S(x):**  
```text
S(x) = log(add(pow(sub(add(d_BprimeO, Shannon_Bprime), abs(Total_HS_FM)), log(log(Total_d_electrons))), add(neg(abs(Shannon_Aprime)), log(mul(EN_Aprime, Val_B)))))
```  
**Stage 1 Classification Metrics:** Accuracy = **71.45%** | F1-Score = **0.8167** | Precision = **0.7400** | Recall = **0.9112**

| Fourier Depth (D) | Stage 1 Symbolic Acc (%) | Stage 1 F1 | **Optimal Best K*** | Stage 2 Sub R² (%) | **Final Pipeline R² (%)** | **Theoretical Limit (%)** | Final MSE | Final MAE | Top Fourier Features (K*) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| D = 3 | 71.45% | 0.8167 | **K* = 3** | 3.38% | **2.45%** | **9.79%** | 0.071698 | 0.1039 | `EN_B`, `Volume_A3`, `Group_B` |
| D = 5 | 71.45% | 0.8167 | **K* = 3** | 4.23% | **3.43%** | **13.74%** | 0.070973 | 0.1034 | `EN_B`, `Group_B`, `Volume_A3` |
| D = 10 | 71.45% | 0.8167 | **K* = 6** | 5.25% | **4.07%** | **16.28%** | 0.070505 | 0.1021 | `EN_B`, `Volume_A3`, `Group_B` |
| D = 50 | 71.45% | 0.8167 | **K* = 2** | 9.45% | **7.66%** | **30.63%** | 0.067869 | 0.1043 | `EN_B`, `Density_g_cm3` |
| D = 100 | 71.45% | 0.8167 | **K* = 10** | 9.91% | **2.44%** | **9.75%** | 0.071706 | 0.1041 | `Density_g_cm3`, `EN_avg`, `Volume_A3` |

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
