"""
src/fourier_regressor.py
========================
1D Fourier Series Regressor with Ridge Regularization for Numerical Stability.
"""

import numpy as np

class FourierSeriesRegressor:
    def __init__(self, depth: int = 3, alpha: float = 1e-4):
        self.depth = depth
        self.alpha = alpha
        self.weights = None
        self.x_min = None
        self.x_max = None
        self.y_min = None
        self.y_max = None

    def _normalize_x(self, x: np.ndarray) -> np.ndarray:
        if self.x_min is None or self.x_max is None:
            self.x_min = float(np.min(x))
            self.x_max = float(np.max(x))

        range_x = self.x_max - self.x_min
        if range_x < 1e-8:
            return np.zeros_like(x)

        x_clipped = np.clip(x, self.x_min, self.x_max)
        return 2.0 * np.pi * (x_clipped - self.x_min) / range_x - np.pi

    def _build_basis(self, x_norm: np.ndarray) -> np.ndarray:
        n_samples = len(x_norm)
        basis = [np.ones(n_samples)]

        for m in range(1, self.depth + 1):
            basis.append(np.cos(m * x_norm))
            basis.append(np.sin(m * x_norm))

        return np.column_stack(basis)

    def fit(self, x: np.ndarray, y: np.ndarray):
        x_flat = np.asarray(x).ravel()
        y_flat = np.asarray(y).ravel()

        self.x_min = float(np.min(x_flat))
        self.x_max = float(np.max(x_flat))
        self.y_min = float(np.min(y_flat))
        self.y_max = float(np.max(y_flat))

        x_norm = self._normalize_x(x_flat)
        Phi = self._build_basis(x_norm)

        reg_matrix = self.alpha * np.eye(Phi.shape[1])
        reg_matrix[0, 0] = 0.0
        self.weights = np.linalg.solve(Phi.T @ Phi + reg_matrix, Phi.T @ y_flat)
        return self

    def predict(self, x: np.ndarray) -> np.ndarray:
        if self.weights is None:
            raise RuntimeError("Regressor is not fitted yet. Call fit() first.")

        x_flat = np.asarray(x).ravel()
        x_norm = self._normalize_x(x_flat)
        Phi = self._build_basis(x_norm)

        raw = Phi @ self.weights
        y_range = max(1.0, self.y_max - self.y_min)
        return np.clip(raw, self.y_min - 0.5 * y_range, self.y_max + 0.5 * y_range)

    def evaluate(self, x: np.ndarray, y: np.ndarray) -> dict:
        y_true = np.asarray(y).ravel()
        y_pred = self.predict(x)

        ss_tot = np.sum((y_true - np.mean(y_true)) ** 2)
        ss_res = np.sum((y_true - y_pred) ** 2)

        r2 = 1.0 - (ss_res / (ss_tot + 1e-10))
        mse = float(np.mean((y_true - y_pred) ** 2))
        mae = float(np.mean(np.abs(y_true - y_pred)))

        return {"r2": float(r2), "mse": mse, "mae": mae}
