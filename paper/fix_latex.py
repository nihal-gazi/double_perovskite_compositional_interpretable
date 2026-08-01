import re

with open("paper.tex", "r", encoding="utf-8") as f:
    text = f.read()

# Replace **text** with \textbf{text}
text = re.sub(r'\*\*(.*?)\*\*', r'\\textbf{\1}', text)

with open("paper.tex", "w", encoding="utf-8") as f:
    f.write(text)

print("Replaced markdown bold with LaTeX \\textbf{}")
