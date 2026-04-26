# Figure Interpretations and Data Sources — Computational Validation

## For Manpreet Kour | CSIR-IGIB

This document explains each computational validation figure in detail: what it shows, exactly how the data was generated, what the numbers mean, and how to interpret the results.

---

## Figure 1: interface_burial_analysis.png / .svg

### What You See
A bar chart with 19 bars. Each bar represents one amino acid residue in the FMC63 scFv that is located at the binding interface with CD19.

### How the Data Was Generated

1. **Downloaded PDB 7URV** — the cryo-EM structure of FMC63 bound to CD19 (Singh et al., 2023, *Science Immunology*).

2. **Extracted individual chains** — separated the complex PDB file into two files: one containing only Chain D (FMC63, isolated) and one containing only Chain C (CD19, isolated).

3. **Calculated SASA for each residue** using the FreeSASA library:
   - SASA in the complex (when CD19 is present) — some surface is hidden by CD19
   - SASA in isolation (when CD19 is absent) — full surface is exposed

4. **Computed dSASA** = SASA(isolated) − SASA(complex) for each residue. This is the area "buried" (hidden) when CD19 binds.

5. **Only residues with dSASA > 5 Å²** are shown (19 residues meet this threshold).

### What the Numbers Mean

| Value | Meaning |
|-------|---------|
| Bar height (Å²) | Surface area buried upon CD19 binding. Higher = more contact with CD19. |
| Red bars | Your 4 target residues: Tyr70, Ser214, Tyr260, Tyr261 |
| Blue bars | Other FMC63 residues at the interface |
| % values on red bars | Percentage of the residue's total surface that is buried |
| "322 Å² / 629 Å² = 51.2%" | The 4 target residues account for more than half the total interface |

### Key Interpretation

The red bars (your targets) are among the tallest bars in the chart. This is **not by design** — it emerges independently from the structural analysis. It means your residue selection targets the most impactful positions at the interface.

### Exact Values Plotted

| Residue | dSASA (Å²) | % Buried | Source |
|---------|-----------|----------|--------|
| TYR 70 | 49.6 | 75.5% | FreeSASA on PDB 7URV |
| TYR 87 | 21.3 | 49.2% | FreeSASA on PDB 7URV |
| HIS 88 | 15.3 | 37.7% | FreeSASA on PDB 7URV |
| ARG 91 | 26.7 | 23.9% | FreeSASA on PDB 7URV |
| ASN 130 | 20.3 | 40.8% | FreeSASA on PDB 7URV |
| PRO 190 | 15.6 | 23.4% | FreeSASA on PDB 7URV |
| ASP 191 | 35.9 | 34.0% | FreeSASA on PDB 7URV |
| TRP 212 | 12.8 | 97.9% | FreeSASA on PDB 7URV |
| GLY 213 | 12.8 | 74.1% | FreeSASA on PDB 7URV |
| SER 214 | 72.1 | 92.1% | FreeSASA on PDB 7URV |
| GLU 215 | 7.0 | 7.5% | FreeSASA on PDB 7URV |
| THR 216 | 32.9 | 45.6% | FreeSASA on PDB 7URV |
| TYR 218 | 12.3 | 15.7% | FreeSASA on PDB 7URV |
| TYR 259 | 27.0 | 32.6% | FreeSASA on PDB 7URV |
| TYR 260 | 98.1 | 85.4% | FreeSASA on PDB 7URV |
| TYR 261 | 102.3 | 78.8% | FreeSASA on PDB 7URV |
| GLY 262 | 18.0 | 98.0% | FreeSASA on PDB 7URV |
| GLY 263 | 24.7 | 88.3% | FreeSASA on PDB 7URV |
| TYR 265 | 24.3 | 54.7% | FreeSASA on PDB 7URV |

**Tool:** FreeSASA (Mitternacht, 2016, *F1000Research* 5:189)
**Algorithm:** Lee-Richards (Shrake-Rupley variant), probe radius 1.4 Å

---

## Figure 2: target_residue_contacts.png / .svg

### What You See
Four panels arranged in a 2×2 grid. Each panel shows one target residue (red box on the left) and all the CD19 residues it contacts (blue/green boxes on the right), connected by lines.

### How the Data Was Generated

1. **For each target residue** in FMC63 (chain D), we searched for all CD19 (chain C) residues with at least one atom within 4.5 Å.

2. **Minimum distance** between any atom pair of the two residues was calculated and is shown.

3. **Hydrogen bonds** were identified as N/O atom pairs within 3.5 Å (shown in green).

4. **Published experimental KD** for the alanine mutant (from Singh et al., 2023) is shown at the bottom of each panel.

### How to Read Each Panel

- **Red box (left):** The FMC63 residue being analyzed
- **Green boxes (right) with distances:** CD19 residues forming hydrogen bonds with this FMC63 residue. The distance is the N/O–N/O distance in Ångströms. Shorter = stronger H-bond.
- **Blue boxes (right):** CD19 residues forming van der Waals contacts (close but no H-bond)
- **Solid green lines:** Hydrogen bond connections (stronger)
- **Dashed blue lines:** Van der Waals connections (weaker)
- **Bottom annotation:** What happens experimentally when this residue is mutated to alanine

### Panel-by-Panel Interpretation

**SER 214 → CD19 contacts:**
- 4 contacts, 2 H-bonds (PRO222 at 2.61 Å, LYS223 at 3.14 Å)
- The 2.61 Å H-bond to PRO222 is exceptionally short — strong interaction
- Alanine mutant: **not yet tested** — this is Manpreet's planned experiment
- **Prediction:** Significant binding loss because the side-chain OG that forms the 2.61 Å H-bond will be removed

**TYR 260 → CD19 contacts:**
- 5 contacts, 1 H-bond (ILE166 at 2.96 Å)
- The H-bond is from TYR260's side-chain OH to ILE166's backbone N
- Alanine mutant: **no binding** (>1000× loss) — published in Singh et al., 2023
- **Interpretation:** Removing the OH destroys a critical side-chain H-bond that cannot be compensated

**TYR 261 → CD19 contacts:**
- 6 contacts (most of any residue), 1 H-bond (PRO219 at 3.20 Å)
- The H-bond is through TYR261's **backbone N** (not side-chain)
- Alanine mutant: KD = 682.5 nM (152× weaker) — Singh et al., 2023
- **Interpretation:** Alanine retains the backbone N, so the H-bond is preserved. The 152-fold loss comes from losing the large aromatic side chain's van der Waals contacts with 6 CD19 residues.

**TYR 70 → CD19 contacts:**
- 3 contacts, 0 H-bonds (van der Waals only)
- Contacts with ARG163, GLU165, ALA160 — all moderate distances
- Alanine mutant: KD = 275.3 nM (61× weaker) — Singh et al., 2023
- **Interpretation:** Fewest contacts and no H-bonds → mildest effect, as expected

### Exact Contact Distances

All distances are minimum inter-atomic distances (Å) computed from PDB 7URV coordinates using BioPython's NeighborSearch:

| FMC63 Residue | CD19 Partner | Min Distance (Å) | Contact Type |
|--------------|-------------|:-----------------:|-------------|
| SER 214 | LYS 220 | 3.93 | van der Waals |
| SER 214 | GLY 221 | 3.52 | van der Waals |
| SER 214 | PRO 222 | 2.61 | **H-bond** |
| SER 214 | LYS 223 | 3.14 | **H-bond** |
| TYR 260 | TYR 157 | 3.75 | Aromatic stacking |
| TYR 260 | PRO 164 | 4.21 | van der Waals |
| TYR 260 | GLU 165 | 3.46 | van der Waals |
| TYR 260 | ILE 166 | 2.96 | **H-bond** |
| TYR 260 | PRO 219 | 3.85 | van der Waals |
| TYR 261 | PRO 164 | 3.28 | van der Waals |
| TYR 261 | VAL 217 | 3.61 | van der Waals |
| TYR 261 | HIS 218 | 3.36 | van der Waals |
| TYR 261 | PRO 219 | 3.20 | **H-bond** |
| TYR 261 | GLY 221 | 3.92 | van der Waals |
| TYR 261 | PRO 222 | 3.35 | van der Waals |
| TYR 70 | ALA 160 | 4.11 | van der Waals (weak) |
| TYR 70 | ARG 163 | 3.70 | Cation-π |
| TYR 70 | GLU 165 | 3.71 | van der Waals |

---

## Figure 3: burial_vs_affinity.png / .svg

### What You See
A scatter plot with three red circles and one gray diamond. The x-axis shows buried surface area; the y-axis shows the experimental binding affinity (KD) of the alanine mutant.

### How the Data Was Generated

This figure combines two independent data sources:

1. **X-axis (dSASA):** Computed from our SASA analysis of PDB 7URV using FreeSASA (see Figure 1 description)

2. **Y-axis (KD):** Published experimental values from Singh et al., 2023:
   - Y70A: KD = 275.3 nM
   - Y260A: No detectable binding — plotted as 5000 nM (this is a lower bound; the actual KD could be much higher)
   - Y261A: KD = 682.5 nM

3. **Bubble size:** Proportional to the number of CD19 contacts identified in our analysis

4. **Gray diamond (Ser214):** No published experimental KD exists. Plotted at y=0 to indicate "not yet tested." The x-value (72.1 Å²) is from our analysis.

5. **Green dashed line:** WT FMC63 KD = 5.1 nM (from Seigner et al., 2023)

### What This Figure Demonstrates

**The general trend:** Residues with larger buried surface area tend to be more important for binding. When mutated to alanine, they cause greater affinity loss (higher KD).

**The nuance:** The correlation is not perfect because **hydrogen bonds matter more than burial alone:**
- TYR 260 (dSASA = 98 Å²) has a greater effect than TYR 261 (dSASA = 102 Å²) despite being slightly less buried — because Y260 has a critical **side-chain** H-bond that is destroyed by Ala
- TYR 70 (dSASA = 50 Å²) has a moderate effect — consistent with its lower burial AND absence of H-bonds

**The prediction for Ser214:** With 72 Å² burial and a 2.61 Å side-chain H-bond, Ser214 is expected to show significant binding loss when mutated — potentially in the Y261A range or stronger. This is a testable prediction from your project.

### Important Notes on Y260A Plotting

Y260A showed "no detectable binding" by SPR. In our plot, we show it at 5000 nM, but the actual KD could be:
- 5,000 nM (mild loss of binding)
- 50,000 nM (severe loss)
- Infinity (truly no binding)

The SPR detection limit depends on the protein concentration range tested. Singh et al. likely tested up to low micromolar concentrations. The key point is that binding was completely abolished, which our structural analysis explains (loss of the critical OH → N H-bond).

---

## Summary Table: What Is Real Data vs. Computed vs. Predicted

| Data Point | Type | Source |
|-----------|------|--------|
| PDB 7URV atom coordinates | Real experimental data | Cryo-EM, Singh et al. 2023 |
| Contact distances (Å) | Computed from real data | BioPython on PDB 7URV |
| dSASA values (Å²) | Computed from real data | FreeSASA on PDB 7URV |
| H-bond identification | Computed from real data | Distance criteria on PDB 7URV |
| WT FMC63 KD = 5.1 nM | Real experimental data | SPR, Seigner et al. 2023 |
| Y260A KD = no binding | Real experimental data | SPR, Singh et al. 2023 |
| Y261A KD = 682.5 nM | Real experimental data | SPR, Singh et al. 2023 |
| Y70A KD = 275.3 nM | Real experimental data | SPR, Singh et al. 2023 |
| S214A prediction | **Computational prediction** | Based on burial + H-bond analysis |
| Bar heights in Figure 1 | Computed from real data | FreeSASA (exact values) |
| Contact maps in Figure 2 | Computed from real data | BioPython (exact distances) |

**Nothing in these figures is fabricated.** Every number either comes from published experimental measurements or is computed directly from the atomic coordinates of a published structure.

---

*Document prepared: 2026-04-27. All analysis on PDB 7URV. Experimental values from Singh et al. (2023) and Seigner et al. (2023).*
