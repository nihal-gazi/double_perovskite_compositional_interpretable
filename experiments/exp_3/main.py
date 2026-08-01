"""
main.py
=======
Single entry-point script to run Experiment 3:
Two-Stage Fourier Ensemble Hurdle Architecture across depths D = {3, 5, 10, 50, 100}.
"""

import os
import sys
import numpy as np

EXP_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, EXP_DIR)

from src.pipeline import run_exp3_pipeline

def main():
    np.random.seed(42)

    root_dir = os.path.abspath(os.path.join(EXP_DIR, "..", ".."))
    dataset_path = os.path.join(root_dir, "data", "data_24_7_2026", "double_perovskite_dataset.csv")
    results_dir = os.path.join(EXP_DIR, "results")

    print("\n" + "#" * 75)
    print("  EXPERIMENT 3: TWO-STAGE FOURIER ENSEMBLE HURDLE ARCHITECTURE EXPERIMENT")
    print("  Zero vs Non-Zero Fourier Classifier + Non-Zero Fourier Regressor (K=5)")
    print("  Evaluating Depths D = {3, 5, 10, 50, 100}")
    print("#" * 75 + "\n")

    results = run_exp3_pipeline(
        dataset_path=dataset_path,
        results_dir=results_dir,
        top_k=5,
        depths=[3, 5, 10, 50, 100]
    )

    print("\n[SUCCESS] Experiment 3 completed cleanly.")

if __name__ == "__main__":
    main()
