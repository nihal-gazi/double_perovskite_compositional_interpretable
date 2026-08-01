"""
main.py
=======
Single entry-point script to run ood_test_2.
Evaluates Master Algorithm using an 80/20 split on the original 2,000 dataset (seed=42).
"""

import os
import sys

TEST2_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, TEST2_DIR)

from pipeline import run_ood_2_pipeline

def main():
    root_dir = os.path.abspath(os.path.join(TEST2_DIR, "..", ".."))
    dataset_path_2000 = os.path.join(root_dir, "data", "data_24_7_2026", "double_perovskite_dataset.csv")
    results_dir = os.path.join(TEST2_DIR, "results")

    print("\n" + "#" * 75)
    print("  OOD_TEST_2: MASTER ALGORITHM BENCHMARK ON 2,000 DATASET")
    print("  80% Train (1,600 materials) / 20% Held-Out Test (400 materials) | Seed = 42")
    print("  100% Pure Compositional Features (Zero 3D Coordinates / Zero Leaked Surrogates)")
    print("#" * 75 + "\n")

    results = run_ood_2_pipeline(
        dataset_path_2000=dataset_path_2000,
        results_dir=results_dir,
        seed=42
    )

    print("\n[SUCCESS] ood_test_2 Evaluation completed cleanly.")

if __name__ == "__main__":
    main()
