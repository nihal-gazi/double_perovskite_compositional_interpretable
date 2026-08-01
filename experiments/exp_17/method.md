# Experiment 17: Tight-Binding Proxies & Mendeleev Feature Engine with Cost-Sensitive Stage 1

## 1. Executive Summary & Data Leakage Audit

Following the strict data leakage audit, **3 leaked GNN-derived structural proxies remain permanently excluded** (`E_GNN`, `M_net`, `M_abs`). 

**Experiment 17** introduces **three new classes of 0D quantum & thermodynamic descriptors** anchored in physical units (eV), alongside a **Cost-Sensitive Stage 1 Classifier Optimization**:

1. **HOMO-LUMO Energy Proxies (in eV)**:
   - First Ionization Energy ($IE_B, IE_{B'}$) and Electron Affinity ($EA_B, EA_{B'}$) in eV.
   - Tight-Binding Gap Proxy ($\Delta E_{\text{gap}}$):
     $$\Delta E_{\text{gap}} = \min(IE_B, IE_{B'}) - EA_{\text{Oxygen}}$$
     *(where $EA_{\text{Oxygen}} = 1.461\text{ eV}$)*.

2. **Mendeleev Number / Pettifor Scale ($\mathcal{M}$)**:
   - Continuous 1D chemical similarity mapping of the periodic table.
   - Mendeleev Mismatch:
     $$\Delta \mathcal{M}_B = |\mathcal{M}_B - \mathcal{M}_{B'}|$$

3. **Valence Electron Concentration ($VEC$)**:
   - Total valence electron density per atom across the 10-atom unit cell:
     $$VEC = \frac{2 \cdot \text{Valence}_A + \text{Valence}_B + \text{Valence}_{B'} + 6 \cdot 6}{10}$$

4. **Algorithmic Upgrade: Cost-Sensitive Stage 1 Classifier**:
   - Class-weighted penalty matrix (`class_weight='balanced'` / custom cost matrix) and precision-recall F1 threshold optimization to eliminate false positive/negative leaks entering Stage 2.

---

## 2. Target-Specific Master Architecture Mapping

- **Formation Energy ($\Delta E_f$)**: Direct Multi-Operator Analytical Equation (anchored by Tight-Binding $\Delta E_{\text{gap}}$ and $IE$).
- **Band Gap ($E_g$)**: Direct Multi-Operator Analytical Equation (anchored by Tight-Binding $\Delta E_{\text{gap}} = \min(IE_B, IE_{B'}) - EA_{\text{Oxygen}}$ and Phillips Ionicity).
- **Total Magnetization ($M$)**: Cost-Sensitive Stage 1 Classifier (powered by $VEC$) + Multi-Operator Stage 2 Regressor (powered by $\Delta HS$).
- **Energy Above Hull ($E_{\text{hull}}$)**: Cost-Sensitive Stage 1 Classifier (powered by Mendeleev Mismatch $\Delta \mathcal{M}_B$) + Multi-Operator Stage 2 Regressor.

---

## 3. Reference Theoretical Limits (Literature Benchmark)

- **Formation Energy ($\Delta E_f$)**: $R^2_{\text{limit}} = 65.0\%$ [Ouyang et al. 2018, Bartel et al. 2019]
- **Total Magnetization ($M$)**: $R^2_{\text{limit}} = 60.0\%$ [Ouyang et al. 2018, Ghiringhelli et al. 2015]
- **Band Gap ($E_g$)**: $R^2_{\text{limit}} = 50.0\%$ [Ouyang et al. 2018, Borlido et al. 2019]
- **Energy Above Hull ($E_{\text{hull}}$)**: $R^2_{\text{limit}} = 25.0\%$ [Bartel et al. 2019 SciAdv, Sun et al. 2016]

$$\text{Theoretical Limit (\%)} = \frac{\max(0.0, R^2_{\text{pipeline}})}{R^2_{\text{limit}}} \times 100\%$$
