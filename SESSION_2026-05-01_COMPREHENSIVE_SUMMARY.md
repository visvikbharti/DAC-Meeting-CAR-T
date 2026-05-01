# Session Summary — 2026-05-01

## DAC Meeting CAR-T Project | Comprehensive context for next session

This document is the authoritative record of all work completed on **2026-05-01**. It is designed to allow a future session (or another collaborator) to pick up cold without losing context. Read this in full before resuming work.

---

## 1. Where the project stands as of 2026-05-01

### Student & PI
- **Student**: Manpreet Kour, PhD scholar, CSIR-IGIB, AcSIR Reg. 10BB25J02028
- **PI**: Dr. Kausik Chakraborty (Chief Scientist, CSIR-IGIB) — *highly skeptical of AI; zero tolerance for fabricated/hallucinated citations*
- **Co-PI**: Dr. Ankesh Kumar Jaiswal (Project Scientist, CSIR-IGIB)
- **DAC committee**: Dr. Arpan Parichha, Dr. Chetana Sachidanandan, Dr. Sheetal Gandotra
- **Vishal** (the user, vishalvikashbharti@gmail.com, GitHub visvikbharti) is helping his friend Manpreet prepare DAC materials

### Project
- **Title**: Advancing CAR-T Cell Therapy by Understanding the Kinetics of Ag-Ab Interaction Parameters
- **System**: Anti-CD19 CAR (FMC63 scFv); target CD19 ECD; structure PDB 7URV
- **Library**: NNK saturation at 4 positions
  - **PRIMARY (novel — never published)**: S214, Trp212
  - **SECONDARY** (NNK saturation goes beyond He et al. 2023's single Ala): Y260, Y261
- **In vivo**: NSG (or NSG-MHC-DKO if rest >4 wk) + NALM-6-luciferase
- **In vitro**: NALM-6 with graded CD19 expression
- **Biophysics**: Expi293F-produced scFv + SF-CD19 (Laurent 2021); SPR + 2D micropipette adhesion frequency

### GitHub
- Private repo: `visvikbharti/DAC-Meeting-CAR-T`
- Main branch: `main`
- Today's commits (5): `0672896`, `9610d7e`, `40a6088`, `bc0c3da`, `e482ede`

---

## 2. Manpreet's stated questions and objectives (as of 2026-05-01)

She has defined her thesis around two questions, each paired with one objective. **These are the canonical statements — earlier reformulations I proposed were rejected**:

> **Question 1**: Can tuning the affinity affect the amplitude of the CAR-T signal?
> **Objective 1**: To determine CAR-T cell efficacy in vivo and in vitro using scFv mutant CAR library.
>
> **Question 2**: Is there any affinity window for CAR-T cells having better therapeutic outcomes?
> **Objective 2**: To do biophysical characterization of scFv mutants which performed better in vivo as well as in vitro.

### Sub-objective structure (from her DAC1_draft2.pptx)

- **Objective 1.1** (slides 21-26): To develop scFv mutant library of CAR & make mutant CARPOOL T cells
- **Objective 1.2** (slide 27): To test mutant CARPOOL T cells in vivo using luciferinized NALM-6 mouse model *(heading was originally a duplicate of 1.1; corrected this session)*
- **Objective 1.3, 2.1, 2.2…** : not yet drafted — slides 28-33 are blank

---

## 3. Manpreet's experimental plan (as described by Vishal, 2026-05-01)

### In vivo arm
1. Make CAR-T cell library with scFv mutants (S214, Trp212, Y260, Y261).
2. Inject into luciferinized NALM-6-bearing humanized mice.
3. Sample T cells **day 1, 2, 4** — for **activation/exhaustion kinetics** (CD69, CD25, PD-1, TIM-3, LAG-3, TOX). *Vishal explicitly clarified this is NOT for memory phenotyping.*
4. Surviving mice get **21-day rest** for memory contraction.
5. Rechallenge with fresh NALM-6-luciferase.
6. Sample T cells day 1, 2, 4 post-rechallenge — for **recall response kinetics**.
7. Sacrifice → harvest spleen, lymph node, bone marrow.
8. Sort memory T cells → bulk NGS → identify which scFv mutants enrich in the memory pool.

### In vitro arm
- CAR-T library co-cultured with NALM-6 cells expressing different CD19 levels.
- Identify mutants behaving differently from WT.

### Biophysics arm (top hits only)
- Purify scFv in **Expi293F**.
- Purify CD19 in **HEK293S** *(per her stated plan; flagged as wrong choice — see §6.4)*.
- Measure KD, kon, koff, dwell time by **SPR**.
- 2D kinetics by **micropipette adhesion frequency assay**.

---

## 4. What was delivered today (2026-05-01)

### 4.1 Documents created

| File | Lines / Size | Purpose |
|---|---|---|
| `18_Experimental_Design_Expert_Review.md` | ~720 lines | Comprehensive confounder audit across in vivo + in vitro + biophysics arms; verified citations; §3a activation/exhaustion kinetics; §5.2 CD19 production protocol; §11 aims/objectives critique |
| `19_Aims_and_Objectives_Reframing.md` | ~150 lines | Standalone concise critique of her Q1/Q2 + Obj 1/Obj 2; reformulation suggestions; proposed 3-4 aim structure (rejected by Manpreet — she kept original) |
| `Experimental_Design_Reviewer_Slides.pptx` | 16 slides | Integration-ready deck with reviewer-level content |
| `Specific_Aims_Slide.pptx` | 1 slide | Standalone single slide for direct DAC deck integration (based on the rejected 4-aim reformulation — kept for archival reference) |
| `build_reviewer_slides.py` | build script | Python-pptx generator for reviewer slides |
| `build_aims_slide.py` | build script | Python-pptx generator for the standalone aims slide |
| `.fix_citations.py` | helper script | Singh→He correction across 16 files (84 replacements) |
| `.fix_dac_draft.py` | helper script | DAC1_draft2 slide 20 + slide 27 edits |

### 4.2 Documents modified — citation corrections (Singh→He)

84 replacements applied across 16 markdown files via `.fix_citations.py`:

| File | Replacements |
|---|---:|
| `17_Novelty_Strategy_and_Residue_Selection.md` | 16 |
| `computational_validation/FIGURE_INTERPRETATIONS.md` | 12 |
| `12_Biophysical_Platforms_Kinetics.md` | 9 |
| `computational_validation/HOW_THIS_ANALYSIS_WORKS.md` | 7 |
| `computational_validation/COMPLETE_GUIDE_FOR_MANPREET.md` | 7 |
| `computational_validation/mCSM_AB2_RESULTS_INTERPRETATION.md` | 7 |
| `14_Computational_Validation.md` | 6 |
| `computational_validation/14_Computational_Validation_Complete.md` | 6 |
| `README.md` | 3 |
| `FUTURE_PLAN_SESSION3.md` | 3 |
| `SESSION_SUMMARY.md` | 2 |
| `COMPLETE_Reference_Document.md` | 2 |
| `QA_and_Slide_Narration.md` | 2 |
| `Figure_Interpretations_and_Data_Sources.md` | 1 |
| `16_Primary_T_Cell_Validation.md` | 1 |
| `computational_validation/WEB_SERVER_DDG_PREDICTIONS.md` | 1 |

**Files NOT modified (intentional)**:
- `07_ET_Ratios_and_TimePoints.md` — contains a *different* "Selli, Singh et al. 2023" *STAR Protocols* paper (PMC9826863) where Singh N is **senior author**, not first author (Selli ME is first). This is a real verified paper, kept unchanged.
- `18_Experimental_Design_Expert_Review.md` — intentionally discusses the Singh→He correction itself.

### 4.3 Manpreet's draft updated — `DAC1_draft2.pptx`

**Slide 20 (Objectives)**:
| Slot | Before | After |
|---|---|---|
| Oval **1** | (empty) | "To determine CAR-T cell efficacy in vivo and in vitro using scFv mutant CAR library" |
| Oval **2** | (empty) | "To do biophysical characterization of scFv mutants which performed better in vivo as well as in vitro" |
| Oval **3** | "To Understand the Parameters of Ag-Ab Binding which Affects the Amplitude of the Signal" | unchanged |

**Slide 27 (in vivo experimental design)** — heading corrected:
- Before: "OBJECTIVE 1.2 To develop scFv mutant library of CAR & make mutant CARPOOL T cells" *(was a duplicate of slides 21-26 heading)*
- After: "OBJECTIVE 1.2 To test mutant CARPOOL T cells in vivo using luciferinized NALM-6 mouse model"

**Backup**: `DAC1_draft2.backup.pptx` saved in repo for safe rollback.

---

## 5. Citations verified during this session (PubMed-confirmed)

### NEW corrections applied today

| Citation | Wrong (earlier sessions) | Correct (verified 2026-05-01) |
|---|---|---|
| FMC63-CD19 cryo-EM / PDB 7URV / Sci Immunol 2023 | "Singh et al." | **He C, Mansilla-Soto J, Khanra N, Hamieh M, Bustos V, Paquette AJ, Garcia Angus A, Shore DM, Rice WJ, Khelashvili G, Sadelain M, Meyerson JR.** *Sci Immunol* 8(81):eadf1426, 2023. **PMID 36867678**. PMCID PMC10228544. DOI 10.1126/sciimmunol.adf1426. |
| Original FMC63 scFv | PMID 9220002 (was a phage λ paper) | **Nicholson IC et al.** *Mol Immunol* 34(16-17):1157-65, 1997. **PMID 9566763** |
| HEK293S GnTI⁻ origin | PMID 12077305 (was unrelated) | **Reeves PJ et al.** *PNAS* 99(21):13419-24, 2002. **PMID 12370423** |
| 2D adhesion frequency origin | PMID 9591180 (was unrelated) | **Chesla SE, Selvaraj P, Zhu C.** *Biophys J* 75(3):1553-72, 1998. **PMID 9726957** |
| SF-CD19 stabilized monomer | "Zajc 2021" (Zajc not on author list) | **Laurent E et al.** *ACS Synth Biol* 10(5):1184-1198, 2021. **PMID 33843201**. Senior author Traxlmayr (same group as Seigner 2023). |
| Optimal CAR affinity window 10-60 nM | PMID 36389699 (was Wei et al. on bispecifics) | **Mao R, Kong W, He Y.** *Front Immunol* 13:1032403, 2022. **PMID 36325345** |
| Caruso 2015 EGFR CAR | "EGFRvIII" (was actually wild-type EGFR) | **Caruso HG et al.** "Tuning Sensitivity of CAR to EGFR Density…" *Cancer Res* 75:3505-3518, 2015. **PMID 26330164**. Wild-type EGFR (nimotuzumab vs cetuximab). |
| Liu 2015 CAR affinity | "Cancer Immunol Res, GD2 CAR" | **Liu X et al.** "Affinity-Tuned ErbB2 or EGFR CAR T Cells…" *Cancer Res* 75:3596-3607, 2015. **PMID 26330166**. ErbB2/EGFR (not GD2); journal is Cancer Research. |
| Park 2017 ROR1 CAR | PMID 28676346 (unverifiable; was Acinetobacter paper) | Use **Hudecek M et al.** "Receptor affinity and extracellular domain modifications affect tumor recognition by ROR1-specific chimeric antigen receptor T cells." *Clin Cancer Res* 19(12):3153-64, 2013. **PMID 23620405** |

### Additional PMIDs verified (no prior error; just confirmed)

| Citation | PMID |
|---|---|
| Brehm MA et al. 2019 NSG-MHC-DKO *FASEB J* 33:3137-51 | **30383447** |
| Brentjens RJ et al. 2003 NALM-6 SCID-Beige *Nat Med* | **12579196** |
| Brentjens RJ et al. 2007 NALM-6 + FMC63 *Clin Cancer Res* | **17855649** |
| Castellanos-Rueda R et al. 2022 speedingCARs *Nat Commun* | **36323661** |
| Daniels KG et al. 2022 CAR motif library *Science* | **36480602** |
| Davila ML et al. 2013 mouse CD19 CAR *PLoS One* | **23585867** |
| Davila ML et al. 2014 clinical 19-28z *Sci Transl Med* | **24553386** |
| Drent E et al. 2019 CD28+4-1BB *Clin Cancer Res* | **30979735** |
| Eyquem J et al. 2017 TRAC knock-in *Nature* | **28225754** |
| Gattinoni L et al. 2011 Tscm *Nat Med* | **21926977** |
| Ghorashian S et al. 2019 low-affinity CAT CAR *Nat Med* | **31477906** |
| Goodman/Roybal 2022 CAR Pooling *Sci Transl Med* | **36350984** |
| Huppa JB et al. 2010 TCR-pMHC in situ *Nature* | **20164930** |
| Kawalekar OU et al. 2016 4-1BB Tcm *Immunity* | **26885860** |
| Kivioja T et al. 2011 UMIs *Nat Methods* | **22101854** |
| LaFleur MW et al. 2019 CHIME *Nat Commun* | **30971695** |
| Li W et al. 2014 MAGeCK *Genome Biol* | **25476604** |
| Liu B et al. 2014 TCR catch bonds *Cell* | **24725404** |
| Long AH et al. 2015 4-1BB exhaustion *Nat Med* | **25939063** |
| Lugli E et al. 2013 Tscm sorting *Nat Protoc* | **23222456** |
| Mackay LK et al. 2013 Trm pathway *Nat Immunol* | **24162776** |
| Mahnke YD et al. 2013 memory subset markers *Eur J Immunol* | **24258910** |
| Majzner RG et al. 2020 antigen density *Cancer Discov* | **32193224** |
| Milone MC et al. 2009 4-1BB CAR *Mol Ther* | **19384291** |
| Rios X et al. 2023 barcoded CAR *Mol Ther* | **37705245** |
| Roth TL et al. 2018 non-viral CRISPR *Nature* | **30022017** |
| Sabatino M et al. 2016 CAR Tscm *Blood* | **27226436** |
| Sallusto F et al. 1999 Tcm/Tem *Nature* | **10537110** |
| Seigner J et al. 2023 FMC63-CD19 KD = 5.1 nM *Sci Rep* | **38155191** |
| Shultz LD et al. 2012 humanized mouse review *Nat Rev Immunol* | **23059428** |
| Sotillo E et al. 2015 CD19 antigen escape *Cancer Discov* | **26583447** |
| Wunderlich M et al. 2018 NSGS *PLoS One* | **30586420** |
| Xu Y et al. 2014 CAR Tscm persistence *Blood* | **24782509** |

---

## 6. Key scientific findings established this session

### 6.1 Activation / exhaustion kinetics — day 1, 2, 4 sampling (from Manpreet's clarification)

Day 1, 2, 4 sampling is for activation/exhaustion kinetic profiling — **NOT memory phenotyping**.

| Day | Activation markers | Effector function | Early exhaustion |
|---|---|---|---|
| Day 1 (~24 h) | CD69 peak; CD25 ramping; ICOS/OX40 induction | IFN-γ, TNF-α, IL-2 initiating | PD-1 mRNA induction |
| Day 2 (~48 h) | CD25 plateau; CD69 declining; ICOS/OX40 sustained | Granzyme B / perforin granule loading | PD-1 surface protein elevated; TIM-3 / LAG-3 emerging |
| Day 4 | Effector differentiation | IFN-γ / TNF-α / cytotoxicity peak | PD-1, TIM-3, LAG-3 sustained; TOX accumulating |

**Key reference**: Long et al. 2015 *Nat Med* PMID 25939063 (4-1BB ameliorates tonic-signaling-driven CAR-T exhaustion).

**Sort-then-NGS strategy recommended**: at each timepoint, sort CAR+ cells into bins (CD69+ vs CD69-, PD-1ʰⁱ vs PD-1ˡᵒ, TOX+ vs TOX-) → variant NGS in each bin → identifies which mutants enrich in each phenotype.

### 6.2 Memory phenotype — terminal sacrifice readout

Memory phenotype (Tn / Tscm / Tcm / Tem / Trm) is read out from terminal sacrifice tissues (spleen + LN + BM). **Critical marker**: CD95 distinguishes Tscm from Tn — without CD95, Tscm are mis-scored.

### 6.3 Mouse model — NSG (or NSG-MHC-DKO if rest >4 wk)

For adoptive CAR-T transfer to NALM-6, full immune reconstitution is **not needed**. Use plain immunodeficient host:
- **NSG**: standard, ≤21-d rest fine
- **NSG-MHC-DKO** (Brehm 2019 PMID 30383447): substantially delayed xeno-GvHD — use if any rest period exceeds 4 weeks
- **AVOID**: PBMC- or HSC-humanized mice (xeno-GvHD onset ~28 d will mask memory readout)

### 6.4 CD19 production — Expi293F + SF-CD19, NOT HEK293S

**HEK293S in the field universally means the GnTI⁻ line** (high-mannose only glycans; for crystallography). **Wrong choice** for SPR/BLI binding studies of FMC63 mutants.

**Correct choice**: **Expi293F + SF-CD19 stabilized monomer construct (Laurent 2021, PMID 33843201)**. SF-CD19 = "SuperFolder" stabilizing mutations from yeast-display directed evolution. Solves WT-CD19-ECD aggregation problem. Same construct used by Seigner 2023 (PMID 38155191) to get the consensus FMC63-CD19 KD = 5.1 nM by Biacore T200.

### 6.5 SPR protocol benchmark (from Seigner 2023)

```
Chip:           Biotin CAPture S Series (Cytiva), re-loadable
Ligand on chip: Biotinylated FMC63-Avi-His scFv (~1000 RU), oriented
Analyte:        SF-CD19 monomer, 5 conc. (0.5, 4, 20, 100, 500 nM), single-cycle kinetics
Buffer:         PBS + 0.1% BSA + 0.05% Tween-20, pH 7.4
T / flow:       25 °C / 30 µL/min
Assoc / dissoc: 600 s / 1200 s (koff ~5×10⁻⁴ s⁻¹ → t½ ~22 min, need ≥3 t½)
Regeneration:   3 M GuHCl + 1 M NaOH, 120 s
Fitting:        1:1 Langmuir
Replicates:     n ≥ 3 independent runs
```

### 6.6 FMC63 diabody artifact

Seigner 2023 reports FMC63-scFv exhibits a **20% diabody dimer equilibrium** that SEC alone cannot remove. **For top 3 mutants, run Fab format as orthogonal validation** — eliminates the diabody artifact.

### 6.7 2D micropipette / catch bonds — novelty for any CAR

**No published 2D adhesion frequency or BFP catch-bond data exists for any CAR-antigen system.** Genuinely novel for FMC63-CD19. Requires external collaboration (suggested labs: Cheng Zhu Georgia Tech, Baoyu Liu Utah, Hai Qi Tsinghua). Throughput ~5-10 mutants/month — reserve for top 2-3 hits.

### 6.8 Tiered biophysics strategy

| Tier | Method | # mutants | Purpose |
|---|---|---|---|
| 1 | Functional screens | 50-100 | Identify functionally interesting variants |
| 2 | BLI / Octet | 20-30 | Rapid kinetic triage |
| 3 | SPR (Biacore) | 6-10 | Primary 3D kinetic dataset |
| 4 | 2D adhesion frequency | 2-3 | Membrane-context kinetics; novel |
| 5 | BFP catch bond (Phase 2) | 1-2 | Mechanobiology; secondary novelty |

### 6.9 Pooled in vivo scFv variant CAR-T screens — no precedent

All published CAR pooled screens (Daniels 2022, Goodman/Roybal 2022, Castellanos-Rueda 2022, Rios 2023) run the **pooled phase in vitro** with in vivo work limited to per-construct validation. **No published precedent for fully in vivo pooled scFv variant screen with NGS readout.** Either novel opportunity or technical bottleneck — DAC will probably ask both.

---

## 7. Open issues for next session

### 7.1 Unmodified items in Manpreet's DAC1_draft2.pptx

1. **Slide 20 slot 3** — "To Understand the Parameters of Ag-Ab Binding which Affects the Amplitude of the Signal" — reads like an overarching thesis goal. May want to either move to a header or remove (only 2 stated objectives).
2. **Slide 27 timeline labels** — every step has "Day 0" except one "Day 4" — placeholders need filling (Day 0 inject, Day 1/2/4 blood, Day 21 rechallenge, etc.).
3. **Slide 27 sacrifice timing** — "Sacrifice at day 14" for post-rechallenge cohort. May want to align with kinetic timeline (day 4-7 effector window, day 14 contraction, day 28 long-term recall).
4. **Slides 28-33** — blank — Objective 2 sub-objectives still to be drafted (biophysical characterization workflow).

### 7.2 Items requiring Manpreet/PI input

1. Confirm "humanized mouse" intent — PBMC/HSC engrafted, or plain immunodeficient NSG host for adoptive CAR-T?
2. Confirm "HEK293S" intent — GnTI⁻ specifically, or generic HEK293/Expi293 by reflex?
3. CAR-detection reagent in her vector — CD19-Fc tetramer? truncated CD34? EGFRt?
4. Biacore T200 / 8K accessibility at CSIR-IGIB (or collaborative access at NCBS / IISc / IIT-B)?
5. z-Movi (Lumicks) availability in India (NCBS Bangalore?)
6. 2D / BFP collaborator — which lab to engage?
7. Mouse budget approval (≥65 mice for in vivo arm)

### 7.3 Binary deck citations still needing manual fix

- `DAC_Presentation_v2.pptx` (33 slides, large) — may still contain "Singh" references in slide text (markdown files corrected, but binary slides not edited)
- `Computational_Validation_Presentation.pptx` (12 slides) — same caveat
- These need manual correction in PowerPoint or rebuild from corrected markdown

### 7.4 Residue mapping (load-bearing for NGS design)

S214, Trp212, Y260, Y261 must be mapped onto the FMC63 VL-Whitlow218-VH sequence to confirm whether all four positions fit within a single 300-bp Illumina read. **This determines whether DNA barcoding is mandatory or whether single-amplicon sequencing suffices.** Action: pull annotated FMC63 sequence (Addgene FMC63-218-CAR vectors or He 2023 PDB 7URV chain definitions); mark VL/linker/VH boundaries and the four residues.

### 7.5 Translational / Phase 2

- Aim 4 (primary T cell validation in NSG-MHC-DKO) discussed but not committed — depends on scope/timeline
- Catch bond / BFP — defer to Phase 2 collaboration

---

## 8. Files in repo as of end of 2026-05-01

### Top-level documents (16 markdown + 1 mega-document)
```
README.md
SESSION_SUMMARY.md
SESSION_2026-05-01_COMPREHENSIVE_SUMMARY.md  ← this file (2026-05-01)
COMPLETE_Reference_Document.md
01_pMHC_TCR_Binding_Kinetics_and_Affinity.md
02_TCR_Clustering_and_Serial_Engagement.md
03_Mechanical_Forces_in_TCR_Signaling.md
04_Self_vs_NonSelf_TCR_Affinity_Windows.md
05_Comprehensive_Integration_for_DAC.md
06_Raji_Coculture_System.md
07_ET_Ratios_and_TimePoints.md
08_FACS_Panel_Design.md
09_Rechallenge_Assay_Protocols.md
10_Controls_and_Statistics.md
11_Alternative_Assay_Systems.md
12_Biophysical_Platforms_Kinetics.md
13_Nanobody_VHH_CAR_T_Cells.md
14_Computational_Validation.md
15_Costimulatory_Domain_Comparison.md
16_Primary_T_Cell_Validation.md
17_Novelty_Strategy_and_Residue_Selection.md
18_Experimental_Design_Expert_Review.md           ← new 2026-05-01 (~720 lines)
19_Aims_and_Objectives_Reframing.md               ← new 2026-05-01
Figure_Interpretations_and_Data_Sources.md
QA_and_Slide_Narration.md
FUTURE_PLAN_SESSION3.md
```

### computational_validation/ (6 markdown + figures + scripts + structures)
```
14_Computational_Validation_Complete.md
COMPLETE_GUIDE_FOR_MANPREET.md
FIGURE_INTERPRETATIONS.md
HOW_THIS_ANALYSIS_WORKS.md
NEXT_STEPS_WEB_SERVER_GUIDE.md
WEB_SERVER_DDG_PREDICTIONS.md
mCSM_AB2_RESULTS_INTERPRETATION.md
figures/  results/  scripts/  structures/  logs/
```

### Presentations
```
DAC1_draft2.pptx                                  ← Manpreet's working draft (modified 2026-05-01)
DAC1_draft2.backup.pptx                           ← backup of pre-modification state
DAC_Presentation_v2.pptx                          ← prior 33-slide deck (still has "Singh" in slides)
DAC_Presentation.pptx                             ← original 25-slide deck
Computational_Validation_Presentation.pptx       ← 12-slide deck (still has "Singh" in slides)
draft1.pptx                                       ← original
projectproposal.pptx                              ← original
Experimental_Design_Reviewer_Slides.pptx          ← new 2026-05-01 (16 slides)
Specific_Aims_Slide.pptx                          ← new 2026-05-01 (1 slide; based on rejected reformulation)
```

### Build / helper scripts
```
build_ppt.py                                     ← original PPT builder
build_reviewer_slides.py                         ← new 2026-05-01
build_aims_slide.py                              ← new 2026-05-01
.fix_citations.py                                ← Singh→He script
.fix_dac_draft.py                                ← DAC1_draft2 update script
```

### Figures (in figures/, ~19 PNG + SVG pairs)

---

## 9. Today's git history (2026-05-01)

```
e482ede  Populate Manpreet's DAC1_draft2.pptx slide 20 with her stated objectives
bc0c3da  Add standalone Specific Aims slide for direct DAC deck integration
40a6088  Add aims/objectives critique and 4-aim reframing
9610d7e  Correct Singh -> He attribution for Sci Immunol 2023 / PDB 7URV paper
0672896  Add expert experimental-design review for thesis plan + integration-ready slides
```

Prior commits (Sessions 1-3, Apr 26-27):
```
fbf59db  Add novelty strategy addressing Singh et al. 2023 overlap concern
84b569f  Fix optimal CAR affinity window to 10-60 nM (Mao et al. 2022 clinical data)
05e7525  Complete DAC meeting documentation for CAR-T affinity optimization project
```

---

## 10. Lessons captured (memory-worthy feedback)

1. **Manpreet wants HER framing of objectives kept** — do not reformulate her Q1/Q2 + Obj 1/Obj 2 into a 3-4 aim structure unless she explicitly asks. The 4-aim version was useful as a reviewer suggestion but was rejected.
2. **Day 1, 2, 4 sampling is for activation/exhaustion** (CD69, CD25, PD-1, TIM-3, LAG-3, TOX), NOT memory. Memory readout = terminal sacrifice (end of 21-d rest, post-rechallenge).
3. **PI is hyper-strict about citations** — every PMID must be web-verified. Multiple errors caught this session (Singh→He, Zajc→Laurent, Mao PMID, Park unverifiable, etc.). Always verify before final use.
4. **"HEK293S" almost always means GnTI⁻ line in the field** — wrong choice for functional kinetics; switch to Expi293F. But always confirm with the student first.
5. **"Humanized mouse" is being used loosely** — for adoptive CAR-T transfer, NSG (not PBMC/HSC-humanized) is what's needed. Clarify terminology.
6. **Subagent citation verification is unreliable** — Agent 3 cited "Zajc 2021" for SF-CD19 paper (Laurent is the actual first author); Agent 1 had hallucinated authors "Frey NV, Engels B" in a Singh-attributed reference. Spot-check every key citation.

---

## 11. NEXT-SESSION PROMPT (copy-paste ready)

> Hi,
>
> I'm Vishal, continuing to help my friend **Manpreet Kour** prepare for her PhD DAC meeting at CSIR-IGIB. PI is **Dr. Kausik Chakraborty**. The project is anti-CD19 CAR-T affinity optimization with FMC63 scFv NNK saturation library at S214, Trp212 (primary, novel), Y260, Y261 (secondary). Repo: `visvikbharti/DAC-Meeting-CAR-T` at `/Users/vishalbharti/Downloads/DAC-Meeting-CAR-T-MANPREET`.
>
> Before we proceed, please:
> 1. Read your auto-memory files (`MEMORY.md` and the linked entries) for the project context.
> 2. Read `SESSION_2026-05-01_COMPREHENSIVE_SUMMARY.md` in the repo for the full state as of last session — that document is the authoritative record. Critical highlights:
>    - Manpreet keeps her own Q1/Q2 + Objective 1/Objective 2 framing — do NOT reformulate to a 3/4-aim structure unless she asks.
>    - Day 1, 2, 4 sampling = activation/exhaustion kinetics; memory readout = terminal sacrifice.
>    - "Singh et al. 2023" was a wrong attribution — correct is **He C et al. 2023** *Sci Immunol* 8:eadf1426 PMID 36867678. 16 markdown files were find/replaced last session; binary `.pptx` files (DAC_Presentation_v2, Computational_Validation_Presentation) may still contain "Singh" — flag if seen.
>    - For CD19 production use **Expi293F + SF-CD19** (Laurent 2021 PMID 33843201, NOT Zajc).
>    - PI is highly skeptical of AI; **every citation requires PMID verification before being included**.
> 3. Read `18_Experimental_Design_Expert_Review.md` for the comprehensive confounder audit if context-dependent decisions are needed.
> 4. Check `DAC1_draft2.pptx` for Manpreet's current draft state (slide 20 objectives populated; slide 27 in vivo design heading corrected; slides 28-33 still blank).
>
> Open items I may want to work on this session (will pick from):
> - Slide 27 timeline labels (currently mostly "Day 0" placeholders)
> - Drafting sub-objective slides for Objective 2 (biophysical characterization, slides 28-33)
> - FMC63 residue mapping (S214, Trp212, Y260, Y261 onto VL-218-VH sequence)
> - Manual correction of "Singh" in DAC_Presentation_v2.pptx and Computational_Validation_Presentation.pptx
> - Anything PI flagged on the latest draft
>
> Tell me what's outstanding and we'll prioritize.

---

*Document prepared 2026-05-01 23:59 IST as authoritative session record. All claims web-verified against PubMed where citations are involved.*
