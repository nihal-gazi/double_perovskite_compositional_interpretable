"""
main.py
=======
Single entry-point script to run Experiment 2:
Multi-descriptor 1D Fourier Transform distillation and top-K ensemble averaging across depths D = {3, 5, 10, 50, 100}.
"""

import os
import sys
import numpy as np

EXP_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, EXP_DIR)

from src.pipeline import run_exp2_pipeline

def main():
    np.random.seed(42)

    root_dir = os.path.abspath(os.path.join(EXP_DIR, "..", ".."))
    dataset_path = os.path.join(root_dir, "data", "data_24_7_2026", "double_perovskite_dataset.csv")
    results_dir = os.path.join(EXP_DIR, "results")

    print("\n" + "#" * 75)
    print("      EXPERIMENT 2: MULTI-DESCRIPTOR FOURIER TRANSFORM DISTILLATION")
    print("  Evaluating Top-K=5 Ensemble Averaging Across Depths D = {3, 5, 10, 50, 100}")
    print("#" * 75 + "\n")

    results = run_exp2_pipeline(
        dataset_path=dataset_path,
        results_dir=results_dir,
        top_k=5,
        depths=[3, 5, 10, 50, 100]
    )

    print("\n[SUCCESS] Experiment 2 completed cleanly.")

if __name__ == "__main__":
    main()
