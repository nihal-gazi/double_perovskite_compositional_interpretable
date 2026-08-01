"""
src/log_target_hull_model.py
============================
Engine for Experiment 21:
Log-Transformed Target Stage 2 Regressor & High-C (C=300.0) Hard-Margin Classifier.
"""

import numpy as np
from sklearn.svm import SVC
from sklearn.linear_model import Ridge, LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error, accuracy_score, precision_score, recall_score, f1_score

class LogTargetHullModel:
    """
    Log-Target Convex Hull Model Manager for Exp 21.
    """

    def __init__(self, target_name: str):
        self.target_name = target_name
        self.scaler = StandardScaler()
        
        if "Formation Energy" in target_name:
            self.arch_type = "direct_multi_operator"
            self.reg_model = Ridge(alpha=1.0, random_state=42)
            self.cls_model = None
            self.use_log_target = False
        elif "Band Gap" in target_name:
            self.arch_type = "soft_gated_regressor"
            self.reg_model = Ridge(alpha=1.0, random_state=42)
            self.cls_model = SVC(kernel='rbf', C=50.0, class_weight='balanced', probability=True, random_state=42)
            self.use_log_target = False
        elif "Energy Above Hull" in target_name:
            self.arch_type = "log_target_hurdle"
            self.reg_model = Ridge(alpha=1.0, random_state=42)
            self.cls_model = SVC(kernel='rbf', C=300.0, class_weight='balanced', probability=True, random_state=42)
            self.use_log_target = True
        else: # Total Magnetization
            self.arch_type = "hard_margin_hurdle"
            self.reg_model = Ridge(alpha=1.0, random_state=42)
            self.cls_model = SVC(kernel='rbf', C=200.0, class_weight='balanced', probability=True, random_state=42)
            self.use_log_target = False

        self.best_tau = 0.5
        self.feature_names = None
        self.is_fitted = False

    def fit(self, X: np.ndarray, y: np.ndarray, threshold: float = None, feature_names: list = None):
        self.feature_names = feature_names
        X_scaled = self.scaler.fit_transform(X)

        if self.arch_type == "direct_multi_operator":
            self.reg_model.fit(X_scaled, y)
        elif self.arch_type == "soft_gated_regressor":
            y_bin = (y > threshold).astype(int)
            self.cls_model.fit(X_scaled, y_bin)

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

            nz_idx = y > threshold
            X_nz_scaled = X_scaled[nz_idx]
            y_nz = y[nz_idx]
            self.reg_model.fit(X_nz_scaled, y_nz)
        elif self.arch_type == "log_target_hurdle":
            y_bin = (y > threshold).astype(int)
            self.cls_model.fit(X_scaled, y_bin)

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

            nz_idx = y > threshold
            X_nz_scaled = X_scaled[nz_idx]
            y_nz = y[nz_idx]
            
            # Log-transform target for variance stabilization across near-hull metastable phases
            z_nz = np.log(y_nz + 1.0)
            self.reg_model.fit(X_nz_scaled, z_nz)
        else: # Hard-Margin Hurdle
            y_bin = (y > threshold).astype(int)
            self.cls_model.fit(X_scaled, y_bin)

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
        elif self.arch_type == "soft_gated_regressor":
            probs = self.cls_model.predict_proba(X_scaled)[:, 1]
            pred_nz = self.reg_model.predict(X_scaled)
            if not allow_negative:
                pred_nz = np.maximum(0.0, pred_nz)

            pipeline_preds = probs * pred_nz
            cls_metrics = {'best_tau': self.best_tau}
            return pipeline_preds, cls_metrics
        elif self.arch_type == "log_target_hurdle":
            probs = self.cls_model.predict_proba(X_scaled)[:, 1]
            pred_bin = (probs >= self.best_tau).astype(int)
            pred_z = self.reg_model.predict(X_scaled)
            
            # Inverse log-transform: y = exp(z) - 1.0
            pred_nz = np.exp(pred_z) - 1.0
            if not allow_negative:
                pred_nz = np.maximum(0.0, pred_nz)

            pipeline_preds = np.where(pred_bin == 0, 0.0, pred_nz)
            cls_metrics = {'best_tau': self.best_tau}
            return pipeline_preds, cls_metrics
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

        eq_str = "f(x) = " + "\n    ".join(terms)
        if self.use_log_target:
            return f"log({self.target_name} + 1.0) = \n    " + "\n    ".join(terms)
        return f"{self.target_name} = " + "\n    ".join(terms)
