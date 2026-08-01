"""
main.py
=======
Single entry-point script to run Experiment 14:
100% Fully Interpretable Multi-Operator Hurdle Model across all 4 target properties.
"""

import os
import sys
import numpy as np

EXP_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, EXP_DIR)

from src.pipeline import run_exp14_pipeline

def main():
    np.random.seed(42)

    root_dir = os.path.abspath(os.path.join(EXP_DIR, "..", ".."))
    dataset_path = os.path.join(root_dir, "data", "data_24_7_2026", "double_perovskite_dataset.csv")
    results_dir = os.path.join(EXP_DIR, "results")

    print("\n" + "#" * 75)
    print("      EXPERIMENT 14: 100% FULLY INTERPRETABLE MULTI-OPERATOR HURDLE MODEL")
    print("  Stage 1: Analytical Log-Odds Decision Boundary (S_cls(x) > tau*)")
    print("  Stage 2: Multi-Operator Physical Interaction Regressor (Ridge)")
    print("  Clean Physical Descriptors (No Data Leakage)")
    print("#" * 75 + "\n")

    results = run_exp14_pipeline(
        dataset_path=dataset_path,
        results_dir=results_dir,
        reg_model_type="ridge",
        alpha=1.0,
        l1_ratio=0.0
    )

    print("\n[SUCCESS] Experiment 14 completed cleanly.")

if __name__ == "__main__":
    main()
