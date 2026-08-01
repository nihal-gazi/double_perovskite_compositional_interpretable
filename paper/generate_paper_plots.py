"""
generate_paper_plots.py
========================
Generates publication-quality bar charts comparing Our Method against
literature SOTA baselines across both 2,000 and 5,000 datasets for all
4 target properties.

Outputs:
- figures/sota_comparison_r2_bar.png (Figure 7: In-Sample R2 Comparison)
- figures/sota_comparison_limit_bar.png (Figure 8: Limit Achieved % Comparison)
"""

import os
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = 'Arial'
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['axes.edgecolor'] = '#333333'
plt.rcParams['axes.linewidth'] = 1.2

FIGURES_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "figures"))
os.makedirs(FIGURES_DIR, exist_ok=True)

targets = ['Formation Energy\n($\Delta E_f$)', 'Total Magnetization\n($M$)', 'Band Gap\n($E_g$)', 'Energy Above Hull\n($E_{\text{hull}}$)']
lit_limits = [65.0, 60.0, 50.0, 25.0]

sota_2k = [48.31, 1.70, 0.0, 0.41]
sota_5k = [48.70, 3.12, 0.89, 0.61]

our_2k = [71.26, 62.23, 50.71, 16.67]
our_5k = [70.10, 46.51, 42.38, 17.72]

x = np.arange(len(targets))
width = 0.18

# -------------------------------------------------------------
# Figure 7: In-Sample R^2 Comparison (2k & 5k Datasets)
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(11, 5.8), dpi=300)

r1 = ax.bar(x - 1.5*width, sota_2k, width, label='SOTA Baseline (2k Dataset)', color='#d95f02', edgecolor='black', alpha=0.85)
r2 = ax.bar(x - 0.5*width, sota_5k, width, label='SOTA Baseline (5k Dataset)', color='#e6ab02', edgecolor='black', alpha=0.85, hatch='..')
r3 = ax.bar(x + 0.5*width, our_2k, width, label='Our Method (2k Dataset)', color='#1b9e77', edgecolor='black', alpha=0.95)
r4 = ax.bar(x + 1.5*width, our_5k, width, label='Our Method (5k Dataset)', color='#2b8cbe', edgecolor='black', alpha=0.95, hatch='//')

# Reference limit lines
for i in range(len(targets)):
    ax.hlines(y=lit_limits[i], xmin=x[i]-2*width, xmax=x[i]+2*width, colors='#7570b3', linestyles='--', linewidth=2.0)

ax.set_ylabel('In-Sample $R^2$ Score (%)', fontsize=12, fontweight='bold')
ax.set_title('In-Sample Performance Comparison: Our Method vs. SOTA Baselines (2k & 5k Datasets)', fontsize=13, fontweight='bold', pad=12)
ax.set_xticks(x)
ax.set_xticklabels(targets, fontsize=11, fontweight='bold')
ax.legend(frameon=True, facecolor='white', framealpha=0.9, fontsize=9.5, loc='upper right')
ax.grid(axis='y', linestyle='--', alpha=0.4)
ax.set_ylim(-10, 115)

# Value annotations
for bars in [r1, r2, r3, r4]:
    for rect in bars:
        h = rect.get_height()
        ax.annotate(f'{h:.1f}%',
                    xy=(rect.get_x() + rect.get_width() / 2, max(0, h)),
                    xytext=(0, 2.5),
                    textcoords="offset points",
                    ha='center', va='bottom', fontsize=8, fontweight='bold')

plt.tight_layout()
out_r2_path = os.path.join(FIGURES_DIR, "sota_comparison_r2_bar.png")
plt.savefig(out_r2_path, dpi=300)
plt.close()
print(f"Saved R2 comparison bar chart: {out_r2_path}")

# -------------------------------------------------------------
# Figure 8: Limit Achieved (%) Comparison (2k & 5k Datasets)
# -------------------------------------------------------------
limit_sota_2k = [ (max(0, v)/lim)*100.0 for v, lim in zip(sota_2k, lit_limits) ]
limit_sota_5k = [ (max(0, v)/lim)*100.0 for v, lim in zip(sota_5k, lit_limits) ]
limit_our_2k  = [ (max(0, v)/lim)*100.0 for v, lim in zip(our_2k, lit_limits) ]
limit_our_5k  = [ (max(0, v)/lim)*100.0 for v, lim in zip(our_5k, lit_limits) ]

fig, ax = plt.subplots(figsize=(11, 5.8), dpi=300)

r1 = ax.bar(x - 1.5*width, limit_sota_2k, width, label='SOTA Baseline (2k Dataset)', color='#e7298a', edgecolor='black', alpha=0.85)
r2 = ax.bar(x - 0.5*width, limit_sota_5k, width, label='SOTA Baseline (5k Dataset)', color='#ce1256', edgecolor='black', alpha=0.85, hatch='..')
r3 = ax.bar(x + 0.5*width, limit_our_2k, width, label='Our Method (2k Dataset)', color='#08519c', edgecolor='black', alpha=0.95)
r4 = ax.bar(x + 1.5*width, limit_our_5k, width, label='Our Method (5k Dataset)', color='#3182bd', edgecolor='black', alpha=0.95, hatch='//')

# 100% Reference limit line
ax.axhline(100.0, color='red', linestyle='--', linewidth=1.8, label='100% Theoretical Literature Limit Ceiling ($R^2_{\mathrm{limit}}$)')

ax.set_ylabel('Percentage of Theoretical Limit Achieved (%)', fontsize=12, fontweight='bold')
ax.set_title('Percentage of Theoretical Literature Limit Achieved ($R^2 / R^2_{\mathrm{limit}}$)', fontsize=13, fontweight='bold', pad=12)
ax.set_xticks(x)
ax.set_xticklabels(targets, fontsize=11, fontweight='bold')
ax.legend(frameon=True, facecolor='white', framealpha=0.9, fontsize=9.5, loc='upper right')
ax.grid(axis='y', linestyle='--', alpha=0.4)
ax.set_ylim(0, 130)

for bars in [r1, r2, r3, r4]:
    for rect in bars:
        h = rect.get_height()
        ax.annotate(f'{h:.1f}%',
                    xy=(rect.get_x() + rect.get_width() / 2, max(1, h)),
                    xytext=(0, 2.5),
                    textcoords="offset points",
                    ha='center', va='bottom', fontsize=8, fontweight='bold')

plt.tight_layout()
out_limit_path = os.path.join(FIGURES_DIR, "sota_comparison_limit_bar.png")
plt.savefig(out_limit_path, dpi=300)
plt.close()
print(f"Saved Limit Achieved bar chart: {out_limit_path}")
