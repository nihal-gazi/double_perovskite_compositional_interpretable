# Multi-Seed 80/20 Benchmark Evaluation (5,000 Dataset)

This directory contains the production-grade **Multi-Seed 80/20 Train-Test Benchmark Evaluation** for our Master Capstone Algorithm across **25 distinct random seeds** on the 5,000 double perovskites dataset (`exp_v2/data/data_28_7_2026/double_perovskite_dataset_5000.csv`).

---

## 1. Directory Architecture

```text
exp_v2/research/ood_test/
├── README.md               # Overview and execution guide
├── method.md               # Formal 25-seed 80/20 methodology specification
├── fetch_dataset_5000.py   # Materials Project API data retrieval script
├── multi_seed_evaluator.py # Core 25-seed evaluation engine & aggregator
├── pipeline.py             # Pipeline orchestrator
├── requirements.txt        # Package dependencies
├── main.py                 # Single entry-point script to run the benchmark
├── multi_seed_report.md    # Publication-grade Markdown summary report (mean +/- std)
├── multi_seed_summary.json # Complete raw JSON summary across all 25 seeds
└── results/                # Seed-by-seed metric outputs
    └── seeds/              # JSON metrics for individual seeds (seed_42 to seed_120)
```

---

## 2. Benchmark Protocol

- **Dataset Size:** 5,000 double perovskites ($A_2 B B' O_6$)
- **Split Ratio:** 80% Train (4,000 materials) / 20% Held-Out Test (1,000 materials)
- **Seeds Evaluated (25):** `[42, 100, 2026, 777, 999, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120]`
- **Report Outputs:** Mean $\pm$ Standard Deviation ($\mu \pm \sigma$) across all 25 seeds in [`multi_seed_report.md`](multi_seed_report.md).

---

## 3. How to Run

Execute the single entry point script:

```bash
python exp_v2/research/ood_test/main.py
```
