# Experiment 3: Two-Stage Fourier Ensemble Hurdle Architecture for Zero-Inflated Double Perovskite Properties

## 1. Executive Summary & Core Concept

Many functional material properties computed via Density Functional Theory (DFT)—such as Band Gap ($E_g$), Total Magnetization ($M$), and Energy Above Hull ($E_{hull}$)—exhibit heavy **zero-inflation**:
- **Band Gap ($E_g$)**: ~37.5% zeros (Metals vs. Semiconductors)
- **Total Magnetization ($M$)**: ~43.7% zeros (Non-magnetic / Antiferromagnetic vs. Ferromagnetic / Ferrimagnetic)
- **Energy Above Hull ($E_{hull}$)**: ~30.2% zeros (Convex hull ground states vs. Metastable compounds)

Standard single-stage continuous regression models fail on zero-inflated data because fitting a smooth continuous function to step-function jumps from zero to non-zero values causes severe distortion and poor generalization.

**Experiment 3** introduces a **Two-Stage Fourier Ensemble Hurdle Architecture**:
1. **Stage 1 (Fourier Ensemble Binary Classifier)**: Predicts whether a double perovskite compound will have a zero or non-zero property value.
2. **Stage 2 (Fourier Ensemble Non-Zero Regressor)**: Fits a non-zero continuous Fourier ensemble model exclusively on the active non-zero subset ($y > \text{threshold}$).
3. **Combined Pipeline Inference**: Multiplies Stage 1 binary mask with Stage 2 non-zero predictions to yield the final property estimate.

---

## 2. Mathematical Formulation & Architecture

### Stage 1: Fourier Ensemble Binary Classification
Given input feature list $I = [I_0, I_1, \dots, I_{N-1}]$ and binary indicator $y_{\text{bin}} \in \{0, 1\}$ (where $1$ if $y > \text{threshold}$, else $0$):

1. For each input feature $I_i$, normalize $I_i \to [-\pi, \pi]$ and construct Fourier basis matrix $\Phi_D(I_i)$ of depth $D$:
   $$\Phi_D(I_i) = \Big[ 1, \cos(1 \cdot I_i), \sin(1 \cdot I_i), \dots, \cos(D \cdot I_i), \sin(D \cdot I_i) \Big] \in \mathbb{R}^{M \times (2D+1)}$$

2. Fit Fourier classification weights $\mathbf{w}^{\text{cls}}_i = \text{lstsq}(\Phi_D(I_i), y_{\text{bin}})$.

3. Select the **top $K=5$** Fourier classifiers with the highest classification accuracy / $R^2$.

4. Form the **Ensemble Classification Function**:
   $$F_{\text{class}}(\mathbf{x}) = \frac{1}{K} \sum_{j=0}^{K-1} f^{\text{cls}}_j\left(I_{(j)}\right)$$

5. Decision Rule:
   $$\widehat{y}_{\text{bin}} = \begin{cases} 1 & \text{if } F_{\text{class}}(\mathbf{x}) > 0.5 \\ 0 & \text{if } F_{\text{class}}(\mathbf{x}) \le 0.5 \end{cases}$$

---

### Stage 2: Fourier Ensemble Non-Zero Regression
Filtered dataset for active non-zero samples ($y > \text{threshold}$):

1. For each input feature $I_i$, fit non-zero Fourier series weights $\mathbf{w}^{\text{reg}}_i = \text{lstsq}(\Phi_D(I_i^{\text{nz}}), y^{\text{nz}})$.

2. Select the **top $K=5$** non-zero Fourier regressors with the highest subset $R^2$.

3. Form the **Ensemble Non-Zero Regressor**:
   $$F_{\text{reg}}(\mathbf{x}) = \frac{1}{K} \sum_{j=0}^{K-1} f^{\text{reg}}_j\left(I_{(j)}\right)$$

---

### Stage 3: Combined Hurdle Pipeline Inference
$$\widehat{y}_{\text{pipeline}} = \begin{cases} 0.0 & \text{if } \widehat{y}_{\text{bin}} == 0 \\ \max\left(0.0, F_{\text{reg}}(\mathbf{x})\right) & \text{if } \widehat{y}_{\text{bin}} == 1 \end{cases}$$

---

## 3. Hyperparameters & Configuration Contract

| Hyperparameter | Value / Setting | Description |
| :--- | :--- | :--- |
| **Random Seed** | `42` | PyTorch & NumPy random seed for 100% reproducibility |
| **Dataset Location** | `exp_v2/data/data_24_7_2026/double_perovskite_dataset.csv` | Compiled dataset of 2,000 double perovskites |
| **Top-K Ensemble Size** | `K = 5` | Number of top Fourier series models to average |
| **Fourier Depths ($D$)** | `[3, 5, 10, 50, 100]` | Number of frequency harmonics evaluated |
| **Band Gap Threshold** | `0.01 eV` | Zero threshold for Band Gap |
| **Magnetization Threshold** | `0.05 uB` | Zero threshold for Total Magnetization |
| **Hull Energy Threshold** | `0.01 eV` | Zero threshold for Energy Above Hull |
| **Formation Energy** | `None` | Continuous baseline property (0% zeros) |

---

## 4. Evaluation Metrics Tracked

1. **Stage 1 Classification**: Accuracy (%), Precision, Recall, F1-Score.
2. **Stage 2 Subset Regression**: Non-Zero Subset $R^2$ (%), Non-Zero Subset MSE, Non-Zero Subset MAE.
3. **Combined Pipeline**: Final Combined $R^2$ (%), Combined MSE, Combined MAE.
