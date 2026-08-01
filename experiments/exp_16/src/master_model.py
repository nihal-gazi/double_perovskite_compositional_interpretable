"""
src/master_model.py
===================
Master Target-Specific Model Engine for Experiment 16.
Selects the optimal architecture per property:
1. Formation Energy (ΔEf): Direct Multi-Operator Analytical Formula
2. Band Gap (Eg): Direct Multi-Operator Analytical Formula
3. Total Magnetization (M): Non-Linear Decision Boundary Hurdle Model
4. Energy Above Hull (E_hull): Non-Linear Decision Boundary Hurdle Model
"""

import numpy as np
from sklearn.svm import SVC
from sklearn.linear_model import Ridge, LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error, accuracy_score, precision_score, recall_score, f1_score

class MasterOptimalModel:
    """
    Target-Specific Master Model Manager.
    """

    def __init__(self, target_name: str):
        self.target_name = target_name
        self.scaler = StandardScaler()
        
        # Determine model architecture by target property
        if "Formation Energy" in target_name or "Band Gap" in target_name:
            self.arch_type = "direct_multi_operator"
            self.reg_model = Ridge(alpha=1.0, random_state=42)
            self.cls_model = None
        else:
            self.arch_type = "nonlinear_hurdle"
            self.reg_model = Ridge(alpha=1.0, random_state=42)
            self.cls_model = SVC(kernel='rbf', C=5.0, gamma='scale', probability=True, random_state=42)

        self.feature_names = None
        self.is_fitted = False

    def fit(self, X: np.ndarray, y: np.ndarray, threshold: float = None, feature_names: list = None):
        self.feature_names = feature_names
        X_scaled = self.scaler.fit_transform(X)

        if self.arch_type == "direct_multi_operator":
            self.reg_model.fit(X_scaled, y)
        else:
            # Fit Stage 1 Classifier
            y_bin = (y > threshold).astype(int)
            self.cls_model.fit(X_scaled, y_bin)

            # Fit Stage 2 Regressor on active non-zeros
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
            cls_metrics = {'accuracy': 1.0, 'f1': 1.0, 'precision': 1.0, 'recall': 1.0}
            return preds, cls_metrics
        else:
            pred_bin = self.cls_model.predict(X_scaled)
            pred_nz = self.reg_model.predict(X_scaled)
            if not allow_negative:
                pred_nz = np.maximum(0.0, pred_nz)

            pipeline_preds = np.where(pred_bin == 0, 0.0, pred_nz)
            cls_metrics = {}
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
