"""
src/fourier_classifier.py
=========================
1D Fourier Series Classifier with Ridge Regularization for Numerical Stability at High Depths.
"""

import numpy as np
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

class FourierSeriesClassifier:
    """
    Fits 1D Fourier series representation mapping scalar feature x to binary target y_bin (0 or 1):
        f(x) = a_0 + sum_{m=1}^D [ a_m * cos(m * x_norm) + b_m * sin(m * x_norm) ]

    Parameters
    ----------
    depth : int
        Number of Fourier frequency modes / harmonics D (default: 3).
    alpha : float
        L2 Ridge regularization parameter for numerical stability at high D (default: 1e-4).
    """
    def __init__(self, depth: int = 3, alpha: float = 1e-4):
        self.depth = depth
        self.alpha = alpha
        self.weights = None
        self.x_min = None
        self.x_max = None

    def _normalize_x(self, x: np.ndarray) -> np.ndarray:
        if self.x_min is None or self.x_max is None:
            self.x_min = float(np.min(x))
            self.x_max = float(np.max(x))

        range_x = self.x_max - self.x_min
        if range_x < 1e-8:
            return np.zeros_like(x)

        # Clip x to training bounds [x_min, x_max] to prevent extrapolation explosion
        x_clipped = np.clip(x, self.x_min, self.x_max)
        return 2.0 * np.pi * (x_clipped - self.x_min) / range_x - np.pi

    def _build_basis(self, x_norm: np.ndarray) -> np.ndarray:
        n_samples = len(x_norm)
        basis = [np.ones(n_samples)]

        for m in range(1, self.depth + 1):
            basis.append(np.cos(m * x_norm))
            basis.append(np.sin(m * x_norm))

        return np.column_stack(basis)

    def fit(self, x: np.ndarray, y_bin: np.ndarray):
        x_flat = np.asarray(x).ravel()
        y_flat = np.asarray(y_bin).ravel()

        self.x_min = float(np.min(x_flat))
        self.x_max = float(np.max(x_flat))

        x_norm = self._normalize_x(x_flat)
        Phi = self._build_basis(x_norm)

        # Ridge Regression: (Phi^T Phi + alpha * I) w = Phi^T y
        reg_matrix = self.alpha * np.eye(Phi.shape[1])
        reg_matrix[0, 0] = 0.0  # Do not penalize constant bias term
        self.weights = np.linalg.solve(Phi.T @ Phi + reg_matrix, Phi.T @ y_flat)
        return self

    def predict_raw(self, x: np.ndarray) -> np.ndarray:
        if self.weights is None:
            raise RuntimeError("Classifier is not fitted yet. Call fit() first.")

        x_flat = np.asarray(x).ravel()
        x_norm = self._normalize_x(x_flat)
        Phi = self._build_basis(x_norm)

        raw = Phi @ self.weights
        return np.clip(raw, -0.5, 1.5)

    def predict(self, x: np.ndarray, threshold: float = 0.5) -> np.ndarray:
        raw_preds = self.predict_raw(x)
        return (raw_preds > threshold).astype(int)

    def evaluate(self, x: np.ndarray, y_bin: np.ndarray) -> dict:
        y_true = np.asarray(y_bin).ravel()
        raw_preds = self.predict_raw(x)
        pred_bin = (raw_preds > 0.5).astype(int)

        acc = float(accuracy_score(y_true, pred_bin))
        prec = float(precision_score(y_true, pred_bin, zero_division=0))
        rec = float(recall_score(y_true, pred_bin, zero_division=0))
        f1 = float(f1_score(y_true, pred_bin, zero_division=0))
        mse = float(np.mean((y_true - raw_preds) ** 2))

        return {
            "accuracy": acc,
            "precision": prec,
            "recall": rec,
            "f1": f1,
            "mse": mse
        }
