# ood_test_2 Evaluation Methodology (2,000 Dataset)

## 1. Executive Summary

This document specifies the methodology for **ood_test_2**, evaluating the Master Capstone Double Perovskite Machine Learning Algorithm (`exp_v2/research/algorithm/`) strictly on the original **2,000 double perovskites dataset** (`exp_v2/data/data_24_7_2026/double_perovskite_dataset.csv`) using a rigorous **80/20 Train-Test Split protocol**.

---

## 2. Experimental Protocol

1. **Dataset Partitioning (80/20 Split)**:
   - Total dataset: 2,000 double perovskites ($A_2 B B' O_6$).
   - Training Set (80%): 1,600 materials sampled with `seed = 42`.
   - Held-Out Test Set (20%): 400 materials.

2. **Feature Generation**:
   - Master 98 0D compositional descriptors generated independently for both splits using `generate_algorithm_features`.

3. **In-Distribution Training (80% Train Set - 1,600 Materials)**:
   - Master Algorithm fits decision boundaries and physical equation weights on the 1,600 training materials.
   - Record in-distribution training set performance metrics.

4. **Out-of-Sample Testing (20% Test Set - 400 Materials)**:
   - Fitted physical equations and Stage 1 classifiers evaluate the 400 unseen test materials in zero-shot inference mode.
   - Record held-out test set performance metrics.

5. **Evaluated Metrics**:
   - Stage 1 Classification Accuracy (%) & F1-score
   - Stage 2 Non-Zero Sub $R^2$ (%)
   - Final Pipeline $R^2$ (%)
   - MSE & MAE
   - Relative Theoretical Physical Limit Achieved (%)
