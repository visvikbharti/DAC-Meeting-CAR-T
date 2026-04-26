# Session Summary — DAC Meeting CAR-T Project

## Session 1: 2026-04-26

### Context
Vishal is helping his friend Manpreet Kour (PhD Scholar, CSIR-IGIB) prepare materials for her first DAC meeting. Project title: "Advancing CAR-T Cell Therapy by Understanding the Kinetics of Ag-Ab Interaction Parameters." PI: Dr. Kausik Chakraborty. Co-PI: Dr. Ankesh Kumar Jaiswal.

### What Was Done

**Literature Research (web-verified citations):**
- Performed 20+ targeted web searches across PubMed, journal sites
- Verified all landmark references (Valitutti 1995, McKeithan 1995, Liu et al. 2014, Stone et al. 2009, Huang et al. 2010, Kalergis et al. 2001, Davenport et al. 2018, Crites et al. 2014, etc.)

**Documents Created (01-05):**
1. `01_pMHC_TCR_Binding_Kinetics_and_Affinity.md` — 18 KB
2. `02_TCR_Clustering_and_Serial_Engagement.md` — 18 KB
3. `03_Mechanical_Forces_in_TCR_Signaling.md` — 21 KB
4. `04_Self_vs_NonSelf_TCR_Affinity_Windows.md` — 19 KB
5. `05_Comprehensive_Integration_for_DAC.md` — 16 KB
6. `COMPLETE_Reference_Document.md` — 94 KB mega-document
7. `DAC_Presentation.pptx` — 25 slides, widescreen
8. `QA_and_Slide_Narration.md` — narration + 18 Q&As
9. `Figure_Interpretations_and_Data_Sources.md`

**Figures Generated (9 total in figures/):**
- catch_vs_slip_bond.png, affinity_windows.png, optimal_dwell_time.png
- car_vs_tcr_affinity.png, kinetic_proofreading.png, tcr_synapse_organization.png
- signaling_cascade.png, serial_engagement.png, experimental_workflow.png

**GitHub Repo:** https://github.com/visvikbharti/DAC-Meeting-CAR-T (private)

---

## Session 2: 2026-04-27

### What Was Done

**Part A: Experimental Design Protocols (Documents 06-10)**

Comprehensive experimental design research using 7 parallel research agents, 100+ web searches across PubMed/PMC, ATCC, vendor sites (BioLegend, Miltenyi, Thermo Fisher, Cytiva, Sartorius, NanoTemper). All citations verified.

**Documents Created:**
1. `06_Raji_Coculture_System.md` (11 KB) — ATCC specs for Raji/Jurkat/K562, co-culture setup (plate format, seeding, volumes), 5 cytotoxicity readout methods, tiered assay strategy
2. `07_ET_Ratios_and_TimePoints.md` (25 KB) — E:T ratio justification (0.2:1 to 10:1), time points for cytotoxicity/activation/exhaustion, Jurkat-specific caveats, 7 verified references
3. `08_FACS_Panel_Design.md` (30 KB) — 4 complete panels (exhaustion, activation, memory, TOX intracellular), 15+ verified antibody clones with cat#, CD107a protocol, CAR detection (Miltenyi REA1297), laser configs for FACSCanto II
4. `09_Rechallenge_Assay_Protocols.md` (29 KB) — 3 published protocol variants (Wang 2019, effector transfer, Ghassemi/Selli chronic), CellTrace Violet protocol, counting methods, Jurkat caveats
5. `10_Controls_and_Statistics.md` (15 KB) — 8 essential controls, FMO vs isotype, Dunnett's test with optimal allocation, NNK screening strategy (single-position then combinatorial), QC metrics

**Part B: Alternative Systems & Kinetics Platforms (Documents 11-12)**

Research prompted by Vishal's questions about Raji limitations, alternative systems for tunable CD19 density, and binding kinetics platform comparison.

6. `11_Alternative_Assay_Systems.md` (30+ KB) — NALM-6 CD19-KO + graded re-expression (Majzner 2020), K562-CD19, CHO-CD19 (Low/Med/High for xCELLigence), SLB systems (5 papers), 2D kinetics (micropipette/BFP), FACS solutions (Raji-GFP-Luc2, counting beads), 4-phase implementation strategy, 19 verified references
7. `12_Biophysical_Platforms_Kinetics.md` (47 KB) — SPR vs BLI vs MST vs ITC vs flow cytometry vs 2D kinetics comparison, published FMC63-CD19 KD values (5.1 nM Seigner 2023, 4.5 nM Singh 2023), 7-platform comparison table, instrument costs, CSIR-IGIB availability notes

**Mega-document updated:** `COMPLETE_Reference_Document.md` now includes Part II (Sections 6-10) with experimental design summaries + 14 new verified references.

### Key Findings

**Published FMC63-CD19 Kinetics (Verified):**
- KD = 5.1 nM (Seigner et al. 2023, *Sci Rep*, Biacore T200): kon = 1.0 x 10^5 M^-1 s^-1, koff = 5.3 x 10^-4 s^-1
- KD = 4.5 nM (Singh et al. 2023, *Science Immunology*)
- Published range: 0.3-47 nM (>100-fold variation due to artifacts)

**Published FMC63 Affinity Variants at Target Residues:**
- Y260A: No detectable SPR binding (>5000 nM) — avidity-rescued modest activity
- Y261A: KD = 682.5 nM (152-fold weaker than WT)
- Y70A: KD = 275.3 nM (61-fold weaker)

**Citation Correction:** "Guedan et al. 2023" should be **Seigner et al. 2023** (*Scientific Reports* 13:23024, PMC10754921)

**Literature Gap Identified:** No published 2D kinetics (micropipette adhesion, BFP) for ANY CAR-antigen interaction. This is a significant gap and potential novelty angle for the project.

**Antigen Density Matters:** CAR-T function drops sharply below ~2,000 CD19 molecules/cell (Majzner et al. 2020). NALM-6 CD19-KO + graded re-expression is the gold standard system for studying this.

### What Remains for Next Session(s)
1. Refinement of PPT slides with experimental design details
2. Nanobody/VHH-based CAR section (from original PPT)
3. ~~4-1BB vs CD28 costimulation deeper discussion~~ **COMPLETED (Session 3)** -- see `15_Costimulatory_Domain_Comparison.md`
4. Computational validation (alanine scanning / Rosetta on FMC63-CD19 interface)
5. Primary T cell validation plan
6. Timeline slide refinement
7. Integration of alternative systems into experimental plan slide

---

## Session 3: 2026-04-27 (continued)

### What Was Done

**4-1BB vs CD28 Costimulatory Domain Comprehensive Comparison**

Performed 20+ targeted web searches across PubMed, journal sites, and clinical trial databases. All citations verified.

**Document Created:**
- `15_Costimulatory_Domain_Comparison.md` -- Comprehensive comparison document covering:
  1. Signaling pathways (CD28: PI3K/AKT/mTOR via YMNM/PYAP motifs; 4-1BB: TRAF1/2/3 --> canonical + noncanonical NF-kB)
  2. Functional differences (cytotoxicity, persistence, memory phenotype, exhaustion, metabolism, cytokine profiles, expansion kinetics)
  3. Clinical data from all three FDA-approved anti-CD19 CAR-T products (JULIET, ZUMA-1, TRANSCEND NHL 001)
  4. Affinity-costimulation interaction analysis (Drent et al. 2019, Majzner et al. 2020)
  5. Recommendation for Manpreet: 4-1BB backbone for primary screen, both backbones for validation
  6. Prepared DAC answer with follow-up Q&A responses
  7. 15 verified references with PMIDs

**Key Verified References Added:**
- Long et al. 2015, *Nat Med* 21:581-590 (PMID: 25939063) -- 4-1BB ameliorates tonic signaling exhaustion
- Kawalekar et al. 2016, *Immunity* 44:380-390 (PMID: 26885860) -- 4-1BB=Tcm/OXPHOS; CD28=Tem/glycolysis
- Majzner et al. 2020, *Cancer Discov* 10:702-723 (PMID: 32193224) -- CD28 better at low antigen density
- Drent et al. 2019, *Clin Cancer Res* 25:4014-4025 (PMID: 30979735) -- Affinity-costimulation interaction
- Cappell & Kochenderfer 2021, *Nat Rev Clin Oncol* 18:715-727 (PMID: 34230645) -- Definitive review
- Philipson et al. 2020, *Sci Signal* 13:eaay8248 (PMID: 32234960) -- ncNF-kB survival mechanism
- Salter et al. 2018, *JCI Insight* 3:e121322 (PMID: 30232281) -- TRAF requirement for 4-1BB function
- Schuster et al. 2019, *NEJM* 380:45-56 (PMID: 30501490) -- JULIET trial
- Neelapu et al. 2017, *NEJM* 377:2531-2544 (PMID: 28099430) -- ZUMA-1 trial
- Abramson et al. 2020, *Lancet* 396:839-852 (PMID: 32888407) -- TRANSCEND NHL 001
