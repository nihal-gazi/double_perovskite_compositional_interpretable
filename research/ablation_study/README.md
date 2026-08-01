# Master Algorithm Ablation Study

This directory contains the production-grade **Systematic Ablation Study** evaluating 8 distinct experimental conditions (C0 to C7) across all four target properties ($\Delta E_f, M, E_g, E_{\text{hull}}$).

---

## 1. Directory Structure

```text
exp_v2/research/ablation_study/
├── README.md               # Overview and usage instructions
├── method.md               # Formal mathematical specification of conditions C0-C7
├── ablation_matrix.py      # Feature and architecture isolation engine
├── pipeline.py             # Systematic evaluation orchestrator across C0-C7
├── requirements.txt        # Package dependencies
├── main.py                 # Single entry-point script to run the ablation study
└── results/                # Generated markdown reports, logs, and JSON data
    ├── ablation_summary_table.md
    ├── metrics_summary.txt
    └── ablation_summary.json
```

---

## 2. How to Run

Execute the single entry point:

```bash
python exp_v2/research/ablation_study/main.py
```
