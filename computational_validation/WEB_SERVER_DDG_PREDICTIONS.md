# Web Server-Based ddG Prediction Tools for FMC63-CD19 Interface

## Recommended Tools for Manpreet's Project (PDB 7URV)

This document lists verified web-based tools for predicting binding affinity changes (ddG) upon mutation at the FMC63-CD19 interface. These complement our structural analysis with energy-based predictions.

---

## Experimental Validation Benchmark

Before using any prediction tool, convert the published experimental KD values to ddG for comparison:

**Formula:** dG = RT × ln(KD), where R = 0.001987 kcal/(mol·K), T = 298.15 K

| Mutation | KD (nM) | dG (kcal/mol) | ddG vs WT (kcal/mol) | Classification |
|----------|---------|---------------|:--------------------:|:--------------:|
| WT FMC63 | 4.5 | -11.37 | 0 (reference) | — |
| Y70A | 275.3 | -8.95 | **+2.42** | Hotspot (>2.0) |
| Y261A | 682.5 | -8.41 | **+2.96** | Hotspot (>2.0) |
| Y260A | No binding | — | **>>+4.0** | Critical hotspot |

*KD source: Singh et al., 2023, Science Immunology (PMC10228544)*

**Convention:** ddG > 2.0 kcal/mol = hotspot; ddG > 1.0 kcal/mol = warm spot; ddG < 1.0 = neutral

---

## Tier 1: Recommended Web Servers (No Installation)

### 1. mCSM-AB2 (Antibody-Antigen Specific — HIGHEST PRIORITY)

| Field | Detail |
|-------|--------|
| URL | https://biosig.lab.uq.edu.au/mcsm_ab2/ |
| Input | PDB file + mutation (chain, WT residue, position, mutant residue) |
| Output | Predicted ddG (kcal/mol) for binding affinity change |
| Accuracy | Pearson r = 0.73-0.74 on antibody-antigen benchmarks (1,810 mutations) |
| Why use it | **Specifically trained on antibody-antigen data** — most appropriate for FMC63-CD19 |
| Reference | Myung et al., Bioinformatics 36:1453-1459, 2020. PMID: 31665262 |

### 2. mCSM-PPI2 (General Protein-Protein Interface)

| Field | Detail |
|-------|--------|
| URL | https://biosig.lab.uq.edu.au/mcsm_ppi2/ |
| Input | PDB + mutation; has "Alanine Scanning" and "Saturation Mutagenesis" modes |
| Output | ddG (kcal/mol) + heatmap for saturation mutagenesis |
| Accuracy | Pearson r = 0.82 on S8338 dataset |
| Modes | Single mutation, alanine scanning (all interface residues), saturation mutagenesis (all 19 substitutions) |
| Reference | Rodrigues et al., Nucleic Acids Res 47:W338-W344, 2019. PMID: 31114883 |

### 3. DDMut-PPI (Newest Deep Learning Approach)

| Field | Detail |
|-------|--------|
| URL | https://biosig.lab.uq.edu.au/ddmut_ppi/ |
| Input | PDB + chain IDs + mutation(s) |
| Output | ddG (kcal/mol) |
| Accuracy | Pearson r = 0.75; validated on SKEMPI 2.0 (3,268 mutations) and AB-Bind (645 antibody mutations) |
| Method | Graph convolutional network + ProtT5 protein language model embeddings |
| Reference | Zhou et al., Nucleic Acids Res 52:W207-W214, 2024. PMID: 38783112 |

### 4. BeAtMuSiC (Fast Coarse-Grained)

| Field | Detail |
|-------|--------|
| URL | http://babylone.ulb.ac.be/beatmusic/ |
| Input | PDB of protein-protein complex |
| Output | ddG for all possible interface mutations (fast, coarse-grained) |
| Accuracy | Pearson r = 0.55 (full dataset), 0.76 (top 90%) |
| Reference | Dehouck et al., Nucleic Acids Res 41:W333-W339, 2013. PMID: 23723246 |

### 5. Robetta Alanine Scanning

| Field | Detail |
|-------|--------|
| URL | https://robetta.bakerlab.org/alascansubmit.jsp |
| Input | PDB coordinates + chain partner definitions |
| Output | ddG_bind for each interface residue mutated to Ala (emailed) |
| Accuracy | 79% hotspots correctly identified (233 mutations, 19 complexes) |
| Reference | Kortemme & Baker, PNAS 99:14116-14121, 2002 |

### 6. DrugScorePPI (Purpose-Built for Alanine Scanning)

| Field | Detail |
|-------|--------|
| URL | https://cpclab.uni-duesseldorf.de/dsppi/ |
| Input | PDB of protein-protein complex |
| Output | ddG for WT→Ala mutations + bar plot + 3D visualization |
| Accuracy | Validated against 309 experimental alanine scanning results |
| Reference | Krueger & Gohlke, Nucleic Acids Res 38:W480-W486, 2010. PMID: 20511591 |

---

## Tier 2: Standalone Software (If Available)

### FoldX (Free Academic License)

| Field | Detail |
|-------|--------|
| URL | https://foldxsuite.crg.eu/ |
| License | Free for academic/non-profit; register online |
| Commands | RepairPDB → AlaScan → PositionScan (saturation mutagenesis) |
| Accuracy | AUC 0.87 for binder classification; improved force field (2025) |
| Reference | Schymkowitz et al., Nucleic Acids Res 33:W382-W388, 2005. PMID: 15980494 |

### Rosetta flex_ddG

| Field | Detail |
|-------|--------|
| URL | https://github.com/Kortemme-Lab/flex_ddG_tutorial |
| Cost | ~1 day per mutation on single CPU; needs HPC for full scanning |
| Accuracy | Pearson r = 0.65 (best on antibody-antigen subset) |
| Reference | Barlow et al., J Phys Chem B 122:5389-5399, 2018. PMID: 29401388 |

---

## Recommended Protocol for This Project

### Step 1: Validate tools with known mutations
Submit Y260A, Y261A, Y70A to each web server. Compare predicted ddG with experimental ddG. Check if tools correctly rank Y260A > Y261A > Y70A.

### Step 2: Run full alanine scan
Use mCSM-PPI2's alanine scanning mode on entire FMC63-CD19 interface. This will rank ALL interface residues by predicted binding contribution.

### Step 3: Run saturation mutagenesis at target positions
Use mCSM-PPI2's saturation mutagenesis mode for positions 214, 260, 261. This generates a 20-amino-acid heatmap for each position — predicting which substitutions increase vs decrease affinity.

### Step 4: Consensus prediction
Combine results from 3+ tools. Residues predicted as hotspots by multiple tools are high-confidence targets.

### Step 5: Present as multi-tool table
| Residue | Exp. ddG | mCSM-AB2 | mCSM-PPI2 | DDMut-PPI | BeAtMuSiC | Consensus |
|---------|---------|----------|-----------|-----------|-----------|-----------|
| Y260A | >>+4.0 | ? | ? | ? | ? | Hotspot |
| Y261A | +2.96 | ? | ? | ? | ? | Hotspot |
| Y70A | +2.42 | ? | ? | ? | ? | Hotspot |
| S214A | **?** | ? | ? | ? | ? | **Predicted** |

**Important note:** Manpreet should run these web servers herself and fill in the actual predicted values. The predictions can then be compared with experimental data to demonstrate computational validation.

---

## Important Caveat

A 2025 study in *Nature Computational Science* (DOI: 10.1038/s43588-025-00823-8) found that **no current method reliably predicts antibody-antigen ddG** on truly independent datasets. All tools show limited generalizability. The best approach is multi-tool consensus + structural analysis (which we have done).

**For the DAC:** Present the structural analysis (contacts, burial, H-bonds) as the PRIMARY validation. Web server ddG predictions are SUPPORTING evidence. The fact that structural metrics correctly rank the published mutations (Y260A > Y261A > Y70A) is strong independent validation.

---

*All URLs verified via web search. All PMIDs confirmed. Date: 2026-04-27.*
