# ood_test_2: 80/20 Train-Test Benchmark (2,000 Dataset)

This directory contains the production-grade **ood_test_2 Benchmark Evaluation** for our Master Capstone Algorithm using an **80/20 Train-Test Split** on the original 2,000 double perovskite dataset (`exp_v2/data/data_24_7_2026/double_perovskite_dataset.csv`).

---

## 1. Directory Architecture

```text
exp_v2/research/ood_test_2/
├── README.md               # Overview and execution guide
├── method.md               # Formal 80/20 split methodology specification
├── evaluator.py            # Core evaluation engine
├── pipeline.py             # Pipeline orchestrator
├── main.py                 # Single entry-point script to run the benchmark
└── results/                # Generated markdown reports, logs, and JSON data
    ├── summary_table.md    # Markdown summary report table
    ├── discovered_equations.md # Generated physical analytical equations
    ├── metrics_summary.txt # Full execution log
    └── metrics.json        # Raw JSON metrics
```

---

## 2. Benchmark Protocol

- **Dataset:** 2,000 double perovskite compounds (`exp_v2/data/data_24_7_2026/double_perovskite_dataset.csv`)
- **Split Ratio:** 80% Train (1,600 materials) / 20% Held-Out Test (400 materials)
- **Random Seed:** `seed = 42`

---

## 3. How to Run

Execute the single entry point script:

```bash
python exp_v2/research/ood_test_2/main.py
```
