"""
main.py
=======
Single entry-point script to run data analysis and generate all EDA plots
for exp_v2/research/data/analysis_1/.
"""

import os
import sys

ANALYSIS_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ANALYSIS_DIR)

from src.generate_graphs import generate_all_eda_graphs

def main():
    root_dir = os.path.abspath(os.path.join(ANALYSIS_DIR, "..", "..", ".."))
    dataset_path = os.path.join(root_dir, "data", "data_24_7_2026", "double_perovskite_dataset.csv")
    output_graphs_dir = os.path.join(ANALYSIS_DIR, "graphs")

    print("\n" + "=" * 70)
    print("      DATA ANALYSIS 1: EXPLORATORY DATA ANALYSIS & GRAPH GENERATION")
    print("=" * 70 + "\n")

    generate_all_eda_graphs(
        dataset_path=dataset_path,
        output_graphs_dir=output_graphs_dir
    )

    print("\n[SUCCESS] Main EDA pipeline completed successfully.")

if __name__ == "__main__":
    main()
