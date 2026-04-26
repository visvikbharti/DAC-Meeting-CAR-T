# Rechallenge / Re-stimulation Assay Protocols for CAR-T Cell Persistence and Serial Killing

## Context
- **Project:** Anti-CD19 CAR affinity optimization (FMC63 scFv)
- **System:** Jurkat T cells transduced with anti-CD19 CAR, co-cultured with Raji cells (CD19+ Burkitt lymphoma)
- **Purpose:** Evaluate functional persistence, serial killing capacity, and exhaustion susceptibility of CAR-T constructs with varying affinity
- **Document date:** 2026-04-27
- **Verification status:** All information sourced from published literature and manufacturer protocols; citations provided throughout

---

## 1. RECHALLENGE ASSAY PROTOCOL DESIGN

### 1.1 General Principle

The rechallenge (or "repetitive tumor challenge") assay evaluates whether CAR-T cells retain cytotoxic function after repeated encounters with fresh target cells. It provides a convenient approach to evaluate CAR-T cell functional potency: exhausted T cells may respond well in an initial round but lose capability in subsequent rounds.

**Reference:** Wang et al. (2019) "In vitro tumor cell rechallenge for predictive evaluation of chimeric antigen receptor T cell antitumor function." Journal for ImmunoTherapy of Cancer. [PMC6719706]

### 1.2 Protocol Variant A: Continuous Co-culture with Tumor Re-addition (Wang et al., 2019)

This is a widely cited, well-validated protocol from the Bhoj lab (University of Pennsylvania).

**Initial Setup:**
- Plate format: 96-well flat-bottom tissue culture plate
- Effector cells: 4,000 CAR+ T cells per well
- Target cells: 16,000 tumor cells per well
- Initial E:T ratio: 1:4 (effector:target)
- Medium: Standard T cell medium (RPMI + 10% FBS + supplements); co-culture medium has NO exogenous cytokine supplementation

**Rechallenge Schedule (4 rounds over 7 days):**
- Day 0: Initial co-culture (4,000 CAR-T + 16,000 tumor cells)
- Day 2 (Round 2): Carefully remove 50 uL media from top of well (without disturbing cells); add 32,000 fresh tumor cells; E:T ratio drops to approximately 1:12
- Day 4 (Round 3): Repeat media removal + add 32,000 fresh tumor cells; E:T ratio approximately 1:20
- Day 6 (Round 4): Repeat media removal + add 32,000 fresh tumor cells

**KEY DESIGN FEATURE:** In this variant, T cells are NOT physically recovered/separated between rounds. The co-culture is continuous, and fresh tumor cells are simply added on top. This simulates progressive tumor burden.

**Harvest Protocol:**
- Cells are harvested using 0.05% trypsin-EDTA at 37C for 5 minutes
- Transfer to round-bottom plates
- Centrifuge, wash twice with staining buffer
- Stain with antibody panels for flow cytometry
- DAPI viability staining

**Readouts at Each Timepoint (Days 1, 3, 5, 7):**
- Live cells (DAPI-negative)
- Tumor burden (CD45-negative population)
- CAR+ T cell absolute numbers (CD45+, CAR+ gating)
- T cell activation markers: 4-1BB and CD69 co-expression (6-24 hours post co-culture)
- Exhaustion markers: PD-1, LAG-3, TIM-3
- Memory phenotype: CD45RO and CD62L

**Optimization Notes:**
- E:T ratios need to be adjusted per CAR-tumor combination
- If tumor cells express PD-L1 or other immunoinhibitory molecules, use higher E:T ratio
- A pilot study is recommended to determine conditions where the most potent CAR-T cells can eliminate >80% of tumor cells
- Target cells must be completely lysed before proceeding to rechallenge in some variant protocols

### 1.3 Protocol Variant B: Effector Cell Transfer (Harvest-and-Replate)

This is an alternative approach where T cells are physically recovered between rounds.

**Initial Setup:**
- Cell numbers: 2 x 10^6 effector T cells + 1 x 10^6 target cells (e.g., Raji)
- E:T ratio: 2:1
- Plate format: 24-well GREX plates or standard 24-well plates
- Medium: Standard T cell culture medium

**Rechallenge Schedule (4 rounds, every 3 days):**
- Day 0: Co-culture 2 x 10^6 effector + 1 x 10^6 Raji cells
- Day 3 (Round 2): Harvest all cells, mix thoroughly, collect samples for flow cytometry and cell counting; add 1 x 10^6 fresh Raji cells to the existing culture
- Day 6 (Round 3): Repeat sampling + add 1 x 10^6 fresh Raji cells
- Day 9 (Round 4): Repeat sampling + add 1 x 10^6 fresh Raji cells
- Day 12: Final analysis

**Variant with full separation:**
- After 72 hours of killing, CAR-T cells are removed from the plate, counted, and added to a new plate with freshly plated target cells at 1:1 E:T ratio
- CAR-T transfer repeated for four total rounds of stimulation

**References:**
- Bio-protocol: Anti-tumor Efficacy of CD19 CAR-T in a Raji B Cell Xenografted Mouse Model [PMC10127058]
- Engineering of an Avidity-Optimized CD19-Specific Parallel CAR [PMC8863855]

### 1.4 Protocol Variant C: Short-Interval Rechallenge (Every 18-24 Hours)

Used by some groups for aggressive stress testing:

**Setup:**
- E:T ratio: 1:3 (for CD19-CAR:tumor) or 1:4 (varies by CAR target)
- Fresh target cells (same starting number as initial) added every 18-24 hours
- Duration: 5-7 days total
- Cell counting by flow cytometry at endpoint

**Reference:** Alizadeh et al. (2019) "IL15 Enhances CAR-T Cell Antitumor Activity by Reducing mTORC1 Activity and Preserving Their Stem Cell Memory Phenotype." Cancer Immunology Research 7(5):759-772. [PMC6687561]

### 1.5 Summary Table: Rechallenge Protocol Variants

| Parameter | Variant A (Wang) | Variant B (Transfer) | Variant C (Aggressive) |
|-----------|-------------------|----------------------|------------------------|
| E:T ratio (initial) | 1:4 | 2:1 | 1:3 to 1:4 |
| Plate format | 96-well flat | 24-well / GREX | 24-well |
| Rounds | 4 | 4 | 5-7 |
| Interval | Every 2 days | Every 3 days | Every 18-24 hours |
| Total duration | 7 days | 12 days | 5-7 days |
| T cell recovery | No (continuous) | Partial or full | No (continuous) |
| Fresh targets added | 32,000/round | 1 x 10^6/round | Same as initial |
| Cytokines in co-culture | None | None | None |

---

## 2. STRESS TEST / REPETITIVE STIMULATION PROTOCOLS

### 2.1 Chronic Stimulation Protocol (Ghassemi Lab, UPenn)

This is the gold-standard protocol for deliberately driving CAR-T cells to exhaustion through chronic antigen stimulation. Published as a detailed step-by-step protocol in STAR Protocols.

**Reference:** Ghassemi et al. (2022) "Inducing T cell dysfunction by chronic stimulation of CAR-engineered T cells targeting cancer cells in suspension cultures." STAR Protocols. [PMC9826863]

**Setup:**
- Effector cells: CAR+ T cells (0.25-2 x 10^6 per culture)
- Target cells: Nalm6 cells (CD19+ B-ALL line), with BID gene knocked out to make them partially resistant to killing (this ensures chronic antigen exposure rather than rapid target elimination)
- E:T ratio: 1:8 (1 CAR+ T cell per 8 Nalm6 cells)
- Medium: R10 (RPMI + 10% FBS + supplements)
- NO exogenous cytokines added
- Performed in triplicate
- Cell concentration: 0.25-2 x 10^6 cells/mL

**Stimulation Schedule:**
- E:T ratio re-established every 2 days (every 48 hours)
- At each restimulation: sample 50-100 uL aliquots for analysis
- Count CAR+ T cells and tumor cells by flow cytometry
- Calculate fold-change of both cell populations
- Replenish medium based on pH indicator and cell density
- Culture at 37C, 5% CO2

**Timeline of Exhaustion:**
- Days 0-6/7: PEAK activation phase; potent effector function; T cell expansion
- Days 6-7: Peak CAR-T expansion (optimal for harvesting activated cells)
- Days 10-13: Transition phase; beginning loss of effector function
- Days 13-17: DYSFUNCTION phase; T cells lose ability to control tumor growth; fold-change <1 and/or Nalm6 fold-change >1
- Days 17+: T cell contraction

**Downstream Characterization (at key timepoints):**
- Purify CAR-T cells on Day 0, Day 6-7 (peak), and Day 13-17 (dysfunctional)
- Genomic analysis (ATAC-seq)
- Transcriptomic analysis (RNA-seq)
- Metabolic profiling
- Exhaustion markers by flow cytometry

### 2.2 Exhaustion Markers to Measure

Based on multiple published CAR-T exhaustion studies:

**Surface Markers (by flow cytometry):**
- PD-1 (Programmed Death-1) -- primary exhaustion marker
- TIM-3 (T-cell Immunoglobulin and Mucin-domain containing-3)
- LAG-3 (Lymphocyte-Activation Gene 3)
- CTLA-4
- TIGIT
- CD39

**Co-expression is key:** Single marker expression is insufficient. Co-expression of 2 or more inhibitory receptors (e.g., PD-1+/TIM-3+ or PD-1+/LAG-3+/TIM-3+ triple-positive) is a stronger indicator of true exhaustion.

**Transcription Factors:**
- T-bet (decreased in exhaustion)
- Blimp-1 (increased in exhaustion)
- TOX (master regulator of T cell exhaustion)

**Functional Readouts:**
- Decreased IFN-gamma secretion (ELISA or intracellular staining)
- Decreased TNF-alpha production
- Decreased IL-2 production
- Reduced degranulation (CD107a surface expression)
- Reduced killing capacity in subsequent rounds

**Reference:** Long et al. (2015) "4-1BB costimulation ameliorates T cell exhaustion induced by tonic signaling of chimeric antigen receptors." Nature Medicine 21(6):581-590. [PMC4458184]

### 2.3 Cytokine Supplementation Between Rounds

**IMPORTANT DISTINCTION:** Most published rechallenge/stress test protocols deliberately omit exogenous cytokines during co-culture to test the T cells' intrinsic survival and functional capacity. However, cytokine conditions during the EXPANSION phase (before the rechallenge assay) significantly affect outcomes.

**During T cell expansion (before co-culture):**
- IL-2: 70-100 IU/mL (standard; added every 48 hours)
- IL-7 + IL-15: 10 ng/mL each (alternative; promotes less differentiated phenotype)
- IL-7 + IL-15 + IL-21: Triple combination (most memory-preserving)

**During co-culture/rechallenge:**
- Standard: NO cytokine supplementation (tests intrinsic T cell function)
- Some protocols add low-dose IL-2 (10-50 IU/mL) to sustain viability without masking functional differences

**Key Finding:** CAR-T cells expanded with IL-15 showed superior recursive killing capacity compared to IL-2-expanded cells in rechallenge assays, attributed to reduced mTORC1 activity and preserved stem cell memory phenotype.

**References:**
- Alizadeh et al. (2019) Cancer Immunology Research [PMC6687561]
- Xu et al. (2019) "CAR-T cells expanded with IL-7/IL-15 mediate superior antitumor effects." Protein & Cell 10(10):764-769. [PMC6776495]

---

## 3. PROLIFERATION ASSESSMENT DURING RECHALLENGE

### 3.1 CellTrace Violet (CTV) Dye Dilution Protocol

CellTrace Violet is the current standard for tracking cell proliferation by flow cytometry. Each daughter cell receives half the fluorescence of the parent, creating distinct generation peaks.

**Manufacturer:** Thermo Fisher Scientific, Cat# C34557

**Step-by-Step Protocol:**

1. **Prepare cells:** Count cells, adjust to 1 x 10^6 cells/mL
2. **Reconstitute dye:** Add 20 uL DMSO to one vial of CellTrace Violet stock to make 5 mM stock solution
3. **Prepare working solution:** Dilute stock into 20 mL pre-warmed PBS (37C) for 5 uM final working concentration
4. **Pellet cells:** Centrifuge 10 mL of cells at 300 x g for 5 minutes, pour off supernatant
5. **Stain:** Resuspend cell pellet in 10 mL of CellTrace Violet working solution (5 uM)
6. **Incubate:** 20 minutes in a 37C water bath (protected from light)
7. **Quench:** Add 40 mL OpTmizer T Cell Expansion SFM (or culture medium with 10% FBS) to absorb unbound dye; incubate 5 minutes
8. **Wash:** Centrifuge at 300 x g for 5 minutes; resuspend pellet in pre-warmed culture medium
9. **Analyze Day 0:** Run a small aliquot on flow cytometer to confirm labeling (single bright peak)

**Detection:** Excitation 405 nm (violet laser); Emission ~450 nm (Pacific Blue/BV421 channel)

**Capacity:** Can resolve up to 8-10 generations of cell division before signal is indistinguishable from autofluorescence.

**Alternative: CFSE (Carboxyfluorescein Succinimidyl Ester)**
- Same principle as CTV
- Concentration: 5 uM working solution
- Detected on FITC channel (excitation 492 nm, emission 517 nm)
- Limitation: significant spectral overlap with GFP (relevant if target cells are GFP-labeled)
- CTV is preferred over CFSE for multi-color flow panels due to less spectral spillover

**Reference:** Thermo Fisher Protocol: CellTrace Violet Cell Proliferation Kit [thermofisher.com]

### 3.2 Cell Counting Methods

**a) Flow Cytometry with Counting Beads (Recommended for rechallenge assays):**
- Add a known number of fluorescent counting beads (e.g., CountBright Absolute Counting Beads, Thermo Fisher) to each sample
- Acquire at least 1,000 bead events
- Calculate: Absolute cell count = (cell events / bead events) x known beads added
- Advantages: Simultaneous phenotyping + counting; distinguishes live CAR-T from tumor cells; accounts for variable sample volumes
- Essential for rechallenge assays where you need separate counts of CAR-T cells and residual tumor cells

**b) Automated Cell Counter (e.g., Countess, Luna):**
- Trypan blue exclusion for viability
- Quick, requires small volume (10 uL)
- Does not distinguish CAR-T from tumor cells in mixed culture (limitation for rechallenge assays)
- Best used for total cell counts before/after separation

**c) Hemocytometer:**
- Manual counting with trypan blue
- Low throughput, observer-dependent
- Same limitation as automated counter for mixed cultures

**For rechallenge assays, flow cytometry-based counting is strongly recommended** because it allows simultaneous identification of:
- CAR+ T cells (CD45+, CAR+)
- Residual tumor cells (CD45- or CD19+/GFP+)
- Dead cells (viability dye exclusion)

### 3.3 Fold Expansion Calculations

**Basic fold expansion:**
```
Fold Expansion = (Absolute cell count at timepoint N) / (Absolute cell count at timepoint 0)
```

**Cumulative fold expansion (across multiple rounds):**
```
Cumulative Fold Expansion = Product of (fold change at each round)
```

**Key proliferation indices from dye dilution (CTV/CFSE):**

- **Division Index:** Average number of divisions for ALL cells in the original population (including undivided cells)
- **Proliferation Index:** Average number of divisions for RESPONDING cells only (excluding undivided cells)
- **Replication Index:** Fold expansion of RESPONDING cells only (total daughter cells from responding population / number of responding cells in parent generation)

Software: FlowJo Proliferation Modeling tool can automatically calculate these from dye dilution histograms.

---

## 4. PUBLISHED RECHALLENGE PROTOCOLS: VERIFIED REFERENCES

### Paper 1: Wang et al. (2019)
- **Title:** "In vitro tumor cell rechallenge for predictive evaluation of chimeric antigen receptor T cell antitumor function"
- **Journal:** Journal for ImmunoTherapy of Cancer, 7:217
- **PMC:** PMC6719706
- **DOI:** 10.1186/s40425-019-0690-x
- **Protocol:** 4 rounds over 7 days; 96-well plates; 1:4 E:T; tumor re-added every 2 days; no cytokines in co-culture; flow cytometry readouts for activation, exhaustion, memory phenotype
- **Verification:** Full text accessed and protocol details extracted from PMC6719706

### Paper 2: Ghassemi et al. (2022)
- **Title:** "Inducing T cell dysfunction by chronic stimulation of CAR-engineered T cells targeting cancer cells in suspension cultures"
- **Journal:** STAR Protocols (Cell Press), 4(1):101955
- **PMC:** PMC9826863
- **DOI:** 10.1016/j.xpro.2022.101955
- **Protocol:** 1:8 E:T; restimulation every 48 hours; BID-knockout Nalm6 targets; 13-17 days to exhaustion; no exogenous cytokines; flow cytometry + multi-omics downstream
- **Verification:** Full text accessed and protocol details extracted from PMC9826863

### Paper 3: Alizadeh et al. (2019)
- **Title:** "IL15 Enhances CAR-T Cell Antitumor Activity by Reducing mTORC1 Activity and Preserving Their Stem Cell Memory Phenotype"
- **Journal:** Cancer Immunology Research, 7(5):759-772
- **PMC:** PMC6687561
- **DOI:** 10.1158/2326-6066.CIR-18-0466
- **Protocol:** Recursive killing assay; 1:3 E:T (CD19-CAR) or 1:4 (IL13Ra2-CAR); rechallenge over 5-7 days; flow cytometry for viable tumor and T cell counts; compared IL-2 vs IL-15 expansion
- **Verification:** Full text accessed and protocol details extracted from PMC6687561

### Paper 4: Long et al. (2015)
- **Title:** "4-1BB costimulation ameliorates T cell exhaustion induced by tonic signaling of chimeric antigen receptors"
- **Journal:** Nature Medicine, 21(6):581-590
- **PMC:** PMC4458184
- **DOI:** 10.1038/nm.3838
- **Protocol:** Single-stimulation cytotoxicity (Cr51 release, 6h, E:T 40:1 to 2.5:1); cytokine production at 1:1 for 24h; exhaustion markers PD-1/TIM-3/LAG-3; key study establishing 4-1BB vs CD28 costimulatory domain effects on exhaustion
- **Verification:** Full text accessed from PMC4458184; confirmed focus on tonic signaling-driven exhaustion

### Paper 5: Anti-CD19 antibody cotreatment and serial killing (2025)
- **Title:** "Anti-CD19 antibody cotreatment enhances serial killing activity of anti-CD19 CAR-T/-NK cells and reduces trogocytosis"
- **Journal:** Blood, 145(9):956-969
- **DOI:** Published online 2024/2025 by ASH
- **Protocol:** Sequential killing assay; NALM6 targets added every 2 days for repetitive challenge; measured cytotoxicity, CD107a degranulation, and trogocytosis across rounds
- **Verification:** Search results confirmed journal, title, and DOI from ASH publications

---

## 5. CRITICAL CONSIDERATIONS FOR JURKAT CELLS

### 5.1 Fundamental Limitation: Constitutive Proliferation

Jurkat cells are an immortalized human T-cell acute lymphoblastic leukemia (T-ALL) line. They proliferate constitutively and do not require antigen stimulation to divide. This is the single most important caveat for rechallenge assay interpretation.

**Implications for rechallenge assays:**
- In primary T cell rechallenge assays, increased T cell numbers after antigen re-exposure indicate antigen-driven proliferation
- In Jurkat cell rechallenge assays, cell number increases may reflect constitutive growth rather than antigen-specific activation
- Fold expansion data from Jurkat rechallenge assays CANNOT be directly compared to primary T cell data

### 5.2 Known Genetic Defects in Jurkat Cells

Based on genome-wide surveys (Abraham & Bhoj, BMC Genomics 2018 [PMC5941560]; Kirk et al., Scientific Reports 2025):

| Gene | Mutation Type | Consequence |
|------|---------------|-------------|
| **PTEN** | Frameshift (both alleles) | PTEN-null; constitutive PI3K/AKT activation; hyperproliferation |
| **INPP5D (SHIP1)** | Stop codon + 47bp deletion | Loss of function; dysregulated PI3K signaling |
| **CTLA4** | Heterozygous stop codon (codon 20) | Decreased CTLA4 expression; impaired inhibitory checkpoint |
| **SYK** | Damaging mutation | Altered TCR proximal signaling |
| **TP53** | Mutated | Defective DNA damage response |
| **BAX** | Mutated | Impaired apoptosis |
| **MSH2** | Mutated | Defective mismatch repair; genomic instability |
| **C1GALT1C1** | Mutated | Altered O-linked glycosylation |

**PTEN deficiency is especially relevant:** Loss of PTEN causes constitutive phosphorylation of AKT (Ser-473), hyperactivation of PI3K pathway, hyperresponsiveness to CD3 stimulation, and IL-2-independent growth. Re-expression of PTEN in Jurkat cells reduces proliferation by slowing cell cycle progression.

**Reference:** Shan et al. (2000) "Deficiency of PTEN in Jurkat T Cells Causes Constitutive Localization of Itk to the Plasma Membrane and Hyperresponsiveness to CD3 Stimulation." Mol Cell Biol 20(18):6945-6957. [PMC88770]

### 5.3 Limited Cytotoxic Capacity

- Jurkat cells are CD4+ only -- they lack the CD8+ cytotoxic T cell component
- They have reduced perforin and granzyme B expression compared to activated primary CD8+ T cells
- Killing by Jurkat-CAR cells is less efficient than by primary T-CAR cells
- Jurkat cells do not secrete the full cytokine repertoire of primary T cells
- They DO produce IL-2 and upregulate CD69 upon activation
- They CAN show CD107a (degranulation marker) surface expression after target co-culture

**Key Reference:** Griger et al. (2023) "Using the Jurkat reporter T cell line for evaluating the functionality of novel chimeric antigen receptors." Frontiers in Molecular Medicine 3:1070384. [PMC11285682]

**Also:** Lisby et al. (2024) "Rapid In Vitro Cytotoxicity Evaluation of Jurkat Expressing CAR using Fluorescent Imaging." [PMC11008703]

### 5.4 Genomic Instability

Recent research (Kirk et al., Scientific Reports, 2025) reveals that Jurkat E6-1 populations exhibit substantial genomic heterogeneity BOTH between and WITHIN populations from different laboratories. This includes:
- Karyotypic variation
- Unique mutational profiles between labs
- Differences in protein expression and cytokine production
- Functional variation between Jurkat stocks

**Implication:** Results from Jurkat-based assays may not be reproducible across laboratories using nominally the same cell line.

### 5.5 Recommended Modifications for Jurkat Rechallenge Assays

Given these limitations, the following adaptations are recommended:

**a) Use activation readouts rather than proliferation/expansion as primary endpoints:**
- NFAT reporter activation (if using Jurkat-NFAT-reporter line)
- NF-kB reporter activation
- AP-1 reporter activation
- CD69 upregulation
- CD107a degranulation
- IL-2 secretion

**b) If measuring cytotoxicity:**
- Use luciferase-expressing target cells (Raji-Luc) for bioluminescence-based killing readout
- Or use GFP-labeled Raji cells and quantify residual GFP+ cells by flow cytometry
- Do NOT rely solely on Jurkat cell expansion as evidence of functional capacity

**c) Control for constitutive proliferation:**
- Include untransduced Jurkat cells co-cultured with Raji as a negative control
- Include CAR-Jurkat cells co-cultured with CD19-negative cells as antigen-specificity control
- Include CAR-Jurkat cells cultured alone (no target) to establish baseline proliferation rate
- Calculate ANTIGEN-SPECIFIC expansion = (expansion with target) - (expansion without target)

**d) Validate key findings in primary T cells:**
- Jurkat data should be treated as a screening/ranking tool
- Best constructs must be confirmed using PBMC-derived CD3+ T cells
- This is consistently recommended in the literature

**e) Consider exhaustion marker interpretation carefully:**
- Jurkat cells have mutated CTLA4 (reduced expression) -- cannot reliably measure CTLA-4 upregulation
- PD-1 upregulation upon stimulation CAN be measured in Jurkat cells
- The PTEN-null background creates constitutively high PI3K/AKT signaling, which may mask or alter exhaustion-related signaling dynamics

### 5.6 What Jurkat Cells CAN Reliably Report in Rechallenge Assays

Despite limitations, Jurkat-CAR cells are useful for:
1. **Rapid screening of multiple CAR constructs** -- comparing relative activation levels across variants
2. **Tonic signaling detection** -- antigen-independent CAR activation is detectable and clinically relevant
3. **CAR expression verification** -- transduction efficiency by flow cytometry
4. **Target cell killing** -- relative (not absolute) cytotoxicity ranking between constructs
5. **Signaling pathway activation** -- phosphoproteomics and reporter assays downstream of CAR engagement

---

## 6. RECOMMENDED RECHALLENGE PROTOCOL FOR THIS PROJECT

Given that this project uses Jurkat/CAR-FMC63 cells with Raji targets, here is a suggested protocol combining established methods with Jurkat-appropriate modifications:

### 6.1 Proposed Protocol

**Day -1: Prepare cells**
- Count Jurkat-CAR cells and untransduced Jurkat cells
- Count Raji cells (confirm CD19 expression by flow cytometry)
- Label Raji cells with CellTrace Violet (5 uM, 20 min, 37C) if tracking target cell fate
- Alternatively, use GFP+ Raji cells if available

**Day 0: Set up co-cultures**
- Format: 24-well plates
- E:T ratio: 2:1 (CAR-Jurkat : Raji)
- Cell numbers: 0.5 x 10^6 CAR-Jurkat + 0.25 x 10^6 Raji per well
- Medium: RPMI 1640 + 10% FBS + 1% Pen/Strep + 2 mM L-glutamine
- No exogenous cytokines in co-culture

**Controls (essential):**
1. Untransduced Jurkat + Raji (non-specific killing control)
2. CAR-Jurkat + CD19-negative target cells (antigen-specificity control)
3. CAR-Jurkat alone (baseline proliferation control)
4. Raji alone (target cell growth control)

**Day 3 (Round 2):**
- Collect 100 uL sample for flow cytometry:
  - Absolute cell counts (counting beads)
  - CAR-T vs Raji enumeration
  - Activation markers (CD69, CD107a)
  - Viability (7-AAD or DAPI)
- Collect supernatant for cytokine ELISA (IL-2, IFN-gamma if detectable)
- Add 0.25 x 10^6 fresh Raji cells

**Day 6 (Round 3):**
- Repeat all Day 3 measurements
- Add 0.25 x 10^6 fresh Raji cells
- Check exhaustion markers: PD-1, TIM-3, LAG-3

**Day 9 (Round 4):**
- Repeat all Day 3 measurements
- Add 0.25 x 10^6 fresh Raji cells

**Day 12: Final Analysis**
- Full flow cytometry panel:
  - Absolute counts of CAR-Jurkat and residual Raji
  - Exhaustion markers: PD-1, TIM-3, LAG-3 (co-expression)
  - Memory markers: CD45RO, CD62L, CCR7
  - Activation: CD69, CD25
- Supernatant: ELISA for cytokines
- Calculate: residual tumor cells as % of tumor-alone control = killing efficiency
- Calculate: antigen-specific expansion = (CAR-Jurkat count with Raji) - (CAR-Jurkat count alone)

### 6.2 Data Analysis

**Primary Endpoint:** Residual viable Raji cells at each round as a percentage of the Raji-alone control. This measures killing capacity independent of Jurkat proliferation artifacts.

**Secondary Endpoints:**
- Antigen-specific fold expansion of CAR-Jurkat (corrected for baseline growth)
- Exhaustion marker expression kinetics
- Cytokine secretion per round
- Serial killing efficiency = % tumor eliminated per round, plotted across rounds

---

## 7. UNCERTAINTY FLAGS

The following points contain some uncertainty and should be independently verified:

1. **Jurkat perforin/granzyme expression levels:** While multiple sources confirm Jurkat cells have reduced cytotoxic granule content, exact quantitative data on basal vs stimulated perforin/granzyme levels in Jurkat-CAR cells specifically is limited. The degree to which CAR engagement upregulates these in Jurkat cells needs experimental confirmation.

2. **BID-knockout Nalm6 in Ghassemi protocol:** The BID-KO modification is specific to the Ghassemi lab protocol. Using standard Raji cells (without BID-KO) may result in faster target elimination and less chronic stimulation. The dynamics may differ.

3. **Optimal E:T ratio for Jurkat-CAR/Raji:** The 2:1 ratio suggested is based on published FMC63 CAR-T/Raji studies. Given Jurkat cells' reduced killing efficiency, a higher E:T ratio (e.g., 4:1 or 5:1) may be needed. A pilot experiment to titrate E:T ratios is strongly recommended.

4. **Exhaustion marker dynamics in Jurkat:** Whether Jurkat cells faithfully recapitulate the PD-1/TIM-3/LAG-3 exhaustion trajectory seen in primary T cells during chronic stimulation has not been extensively characterized. The PTEN-null and CTLA4-mutant background may alter these dynamics.

5. **Paper 5 (Blood 2025) on anti-CD19 antibody cotreatment:** This paper's publication date and volume were confirmed through ASH search results, but the complete methods section was not fully extracted due to access limitations. The serial killing protocol details cited are from the search result summaries.

---

## Sources

- [Wang et al. (2019) - In vitro tumor cell rechallenge, J ImmunoTher Cancer](https://pmc.ncbi.nlm.nih.gov/articles/PMC6719706/)
- [Ghassemi et al. (2022) - Chronic stimulation protocol, STAR Protocols](https://pmc.ncbi.nlm.nih.gov/articles/PMC9826863/)
- [Alizadeh et al. (2019) - IL15 and CAR-T recursive killing, Cancer Immunol Res](https://pmc.ncbi.nlm.nih.gov/articles/PMC6687561/)
- [Long et al. (2015) - 4-1BB and T cell exhaustion, Nature Medicine](https://pmc.ncbi.nlm.nih.gov/articles/PMC4458184/)
- [Anti-CD19 antibody cotreatment and serial killing, Blood 2025](https://ashpublications.org/blood/article/145/9/956/534403/Anti-CD19-antibody-cotreatment-enhances-serial)
- [Griger et al. (2023) - Jurkat reporter for CAR evaluation, Front Mol Med](https://pmc.ncbi.nlm.nih.gov/articles/PMC11285682/)
- [Lisby et al. (2024) - Jurkat-CAR cytotoxicity by fluorescent imaging](https://pmc.ncbi.nlm.nih.gov/articles/PMC11008703/)
- [Comparative analysis of CAR-T killing assays, Cancers 2021](https://pmc.ncbi.nlm.nih.gov/articles/PMC8064272/)
- [Abraham & Bhoj (2018) - Genome-wide Jurkat mutations, BMC Genomics](https://pmc.ncbi.nlm.nih.gov/articles/PMC5941560/)
- [Kirk et al. (2025) - Jurkat genomic instability, Scientific Reports](https://www.nature.com/articles/s41598-025-95903-0)
- [Shan et al. (2000) - PTEN deficiency in Jurkat, Mol Cell Biol](https://pmc.ncbi.nlm.nih.gov/articles/PMC88770/)
- [Xu et al. (2019) - IL-7/IL-15 CAR-T expansion, Protein & Cell](https://pmc.ncbi.nlm.nih.gov/articles/PMC6776495/)
- [Thermo Fisher - CellTrace Violet Protocol](https://www.thermofisher.com/us/en/home/references/protocols/cell-and-tissue-analysis/protocols/celltrace-violet-cell-proliferation-protocol.html)
- [Thermo Fisher - Flow Cytometry Counting Beads](https://www.thermofisher.com/us/en/home/life-science/cell-analysis/flow-cytometry/flow-cytometry-calibration/flow-cytometer-cell-counting-beads.html)
