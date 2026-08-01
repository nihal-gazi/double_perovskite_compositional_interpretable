"""
src/hybrid_model.py
===================
Physical Interaction & Polynomial-Linear Hybrid Model for Experiment 12.
Supports Ridge, Lasso, OLS, and Logistic Classification with interaction features.
"""

import numpy as np
from sklearn.linear_model import Ridge, Lasso, LinearRegression, LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error, accuracy_score, precision_score, recall_score, f1_score

class InteractionHybridModel:
    """
    Hybrid Regularized Polynomial-Linear Model supporting Ridge/Lasso feature selection.
    """

    def __init__(self, model_type: str = "ridge", alpha: float = 1.0):
        self.model_type = model_type.lower()
        self.alpha = alpha
        self.scaler = StandardScaler()
        
        if self.model_type == "lasso":
            self.reg_model = Lasso(alpha=alpha, max_iter=10000, random_state=42)
        elif self.model_type == "ridge":
            self.reg_model = Ridge(alpha=alpha, random_state=42)
        else:
            self.reg_model = LinearRegression()

        self.cls_model = LogisticRegression(max_iter=2000, random_state=42)
        self.feature_names = None
        self.is_fitted = False

    def fit_regressor(self, X: np.ndarray, y: np.ndarray, feature_names: list = None):
        self.feature_names = feature_names
        X_scaled = self.scaler.fit_transform(X)
        self.reg_model.fit(X_scaled, y)
        self.is_fitted = True

    def fit_classifier(self, X: np.ndarray, y_bin: np.ndarray, feature_names: list = None):
        self.feature_names = feature_names
        X_scaled = self.scaler.fit_transform(X)
        self.cls_model.fit(X_scaled, y_bin)

    def predict_regressor(self, X: np.ndarray) -> np.ndarray:
        X_scaled = self.scaler.transform(X)
        return self.reg_model.predict(X_scaled)

    def predict_classifier(self, X: np.ndarray) -> np.ndarray:
        X_scaled = self.scaler.transform(X)
        return self.cls_model.predict(X_scaled)

    def evaluate_regressor(self, X: np.ndarray, y: np.ndarray) -> dict:
        preds = self.predict_regressor(X)
        r2 = float(r2_score(y, preds))
        mse = float(mean_squared_error(y, preds))
        mae = float(mean_absolute_error(y, preds))
        return {'r2': r2, 'mse': mse, 'mae': mae, 'preds': preds}

    def evaluate_classifier(self, X: np.ndarray, y_bin: np.ndarray) -> dict:
        preds = self.predict_classifier(X)
        acc = float(accuracy_score(y_bin, preds))
        prec = float(precision_score(y_bin, preds, zero_division=0))
        rec = float(recall_score(y_bin, preds, zero_division=0))
        f1 = float(f1_score(y_bin, preds, zero_division=0))
        return {'accuracy': acc, 'precision': prec, 'recall': rec, 'f1': f1, 'preds': preds}

    def format_discovered_equation(self, target_name: str, top_k: int = 15) -> str:
        """
        Formats the top K most influential interaction & linear terms in unscaled feature space.
        """
        if not self.is_fitted:
            return "N/A"

        w_scaled = self.reg_model.coef_
        b_scaled = self.reg_model.intercept_
        mu = self.scaler.mean_
        std = self.scaler.scale_
        std = np.where(std < 1e-8, 1.0, std)

        w_unscaled = w_scaled / std
        b_unscaled = b_scaled - np.sum(w_scaled * mu / std)

        # Rank features by absolute magnitude of scaled coefficients
        top_indices = np.argsort(np.abs(w_scaled))[::-1][:top_k]

        terms = [f"{b_unscaled:+.6f}"]
        for idx in top_indices:
            coef = w_unscaled[idx]
            name = self.feature_names[idx]
            sign = "+" if coef >= 0 else "-"
            terms.append(f" {sign} {abs(coef):.6f} * {name}")

        return f"{target_name} = " + "\n    ".join(terms)
