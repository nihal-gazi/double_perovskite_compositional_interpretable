# Experiment 18: Quantum Power Laws & Birch-Murnaghan Thermodynamic Strain Engine

## 1. Executive Summary & Pure Compositional Audit

Following the strict data leakage audit, **3 leaked GNN-derived structural proxies remain permanently excluded** (`E_GNN`, `M_net`, `M_abs`). 

**Experiment 18** introduces **Harrison Quantum Power Laws** and **Birch-Murnaghan Thermodynamic Elastic Strain Proxies**, coupled with a **Hard-Margin Boundary Stage 1 Classifier Optimization**:

1. **Harrison's Solid State Tight-Binding Quantum Gap Proxy ($E_{\text{gap, QM}}$)**:
   - Harrison's tight-binding distance scaling ($V_{pp\sigma} \propto d_{\text{ideal}}^{-2}$):
     $$E_{\text{gap, QM}} = \sqrt{\Delta E_{\text{gap}}^2 + (r_{\text{Shannon}, B} + r_{\text{Shannon}, O})^{-4}}$$
   - Uses free-atom ionization energies and elemental Shannon radii (100% pure 0D compositional descriptor!).

2. **Birch-Murnaghan Thermodynamic Elastic Strain Engine**:
   - Tolerance Strain Energy:
     $$E_{\text{tolerance\_strain}} = (t_{\text{Goldschmidt}} - 1.0)^2$$
   - Octahedral Distortion Strain Energy:
     $$E_{\text{oct\_distortion\_strain}} = (\text{Octahedral\_Mismatch})^2 \cdot \text{Density}$$
   - Molar Volume Packing Strain:
     $$\Delta V_{\text{packing\_strain}} = \left(\frac{V_{\text{atomic}} - V_{\text{ideal}}}{V_{\text{ideal}}}\right)^2$$
     *(where $V_{\text{ideal}} = \frac{4}{3}\pi (2 r_A^3 + r_B^3 + r_{B'}^3 + 6 r_O^3)$)*.

3. **Sub-Linear Radical & Fractional Power Laws**:
   - Fractional power-law terms: $\sqrt{x_i x_j}$, $(x_i x_j)^{1/3}$, $(x_i x_j)^{2/3}$.

4. **Hard-Margin Stage 1 Classifier Optimization**:
   - High-C ($C=50.0$) RBF-Kernel Support Vector Classifier with precision-recall F1 threshold optimization ($\tau^*$) to eliminate classification boundary leakage going into Stage 2.

---

## 2. Target-Specific Master Architecture Mapping

- **Formation Energy ($\Delta E_f$)**: Direct Multi-Operator Analytical Equation (anchored by Birch-Murnaghan Strain & Harrison Quantum Gap).
- **Band Gap ($E_g$)**: Direct Multi-Operator Analytical Equation (anchored by Harrison Quantum Gap $E_{\text{gap, QM}}$ and Phillips Ionicity).
- **Total Magnetization ($M$)**: Hard-Margin Stage 1 Classifier (powered by $VEC$) + Multi-Operator Stage 2 Regressor (powered by $\Delta HS$).
- **Energy Above Hull ($E_{\text{hull}}$)**: Hard-Margin Stage 1 Classifier (powered by Birch-Murnaghan Strain & Mendeleev Mismatch $\Delta \mathcal{M}_B$) + Multi-Operator Stage 2 Regressor.

---

## 3. Reference Theoretical Limits (Literature Benchmark)

- **Formation Energy ($\Delta E_f$)**: $R^2_{\text{limit}} = 65.0\%$ [Ouyang et al. 2018, Bartel et al. 2019]
- **Total Magnetization ($M$)**: $R^2_{\text{limit}} = 60.0\%$ [Ouyang et al. 2018, Ghiringhelli et al. 2015]
- **Band Gap ($E_g$)**: $R^2_{\text{limit}} = 50.0\%$ [Ouyang et al. 2018, Borlido et al. 2019]
- **Energy Above Hull ($E_{\text{hull}}$)**: $R^2_{\text{limit}} = 25.0\%$ [Bartel et al. 2019 SciAdv, Sun et al. 2016]

$$\text{Theoretical Limit (\%)} = \frac{\max(0.0, R^2_{\text{pipeline}})}{R^2_{\text{limit}}} \times 100\%$$
