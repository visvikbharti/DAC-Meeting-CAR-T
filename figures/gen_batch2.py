#!/usr/bin/env python3
"""Generate figures 4-6: car_vs_tcr_affinity, kinetic_proofreading, tcr_synapse_organization"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

OUTDIR = '/Users/vishalbharti/Downloads/DAC-Meeting-CAR-T-MANPREET/figures'

def save(fig, name):
    fig.savefig(f'{OUTDIR}/{name}.png', dpi=300, bbox_inches='tight', facecolor='white')
    fig.savefig(f'{OUTDIR}/{name}.svg', bbox_inches='tight', facecolor='white')
    plt.close(fig)
    print(f'  Saved {name}.png + .svg')


# === Figure 4: CAR vs TCR Affinity ===
def fig_car_tcr():
    fig, ax = plt.subplots(figsize=(12, 7))
    categories = ['Natural TCR\n(Foreign Ag)', 'Natural TCR\n(Tumor Self-Ag)',
                   'FMC63 scFv\n(Anti-CD19 CAR)', 'Optimal CAR\nAffinity Window']
    values = [1, 2, -3, -0.3]
    colors = ['#4a90d9', '#f5a623', '#e74c3c', '#2ecc71']
    kd_labels = ['KD ≈ 10 µM', 'KD ≈ 100 µM', 'KD ≈ 1 nM', 'KD ≈ 500 nM']

    bars = ax.bar(categories, values, color=colors, width=0.55, edgecolor='black', linewidth=0.5)

    for bar, kd, val in zip(bars, kd_labels, values):
        ypos = val + 0.15 if val > 0 else val - 0.25
        ax.text(bar.get_x() + bar.get_width()/2, ypos, kd,
                ha='center', va='bottom' if val > 0 else 'top',
                fontsize=12, fontweight='bold')

    ax.axhline(y=0, color='gray', linewidth=0.8, alpha=0.5)
    ax.set_ylabel('log₁₀(KD in µM)', fontsize=13, fontweight='bold')
    ax.set_title('Affinity Comparison: Natural TCR vs CAR scFv',
                 fontsize=15, fontweight='bold')
    ax.set_ylim(-3.5, 2.5)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.tick_params(axis='x', labelsize=11)

    fig.text(0.15, 0.01,
             'Sources: TCR KD ranges from Stone et al., 2009, Immunology 126:165-176; '
             'Aleksic et al., 2007, J Immunol 178:5727.\n'
             'Tumor Ag from Hoffmann & Slansky, 2020. '
             'CAR optimal window from Park et al., 2017, Sci Rep 7:14366.',
             fontsize=7.5, color='gray', fontstyle='italic', va='bottom')
    save(fig, 'car_vs_tcr_affinity')

# === Figure 5: Kinetic Proofreading ===
def fig_kinetic_proofread():
    fig, ax = plt.subplots(figsize=(16, 6))
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 6)
    ax.axis('off')

    steps = [
        (1.5, 3.0, 'TCR + pMHC\nBinding', '#b3d9ff'),
        (4.5, 3.0, 'Step 1:\nCD3ζ ITAM\nPhosphorylation', '#c8e6c9'),
        (7.5, 3.0, 'Step 2:\nZAP-70\nRecruitment', '#fff9c4'),
        (10.5, 3.0, 'Step 3:\nLAT/SLP-76\nPhosphorylation', '#ffccbc'),
        (13.5, 3.0, 'SIGNAL\nOUTPUT\n(Activation)', '#e1bee7'),
    ]
    bw, bh = 2.2, 1.8
    for cx, cy, label, color in steps:
        box = FancyBboxPatch((cx - bw/2, cy - bh/2), bw, bh,
                              boxstyle="round,pad=0.15", facecolor=color,
                              edgecolor='black', linewidth=1.5)
        ax.add_patch(box)
        ax.text(cx, cy, label, ha='center', va='center', fontsize=10, fontweight='bold')

    for i in range(len(steps) - 1):
        x_start = steps[i][0] + bw/2 + 0.05
        x_end = steps[i+1][0] - bw/2 - 0.05
        ax.annotate('', xy=(x_end, 3.0), xytext=(x_start, 3.0),
                    arrowprops=dict(arrowstyle='->', color='green', lw=2.5))

    for cx, cy, label, color in steps[:-1]:
        ax.annotate('', xy=(cx, cy + bh/2 + 0.05), xytext=(cx, cy + bh/2 + 0.6),
                    arrowprops=dict(arrowstyle='->', color='red', lw=1.5))
        ax.text(cx, cy + bh/2 + 0.75, 'pMHC\ndissociates\n(koff)', fontsize=7.5,
                color='red', ha='center', va='bottom')

    ax.text(8, 1.0,
            'Each step = checkpoint. If pMHC dissociates (koff too fast), signal RESETS.\n'
            'N steps amplify discrimination by factor of ~koffⁿ → Exponential discrimination!',
            ha='center', va='center', fontsize=10.5, fontstyle='italic',
            bbox=dict(boxstyle='round,pad=0.5', facecolor='lightyellow', edgecolor='gray'))

    fig.text(0.5, 0.02,
             'Based on: McKeithan TW. PNAS. 1995;92(11):5042-5046. '
             'Validated by Torigoe et al., 2022, Nat Immunol 23:1045.',
             fontsize=8, color='gray', fontstyle='italic', ha='center')
    ax.set_title('Kinetic Proofreading in TCR Signal Transduction',
                 fontsize=15, fontweight='bold', pad=25)
    save(fig, 'kinetic_proofreading')

# === Figure 6: TCR Synapse Organization ===
def fig_synapse():
    fig, ax = plt.subplots(figsize=(8, 9))
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.8, 1.8)
    ax.set_aspect('equal')
    ax.axis('off')

    dsmac = plt.Circle((0, 0), 1.3, color='#90ee90', alpha=0.6, label='dSMAC (Actin-rich)')
    psmac = plt.Circle((0, 0), 0.9, color='#ffcc80', alpha=0.7, label='pSMAC (LFA-1/ICAM-1)')
    csmac = plt.Circle((0, 0), 0.4, color='#ef9a9a', alpha=0.8, label='cSMAC (TCR accumulation)')
    ax.add_patch(dsmac)
    ax.add_patch(psmac)
    ax.add_patch(csmac)

    ax.text(0, 1.15, 'dSMAC\n(Actin-rich)', ha='center', va='center',
            fontsize=10, fontweight='bold', color='#2e7d32')
    ax.text(0, 0.72, 'pSMAC\n(LFA-1/ICAM-1)', ha='center', va='center',
            fontsize=9, fontweight='bold', color='#e65100')
    ax.text(0, 0.0, 'cSMAC\n(TCR accumulation,\nsignal termination)',
            ha='center', va='center', fontsize=8, fontweight='bold', color='#c62828')

    angles = np.linspace(0, 2*np.pi, 8, endpoint=False)
    for a in angles:
        x, y = 0.65 * np.cos(a), 0.65 * np.sin(a)
        ax.plot(x, y, 'o', color='#1565c0', markersize=10, zorder=5)

    ax.text(0, -1.55,
            'Schematic based on: Campi et al., 2005, JEM 202:1031; Varma et al., 2006, Immunity 25:117;\n'
            'Crites et al., 2014, J Immunol 193:56. Microclusters ~0.35-0.5 µm² each.',
            ha='center', fontsize=7, color='gray', fontstyle='italic')

    legend_elements = [
        plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='#1565c0',
                   markersize=10, label='TCR Microclusters (~100 TCRs each)')
    ]
    ax.legend(handles=legend_elements, loc='lower right', fontsize=9, framealpha=0.9)
    ax.set_title('TCR Organization at the Immunological Synapse\n(Top-Down View)',
                 fontsize=14, fontweight='bold', pad=15)
    save(fig, 'tcr_synapse_organization')

fig_car_tcr()
fig_kinetic_proofread()
fig_synapse()
print('Batch 2 complete.')
