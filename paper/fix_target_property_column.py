"""
fix_target_property_column.py
=============================
Fixes target property column width and multirow wrapping in Table 8 (tab:sota_ood_comparison),
and removes duplicate introductory text.
"""

with open("paper.tex", "r", encoding="utf-8") as f:
    text = f.read()

# Remove duplicate intro paragraph
dup_text = r"""To rigorously quantify generalizability against published literature baselines under held-out evaluation, Table~\ref{tab:sota_ood_comparison} compares the 80/20 train/test split performance of literature SOTA algorithms against Our Method across both datasets.

To rigorously quantify generalizability against published literature baselines under held-out evaluation, Table~\ref{tab:sota_ood_comparison} compares the 80/20 train/test split performance of literature SOTA algorithms against Our Method across both datasets."""

single_text = r"""To rigorously quantify generalizability against published literature baselines under held-out evaluation, Table~\ref{tab:sota_ood_comparison} compares the 80/20 train/test split performance of literature SOTA algorithms against Our Method across both datasets."""

text = text.replace(dup_text, single_text)

# Fix Table 8 multirow wrapping and column width
old_table_8 = r"""\begin{table}[H]
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
\end{table}"""

new_table_8 = r"""\begin{table}[H]
\centering
\caption{Direct Out-of-Distribution (80/20 Train/Test Split) Performance Comparison: Our Method vs. SOTA Baselines}
\label{tab:sota_ood_comparison}
\small
\begin{tabularx}{\textwidth}{p{0.25\textwidth} p{0.25\textwidth} c >{\centering\arraybackslash}X >{\centering\arraybackslash}X >{\centering\arraybackslash}X}
\toprule
\textbf{Target Property} & \textbf{Model / Algorithm} & \textbf{Dataset} & \textbf{80\% Train $R^2$} & \textbf{20\% Test $R^2$} & \textbf{Test Limit (\%)} \\
\midrule
\multirow{4}{0.24\textwidth}{\raggedright \textbf{Formation Energy} ($\Delta E_f$)} & Ouyang 2018 SISSO \cite{ouyang2018sisso} & 2,000 & 48.33\% & 48.26\% & 74.24\% \\
 & \textbf{Our Method} & \textbf{2,000} & \textbf{72.14\%} & \textbf{65.89\%} & \textbf{101.37\%} \\
 & Ouyang 2018 SISSO \cite{ouyang2018sisso} & 5,000 & 48.67\% & 49.09\% & 75.53\% \\
 & \textbf{Our Method} & \textbf{5,000} & \textbf{70.10\%} & \textbf{66.36\%} & \textbf{102.13\%} \\
\midrule
\multirow{4}{0.24\textwidth}{\raggedright \textbf{Total Magnetization} ($M$)} & Ghiringhelli 2015 LASSO \cite{ghiringhelli2015bigdata} & 2,000 & 3.71\% & 1.89\% & 3.15\% \\
 & \textbf{Our Method} & \textbf{2,000} & \textbf{63.36\%} & \textbf{16.70\%} & \textbf{30.28\%} \\
 & Ghiringhelli 2015 LASSO \cite{ghiringhelli2015bigdata} & 5,000 & 3.23\% & 2.24\% & 3.74\% \\
 & \textbf{Our Method} & \textbf{5,000} & \textbf{46.51\%} & \textbf{29.15\%} & \textbf{49.49\%} \\
\midrule
\multirow{4}{0.24\textwidth}{\raggedright \textbf{Band Gap} ($E_g$)} & Borlido 2019 SISSO \cite{borlido2019large} & 2,000 & -6.34\% & -6.86\% & 0.00\% \\
 & \textbf{Our Method} & \textbf{2,000} & \textbf{49.63\%} & \textbf{37.45\%} & \textbf{74.90\%} \\
 & Borlido 2019 SISSO \cite{borlido2019large} & 5,000 & 0.77\% & 0.40\% & 0.80\% \\
 & \textbf{Our Method} & \textbf{5,000} & \textbf{42.38\%} & \textbf{36.41\%} & \textbf{72.82\%} \\
\midrule
\multirow{4}{0.24\textwidth}{\raggedright \textbf{Energy Above Hull} ($E_{\text{hull}}$)} & Bartel 2019 $\tau$ \cite{bartel2019new} & 2,000 & 0.44\% & 0.23\% & 0.93\% \\
 & \textbf{Our Method} & \textbf{2,000} & \textbf{17.92\%} & \textbf{6.85\%} & \textbf{27.41\%} \\
 & Bartel 2019 $\tau$ \cite{bartel2019new} & 5,000 & 0.61\% & 0.64\% & 2.54\% \\
 & \textbf{Our Method} & \textbf{5,000} & \textbf{17.72\%} & \textbf{7.04\%} & \textbf{35.38\%} \\
\bottomrule
\end{tabularx}
\end{table}"""

text = text.replace(old_table_8, new_table_8)

with open("paper.tex", "w", encoding="utf-8") as f:
    f.write(text)

print("Fixed target property column width and multirow text wrapping in Table 8!")
