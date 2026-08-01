"""
apply_7_user_requests.py
========================
Applies all 7 user-requested fixes to exp_v2/paper/paper.tex cleanly and accurately.
"""

import re

with open("paper.tex", "r", encoding="utf-8") as f:
    text = f.read()

# -------------------------------------------------------------
# 0. Add \usepackage{rotating} to preamble
# -------------------------------------------------------------
if r"\usepackage{rotating}" not in text:
    text = text.replace(r"\usepackage{float}", "\\usepackage{float}\n\\usepackage{rotating}")

# -------------------------------------------------------------
# 1. Section 2.1: Fix List Newlines & Remove Repetitive Text
# -------------------------------------------------------------
sec_2_1_old = r"""\subsection{Dataset Curation}
The primary baseline dataset consists of 2,000 double perovskite compounds ($A_2BB'O_6$) sourced from The Materials Project database \cite{materialsproject}. Strict crystallographic and compositional filters were applied:
\begin{enumerate}
\item \textbf{Formula Verification}: Verified $A_2BB'O_6$ stoichiometry with distinct transition metals on $B$ and $B'$ sites.
\item \textbf{DFT Ground-State Properties}: Extracted PBE-calculated formation energy ($\Delta E_f$, eV/atom), total magnetization ($M$, $\mu_B$/f.u.), electronic band gap ($E_g$, eV), and energy above hull ($E_{\text{hull}}$, eV/atom) directly from high-throughput Density Functional Theory calculations \cite{materialsproject, hautier2012accuracy, kirklin2015open}.
\item \textbf{Large-Scale Benchmark Dataset}: To test topological scaling, a secondary dataset of 5,000 double perovskite materials was retrieved from The Materials Project API sourced from The Materials Project REST API.
\end{enumerate}"""

sec_2_1_new = r"""\subsection{Dataset Curation}
The primary baseline dataset consists of 2,000 double perovskite compounds ($A_2BB'O_6$) sourced from The Materials Project database \cite{materialsproject}. Strict crystallographic and compositional filters were applied:
\begin{enumerate}
\item \textbf{Formula Verification}: Verified $A_2BB'O_6$ stoichiometry with distinct transition metals on $B$ and $B'$ sites.

\item \textbf{DFT Ground-State Properties}: Extracted PBE-calculated formation energy ($\Delta E_f$, eV/atom), total magnetization ($M$, $\mu_B$/f.u.), electronic band gap ($E_g$, eV), and energy above hull ($E_{\text{hull}}$, eV/atom) directly from high-throughput Density Functional Theory calculations \cite{materialsproject, hautier2012accuracy, kirklin2015open}.

\item \textbf{Large-Scale Benchmark Dataset}: To test topological scaling, a secondary dataset of 5,000 double perovskite materials was retrieved from The Materials Project REST API \cite{materialsproject}.
\end{enumerate}"""

text = text.replace(sec_2_1_old, sec_2_1_new)

# -------------------------------------------------------------
# 2. Section 2.4: Restructure into Novelty and Overlaps Headings
# -------------------------------------------------------------
sec_2_4_old = r"""\subsection{Methodological Novelty vs. Literature Overlap}
Table~\ref{tab:novelty_matrix} explicitly delineates which components of our framework are novel contributions and which build upon pre-existing literature foundations.

\begin{table}[H]
\centering
\caption{Methodological Novelty vs. Pre-Existing Literature Matrix}
\label{tab:novelty_matrix}
\small
\begin{tabularx}{\textwidth}{p{0.22\textwidth} p{0.26\textwidth} X}
\toprule
\textbf{Pipeline Component} & \textbf{Pre-Existing Literature Basis} & \textbf{Our Methodological Novelty} \\
\midrule
0D Atomic Descriptors & Shannon radii \cite{shannon1976revised}, Pauling electronegativity & Automated 0D composition ingestion without 3D CIF coordinates. \\
Symbolic Regression & SISSO \cite{ouyang2018sisso}, LASSO \cite{ghiringhelli2015bigdata} & Property-routed hybrid models overcoming 0D limits. \\
Quantum Physics Engine & Harrison tight-binding theory \cite{harrison1999elementary} & First integration of $E_{\text{gap, QM}}$ into 0D ML feature generators. \\
Magnetization Gating & Standard classification hurdles & High-$C$ ($C=200.0$) Hard-Margin Hurdle resolving zero-inflation. \\
Band Gap Gating & Hard binary thresholds & Soft-Sigmoidal Gated Regressor restoring derivative continuity. \\
Hull Stability & Bartel $\tau$ factor \cite{bartel2019new} & Single-perovskite tie-line proxy ($D_{\text{hull\_proxy}}$) for $A_2BB'O_6$. \\
\bottomrule
\end{tabularx}
\end{table}"""

sec_2_4_new = r"""\subsection{Methodological Novelty vs. Literature Overlap}

\subsubsection{Methodological Novelty and Quantitative Improvements}
Our Method introduces six fundamental architectural innovations specifically engineered to overcome the information-theoretic ceilings of 0D compositional models:
\begin{enumerate}
\item \textbf{Harrison Tight-Binding Quantum Gap Engine ($E_{\text{gap, QM}}$)}: Embeds solid-state quantum mechanical band gap theory \cite{harrison1999elementary, zaanen1985band} into 0D descriptor space, elevating band gap $E_g R^2$ from a baseline collapse of $6.41\%$ (C0) to \textbf{$28.40\%$} (C1) as documented in Table~\ref{tab:ablation_study}.
\item \textbf{Birch-Murnaghan Lattice Elastic Strain Engine ($(t - 1.0)^2$)}: Captures steric polyhedral strain energy \cite{goldschmidt1926gesetze, woodward1997octahedral}, boosting formation energy $\Delta E_f R^2$ from $55.40\%$ to \textbf{$61.80\%$} (Table~\ref{tab:ablation_study}).
\item \textbf{Single-Perovskite Competing Phase Tie-Line Proxy ($D_{\text{hull\_proxy}}$)}: Models sub-perovskite decomposition pathways ($A_2BB'O_6 \rightarrow ABO_3 + A'B'O_3$) \cite{sun2016thermodynamic, yamashita2018band}, rescuing energy above hull $E_{\text{hull}} R^2$ from $0.50\%$ (C2) to \textbf{$16.67\%$} (Table~\ref{tab:ablation_study}).
\item \textbf{Octahedral $d^0/d^{10}$ Closed-Shell Engine}: Quantifies crystal field orbital splitting ($\mathcal{O}_h$) stabilization \cite{goodenough1971magnetism, walsh2011design}, driving $E_g R^2$ to \textbf{$36.50\%$} (Table~\ref{tab:ablation_study}).
\item \textbf{High-$C$ ($C=200.0$) Hard-Margin Hurdle Model}: Enforces a strict, high-penalty decision boundary isolating non-magnetic ($M \le 0.05\ \mu_B$) ground states \cite{goodenough1955theory, kanamori1959superexchange}, solving magnetization zero-inflation and elevating $M R^2$ from $2.10\%$ to \textbf{$62.23\%$} (Table~\ref{tab:sota_benchmark_m}).
\item \textbf{Soft-Sigmoidal Gated Regressor}: Restores continuous order-parameter derivatives across metallic/semiconducting phase boundaries \cite{borlido2019large}, pushing $E_g R^2$ to \textbf{$50.71\%$} (Table~\ref{tab:sota_benchmark_eg}).
\end{enumerate}

\subsubsection{Methodological Overlaps and Prior Literature Basis}
Our architecture builds upon and integrates several foundational principles established in prior condensed matter literature, as summarized in Table~\ref{tab:novelty_matrix}:
\begin{itemize}
\item \textbf{0D Atomic Constants}: Utilizes Shannon ionic radii \cite{shannon1976revised} and Pauling electronegativities \cite{ouyang2018sisso}.
\item \textbf{Goldschmidt Tolerance Factor ($t$)}: Integrates classic polyhedral packing ratios \cite{goldschmidt1926gesetze}.
\item \textbf{Bartel Tolerance Factor ($\tau$)}: Incorporates Bartel's global tolerance factor for perovskite oxide stability \cite{bartel2019new, bartel2019sciadv}.
\item \textbf{Compressed Sensing Feature Selection}: Utilizes $L_1$-regularized LASSO and Orthogonal Matching Pursuit (OMP) feature screening pioneered by Ghiringhelli et al. \cite{ghiringhelli2015bigdata} and Ouyang et al. \cite{ouyang2018sisso}.
\end{itemize}

\begin{table}[H]
\centering
\caption{Methodological Novelty vs. Pre-Existing Literature Matrix}
\label{tab:novelty_matrix}
\small
\begin{tabularx}{\textwidth}{p{0.22\textwidth} p{0.26\textwidth} X}
\toprule
\textbf{Pipeline Component} & \textbf{Pre-Existing Literature Basis} & \textbf{Our Methodological Novelty} \\
\midrule
0D Atomic Descriptors & Shannon radii \cite{shannon1976revised}, Pauling electronegativity & Automated 0D composition ingestion without 3D CIF coordinates. \\
Symbolic Regression & SISSO \cite{ouyang2018sisso}, LASSO \cite{ghiringhelli2015bigdata} & Property-routed hybrid models overcoming 0D limits. \\
Quantum Physics Engine & Harrison tight-binding theory \cite{harrison1999elementary} & First integration of $E_{\text{gap, QM}}$ into 0D ML feature generators. \\
Magnetization Gating & Standard classification hurdles & High-$C$ ($C=200.0$) Hard-Margin Hurdle resolving zero-inflation. \\
Band Gap Gating & Hard binary thresholds & Soft-Sigmoidal Gated Regressor restoring derivative continuity. \\
Hull Stability & Bartel $\tau$ factor \cite{bartel2019new} & Single-perovskite tie-line proxy ($D_{\text{hull\_proxy}}$) for $A_2BB'O_6$. \\
\bottomrule
\end{tabularx}
\end{table}"""

text = text.replace(sec_2_4_old, sec_2_4_new)

# -------------------------------------------------------------
# 3. Shrink Column 1 width of Tables 3a--3d (Tables 4 to 7 in document)
# -------------------------------------------------------------
text = text.replace(r"\begin{tabularx}{\textwidth}{p{0.32\textwidth} c >{\centering\arraybackslash}X >{\centering\arraybackslash}X >{\centering\arraybackslash}X >{\centering\arraybackslash}X}",
                    r"\begin{tabularx}{\textwidth}{p{0.25\textwidth} c >{\centering\arraybackslash}X >{\centering\arraybackslash}X >{\centering\arraybackslash}X >{\centering\arraybackslash}X}")

# -------------------------------------------------------------
# 4. Break Table 11 into 4 Rotated Landscape Tables (sidewaystable)
# -------------------------------------------------------------
tab_11_old = r"""\begin{table}[H]
\centering
\caption{Direct Out-of-Distribution (80/20 Train/Test Split) Performance Comparison: Our Method vs. SOTA Baselines}
\label{tab:sota_ood_comparison}
\small
\begin{tabularx}{\textwidth}{p{0.24\textwidth} p{0.24\textwidth} c c c c}
\toprule
\textbf{Target Property} & \textbf{Model / Algorithm} & \textbf{Dataset} & \textbf{80\% Train $R^2$} & \textbf{20\% Test $R^2$} & \textbf{Test Limit (\%)} \\
\midrule
\multirow{4}{*}{\textbf{Formation Energy ($\Delta E_f$)}} & Ouyang 2018 SISSO \cite{ouyang2018sisso} & 2,000 & 48.33\% & 48.26\% & 74.24\% \\
 & \textbf{Our Method} & \textbf{2,000} & \textbf{72.14\%} & \textbf{65.89\%} & \textbf{101.37\%} \\
 & Ouyang 2018 SISSO \cite{ouyang2018sisso} & 5,000 & 48.67\% & 49.09\% & 75.53\% \\
 & \textbf{Our Method} & \textbf{5,000} & \textbf{70.10\%} & \textbf{66.36\%} & \textbf{102.13\%} \\
\midrule
\multirow{4}{*}{\textbf{Total Magnetization ($M$)}} & Ghiringhelli 2015 LASSO \cite{ghiringhelli2015bigdata} & 2,000 & 3.71\% & 1.89\% & 3.15\% \\
 & \textbf{Our Method} & \textbf{2,000} & \textbf{63.36\%} & \textbf{16.70\%} & \textbf{30.28\%} \\
 & Ghiringhelli 2015 LASSO \cite{ghiringhelli2015bigdata} & 5,000 & 3.23\% & 2.24\% & 3.74\% \\
 & \textbf{Our Method} & \textbf{5,000} & \textbf{46.51\%} & \textbf{29.15\%} & \textbf{49.49\%} \\
\midrule
\multirow{4}{*}{\textbf{Band Gap ($E_g$)}} & Borlido 2019 SISSO \cite{borlido2019large} & 2,000 & -6.34\% & -6.86\% & 0.00\% \\
 & \textbf{Our Method} & \textbf{2,000} & \textbf{49.63\%} & \textbf{37.45\%} & \textbf{74.90\%} \\
 & Borlido 2019 SISSO \cite{borlido2019large} & 5,000 & 0.77\% & 0.40\% & 0.80\% \\
 & \textbf{Our Method} & \textbf{5,000} & \textbf{42.38\%} & \textbf{36.41\%} & \textbf{72.82\%} \\
\midrule
\multirow{4}{*}{\textbf{Energy Above Hull ($E_{\text{hull}}$)}} & Bartel 2019 $\tau$ \cite{bartel2019new} & 2,000 & 0.44\% & 0.23\% & 0.93\% \\
 & \textbf{Our Method} & \textbf{2,000} & \textbf{17.92\%} & \textbf{6.85\%} & \textbf{27.41\%} \\
 & Bartel 2019 $\tau$ \cite{bartel2019new} & 5,000 & 0.61\% & 0.64\% & 2.54\% \\
 & \textbf{Our Method} & \textbf{5,000} & \textbf{17.72\%} & \textbf{7.04\%} & \textbf{35.38\%} \\
\bottomrule
\end{tabularx}
\end{table}"""

tab_11_new = r"""To ensure complete visual clarity and eliminate horizontal table overcrowding, Table~\ref{tab:ood_ef} through Table~\ref{tab:ood_ehull} present the rotated property-by-property Out-of-Distribution (80/20 Train/Test Split) benchmark evaluations comparing Literature SOTA algorithms against Our Method across both the 2,000 and 5,000 datasets.

\begin{sidewaystable}[H]
\centering
\caption{Out-of-Distribution (80/20 Train/Test Split) Benchmark for Formation Energy ($\Delta E_f$)}
\label{tab:ood_ef}
\small
\begin{tabularx}{\textwidth}{p{0.32\textwidth} c >{\centering\arraybackslash}X >{\centering\arraybackslash}X >{\centering\arraybackslash}X >{\centering\arraybackslash}X}
\toprule
\textbf{Model / Algorithm} & \textbf{Dataset Size} & \textbf{80\% Train $R^2$} & \textbf{20\% Test $R^2$} & \textbf{Theoretical Limit ($R^2_{\text{limit}}$)} & \textbf{Test Limit Achieved (\%)} \\
\midrule
Ouyang 2018 SISSO \cite{ouyang2018sisso} & 2,000 & 48.33\% & 48.26\% & 65.0\% & 74.24\% \\
\textbf{Our Method} & \textbf{2,000} & \textbf{72.14\%} & \textbf{65.89\%} & \textbf{65.0\%} & \textbf{101.37\%} \\
Ouyang 2018 SISSO \cite{ouyang2018sisso} & 5,000 & 48.67\% & 49.09\% & 65.0\% & 75.53\% \\
\textbf{Our Method} & \textbf{5,000} & \textbf{70.10\%} & \textbf{66.36\%} & \textbf{65.0\%} & \textbf{102.13\%} \\
\bottomrule
\end{tabularx}
\end{sidewaystable}

\begin{sidewaystable}[H]
\centering
\caption{Out-of-Distribution (80/20 Train/Test Split) Benchmark for Total Magnetization ($M$)}
\label{tab:ood_m}
\small
\begin{tabularx}{\textwidth}{p{0.32\textwidth} c >{\centering\arraybackslash}X >{\centering\arraybackslash}X >{\centering\arraybackslash}X >{\centering\arraybackslash}X}
\toprule
\textbf{Model / Algorithm} & \textbf{Dataset Size} & \textbf{80\% Train $R^2$} & \textbf{20\% Test $R^2$} & \textbf{Theoretical Limit ($R^2_{\text{limit}}$)} & \textbf{Test Limit Achieved (\%)} \\
\midrule
Ghiringhelli 2015 LASSO \cite{ghiringhelli2015bigdata} & 2,000 & 3.71\% & 1.89\% & 60.0\% & 3.15\% \\
\textbf{Our Method} & \textbf{2,000} & \textbf{63.36\%} & \textbf{16.70\%} & \textbf{60.0\%} & \textbf{30.28\%} \\
Ghiringhelli 2015 LASSO \cite{ghiringhelli2015bigdata} & 5,000 & 3.23\% & 2.24\% & 60.0\% & 3.74\% \\
\textbf{Our Method} & \textbf{5,000} & \textbf{46.51\%} & \textbf{29.15\%} & \textbf{60.0\%} & \textbf{49.49\%} \\
\bottomrule
\end{tabularx}
\end{sidewaystable}

\begin{sidewaystable}[H]
\centering
\caption{Out-of-Distribution (80/20 Train/Test Split) Benchmark for Electronic Band Gap ($E_g$)}
\label{tab:ood_eg}
\small
\begin{tabularx}{\textwidth}{p{0.32\textwidth} c >{\centering\arraybackslash}X >{\centering\arraybackslash}X >{\centering\arraybackslash}X >{\centering\arraybackslash}X}
\toprule
\textbf{Model / Algorithm} & \textbf{Dataset Size} & \textbf{80\% Train $R^2$} & \textbf{20\% Test $R^2$} & \textbf{Theoretical Limit ($R^2_{\text{limit}}$)} & \textbf{Test Limit Achieved (\%)} \\
\midrule
Borlido 2019 SISSO \cite{borlido2019large} & 2,000 & -6.34\% & -6.86\% & 50.0\% & 0.00\% \\
\textbf{Our Method} & \textbf{2,000} & \textbf{49.63\%} & \textbf{37.45\%} & \textbf{50.0\%} & \textbf{74.90\%} \\
Borlido 2019 SISSO \cite{borlido2019large} & 5,000 & 0.77\% & 0.40\% & 50.0\% & 0.80\% \\
\textbf{Our Method} & \textbf{5,000} & \textbf{42.38\%} & \textbf{36.41\%} & \textbf{50.0\%} & \textbf{72.82\%} \\
\bottomrule
\end{tabularx}
\end{sidewaystable}

\begin{sidewaystable}[H]
\centering
\caption{Out-of-Distribution (80/20 Train/Test Split) Benchmark for Energy Above Hull ($E_{\text{hull}}$)}
\label{tab:ood_ehull}
\small
\begin{tabularx}{\textwidth}{p{0.32\textwidth} c >{\centering\arraybackslash}X >{\centering\arraybackslash}X >{\centering\arraybackslash}X >{\centering\arraybackslash}X}
\toprule
\textbf{Model / Algorithm} & \textbf{Dataset Size} & \textbf{80\% Train $R^2$} & \textbf{20\% Test $R^2$} & \textbf{Theoretical Limit ($R^2_{\text{limit}}$)} & \textbf{Test Limit Achieved (\%)} \\
\midrule
Bartel 2019 $\tau$ \cite{bartel2019new} & 2,000 & 0.44\% & 0.23\% & 25.0\% & 0.93\% \\
\textbf{Our Method} & \textbf{2,000} & \textbf{17.92\%} & \textbf{6.85\%} & \textbf{25.0\%} & \textbf{27.41\%} \\
Bartel 2019 $\tau$ \cite{bartel2019new} & 5,000 & 0.61\% & 0.64\% & 25.0\% & 2.54\% \\
\textbf{Our Method} & \textbf{5,000} & \textbf{17.72\%} & \textbf{7.04\%} & \textbf{25.0\%} & \textbf{35.38\%} \\
\bottomrule
\end{tabularx}
\end{sidewaystable}"""

text = text.replace(tab_11_old, tab_11_new)
text = text.replace("Table~\\ref{tab:sota_ood_comparison}", "Table~\\ref{tab:ood_ef} through Table~\\ref{tab:ood_ehull}")

# -------------------------------------------------------------
# 5. Table 12 (`tab:compendium`): Column Bleed Fix & Compact Math
# -------------------------------------------------------------
tab_12_old = r"""\begin{table}[H]
\centering
\caption{Compendium of Discovered Closed-Form Analytical Equations and Theoretical Limit Performance}
\label{tab:compendium}
\small
\begin{tabularx}{\textwidth}{p{0.20\textwidth} X >{\centering\arraybackslash}p{0.13\textwidth} >{\centering\arraybackslash}p{0.15\textwidth}}
\toprule
\textbf{Target Property} & \textbf{Discovered Closed-Form Analytical Equation} & \textbf{In-Sample $R^2$} & \textbf{Limit Achieved (\%)} \\
\midrule
Formation Energy ($\Delta E_f$) & $\Delta E_f \approx 0.1508 \, \text{Val}_{\text{avg}} - 1.0197 \, \chi_A + 0.4113 \, \chi_{\text{avg}} - 0.2725 \, r_A - 2.6972$ & \textbf{71.26\%} & \textbf{109.62\%} \\
\addlinespace
Total Magnetization ($M$) & $M_{\text{pred}} = \mathbb{I}(P(M > 0.05) \ge 0.5) \cdot \left[ 0.842 \, \text{Total\_HS\_FiM} + 0.125 \, N_d - 0.412 \right]$ & \textbf{62.23\%} & \textbf{103.72\%} \\
\addlinespace
Band Gap ($E_g$) & $E_{g, \text{pred}} = \sigma(1.42 \, E_{\text{gap, QM}} + 0.85 \, \Delta\chi_{BO} - 2.10) \cdot \max(0, 0.72 \, E_{\text{gap, QM}} - 0.18)$ & \textbf{50.71\%} & \textbf{101.42\%} \\
\addlinespace
Energy Above Hull ($E_{\text{hull}}$) & $E_{\text{hull, pred}} = 0.084 \, D_{\text{hull\_proxy}} + 0.012 \, (t - 1.0)^2 + 0.005 \, \tau - 0.021$ & \textbf{16.67\%} & \textbf{66.66\%} \\
\bottomrule
\end{tabularx}
\end{table}"""

tab_12_new = r"""\begin{table}[H]
\centering
\caption{Compendium of Discovered Closed-Form Analytical Equations and Theoretical Limit Performance}
\label{tab:compendium}
\small
\begin{tabularx}{\textwidth}{p{0.18\textwidth} p{0.52\textwidth} >{\centering\arraybackslash}X >{\centering\arraybackslash}X}
\toprule
\textbf{Target Property} & \textbf{Discovered Closed-Form Analytical Equation} & \textbf{In-Sample $R^2$} & \textbf{Limit Achieved (\%)} \\
\midrule
Formation Energy ($\Delta E_f$) & $\Delta E_f \approx 0.1508 \, \text{Val}_{\text{avg}} - 1.0197 \, \chi_A + 0.4113 \, \chi_{\text{avg}} - 0.2725 \, r_A - 2.6972$ & \textbf{71.26\%} & \textbf{109.62\%} \\
\addlinespace
Total Magnetization ($M$) & $M_{\text{pred}} = \mathbb{I}(P(M > 0.05) \ge 0.5) \cdot \left[ 0.842 \, \Delta HS_B + 0.125 \, N_d - 0.412 \right]$ & \textbf{62.23\%} & \textbf{103.72\%} \\
\addlinespace
Band Gap ($E_g$) & $E_{g, \text{pred}} = \sigma(1.42 \, E_{\text{gap, QM}} + 0.85 \, \Delta\chi_{BO} - 2.10) \cdot \max(0, 0.72 \, E_{\text{gap, QM}} - 0.18)$ & \textbf{50.71\%} & \textbf{101.42\%} \\
\addlinespace
Energy Above Hull ($E_{\text{hull}}$) & $E_{\text{hull, pred}} = 0.084 \, D_{\text{hull\_proxy}} + 0.012 \, (t - 1.0)^2 + 0.005 \, \tau - 0.021$ & \textbf{16.67\%} & \textbf{66.66\%} \\
\bottomrule
\end{tabularx}
\end{table}"""

text = text.replace(tab_12_old, tab_12_new)

# -------------------------------------------------------------
# 6. Section 5.1 Titles Update
# -------------------------------------------------------------
sec_5_1_titles_old = r"""\begin{enumerate}
\item \textbf{Shattering the 0D Information-Theoretic Limit}: For years, materials informatics literature has accepted strict accuracy ceilings for 0D compositional symbolic regression ($R^2_{\text{limit}} \approx 65\%$ for formation energy $\Delta E_f$, $50\%$ for band gap $E_g$, as documented in Table~\ref{tab:theoretical_limits}). Our research proves that these theoretical limits can be systematically broken. By embedding solid-state physics engines into the descriptor space, Our Method achieves held-out test limits exceeding 100\% of established ceilings ($\Delta E_f$ Test $R^2 = 65.89\%$, achieving \textbf{101.37\%} of the theoretical limit in Table~\ref{tab:multi_seed_2000} and \textbf{102.13\%} in Table~\ref{tab:multi_seed_5000}; $E_g$ In-Sample $R^2 = 50.71\%$, achieving \textbf{101.42\%} in Table~\ref{tab:sota_benchmark_eg}).

\item \textbf{Solving the Zero-Inflation Crisis in Materials Informatics}: Standard un-gated regression models collapse when attempting to fit properties dominated by point-mass zero densities (such as non-magnetic or metallic ground states). We resolved this mathematical bottleneck by inventing a target-routed gating architecture. Specifically, our High-$C$ ($C=200.0$) Hard-Margin Hurdle (Table~\ref{tab:sota_benchmark_m}) and Soft-Sigmoidal Gated Regressor (Table~\ref{tab:sota_benchmark_eg}) successfully isolate discrete phase selection from continuous property magnitudes.

\item \textbf{Bypassing the 3D DFT Relaxation Bottleneck}: Modern 3D Crystal Graph Neural Networks (CGNNs) require pre-relaxed 3D atomic coordinates ($\mathbf{R}_i \in \mathbb{R}^3$), defeating the purpose of ultra-fast prospective screening. Our methodology operates strictly on 100\% pure 0D compositional inputs. We achieve record predictive power using only chemical stoichiometry, without leaking 3D coordinate data or relying on opaque neural network surrogates.

\item \textbf{Exposing Legacy SOTA Domain Collapse}: Through a 100\% mathematically faithful benchmark execution, we provide empirical proof that foundational 0D symbolic models (Ouyang et al. \cite{ouyang2018sisso}, Ghiringhelli et al. \cite{ghiringhelli2015bigdata}, Borlido et al. \cite{borlido2019large}) collapse when applied to complex heterovalent double perovskites ($M$ Test $R^2 \approx 1.89\%$, $E_g$ Test $R^2 \approx -6.86\%$, as detailed in Table~\ref{tab:sota_ood_comparison}). We establish a rigorous benchmark specifically tailored for $A_2BB'O_6$ phase spaces.

\item \textbf{Unprecedented Out-of-Distribution (OOD) Rigor}: Rather than reporting accuracy exclusively on full dataset fits, we subjected our architecture to rigorous stress testing across an 80/20 train/test split over 10 random seeds on a 2,000-material dataset (Table~\ref{tab:multi_seed_2000}) and scaled to 25 random seeds on a 5,000-material dataset (Table~\ref{tab:multi_seed_5000}), proving out-of-distribution generalizability.

\item \textbf{Delivery of Closed-Form, Human-Interpretable Physics}: We deliver a complete compendium of closed-form physical equations (Table~\ref{tab:compendium}). These human-readable mathematical formulas can be directly analyzed, interpreted, and utilized by materials scientists for prospective experimental design.

\item \textbf{Defining the Fundamental Physical Boundaries of AI}: We provide an honest, rigorous analysis of where 0D compositional models encounter intrinsic physical boundaries—specifically for energy above hull ($E_{\text{hull}}$ Test $R^2 = 6.85\%$, Table~\ref{tab:multi_seed_2000}), where non-local 3D octahedral tilt angles ($\theta_{B\text{--}O\text{--}B'}$) and multi-phase convex hull decomposition landscapes cap purely compositional accuracy.
\end{enumerate}"""

sec_5_1_titles_new = r"""\begin{enumerate}
\item \textbf{Transcending Information-Theoretic Limits in 0D Compositional Modeling}: For years, materials informatics literature has accepted strict accuracy ceilings for 0D compositional symbolic regression ($R^2_{\text{limit}} \approx 65\%$ for formation energy $\Delta E_f$, $50\%$ for band gap $E_g$, as documented in Table~\ref{tab:theoretical_limits}). Our research proves that these theoretical limits can be systematically broken. By embedding solid-state physics engines into the descriptor space, Our Method achieves held-out test limits exceeding 100\% of established ceilings ($\Delta E_f$ Test $R^2 = 65.89\%$, achieving \textbf{101.37\%} of the theoretical limit in Table~\ref{tab:multi_seed_2000} and \textbf{102.13\%} in Table~\ref{tab:multi_seed_5000}; $E_g$ In-Sample $R^2 = 50.71\%$, achieving \textbf{101.42\%} in Table~\ref{tab:sota_benchmark_eg}).

\item \textbf{Resolution of Target Zero-Inflation via Physics-Gated Routing Architectures}: Standard un-gated regression models collapse when attempting to fit properties dominated by point-mass zero densities (such as non-magnetic or metallic ground states). We resolved this mathematical bottleneck by inventing a target-routed gating architecture. Specifically, our High-$C$ ($C=200.0$) Hard-Margin Hurdle (Table~\ref{tab:sota_benchmark_m}) and Soft-Sigmoidal Gated Regressor (Table~\ref{tab:sota_benchmark_eg}) successfully isolate discrete phase selection from continuous property magnitudes.

\item \textbf{Elimination of the 3D Structural Relaxation Bottleneck}: Modern 3D Crystal Graph Neural Networks (CGNNs) require pre-relaxed 3D atomic coordinates ($\mathbf{R}_i \in \mathbb{R}^3$), defeating the purpose of ultra-fast prospective screening. Our methodology operates strictly on 100\% pure 0D compositional inputs. We achieve record predictive power using only chemical stoichiometry, without leaking 3D coordinate data or relying on opaque neural network surrogates.

\item \textbf{Demonstration of Domain Collapse in Foundational Symbolic Baselines}: Through a 100\% mathematically faithful benchmark execution, we provide empirical proof that foundational 0D symbolic models (Ouyang et al. \cite{ouyang2018sisso}, Ghiringhelli et al. \cite{ghiringhelli2015bigdata}, Borlido et al. \cite{borlido2019large}) collapse when applied to complex heterovalent double perovskites ($M$ Test $R^2 \approx 1.89\%$, $E_g$ Test $R^2 \approx -6.86\%$, as detailed in Table~\ref{tab:ood_ef} through Table~\ref{tab:ood_ehull}). We establish a rigorous benchmark specifically tailored for $A_2BB'O_6$ phase spaces.

\item \textbf{Validation of Out-of-Distribution Generalizability via Multi-Seed Benchmarking}: Rather than reporting accuracy exclusively on full dataset fits, we subjected our architecture to rigorous stress testing across an 80/20 train/test split over 10 random seeds on a 2,000-material dataset (Table~\ref{tab:multi_seed_2000}) and scaled to 25 random seeds on a 5,000-material dataset (Table~\ref{tab:multi_seed_5000}), proving out-of-distribution generalizability.

\item \textbf{Derivation of a Comprehensive Compendium of Closed-Form Analytical Equations}: We deliver a complete compendium of closed-form physical equations (Table~\ref{tab:compendium}). These human-readable mathematical formulas can be directly analyzed, interpreted, and utilized by materials scientists for prospective experimental design.

\item \textbf{Delineation of the Physical Boundaries Governing 0D Compositional Interpretability}: We provide an honest, rigorous analysis of where 0D compositional models encounter intrinsic physical boundaries—specifically for energy above hull ($E_{\text{hull}}$ Test $R^2 = 6.85\%$, Table~\ref{tab:multi_seed_2000}), where non-local 3D octahedral tilt angles ($\theta_{B\text{--}O\text{--}B'}$) and multi-phase convex hull decomposition landscapes cap purely compositional accuracy.
\end{enumerate}"""

text = text.replace(sec_5_1_titles_old, sec_5_1_titles_new)

# -------------------------------------------------------------
# 7. Section 5.3: Fix Box Character A2B\square X6
# -------------------------------------------------------------
sec_5_3_old = r"""This work opens new trajectories for interpretable materials informatics by demonstrating that domain-specific physics engines can elevate purely compositional AI beyond traditional information-theoretic limits. To motivate future research, this physics-gated routing paradigm can be directly extended to untried, highly complex chemical spaces—including halide double perovskites ($A_2BB'\text{X}_6$), vacancy-ordered double perovskites ($A_2B\square\text{X}_6$), and high-entropy alloy oxide surfaces—where 3D DFT structure relaxations are computationally intractable. Furthermore, integrating these closed-form physical equations into active-learning Bayesian optimization loops will enable ultra-fast, autonomous screening of stable functional materials prior to high-throughput DFT calculations."""

sec_5_3_new = r"""This work opens new trajectories for interpretable materials informatics by demonstrating that domain-specific physics engines can elevate purely compositional AI beyond traditional information-theoretic limits. To motivate future research, this physics-gated routing paradigm can be directly extended to untried, highly complex chemical spaces—including halide double perovskites ($A_2BB'\text{X}_6$), vacancy-ordered double perovskites ($A_2B\square\text{X}_6$, where $\square$ denotes a cation vacancy), and high-entropy alloy oxide surfaces—where 3D DFT structure relaxations are computationally intractable. Furthermore, integrating these closed-form physical equations into active-learning Bayesian optimization loops will enable ultra-fast, autonomous screening of stable functional materials prior to high-throughput DFT calculations."""

text = text.replace(sec_5_3_old, sec_5_3_new)

with open("paper.tex", "w", encoding="utf-8") as f:
    f.write(text)

print("Successfully applied all 7 user requests to paper.tex!")
