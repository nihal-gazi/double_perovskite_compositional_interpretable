"""
main.py
=======
Single entry-point script to run the Capstone Double Perovskite Machine Learning Algorithm.
Imports modularized feature, model, and pipeline engines from the research/algorithm package.
"""

import os
import sys
import numpy as np

ALG_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ALG_DIR)

from pipeline import run_master_pipeline

def main():
    np.random.seed(42)

    root_dir = os.path.abspath(os.path.join(ALG_DIR, "..", ".."))
    dataset_path = os.path.join(root_dir, "data", "data_24_7_2026", "double_perovskite_dataset.csv")
    results_dir = os.path.join(ALG_DIR, "results")

    print("\n" + "#" * 75)
    print("  CAPSTONE ALGORITHM: MASTER DOUBLE PEROVSKITE INTERPRETABLE ML")
    print("  100% Pure Compositional Features (Zero 3D Coordinates / Zero Leaked Surrogates)")
    print("  Combines Quantum Tight-Binding, Birch-Murnaghan Strain & Convex Hull Tie-Lines")
    print("#" * 75 + "\n")

    results = run_master_pipeline(
        dataset_path=dataset_path,
        results_dir=results_dir
    )

    print("\n[SUCCESS] Master Capstone Algorithm completed cleanly.")

if __name__ == "__main__":
    main()
