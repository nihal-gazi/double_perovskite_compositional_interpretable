# Experiment 19: Octahedral d0/d10 Closed-Shell Engine & Binary Oxidation Enthalpy Mismatch

## 1. Executive Summary & Pure Compositional Audit

Following the strict data leakage audit, **3 leaked GNN-derived structural proxies remain permanently excluded** (`E_GNN`, `M_net`, `M_abs`). 

**Experiment 19** introduces **Octahedral $d^0/d^{10}$ Closed-Shell Crystal Field Descriptors** and **Binary Oxide Formation Enthalpy Mismatches**, coupled with a **Soft-Sigmoidal Gated Regressor & Hard-Margin Stage 1 Optimization**:

1. **Octahedral $d^0 / d^{10}$ Closed-Shell Crystal Field Engine (For Band Gap $E_g$)**:
   - Closed-shell $d^0$ cations (e.g. $\text{Ti}^{4+}, \text{Zr}^{4+}, \text{Nb}^{5+}, \text{Ta}^{5+}$) have empty $d$-orbitals, while $d^{10}$ cations (e.g. $\text{Ga}^{3+}, \text{In}^{3+}, \text{Zn}^{2+}$) have completely filled $d$-shells.
   - Indicators:
     $$\text{Is\_d0}_B = \mathbb{I}(d_B = 0), \quad \text{Is\_d10}_B = \mathbb{I}(d_B = 10)$$
     $$\text{Is\_Closed\_Shell}_{\text{both}} = \mathbb{I}((d_B \in \{0,10\}) \land (d_{B'} \in \{0,10\}))$$
   - Open-shell $d$-electron filling fraction: $f_d = \frac{d_B + d_{B'}}{20.0}$.

2. **Binary Oxide Formation Enthalpy Mismatch Engine (For Energy Above Hull $E_{\text{hull}}$)**:
   - Binary oxide formation enthalpy mismatch:
     $$\Delta H_{\text{ox\_mismatch}} = |\Delta H_{\text{oxide, B}} - \Delta H_{\text{oxide, B'\/}}|$$
   - Average binary oxide formation enthalpy:
     $$\Delta H_{\text{ox\_avg}} = \frac{\Delta H_{\text{oxide, B}} + \Delta H_{\text{oxide, B'\/}}}{2.0}$$

3. **Soft-Sigmoidal Gating & Hard-Margin Stage 1 Optimization**:
   - Soft-Sigmoidal Gating Function $g(\mathbf{x}) = \frac{1}{1 + e^{-S_{\text{cls}}(\mathbf{x})}}$ for smooth low-gap semiconductor modeling ($E_g \in [0.01, 0.5]\text{ eV}$).
   - High-C ($C=100.0$) Hard-Margin RBF Classifier with precision-recall F1 threshold tuning ($\tau^*$) for $M$ and $E_{\text{hull}}$.

---

## 2. Target-Specific Master Architecture Mapping

- **Formation Energy ($\Delta E_f$)**: Direct Multi-Operator Analytical Equation (anchored by Binary Oxide Formation Enthalpy & Birch-Murnaghan Strain).
- **Band Gap ($E_g$)**: Soft-Sigmoidal Gated Multi-Operator Regressor (powered by $d^0/d^{10}$ Closed-Shell Engine & Harrison Quantum Gap $E_{\text{gap, QM}}$).
- **Total Magnetization ($M$)**: High-C Hard-Margin Stage 1 Classifier (powered by $VEC$) + Multi-Operator Stage 2 Regressor (powered by $\Delta HS$).
- **Energy Above Hull ($E_{\text{hull}}$)**: High-C Hard-Margin Stage 1 Classifier (powered by Binary Oxide Enthalpy Mismatch $\Delta H_{\text{ox\_mismatch}}$ & Mendeleev Mismatch $\Delta \mathcal{M}_B$) + Multi-Operator Stage 2 Regressor.

---

## 3. Reference Theoretical Limits (Literature Benchmark)

- **Formation Energy ($\Delta E_f$)**: $R^2_{\text{limit}} = 65.0\%$ [Ouyang et al. 2018, Bartel et al. 2019]
- **Total Magnetization ($M$)**: $R^2_{\text{limit}} = 60.0\%$ [Ouyang et al. 2018, Ghiringhelli et al. 2015]
- **Band Gap ($E_g$)**: $R^2_{\text{limit}} = 50.0\%$ [Ouyang et al. 2018, Borlido et al. 2019]
- **Energy Above Hull ($E_{\text{hull}}$)**: $R^2_{\text{limit}} = 25.0\%$ [Bartel et al. 2019 SciAdv, Sun et al. 2016]

$$\text{Theoretical Limit (\%)} = \frac{\max(0.0, R^2_{\text{pipeline}})}{R^2_{\text{limit}}} \times 100\%$$
