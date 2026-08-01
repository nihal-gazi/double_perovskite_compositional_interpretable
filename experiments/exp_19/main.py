"""
main.py
=======
Single entry-point script to run Experiment 19:
Octahedral d0/d10 Closed-Shell Engine & Binary Oxidation Enthalpy Mismatch.
"""

import os
import sys
import numpy as np

EXP_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, EXP_DIR)

from src.pipeline import run_exp19_pipeline

def main():
    np.random.seed(42)

    root_dir = os.path.abspath(os.path.join(EXP_DIR, "..", ".."))
    dataset_path = os.path.join(root_dir, "data", "data_24_7_2026", "double_perovskite_dataset.csv")
    results_dir = os.path.join(EXP_DIR, "results")

    print("\n" + "#" * 75)
    print("  EXPERIMENT 19: OCTAHEDRAL d0/d10 CLOSED-SHELL ENGINE & OXIDATION ENTHALPY")
    print("  Octahedral d0/d10 Engine, Binary Oxidation Enthalpy & Soft-Gated Regressor")
    print("  100% Pure Compositional Features (Zero 3D Coordinates / Zero Leaked Surrogates)")
    print("#" * 75 + "\n")

    results = run_exp19_pipeline(
        dataset_path=dataset_path,
        results_dir=results_dir
    )

    print("\n[SUCCESS] Experiment 19 completed cleanly.")

if __name__ == "__main__":
    main()
