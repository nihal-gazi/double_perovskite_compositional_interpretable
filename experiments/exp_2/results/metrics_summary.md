# Experiment 2: Multi-Descriptor Fourier Transform Ensemble Distillation Report

**Dataset:** `exp_v2/data/data_24_7_2026/double_perovskite_dataset.csv` (2,000 double perovskites)  
**Ensemble Strategy:** Top K = 5 Fourier Transforms Average  
**Evaluated Fourier Depths (num_freq D):** `[3, 5, 10, 50, 100]`  

---

## Target Property: Formation Energy (eV/atom)

| Fourier Depth (D) | Final Ensemble R² (%) | Final MSE | Final MAE | Top-5 Input Features Included |
| :---: | :---: | :---: | :---: | :--- |
| D = 3 | **61.37%** | 0.134753 | 0.2374 | `E_GNN`, `EN_avg`, `EN_B`, `EN_A`, `EN_Aprime` |
| D = 5 | **64.03%** | 0.125495 | 0.2278 | `E_GNN`, `EN_avg`, `EN_B`, `EN_A`, `EN_Aprime` |
| D = 10 | **67.85%** | 0.112174 | 0.2155 | `E_GNN`, `EN_A`, `EN_Aprime`, `EN_avg`, `EN_B` |
| D = 50 | **71.55%** | 0.099244 | 0.1984 | `E_GNN`, `EN_avg`, `EN_A`, `EN_Aprime`, `EN_B` |
| D = 100 | **72.09%** | 0.097370 | 0.1958 | `E_GNN`, `EN_avg`, `EN_A`, `EN_Aprime`, `EN_B` |

## Target Property: Band Gap (eV)

| Fourier Depth (D) | Final Ensemble R² (%) | Final MSE | Final MAE | Top-5 Input Features Included |
| :---: | :---: | :---: | :---: | :--- |
| D = 3 | **19.48%** | 1.254622 | 0.9712 | `M_net`, `Group_Bprime`, `Val_Bprime`, `Val_avg`, `Spin_Proxy_Distance` |
| D = 5 | **24.00%** | 1.184196 | 0.9345 | `M_net`, `Group_Bprime`, `Val_Bprime`, `d_electrons_Bprime`, `Val_avg` |
| D = 10 | **27.96%** | 1.122446 | 0.9127 | `M_net`, `d_electrons_Bprime`, `Total_d_electrons`, `Group_Bprime`, `Val_avg` |
| D = 50 | **34.84%** | 1.015238 | 0.8739 | `M_net`, `EN_Bprime`, `d_electrons_Bprime`, `EN_avg`, `M_abs` |
| D = 100 | **37.70%** | 0.970756 | 0.8506 | `M_net`, `EN_avg`, `M_abs`, `EN_Bprime`, `d_electrons_Bprime` |

## Target Property: Total Magnetization (uB)

| Fourier Depth (D) | Final Ensemble R² (%) | Final MSE | Final MAE | Top-5 Input Features Included |
| :---: | :---: | :---: | :---: | :--- |
| D = 3 | **62.43%** | 35.597891 | 3.3145 | `M_net`, `M_abs`, `Volume_A3`, `EN_A`, `EN_Aprime` |
| D = 5 | **67.37%** | 30.913722 | 3.1211 | `M_net`, `M_abs`, `Volume_A3`, `EN_A`, `EN_Aprime` |
| D = 10 | **70.50%** | 27.954293 | 2.9733 | `M_net`, `M_abs`, `Volume_A3`, `EN_A`, `EN_Aprime` |
| D = 50 | **75.93%** | 22.811587 | 2.6488 | `M_net`, `M_abs`, `Volume_A3`, `EN_A`, `EN_Aprime` |
| D = 100 | **76.40%** | 22.364399 | 2.6186 | `M_net`, `M_abs`, `Volume_A3`, `EN_A`, `EN_Aprime` |

## Target Property: Energy Above Hull (eV)

| Fourier Depth (D) | Final Ensemble R² (%) | Final MSE | Final MAE | Top-5 Input Features Included |
| :---: | :---: | :---: | :---: | :--- |
| D = 3 | **17.68%** | 0.060503 | 0.0906 | `E_GNN`, `Volume_A3`, `d_AO`, `Shannon_A`, `Shannon_Aprime` |
| D = 5 | **21.24%** | 0.057887 | 0.0906 | `E_GNN`, `EN_B`, `Group_B`, `Volume_A3`, `d_AO` |
| D = 10 | **26.99%** | 0.053658 | 0.0858 | `E_GNN`, `EN_B`, `EN_A`, `EN_Aprime`, `EN_Bprime` |
| D = 50 | **32.80%** | 0.049386 | 0.0851 | `E_GNN`, `EN_B`, `EN_avg`, `M_net`, `Volume_A3` |
| D = 100 | **35.83%** | 0.047160 | 0.0844 | `E_GNN`, `Density_g_cm3`, `EN_avg`, `M_net`, `EN_B` |

