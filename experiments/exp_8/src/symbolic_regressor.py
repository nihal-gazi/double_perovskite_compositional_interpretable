"""
src/symbolic_regressor.py
=========================
Stage 2 Symbolic Non-Zero Regressor using Genetic Programming (gplearn).
Evaluated on active non-zero samples and includes protected 'pow' operator.
"""

import numpy as np
from sklearn.utils.validation import check_X_y, check_array
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from gplearn.genetic import BaseSymbolic, SymbolicRegressor as GPLearnSymbolicRegressor
from gplearn.functions import make_function

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

def _protected_pow(x1, x2):
    """
    Protected Power Operator: pow(x1, x2) = |x1|^clip(x2, -5, 5)
    Safely prevents NaN, overflow, or complex numbers.
    """
    with np.errstate(all='ignore'):
        abs_x1 = np.abs(x1)
        abs_x1 = np.where(abs_x1 < 1e-6, 1e-6, abs_x1)
        x2_clip = np.clip(x2, -5.0, 5.0)
        res = np.power(abs_x1, x2_clip)
        return np.nan_to_num(res, nan=1.0, posinf=1e6, neginf=-1e6)

pow_primitive = make_function(function=_protected_pow, name='pow', arity=2)

class SymbolicNonZeroRegressor:
    """
    Genetic Programming Symbolic Regressor for active non-zero targets.
    Includes protected 'pow' operator.
    """

    def __init__(
        self,
        population_size: int = 2000,
        generations: int = 25,
        random_state: int = 42,
        parsimony_coefficient: float = 0.001
    ):
        self.population_size = population_size
        self.generations = generations
        self.random_state = random_state
        self.parsimony_coefficient = parsimony_coefficient
        self.model = None
        self.program_str = ""

    def fit(self, X_nz: np.ndarray, y_nz: np.ndarray, feature_names: list = None):
        function_set = ['add', 'sub', 'mul', 'div', 'neg', 'abs', 'log', pow_primitive]

        self.model = GPLearnSymbolicRegressor(
            population_size=self.population_size,
            generations=self.generations,
            metric='mean absolute error',
            function_set=function_set,
            parsimony_coefficient=self.parsimony_coefficient,
            random_state=self.random_state,
            n_jobs=-1,
            feature_names=feature_names,
            verbose=0
        )
        self.model.fit(X_nz, y_nz)
        self.program_str = str(self.model._program)
        return self

    def predict(self, X: np.ndarray) -> np.ndarray:
        if self.model is None:
            raise ValueError("Model has not been fitted yet.")
        raw = self.model.predict(X)
        return np.nan_to_num(raw, nan=0.0, posinf=1e6, neginf=-1e6)

    def evaluate(self, X_nz: np.ndarray, y_nz: np.ndarray) -> dict:
        preds = self.predict(X_nz)
        r2 = float(r2_score(y_nz, preds))
        mse = float(mean_squared_error(y_nz, preds))
        mae = float(mean_absolute_error(y_nz, preds))

        return {
            'r2': r2,
            'mse': mse,
            'mae': mae,
            'program': self.program_str
        }
