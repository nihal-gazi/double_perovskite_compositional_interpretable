"""
src/fourier_fitter.py
=====================
1D Discrete Fourier Series Least Squares Fitter.
Fits a Fourier series of depth D (num_freq) mapping a 1D scalar input feature to a target property.
"""

import numpy as np

class FourierSeries1DFitter:
    """
    Fits 1D Fourier series representation mapping scalar feature x to target property y:
        f(x) = a_0 + sum_{m=1}^D [ a_m * cos(m * x_norm) + b_m * sin(m * x_norm) ]

    Parameters
    ----------
    depth : int
        Number of Fourier frequency modes / harmonics D (default: 3).
    """
    def __init__(self, depth: int = 3):
        self.depth = depth
        self.weights = None
        self.x_min = None
        self.x_max = None

    def _normalize_x(self, x: np.ndarray) -> np.ndarray:
        """Normalizes x to [-pi, pi] for numerical stability in trigonometric functions."""
        if self.x_min is None or self.x_max is None:
            self.x_min = float(np.min(x))
            self.x_max = float(np.max(x))

        range_x = self.x_max - self.x_min
        if range_x < 1e-8:
            return np.zeros_like(x)

        # Scale to [-pi, pi]
        return 2.0 * np.pi * (x - self.x_min) / range_x - np.pi

    def _build_basis(self, x_norm: np.ndarray) -> np.ndarray:
        """Constructs Fourier basis matrix Phi of shape (M, 2*D + 1)."""
        n_samples = len(x_norm)
        basis = [np.ones(n_samples)]

        for m in range(1, self.depth + 1):
            basis.append(np.cos(m * x_norm))
            basis.append(np.sin(m * x_norm))

        return np.column_stack(basis)

    def fit(self, x: np.ndarray, y: np.ndarray):
        """
        Fits Fourier series coefficients w in R^(2*D + 1) using Least Squares.

        Parameters
        ----------
        x : np.ndarray
            1D scalar input feature array of shape (M,).
        y : np.ndarray
            Target property array of shape (M,).

        Returns
        -------
        FourierSeries1DFitter
            Self object with fitted weights.
        """
        x_flat = np.asarray(x).ravel()
        y_flat = np.asarray(y).ravel()

        self.x_min = float(np.min(x_flat))
        self.x_max = float(np.max(x_flat))

        x_norm = self._normalize_x(x_flat)
        Phi = self._build_basis(x_norm)

        # Solve Phi * w = y via Ordinary Least Squares
        self.weights, _, _, _ = np.linalg.lstsq(Phi, y_flat, rcond=None)
        return self

    def predict(self, x: np.ndarray) -> np.ndarray:
        """
        Predicts target y given input x using fitted Fourier series.

        Parameters
        ----------
        x : np.ndarray
            1D scalar input feature array.

        Returns
        -------
        np.ndarray
            Predicted target values.
        """
        if self.weights is None:
            raise RuntimeError("Fitter is not fitted yet. Call fit() first.")

        x_flat = np.asarray(x).ravel()
        x_norm = self._normalize_x(x_flat)
        Phi = self._build_basis(x_norm)

        return Phi @ self.weights

    def evaluate(self, x: np.ndarray, y: np.ndarray) -> dict:
        """Evaluates R^2, MSE, and MAE metrics."""
        y_true = np.asarray(y).ravel()
        y_pred = self.predict(x)

        ss_tot = np.sum((y_true - np.mean(y_true)) ** 2)
        ss_res = np.sum((y_true - y_pred) ** 2)

        r2 = 1.0 - (ss_res / (ss_tot + 1e-10))
        mse = float(np.mean((y_true - y_pred) ** 2))
        mae = float(np.mean(np.abs(y_true - y_pred)))

        return {"r2": float(r2), "mse": mse, "mae": mae}
