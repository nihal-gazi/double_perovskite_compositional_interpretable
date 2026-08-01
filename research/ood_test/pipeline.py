"""
pipeline.py
===========
Pipeline orchestrator for 80/20 train-test evaluation on 5,000 dataset.
"""

import os
import sys
from ood_evaluator import evaluate_80_20_split

def run_ood_pipeline(
    train_dataset_path: str,
    ood_dataset_path: str,
    results_dir: str
):
    return evaluate_80_20_split(
        dataset_path_5000=ood_dataset_path,
        results_dir=results_dir
    )
