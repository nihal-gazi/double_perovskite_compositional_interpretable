"""
pipeline.py
===========
Pipeline orchestrator for ood_test_2_multi_seed evaluation.
"""

import os
import sys
from multi_seed_evaluator import run_multi_seed_evaluation_2000

def run_ood_2_multi_seed_pipeline(
    dataset_path_2000: str,
    base_output_dir: str
):
    return run_multi_seed_evaluation_2000(
        dataset_path_2000=dataset_path_2000,
        base_output_dir=base_output_dir
    )
