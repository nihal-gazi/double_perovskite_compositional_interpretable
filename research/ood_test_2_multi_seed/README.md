# ood_test_2_multi_seed: 10-Seed 80/20 Benchmark (2,000 Dataset)

This directory contains the production-grade **ood_test_2_multi_seed Benchmark Evaluation** for our Master Capstone Algorithm across **10 random seeds** (42 + 9 more: 100, 2026, 777, 999, 101, 102, 103, 104, 105) on the original 2,000 double perovskite dataset (`exp_v2/data/data_24_7_2026/double_perovskite_dataset.csv`).

---

## 1. Directory Architecture

```text
exp_v2/research/ood_test_2_multi_seed/
├── README.md               # Overview and execution guide
├── method.md               # Formal 10-seed 80/20 split methodology specification
├── multi_seed_evaluator.py # Core 10-seed evaluation engine & aggregator
├── pipeline.py             # Pipeline orchestrator
├── main.py                 # Single entry-point script to run the benchmark
├── multi_seed_report.md    # Publication-grade Markdown summary report (mean +/- std)
├── multi_seed_summary.json # Complete raw JSON summary across all 10 seeds
└── results/                # Seed-by-seed metric outputs
    └── seeds/              # JSON metrics for individual seeds
```

---

## 2. Benchmark Protocol

- **Dataset:** 2,000 double perovskites ($A_2 B B' O_6$)
- **Split Ratio:** 80% Train (1,600 materials) / 20% Held-Out Test (400 materials)
- **Seeds Evaluated (10):** `[42, 100, 2026, 777, 999, 101, 102, 103, 104, 105]`

---

## 3. How to Run

Execute the single entry point script:

```bash
python exp_v2/research/ood_test_2_multi_seed/main.py
```
