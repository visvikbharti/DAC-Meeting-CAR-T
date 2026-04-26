# Next Steps: Running Web Server ddG Predictions — Complete Guide for Manpreet

## What This Document Is

This is a step-by-step guide for Manpreet to run binding affinity predictions on the FMC63-CD19 interface using verified web servers. After completing these steps, you will have **predicted ddG values** for all mutations at your target residues, which you can compare with your experimental data and present to the DAC.

---

## Why Run These Predictions?

### Rationale

Our structural analysis (contacts, SASA burial, hydrogen bonds) validates the target residue selection **qualitatively** — it shows these residues are important but does not quantify *how much* binding energy each residue contributes.

Web-based ddG prediction tools estimate the **change in binding free energy (ddG, in kcal/mol)** when a residue is mutated. This provides:

1. **Quantitative predictions** — not just "this residue is at the interface" but "mutating this residue is predicted to cost 3.2 kcal/mol of binding energy"
2. **Validation checkpoint** — if the tools correctly predict the published experimental results (Y260A, Y261A, Y70A), we have confidence in their predictions for untested mutations (S214A and all NNK substitutions)
3. **Pre-screening of the NNK library** — saturation mutagenesis mode predicts which of the 20 amino acids at each position will increase, decrease, or maintain binding
4. **DAC presentation strength** — showing multi-tool computational consensus alongside structural analysis demonstrates rigorous, multi-pronged validation

### Scientific Basis

Protein-protein binding affinity depends on the sum of all non-covalent interactions at the interface: van der Waals forces, hydrogen bonds, electrostatic interactions, hydrophobic packing, and the entropy cost of immobilizing flexible residues. Computational tools estimate how these contributions change when a residue is mutated, using either:
- **Machine learning** trained on experimental binding data (mCSM, DDMut)
- **Physics-based energy functions** (FoldX, Rosetta)
- **Statistical potentials** derived from structural databases (BeAtMuSiC)

Published benchmark: mCSM-AB2 achieves Pearson correlation r = 0.73-0.74 against experimental antibody-antigen ddG values (Myung et al., 2020, PMID: 31665262).

---

## Step-by-Step Protocol

### STEP 1: Prepare the Input File

**What you need:** The PDB file of the FMC63-CD19 complex.

**File:** `computational_validation/structures/7urv.pdb` (already downloaded)

**Chain assignments in 7URV:**
- Chain C = CD19 (the antigen)
- Chain D = FMC63 scFv (the antibody — this is where your mutations are)

**Important:** Some web servers may ask you to specify which chains form the complex. Always specify: Chain D (antibody/receptor) binds Chain C (antigen/ligand).

---

### STEP 2: Run mCSM-AB2 (Antibody-Specific — Do This First)

**URL:** https://biosig.lab.uq.edu.au/mcsm_ab2/

**Why this tool first:** It is specifically trained on antibody-antigen binding data (1,810 mutations), making it the most appropriate tool for FMC63-CD19.

**Reference:** Myung Y, Rodrigues CHM, Ascher DB, Pires DEV. "mCSM-AB2: guiding rational antibody design using graph-based signatures." *Bioinformatics* 36:1453-1459, 2020. PMID: 31665262.

**Step-by-step:**

1. Go to https://biosig.lab.uq.edu.au/mcsm_ab2/
2. Click **"Predict"** or **"Submit"**
3. **Upload PDB file:** Click "Choose File" and select `7urv.pdb`
   - OR enter PDB ID: `7URV`
4. **Specify chain:** Antibody chain = **D**
5. **Enter mutation:** Format is `D Y260A` (chain, wild-type residue in 1-letter code, position number, mutant residue in 1-letter code)
6. Click **Submit**
7. Wait for results (typically 1-5 minutes)

**Mutations to submit (one at a time):**

| Mutation Code | What It Means | Why |
|--------------|---------------|-----|
| `D Y260A` | Tyr260 → Ala in FMC63 | Published: no binding (validation) |
| `D Y261A` | Tyr261 → Ala in FMC63 | Published: KD = 682.5 nM (validation) |
| `D Y70A` | Tyr70 → Ala in FMC63 | Published: KD = 275.3 nM (validation) |
| `D S214A` | Ser214 → Ala in FMC63 | **Your target — no published data** |

**How to interpret the output:**

| Output Field | What It Means |
|-------------|---------------|
| ddG (kcal/mol) | Predicted change in binding free energy. **Positive** = destabilizing (weaker binding). **Negative** = stabilizing (stronger binding). |
| ddG > +2.0 | **Hotspot** — mutation causes major binding loss |
| ddG +1.0 to +2.0 | **Warm spot** — moderate binding loss |
| ddG -1.0 to +1.0 | **Neutral** — minimal effect |
| ddG < -1.0 | **Stabilizing** — mutation may improve binding |

**What to save:**
- Screenshot the results page
- Record the ddG value for each mutation in a table
- Save any downloadable results file (CSV/text)
- Note the prediction confidence if provided

**Expected results (based on experimental data):**
- Y260A: should predict large positive ddG (>3 kcal/mol) — binding loss
- Y261A: should predict moderate-to-large positive ddG (~2-3 kcal/mol)
- Y70A: should predict moderate positive ddG (~1.5-2.5 kcal/mol)
- S214A: **this is unknown** — record whatever the tool predicts

---

### STEP 3: Run mCSM-PPI2 (General PPI — Alanine Scanning + Saturation Mutagenesis)

**URL:** https://biosig.lab.uq.edu.au/mcsm_ppi2/

**Why this tool:** It has dedicated "Alanine Scanning" and "Saturation Mutagenesis" modes that can scan the entire interface or predict all 20 amino acid substitutions at once.

**Reference:** Rodrigues CHM, Myung Y, Pires DEV, Ascher DB. "mCSM-PPI v2: predicting the effects of mutations on protein-protein interactions." *Nucleic Acids Research* 47:W338-W344, 2019. PMID: 31114883.

**Step-by-step for Alanine Scanning mode:**

1. Go to https://biosig.lab.uq.edu.au/mcsm_ppi2/
2. Select **"Alanine Scanning"** mode
3. Upload `7urv.pdb` or enter PDB ID `7URV`
4. Specify chains: Chain D (partner 1) and Chain C (partner 2)
5. Submit
6. The tool will mutate **every interface residue** to alanine and predict ddG for each

**What to save from Alanine Scanning:**
- The complete ranked list of interface residues by predicted ddG
- Confirm that Tyr260, Tyr261, Ser214 are among the top-ranked hotspots
- Download the results table (if available)

**Step-by-step for Saturation Mutagenesis mode:**

1. On the same site, select **"Saturation Mutagenesis"** mode
2. Upload `7urv.pdb`
3. Specify the **position(s)** to scan: 260, 261, 214 (one at a time)
4. The tool will predict ddG for all 19 possible amino acid substitutions at that position
5. Output is typically a **heatmap** showing which substitutions are predicted to be stabilizing vs destabilizing

**What to save from Saturation Mutagenesis:**
- The heatmap image for each position (260, 261, 214)
- The complete ddG table for all 20 amino acids at each position
- Save the downloadable data file

**How to interpret the heatmap:**
- Rows = positions, Columns = substituted amino acid
- Red/warm colors = destabilizing (weaker binding, positive ddG)
- Blue/cool colors = stabilizing (stronger binding, negative ddG)
- White/neutral = minimal effect
- Look for patterns: e.g., at position 260, are all substitutions destabilizing? Or do some maintain binding?

---

### STEP 4: Run DDMut-PPI (Deep Learning Approach)

**URL:** https://biosig.lab.uq.edu.au/ddmut_ppi/

**Why this tool:** Newest approach using graph convolutional networks and protein language models. Validated on AB-Bind (645 antibody mutations).

**Reference:** Zhou Y, Myung Y, Rodrigues CHM, Ascher DB. "DDMut-PPI: predicting effects of mutations on protein-protein interactions using graph-based deep learning." *Nucleic Acids Research* 52:W207-W214, 2024. PMID: 38783112.

**Step-by-step:**

1. Go to https://biosig.lab.uq.edu.au/ddmut_ppi/
2. Upload `7urv.pdb` or enter PDB ID
3. Specify chain D (where mutations are) and chain C (binding partner)
4. Enter mutations: `D Y260A`, `D Y261A`, `D Y70A`, `D S214A`
5. Submit and record results

**What to save:** Same as mCSM-AB2 — ddG values for each mutation.

---

### STEP 5: Run BeAtMuSiC (Fast Coarse-Grained Scan)

**URL:** http://babylone.ulb.ac.be/beatmusic/

**Why this tool:** Uses statistical potentials, very fast, scans entire interface at once. Different methodology provides independent validation.

**Reference:** Dehouck Y, Kwasigroch JM, Rooman M, Gilis D. "BeAtMuSiC: prediction of changes in protein-protein binding affinity on mutations." *Nucleic Acids Research* 41:W333-W339, 2013. PMID: 23723246.

**Step-by-step:**

1. Go to http://babylone.ulb.ac.be/beatmusic/
2. Upload `7urv.pdb`
3. The tool will automatically scan interface mutations
4. Record ddG predictions for your target residues

---

### STEP 6: Compile Results into a Consensus Table

After running all tools, fill in this table:

```
| Mutation | Exp. ddG    | mCSM-AB2 | mCSM-PPI2 | DDMut-PPI | BeAtMuSiC | Consensus     |
|          | (kcal/mol)  | (kcal/mol)| (kcal/mol)| (kcal/mol)| (kcal/mol)| Classification|
|----------|-------------|----------|-----------|-----------|-----------|---------------|
| Y260A    | >>+4.0      |          |           |           |           |               |
| Y261A    | +2.96       |          |           |           |           |               |
| Y70A     | +2.42       |          |           |           |           |               |
| S214A    | NOT TESTED  |          |           |           |           |               |
```

**How to fill in "Consensus Classification":**
- If ≥3 tools predict ddG > +2.0 → **"Hotspot (consensus)"**
- If ≥3 tools predict ddG +1.0 to +2.0 → **"Warm spot (consensus)"**
- If tools disagree → **"Uncertain — tools disagree"**

**What this gives you for the DAC:**
- Y260A, Y261A, Y70A: tools should agree with experimental data (validation)
- S214A: **the first computational prediction for this mutation** — genuinely novel

---

### STEP 7: Save Saturation Mutagenesis Heatmaps

For each target position (260, 261, 214), save the mCSM-PPI2 saturation mutagenesis heatmap showing predicted ddG for all 20 amino acids.

**Where to save:**
```
computational_validation/results/
├── mcsm_ab2_results.csv          ← ddG values from mCSM-AB2
├── mcsm_ppi2_ala_scan.csv        ← Full interface alanine scan
├── mcsm_ppi2_satmut_260.csv      ← All 20 amino acids at position 260
├── mcsm_ppi2_satmut_261.csv      ← All 20 amino acids at position 261
├── mcsm_ppi2_satmut_214.csv      ← All 20 amino acids at position 214
├── ddmut_ppi_results.csv         ← ddG values from DDMut-PPI
├── beatmusic_results.csv         ← ddG values from BeAtMuSiC
├── consensus_table.csv           ← Final compiled consensus table
└── heatmaps/
    ├── satmut_heatmap_260.png    ← Heatmap screenshot from mCSM-PPI2
    ├── satmut_heatmap_261.png
    └── satmut_heatmap_214.png
```

---

## How to Present These Results to the DAC

### Slide content recommendation:

**Title:** "Computational Validation: Multi-Tool Consensus Confirms Target Residues"

**Show:**
1. The consensus table (Step 6) — tools correctly predict published experimental results
2. The saturation mutagenesis heatmaps — predict which NNK substitutions will increase/decrease binding
3. One sentence: "We validated 4 computational tools against published experimental data, then used them to predict outcomes for untested mutations, providing a rational basis for interpreting our NNK library screening results."

### If the PI asks "How reliable are these predictions?":

**Honest answer:** "The best tool (mCSM-AB2) achieves Pearson correlation of 0.73-0.74 against experimental antibody-antigen binding data. However, a 2025 study in Nature Computational Science showed that all current methods have limited generalizability for antibody-antigen ddG prediction. That is why we use multiple tools and look for consensus, rather than relying on any single prediction. Importantly, our structural analysis — which uses no machine learning, only the atomic coordinates — independently validates the same residue ranking."

---

## Estimated Time to Complete All Steps

| Step | Tool | Time per mutation | Total time |
|------|------|:-----------------:|:----------:|
| 2 | mCSM-AB2 | 1-5 min | ~20 min (4 mutations) |
| 3a | mCSM-PPI2 Ala Scan | 5-10 min | ~10 min (full scan) |
| 3b | mCSM-PPI2 Sat Mut | 5-10 min/position | ~30 min (3 positions) |
| 4 | DDMut-PPI | 1-5 min | ~20 min (4 mutations) |
| 5 | BeAtMuSiC | 5-10 min | ~10 min (full scan) |
| 6 | Compile table | — | ~15 min |
| **Total** | | | **~2 hours** |

---

## Important Reminders

1. **Save everything** — screenshots, downloaded files, the exact PDB file used, the exact mutation codes entered
2. **Note the date** — web servers are updated periodically; note which version/date you used
3. **Record discrepancies** — if different tools give very different predictions, note this honestly. Disagreement is scientifically informative.
4. **Do NOT cherry-pick** — report results from all tools, not just the ones that agree with your expectations
5. **These are predictions** — until you do the experiment, they remain computational predictions. Label them clearly as such in any presentation.

---

*Document prepared: 2026-04-27. All web server URLs verified. All PMIDs confirmed.*
