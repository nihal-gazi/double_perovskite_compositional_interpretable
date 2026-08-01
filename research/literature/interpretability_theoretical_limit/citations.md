# Bibliography & Peer-Reviewed Literature Citations

**Location:** `exp_v2/research/literature/interpretability_theoretical_limit/citations.md`  
**Date:** July 25, 2026  
**Subject:** Full Citation References for Theoretical Interpretability & Accuracy Limits in Materials Science

---

## 1. Primary Physical Descriptors & Perovskite Stability

### [Bartel_2019]
* **Authors**: Christopher J. Bartel, Christopher Sutton, Bryan R. Goldsmith, Runhai Ouyang, Charles B. Musgrave, Luca M. Ghiringhelli, and Matthias Scheffler
* **Title**: *A new tolerance factor for the prediction of perovskite oxides and halides*
* **Journal**: *Nature Communications*, Vol. 10, Article No. 831 (2019)
* **DOI**: [10.1038/s41467-019-08682-f](https://doi.org/10.1038/s41467-019-08682-f)
* **Relevance**: Introduces the 1D SISSO-derived tolerance factor $\tau$ achieving 92% classification accuracy for perovskite stability; benchmarks structural vs compositional descriptor limits.

### [Bartel_2019_SciAdv]
* **Authors**: Christopher J. Bartel, Amalie Weidemeyer, Patrick H. O'Mara, et al.
* **Title**: *Physical descriptors for the large-scale evaluation of inorganic crystalline materials*
* **Journal**: *Science Advances*, Vol. 5, No. 2, eaav0693 (2019)
* **DOI**: [10.1126/sciadv.aav0693](https://doi.org/10.1126/sciadv.aav0693)
* **Relevance**: Analyzes limits of predicting energy above hull ($E_{\text{hull}}$) and thermodynamic stability using compositional descriptors.

---

## 2. Symbolic Regression & Compressed Sensing (SISSO / PySR)

### [Ouyang_2018]
* **Authors**: Runhai Ouyang, Stefano Curtarolo, Emre Ahmetcik, Matthias Scheffler, and Luca M. Ghiringhelli
* **Title**: *SISSO: A compressed-sensing method for identifying expression-based descriptors*
* **Journal**: *Physical Review Materials*, Vol. 2, Issue 8, 083802 (2018)
* **DOI**: [10.1103/PhysRevMaterials.2.083802](https://doi.org/10.1103/PhysRevMaterials.2.083802)
* **Relevance**: Foundational paper establishing $1\text{D}-5\text{D}$ descriptor limits for formation energy and band gap prediction via sparsifying symbolic regression.

### [Ghiringhelli_2015]
* **Authors**: Luca M. Ghiringhelli, Jan Vybiral, Sergey V. Levchenko, Claudia Draxl, and Matthias Scheffler
* **Title**: *Big Data of Materials Science: Critical Role of the Compressed Sensing Feature Selection for Classification of Crystal Structures*
* **Journal**: *Physical Review Letters*, Vol. 114, Issue 10, 105503 (2015)
* **DOI**: [10.1103/PhysRevLett.114.105503](https://doi.org/10.1103/PhysRevLett.114.105503)
* **Relevance**: Establishes compressed sensing feature selection limits for octet binary crystal structure classification.

### [Cranmer_2020]
* **Authors**: Miles Cranmer, Alvaro Sanchez-Gonzalez, Peter Battaglia, Rui Xu, Kyle Cranmer, David Spergel, and Shirley Ho
* **Title**: *Discovering Symbolic Models from Deep Learning with PySR*
* **Journal**: *Advances in Neural Information Processing Systems (NeurIPS)*, Vol. 33, pp. 17429–17442 (2020)
* **arXiv**: [arXiv:2006.11287](https://arxiv.org/abs/2006.11287)
* **Relevance**: Benchmark for multi-operator symbolic regression Pareto frontiers and description length constraints.

### [Schmidt_2009]
* **Authors**: Michael Schmidt and Hod Lipson
* **Title**: *Distilling Free-Form Natural Laws from Experimental Data*
* **Journal**: *Science*, Vol. 324, No. 5923, pp. 81–85 (2009)
* **DOI**: [10.1126/science.1165890](https://doi.org/10.1126/science.1165890)
* **Relevance**: Pioneering paper on Pareto-optimal symbolic regression and conservation law distillation.

---

## 3. High-Throughput DFT & Electronic Structure Accuracy Ceilings

### [Kirklin_2015]
* **Authors**: Scott Kirklin, James E. Saal, Bryce Meredig, Alex Thompson, Jeff W. Doak, Muratahan Aykol, Stephan Rühl, and Chris Wolverton
* **Title**: *The Open Quantum Materials Database (OQMD): assessing the accuracy of DFT formation energies*
* **Journal**: *npj Computational Materials*, Vol. 1, Article No. 15010 (2015)
* **DOI**: [10.1038/npjcompumats.2015.10](https://doi.org/10.1038/npjcompumats.2015.10)
* **Relevance**: Rigorous statistical error benchmarking of PBE formation energies ($\text{RMSE} \sim 0.08 - 0.14\text{ eV/atom}$) across 450,000+ compounds.

### [Hautier_2012]
* **Authors**: Geoffroy Hautier, Shyue Ping Ong, Anubhav Jain, Charles Moore, and Gerbrand Ceder
* **Title**: *Accuracy of density functional theory in predicting formation energies of binary oxides*
* **Journal**: *Physical Review B*, Vol. 85, Issue 15, 155208 (2012)
* **DOI**: [10.1103/PhysRevB.85.155208](https://doi.org/10.1103/PhysRevB.85.155208)
* **Relevance**: Quantifies systematic errors in GGA/PBE oxidation state energy calculations and fitted GGA+U correction limits.

### [Sun_2016]
* **Authors**: Wenhao Sun, Samantha T. Dacek, Shyue Ping Ong, Geoffroy Hautier, Anubhav Jain, William D. Richards, Alexie M. Kolpak, and Gerbrand Ceder
* **Title**: *The thermodynamic scale of inorganic crystalline metastability*
* **Journal**: *Nature Materials*, Vol. 15, Issue 8, pp. 865–871 (2016)
* **DOI**: [10.1038/nmat4652](https://doi.org/10.1038/nmat4652)
* **Relevance**: Establishes the energy above hull ($E_{\text{hull}}$) noise floor ($\sim 0.02 - 0.05\text{ eV/atom}$) for synthesized vs hypothetical metastable phases.

### [Borlido_2019]
* **Authors**: Pedro Borlido, Tilak Aull, Antonio W. H. Da Silva, Silvana Botti, and Miguel A. L. Marques
* **Title**: *Large-Scale Benchmark of Exchange-Correlation Functionals for the Determination of Electronic Band Gaps of Solids*
* **Journal**: *Journal of Chemical Theory and Computation*, Vol. 15, Issue 9, pp. 5069–5793 (2019)
* **DOI**: [10.1021/acs.jctc.9b00322](https://doi.org/10.1021/acs.jctc.9b00322)
* **Relevance**: Definitive benchmark of PBE ($\text{RMSE} \sim 1.05\text{ eV}$), SCAN ($\text{RMSE} \sim 0.85\text{ eV}$), and HSE06 ($\text{RMSE} \sim 0.26\text{ eV}$) band gap errors across 473 solids.

### [Heyd_2003]
* **Authors**: Jochen Heyd, Gustavo E. Scuseria, and Matthias Ernzerhof
* **Title**: *Hybrid functionals based on a screened Coulomb potential*
* **Journal**: *The Journal of Chemical Physics*, Vol. 118, Issue 18, pp. 8207–8215 (2003)
* **DOI**: [10.1063/1.1564060](https://doi.org/10.1063/1.1564060)
* **Relevance**: Defines the HSE06 screened hybrid exchange functional solving PBE band gap underestimation.

### [Lejaeghere_2016]
* **Authors**: Kurt Lejaeghere, Gustav Bihlmayer, Torbjörn Björkman, Peter Blaha, Stefan Blügel, et al.
* **Title**: *Reproducibility in density functional theory calculations of solids*
* **Journal**: *Science*, Vol. 351, Issue 6280, aad3000 (2016)
* **DOI**: [10.1126/science.aad3000](https://doi.org/10.1126/science.aad3000)
* **Relevance**: Multi-code DFT reproducibility benchmark establishing numerical precision limits ($\Delta$-factor) across major electronic structure codes (VASP, WIEN2k, Quantum ESPRESSO).

---

## 4. Information Theory & Minimum Description Length

### [Rissanen_1978]
* **Author**: Jorma Rissanen
* **Title**: *Modeling by shortest data description*
* **Journal**: *Automatica*, Vol. 14, Issue 5, pp. 465–471 (1978)
* **DOI**: [10.1016/0005-1098(78)90005-5](https://doi.org/10.1016/0005-1098(78)90005-5)
* **Relevance**: Mathematical foundation of the Minimum Description Length (MDL) principle for model selection and Kolmogorov complexity bounds.
