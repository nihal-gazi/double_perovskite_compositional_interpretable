"""
src/interpretable_hurdle_model.py
==================================
100% Fully Interpretable Hurdle Model Engine for Experiment 14.
Stage 1: Analytical Regularized Log-Odds Classifier S_cls(x) > tau* with F1-Threshold Tuning.
Stage 2: Analytical Regularized Physical Interaction Regressor y_nz = c0 + sum(ci * Phi_i(x)).
"""

import numpy as np
from sklearn.linear_model import LogisticRegression, Ridge, Lasso, ElasticNet, LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error, accuracy_score, precision_score, recall_score, f1_score

class InterpretableHurdleModel:
    """
    100% Fully Interpretable Analytical Hurdle Model Engine.
    Stage 1: Analytical Regularized Log-Odds Classifier with Precision-Recall Threshold Tuning.
    Stage 2: Analytical Regularized Physical Interaction Regressor.
    """

    def __init__(self, reg_model_type: str = "elasticnet", alpha: float = 0.5, l1_ratio: float = 0.5):
        self.reg_model_type = reg_model_type.lower()
        self.alpha = alpha
        self.l1_ratio = l1_ratio
        self.scaler = StandardScaler()
        
        # Stage 2 Analytical Regressor
        if self.reg_model_type == "lasso":
            self.reg_model = Lasso(alpha=alpha, max_iter=10000, random_state=42)
        elif self.reg_model_type == "elasticnet":
            self.reg_model = ElasticNet(alpha=alpha, l1_ratio=l1_ratio, max_iter=10000, random_state=42)
        elif self.reg_model_type == "ridge":
            self.reg_model = Ridge(alpha=alpha, random_state=42)
        else:
            self.reg_model = LinearRegression()

        # Stage 1 Analytical Log-Odds Classifier
        self.cls_model = LogisticRegression(penalty='l2', C=2.0, max_iter=2000, random_state=42)
        self.best_tau = 0.5
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

        # Optimize Threshold tau* on Precision-Recall F1 Space
        probs = self.cls_model.predict_proba(X_scaled)[:, 1]
        best_f1 = -1.0
        best_t = 0.5

        for t in np.linspace(0.1, 0.9, 81):
            preds_t = (probs >= t).astype(int)
            f1_t = f1_score(y_bin, preds_t, zero_division=0)
            if f1_t > best_f1:
                best_f1 = f1_t
                best_t = t

        self.best_tau = float(best_t)

    def predict_regressor(self, X: np.ndarray) -> np.ndarray:
        X_scaled = self.scaler.transform(X)
        return self.reg_model.predict(X_scaled)

    def predict_classifier(self, X: np.ndarray) -> np.ndarray:
        X_scaled = self.scaler.transform(X)
        probs = self.cls_model.predict_proba(X_scaled)[:, 1]
        return (probs >= self.best_tau).astype(int)

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
        return {'accuracy': acc, 'precision': prec, 'recall': rec, 'f1': f1, 'preds': preds, 'best_tau': self.best_tau}

    def format_stage1_equation(self, target_name: str, top_k: int = 10) -> str:
        """
        Formats Stage 1 Analytical Decision Boundary Formula S_cls(x) > tau*.
        """
        w_scaled = self.cls_model.coef_[0]
        b_scaled = self.cls_model.intercept_[0]
        mu = self.scaler.mean_
        std = self.scaler.scale_
        std = np.where(std < 1e-8, 1.0, std)

        w_unscaled = w_scaled / std
        b_unscaled = b_scaled - np.sum(w_scaled * mu / std)

        top_indices = np.argsort(np.abs(w_scaled))[::-1][:top_k]

        terms = [f"{b_unscaled:+.6f}"]
        for idx in top_indices:
            coef = w_unscaled[idx]
            name = self.feature_names[idx]
            sign = "+" if coef >= 0 else "-"
            terms.append(f" {sign} {abs(coef):.6f} * {name}")

        formula_str = f"S_cls(x) = " + "\n    ".join(terms)
        rule_str = f"Predict Active Non-Zero ({target_name} > 0) IF S_cls(x) > {self.best_tau:.4f}"
        return formula_str + "\n\n" + rule_str

    def format_stage2_equation(self, target_name: str, top_k: int = 15) -> str:
        """
        Formats Stage 2 Analytical Magnitude Equation y_nz = c0 + sum(ci * Phi_i(x)).
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

        top_indices = np.argsort(np.abs(w_scaled))[::-1][:top_k]

        terms = [f"{b_unscaled:+.6f}"]
        for idx in top_indices:
            coef = w_unscaled[idx]
            name = self.feature_names[idx]
            sign = "+" if coef >= 0 else "-"
            terms.append(f" {sign} {abs(coef):.6f} * {name}")

        return f"{target_name} = " + "\n    ".join(terms)
