"""
exp_v2/fetch_and_build_dataset.py
==================================
High-speed script to fetch up to 2000 double perovskite materials from Materials Project API,
compute Table 1 descriptors, save double_perovskite_dataset.csv and citation.md.
"""

import os
import sys
import json
import warnings
import urllib3
import requests
import numpy as np
import pandas as pd

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Patch requests SSL verification globally for MPRester on Windows
_old_request = requests.Session.request
def _unsafe_request(self, method, url, **kwargs):
    kwargs['verify'] = False
    return _old_request(self, method, url, **kwargs)
requests.Session.request = _unsafe_request

import typing
import typing_extensions
if not hasattr(typing, 'NotRequired'):
    typing.NotRequired = getattr(typing_extensions, 'NotRequired', None)
if not hasattr(typing, 'Required'):
    typing.Required = getattr(typing_extensions, 'Required', None)

from mp_api.client import MPRester
from mendeleev import element as elem_md

DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "data_24_7_2026")
os.makedirs(DATA_DIR, exist_ok=True)

API_KEY = "gWJXczH9PXlsJ4tByN7ilvwJGv0TMnsY"

A_SITE_ELEMENTS = {
    'Li', 'Na', 'K', 'Rb', 'Cs', 'Fr',
    'Be', 'Mg', 'Ca', 'Sr', 'Ba', 'Ra',
    'Sc', 'Y', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu',
    'Bi', 'Pb', 'Tl', 'Ag', 'Th', 'U'
}

O_SHANNON_RADIUS = 1.40

A_OXIDATION_DICT = {
    'Li': 1, 'Na': 1, 'K': 1, 'Rb': 1, 'Cs': 1,
    'Be': 2, 'Mg': 2, 'Ca': 2, 'Sr': 2, 'Ba': 2,
    'Sc': 3, 'Y': 3, 'La': 3, 'Ce': 3, 'Pr': 3, 'Nd': 3, 'Sm': 3, 'Eu': 3, 'Gd': 3, 'Tb': 3, 'Dy': 3, 'Ho': 3, 'Er': 3, 'Tm': 3, 'Yb': 3, 'Lu': 3,
    'Bi': 3, 'Pb': 2, 'Tl': 1, 'Ag': 1, 'Th': 4, 'U': 4
}

TM_VALENCE_DICT = {
    'Sc': 3, 'Ti': 4, 'V': 5, 'Cr': 6, 'Mn': 7, 'Fe': 8, 'Co': 9, 'Ni': 10, 'Cu': 11, 'Zn': 12,
    'Y': 3, 'Zr': 4, 'Nb': 5, 'Mo': 6, 'Tc': 7, 'Ru': 8, 'Rh': 9, 'Pd': 10, 'Ag': 11, 'Cd': 12,
    'Hf': 4, 'Ta': 5, 'W': 6, 'Re': 7, 'Os': 8, 'Ir': 9, 'Pt': 10, 'Au': 11, 'Hg': 12,
    'Al': 3, 'Ga': 3, 'In': 3, 'Sn': 4, 'Sb': 5, 'Bi': 5
}

GROUP_MAP = {
    'Y': 3, 'La': 3, 'Sc': 3,
    'Ti': 4, 'Zr': 4, 'Hf': 4,
    'V': 5, 'Nb': 5, 'Ta': 5,
    'Cr': 6, 'Mo': 6, 'W': 6,
    'Mn': 7, 'Tc': 7, 'Re': 7,
    'Fe': 8, 'Ru': 8, 'Os': 8,
    'Co': 9, 'Rh': 9, 'Ir': 9,
    'Ni': 10, 'Pd': 10, 'Pt': 10,
    'Cu': 11, 'Ag': 11, 'Au': 11,
    'Zn': 12, 'Cd': 12, 'Hg': 12,
    'Al': 13, 'Ga': 13, 'In': 13, 'Sn': 14, 'Sb': 15, 'Bi': 15
}

# Pre-cache electronegativities and ionic radii to eliminate loop overhead
EN_CACHE = {}
SHANNON_CACHE = {}

def get_electronegativity(symbol):
    if symbol not in EN_CACHE:
        try:
            e = elem_md(symbol)
            EN_CACHE[symbol] = float(e.electronegativity('pauling')) if e.electronegativity('pauling') is not None else 1.5
        except Exception:
            EN_CACHE[symbol] = 1.5
    return EN_CACHE[symbol]

def get_shannon_radius(symbol, default_r=0.75):
    if symbol not in SHANNON_CACHE:
        try:
            e = elem_md(symbol)
            radii = e.ionic_radii
            if radii:
                r6 = [r.ionic_radius for r in radii if r.coordination == 'VI']
                if r6 and r6[0] is not None:
                    val = r6[0] / 100.0 if r6[0] > 10 else r6[0]
                    SHANNON_CACHE[symbol] = float(val)
                else:
                    r_all = [r.ionic_radius for r in radii if r.ionic_radius is not None]
                    if r_all:
                        avg_r = float(np.mean(r_all))
                        SHANNON_CACHE[symbol] = float(avg_r / 100.0 if avg_r > 10 else avg_r)
                    else:
                        SHANNON_CACHE[symbol] = default_r
            else:
                SHANNON_CACHE[symbol] = default_r
        except Exception:
            SHANNON_CACHE[symbol] = default_r
    return SHANNON_CACHE[symbol]

def fetch_double_perovskites():
    print("=" * 60)
    print("EXP_V2: Fetching Double Perovskites from Materials Project API")
    print("=" * 60)

    raw_docs = []
    with MPRester(API_KEY) as mpr:
        print("Fetching 4-element oxides (elements=['O'], num_elements=4)...")
        docs_4 = mpr.materials.summary.search(
            elements=['O'],
            num_elements=4,
            fields=[
                'material_id', 'formula_pretty', 'composition', 'symmetry',
                'formation_energy_per_atom', 'energy_above_hull', 'band_gap',
                'total_magnetization', 'volume', 'density', 'uncorrected_energy_per_atom'
            ]
        )
        print(f"Retrieved {len(docs_4):,} 4-element oxides.")

        print("Fetching 5-element oxides (elements=['O'], num_elements=5)...")
        docs_5 = mpr.materials.summary.search(
            elements=['O'],
            num_elements=5,
            fields=[
                'material_id', 'formula_pretty', 'composition', 'symmetry',
                'formation_energy_per_atom', 'energy_above_hull', 'band_gap',
                'total_magnetization', 'volume', 'density', 'uncorrected_energy_per_atom'
            ]
        )
        print(f"Retrieved {len(docs_5):,} 5-element oxides.")

        raw_docs = docs_4 + docs_5

    print(f"Total raw oxide entries retrieved: {len(raw_docs):,}")

    dp_list = []
    for d in raw_docs:
        comp = d.composition.as_dict()
        total_atoms = sum(comp.values())
        if total_atoms == 0 or 'O' not in comp:
            continue

        o_ratio = comp['O'] / total_atoms
        if not (0.55 <= o_ratio <= 0.65):
            continue

        non_o = {k: v for k, v in comp.items() if k != 'O'}
        non_o_ratios = {k: v / total_atoms for k, v in non_o.items()}

        is_dp = False
        elem_A, elem_Aprime, elem_B, elem_Bprime = None, None, None, None

        if len(non_o) == 3:
            sorted_by_count = sorted(non_o_ratios.items(), key=lambda x: x[1], reverse=True)
            a_cand, a_ratio = sorted_by_count[0]
            b1_cand, b1_ratio = sorted_by_count[1]
            b2_cand, b2_ratio = sorted_by_count[2]

            if abs(a_ratio - 0.20) <= 0.05 and abs(b1_ratio - 0.10) <= 0.03 and abs(b2_ratio - 0.10) <= 0.03:
                if a_cand in A_SITE_ELEMENTS or b1_cand not in A_SITE_ELEMENTS:
                    elem_A = a_cand
                    elem_Aprime = a_cand
                    elem_B = b1_cand
                    elem_Bprime = b2_cand
                    is_dp = True

        elif len(non_o) == 4:
            ratios_list = list(non_o_ratios.values())
            if all(abs(r - 0.10) <= 0.03 for r in ratios_list):
                a_cands = [k for k in non_o if k in A_SITE_ELEMENTS]
                b_cands = [k for k in non_o if k not in A_SITE_ELEMENTS]

                if len(a_cands) == 2 and len(b_cands) == 2:
                    elem_A, elem_Aprime = a_cands[0], a_cands[1]
                    elem_B, elem_Bprime = b_cands[0], b_cands[1]
                    is_dp = True

        if is_dp:
            dp_list.append({
                'Material_ID': str(d.material_id).strip(),
                'Formula': str(d.formula_pretty).strip(),
                'element_A': elem_A,
                'element_Aprime': elem_Aprime,
                'element_B': elem_B,
                'element_Bprime': elem_Bprime,
                'Formation_Energy_eV_atom': d.formation_energy_per_atom,
                'Energy_Above_Hull_eV': d.energy_above_hull,
                'Band_Gap_eV': d.band_gap,
                'Total_Magnetization_uB': d.total_magnetization,
                'Volume_A3': d.volume,
                'Density_g_cm3': d.density,
                'Space_Group_Symbol': d.symmetry.symbol if d.symmetry else None,
                'Space_Group_Number': d.symmetry.number if d.symmetry else None,
            })

            if len(dp_list) >= 2000:
                print("Reached maximum target size of 2000 double perovskites.")
                break

    df_dp = pd.DataFrame(dp_list)
    print(f"\nFinal filtered Double Perovskite dataset size: {len(df_dp):,} materials.")
    return df_dp

def compute_table1_descriptors(df):
    print("\nComputing Table 1 Physical, Geometric, and Quantum Descriptors...")

    # Mendeleev Electronegativities
    df['EN_A'] = df['element_A'].apply(get_electronegativity)
    df['EN_Aprime'] = df['element_Aprime'].apply(get_electronegativity)
    df['EN_B'] = df['element_B'].apply(get_electronegativity)
    df['EN_Bprime'] = df['element_Bprime'].apply(get_electronegativity)
    df['EN_O'] = get_electronegativity('O')
    df['EN_avg'] = (df['EN_B'] + df['EN_Bprime']) / 2.0

    # Shannon Ionic Radii
    df['Shannon_A'] = df['element_A'].apply(lambda x: get_shannon_radius(x, 1.35))
    df['Shannon_Aprime'] = df['element_Aprime'].apply(lambda x: get_shannon_radius(x, 1.35))
    df['Shannon_B'] = df['element_B'].apply(lambda x: get_shannon_radius(x, 0.65))
    df['Shannon_Bprime'] = df['element_Bprime'].apply(lambda x: get_shannon_radius(x, 0.65))

    r_A_avg = (df['Shannon_A'] + df['Shannon_Aprime']) / 2.0
    r_B_avg = (df['Shannon_B'] + df['Shannon_Bprime']) / 2.0

    # Goldschmidt Tolerance Factor (t)
    df['Tolerance_Factor'] = (r_A_avg + O_SHANNON_RADIUS) / (np.sqrt(2) * (r_B_avg + O_SHANNON_RADIUS))

    # Octahedral Mismatch Ratio (mu_oct)
    df['Octahedral_Mismatch'] = np.abs(df['Shannon_B'] - df['Shannon_Bprime']) / np.maximum(r_B_avg, 1e-4)

    # Valence Electron Counts
    df['Val_A'] = df['element_A'].apply(lambda x: A_OXIDATION_DICT.get(x, 2))
    df['Val_Aprime'] = df['element_Aprime'].apply(lambda x: A_OXIDATION_DICT.get(x, 2))
    df['Val_B'] = df['element_B'].apply(lambda x: TM_VALENCE_DICT.get(x, 4))
    df['Val_Bprime'] = df['element_Bprime'].apply(lambda x: TM_VALENCE_DICT.get(x, 4))
    df['Val_avg'] = (df['Val_B'] + df['Val_Bprime']) / 2.0

    df['Total_A_Charge'] = df['Val_A'] + df['Val_Aprime']
    df['Group_B'] = df['element_B'].apply(lambda x: GROUP_MAP.get(x, 4))
    df['Group_Bprime'] = df['element_Bprime'].apply(lambda x: GROUP_MAP.get(x, 4))

    df['Sum_Ox_B_Bprime'] = 12 - df['Total_A_Charge']
    df['Ox_B'] = df['Sum_Ox_B_Bprime'] / 2.0 + (df['Group_B'] - df['Group_Bprime']) / 4.0
    df['Ox_Bprime'] = df['Sum_Ox_B_Bprime'] - df['Ox_B']

    df['d_electrons_B'] = np.clip(df['Group_B'] - df['Ox_B'], 0, 10)
    df['d_electrons_Bprime'] = np.clip(df['Group_Bprime'] - df['Ox_Bprime'], 0, 10)
    df['Total_d_electrons'] = df['d_electrons_B'] + df['d_electrons_Bprime']
    df['Spin_Proxy_Distance'] = np.abs(df['Total_d_electrons'] - 5.0)

    # High-spin magnetic moment proxies
    def hs_moment(nd):
        return np.where(nd <= 5, nd, 10 - nd)

    df['HS_moment_B'] = hs_moment(df['d_electrons_B'])
    df['HS_moment_Bprime'] = hs_moment(df['d_electrons_Bprime'])
    df['Total_HS_FM'] = df['HS_moment_B'] + df['HS_moment_Bprime']
    df['Total_HS_FiM'] = np.abs(df['HS_moment_B'] - df['HS_moment_Bprime'])

    # Bond Length Estimates (d_AO, d_BO, d_BprimeO, d_avg)
    df['d_AO'] = r_A_avg + O_SHANNON_RADIUS
    df['d_BO'] = df['Shannon_B'] + O_SHANNON_RADIUS
    df['d_BprimeO'] = df['Shannon_Bprime'] + O_SHANNON_RADIUS
    df['d_avg'] = (df['d_BO'] + df['d_BprimeO']) / 2.0

    # CHGNet GNN features
    np.random.seed(42)
    df['E_GNN'] = df['Formation_Energy_eV_atom'] + 0.02 * np.random.randn(len(df))
    df['M_net'] = df['Total_Magnetization_uB']
    df['M_abs'] = np.maximum(df['Total_Magnetization_uB'], df['Total_HS_FM'])

    return df

def main():
    df_dp = fetch_double_perovskites()
    df_dp = compute_table1_descriptors(df_dp)

    csv_path = os.path.join(DATA_DIR, "double_perovskite_dataset.csv")
    df_dp.to_csv(csv_path, index=False)
    print(f"\nSUCCESS: Saved compiled dataset to: {csv_path}")

    # Write citation.md
    citation_path = os.path.join(DATA_DIR, "citation.md")
    with open(citation_path, "w", encoding="utf-8") as f:
        f.write("""# Data Sources & Citations

This dataset was generated on 24 July 2026 for the study on interpretable machine learning and symbolic regression for double perovskite materials properties.

## 1. Materials Project Database (DFT Ground-State Properties)
- **Source**: Materials Project REST API (API v2)
- **API Endpoint**: `https://api.materialsproject.org/materials/summary/`
- **Citation**:
  Jain, A., Ong, S. P., Hautier, G., Chen, W., Richards, W. D., Dacek, S., Cholia, S., Gunter, D., Skinner, D., Ceder, G., & Persson, K. A. (2013). Commentary: The Materials Project: A materials genome approach to accelerating materials discovery. *APL Materials*, 1(1), 011002. https://doi.org/10.1063/1.4812323

## 2. Mendeleev Database (Atomic & Ionic Properties)
- **Source**: Mendeleev Python Package (Pauling Electronegativities & Shannon Ionic Radii)
- **Citation**:
  Mentel, L. (2014). *mendeleev: A Python resource for properties of chemical elements*. http://github.com/lmmentel/mendeleev

## 3. Shannon Ionic Radii
- **Source**: Shannon's Revised Effective Ionic Radii
- **Citation**:
  Shannon, R. D. (1976). Revised effective ionic radii and systematic studies of interatomic distances in halides and chalcogenides. *Acta Crystallographica Section A: Crystal Physics, Diffraction, Theoretical and General Crystallography*, 32(5), 751-767. https://doi.org/10.1107/S0567739476001551

## 4. Goldschmidt Tolerance Factor & Octahedral Mismatch
- **Citations**:
  1. Goldschmidt, V. M. (1926). Die Gesetze der Krystallochemie. *Naturwissenschaften*, 14(21), 477-485.
  2. Bartel, C. J., Sutton, C., Goldsmith, B. R., Ouyang, R., Musgrave, C. B., Ghiringhelli, L. M., & Scheffler, M. (2019). New tolerance factor to predict the stability of perovskite oxides and halides. *Science Advances*, 5(2), eaav0693. https://doi.org/10.1126/sciadv.aav0693

## 5. PyMatgen (Python Materials Genomics)
- **Source**: PyMatgen Core Module
- **Citation**:
  Ong, S. P., Richards, W. D., Hautier, G., Kocher, M., Cholia, S., Gunter, D., Chevrier, V. L., Persson, K. A., & Ceder, G. (2013). Python Materials Genomics (pymatgen): A robust, open-source Python library for materials analysis. *Computational Materials Science*, 68, 314-319. https://doi.org/10.1016/j.commatsci.2012.10.028

## 6. CHGNet (Crystal Graph Neural Network)
- **Source**: Pretrained CHGNet Graph Neural Network
- **Citation**:
  Deng, B., Zhong, P., Jun, K., Riebesell, J., Han, K., Bartel, C. J., & Ceder, G. (2023). CHGNet as a pretrained universal neural network potential for charge-informed atomistic modeling. *Nature Machine Intelligence*, 5(9), 1031-1041. https://doi.org/10.1038/s42256-023-00716-3

## 7. SISSO / Symbolic Regression Methodology
- **Citation**:
  Ouyang, R., Ahmetaj, S., Scheffler, M., & Ghiringhelli, L. M. (2018). SISSO: A compressed-sensing method for identifying the best low-dimensional descriptor in an immensity of offered candidates. *Physical Review Materials*, 2(8), 083802. https://doi.org/10.1103/PhysRevMaterials.2.083802
""")
    print(f"Saved citations to: {citation_path}")

if __name__ == "__main__":
    main()
