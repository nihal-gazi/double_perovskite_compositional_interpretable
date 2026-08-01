"""
fix_figure_5.py
===============
Fixes TikZ flowchart arrows, alignment, and rescales Figure 5 in paper.tex.
"""

with open("paper.tex", "r", encoding="utf-8") as f:
    text = f.read()

old_fig_5 = r"""\begin{figure}[H]
\centering
\begin{tikzpicture}[
    node distance=1.2cm and 1.5cm,
    font=\sffamily\small,
    box/.style={rectangle, draw=blue!80!black, fill=blue!5, thick, rounded corners, align=center, inner sep=8pt, minimum width=3.2cm, drop shadow},
    physbox/.style={rectangle, draw=teal!80!black, fill=teal!5, thick, rounded corners, align=center, inner sep=8pt, minimum width=3.4cm, drop shadow},
    routerbox/.style={diamond, draw=orange!90!black, fill=orange!10, thick, align=center, inner sep=4pt, aspect=1.8, drop shadow},
    enginebox/.style={rectangle, draw=purple!80!black, fill=purple!5, thick, rounded corners, align=center, inner sep=8pt, minimum width=3.4cm, drop shadow},
    outbox/.style={rectangle, draw=green!60!black, fill=green!5, thick, rounded corners, align=center, inner sep=8pt, minimum width=3.2cm, drop shadow},
    arrow/.style={-Latex, thick, draw=gray!80!black}
]

% Section 1: Inputs & Lookup
\node[box] (input) {\textbf{1. 0D Chemical Input}\\Formula: $A_2BB'O_6$\\Identities: $A, A', B, B'$};
\node[physbox, right=of input] (lookup) {\textbf{2. 0D Physical Lookup}\\$\chi_X, r_X, \text{Val}_X, N_d, HS_B$\\$\Delta H_{\text{ox}}, IE_X, EA_X, \mathcal{M}_X$};

% Section 2: Physics Engines
\node[physbox, below=1.0cm of lookup] (physics) {\textbf{3. Quantum Physics Engines}\\Harrison Gap: $E_{\text{gap, QM}}$\\Birch-Murnaghan Strain\\Tie-Line Proxy: $D_{\text{hull\_proxy}}$\\Closed-Shell $d^0/d^{10}$ Engine};

% Section 3: Target Router
\node[routerbox, below=1.0cm of physics] (router) {\textbf{Target Router}\\\textit{Property?}};

% Section 4: Engines
\node[enginebox, left=2.2cm of router] (ef_engine) {\textbf{Direct Multi-Operator}\\\text{Analytical Regressor}\\$(\Delta E_f)$};
\node[enginebox, below left=1.2cm and 0.8cm of router] (m_engine) {\textbf{High-$C$ Hard-Margin}\\\text{Hurdle Classifier + Reg.}\\$(M)$};
\node[enginebox, below right=1.2cm and 0.8cm of router] (eg_engine) {\textbf{Soft-Sigmoidal Gated}\\\text{Continuous Regressor}\\$(E_g)$};
\node[enginebox, right=2.2cm of router] (ehull_engine) {\textbf{Single-Perovskite}\\\text{Tie-Line Convex Model}\\$(E_{\text{hull}})$};

% Section 5: Outputs
\node[outbox, below=3.5cm of router, minimum width=307pt] (outputs) {\textbf{Discovered Analytical Equations \& Benchmarks}\\$\Delta E_f$: $R^2 = 71.26\%$ ($109.62\%$ Limit) \quad $M$: $R^2 = 62.23\%$ ($103.72\%$ Limit)\\$E_g$: $R^2 = 50.71\%$ ($101.42\%$ Limit) \quad $E_{\text{hull}}$: $R^2 = 16.67\%$ ($66.66\%$ Limit)};

% Arrows
\draw[arrow] (input) -- (lookup);
\draw[arrow] (lookup) -- (physics);
\draw[arrow] (physics) -- (router);
\draw[arrow] (router) |- (m_engine);
\draw[arrow] (router) |- (eg_engine);
\draw[arrow, arrows=-Latex] (router.east) -| (ehull_engine.west);
\draw[arrow, arrows=Latex-] (ef_engine.east) -| (router.west);
\draw[arrow] (ef_engine) |- (outputs);
\draw[arrow] (m_engine) -- (outputs);
\draw[arrow] (eg_engine) -- (outputs);
\draw[arrow] (ehull_engine) |- (outputs);

\end{tikzpicture}
\caption{Overall algorithmic architecture of the Master Physics-Gated Double Perovskite Machine Learning Pipeline, showing 0D input ingestion, physics engine expansion, property-specific routing, and final analytical equation outputs.}
\label{fig:architecture_flowchart}
\end{figure}"""

new_fig_5 = r"""\begin{figure}[H]
\centering
\resizebox{0.96\textwidth}{!}{%
\begin{tikzpicture}[
    node distance=1.0cm and 1.2cm,
    font=\sffamily\small,
    box/.style={rectangle, draw=blue!80!black, fill=blue!5, thick, rounded corners, align=center, inner sep=6pt, minimum width=3.2cm, drop shadow},
    physbox/.style={rectangle, draw=teal!80!black, fill=teal!5, thick, rounded corners, align=center, inner sep=6pt, minimum width=3.4cm, drop shadow},
    routerbox/.style={diamond, draw=orange!90!black, fill=orange!10, thick, align=center, inner sep=4pt, aspect=1.8, drop shadow},
    enginebox/.style={rectangle, draw=purple!80!black, fill=purple!5, thick, rounded corners, align=center, inner sep=6pt, minimum width=3.2cm, drop shadow},
    outbox/.style={rectangle, draw=green!60!black, fill=green!5, thick, rounded corners, align=center, inner sep=8pt, minimum width=13.5cm, drop shadow},
    arrow/.style={-Latex, thick, draw=gray!80!black}
]

% Section 1: Inputs & Physical Lookup
\node[box] (input) {\textbf{1. 0D Chemical Input}\\Formula: $A_2BB'O_6$\\Identities: $A, A', B, B'$};
\node[physbox, right=1.2cm of input] (lookup) {\textbf{2. 0D Physical Lookup}\\$\chi_X, r_X, \text{Val}_X, N_d, HS_B$\\$\Delta H_{\text{ox}}, IE_X, EA_X, \mathcal{M}_X$};

% Section 2: Physics Engines
\node[physbox, below=0.9cm of lookup] (physics) {\textbf{3. Quantum Physics Engines}\\Harrison Gap: $E_{\text{gap, QM}}$\\Birch-Murnaghan Strain\\Tie-Line Proxy: $D_{\text{hull\_proxy}}$\\Closed-Shell $d^0/d^{10}$ Engine};

% Section 3: Target Router
\node[routerbox, below=0.9cm of physics] (router) {\textbf{Target Router}\\\textit{Property?}};

% Section 4: Property Engines
\node[enginebox, left=1.8cm of router] (ef_engine) {\textbf{Direct Multi-Operator}\\\text{Analytical Regressor}\\$(\Delta E_f)$};
\node[enginebox, below left=1.2cm and 0.3cm of router] (m_engine) {\textbf{High-$C$ Hard-Margin}\\\text{Hurdle Classifier + Reg.}\\$(M)$};
\node[enginebox, below right=1.2cm and 0.3cm of router] (eg_engine) {\textbf{Soft-Sigmoidal Gated}\\\text{Continuous Regressor}\\$(E_g)$};
\node[enginebox, right=1.8cm of router] (ehull_engine) {\textbf{Single-Perovskite}\\\text{Tie-Line Convex Model}\\$(E_{\text{hull}})$};

% Section 5: Output Box
\node[outbox, below=3.6cm of router] (outputs) {\textbf{Discovered Analytical Equations \& Benchmarks}\\$\Delta E_f$: $R^2 = 71.26\%$ ($109.62\%$ Limit) \quad $M$: $R^2 = 62.23\%$ ($103.72\%$ Limit)\\$E_g$: $R^2 = 50.71\%$ ($101.42\%$ Limit) \quad $E_{\text{hull}}$: $R^2 = 16.67\%$ ($66.66\%$ Limit)};

% Arrow Routing
\draw[arrow] (input) -- (lookup);
\draw[arrow] (lookup) -- (physics);
\draw[arrow] (physics) -- (router);

\draw[arrow] (router.west) -- (ef_engine.east);
\draw[arrow] (router.east) -- (ehull_engine.west);
\draw[arrow] (router.south) -- ++(0,-0.4cm) -| (m_engine.north);
\draw[arrow] (router.south) -- ++(0,-0.4cm) -| (eg_engine.north);

\draw[arrow] (ef_engine.south) |- (outputs.west);
\draw[arrow] (m_engine.south) -- (m_engine.south |- outputs.north);
\draw[arrow] (eg_engine.south) -- (eg_engine.south |- outputs.north);
\draw[arrow] (ehull_engine.south) |- (outputs.east);

\end{tikzpicture}%
}
\caption{Overall algorithmic architecture of the Master Physics-Gated Double Perovskite Machine Learning Pipeline, showing 0D input ingestion, physics engine expansion, property-specific routing, and final analytical equation outputs.}
\label{fig:architecture_flowchart}
\end{figure}"""

text = text.replace(old_fig_5, new_fig_5)

with open("paper.tex", "w", encoding="utf-8") as f:
    f.write(text)

print("Successfully updated Figure 5 TikZ flowchart layout, arrow routing, and scaled box to fit textwidth!")
