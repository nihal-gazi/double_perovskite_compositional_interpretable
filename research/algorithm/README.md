# Master Capstone Algorithm: Double Perovskite Interpretable Machine Learning

This directory contains the production-grade, fully modularized **Master Capstone Algorithm** for predicting key quantum, thermodynamic, and electronic properties of double perovskites ($A_2 B B' O_6$) using **100% pure 0D compositional descriptors**.

---

## 1. Directory Architecture

```text
exp_v2/research/algorithm/
├── README.md               # Complete architectural overview, mathematical formulas & usage
├── data_lookup.py          # Elemental lookup tables (Pettifor Mendeleev, IE, EA, Binary Oxide Enthalpies)
├── feature_engine.py       # Master 0D Pure Compositional Feature Engine (Quantum, Strain, Tie-Line, Mismatches)
├── model_engine.py         # Target-Specific Master Models (Direct Regressor, Soft-Sigmoidal Gated, Hard-Margin Hurdle)
├── pipeline.py             # Consolidated Evaluation Pipeline & Theoretical Limit Benchmark Engine
├── requirements.txt        # Package dependencies
└── main.py                 # Single entry-point script to run the master algorithm
```

---

## 2. Core Scientific & Physical Principles

1. **Strict Data Leakage & 3D Audit Compliance**:
   - Zero 3D atomic coordinates.
   - Zero GNN surrogates (`E_GNN`, `M_net`, `M_abs` permanently excluded).
   - 100% Pure 0D Compositional & Quantum Descriptors.

2. **Harrison's Solid-State Tight-Binding Quantum Gap ($E_{\text{gap, QM}}$)**:
   $$E_{\text{gap, QM}} = \sqrt{(\min(IE_B, IE_{B'}) - EA_{\text{Oxygen}})^2 + V_{\text{transfer}}^2}$$

3. **Single-Perovskite Competing Phase Tie-Line Engine ($D_{\text{hull\_proxy}}$)**:
   $$D_{\text{hull\_proxy}} = |t_{ABO3} - t_{A'B'O3}| \cdot |\Delta H_{\text{ox, B}} + \Delta H_{\text{ox, A'}} - \Delta H_{\text{ox, B'}} - \Delta H_{\text{ox, A}}|$$

4. **Octahedral $d^0 / d^{10}$ Closed-Shell Crystal Field Engine**:
   - Closed-shell indicators: `Is_d0_B`, `Is_d10_B`, `Is_Closed_Shell_both`.

5. **Soft-Sigmoidal Gated Regressor Architecture**:
   $$\hat{y}(\mathbf{x}) = \left( \frac{1}{1 + e^{-S_{\text{cls}}(\mathbf{x})}} \right) \cdot \left[ b_0 + \sum w_i f_i(\mathbf{x}) \right]$$

---

## 3. How to Run

Execute the main entry script:

```bash
python exp_v2/research/algorithm/main.py
```
