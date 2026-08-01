"""
src/symbolic_classifier.py
===========================
Short Symbolic Regression Decision Boundary Classifier using gplearn
with custom +1/-1 classification fitness scoring metric and 19 extended mathematical operators.
"""

import numpy as np
from sklearn.utils.validation import check_X_y, check_array
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from gplearn.genetic import BaseSymbolic, SymbolicRegressor
from gplearn.fitness import make_fitness
from .primitives import EXTENDED_FUNCTION_SET

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

def _classification_score(y_true, y_pred, sample_weight=None):
    """
    Custom Fitness Score:
    +1 for every correct classification (pred > 0 <=> y == 1)
    -1 for every wrong classification
    """
    pred_bin = (y_pred > 0.0).astype(int)
    score = np.where(pred_bin == y_true, 1.0, -1.0)
    return float(np.sum(score))

custom_classification_fitness = make_fitness(
    function=_classification_score,
    greater_is_better=True
)

class SymbolicBoundaryClassifier:
    """
    Symbolic Regression Classifier finding an analytical decision boundary S(x) = 0:
        S(x) > 0  => Class 1 (Non-Zero)
        S(x) <= 0 => Class 0 (Zero)
    Uses 19 extended mathematical operators.
    """
    def __init__(
        self,
        population_size: int = 1500,
        generations: int = 15,
        random_state: int = 42
    ):
        self.population_size = population_size
        self.generations = generations
        self.random_state = random_state
        self.model = None
        self.feature_names = None
        self.program_str = ""

    def fit(self, X: np.ndarray, y_bin: np.ndarray, feature_names: list = None):
        self.feature_names = feature_names

        self.model = SymbolicRegressor(
            population_size=self.population_size,
            generations=self.generations,
            metric=custom_classification_fitness,
            function_set=EXTENDED_FUNCTION_SET,
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

        self.model.fit(X, y_bin)
        self.program_str = str(self.model._program)
        return self

    def predict_raw(self, X: np.ndarray) -> np.ndarray:
        if self.model is None:
            raise RuntimeError("SymbolicBoundaryClassifier is not fitted yet. Call fit() first.")
        raw = self.model.predict(X)
        return np.nan_to_num(raw, nan=-1.0, posinf=1.0, neginf=-1.0)

    def predict(self, X: np.ndarray) -> np.ndarray:
        raw_preds = self.predict_raw(X)
        return (raw_preds > 0.0).astype(int)

    def evaluate(self, X: np.ndarray, y_bin: np.ndarray) -> dict:
        y_true = np.asarray(y_bin).ravel()
        pred_bin = self.predict(X)

        acc = float(accuracy_score(y_true, pred_bin))
        prec = float(precision_score(y_true, pred_bin, zero_division=0))
        rec = float(recall_score(y_true, pred_bin, zero_division=0))
        f1 = float(f1_score(y_true, pred_bin, zero_division=0))

        return {
            "accuracy": acc,
            "precision": prec,
            "recall": rec,
            "f1": f1,
            "program": self.program_str
        }
