# Data Source & Provenance Citation: Materials Project 5,000 Double Perovskite Dataset

**Location:** `exp_v2/data/data_28_7_2026/citation.md`  
**Date:** July 28, 2026  
**Source Database:** The Materials Project API (v2 / v3)  
**API Endpoint:** `https://api.materialsproject.org/v2/summary/`  
**Dataset File:** `exp_v2/data/data_28_7_2026/double_perovskite_dataset_5000.csv`  

---

## 1. Citation Reference

### [MaterialsProject_2013]
* **Authors**: Anubhav Jain, Shyue Ping Ong, Geoffroy Hautier, Wei Chen, William Davidson Richards, Stephen Dacek, Shreyas Cholia, Dan Gunter, David Skinner, Gerbrand Ceder, and Kristin A. Persson
* **Title**: *Commentary: The Materials Project: A materials genome approach to accelerating materials innovation*
* **Journal**: *APL Materials*, Vol. 1, Issue 1, 011002 (2013)
* **DOI**: [10.1063/1.4812323](https://doi.org/10.1063/1.4812323)
* **URL**: [https://materialsproject.org](https://materialsproject.org)

---

## 2. Dataset Query Criteria

- **Target Formula Pattern**: Oxide Perovskites ($A_2 B B' O_6$ or $A A' B B' O_6$)
- **Elements Included**: Oxygen ($O$) + 4 site cations ($A, A', B, B'$)
- **Properties Retrieved**:
  1. `material_id`: Materials Project Identifier (e.g. `mp-12345`)
  2. `formula_pretty`: Reduced Chemical Formula
  3. `Formation_Energy_eV_atom`: DFT PBE formation energy in eV/atom
  4. `Total_Magnetization_uB`: Total net magnetic moment in $\mu_B$/formula unit
  5. `Band_Gap_eV`: Fundamental electronic band gap in eV
  6. `Energy_Above_Hull_eV`: Thermodynamic energy above hull in eV/atom
- **Total Records Extracted**: 5,000 double perovskite materials
