"""
main.py
=======
Single entry-point script to run Experiment 8:
Dual Symbolic Regression Hurdle Architecture with protected 'pow' operator in BOTH Stage 1 Classifier and Stage 2 Regressor.
"""

import os
import sys
import numpy as np

EXP_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, EXP_DIR)

from src.pipeline import run_exp8_pipeline

def main():
    np.random.seed(42)

    root_dir = os.path.abspath(os.path.join(EXP_DIR, "..", ".."))
    dataset_path = os.path.join(root_dir, "data", "data_24_7_2026", "double_perovskite_dataset.csv")
    results_dir = os.path.join(EXP_DIR, "results")

    print("\n" + "#" * 75)
    print("      EXPERIMENT 8: DUAL SYMBOLIC REGRESSION WITH POWER OPERATOR (pow)")
    print("  Stage 1: Short Symbolic Regression Decision Boundary (+1/-1 Fitness with 'pow')")
    print("  Stage 2: Standard Symbolic Regression for Non-Zero Target Magnitude (with 'pow')")
    print("  Operators: add, sub, mul, div, neg, abs, log, pow")
    print("#" * 75 + "\n")

    results = run_exp8_pipeline(
        dataset_path=dataset_path,
        results_dir=results_dir
    )

    print("\n[SUCCESS] Experiment 8 completed cleanly.")

if __name__ == "__main__":
    main()
