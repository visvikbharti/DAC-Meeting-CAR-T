#!/usr/bin/env python3
"""Generate figures 7-9: signaling_cascade, serial_engagement, experimental_workflow"""
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


# === Figure 7: Signaling Cascade ===
def fig_signaling():
    fig, ax = plt.subplots(figsize=(8, 14))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 18)
    ax.axis('off')

    steps = [
        (5, 16.5, 'pMHC binds TCR (KD, kon, koff)', '#bbdefb', 3.5, 0.7),
        (5, 15.0, 'Mechanical Force Applied (~10 pN)', '#c8e6c9', 3.5, 0.7),
        (5, 13.5, 'Catch Bond (agonist) or\nSlip Bond (antagonist)', '#fff9c4', 3.5, 0.8),
        (5, 12.0, 'Cβ FG Loop Conformational Change', '#ffe0b2', 3.5, 0.7),
        (5, 10.5, 'CD3ζ ITAM Exposure &\nPhosphorylation', '#f8bbd0', 3.5, 0.8),
        (5, 9.0, 'ZAP-70 → LAT → SLP-76 → PLCγ', '#e1bee7', 3.5, 0.7),
        (5, 7.5, 'Kinetic Proofreading Checkpoints', '#d1c4e9', 3.5, 0.7),
        (5, 6.0, 'Ca²⁺ Flux, NFAT, NF-κB,\nAP-1 Activation', '#b2dfdb', 3.5, 0.8),
    ]

    for cx, cy, label, color, bw, bh in steps:
        box = FancyBboxPatch((cx - bw/2, cy - bh/2), bw, bh,
                              boxstyle="round,pad=0.12", facecolor=color,
                              edgecolor='black', linewidth=1.2)
        ax.add_patch(box)
        ax.text(cx, cy, label, ha='center', va='center', fontsize=9.5, fontweight='bold')

    for i in range(len(steps) - 1):
        y_start = steps[i][1] - steps[i][5]/2 - 0.05
        y_end = steps[i+1][1] + steps[i+1][5]/2 + 0.05
        ax.annotate('', xy=(5, y_end), xytext=(5, y_start),
                    arrowprops=dict(arrowstyle='->', color='#333333', lw=1.8))

    ax.text(5, 4.8, 'Functional Outcomes', ha='center', fontsize=11, fontweight='bold')

    outcomes = [
        (1.8, 3.8, 'Cytokine\nProduction', '#bbdefb'),
        (4.0, 3.8, 'Cytotoxicity\n(Killing)', '#c8e6c9'),
        (6.2, 3.8, 'Proliferation\n& Memory', '#fff9c4'),
        (8.4, 3.8, 'Exhaustion\n(if chronic)', '#ffccbc'),
    ]
    for cx, cy, label, color in outcomes:
        box = FancyBboxPatch((cx - 1.0, cy - 0.5), 2.0, 1.0,
                              boxstyle="round,pad=0.1", facecolor=color,
                              edgecolor='black', linewidth=1.0)
        ax.add_patch(box)
        ax.text(cx, cy, label, ha='center', va='center', fontsize=8.5, fontweight='bold')

    for cx, cy, label, color in outcomes:
        ax.annotate('', xy=(cx, cy + 0.5 + 0.05), xytext=(5, 4.5),
                    arrowprops=dict(arrowstyle='->', color='gray', lw=1.0, alpha=0.6))

    ax.set_title('From pMHC Binding to T Cell Function',
                 fontsize=15, fontweight='bold', pad=10)
    fig.text(0.5, 0.02,
             'Composite model based on: Liu et al., 2014, Cell; Brazin et al., 2015, PNAS;\n'
             'McKeithan, 1995, PNAS; Kim et al., 2009, JBC. Force values from Liu et al., 2016, PNAS.',
             fontsize=7, color='gray', fontstyle='italic', ha='center')
    save(fig, 'signaling_cascade')


# === Figure 8: Serial Engagement ===
def fig_serial():
    fig, ax = plt.subplots(figsize=(14, 7))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 8)
    ax.axis('off')

    ax.annotate('', xy=(12.5, 7.0), xytext=(1.5, 7.0),
                arrowprops=dict(arrowstyle='->', lw=2.5, color='black'))
    ax.text(7, 7.4, 'Time →', ha='center', fontsize=13, fontweight='bold')

    ax.add_patch(plt.Rectangle((1, 4.2), 12, 0.6, color='#90caf9', alpha=0.7))
    ax.text(7, 5.1, 'T Cell Surface', ha='center', fontsize=12,
            fontweight='bold', color='#1565c0')

    ax.add_patch(plt.Rectangle((1, 2.8), 12, 0.5, color='#ffcc80', alpha=0.7))
    ax.text(7, 2.5, 'APC Surface', ha='center', fontsize=12,
            fontweight='bold', color='#e65100')

    engage_x = [3, 6.5, 10]
    for i, ex in enumerate(engage_x):
        ax.plot(ex, 3.3, 'v', color='red', markersize=15, zorder=5)
        ax.annotate('', xy=(ex, 4.2), xytext=(ex, 3.5),
                    arrowprops=dict(arrowstyle='->', color='green', lw=2))
        ax.text(ex, 5.9, f'Engage\n#{i+1}', ha='center', fontsize=9,
                fontweight='bold', color='darkgreen')
        ax.plot(ex, 4.5, '^', color='#1565c0', markersize=13, zorder=5)
        if i < len(engage_x) - 1:
            mid = (ex + engage_x[i+1]) / 2
            ax.annotate('', xy=(engage_x[i+1] - 0.5, 3.3),
                        xytext=(ex + 0.5, 3.3),
                        arrowprops=dict(arrowstyle='->', color='red',
                                        lw=2, linestyle='dashed'))

    for tx in [2, 4, 5.5, 7.5, 8.5, 9, 11, 11.5, 12]:
        ax.plot(tx, 4.5, '^', color='#90caf9', markersize=8, alpha=0.5, zorder=4)

    ax.text(7, 1.5,
            'One pMHC serially engages ~200 TCRs  |  Up to 18,000 TCRs triggered per T cell',
            ha='center', va='center', fontsize=11, fontstyle='italic',
            bbox=dict(boxstyle='round,pad=0.4', facecolor='lightyellow', edgecolor='gray'))

    legend_elements = [
        plt.Line2D([0], [0], marker='v', color='w', markerfacecolor='red',
                   markersize=12, label='pMHC (single)'),
        plt.Line2D([0], [0], marker='^', color='w', markerfacecolor='#1565c0',
                   markersize=12, label='TCR (triggered)'),
        plt.Line2D([0], [0], marker='^', color='w', markerfacecolor='#90caf9',
                   markersize=10, label='TCR (un-triggered)', alpha=0.5),
    ]
    ax.legend(handles=legend_elements, loc='lower right', fontsize=10, framealpha=0.9)

    fig.text(0.5, 0.02,
             'Based on: Valitutti S et al., Nature. 1995;375:148-151. '
             'Review: Valitutti, 2012, Front Immunol 3:272.',
             fontsize=8, color='gray', fontstyle='italic', ha='center')
    ax.set_title('Serial Engagement Model', fontsize=15, fontweight='bold', pad=15)
    save(fig, 'serial_engagement')


# === Figure 9: Experimental Workflow ===
def fig_workflow():
    fig, ax = plt.subplots(figsize=(16, 10))
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 10)
    ax.axis('off')

    boxes = [
        (2.5, 8.5, 'STEP 1\nCAR Construct Design\n(pLV-CAR-BFP &\npLV-CAR-eGFP)', '#bbdefb'),
        (8.0, 8.5, 'STEP 2\nIdentify Key Interacting\nResidues (PDB/Chimera/X)\nTyr260, Tyr261, Ser214', '#c8e6c9'),
        (13.5, 8.5, 'STEP 3\nSite-Saturation\nMutagenesis\n(NNK Primers)', '#fff9c4'),

        (2.5, 5.0, 'STEP 4\nFunctional Screening\n• Cytotoxicity (Raji co-culture)\n• Exhaustion markers\n• Memory phenotype\n• Proliferation', '#ffe0b2'),
        (8.0, 5.0, 'STEP 5\nSelect Mutants with\nDesired Phenotypes\n• Best cytotoxicity\n• Least exhaustion\n• Best memory', '#f8bbd0'),
        (13.5, 5.0, 'STEP 6\nClone scFvs in Expression\nVector (pET-CON2 or pTT5)\n& Purify Protein', '#e1bee7'),

        (5.0, 1.5, 'STEP 7\nKinetic Characterization\n(SPR / BLI)\n• KD, kon, koff\n• Binding thermodynamics\n• Force-dependent behavior', '#d1c4e9'),
        (11.5, 1.5, 'STEP 8\nCorrelate Kinetics\nwith Function\n• Identify optimal affinity window\n• Generalizable key residue rules\n• Therapeutic implications', '#b2dfdb'),
    ]

    bw, bh = 4.2, 2.2
    for cx, cy, label, color in boxes:
        box = FancyBboxPatch((cx - bw/2, cy - bh/2), bw, bh,
                              boxstyle="round,pad=0.2", facecolor=color,
                              edgecolor='black', linewidth=1.3)
        ax.add_patch(box)
        ax.text(cx, cy, label, ha='center', va='center', fontsize=8.5, fontweight='bold')

    arrows = [
        (2.5 + bw/2, 8.5, 8.0 - bw/2, 8.5),
        (8.0 + bw/2, 8.5, 13.5 - bw/2, 8.5),
        (13.5, 8.5 - bh/2, 13.5, 5.0 + bh/2),
        (13.5 - bw/2, 5.0, 8.0 + bw/2, 5.0),
        (8.0 - bw/2, 5.0, 2.5 + bw/2, 5.0),
        (2.5, 5.0 - bh/2, 5.0, 1.5 + bh/2),
        (5.0 + bw/2, 1.5, 11.5 - bw/2, 1.5),
    ]
    for x1, y1, x2, y2 in arrows:
        ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                    arrowprops=dict(arrowstyle='->', color='#333333', lw=2, connectionstyle='arc3,rad=0'))

    ax.set_title('Experimental Design Workflow', fontsize=16, fontweight='bold', pad=15)
    save(fig, 'experimental_workflow')


fig_signaling()
fig_serial()
fig_workflow()
print('Batch 3 complete.')
