"""
main.py
=======
Single entry-point script to run ood_test_2_multi_seed.
Evaluates Master Algorithm across 10 random seeds on the 2,000 dataset.
"""

import os
import sys

DIR_PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, DIR_PATH)

from pipeline import run_ood_2_multi_seed_pipeline

def main():
    root_dir = os.path.abspath(os.path.join(DIR_PATH, "..", ".."))
    dataset_path_2000 = os.path.join(root_dir, "data", "data_24_7_2026", "double_perovskite_dataset.csv")

    print("\n" + "#" * 75)
    print("  OOD_TEST_2_MULTI_SEED: MASTER ALGORITHM BENCHMARK ON 2,000 DATASET")
    print("  Evaluating Master Model across 10 Random Seeds (42 + 9 more)")
    print("  100% Pure Compositional Features (Zero 3D Coordinates / Zero Leaked Surrogates)")
    print("#" * 75 + "\n")

    summary_stats = run_ood_2_multi_seed_pipeline(
        dataset_path_2000=dataset_path_2000,
        base_output_dir=DIR_PATH
    )

    print("\n[SUCCESS] ood_test_2_multi_seed Evaluation completed cleanly.")

if __name__ == "__main__":
    main()
