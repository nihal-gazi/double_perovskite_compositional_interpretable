# Experiment 4: Top-K Ensemble Size Sweep (K = 1 to 10) for Two-Stage Fourier Ensemble Architecture

## 1. Executive Summary & Objective

In **Experiment 3**, we introduced the Two-Stage Fourier Ensemble Hurdle Architecture with a fixed ensemble size $K = 5$. 

In **Experiment 4**, we perform a systematic **Top-$K$ Ensemble Size Sweep** across $K \in \{1, 2, 3, 4, 5, 6, 7, 8, 9, 10\}$ and Fourier depths $D \in \{3, 5, 10, 50, 100\}$ to answer two key scientific questions:
1. **Optimal Ensemble Capacity ($K^*$)**: What is the ideal number of top Fourier descriptor transforms to average to maximize overall pipeline $R^2$ accuracy while avoiding noise dilution?
2. **Single Best Feature ($K=1$) vs. Ensemble ($K > 1$)**: Does averaging multiple physical descriptor Fourier transforms ($K > 1$) consistently outperform relying on the single best individual feature ($K=1$)?

---

## 2. Mathematical Formulation of Top-K Sweep

For a given target property $T$, Fourier depth $D \in \{3, 5, 10, 50, 100\}$, and ensemble size $K \in \{1, 2, \dots, 10\}$:

### Stage 1: Top-K Ensemble Classifier
1. Fit 1D Fourier classifiers $f^{\text{cls}}_{I_i}(x)$ mapping each input feature $I_i$ ($i = 0, \dots, N-1$) to binary state $y_{\text{bin}} \in \{0, 1\}$.
2. Rank all features $I_i$ by classification accuracy descending.
3. Form the **Top-$K$ Ensemble Classifier**:
   $$F_{\text{class}}^{(K)}(\mathbf{x}) = \frac{1}{K} \sum_{j=0}^{K-1} f^{\text{cls}}_{(j)}\left(I_{(j)}\right)$$
4. Binary decision: $\widehat{y}_{\text{bin}}^{(K)} = 1$ if $F_{\text{class}}^{(K)}(\mathbf{x}) > 0.5$ else $0$.

### Stage 2: Top-K Ensemble Regressor
1. Fit 1D Fourier regressors $f^{\text{reg}}_{I_i}(x)$ mapping $I_i \to y_{\text{nonzero}}$ on active non-zero samples ($y > \text{threshold}$).
2. Rank all features $I_i$ by non-zero subset $R^2$ descending.
3. Form the **Top-$K$ Ensemble Regressor**:
   $$F_{\text{reg}}^{(K)}(\mathbf{x}) = \frac{1}{K} \sum_{j=0}^{K-1} f^{\text{reg}}_{(j)}\left(I_{(j)}\right)$$

### Stage 3: Two-Stage Hurdle Pipeline Inference
$$\widehat{y}_{\text{pipeline}}^{(K)} = \begin{cases} 0.0 & \text{if } \widehat{y}_{\text{bin}}^{(K)} == 0 \\ F_{\text{reg}}^{(K)}(\mathbf{x}) & \text{if } \widehat{y}_{\text{bin}}^{(K)} == 1 \end{cases}$$

### Best-K Selection Criteria:
$$K^*(D) = \arg\max_{K \in \{1, \dots, 10\}} R^2_{\text{pipeline}}(K, D)$$

---

## 3. Hyperparameter & Grid Configuration

| Hyperparameter | Value / Range | Description |
| :--- | :--- | :--- |
| **Ensemble Size Sweep ($K$)** | `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]` | Number of top Fourier transforms averaged |
| **Fourier Depths ($D$)** | `[3, 5, 10, 50, 100]` | Frequency harmonics evaluated |
| **Ridge Regularization ($\alpha$)** | `1e-4` | L2 penalty for numerical stability at high D |
| **Random Seed** | `42` | PyTorch & NumPy random seed |
| **Target Properties** | Band Gap, Magnetization, Hull Energy, Formation Energy | 2,000 double perovskite materials |
