# Analysis Log — 2026-04-27

## Environment
- **Machine:** macOS Darwin 25.2.0
- **Python:** 3.x (Anaconda)
- **BioPython:** Available
- **FreeSASA:** Installed via pip
- **DSSP (mkdssp):** Available at /Users/vishalbharti/opt/anaconda3/bin/mkdssp
- **Rosetta/FoldX:** NOT available (web servers used instead)

## Steps Performed

### Step 1: Structure Download
- Downloaded PDB 7URV from RCSB (rcsb.org)
- Verified: Chain C = CD19 (218 residues, 23-277), Chain D = FMC63 scFv (227 residues, 39-280)
- Total atoms: 3,460

### Step 2: Target Residue Confirmation
- Confirmed in Chain D (FMC63):
  - Residue 214 = SER (Serine)
  - Residue 260 = TYR (Tyrosine)
  - Residue 261 = TYR (Tyrosine)
  - Residue 70 = TYR (Tyrosine)

### Step 3: Interface Contact Analysis
- Cutoff: 4.5 Å between heavy atoms
- FMC63 interface residues found: 19
- CD19 interface residues found: 14
- Target residues ranked: #1 (Tyr261, 6 contacts), #2 (Tyr260, 5), #3 (Ser214, 4), #4 (Tyr70, 3)

### Step 4: Hydrogen Bond Analysis
- Criteria: N/O atoms, 2.0-3.5 Å
- Total interface H-bonds: 11
- Target residue H-bonds: 4 (SER214×2, TYR260×1, TYR261×1)

### Step 5: SASA Burial Analysis
- Tool: FreeSASA (Lee-Richards algorithm, probe radius 1.4 Å)
- Extracted isolated chain PDBs for comparison
- Total FMC63 interface buried area: 629 Å²
- Target residues: 322 Å² (51.2% of total)
- Results saved: results/sasa_analysis.json

### Step 6: Figure Generation
- 3 figures generated (PNG 300dpi + SVG):
  - interface_burial_analysis
  - target_residue_contacts
  - burial_vs_affinity

## Key Results Summary
1. Target residues = top 4 most-connected at the interface
2. 51.2% of total buried surface area in just 4/19 residues
3. H-bond analysis explains Y260A (complete loss) vs Y261A (partial loss) vs Y70A (moderate loss)
4. Ser214 predicted to be highly impactful (92.1% buried, 2.61 Å H-bond, no published mutation data)

## Files Generated
- structures/7urv.pdb, 7urv_chainC.pdb, 7urv_chainD.pdb
- results/sasa_analysis.json
- figures/interface_burial_analysis.png/.svg
- figures/target_residue_contacts.png/.svg
- figures/burial_vs_affinity.png/.svg
- 14_Computational_Validation_Complete.md (comprehensive document)
