# Experiment 3: Two-Stage Fourier Ensemble Hurdle Architecture Report

**Dataset:** `exp_v2/data/data_24_7_2026/double_perovskite_dataset.csv` (2,000 double perovskites)  
**Ensemble Strategy:** Top K = 5 Fourier Models Average  
**Evaluated Fourier Depths (num_freq D):** `[3, 5, 10, 50, 100]`  

---

## Target Property: Band Gap (eV)

| Fourier Depth (D) | Stage 1 Cls Acc (%) | Stage 1 F1 | Stage 2 Sub R² (%) | **Final Pipeline R² (%)** | Final MSE | Final MAE | Top-5 Stage 1 Features | Top-5 Stage 2 Features |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- | :--- |
| D = 3 | 64.45% | 0.7745 | 26.50% | **-5.00%** | 1.636097 | 1.0866 | `Group_Bprime`, `Val_Bprime`, `Val_B` | `M_net`, `Spin_Proxy_Distance`, `Val_avg` |
| D = 5 | 69.95% | 0.7993 | 28.74% | **9.20%** | 1.414813 | 0.9617 | `M_net`, `Val_Bprime`, `Group_Bprime` | `M_net`, `Spin_Proxy_Distance`, `Total_d_electrons` |
| D = 10 | 69.40% | 0.7937 | 32.23% | **12.24%** | 1.367404 | 0.9426 | `M_net`, `Val_Bprime`, `Group_Bprime` | `M_net`, `Total_d_electrons`, `d_electrons_Bprime` |
| D = 50 | 73.45% | 0.8175 | 36.31% | **20.16%** | 1.244115 | 0.8682 | `M_net`, `Val_Bprime`, `Group_Bprime` | `M_net`, `d_electrons_Bprime`, `Total_d_electrons` |
| D = 100 | 73.60% | 0.8195 | 41.24% | **24.14%** | 1.182083 | 0.8464 | `M_net`, `EN_avg`, `M_abs` | `M_net`, `EN_avg`, `d_electrons_Bprime` |

## Target Property: Total Magnetization (uB)

| Fourier Depth (D) | Stage 1 Cls Acc (%) | Stage 1 F1 | Stage 2 Sub R² (%) | **Final Pipeline R² (%)** | Final MSE | Final MAE | Top-5 Stage 1 Features | Top-5 Stage 2 Features |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- | :--- |
| D = 3 | 85.15% | 0.8709 | 62.19% | **62.80%** | 35.247636 | 2.5599 | `M_net`, `Val_Bprime`, `Group_Bprime` | `M_net`, `M_abs`, `Volume_A3` |
| D = 5 | 86.20% | 0.8826 | 63.96% | **66.20%** | 32.027559 | 2.4950 | `M_net`, `d_electrons_Bprime`, `M_abs` | `M_net`, `M_abs`, `Volume_A3` |
| D = 10 | 88.90% | 0.9062 | 67.93% | **67.77%** | 30.543410 | 2.4159 | `M_net`, `d_electrons_Bprime`, `M_abs` | `M_net`, `M_abs`, `Volume_A3` |
| D = 50 | 91.05% | 0.9238 | 75.05% | **70.09%** | 28.340001 | 2.2330 | `M_net`, `M_abs`, `d_electrons_Bprime` | `M_abs`, `M_net`, `Volume_A3` |
| D = 100 | 91.60% | 0.9286 | 76.42% | **68.38%** | 29.957496 | 2.3176 | `M_net`, `M_abs`, `d_electrons_Bprime` | `M_abs`, `M_net`, `Volume_A3` |

## Target Property: Energy Above Hull (eV)

| Fourier Depth (D) | Stage 1 Cls Acc (%) | Stage 1 F1 | Stage 2 Sub R² (%) | **Final Pipeline R² (%)** | Final MSE | Final MAE | Top-5 Stage 1 Features | Top-5 Stage 2 Features |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- | :--- |
| D = 3 | 72.75% | 0.8346 | 18.75% | **15.96%** | 0.061769 | 0.1072 | `EN_A`, `EN_Aprime`, `EN_Bprime` | `E_GNN`, `EN_B`, `Volume_A3` |
| D = 5 | 74.75% | 0.8304 | 22.24% | **13.22%** | 0.063779 | 0.0951 | `EN_A`, `EN_Aprime`, `Shannon_A` | `E_GNN`, `EN_B`, `Group_B` |
| D = 10 | 74.75% | 0.8304 | 26.55% | **16.90%** | 0.061075 | 0.0921 | `EN_A`, `EN_Aprime`, `Shannon_A` | `E_GNN`, `EN_B`, `Volume_A3` |
| D = 50 | 75.20% | 0.8331 | 33.62% | **19.94%** | 0.058844 | 0.0908 | `EN_A`, `EN_Aprime`, `Shannon_A` | `E_GNN`, `EN_B`, `Density_g_cm3` |
| D = 100 | 76.20% | 0.8374 | 36.89% | **-1.55%** | 0.074636 | 0.0943 | `EN_A`, `EN_Aprime`, `Shannon_A` | `E_GNN`, `Density_g_cm3`, `EN_avg` |

## Target Property: Formation Energy (eV/atom)

| Fourier Depth (D) | Stage 1 Cls Acc (%) | Stage 1 F1 | Stage 2 Sub R² (%) | **Final Pipeline R² (%)** | Final MSE | Final MAE | Top-5 Stage 1 Features | Top-5 Stage 2 Features |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- | :--- |
| D = 3 | 100.00% | 1.0000 | 61.37% | **61.37%** | 0.134753 | 0.2374 | `N/A (Continuous)`, `N/A (Continuous)`, `N/A (Continuous)` | `E_GNN`, `EN_avg`, `EN_B` |
| D = 5 | 100.00% | 1.0000 | 64.03% | **64.03%** | 0.125496 | 0.2278 | `N/A (Continuous)`, `N/A (Continuous)`, `N/A (Continuous)` | `E_GNN`, `EN_avg`, `EN_B` |
| D = 10 | 100.00% | 1.0000 | 67.53% | **67.53%** | 0.113263 | 0.2159 | `N/A (Continuous)`, `N/A (Continuous)`, `N/A (Continuous)` | `E_GNN`, `EN_A`, `EN_Aprime` |
| D = 50 | 100.00% | 1.0000 | 71.28% | **71.28%** | 0.100183 | 0.1996 | `N/A (Continuous)`, `N/A (Continuous)`, `N/A (Continuous)` | `E_GNN`, `EN_avg`, `EN_A` |
| D = 100 | 100.00% | 1.0000 | 71.98% | **71.98%** | 0.097745 | 0.1963 | `N/A (Continuous)`, `N/A (Continuous)`, `N/A (Continuous)` | `E_GNN`, `EN_avg`, `EN_A` |

