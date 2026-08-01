with open("paper.tex", "r", encoding="utf-8") as f:
    text = f.read()

# Replace Table 3.1 (tab:sota_benchmark)
old_tab_31 = r"\begin{tabularx}{\textwidth}{p{0.25\textwidth} p{0.22\textwidth} c c c c c}"
new_tab_31 = r"\begin{tabularx}{\textwidth}{p{0.24\textwidth} p{0.22\textwidth} >{\centering\arraybackslash}X >{\centering\arraybackslash}X >{\centering\arraybackslash}X >{\centering\arraybackslash}X}"
text = text.replace(old_tab_31, new_tab_31)

# Replace Table 5 (tab:multi_seed_2000)
old_tab_5 = r"\begin{tabularx}{\textwidth}{p{0.25\textwidth} c c c c c}"
new_tab_5 = r"\begin{tabularx}{\textwidth}{p{0.26\textwidth} >{\centering\arraybackslash}X >{\centering\arraybackslash}X >{\centering\arraybackslash}X >{\centering\arraybackslash}X >{\centering\arraybackslash}X}"
text = text.replace(old_tab_5, new_tab_5)

# Replace Table 6 (tab:multi_seed_5000)
old_tab_6 = r"\begin{tabularx}{\textwidth}{p{0.25\textwidth} c c c c c}"
new_tab_6 = r"\begin{tabularx}{\textwidth}{p{0.26\textwidth} >{\centering\arraybackslash}X >{\centering\arraybackslash}X >{\centering\arraybackslash}X >{\centering\arraybackslash}X >{\centering\arraybackslash}X}"
text = text.replace(old_tab_6, new_tab_6)

# Fix duplicate labels if any
text = text.replace(r"\caption{10-Seed 80/20 Train/Test Benchmark Summary on the 2,000 Dataset (Mean $\pm$ Std)}" + "\n" + r"\label{tab:multi_seed_2000}",
                    r"\caption{10-Seed 80/20 Train/Test Benchmark Summary on the 2,000 Dataset (Mean $\pm$ Std)}" + "\n" + r"\label{tab:multi_seed_2000_summary}")

with open("paper.tex", "w", encoding="utf-8") as f:
    f.write(text)

print("Updated table column types and labels in paper.tex")
