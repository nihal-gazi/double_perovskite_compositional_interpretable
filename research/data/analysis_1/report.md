# Data Analysis Methodology & Property Specifications Report

**Location:** `exp_v2/research/data/analysis_1/report.md`  
**Dataset:** `exp_v2/data/data_24_7_2026/double_perovskite_dataset.csv` (2,000 double perovskite material samples)  

---

## 1. Overview of Target Properties

The dataset evaluates four primary quantum-mechanical and thermodynamic target properties calculated via Density Functional Theory (DFT) across 2,000 double perovskites ($A_2BB'O_6$):

1. **Formation Energy ($\Delta E_f$, eV/atom)**:
   - *Physical Meaning*: The enthalpy change per atom when forming the compound from pure elemental standard states. Negative values indicate exothermic stability.
   - *Distribution*: Continuous, non-zero-inflated pseudo-Gaussian distribution (range: $-3.5\text{ eV/atom}$ to $+0.5\text{ eV/atom}$, mean: $-1.82\text{ eV/atom}$).
2. **Energy Above Hull ($E_{\text{hull}}$, eV/atom)**:
   - *Physical Meaning*: The thermodynamic decomposition energy relative to the lowest-energy convex hull of competing phases. $E_{\text{hull}} = 0$ indicates a ground-state stable phase.
   - *Distribution*: Zero-inflated (**30.2% zeros** at threshold $0.01\text{ eV}$), right-skewed decay.
3. **Band Gap ($E_g$, eV)**:
   - *Physical Meaning*: The fundamental electronic band gap between valence band maximum (VBM) and conduction band minimum (CBM). $E_g = 0$ indicates a metallic state.
   - *Distribution*: Zero-inflated (**37.5% zeros** at threshold $0.01\text{ eV}$), continuous semiconductor/insulator tail up to $4.5\text{ eV}$.
4. **Total Magnetization ($M$, $\mu_B$/formula unit)**:
   - *Physical Meaning*: Net spin plus orbital magnetic moment per formula unit. $M = 0$ indicates non-magnetic / diamagnetic ordering.
   - *Distribution*: Zero-inflated (**43.7% zeros** at threshold $0.05\ \mu_B$), discrete multi-spin state spectrum up to $10.0\ \mu_B$.

---

## 2. Input Physical Descriptors (33 Clean Features)

Following a strict Data Leakage Audit, all GNN-derived surrogate outputs (`E_GNN`, `M_net`, `M_abs`) were excluded. The analysis is performed on **33 pure physical and chemical descriptors**:

### A. Electronegativities (Pauling Scale)
- `EN_A`, `EN_Aprime`: Pauling electronegativity of A and A' site cations
- `EN_B`, `EN_Bprime`: Pauling electronegativity of B and B' site transition metals
- `EN_avg`: Stoichiometric average Pauling electronegativity across all sites

### B. Ionic Radii & Structural Geometry (Shannon Radii)
- `Shannon_A`, `Shannon_Aprime`: Shannon ionic radii of A and A' cations ($\text{\AA}$)
- `Shannon_B`, `Shannon_Bprime`: Shannon ionic radii of B and B' cations ($\text{\AA}$)
- `Tolerance_Factor` ($t$): Goldschmidt tolerance factor $t = \frac{r_A + r_O}{\sqrt{2}(r_B + r_O)}$
- `Octahedral_Mismatch` ($\mu_{\text{oct}}$): Octahedral size distortion $|r_B - r_{B'}| / (r_B + r_{B'})$
- `d_AO`, `d_BO`, `d_BprimeO`, `d_avg`: Interatomic bond lengths ($\text{\AA}$) derived from ionic radii sum
- `Volume_A3`: Estimated unit cell volume ($\text{\AA}^3$)
- `Density_g_cm3`: Calculated crystallographic mass density ($\text{g/cm}^3$)

### C. Valence Charges & Electronic Configurations
- `Val_A`, `Val_Aprime`, `Val_B`, `Val_Bprime`, `Val_avg`: Formal oxidation states
- `Total_A_Charge`: Sum of A-site charges
- `Group_B`, `Group_Bprime`: Periodic table group numbers of B and B' cations
- `d_electrons_B`, `d_electrons_Bprime`, `Total_d_electrons`: Number of valence $d$-electrons

### D. Spin & Magnetic Proxies (Hund's Rule Free-Ion Moments)
- `HS_moment_B`, `HS_moment_Bprime`: High-spin magnetic moment proxies based on Hund's rules
- `Total_HS_FM`: Ferromagnetic total spin moment sum
- `Total_HS_FiM`: Ferrimagnetic net spin moment difference
- `Spin_Proxy_Distance`: Inter-spin distance proxy

---

## 3. Data Science & Exploratory Analysis Methods Used

1. **Kernel Density Estimation (KDE) & Zero-Inflation Profiling**:
   - Quantified zero-inflation percentages across target properties to justify two-stage hurdle architectures.
2. **Pearson Correlation Heatmap & Ranking**:
   - Computed pairwise linear correlation coefficients ($r \in [-1, 1]$) across all 33 features and 4 targets to identify dominant physical drivers.
3. **Principal Component Analysis (PCA)**:
   - Standardized features via $Z$-score normalization and performed spectral decomposition of the covariance matrix.
   - Generated Scree plots (explained variance ratio) and 2D projections (PC1 vs PC2) to determine the effective dimensionality ($\sim 8$ PCs explain $>90\%$ variance).
4. **t-Distributed Stochastic Neighbor Embedding (t-SNE)**:
   - Non-linear manifold learning projection (perplexity = 30) mapping the 33-dimensional space to 2D to uncover non-linear stability clusters.
5. **Pairwise Scatter Matrix (Pairplots)**:
   - Multi-panel pairwise feature analysis evaluating non-linear boundary constraints between Goldschmidt tolerance factor, octahedral mismatch, Hund's spin moment, and density.

---

*For visual plots and graph interpretations, refer to [`data_analysis.md`](file:///C:/Users/user/Desktop/IEM/IEM%20projects/Prof%20SOP%20sir/exp_v2/research/data/analysis_1/data_analysis.md).*
