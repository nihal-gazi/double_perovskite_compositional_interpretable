"""
main.py
=======
Single entry-point script to run Experiment 5:
Hybrid Symbolic Regression Decision Boundary Classifier (+1/-1 fitness)
+ Optimal Top-K* Fourier Ensemble Non-Zero Regressor (dynamically sweeping K=1..10 per depth D).
"""

import os
import sys
import numpy as np

EXP_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, EXP_DIR)

from src.pipeline import run_exp5_pipeline

def main():
    np.random.seed(42)

    root_dir = os.path.abspath(os.path.join(EXP_DIR, "..", ".."))
    dataset_path = os.path.join(root_dir, "data", "data_24_7_2026", "double_perovskite_dataset.csv")
    results_dir = os.path.join(EXP_DIR, "results")

    print("\n" + "#" * 75)
    print("      EXPERIMENT 5: HYBRID SYMBOLIC BOUNDARY CLASSIFIER + FOURIER REGRESSOR")
    print("  Stage 1: Short Symbolic Regression Decision Boundary (+1/-1 Fitness)")
    print("  Stage 2: Optimal Top-K* Fourier Ensemble Non-Zero Regressor Across Depths D")
    print("#" * 75 + "\n")

    results = run_exp5_pipeline(
        dataset_path=dataset_path,
        results_dir=results_dir,
        k_range=list(range(1, 11)),
        depths=[3, 5, 10, 50, 100]
    )

    print("\n[SUCCESS] Experiment 5 completed cleanly.")

if __name__ == "__main__":
    main()
