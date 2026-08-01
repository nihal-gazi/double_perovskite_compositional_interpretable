"""
extract_paper_paragraphs.py
===========================
Extracts all narrative text paragraphs from paper.tex and saves them into contents.txt
with clear section headings for easy manual editing and paraphrasing.
"""

import re

with open("paper.tex", "r", encoding="utf-8") as f:
    latex_content = f.read()

# Lines to ignore or strip
lines = latex_content.splitlines()

output_blocks = []
current_section = "Header / Preamble"
in_abstract = False
in_table = False
in_figure = False
in_equation = False
in_enumerate = False

current_paragraph = []

def flush_paragraph(sec, para_lines):
    if not para_lines:
        return
    text = " ".join([l.strip() for l in para_lines if l.strip()])
    # Clean LaTeX inline commands for text readability
    # e.g., \textbf{x} -> x, \textit{x} -> x, \cite{...} -> [cite], \ref{...} -> [ref]
    if text:
        output_blocks.append((sec, text))

section_pattern = re.compile(r'\\(section|subsection|subsubsection)\*?\{(.*?)\}')

i = 0
while i < len(lines):
    line = lines[i].strip()

    # Abstract start/end
    if r"\begin{abstract}" in line:
        in_abstract = True
        current_section = "[Abstract]"
        i += 1
        continue
    elif r"\end{abstract}" in line:
        flush_paragraph(current_section, current_paragraph)
        current_paragraph = []
        in_abstract = False
        i += 1
        continue

    # Environments to skip (tables, figures, tikz, equations)
    if r"\begin{table}" in line or r"\begin{sidewaystable}" in line:
        flush_paragraph(current_section, current_paragraph)
        current_paragraph = []
        in_table = True
    elif r"\end{table}" in line or r"\end{sidewaystable}" in line:
        in_table = False
        i += 1
        continue

    if r"\begin{figure}" in line:
        flush_paragraph(current_section, current_paragraph)
        current_paragraph = []
        in_figure = True
    elif r"\end{figure}" in line:
        in_figure = False
        i += 1
        continue

    if r"\begin{equation}" in line or r"\begin{align}" in line or r"\[" in line:
        flush_paragraph(current_section, current_paragraph)
        current_paragraph = []
        in_equation = True
    elif r"\end{equation}" in line or r"\end{align}" in line or r"\]" in line:
        in_equation = False
        i += 1
        continue

    if in_table or in_figure or in_equation:
        i += 1
        continue

    # Detect section headers
    sec_match = section_pattern.search(line)
    if sec_match:
        flush_paragraph(current_section, current_paragraph)
        current_paragraph = []
        sec_type = sec_match.group(1)
        sec_title = sec_match.group(2).replace(r'\&', '&').replace(r'\textit', '').replace('{', '').replace('}', '')
        current_section = f"[{sec_title}]"
        i += 1
        continue

    # Skip LaTeX commands outside text (preamble, bibliography, \begin{document}, \maketitle, \toprule, \midrule, etc.)
    if line.startswith(r"\documentclass") or line.startswith(r"\usepackage") or line.startswith(r"\PassOptionsToPackage") or line.startswith(r"\journal") or line.startswith(r"\bibliographystyle") or line.startswith(r"\begin{document}") or line.startswith(r"\maketitle") or line.startswith(r"\bibliography") or line.startswith(r"\end{document}") or line.startswith(r"\begin{frontmatter}") or line.startswith(r"\end{frontmatter}") or line.startswith(r"\title") or line.startswith(r"\author") or line.startswith(r"\address") or line.startswith(r"\begin{keyword}") or line.startswith(r"\end{keyword}") or line.startswith("---") or line.startswith("%"):
        flush_paragraph(current_section, current_paragraph)
        current_paragraph = []
        i += 1
        continue

    # Blank line indicates end of paragraph
    if not line:
        flush_paragraph(current_section, current_paragraph)
        current_paragraph = []
        i += 1
        continue

    # Collect line text
    current_paragraph.append(line)
    i += 1

flush_paragraph(current_section, current_paragraph)

# Write to contents.txt
with open("contents.txt", "w", encoding="utf-8") as f:
    last_sec = None
    for sec, para in output_blocks:
        if sec == "Header / Preamble":
            continue
        if sec != last_sec:
            f.write(f"\n================================================================================\n")
            f.write(f"{sec}\n")
            f.write(f"================================================================================\n\n")
            last_sec = sec
        f.write(f"{para}\n\n")

print(f"Successfully extracted {len(output_blocks)} paragraphs into contents.txt!")
