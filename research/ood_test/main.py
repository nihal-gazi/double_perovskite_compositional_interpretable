"""
main.py
=======
Single entry-point script to run the Multi-Seed 80/20 Train-Test Evaluation (5,000 Dataset).
Evaluates Master Algorithm across random seeds: 42, 100, 2026, 777, 999.
"""

import os
import sys

OOD_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, OOD_DIR)

from multi_seed_evaluator import run_multi_seed_evaluation

def main():
    root_dir = os.path.abspath(os.path.join(OOD_DIR, "..", ".."))
    ood_dataset_path = os.path.join(root_dir, "data", "data_28_7_2026", "double_perovskite_dataset_5000.csv")

    print("\n" + "#" * 75)
    print("  MULTI-SEED 80/20 TRAIN-TEST BENCHMARK: MASTER ALGORITHM")
    print("  Evaluating Master Model across Random Seeds: [42, 100, 2026, 777, 999]")
    print("  100% Pure Compositional Features (Zero 3D Coordinates / Zero Leaked Surrogates)")
    print("#" * 75 + "\n")

    summary_stats = run_multi_seed_evaluation(
        dataset_path_5000=ood_dataset_path,
        base_output_dir=OOD_DIR
    )

    print("\n[SUCCESS] Multi-Seed Evaluation completed cleanly.")

if __name__ == "__main__":
    main()
