# Physics-Gated Interpretable Machine Learning for Double Perovskites

[![Paper PDF](https://img.shields.io/badge/Paper-PDF-red.svg)](paper/paper.pdf)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Official repository for the manuscript:  
**"Physics-Gated Interpretable Machine Learning and Symbolic Regression for Double Perovskites: Overcoming Theoretical Limits Beyond 0D Compositional Models"**

---

## 📌 Abstract

Predicting the electronic, magnetic, and thermodynamic ground states of double perovskites ($A_2BB'O_6$) via Density Functional Theory (DFT) presents a formidable computational bottleneck. While black-box 3D Crystal Graph Neural Networks (CGNNs) achieve high accuracy, they rely on pre-relaxed atomic coordinates and operate without physical transparency. Conversely, traditional 0D compositional symbolic regression models encounter strict accuracy ceilings ($R^2_{\text{limit}} \approx 65\%$ for formation energy $\Delta E_f$, $60\%$ for magnetization $M$, $50\%$ for band gap $E_g$, and $25\%$ for energy above hull $E_{\text{hull}}$).

Here, we present a novel **Physics-Gated Machine Learning Architecture** that operates on 100% pure 0D compositional inputs without 3D spatial coordinates or leaked GNN surrogates. Our framework integrates fundamental solid-state physics engines—including Harrison's tight-binding quantum gap, octahedral $d^0/d^{10}$ splitting, Birch-Murnaghan elastic strain, and single-perovskite tie-line convex hull decomposition—with specialized property-routing mechanisms. Evaluated across 25 random seeds on a 5,000 double perovskite dataset and an 80/20 train/test benchmark on a 2,000 dataset, our algorithm surpasses theoretical literature limits on held-out test sets.

---

## 📁 Repository Structure

```
.
├── paper/
│   ├── paper.pdf                  # Compiled 35-page Elsevier PDF manuscript
│   ├── paper.tex                  # Complete Elsevier LaTeX source
│   ├── references.bib             # BibTeX bibliography database
│   ├── generate_paper_plots.py    # Python script for generating manuscript figures
│   └── figures/                   # Publication-grade figures (PNG/PDF)
├── research/
│   ├── literature/sota/           # 100% faithful replication of literature SOTA algorithms
│   │   ├── formation_energy/      # Ouyang et al. (2018) SISSO baseline benchmarks
│   │   ├── total_magnetization/   # Ghiringhelli et al. (2015) LASSO baseline benchmarks
│   │   ├── band_gap/              # Borlido et al. (2019) SISSO baseline benchmarks
│   │   ├── energy_above_hull/     # Bartel et al. (2019) tau-factor baseline benchmarks
│   │   └── sota_summary_report.md # Master benchmark summary report
│   ├── ablation_study/            # Step-by-step ablation study across conditions C0--C7
│   └── algorithm/                 # Detailed master architecture flow & routing specifications
├── data/                          # Curated 2,000 and 5,000 double perovskite DFT datasets
├── run_data_analysis.py           # Statistical profiling and zero-inflation analysis script
└── fetch_and_build_dataset.py     # High-throughput REST API dataset curation script
```

---

## 📊 Summary of Main Results

| Target Property | Baseline $R^2_{\text{limit}}$ | In-Sample $R^2$ | Limit Achieved (%) | 20% Held-Out Test $R^2$ | Test Limit Achieved (%) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Formation Energy ($\Delta E_f$)** | **65.0%** | **71.26%** | **109.62%** | **65.89 $\pm$ 6.92%** | **101.37%** |
| **Total Magnetization ($M$)** | **60.0%** | **62.23%** | **103.72%** | **16.70 $\pm$ 14.02%** | **30.28%** |
| **Electronic Band Gap ($E_g$)** | **50.0%** | **50.71%** | **101.42%** | **37.45 $\pm$ 3.66%** | **74.90%** |
| **Energy Above Hull ($E_{\text{hull}}$)** | **25.0%** | **16.67%** | **66.66%** | **6.85 $\pm$ 2.62%** | **27.41%** |

---

## 🛠️ Installation & Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/nihal-gazi/double_perovskite_compositional_interpretable.git
   cd double_perovskite_compositional_interpretable
   ```

2. **Install Dependencies**:
   ```bash
   pip install numpy pandas scikit-learn matplotlib seaborn
   ```

3. **Run Literature SOTA Benchmarks**:
   ```bash
   python research/literature/sota/run_sota_benchmarks.py
   ```

4. **Run Data Analysis**:
   ```bash
   python run_data_analysis.py
   ```

---

## 📜 Citation

If you use this codebase or data in your research, please cite our manuscript:

```bibtex
@article{gazi2026physicsgated,
  title={Physics-Gated Interpretable Machine Learning and Symbolic Regression for Double Perovskites: Overcoming Theoretical Limits Beyond 0D Compositional Models},
  author={Gazi, Nihal and Ghosh, Meghneel and Datta, Subarna and Pal, Soumyadipta},
  journal={Computational Materials Science},
  year={2026}
}
```
