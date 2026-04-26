#!/usr/bin/env python3
"""Generate figures 1-3: catch_vs_slip_bond, affinity_windows, optimal_dwell_time"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

OUTDIR = '/Users/vishalbharti/Downloads/DAC-Meeting-CAR-T-MANPREET/figures'

def save(fig, name):
    fig.savefig(f'{OUTDIR}/{name}.png', dpi=300, bbox_inches='tight', facecolor='white')
    fig.savefig(f'{OUTDIR}/{name}.svg', bbox_inches='tight', facecolor='white')
    plt.close(fig)
    print(f'  Saved {name}.png + .svg')


# === Figure 1: Catch Bond vs Slip Bond ===
def fig_catch_slip():
    fig, ax = plt.subplots(figsize=(10, 7))
    force = np.linspace(0, 25, 300)
    catch = 0.8 * np.exp(-((force - 10)**2) / 40) + 0.1 * np.exp(-force / 8)
    catch = catch / catch.max() * 2.8
    slip = 1.4 * np.exp(-force / 5)
    ax.plot(force, catch, 'b-', linewidth=3, label='Agonist pMHC (Catch Bond)')
    ax.plot(force, slip, 'r--', linewidth=2.5, label='Antagonist pMHC (Slip Bond)')
    ax.annotate('Optimal Force\n~10 pN', xy=(10, catch[np.argmin(np.abs(force-10))]),
                xytext=(3, 2.5), fontsize=11, fontweight='bold', color='darkgreen',
                arrowprops=dict(arrowstyle='->', color='darkgreen', lw=1.5))
    ax.annotate('Force STRENGTHENS\nagonist bonds', xy=(16, 1.5),
                fontsize=10, fontstyle='italic', color='blue', ha='center')
    ax.annotate('Force WEAKENS\nantagonist bonds', xy=(18, 0.25),
                fontsize=10, fontstyle='italic', color='red', ha='center')
    ax.set_xlabel('Force (pN)', fontsize=13)
    ax.set_ylabel('Bond Lifetime (seconds)', fontsize=13)
    ax.set_title('Catch Bond vs Slip Bond Behavior in TCR-pMHC Interaction',
                 fontsize=14, fontweight='bold')
    ax.legend(fontsize=11, loc='upper right')
    ax.set_xlim(0, 25)
    ax.set_ylim(0, 3.0)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    fig.text(0.12, 0.01,
             'Schematic based on: Liu B, Chen W, Evavold BD, Zhu C. Cell. 2014;157(2):357-368.\n'
             'OT-I TCR system: OVA/A2/G4 (agonists, catch bonds) vs R4E1 (antagonist, slip bonds).\n'
             'Curve shapes are illustrative of the biphasic catch-slip vs monotonic slip behavior reported.',
             fontsize=7.5, color='gray', va='bottom')
    save(fig, 'catch_vs_slip_bond')

# === Figure 2: Affinity Windows ===
def fig_affinity_windows():
    fig, ax = plt.subplots(figsize=(14, 7))
    zones = [
        (np.log10(0.01), np.log10(6), 'Strong Agonist\n/ Deletion\n(<6 µM)', '#ff6b6b'),
        (np.log10(6), np.log10(10), 'Negative\nSelection\n(6-10 µM)', '#ffa07a'),
        (np.log10(10), np.log10(100), 'Transition\nZone\n(10-100 µM)', '#ffd700'),
        (np.log10(100), np.log10(300), 'Positive\nSelection\n(100-300 µM)', '#90ee90'),
        (np.log10(300), np.log10(1000), 'Death by\nNeglect\n(>300 µM)', '#d3d3d3'),
    ]
    for x0, x1, label, color in zones:
        ax.axvspan(x0, x1, ymin=0.35, ymax=0.85, color=color, alpha=0.8)
        cx = (x0 + x1) / 2
        ax.text(cx, 0.62, label, ha='center', va='center', fontsize=10.5, fontweight='bold',
                transform=ax.get_xaxis_transform())

    arrow_data = [
        (np.log10(0.005), 'CAR scFv\n(~1-10 nM)', 'green', 0.22),
        (np.log10(10), 'Viral Ag\n(~10 µM)', 'blue', 0.22),
        (np.log10(80), 'Tumor Self-Ag\n(~100 µM)', 'red', 0.22),
        (np.log10(300), 'Autoimmune\n(~200 µM)', 'purple', 0.08),
    ]
    for xpos, label, color, ypos in arrow_data:
        ax.annotate('', xy=(xpos, 0.38), xytext=(xpos, ypos),
                    xycoords=('data', 'axes fraction'), textcoords=('data', 'axes fraction'),
                    arrowprops=dict(arrowstyle='->', color=color, lw=2))
        ax.text(xpos, ypos - 0.06, label, ha='center', va='top', fontsize=10,
                fontweight='bold', color=color, transform=ax.get_xaxis_transform())

    ax.set_xlim(np.log10(0.005), np.log10(1500))
    ax.set_xticks([np.log10(0.01), np.log10(0.1), np.log10(1), np.log10(10),
                   np.log10(100), np.log10(1000)])
    ax.set_xticklabels(['0.01 µM\n(10 nM)', '0.1 µM\n(100 nM)', '1 µM',
                        '10 µM', '100 µM', '1000 µM'], fontsize=10)
    ax.set_xlabel('log₁₀(KD in µM) ← Stronger Binding | Weaker Binding →',
                  fontsize=13, fontweight='bold')
    ax.set_title('TCR Affinity Windows: Thymic Selection and Antigen Categories',
                 fontsize=15, fontweight='bold', pad=15)
    ax.set_yticks([])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)

    fig.text(0.10, 0.08,
             'Data sources: Selection thresholds from Juang et al., 2010, JEM 207:1223-1234 (OT-1/Kb system).\n'
             'Antigen categories from Hoffmann & Slansky, 2020, Mol Carcinog 59:862-870. '
             'CAR affinity from Park et al., 2017.',
             fontsize=7.5, color='gray', va='top')
    plt.subplots_adjust(bottom=0.20, top=0.92)
    save(fig, 'affinity_windows')

# === Figure 3: Optimal Dwell Time ===
def fig_optimal_dwell():
    fig, ax = plt.subplots(figsize=(10, 7))
    t = np.linspace(0, 130, 500)
    activation = t**1.8 * np.exp(-t / 25)
    activation = activation / activation.max() * 2.9

    ax.fill_between(t, 0, 3.0, where=(t < 10), color='#ffcccc', alpha=0.4)
    ax.fill_between(t, 0, 3.0, where=((t >= 10) & (t < 55)), color='#ccffcc', alpha=0.4)
    ax.fill_between(t, 0, 3.0, where=(t >= 55), color='#fff3cc', alpha=0.4)

    ax.plot(t, activation, 'b-', linewidth=3)
    ax.axvline(x=34, color='green', linestyle='--', linewidth=1.5)
    ax.text(36, 2.6, 'Optimal t½ ≈ 34 s\n(Kalergis et al., 2001)',
            fontsize=11, fontweight='bold', color='darkgreen')

    ax.text(3, 2.85, 'No kinetic\nproofreading\ncompleted', fontsize=8.5, fontstyle='italic',
            color='red', ha='center', va='top',
            bbox=dict(boxstyle='round,pad=0.2', facecolor='white', alpha=0.7, edgecolor='none'))
    ax.text(100, 1.6, 'Serial engagement\nblocked', fontsize=8.5, fontstyle='italic',
            color='#996600', ha='center', va='center',
            bbox=dict(boxstyle='round,pad=0.2', facecolor='white', alpha=0.7, edgecolor='none'))

    ax.set_xlabel('TCR-pMHC Dwell Time / Half-life (seconds)', fontsize=13)
    ax.set_ylabel('T Cell Activation (Relative)', fontsize=13)
    ax.set_title('The Optimal Dwell Time ("Goldilocks") Concept',
                 fontsize=14, fontweight='bold')
    ax.set_xlim(0, 130)
    ax.set_ylim(0, 3.0)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    fig.text(0.12, 0.01,
             'Based on: Kalergis AM et al., Nat Immunol. 2001;2(3):229-234.\n'
             'Data: t½ ≤10.3s (no killing), 34s (max killing), 77s (impaired). '
             'Bell-shaped curve is illustrative.',
             fontsize=7.5, color='gray', va='bottom')
    save(fig, 'optimal_dwell_time')

fig_catch_slip()
fig_affinity_windows()
fig_optimal_dwell()
print('Batch 1 complete.')
