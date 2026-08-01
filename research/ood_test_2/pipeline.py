"""
pipeline.py
===========
Pipeline orchestrator for ood_test_2: 80/20 train-test split evaluation on the 2,000 dataset.
"""

import os
import sys
from evaluator import evaluate_2000_split

def run_ood_2_pipeline(
    dataset_path_2000: str,
    results_dir: str,
    seed: int = 42
):
    return evaluate_2000_split(
        dataset_path_2000=dataset_path_2000,
        results_dir=results_dir,
        seed=seed
    )
