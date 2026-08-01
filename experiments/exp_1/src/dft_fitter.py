"""
src/dft_fitter.py
=================
Multi-Dimensional DFT Curve Fitter using Complex K-Space Least Squares Solver.
Solves for the exact complex scaling matrix W in frequency space using FFT2 + Pseudo-Inverse.
"""

import torch

class DFTCurveFitter:
    """
    Deterministic Fourier operator solver fitting complex transfer matrices in K-space.

    Parameters
    ----------
    mode_k : int
        Number of low-frequency Fourier modes per spatial axis (k x k corner grid).
    """
    def __init__(self, mode_k: int = 4):
        self.mode_k = mode_k
        self.W = None
        self.c_in = None
        self.c_out = None

    def fit(self, X: torch.Tensor, Y: torch.Tensor) -> torch.Tensor:
        """
        Fits complex scaling weight matrix W using Complex Least Squares on 2D FFT modes.

        Parameters
        ----------
        X : torch.Tensor
            Input feature tensor of shape (B, N, N, C_in).
        Y : torch.Tensor
            Target feature tensor of shape (B, N, N, C_out).

        Returns
        -------
        torch.Tensor
            Complex scaling weight matrix W of shape (C_in, C_out).
        """
        B_sz, N1, N2, c_in = X.shape
        _, _, _, c_out = Y.shape

        self.c_in = c_in
        self.c_out = c_out

        k = min(self.mode_k, N1 // 2, N2 // 2)

        # 1. Forward 2D FFT over spatial dimensions (1, 2)
        X_hat = torch.fft.fft2(X, dim=(1, 2))  # (B, N, N, C_in)
        Y_hat = torch.fft.fft2(Y, dim=(1, 2))  # (B, N, N, C_out)

        # 2. Truncate low-frequency modes (k x k corner grid)
        X_trunc = X_hat[:, :k, :k, :]  # (B, k, k, C_in)
        Y_trunc = Y_hat[:, :k, :k, :]  # (B, k, k, C_out)

        # 3. Reshape for Complex Least Squares fitting (A W = B_mat)
        A = X_trunc.reshape(-1, c_in)    # (M, C_in) where M = B * k * k
        B_mat = Y_trunc.reshape(-1, c_out) # (M, C_out)

        # 4. Complex Least Squares solution W in C^(C_in x C_out)
        self.W = torch.linalg.lstsq(A, B_mat).solution  # (C_in, C_out)

        return self.W

    def predict(self, X: torch.Tensor) -> torch.Tensor:
        """
        Applies learned Fourier operator f(X) in K-space and reconstructs Y via Inverse 2D FFT.

        Parameters
        ----------
        X : torch.Tensor
            Input feature tensor of shape (B, N, N, C_in).

        Returns
        -------
        torch.Tensor
            Reconstructed real output tensor of shape (B, N, N, C_out).
        """
        if self.W is None:
            raise RuntimeError("DFTCurveFitter model is not fitted yet. Call fit() first.")

        B_sz, N1, N2, _ = X.shape
        k = min(self.mode_k, N1 // 2, N2 // 2)

        # 1. Forward 2D FFT
        X_hat = torch.fft.fft2(X, dim=(1, 2))  # (B, N, N, C_in)
        X_trunc = X_hat[:, :k, :k, :]          # (B, k, k, C_in)

        # 2. Predict intermediate complex modes in K-space
        Y_trunc_pred = torch.einsum('bjkc,cd->bjkd', X_trunc, self.W)  # (B, k, k, C_out)

        # 3. Zero-pad back to full spatial grid (B, N, N, C_out)
        Y_full = torch.zeros(B_sz, N1, N2, self.c_out, dtype=X_hat.dtype, device=X.device)
        Y_full[:, :k, :k, :] = Y_trunc_pred

        # 4. Inverse 2D FFT and take real component
        Y_pred = torch.real(torch.fft.ifft2(Y_full, dim=(1, 2)))

        return Y_pred
