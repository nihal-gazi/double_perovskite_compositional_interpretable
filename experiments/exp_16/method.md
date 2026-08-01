# Experiment 16: Compositional Physical Mismatch & Ionicity-Enhanced Pipeline (100% Pure Compositional Descriptors)

## 1. Strict Data Leakage & 3D Audit Compliance Guarantee

To ensure **100% compliance with the Pure Compositional Theoretical Limit ($R^2_{\text{limit}} = 65.0\%$ for Formation Energy, $60.0\%$ for Magnetization, $50.0\%$ for Band Gap, $25.0\%$ for Hull Energy)**, Experiment 16 strictly enforces:

- ❌ **ZERO 3D Atomic Coordinates** $(x_i, y_i, z_i)$ or unit cell relaxation parameters.
- ❌ **ZERO DFT-Relaxed 3D Bond Angles or Interatomic Vectors**.
- ❌ **ZERO GNN-Derived Surrogates** (`E_GNN`, `M_net`, `M_abs` remain permanently removed).
- ✅ **100% PURE COMPOSITIONAL DESCRIPTORS ONLY**: Derived exclusively from elemental chemical formulas, Shannon free-ion radii lookup tables, Pauling electronegativities, and formal oxidation state accounting.

---

## 2. Pure Compositional Mismatch & Ionicity Feature Engine

Experiment 16 introduces **6 new pure compositional mismatch metrics** and their multi-operator expansions:

1. **B-Site & A-Site Electronegativity Mismatches**:
   $$\Delta\chi_B = |\chi_B - \chi_{B'}|, \quad \Delta\chi_{AB} = \left| \frac{\chi_B + \chi_{B'}}{2} - \frac{\chi_A + \chi_{A'}}{2} \right|$$

2. **Phillips Ionicity Index Proxy ($f_i$)**:
   $$f_i = \frac{\Delta\chi_{AB}^2}{\Delta\chi_{AB}^2 + (r_{\text{Shannon}, B} + r_{\text{Shannon}, O})^{-2}}$$

3. **B-Site Ferrimagnetic Spin Difference ($\Delta HS$)**:
   $$\Delta HS = |HS_B - HS_{B'}|$$

4. **B-Site & A-Site Formal Charge (Valence) Mismatches**:
   $$\Delta\text{Val}_B = |\text{Val}_B - \text{Val}_{B'}|, \quad \Delta\text{Val}_A = |\text{Val}_A - \text{Val}_{A'}|$$

5. **B-Site & A-Site Shannon Ionic Radii Mismatches**:
   $$\Delta r_B = |r_{\text{Shannon}, B} - r_{\text{Shannon}, B'}|, \quad \Delta r_A = |r_{\text{Shannon}, A} - r_{\text{Shannon}, A'}|$$

6. **B-Site Periodic Group Mismatch**:
   $$\Delta\text{Group}_B = |\text{Group}_B - \text{Group}_{B'}|$$

---

## 3. Target-Specific Master Architecture Mapping

- **Formation Energy ($\Delta E_f$)**: Direct Multi-Operator Analytical Equation.
- **Band Gap ($E_g$)**: Direct Multi-Operator Analytical Equation (powered by Phillips Ionicity $f_i$ and $\Delta\chi_{AB}^2$).
- **Total Magnetization ($M$)**: Non-Linear Decision Boundary Hurdle Model (powered by Ferrimagnetic Spin Difference $\Delta HS$).
- **Energy Above Hull ($E_{\text{hull}}$)**: Non-Linear Decision Boundary Hurdle Model (powered by Valence Mismatch $\Delta\text{Val}_B$).

---

## 4. Reference Theoretical Limits (Literature Benchmark)

- **Formation Energy ($\Delta E_f$)**: $R^2_{\text{limit}} = 65.0\%$ [Ouyang et al. 2018, Bartel et al. 2019]
- **Total Magnetization ($M$)**: $R^2_{\text{limit}} = 60.0\%$ [Ouyang et al. 2018, Ghiringhelli et al. 2015]
- **Band Gap ($E_g$)**: $R^2_{\text{limit}} = 50.0\%$ [Ouyang et al. 2018, Borlido et al. 2019]
- **Energy Above Hull ($E_{\text{hull}}$)**: $R^2_{\text{limit}} = 25.0\%$ [Bartel et al. 2019 SciAdv, Sun et al. 2016]

$$\text{Theoretical Limit (\%)} = \frac{\max(0.0, R^2_{\text{pipeline}})}{R^2_{\text{limit}}} \times 100\%$$
