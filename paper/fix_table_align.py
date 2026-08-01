with open("paper.tex", "r", encoding="utf-8") as f:
    text = f.read()

text = text.replace(
    r"\begin{tabularx}{\textwidth}{p{0.28\textwidth} c c c c c c}",
    r"\begin{tabularx}{\textwidth}{p{0.25\textwidth} c c c c c}"
)

text = text.replace(
    r"\begin{tabularx}{\textwidth}{p{0.28\textwidth} c c c c c}",
    r"\begin{tabularx}{\textwidth}{p{0.25\textwidth} c c c c}"
)

text = text.replace(
    r"\begin{tabularx}{\textwidth}{p{0.24\textwidth} p{0.22\textwidth} c c c c c}",
    r"\begin{tabularx}{\textwidth}{p{0.25\textwidth} p{0.22\textwidth} c c c c c}"
)

with open("paper.tex", "w", encoding="utf-8") as f:
    f.write(text)

print("Fixed table column alignment in paper.tex")
