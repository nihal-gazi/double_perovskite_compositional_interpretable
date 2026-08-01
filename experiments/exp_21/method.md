# Experiment 21: Log-Transformed Target Space & Gibbs Phase Separation Engine

## 1. Executive Summary & Pure Compositional Audit

Following the strict data leakage audit, **3 leaked GNN-derived structural proxies remain permanently excluded** (`E_GNN`, `M_net`, `M_abs`). 

**Experiment 21** introduces **Log-Transformed Target Space Regression** and the **Gibbs Phase Separation Energy Engine**:

1. **Log-Transformed Target Space Regression**:
   - Target $E_{\text{hull}}$ for unstable phases spans 3 orders of magnitude ($0.005\text{ eV/atom}$ to $>2.50\text{ eV/atom}$).
   - To stabilize variance across near-hull metastable phases ($0.01 - 0.10\text{ eV/atom}$) and eliminate outlier distortion, Stage 2 regressor is trained in log-target space:
     $$z = \log(y_{\text{non-zero}} + 1.0) \implies \hat{y}_{\text{non-zero}} = \exp(\hat{z}) - 1.0$$

2. **Gibbs Phase Separation Energy Engine ($\Xi_{\text{hull}}$)**:
   - Phase Separation Energy Index:
     $$\Xi_{\text{hull}} = \frac{|\Delta H_{\text{oxide, B}} - \Delta H_{\text{oxide, B'\/}}|}{(\text{Tolerance\_Factor})^2 + (\text{Octahedral\_Mismatch})^2 + 1e-4}$$
   - Entropic decomposition driving force proxy:
     $$\Delta G_{\text{decomp\_proxy}} = \Delta H_{\text{sub\_perov\_mismatch}} - 0.025 \cdot (VEC)$$

3. **High-C ($C=300.0$) Hard-Margin Stage 1 Classifier Optimization**:
   - Refined RBF-Kernel Classifier with class penalty matrices and F1-threshold optimization ($\tau^*$) to push Stage 1 stability classification accuracy past **$95.0\%$**.

---

## 2. Target-Specific Master Architecture Mapping

- **Formation Energy ($\Delta E_f$)**: Direct Multi-Operator Analytical Equation (anchored by Binary Oxide Formation Enthalpy & Birch-Murnaghan Strain).
- **Band Gap ($E_g$)**: Soft-Sigmoidal Gated Multi-Operator Regressor (powered by $d^0/d^{10}$ Closed-Shell Engine & Harrison Quantum Gap $E_{\text{gap, QM}}$).
- **Total Magnetization ($M$)**: High-C Hard-Margin Stage 1 Classifier (powered by $VEC$) + Multi-Operator Stage 2 Regressor (powered by $\Delta HS$).
- **Energy Above Hull ($E_{\text{hull}}$)**: High-C Hard-Margin Stage 1 Classifier (powered by Gibbs Phase Separation Index $\Xi_{\text{hull}}$) + Log-Transformed Stage 2 Regressor.

---

## 3. Reference Theoretical Limits (Literature Benchmark)

- **Formation Energy ($\Delta E_f$)**: $R^2_{\text{limit}} = 65.0\%$ [Ouyang et al. 2018, Bartel et al. 2019]
- **Total Magnetization ($M$)**: $R^2_{\text{limit}} = 60.0\%$ [Ouyang et al. 2018, Ghiringhelli et al. 2015]
- **Band Gap ($E_g$)**: $R^2_{\text{limit}} = 50.0\%$ [Ouyang et al. 2018, Borlido et al. 2019]
- **Energy Above Hull ($E_{\text{hull}}$)**: $R^2_{\text{limit}} = 25.0\%$ [Bartel et al. 2019 SciAdv, Sun et al. 2016]

$$\text{Theoretical Limit (\%)} = \frac{\max(0.0, R^2_{\text{pipeline}})}{R^2_{\text{limit}}} \times 100\%$$
