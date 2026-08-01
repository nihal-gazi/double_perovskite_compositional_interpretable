"""
src/pairformer.py
=================
Implementation of PyTorch Pairformer Sub-Blocks (L1 and L2 stages).
Operates on 4D pairwise representations Z in R^(B x N x N x C).
"""

import torch
import torch.nn as nn

class PairformerBlock(nn.Module):
    """
    Two-stage Pairformer Sub-Block module.

    Parameters
    ----------
    c_in : int
        Channel dimension C of the input pairwise representation.
    """
    def __init__(self, c_in: int = 32):
        super().__init__()
        self.c_in = c_in
        self.c_mid = c_in // 2

        # Stage 1: Triangular Multiplicative Update
        self.ln1 = nn.LayerNorm(c_in)
        self.proj_L = nn.Linear(c_in, self.c_mid)
        self.proj_R = nn.Linear(c_in, self.c_mid)
        self.proj_out = nn.Linear(self.c_mid, c_in)

        # Stage 2: Multi-Layer Perceptron Transition
        self.ln2 = nn.LayerNorm(c_in)
        self.mlp_linear1 = nn.Linear(c_in, 2 * c_in)
        self.act = nn.GELU()
        self.mlp_linear2 = nn.Linear(2 * c_in, c_in)

    def forward(self, z: torch.Tensor):
        """
        Forward pass of PairformerBlock.

        Parameters
        ----------
        z : torch.Tensor
            Input pairwise tensor of shape (B, N, N, C).

        Returns
        -------
        tuple of (torch.Tensor, torch.Tensor)
            Tuple containing intermediate tensor L1 and final output L2.
        """
        # 1. Symmetrization across spatial dimensions (1, 2)
        z_sym = 0.5 * (z + z.transpose(1, 2))

        # 2. Stage 1: Triangular Multiplicative Update (Z_in -> L1)
        z_norm1 = self.ln1(z_sym)
        L = self.proj_L(z_norm1)  # (B, N, N, C/2)
        R = self.proj_R(z_norm1)  # (B, N, N, C/2)

        # Batched tensor contraction U_{i,j,c} = sum_k L_{i,k,c} * R_{j,k,c}
        U = torch.einsum('bikc,bjkc->bijc', L, R)  # (B, N, N, C/2)
        U_proj = self.proj_out(U)  # (B, N, N, C)

        # Residual Connection for Stage 1
        L1 = z + U_proj

        # 3. Stage 2: MLP Transition (L1 -> L2)
        L1_norm = self.ln2(L1)
        mlp_out = self.mlp_linear2(self.act(self.mlp_linear1(L1_norm)))

        # Residual Connection for Stage 2
        L2 = L1 + mlp_out

        return L1, L2
