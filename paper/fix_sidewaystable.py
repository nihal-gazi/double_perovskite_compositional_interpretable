"""
fix_sidewaystable.py
====================
Fixes sidewaystable specifiers and text width in paper.tex.
"""

with open("paper.tex", "r", encoding="utf-8") as f:
    text = f.read()

# Replace \begin{sidewaystable}[H] with \begin{sidewaystable}[htbp]
text = text.replace(r"\begin{sidewaystable}[H]", r"\begin{sidewaystable}[htbp]")

# Inside sidewaystable, change \begin{tabularx}{\textwidth} to \begin{tabularx}{\textheight}
# so it expands along the full landscape height (30cm)
old_sideways_block = r"""\begin{sidewaystable}[htbp]
\centering
\caption{Out-of-Distribution (80/20 Train/Test Split) Benchmark for Formation Energy ($\Delta E_f$)}
\label{tab:ood_ef}
\small
\begin{tabularx}{\textwidth}{p{0.32\textwidth} c >{\centering\arraybackslash}X >{\centering\arraybackslash}X >{\centering\arraybackslash}X >{\centering\arraybackslash}X}"""

new_sideways_block = r"""\begin{sidewaystable}[htbp]
\centering
\caption{Out-of-Distribution (80/20 Train/Test Split) Benchmark for Formation Energy ($\Delta E_f$)}
\label{tab:ood_ef}
\small
\begin{tabularx}{\textheight}{p{0.32\textheight} c >{\centering\arraybackslash}X >{\centering\arraybackslash}X >{\centering\arraybackslash}X >{\centering\arraybackslash}X}"""

text = text.replace(r"\begin{tabularx}{\textwidth}{p{0.32\textwidth} c >{\centering\arraybackslash}X >{\centering\arraybackslash}X >{\centering\arraybackslash}X >{\centering\arraybackslash}X}",
                    r"\begin{tabularx}{\textheight}{p{0.28\textheight} c >{\centering\arraybackslash}X >{\centering\arraybackslash}X >{\centering\arraybackslash}X >{\centering\arraybackslash}X}")

with open("paper.tex", "w", encoding="utf-8") as f:
    f.write(text)

print("Fixed sidewaystable specifier and textheight!")
