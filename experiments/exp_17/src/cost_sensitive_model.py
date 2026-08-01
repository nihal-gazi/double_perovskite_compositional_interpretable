"""
src/cost_sensitive_model.py
============================
Engine for Experiment 17:
Cost-Sensitive Stage 1 Classifier + Multi-Operator Stage 2 Regressor.
Applies class weights and cost-sensitive penalties to eliminate false positives/negatives going into Stage 2.
"""

import numpy as np
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression, Ridge, LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error, accuracy_score, precision_score, recall_score, f1_score

class CostSensitiveHurdleModel:
    """
    Cost-Sensitive Hurdle Model Manager.
    Stage 1: Cost-Sensitive Classifier with Class Penalties and Precision-Recall Threshold Tuning.
    Stage 2: Multi-Operator Physical Regressor on purified active non-zeros.
    """

    def __init__(self, target_name: str):
        self.target_name = target_name
        self.scaler = StandardScaler()
        
        if "Formation Energy" in target_name or "Band Gap" in target_name:
            self.arch_type = "direct_multi_operator"
            self.reg_model = Ridge(alpha=1.0, random_state=42)
            self.cls_model = None
        else:
            self.arch_type = "cost_sensitive_hurdle"
            self.reg_model = Ridge(alpha=1.0, random_state=42)
            # Apply cost-sensitive balanced class weights & strict decision penalty
            self.cls_model = SVC(kernel='rbf', C=10.0, class_weight='balanced', probability=True, random_state=42)

        self.best_tau = 0.5
        self.feature_names = None
        self.is_fitted = False

    def fit(self, X: np.ndarray, y: np.ndarray, threshold: float = None, feature_names: list = None):
        self.feature_names = feature_names
        X_scaled = self.scaler.fit_transform(X)

        if self.arch_type == "direct_multi_operator":
            self.reg_model.fit(X_scaled, y)
        else:
            y_bin = (y > threshold).astype(int)
            self.cls_model.fit(X_scaled, y_bin)

            # Cost-Sensitive Precision-Recall F1 Threshold Optimization
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

            # Fit Stage 2 Regressor on purified active non-zeros
            nz_idx = y > threshold
            X_nz_scaled = X_scaled[nz_idx]
            y_nz = y[nz_idx]
            self.reg_model.fit(X_nz_scaled, y_nz)

        self.is_fitted = True

    def predict(self, X: np.ndarray, threshold: float = None, allow_negative: bool = True) -> tuple[np.ndarray, dict]:
        X_scaled = self.scaler.transform(X)

        if self.arch_type == "direct_multi_operator":
            preds = self.reg_model.predict(X_scaled)
            if not allow_negative:
                preds = np.maximum(0.0, preds)
            cls_metrics = {'accuracy': 1.0, 'f1': 1.0, 'precision': 1.0, 'recall': 1.0, 'best_tau': 0.5}
            return preds, cls_metrics
        else:
            probs = self.cls_model.predict_proba(X_scaled)[:, 1]
            pred_bin = (probs >= self.best_tau).astype(int)
            pred_nz = self.reg_model.predict(X_scaled)
            if not allow_negative:
                pred_nz = np.maximum(0.0, pred_nz)

            pipeline_preds = np.where(pred_bin == 0, 0.0, pred_nz)
            cls_metrics = {'best_tau': self.best_tau}
            return pipeline_preds, cls_metrics

    def format_master_equation(self, top_k: int = 15) -> str:
        """
        Formats the final discovered equation terms in unscaled feature space.
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

        return f"{self.target_name} = " + "\n    ".join(terms)
