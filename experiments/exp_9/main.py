"""
main.py
=======
Single entry-point script to run Experiment 9:
Dual Symbolic Regression Hurdle Architecture with 19 extended mathematical operators in BOTH Stage 1 Classifier and Stage 2 Regressor.
Operators: add, sub, mul, div, neg, abs, log, pow, sin, cos, exp, tan, cosec, sec, mod, ceil, sign, nth_root, gaussian_function.
"""

import os
import sys
import numpy as np

EXP_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, EXP_DIR)

from src.pipeline import run_exp9_pipeline

def main():
    np.random.seed(42)

    root_dir = os.path.abspath(os.path.join(EXP_DIR, "..", ".."))
    dataset_path = os.path.join(root_dir, "data", "data_24_7_2026", "double_perovskite_dataset.csv")
    results_dir = os.path.join(EXP_DIR, "results")

    print("\n" + "#" * 75)
    print("      EXPERIMENT 9: DUAL SYMBOLIC REGRESSION WITH 19 EXTENDED OPERATORS")
    print("  Stage 1: Short Symbolic Boundary Classifier (+1/-1 Fitness)")
    print("  Stage 2: Standard Symbolic Regressor for Non-Zero Target Magnitude")
    print("  Operators: add, sub, mul, div, neg, abs, log, pow, sin, cos, exp, tan,")
    print("             cosec, sec, mod, ceil, sign, nth_root, gaussian_function")
    print("#" * 75 + "\n")

    results = run_exp9_pipeline(
        dataset_path=dataset_path,
        results_dir=results_dir
    )

    print("\n[SUCCESS] Experiment 9 completed cleanly.")

if __name__ == "__main__":
    main()
