"""
main.py
=======
Single entry-point script to run the Master Algorithm Ablation Study.
Evaluates Conditions C0 through C7 across all 4 target properties.
"""

import os
import sys
import numpy as np

ABL_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ABL_DIR)

from pipeline import run_ablation_study

def main():
    np.random.seed(42)

    root_dir = os.path.abspath(os.path.join(ABL_DIR, "..", ".."))
    dataset_path = os.path.join(root_dir, "data", "data_24_7_2026", "double_perovskite_dataset.csv")
    results_dir = os.path.join(ABL_DIR, "results")

    print("\n" + "#" * 75)
    print("  SYSTEMATIC ABLATION STUDY: MASTER DOUBLE PEROVSKITE INTERPRETABLE ML")
    print("  Evaluating Conditions C0 -> C7 across all 4 target properties")
    print("  100% Pure Compositional Features (Zero 3D Coordinates / Zero Leaked Surrogates)")
    print("#" * 75 + "\n")

    results = run_ablation_study(
        dataset_path=dataset_path,
        results_dir=results_dir
    )

    print("\n[SUCCESS] Systematic Ablation Study completed cleanly.")

if __name__ == "__main__":
    main()
