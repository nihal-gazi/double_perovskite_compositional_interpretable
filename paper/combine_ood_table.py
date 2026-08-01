"""
combine_ood_table.py
====================
Reverts the rotated sidewaystable OOD tables back into a single combined
table (Table \ref{tab:sota_ood_comparison}) with compact column widths.
"""

with open("paper.tex", "r", encoding="utf-8") as f:
    text = f.read()

# Replace the rotated sidewaystable section and its text reference
old_block = r"""To ensure complete visual clarity and eliminate horizontal table overcrowding, Table~\ref{tab:ood_ef} through Table~\ref{tab:ood_ehull} present the rotated property-by-property Out-of-Distribution (80/20 Train/Test Split) benchmark evaluations comparing Literature SOTA algorithms against Our Method across both the 2,000 and 5,000 datasets.

\begin{sidewaystable}[htbp]
\centering
\caption{Out-of-Distribution (80/20 Train/Test Split) Benchmark for Formation Energy ($\Delta E_f$)}
\label{tab:ood_ef}
\small
\begin{tabularx}{\textheight}{p{0.28\textheight} c >{\centering\arraybackslash}X >{\centering\arraybackslash}X >{\centering\arraybackslash}X >{\centering\arraybackslash}X}
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

\begin{sidewaystable}[htbp]
\centering
\caption{Out-of-Distribution (80/20 Train/Test Split) Benchmark for Total Magnetization ($M$)}
\label{tab:ood_m}
\small
\begin{tabularx}{\textheight}{p{0.28\textheight} c >{\centering\arraybackslash}X >{\centering\arraybackslash}X >{\centering\arraybackslash}X >{\centering\arraybackslash}X}
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

\begin{sidewaystable}[htbp]
\centering
\caption{Out-of-Distribution (80/20 Train/Test Split) Benchmark for Electronic Band Gap ($E_g$)}
\label{tab:ood_eg}
\small
\begin{tabularx}{\textheight}{p{0.28\textheight} c >{\centering\arraybackslash}X >{\centering\arraybackslash}X >{\centering\arraybackslash}X >{\centering\arraybackslash}X}
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

\begin{sidewaystable}[htbp]
\centering
\caption{Out-of-Distribution (80/20 Train/Test Split) Benchmark for Energy Above Hull ($E_{\text{hull}}$)}
\label{tab:ood_ehull}
\small
\begin{tabularx}{\textheight}{p{0.28\textheight} c >{\centering\arraybackslash}X >{\centering\arraybackslash}X >{\centering\arraybackslash}X >{\centering\arraybackslash}X}
\toprule
\textbf{Model / Algorithm} & \textbf{Dataset Size} & \textbf{80\% Train $R^2$} & \textbf{20\% Test $R^2$} & \textbf{Theoretical Limit ($R^2_{\text{limit}}$)} & \textbf{Test Limit Achieved (\%)} \\
\midrule
Bartel 2019 $\tau$ \cite{bartel2019new} & 2,000 & 0.44\% & 0.23\% & 25.0\% & 0.93\% \\
\textbf{Our Method} & \textbf{2,000} & \textbf{17.92\%} & \textbf{6.85\%} & \textbf{25.0\%} & \textbf{27.41\%} \\
Bartel 2019 $\tau$ \cite{bartel2019new} & 5,000 & 0.61\% & 0.64\% & 25.0\% & 2.54\% \\
\textbf{Our Method} & \textbf{5,000} & \textbf{17.72\%} & \textbf{7.04\%} & \textbf{25.0\%} & \textbf{35.38\%} \\
\bottomrule
\end{tabularx}
\end{sidewaystable}

As demonstrated in Table~\ref{tab:ood_ef} through Table~\ref{tab:ood_ehull}, published literature SOTA baselines experience severe out-of-distribution collapse on double perovskites, whereas Our Method achieves a massive predictive advantage across all targets on held-out test splits."""

new_block = r"""To rigorously quantify generalizability against published literature baselines under held-out evaluation, Table~\ref{tab:sota_ood_comparison} compares the 80/20 train/test split performance of literature SOTA algorithms against Our Method across both datasets.

\begin{table}[H]
\centering
\caption{Direct Out-of-Distribution (80/20 Train/Test Split) Performance Comparison: Our Method vs. SOTA Baselines}
\label{tab:sota_ood_comparison}
\small
\begin{tabularx}{\textwidth}{p{0.20\textwidth} p{0.22\textwidth} c >{\centering\arraybackslash}X >{\centering\arraybackslash}X >{\centering\arraybackslash}X}
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
\end{table}

As demonstrated in Table~\ref{tab:sota_ood_comparison}, published literature SOTA baselines experience severe out-of-distribution collapse on double perovskites, whereas Our Method achieves a massive predictive advantage across all targets on held-out test splits."""

text = text.replace(old_block, new_block)

# Also fix Section 5.1 reference if needed
text = text.replace("Table~\\ref{tab:ood_ef} through Table~\\ref{tab:ood_ehull}", "Table~\\ref{tab:sota_ood_comparison}")

with open("paper.tex", "w", encoding="utf-8") as f:
    f.write(text)

print("Successfully combined OOD table into Table \\ref{tab:sota_ood_comparison} with shrunken first 2 columns!")
