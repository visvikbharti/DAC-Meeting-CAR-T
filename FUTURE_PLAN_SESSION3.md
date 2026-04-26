# Future Plan — Session 3 and Beyond

## DAC Meeting Preparation for Manpreet Kour
### Status as of Session 2 (2026-04-27)

---

## What Has Been Completed

### Session 1 (2026-04-26) — Literature Review
- 5 topic documents (01-05): TCR-pMHC kinetics, clustering, mechanical forces, affinity windows, integration
- 25-slide PPT with 9 source-annotated figures
- Q&A guide (18 anticipated questions with answers)
- Figure interpretations document
- Mega-document (COMPLETE_Reference_Document.md)

### Session 2 (2026-04-27) — Experimental Design + Systems
- 8 new documents (06-13): co-culture, E:T ratios, FACS panels, rechallenge, controls/stats, alternative systems, kinetics platforms, nanobody/VHH
- Expanded PPT to 33 slides (DAC_Presentation_v2.pptx)
- 5 new verified-data figures (FMC63 variants, antigen density, platform comparison, FACS panels, screening strategy)
- All 14 figures corrected for text overlap, saved as PNG + SVG
- Mega-document updated with Sections 6-12 and 23 new verified references
- FMC63 KD corrected to 5.1 nM (Seigner 2023), Q&A updated

---

## What Remains — Session 3 Topics

### Priority 1: Computational Validation (Rosetta/FoldX on FMC63-CD19)

**Goal:** In silico alanine scanning or saturation mutagenesis of the FMC63-CD19 interface to predict which mutations at Tyr260, Tyr261, Ser214 will increase/decrease affinity.

**Tasks:**
1. Download PDB 7URV (FMC63-CD19 cryo-EM structure, Singh et al. 2023)
2. Run computational alanine scanning using Rosetta or FoldX:
   - Calculate ddG (change in binding free energy) for all 20 amino acids at each position
   - Predict stabilizing vs. destabilizing mutations
   - Compare predictions with published experimental data (Y260A, Y261A, Y70A from Singh 2023)
3. Generate a heatmap figure showing predicted ddG values
4. Create document: `14_Computational_Validation.md`
5. Add computational validation slide to PPT

**Why this matters for DAC:** Demonstrates that the residue selection is computationally validated, not just based on buried SASA. If Rosetta predictions match the published Y260A/Y261A data, it strengthens the rationale.

**Requirements:** Rosetta or FoldX installed (or use web servers like DUET, mCSM, etc.)

### Priority 2: 4-1BB vs CD28 Costimulation Discussion -- COMPLETED

**Status:** DONE (2026-04-27). See `15_Costimulatory_Domain_Comparison.md`

**Goal:** Deep-dive into how costimulatory domain choice (4-1BB vs CD28) affects the affinity-function relationship in CARs.

**Tasks:**
1. Review published literature on 4-1BB vs CD28 costimulation:
   - Long et al. 2015, Nature Medicine (4-1BB ameliorates tonic signaling-driven exhaustion)
   - Majzner et al. 2020 (CD28ζ outperforms 4-1BBζ at low antigen density)
   - Differences in signaling kinetics, metabolism, persistence
2. Discuss whether FMC63 affinity variants will behave differently in CD28 vs 4-1BB CAR backbones
3. Create document: `15_Costimulatory_Domain_Comparison.md`
4. Add slide to PPT (or expand existing slide 14)

**Why this matters for DAC:** DAC will likely ask "which costimulatory domain are you using and why?" This provides the scientific rationale.

### Priority 3: Primary T Cell Validation Plan

**Goal:** Outline the plan for validating top CAR mutant candidates in primary human T cells (after Jurkat screening).

**Tasks:**
1. Protocol for primary T cell isolation, activation, lentiviral transduction
2. Donor considerations (n=4 donors recommended)
3. Key differences from Jurkat: cytotoxicity readout, real proliferation, full cytokine repertoire
4. In vivo xenograft model design (Raji-Luc2 in NSG mice)
5. Create document: `16_Primary_T_Cell_Validation.md`
6. Add slide to PPT

**Why this matters for DAC:** Shows the student has a plan beyond Jurkat cells. Addresses the Q&A about Jurkat limitations.

### Priority 4: Timeline Slide

**Goal:** Create a Gantt-chart style timeline showing the PhD project phases.

**Tasks:**
1. Define milestones:
   - Year 1: Construct design, mutagenesis, library construction, initial Jurkat screening
   - Year 2: Complete functional screening, rechallenge assays, exhaustion/memory phenotyping
   - Year 3: SPR/BLI kinetic characterization, primary T cell validation, correlation analysis
   - Year 4: Advanced validation (in vivo?), manuscript preparation, thesis writing
2. Generate timeline figure (Gantt chart)
3. Add timeline slide to PPT

### Priority 5: PPT Polish and Finalization

**Tasks:**
1. Update Presentation Outline slide (slide 2) with new slide listing
2. Ensure formatting consistency across all 33+ slides
3. Reorder slides if needed for logical flow
4. Replace any remaining old figures with user's manually refined versions
5. Add slide numbers
6. Final proofread of all text for accuracy and typos

---

## Suggested Session 3 Prompt

Copy and paste this prompt to start Session 3:

```
Hi,

We're continuing Manpreet Kour's DAC meeting prep for her CAR-T affinity
optimization project at CSIR-IGIB. Check your memory and read SESSION_SUMMARY.md
for full context.

Sessions 1-2 completed: all literature review documents (01-05), experimental
design documents (06-13 including nanobody/VHH), 33-slide PPT v2 with 14
verified-data figures, Q&A guide, mega-document — all pushed to GitHub
(visvikbharti/DAC-Meeting-CAR-T).

Now let's tackle the remaining items:

1. Computational validation — run in silico alanine scanning on FMC63-CD19
   (PDB 7URV) using Rosetta/FoldX or web servers. Compare predictions with
   published Y260A/Y261A/Y70A data from Singh et al. 2023. Generate a
   heatmap figure.

2. 4-1BB vs CD28 costimulation — deeper discussion of how costimulatory
   domain affects the affinity-function relationship. Which domain is
   Manpreet using and why?

3. Primary T cell validation plan — outline the protocol for validating
   top CAR candidates in primary human T cells after Jurkat screening.

4. Timeline slide — create a Gantt chart showing PhD project phases
   (Years 1-4).

5. PPT final polish — update outline slide, ensure consistency, add slide
   numbers, finalize.

Same rules: 100% authentic, verified citations, no hallucination. PI is
very particular.

Also check if the user manually refined any figures (affinity_windows_final.png
was saved) and incorporate into the PPT.
```

---

## Document Inventory (Current)

| # | File | Size | Status |
|---|------|------|--------|
| 01 | pMHC_TCR_Binding_Kinetics_and_Affinity.md | 18 KB | Complete |
| 02 | TCR_Clustering_and_Serial_Engagement.md | 18 KB | Complete |
| 03 | Mechanical_Forces_in_TCR_Signaling.md | 21 KB | Complete |
| 04 | Self_vs_NonSelf_TCR_Affinity_Windows.md | 19 KB | Complete |
| 05 | Comprehensive_Integration_for_DAC.md | 16 KB | Complete |
| 06 | Raji_Coculture_System.md | 11 KB | Complete |
| 07 | ET_Ratios_and_TimePoints.md | 25 KB | Complete |
| 08 | FACS_Panel_Design.md | 30 KB | Complete |
| 09 | Rechallenge_Assay_Protocols.md | 29 KB | Complete |
| 10 | Controls_and_Statistics.md | 15 KB | Complete |
| 11 | Alternative_Assay_Systems.md | 43 KB | Complete |
| 12 | Biophysical_Platforms_Kinetics.md | 47 KB | Complete |
| 13 | Nanobody_VHH_CAR_T_Cells.md | 29 KB | Complete |
| 14 | Computational_Validation.md | — | **Session 3** |
| 15 | Costimulatory_Domain_Comparison.md | — | **Session 3** |
| 16 | Primary_T_Cell_Validation.md | — | **Session 3** |
| — | COMPLETE_Reference_Document.md | 106 KB | Updated through Session 2 |
| — | DAC_Presentation_v2.pptx | 33 slides | Updated through Session 2 |
| — | QA_and_Slide_Narration.md | 32 KB | KD corrected in Session 2 |
| — | Figure_Interpretations_and_Data_Sources.md | 30 KB | Updated with 5 new figures |

### Figures (14 total, all PNG + SVG)
**Original 9 (corrected):** catch_vs_slip_bond, affinity_windows, optimal_dwell_time, car_vs_tcr_affinity, kinetic_proofreading, tcr_synapse_organization, signaling_cascade, serial_engagement, experimental_workflow

**New 5 (Session 2):** fmc63_variant_affinities, antigen_density_threshold, platform_comparison, facs_panel_summary, screening_strategy

**User-refined:** affinity_windows_final.png

---

*Plan created: 2026-04-27*
