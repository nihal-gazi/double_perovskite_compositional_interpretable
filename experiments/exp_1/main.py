"""
main.py
=======
Single entry-point script to run training, complex K-space DFT distillation,
and persistent artifact saving for exp_1.
"""

import os
import sys
import torch

# Add parent directory to path so src imports work cleanly
EXP_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, EXP_DIR)

from src.pipeline import run_distillation_pipeline

def main():
    # 1. Deterministic Execution Seed
    SEED = 42
    torch.manual_seed(SEED)

    results_dir = os.path.join(EXP_DIR, "results")

    print("\n" + "#" * 75)
    print("      NOVEL INTERPRETABLE AI ARCHITECTURE EXPERIMENT (EXP_1)")
    print("  Sequential DFT-Symbolic Distillation of Pairformer Block (K-Space)")
    print("#" * 75 + "\n")

    # 2. Run Pipeline
    metrics = run_distillation_pipeline(
        b_size=64,
        n_spatial=16,
        c_channels=32,
        epochs=50,
        mode_k=4,
        results_dir=results_dir
    )

    print("\n[SUCCESS] Execution completed cleanly.")

if __name__ == "__main__":
    main()
