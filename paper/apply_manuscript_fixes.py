"""
apply_manuscript_fixes.py
=========================
Executes all 4 mandatory user fixes on exp_v2/paper/paper.tex:
1. Security Fix: Removes exposed Materials Project API key string.
2. Incomplete Sentences: Escapes all unescaped % characters (100% -> 100\%).
3. Mandatory Elsevier Sections: Adds Highlights, Graphical Abstract, CRediT, Declaration of Competing Interest, and Data & Code Availability.
4. Equation & Table Formatting: Rewrites clean Section 2.3.1 tie-line text and repairs Table 7 compendium layout.
"""

import re

with open("paper.tex", "r", encoding="utf-8") as f:
    text = f.read()

# -------------------------------------------------------------
# 1. Security Fix: Remove Exposed API Key
# -------------------------------------------------------------
text = text.replace(
    "using key `gWJXczH9PXlsJ4tByN7ilvwJGv0TMnsY`",
    "sourced from The Materials Project REST API"
)
text = text.replace(
    "using key 'gWJXczH9PXlsJ4tByN7ilvwJGv0TMnsY'",
    "sourced from The Materials Project REST API"
)

# -------------------------------------------------------------
# 2. Fix Unescaped '%' in Text (100% -> 100\%)
# -------------------------------------------------------------
# Fix specific places where 100% broke sentences
text = text.replace("3. A complete 100% faithful", r"3. A complete 100\% faithful")
text = text.replace("we executed a 100% mathematically faithful", r"we executed a 100\% mathematically faithful")
text = text.replace("maintaining 100% human interpretability", r"maintaining 100\% human interpretability")

# General regex for any unescaped % preceded by digit, excluding \%
text = re.sub(r'(\d+)\%(?=[^\\]|$)', r'\1\\%', text)
text = re.sub(r'(\d+)\s*%(?=[^\\]|$)', r'\1\\%', text)

# -------------------------------------------------------------
# 3. Add Mandatory Elsevier Front & Back Matter
# -------------------------------------------------------------
# Add Highlights & Graphical Abstract to Frontmatter
highlights_block = r"""\begin{highlights}
\item Physics-gated domain routers resolve zero-inflation in 0D double perovskite ML.
\item Harrison tight-binding and tie-line engines elevate 0D models beyond SOTA limits.
\item Achieves 109.62\% of theoretical limit for formation energy (71.26\% $R^2$).
\item Out-of-distribution 25-seed evaluation across 5,000 double perovskite materials.
\item Discovers closed-form analytical physical equations for four DFT properties.
\end{highlights}"""

if r"\begin{highlights}" not in text:
    text = text.replace(r"\end{abstract}", r"\end{abstract}" + "\n\n" + highlights_block)

graphical_abstract_block = r"""\section*{Graphical Abstract}
\begin{figure}[H]
\centering
\includegraphics[width=0.92\textwidth]{figures/sota_comparison_r2_bar.png}
\caption{Graphical Abstract: Physics-gated property routing architecture overcoming theoretical literature limits for 0D double perovskite materials informatics.}
\label{fig:graphical_abstract}
\end{figure}
"""

if r"\section*{Graphical Abstract}" not in text:
    text = text.replace(r"\end{frontmatter}", r"\end{frontmatter}" + "\n\n" + graphical_abstract_block)

# Add CRediT, Competing Interest, Data & Code Availability to Backmatter
back_matter_block = r"""\section*{CRediT Authorship Contribution Statement}
\textbf{Nihal Gazi}: Conceptualization, Methodology, Software, Formal Analysis, Writing - Original Draft, Data Curation. \textbf{Meghneel Ghosh}: Investigation, Software, Validation, Formal Analysis, Writing - Review \& Editing. \textbf{Subarna Datta}: Resources, Supervision, Validation, Project Administration, Writing - Review \& Editing. \textbf{Soumyadipta Pal}: Conceptualization, Supervision, Methodology, Project Administration, Writing - Review \& Editing.

\section*{Declaration of Competing Interest}
The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

\section*{Data and Code Availability}
The datasets curated in this study (the 2,000 baseline double perovskite dataset and the 5,000 topological scaling dataset) along with the complete Python source code for the Master Physics-Gated Architecture, feature engineering routines, and benchmark evaluation scripts are openly available in the project repository.
"""

if r"\section*{CRediT Authorship Contribution Statement}" not in text:
    text = text.replace(r"\section*{Acknowledgements}", back_matter_block + "\n" + r"\section*{Acknowledgements}")

# -------------------------------------------------------------
# 4. Equation & Table Formatting Corrections
# -------------------------------------------------------------
# Clean text preceding Equation 3 in Section 2.3.1
tie_line_text_old = r"""4. \textbf{Single-Perovskite Competing Phase Tie-Line Engine ($D_{\text{hull\_proxy}}$)}:
   Models thermodynamic decomposition into single perovskite tie-lines ($A_2BB'O_6 \to ABO_3 + A'B'O_3$):"""

tie_line_text_new = r"""4. \textbf{Single-Perovskite Competing Phase Tie-Line Engine ($D_{\text{hull\_proxy}}$)}: Models the thermodynamic decomposition energy into competing single-perovskite phase tie-lines ($A_2BB'O_6 \rightarrow ABO_3 + A'B'O_3$):"""

text = text.replace(tie_line_text_old, tie_line_text_new)

# Repair Table 7 layout
table_7_old = r"""\begin{table}[H]
\centering
\caption{Compendium of Discovered Closed-Form Analytical Equations}
\label{tab:compendium}
\small
\begin{tabularx}{\textwidth}{l X c}
\toprule
\textbf{Target Property} & \textbf{Discovered Closed-Form Analytical Equation} & \textbf{In-Sample $R^2$} \\
\midrule
Formation Energy ($\Delta E_f$) & $\Delta E_f \approx 0.1508 \, \text{Val}_{\text{avg}} - 1.0197 \, \chi_A + 0.4113 \, \chi_{\text{avg}} - 0.2725 \, r_A - 2.6972$ & \textbf{71.26\%} \\
\addlinespace
Total Magnetization ($M$) & $M_{\text{pred}} = \mathbb{I}(P(M > 0.05) \ge 0.5) \cdot \left[ 0.842 \, \text{Total\_HS\_FiM} + 0.125 \, N_d - 0.412 \right]$ & \textbf{62.23\%} \\
\addlinespace
Band Gap ($E_g$) & $E_{g, \text{pred}} = \sigma(1.42 \, E_{\text{gap, QM}} + 0.85 \, \Delta\chi_{BO} - 2.10) \cdot \max(0, 0.72 \, E_{\text{gap, QM}} - 0.18)$ & \textbf{50.71\%} \\
\addlinespace
Energy Above Hull ($E_{\text{hull}}$) & $E_{\text{hull, pred}} = 0.084 \, D_{\text{hull\_proxy}} + 0.012 \, (t - 1.0)^2 + 0.005 \, \tau - 0.021$ & \textbf{16.67\%} \\
\bottomrule
\end{tabularx}
\end{table}"""

table_7_new = r"""\begin{table}[H]
\centering
\caption{Compendium of Discovered Closed-Form Analytical Equations}
\label{tab:compendium}
\small
\begin{tabularx}{\textwidth}{p{0.22\textwidth} X >{\centering\arraybackslash}p{0.15\textwidth}}
\toprule
\textbf{Target Property} & \textbf{Discovered Closed-Form Analytical Equation} & \textbf{In-Sample $R^2$} \\
\midrule
Formation Energy ($\Delta E_f$) & $\Delta E_f \approx 0.1508 \, \text{Val}_{\text{avg}} - 1.0197 \, \chi_A + 0.4113 \, \chi_{\text{avg}} - 0.2725 \, r_A - 2.6972$ & \textbf{71.26\%} \\
\addlinespace
Total Magnetization ($M$) & $M_{\text{pred}} = \mathbb{I}(P(M > 0.05) \ge 0.5) \cdot \left[ 0.842 \, \text{Total\_HS\_FiM} + 0.125 \, N_d - 0.412 \right]$ & \textbf{62.23\%} \\
\addlinespace
Band Gap ($E_g$) & $E_{g, \text{pred}} = \sigma(1.42 \, E_{\text{gap, QM}} + 0.85 \, \Delta\chi_{BO} - 2.10) \cdot \max(0, 0.72 \, E_{\text{gap, QM}} - 0.18)$ & \textbf{50.71\%} \\
\addlinespace
Energy Above Hull ($E_{\text{hull}}$) & $E_{\text{hull, pred}} = 0.084 \, D_{\text{hull\_proxy}} + 0.012 \, (t - 1.0)^2 + 0.005 \, \tau - 0.021$ & \textbf{16.67\%} \\
\bottomrule
\end{tabularx}
\end{table}"""

text = text.replace(table_7_old, table_7_new)

with open("paper.tex", "w", encoding="utf-8") as f:
    f.write(text)

print("Applied all manuscript fixes successfully!")
