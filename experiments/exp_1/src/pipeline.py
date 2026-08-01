"""
src/pipeline.py
===============
Sequential Distillation & Evaluation Orchestration Pipeline.
Conducts base model training, intermediate tensor extraction, sequential complex DFT fitting,
and metric persistence.
"""

import os
import torch
import torch.nn as nn
from .pairformer import PairformerBlock
from .dft_fitter import DFTCurveFitter

def run_distillation_pipeline(
    b_size: int = 64,
    n_spatial: int = 16,
    c_channels: int = 32,
    epochs: int = 50,
    mode_k: int = 4,
    results_dir: str = None
):
    """
    Executes the full sequential distillation pipeline.

    Parameters
    ----------
    b_size : int
        Batch size (default: 64).
    n_spatial : int
        Spatial size N for (N x N) pairwise grid (default: 16).
    c_channels : int
        Channel dimension C (default: 32).
    epochs : int
        Base model training epochs (default: 50).
    mode_k : int
        Number of low-frequency Fourier modes per spatial dimension (default: 4).
    results_dir : str
        Directory to save results and weight matrices.

    Returns
    -------
    dict
        Dictionary containing pipeline metrics, model outputs, and saved paths.
    """
    print("=" * 70)
    print("STAGE 1: Synthetic Data Generation & Pairformer Base Model Setup")
    print("=" * 70)

    # 1. Synthetic Pairwise Feature Input Z_in ~ N(0, 1)
    Z_in = torch.randn(b_size, n_spatial, n_spatial, c_channels)
    print(f"Generated input tensor Z_in: shape {Z_in.shape}, mean {Z_in.mean().item():.4f}, std {Z_in.std().item():.4f}")

    # Non-linear synthetic target T
    Target = torch.sin(Z_in) + 0.5 * (Z_in ** 2)

    # 2. Base Model Training
    base_model = PairformerBlock(c_in=c_channels)
    optimizer = torch.optim.Adam(base_model.parameters(), lr=0.005)
    criterion = nn.MSELoss()

    print(f"\nTraining PairformerBlock for {epochs} epochs on non-linear task Z_in -> Target...")
    base_model.train()
    for epoch in range(1, epochs + 1):
        optimizer.zero_grad()
        _, L2_pred = base_model(Z_in)
        loss = criterion(L2_pred, Target)
        loss.backward()
        optimizer.step()

        if epoch % 10 == 0 or epoch == 1:
            print(f"  Epoch [{epoch:02d}/{epochs:02d}] - MSE Loss: {loss.item():.6f}")

    # 3. Freeze Base Model & Extract Intermediate Tensors
    base_model.eval()
    for param in base_model.parameters():
        param.requires_grad = False

    with torch.no_grad():
        L1_gt, L2_gt = base_model(Z_in)

    print(f"\nExtracted Ground-Truth Tensors from Base Model:")
    print(f"  Input  Z_in : shape {Z_in.shape}")
    print(f"  Stage 1 L1  : shape {L1_gt.shape}, norm {torch.norm(L1_gt).item():.4f}")
    print(f"  Stage 2 L2  : shape {L2_gt.shape}, norm {torch.norm(L2_gt).item():.4f}")

    # 4. Distillation Stage 1 (Z_in -> L1)
    print("\n" + "=" * 70)
    print("STAGE 2: Complex K-Space DFT Distillation Stage 1 (Z_in -> L1)")
    print("=" * 70)

    fitter1 = DFTCurveFitter(mode_k=mode_k)
    W1 = fitter1.fit(Z_in, L1_gt)
    L1_hat = fitter1.predict(Z_in)

    mse_stage1 = torch.mean((L1_gt - L1_hat) ** 2).item()
    rel_l2_stage1 = (torch.norm(L1_gt - L1_hat) / torch.norm(L1_gt)).item()

    print(f"Stage 1 Fitted Complex Weight W1: shape {W1.shape}, dtype {W1.dtype}")
    print(f"Stage 1 Distillation Metrics (Z_in -> L1_hat):")
    print(f"  - Mean Squared Error (MSE)   : {mse_stage1:.6e}")
    print(f"  - Relative L2 Error          : {rel_l2_stage1 * 100:.2f}% ({rel_l2_stage1:.6f})")

    # 5. Distillation Stage 2 (L1_hat -> L2)
    print("\n" + "=" * 70)
    print("STAGE 3: Complex K-Space DFT Distillation Stage 2 (L1_hat -> L2)")
    print("=" * 70)

    fitter2 = DFTCurveFitter(mode_k=mode_k)
    W2 = fitter2.fit(L1_hat, L2_gt)
    L2_hat = fitter2.predict(L1_hat)

    mse_stage2 = torch.mean((L2_gt - L2_hat) ** 2).item()
    rel_l2_stage2 = (torch.norm(L2_gt - L2_hat) / torch.norm(L2_gt)).item()

    print(f"Stage 2 Fitted Complex Weight W2: shape {W2.shape}, dtype {W2.dtype}")
    print(f"Stage 2 Distillation Metrics (L1_hat -> L2_hat):")
    print(f"  - Mean Squared Error (MSE)   : {mse_stage2:.6e}")
    print(f"  - Relative L2 Error          : {rel_l2_stage2 * 100:.2f}% ({rel_l2_stage2:.6f})")

    # 6. Artifact Persistence
    if results_dir:
        os.makedirs(results_dir, exist_ok=True)
        w1_path = os.path.join(results_dir, "W1.pt")
        w2_path = os.path.join(results_dir, "W2.pt")
        summary_path = os.path.join(results_dir, "metrics_summary.txt")

        torch.save(W1, w1_path)
        torch.save(W2, w2_path)

        summary_content = f"""======================================================================
SEQUENTIAL DFT-SYMBOLIC DISTILLATION OF PAIRFORMER BLOCK
======================================================================
Generated Results Summary
Date / Seed: torch.manual_seed(42)

1. ARCHITECTURAL & TENSOR DIMENSIONS
------------------------------------
Input Tensor Z_in      : {list(Z_in.shape)}
Intermediate L1        : {list(L1_gt.shape)}
Final Output L2        : {list(L2_gt.shape)}
Fourier Mode Grid (k)  : {mode_k} x {mode_k} corner grid (out of {n_spatial}x{n_spatial})
Complex Weight W1      : {list(W1.shape)} (dtype: {W1.dtype})
Complex Weight W2      : {list(W2.shape)} (dtype: {W2.dtype})

2. BASE MODEL TRAINING METRICS
------------------------------
Task                   : Synthetic Non-Linear Target Z_in -> Target
Epochs                 : {epochs}
Final Base Training MSE: {loss.item():.6e}

3. DISTILLATION PERFORMANCE METRICS
-----------------------------------
Stage 1 (Z_in -> L1):
  - MSE Error          : {mse_stage1:.6e}
  - Relative L2 Error  : {rel_l2_stage1:.6f} ({rel_l2_stage1 * 100:.2f}%)

Stage 2 (L1_hat -> L2):
  - MSE Error          : {mse_stage2:.6e}
  - Relative L2 Error  : {rel_l2_stage2:.6f} ({rel_l2_stage2 * 100:.2f}%)

End-to-End Reconstructed Error (Z_in -> L2_hat):
  - Final MSE          : {mse_stage2:.6e}
  - Final Relative L2  : {rel_l2_stage2:.6f} ({rel_l2_stage2 * 100:.2f}%)

4. ARTIFACT SAVED PATHS
-----------------------
Weight Matrix W1       : {w1_path}
Weight Matrix W2       : {w2_path}
Metrics Summary        : {summary_path}
======================================================================
"""
        with open(summary_path, "w", encoding="utf-8") as f:
            f.write(summary_content)

        print("\n" + "=" * 70)
        print(f"Artifacts successfully saved to: {results_dir}")
        print(f"  - Weight Matrix W1: {w1_path}")
        print(f"  - Weight Matrix W2: {w2_path}")
        print(f"  - Metrics Summary : {summary_path}")
        print("=" * 70)

    return {
        "W1": W1,
        "W2": W2,
        "mse_stage1": mse_stage1,
        "rel_l2_stage1": rel_l2_stage1,
        "mse_stage2": mse_stage2,
        "rel_l2_stage2": rel_l2_stage2,
        "Z_in": Z_in,
        "L1_gt": L1_gt,
        "L2_gt": L2_gt,
        "L1_hat": L1_hat,
        "L2_hat": L2_hat
    }
