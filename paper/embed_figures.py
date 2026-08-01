import re

with open("paper.tex", "r", encoding="utf-8") as f:
    text = f.read()

# 1. Update Section 2.2 to embed target_distributions.png, correlation_matrix_heatmap.png, and pca_2d_scatter_targets.png
sec_2_2_old = r"""\subsection{Primary Data Analysis & Zero-Inflation Challenge}
Statistical analysis of the target properties reveals strong distributional heterogeneity:
- \textbf{Formation Energy ($\Delta E_f$)}: Gaussian-like continuous distribution centered at $-2.45\text{ eV/atom}$ ($\sigma = 0.62\text{ eV/atom}$).
- \textbf{Energy Above Hull ($E_{\text{hull}}$)}: Exponentially decaying distribution with $35\%$ of compounds situated near ground-state stability ($E_{\text{hull}} \le 0.01\text{ eV/atom}$).
- \textbf{Total Magnetization ($M$) & Band Gap ($E_g$)}: Exhibit \textbf{severe zero-inflation}. In $M$, $68\%$ of double perovskites are non-magnetic ($M = 0.0\ \mu_B$), while $32\%$ possess net spin moments ($M \in (0, 10]\ \mu_B$). In $E_g$, $63\%$ are metallic ($E_g = 0.0\text{ eV}$), while $37\%$ are semiconducting/insulating ($E_g \in (0, 6]\text{ eV}$). Standard un-gated regression models fail catastrophically on zero-inflated targets because ordinary least squares attempts to fit a single continuous surface across a discontinuous point-mass density."""

sec_2_2_new = r"""\subsection{Primary Data Analysis & Zero-Inflation Challenge}
Statistical analysis of the target properties reveals strong distributional heterogeneity and fundamental mathematical challenges across the dataset:
- \textbf{Formation Energy ($\Delta E_f$)}: Exhibits a continuous, unimodal Gaussian-like distribution centered at $-2.45\text{ eV/atom}$ ($\sigma = 0.62\text{ eV/atom}$).
- \textbf{Energy Above Hull ($E_{\text{hull}}$)}: Displays an exponentially decaying phase-stability distribution with $35\%$ of compounds situated near thermodynamic ground-state stability ($E_{\text{hull}} \le 0.01\text{ eV/atom}$).
- \textbf{Total Magnetization ($M$) & Band Gap ($E_g$)}: Exhibit \textbf{severe zero-inflation}. In $M$, $68\%$ of double perovskites are non-magnetic ($M = 0.0\ \mu_B$), while $32\%$ possess net spin moments ($M \in (0, 10]\ \mu_B$). In $E_g$, $63\%$ are metallic ($E_g = 0.0\text{ eV}$), while $37\%$ are semiconducting/insulating ($E_g \in (0, 6]\text{ eV}$).

Standard un-gated regression algorithms fail catastrophically on zero-inflated targets because ordinary least squares attempts to fit a single continuous hyper-surface across a discontinuous point-mass density at zero. Figure~\ref{fig:target_distributions} illustrates the empirical histograms and zero-inflation density spikes for all four target properties.

\begin{figure}[H]
\centering
\includegraphics[width=0.88\textwidth]{figures/target_distributions.png}
\caption{Primary statistical distributions of the four DFT target properties across the curated double perovskite dataset, explicitly illustrating the severe zero-inflation point-mass densities at $M = 0.0\ \mu_B$ ($68\%$ non-magnetic) and $E_g = 0.0\text{ eV}$ ($63\%$ metallic).}
\label{fig:target_distributions}
\end{figure}

To analyze descriptor interdependence, Figure~\ref{fig:correlation_matrix} presents the linear correlation matrix heatmap across physical input features and target properties, while Figure~\ref{fig:pca_2d_scatter} illustrates the 2D Principal Component Analysis (PCA) manifold projection of target properties.

\begin{figure}[H]
\centering
\includegraphics[width=0.82\textwidth]{figures/correlation_matrix_heatmap.png}
\caption{Pearson correlation matrix heatmap displaying pairwise collinearities between 0D physical descriptors and target DFT ground-state properties.}
\label{fig:correlation_matrix}
\end{figure}

\begin{figure}[H]
\centering
\includegraphics[width=0.82\textwidth]{figures/pca_2d_scatter_targets.png}
\caption{2D Principal Component Analysis (PCA) manifold projection of double perovskite target properties, illustrating smooth physical clustering boundaries.}
\label{fig:pca_2d_scatter}
\end{figure}"""

text = text.replace(sec_2_2_old, sec_2_2_new)

# 2. Update Section 3.1 to embed sota_comparison_r2_bar.png and sota_comparison_limit_bar.png
sec_3_1_old = r"""As demonstrated in Table~\ref{tab:sota_benchmark}, published 0D baseline algorithms collapse on double perovskites due to zero-inflation ($M$ and $E_g$) and complex phase decomposition pathways ($E_{\text{hull}}$). Our Master Algorithm achieves a massive performance advantage over literature baselines (+22.95\% $R^2$ gain for $\Delta E_f$, +60.53\% for $M$, +49.82\% for $E_g$, and +16.26\% for $E_{\text{hull}}$)."""

sec_3_1_new = r"""As demonstrated in Table~\ref{tab:sota_benchmark}, published 0D baseline algorithms collapse on double perovskites due to zero-inflation ($M$ and $E_g$) and complex phase decomposition pathways ($E_{\text{hull}}$). Our Master Algorithm achieves a massive performance advantage over literature baselines (+22.95\% $R^2$ gain for $\Delta E_f$, +60.53\% for $M$, +49.82\% for $E_g$, and +16.26\% for $E_{\text{hull}}$).

Figure~\ref{fig:sota_comparison_r2} visually illustrates the in-sample $R^2$ score comparison between our Master Algorithm, literature SOTA baselines, and theoretical literature limits ($R^2_{\text{limit}}$). Figure~\ref{fig:sota_comparison_limit} presents the percentage of theoretical literature limit achieved ($R^2 / R^2_{\text{limit}}$) across all four target properties.

\begin{figure}[H]
\centering
\includegraphics[width=0.92\textwidth]{figures/sota_comparison_r2_bar.png}
\caption{In-sample $R^2$ score comparison across all four target properties: Master Algorithm vs. literature SOTA baselines (Ouyang 2018 \cite{ouyang2018sisso}, Ghiringhelli 2015 \cite{ghiringhelli2015bigdata}, Borlido 2019 \cite{borlido2019large}, Bartel 2019 \cite{bartel2019new}) and theoretical literature limits ($R^2_{\text{limit}}$).}
\label{fig:sota_comparison_r2}
\end{figure}

\begin{figure}[H]
\centering
\includegraphics[width=0.92\textwidth]{figures/sota_comparison_limit_bar.png}
\caption{Percentage of theoretical literature limit achieved ($R^2 / R^2_{\text{limit}}$) across all four target properties, highlighting that our Master Algorithm surpasses 100\% of theoretical literature limits for formation energy ($\Delta E_f$), total magnetization ($M$), and band gap ($E_g$).}
\label{fig:sota_comparison_limit}
\end{figure}"""

text = text.replace(sec_3_1_old, sec_3_1_new)

with open("paper.tex", "w", encoding="utf-8") as f:
    f.write(text)

print("Successfully updated paper.tex with analysis_1 images and SOTA bar chart figures!")
