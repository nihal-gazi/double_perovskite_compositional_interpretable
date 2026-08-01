"""
main.py
=======
Single entry-point script to run Experiment 4:
Top-K Ensemble Size Sweep (K = 1 to 10) for Two-Stage Fourier Ensemble Architecture across depths D = {3, 5, 10, 50, 100}.
Identifies and reports the best K value for each target property and Fourier depth.
"""

import os
import sys
import numpy as np

EXP_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, EXP_DIR)

from src.pipeline import run_exp4_pipeline

def main():
    np.random.seed(42)

    root_dir = os.path.abspath(os.path.join(EXP_DIR, "..", ".."))
    dataset_path = os.path.join(root_dir, "data", "data_24_7_2026", "double_perovskite_dataset.csv")
    results_dir = os.path.join(EXP_DIR, "results")

    print("\n" + "#" * 75)
    print("      EXPERIMENT 4: TOP-K ENSEMBLE SIZE SWEEP (K = 1 TO 10)")
    print("  Evaluating Classifier-Regressor Fourier Ensemble Across Depths D = {3, 5, 10, 50, 100}")
    print("#" * 75 + "\n")

    results, best_k_summary = run_exp4_pipeline(
        dataset_path=dataset_path,
        results_dir=results_dir,
        k_range=list(range(1, 11)),
        depths=[3, 5, 10, 50, 100]
    )

    print("\n[SUCCESS] Experiment 4 completed cleanly.")

if __name__ == "__main__":
    main()
