# Advancing CAR-T Cell Therapy by Understanding the Kinetics of Ag-Ab Interaction Parameters

## DAC Meeting Documentation

PhD Project | CSIR-IGIB | AcSIR

**PI:** Dr. Kausik Chakraborty (Chief Scientist, CSIR-IGIB)
**Co-PI:** Dr. Ankesh Kumar Jaiswal (Project Scientist, CSIR-IGIB)
**Student:** Manpreet Kour (AcSIR Reg. 10BB25J02028)

---

## Overview

This repository contains comprehensive, citation-verified documentation for the first Doctoral Advisory Committee (DAC) meeting. The project investigates how the biophysical parameters of antigen-scFv interaction — particularly affinity, kinetic rates, and force-dependent bond stability — determine CAR-T cell signaling, activation, exhaustion, and memory formation.

**Total:** 16 reference documents, 3 presentations, 19 figures, computational validation with mCSM-AB2 predictions.

---

## Documents

### Part I: Literature Review

| # | Document | Description |
|---|----------|-------------|
| 01 | [pMHC-TCR Binding Kinetics & Affinity](01_pMHC_TCR_Binding_Kinetics_and_Affinity.md) | KD, kon, koff fundamentals; kinetic proofreading; optimal dwell time |
| 02 | [TCR Clustering & Serial Engagement](02_TCR_Clustering_and_Serial_Engagement.md) | Serial engagement model; TCR microclusters; nanoclusters; CD45 exclusion |
| 03 | [Mechanical Forces in TCR Signaling](03_Mechanical_Forces_in_TCR_Signaling.md) | Catch vs slip bonds; piconewton force measurements; mechanotransduction |
| 04 | [Self vs Non-Self Affinity Windows](04_Self_vs_NonSelf_TCR_Affinity_Windows.md) | Thymic selection thresholds; affinity ceiling concept; CAR optimization |
| 05 | [Comprehensive Integration](05_Comprehensive_Integration_for_DAC.md) | Unified framework; quantitative parameter tables; project hypothesis |

### Part II: Experimental Design & Protocols

| # | Document | Description |
|---|----------|-------------|
| 06 | [Raji Co-Culture System](06_Raji_Coculture_System.md) | Cell line specs (ATCC), co-culture setup, 5 cytotoxicity readout methods |
| 07 | [E:T Ratios & Time Points](07_ET_Ratios_and_TimePoints.md) | E:T ratio justification, time points, activation/exhaustion marker kinetics |
| 08 | [FACS Panel Design](08_FACS_Panel_Design.md) | 4 panels with verified antibody clones, fluorochromes, laser configs |
| 09 | [Rechallenge Assay Protocols](09_Rechallenge_Assay_Protocols.md) | 3 published protocol variants, CellTrace Violet, Jurkat caveats |
| 10 | [Controls & Statistics](10_Controls_and_Statistics.md) | 8 controls, Dunnett's test, NNK screening strategy, QC metrics |
| 11 | [Alternative Assay Systems](11_Alternative_Assay_Systems.md) | NALM-6 tunable CD19, CHO-CD19, SLB, 2D kinetics, FACS solutions |
| 12 | [Biophysical Platforms](12_Biophysical_Platforms_Kinetics.md) | SPR vs BLI vs MST vs ITC vs 2D kinetics; published FMC63 KD values |

### Part III: CAR Design & Future Directions

| # | Document | Description |
|---|----------|-------------|
| 13 | [Nanobody/VHH CAR-T Cells](13_Nanobody_VHH_CAR_T_Cells.md) | Anti-CD19 VHH clones, cilta-cel, SL1716, VHH as future direction |
| 15 | [Costimulatory Domain Comparison](15_Costimulatory_Domain_Comparison.md) | CD28 vs 4-1BB signaling, clinical data, affinity interaction, backbone recommendation |
| 16 | [Primary T Cell Validation](16_Primary_T_Cell_Validation.md) | Isolation, transduction, functional assays, xenograft model, ethics |

### Part IV: Computational Validation

| # | Document | Description |
|---|----------|-------------|
| 14 | [Computational Validation](14_Computational_Validation.md) | PDB 7URV structural analysis, contacts, H-bonds, SASA burial, mCSM-AB2 predictions |

**Computational validation directory** (`computational_validation/`):

| Document | Description |
|----------|-------------|
| [Complete Guide for Manpreet](computational_validation/COMPLETE_GUIDE_FOR_MANPREET.md) | Everything explained from scratch — every analysis step, every column, every result, PI Q&A |
| [mCSM-AB2 Results Interpretation](computational_validation/mCSM_AB2_RESULTS_INTERPRETATION.md) | Detailed interpretation of all 18 mutation predictions |
| [Figure Interpretations](computational_validation/FIGURE_INTERPRETATIONS.md) | How each computational figure was generated and what the data means |
| [How This Analysis Works](computational_validation/HOW_THIS_ANALYSIS_WORKS.md) | Step-by-step explanation of methods for non-experts |
| [Web Server Guide](computational_validation/NEXT_STEPS_WEB_SERVER_GUIDE.md) | How to run mCSM-AB2/DDMut-PPI with exact input format and interpretation |
| [Web Server ddG Tools](computational_validation/WEB_SERVER_DDG_PREDICTIONS.md) | 6 verified tools compared with accuracy benchmarks |

### Reference Documents

| Document | Description |
|----------|-------------|
| [Complete Reference Document](COMPLETE_Reference_Document.md) | Mega-document (106 KB) merging all topics with full detail |
| [Q&A and Slide Narration](QA_and_Slide_Narration.md) | 25-slide narration + 18 anticipated DAC questions (KD corrected to 5.1 nM) |
| [Figure Interpretations](Figure_Interpretations_and_Data_Sources.md) | Data sources and interpretation guide for all 14 figures |
| [Session Summary](SESSION_SUMMARY.md) | Complete record of all sessions and work done |
| [Future Plan](FUTURE_PLAN_SESSION3.md) | Remaining tasks and next session prompt |

---

## Presentations

| File | Slides | Description |
|------|:------:|-------------|
| `DAC_Presentation_v2.pptx` | 33 | Main DAC presentation — literature review + experimental design |
| `Computational_Validation_Presentation.pptx` | 12 | Computational validation — structural analysis, mCSM-AB2, timeline |
| `DAC_Presentation.pptx` | 25 | Original presentation (superseded by v2) |

---

## Experimental System

- **CAR construct:** Anti-CD19 CAR (FMC63 scFv)
- **Costimulatory domain:** 4-1BB recommended (Drent et al. 2019: 4-1BB more sensitive to affinity changes than CD28)
- **Target antigen:** CD19 (PDB: 7URV, cryo-EM: Singh et al. 2023)
- **Key interacting residues:** Tyr260, Tyr261, Ser214
- **Published FMC63-CD19 KD:** 5.1 nM (Seigner et al. 2023) / 4.5 nM (Singh et al. 2023) by SPR
- **Mutagenesis:** Site-saturation mutagenesis using NNK primers
- **Published variant data:** Y260A (no binding), Y261A (682 nM), Y70A (275 nM) — Singh et al. 2023
- **Functional readouts:** CD69 activation, cytotoxicity, exhaustion (PD-1/TIM-3/LAG-3), memory, cytokines
- **Kinetic characterization:** SPR (Biacore T200) primary; BLI (Octet) screening
- **Cell system:** Jurkat (screening) → Primary T cells (validation) → NSG mice (in vivo, optional)

## Computational Validation Highlights

**Structural analysis** (PDB 7URV, BioPython + FreeSASA):
- Target residues are the **top 4 most-connected** at the FMC63-CD19 interface
- Account for **51.2% of total interface buried area** (322/629 Å²)
- H-bond analysis explains published data: Y260A loses critical side-chain H-bond → no binding

**mCSM-AB2 predictions** (18 mutations, all High confidence):
- **Y260:** ALL hotspots (ΔΔG -2.88 to -4.79) — every substitution catastrophic
- **Y261:** ALL hotspots (ΔΔG -2.33 to -4.95) — every substitution severe
- **S214:** ALL neutral (ΔΔG -0.91 to +0.90) — tolerates mutations, ideal for fine-tuning
- **S214D predicted to INCREASE affinity** (+0.90 kcal/mol) — potential gain-of-function

## Key Findings

- koff is a better predictor of T cell activation than KD
- Optimal dwell time ~34s for CD8+ T cells (Kalergis et al. 2001)
- CARs operate at 0.1-10 nM KD vs TCRs at 1-100 uM — fundamentally different signaling regime
- Lower-affinity CARs can outperform higher-affinity ones (Ghorashian et al. 2019)
- 4-1BB CARs are more sensitive to affinity changes than CD28 CARs (Drent et al. 2019)
- No published 2D kinetics exist for any CAR-antigen system — literature gap
- CAR function threshold at ~2,000 CD19 molecules/cell (Majzner et al. 2020)
- Cilta-cel (CARVYKTI) is the first FDA-approved VHH-based CAR-T product (anti-BCMA, 2022)

## Figures (19 total, all PNG + SVG)

**Literature & Experimental Design (9):** catch_vs_slip_bond, affinity_windows, optimal_dwell_time, car_vs_tcr_affinity, kinetic_proofreading, tcr_synapse_organization, signaling_cascade, serial_engagement, experimental_workflow

**Data Figures (5):** fmc63_variant_affinities, antigen_density_threshold, platform_comparison, facs_panel_summary, screening_strategy

**Computational Validation (5):** interface_burial_analysis, target_residue_contacts, burial_vs_affinity, mcsm_ab2_ddg_predictions, project_timeline

## Citation Integrity

All references verified through PubMed/PMC and journal website searches. Quantitative values traced to verified published sources. Uncertainties explicitly flagged. Zero tolerance for hallucinated data. mCSM-AB2 predictions from actual web server output (not fabricated).

---

> This repository is maintained for academic research purposes.
