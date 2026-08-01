# Multi-Seed 80/20 Train-Test Evaluation Methodology (5,000 Dataset)

## 1. Executive Summary

This document specifies the formal methodology for evaluating the Master Capstone Double Perovskite Machine Learning Algorithm (`exp_v2/research/algorithm/`) on the **5,000 double perovskite dataset** (`exp_v2/data/data_28_7_2026/double_perovskite_dataset_5000.csv`) using a rigorous **25-Seed 80/20 Train-Test Benchmark Protocol**.

To guarantee bulletproof statistical validity, eliminate random partition bias, and prove model transferability, the Master Model is evaluated across **25 distinct random seeds**:
`SEEDS = [42, 100, 2026, 777, 999, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120]`

---

## 2. Multi-Seed Protocol & Workflow

For each random seed $S_i \in \text{SEEDS}$:

1. **Dataset Partitioning (80/20 Split)**:
   - Total dataset: 5,000 double perovskite compounds ($A_2 B B' O_6$).
   - Training Set (80%): 4,000 materials sampled with `random_state = S_i`.
   - Held-Out Test Set (20%): 1,000 materials.

2. **Feature Generation**:
   - Master 98 0D compositional descriptors generated independently for both train and test splits using `generate_algorithm_features` (Harrison Tight-Binding Gap, Single-Perovskite Tie-Lines, Closed-Shell Crystal Field, Birch-Murnaghan Strain).

3. **In-Distribution Training (80% Train Set - 4,000 Materials)**:
   - Master Algorithm fits decision boundaries and physical equation weights on the 4,000 training materials.
   - Record in-distribution training set performance metrics.

4. **Out-of-Sample Testing (20% Test Set - 1,000 Materials)**:
   - Fitted physical equations and Stage 1 classifiers evaluate the 1,000 unseen test materials in zero-shot inference mode.
   - Record held-out test set performance metrics.

5. **Statistical Compilation ($\mu \pm \sigma$)**:
   - Calculate the mean ($\mu$) and standard deviation ($\sigma$) across all 25 random seeds for every metric:
     - Stage 1 Classification Accuracy (%) & F1-score
     - Stage 2 Non-Zero Sub $R^2$ (%)
     - Final Pipeline $R^2$ (%)
     - Mean Squared Error (MSE)
     - Mean Absolute Error (MAE)
     - Relative Theoretical Physical Limit Achieved (%)

---

## 3. Data Leakage & 3D Audit

- **Compositional Compliance**: 100% 0D pure compositional inputs derived strictly from stoichiometry $A_2 B B' O_6$.
- **Zero 3D Atomic Coordinates**: No DFT relaxed crystal structures, cell vectors, or atomic positions used.
- **Zero GNN Surrogates**: No graph neural network pre-trainings or leaked structural embeddings.
