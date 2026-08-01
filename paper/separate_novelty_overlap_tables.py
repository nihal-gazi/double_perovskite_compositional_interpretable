"""
separate_novelty_overlap_tables.py
===================================
Separates Section 2.4 tables into two distinct matrices:
1. Table \ref{tab:novelty_matrix} (in 2.4.1) for Novelty & Quantitative Gains (NO CITATIONS)
2. Table \ref{tab:overlap_matrix} (in 2.4.2) for Literature Overlaps & Foundations (WITH CITATIONS)
"""

with open("paper.tex", "r", encoding="utf-8") as f:
    text = f.read()

old_sec_2_4 = r"""\subsection{Methodological Novelty vs. Literature Overlap}

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

new_sec_2_4 = r"""\subsection{Methodological Novelty vs. Literature Overlap}

\subsubsection{Methodological Novelty and Quantitative Improvements}
Our Method introduces six fundamental architectural innovations specifically engineered to overcome the information-theoretic ceilings of 0D compositional models. Table~\ref{tab:novelty_matrix} summarizes these methodological novelties and their quantitative performance gains over standard 0D baselines.

\begin{table}[H]
\centering
\caption{Methodological Novelty and Architectural Innovation Matrix}
\label{tab:novelty_matrix}
\small
\begin{tabularx}{\textwidth}{p{0.25\textwidth} X >{\centering\arraybackslash}p{0.25\textwidth}}
\toprule
\textbf{Pipeline Module} & \textbf{Our Methodological Novelty} & \textbf{Quantitative Baseline Gain} \\
\midrule
0D Descriptor Ingestion & Pure 0D composition processing without 3D atomic coordinates or GNN surrogates & Leakage-free 0D screening \\
Quantum Physics Engine & First integration of Harrison tight-binding gap ($E_{\text{gap, QM}}$) into 0D ML descriptor space & $E_g R^2$: $6.41\% \to 28.40\%$ \\
Elastic Strain Engine & Birch-Murnaghan lattice steric strain proxy ($(t - 1.0)^2$) for 0D volumetric stress & $\Delta E_f R^2$: $55.40\% \to 61.80\%$ \\
Tie-Line Hull Proxy Engine & Single-perovskite decomposition tie-line proxy ($D_{\text{hull\_proxy}}$) for $A_2BB'O_6$ & $E_{\text{hull}} R^2$: $0.50\% \to 16.67\%$ \\
Magnetization Router & High-$C$ ($C=200.0$) Hard-Margin Hurdle resolving zero-inflation density spikes & $M R^2$: $2.10\% \to 62.23\%$ \\
Band Gap Router & Differentiable Soft-Sigmoidal Gated Regressor restoring derivative continuity & $E_g R^2$: $28.50\% \to 50.71\%$ \\
\bottomrule
\end{tabularx}
\end{table}

The physical rationale behind each novel module is detailed below:
\begin{enumerate}
\item \textbf{Harrison Tight-Binding Quantum Gap Engine ($E_{\text{gap, QM}}$)}: Embeds solid-state quantum mechanical band gap theory \cite{harrison1999elementary, zaanen1985band} into 0D descriptor space, elevating band gap $E_g R^2$ from a baseline collapse of $6.41\%$ (C0) to \textbf{$28.40\%$} (C1) as documented in Table~\ref{tab:ablation_study}.
\item \textbf{Birch-Murnaghan Lattice Elastic Strain Engine ($(t - 1.0)^2$)}: Captures steric polyhedral strain energy \cite{goldschmidt1926gesetze, woodward1997octahedral}, boosting formation energy $\Delta E_f R^2$ from $55.40\%$ to \textbf{$61.80\%$} (Table~\ref{tab:ablation_study}).
\item \textbf{Single-Perovskite Competing Phase Tie-Line Proxy ($D_{\text{hull\_proxy}}$)}: Models sub-perovskite decomposition pathways ($A_2BB'O_6 \rightarrow ABO_3 + A'B'O_3$) \cite{sun2016thermodynamic, yamashita2018band}, rescuing energy above hull $E_{\text{hull}} R^2$ from $0.50\%$ (C2) to \textbf{$16.67\%$} (Table~\ref{tab:ablation_study}).
\item \textbf{Octahedral $d^0/d^{10}$ Closed-Shell Engine}: Quantifies crystal field orbital splitting ($\mathcal{O}_h$) stabilization \cite{goodenough1971magnetism, walsh2011design}, driving $E_g R^2$ to \textbf{$36.50\%$} (Table~\ref{tab:ablation_study}).
\item \textbf{High-$C$ ($C=200.0$) Hard-Margin Hurdle Model}: Enforces a strict, high-penalty decision boundary isolating non-magnetic ($M \le 0.05\ \mu_B$) ground states \cite{goodenough1955theory, kanamori1959superexchange}, solving magnetization zero-inflation and elevating $M R^2$ from $2.10\%$ to \textbf{$62.23\%$} (Table~\ref{tab:sota_benchmark_m}).
\item \textbf{Soft-Sigmoidal Gated Regressor}: Restores continuous order-parameter derivatives across metallic/semiconducting phase boundaries \cite{borlido2019large}, pushing $E_g R^2$ to \textbf{$50.71\%$} (Table~\ref{tab:sota_benchmark_eg}).
\end{enumerate}

\subsubsection{Methodological Overlaps and Prior Literature Basis}
Our architecture builds upon and integrates several foundational principles established in prior condensed matter literature, as summarized in Table~\ref{tab:overlap_matrix}.

\begin{table}[H]
\centering
\caption{Prior Literature Foundations and Methodological Overlap Matrix}
\label{tab:overlap_matrix}
\small
\begin{tabularx}{\textwidth}{p{0.24\textwidth} p{0.36\textwidth} X}
\toprule
\textbf{Pipeline Component} & \textbf{Pre-Existing Literature Basis} & \textbf{Literature Citation} \\
\midrule
0D Atomic Descriptors & Shannon ionic radii and Pauling electronegativities & Shannon \cite{shannon1976revised}, Ouyang et al. \cite{ouyang2018sisso} \\
Lattice Geometry & Goldschmidt tolerance factor ($t$) for octahedral tilting & Goldschmidt \cite{goldschmidt1926gesetze} \\
Perovskite Stability & Bartel tolerance factor ($\tau$) for oxide stability & Bartel et al. \cite{bartel2019new, bartel2019sciadv} \\
Symbolic Feature Selection & $L_1$-LASSO coordinate descent and OMP screening & Ghiringhelli et al. \cite{ghiringhelli2015bigdata}, Ouyang et al. \cite{ouyang2018sisso} \\
Solid-State Electronic Theory & Tight-binding orbital transfer matrices and ZSA insulator theory & Harrison \cite{harrison1999elementary}, Zaanen et al. \cite{zaanen1985band} \\
Superexchange Magnetism & $180^\circ$ cation-anion-cation orbital coupling rules & Goodenough \cite{goodenough1955theory}, Kanamori \cite{kanamori1959superexchange} \\
\bottomrule
\end{tabularx}
\end{table}"""

text = text.replace(old_sec_2_4, new_sec_2_4)

with open("paper.tex", "w", encoding="utf-8") as f:
    f.write(text)

print("Successfully separated Novelty matrix (no citations) and Overlap matrix (with citations) in Section 2.4!")
