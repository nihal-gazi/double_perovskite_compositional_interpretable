"""
main.py
=======
Single entry-point script to run Experiment 17:
Tight-Binding Proxies & Mendeleev Feature Engine with Cost-Sensitive Stage 1.
"""

import os
import sys
import numpy as np

EXP_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, EXP_DIR)

from src.pipeline import run_exp17_pipeline

def main():
    np.random.seed(42)

    root_dir = os.path.abspath(os.path.join(EXP_DIR, "..", ".."))
    dataset_path = os.path.join(root_dir, "data", "data_24_7_2026", "double_perovskite_dataset.csv")
    results_dir = os.path.join(EXP_DIR, "results")

    print("\n" + "#" * 75)
    print("  EXPERIMENT 17: TIGHT-BINDING PROXIES & MENDELEEV FEATURE ENGINE")
    print("  HOMO-LUMO Energy Proxies, Mendeleev Mismatch, VEC & Cost-Sensitive Stage 1")
    print("  100% Pure Compositional Features (Zero 3D Coordinates / Zero Leaked Surrogates)")
    print("#" * 75 + "\n")

    results = run_exp17_pipeline(
        dataset_path=dataset_path,
        results_dir=results_dir
    )

    print("\n[SUCCESS] Experiment 17 completed cleanly.")

if __name__ == "__main__":
    main()
