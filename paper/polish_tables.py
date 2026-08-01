with open("paper.tex", "r", encoding="utf-8") as f:
    text = f.read()

# Refine Table 3.1 spec for 7 columns to fit page width
old_tab_31 = r"\begin{tabularx}{\textwidth}{p{0.22\textwidth} p{0.22\textwidth} c >{\centering\arraybackslash}X >{\centering\arraybackslash}X >{\centering\arraybackslash}X >{\centering\arraybackslash}X}"
new_tab_31 = r"\begin{tabularx}{\textwidth}{p{0.18\textwidth} p{0.18\textwidth} c c c c c}"
text = text.replace(old_tab_31, new_tab_31)

with open("paper.tex", "w", encoding="utf-8") as f:
    f.write(text)

print("Polished Table 3.1 spec in paper.tex")
