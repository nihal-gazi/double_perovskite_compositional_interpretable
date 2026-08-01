"""
src/symbolic_regressor.py
=========================
Standard Symbolic Regressor for Stage 2 non-zero property magnitude prediction using gplearn.
"""

import numpy as np
from sklearn.utils.validation import check_X_y, check_array
from gplearn.genetic import BaseSymbolic, SymbolicRegressor

# Patch sklearn _validate_data compatibility for gplearn in newer sklearn versions
if not hasattr(BaseSymbolic, '_validate_data'):
    def _validate_data(self, X, y=None, **kwargs):
        if y is not None:
            X_out, y_out = check_X_y(X, y)
            self.n_features_in_ = X_out.shape[1]
            return X_out, y_out
        else:
            X_out = check_array(X)
            self.n_features_in_ = X_out.shape[1]
            return X_out
    BaseSymbolic._validate_data = _validate_data

class SymbolicNonZeroRegressor:
    """
    Symbolic Regressor for continuous non-zero target property prediction:
        S_reg(x) = analytical expression

    Parameters
    ----------
    population_size : int
        Number of GP candidate programs per generation (default: 2000).
    generations : int
        Number of evolution generations (default: 25).
    random_state : int
        Random seed for reproducibility (default: 42).
    """
    def __init__(
        self,
        population_size: int = 2000,
        generations: int = 25,
        random_state: int = 42
    ):
        self.population_size = population_size
        self.generations = generations
        self.random_state = random_state
        self.model = None
        self.feature_names = None
        self.program_str = ""

    def fit(self, X: np.ndarray, y: np.ndarray, feature_names: list = None):
        self.feature_names = feature_names

        self.model = SymbolicRegressor(
            population_size=self.population_size,
            generations=self.generations,
            metric='mean absolute error',
            function_set=('add', 'sub', 'mul', 'div', 'neg', 'abs', 'log'),
            parsimony_coefficient=0.005,
            p_crossover=0.7,
            p_subtree_mutation=0.1,
            p_hoist_mutation=0.05,
            p_point_mutation=0.1,
            max_samples=0.9,
            feature_names=feature_names,
            random_state=self.random_state,
            n_jobs=-1,
            verbose=0
        )

        self.model.fit(X, y)
        self.program_str = str(self.model._program)
        return self

    def predict(self, X: np.ndarray) -> np.ndarray:
        if self.model is None:
            raise RuntimeError("SymbolicNonZeroRegressor is not fitted yet. Call fit() first.")
        raw = self.model.predict(X)
        return np.nan_to_num(raw, nan=0.0, posinf=1e6, neginf=-1e6)

    def evaluate(self, X: np.ndarray, y: np.ndarray) -> dict:
        y_true = np.asarray(y).ravel()
        y_pred = self.predict(X)

        ss_tot = np.sum((y_true - np.mean(y_true)) ** 2)
        ss_res = np.sum((y_true - y_pred) ** 2)

        r2 = 1.0 - (ss_res / (ss_tot + 1e-10))
        mse = float(np.mean((y_true - y_pred) ** 2))
        mae = float(np.mean(np.abs(y_true - y_pred)))

        return {
            "r2": float(r2),
            "mse": mse,
            "mae": mae,
            "program": self.program_str
        }
