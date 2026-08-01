with open("paper.tex", "r", encoding="utf-8") as f:
    text = f.read()

# Make Table 3.1 dynamically scale across text width
old_tab_31 = r"\begin{tabularx}{\textwidth}{p{0.18\textwidth} p{0.18\textwidth} c c c c c}"
new_tab_31 = r"\begin{tabularx}{\textwidth}{p{0.22\textwidth} p{0.22\textwidth} >{\centering\arraybackslash}X >{\centering\arraybackslash}X >{\centering\arraybackslash}X >{\centering\arraybackslash}X >{\centering\arraybackslash}X}"
text = text.replace(old_tab_31, new_tab_31)

with open("paper.tex", "w", encoding="utf-8") as f:
    f.write(text)

print("Dynamic X scaling applied to Table 3.1")
