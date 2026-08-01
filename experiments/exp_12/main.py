"""
main.py
=======
Single entry-point script to run Experiment 12:
Physical Interaction & Polynomial-Linear Hybrid Model Baseline across all 4 target properties.
"""

import os
import sys
import numpy as np

EXP_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, EXP_DIR)

from src.pipeline import run_exp12_pipeline

def main():
    np.random.seed(42)

    root_dir = os.path.abspath(os.path.join(EXP_DIR, "..", ".."))
    dataset_path = os.path.join(root_dir, "data", "data_24_7_2026", "double_perovskite_dataset.csv")
    results_dir = os.path.join(EXP_DIR, "results")

    print("\n" + "#" * 75)
    print("      EXPERIMENT 12: PHYSICAL INTERACTION & POLYNOMIAL-LINEAR HYBRID MODEL")
    print("  Direct Interaction Model & Two-Stage Interaction Hurdle System")
    print("  Clean Physical Descriptors + 2nd-Order Interactions (x_i*x_j, x_i/x_j, x_i^2)")
    print("#" * 75 + "\n")

    results = run_exp12_pipeline(
        dataset_path=dataset_path,
        results_dir=results_dir,
        model_type="ridge",
        alpha=1.0
    )

    print("\n[SUCCESS] Experiment 12 completed cleanly.")

if __name__ == "__main__":
    main()
