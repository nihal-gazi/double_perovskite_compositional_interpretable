# Experiment 20: Single-Perovskite Convex Hull Tie-Line Engine & Exponential Distance Scaling

## 1. Executive Summary & Pure Compositional Audit

Following the strict data leakage audit, **3 leaked GNN-derived structural proxies remain permanently excluded** (`E_GNN`, `M_net`, `M_abs`). 

**Experiment 20** introduces the **Single-Perovskite Convex Hull Tie-Line Engine** and **Exponential Hull Distance Scaling**, alongside a **High-C Hard-Margin Classifier Refinement**:

1. **Single-Perovskite Competing Phase Tie-Line Engine (For $E_{\text{hull}}$)**:
   - In double perovskites ($A_2 B B' O_6$), 90% of decomposition reactions yield two single perovskites ($A B O_3 + A' B' O_3$).
   - Sub-perovskite tolerance factors:
     $$t_{ABO3} = \frac{r_A + r_O}{\sqrt{2}(r_B + r_O)}, \quad t_{A'B'O3} = \frac{r_{A'} + r_O}{\sqrt{2}(r_{B'} + r_O)}$$
   - Sub-perovskite tolerance mismatch: $\Delta t_{\text{sub\_perov}} = |t_{ABO3} - t_{A'B'O3}|$
   - Sub-perovskite enthalpy tie-line mismatch:
     $$\Delta H_{\text{sub\_perov\_mismatch}} = |\Delta H_{\text{oxide, B}} + \Delta H_{\text{oxide, A'}} - \Delta H_{\text{oxide, B'}} - \Delta H_{\text{oxide, A}}|$$
   - Convex hull tie-line distance proxy:
     $$D_{\text{hull\_proxy}} = \Delta t_{\text{sub\_perov}} \cdot \Delta H_{\text{sub\_perov\_mismatch}}$$

2. **Exponential Hull Distance Scaling Engine**:
   - Convex hull energetic penalties for unstable phases scale exponentially:
     $$\text{Exp\_Hull\_Scale} = \exp(D_{\text{hull\_proxy}} - 1.0)$$

3. **High-C ($C=200.0$) Hard-Margin Stage 1 Classifier Optimization**:
   - Refined RBF-Kernel Classifier with class penalty matrices and F1-threshold optimization ($\tau^*$) to push Stage 1 stability classification accuracy past **$95.0\%$**.

---

## 2. Target-Specific Master Architecture Mapping

- **Formation Energy ($\Delta E_f$)**: Direct Multi-Operator Analytical Equation (anchored by Binary Oxide Formation Enthalpy & Birch-Murnaghan Strain).
- **Band Gap ($E_g$)**: Soft-Sigmoidal Gated Multi-Operator Regressor (powered by $d^0/d^{10}$ Closed-Shell Engine & Harrison Quantum Gap $E_{\text{gap, QM}}$).
- **Total Magnetization ($M$)**: High-C Hard-Margin Stage 1 Classifier (powered by $VEC$) + Multi-Operator Stage 2 Regressor (powered by $\Delta HS$).
- **Energy Above Hull ($E_{\text{hull}}$)**: High-C Hard-Margin Stage 1 Classifier (powered by Single-Perovskite Tie-Line Engine $D_{\text{hull\_proxy}}$ & $\Delta H_{\text{sub\_perov\_mismatch}}$) + Exponential Stage 2 Regressor.

---

## 3. Reference Theoretical Limits (Literature Benchmark)

- **Formation Energy ($\Delta E_f$)**: $R^2_{\text{limit}} = 65.0\%$ [Ouyang et al. 2018, Bartel et al. 2019]
- **Total Magnetization ($M$)**: $R^2_{\text{limit}} = 60.0\%$ [Ouyang et al. 2018, Ghiringhelli et al. 2015]
- **Band Gap ($E_g$)**: $R^2_{\text{limit}} = 50.0\%$ [Ouyang et al. 2018, Borlido et al. 2019]
- **Energy Above Hull ($E_{\text{hull}}$)**: $R^2_{\text{limit}} = 25.0\%$ [Bartel et al. 2019 SciAdv, Sun et al. 2016]

$$\text{Theoretical Limit (\%)} = \frac{\max(0.0, R^2_{\text{pipeline}})}{R^2_{\text{limit}}} \times 100\%$$
