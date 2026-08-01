"""
main.py
=======
Single entry-point script to run Experiment 11:
Standard Linear Regression Baseline across all 4 target properties.
"""

import os
import sys
import numpy as np

EXP_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, EXP_DIR)

from src.pipeline import run_exp11_pipeline

def main():
    np.random.seed(42)

    root_dir = os.path.abspath(os.path.join(EXP_DIR, "..", ".."))
    dataset_path = os.path.join(root_dir, "data", "data_24_7_2026", "double_perovskite_dataset.csv")
    results_dir = os.path.join(EXP_DIR, "results")

    print("\n" + "#" * 75)
    print("      EXPERIMENT 11: STANDARD LINEAR REGRESSION BASELINE")
    print("  Direct OLS Linear Regression & Two-Stage Linear Hurdle System")
    print("  Clean Physical Descriptors (33 Features, No Data Leakage)")
    print("#" * 75 + "\n")

    results = run_exp11_pipeline(
        dataset_path=dataset_path,
        results_dir=results_dir
    )

    print("\n[SUCCESS] Experiment 11 completed cleanly.")

if __name__ == "__main__":
    main()
