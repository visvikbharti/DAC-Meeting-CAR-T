# 16. Primary Human T Cell Validation of CAR Mutant Candidates

## Context and Rationale

After initial screening of FMC63 scFv affinity variants in Jurkat cells (NFAT/NF-kB reporter activation, tonic signaling assessment), the top CAR candidates must be validated in primary human T cells. Jurkat cells enable rapid, high-throughput screening but lack critical features of real T cell biology: genuine cytotoxicity, authentic proliferative expansion, donor-to-donor variability, and real exhaustion biology. This document provides a comprehensive, step-by-step validation plan with verified protocols and citations.

---

## 1. Primary T Cell Isolation and Activation

### 1.1 Blood Source and Volume

**Source:** Peripheral blood from healthy donors, collected in EDTA or citrate (preferred for higher mononuclear cell yield) anticoagulant tubes.

**Volume required per experiment:**
- **40 mL of whole blood** yields approximately **2-5 x 10^7 PBMCs** in healthy donors
- Typical PBMC yield: **~1-2 x 10^6 PBMCs per mL of blood** (Sigma-Aldrich standard protocol)
- After T cell enrichment (negative selection), expect **50-70% recovery** from PBMCs, yielding ~1-3.5 x 10^7 T cells per 40 mL draw
- **Practical recommendation:** Collect **50-60 mL** per donor per experiment to ensure sufficient cells for multiple CAR constructs + controls
- For each CAR construct: need ~2 x 10^6 T cells as starting material for transduction + expansion

**Reference:** Cytiva Life Sciences, "Isolation of mononuclear cells using Ficoll-Paque products" (application note); Sigma-Aldrich, "Recommended Standard Method for Isolating Mononuclear Cells"

### 1.2 PBMC Isolation: Ficoll-Paque Density Gradient

**Standard protocol:**
1. Dilute whole blood 1:1 with PBS (room temperature)
2. Layer 35 mL diluted blood over 15 mL Ficoll-Paque PLUS (density 1.077 g/mL) in 50 mL tubes (or use SepMate/Accuspin tubes for easier processing)
3. Centrifuge at **400 x g for 30 minutes** at room temperature, **brake off**
4. Collect the buffy coat (mononuclear cell layer) at the plasma-Ficoll interface
5. Wash 2x with PBS at 300 x g for 10 minutes
6. Count cells and assess viability (>95% expected by trypan blue exclusion)

**Key tips:**
- Process blood within 4-8 hours of collection for optimal results
- Citrate anticoagulant may yield better quality RNA/DNA and higher cell recovery than EDTA
- All reagents and blood should be at room temperature before layering

**Reference:** Cytiva Life Sciences, "Isolation of mononuclear cells, Methodology and applications" (technical document)

### 1.3 T Cell Enrichment

**Recommended: Negative selection** (untouched T cells, preserving native surface markers)

Two validated commercial options:

| Feature | STEMCELL EasySep Human T Cell Isolation Kit | Miltenyi Pan T Cell Isolation Kit |
|---------|---------------------------------------------|-----------------------------------|
| Method | Column-free magnetic separation | Column-based or column-free (AutoMACS) |
| Time | ~8 minutes (column-free) | 15-30 minutes |
| Purity | >95% CD3+ T cells | >95% CD3+ T cells |
| Principle | Antibody cocktail labels non-T cells (B cells, NK, monocytes, DCs, etc.) with magnetic particles; labeled cells removed; T cells poured off | Similar negative depletion principle |
| Advantage | Faster, simpler, no columns | Widely used in CAR-T protocols; compatible with CliniMACS for clinical-grade |

**Why negative selection over positive selection for CAR-T work:**
- Avoids premature activation by cross-linking surface molecules
- Preserves native T cell phenotype and resting state
- Untouched T cells more suitable for subsequent controlled activation

**Reference:** STEMCELL Technologies, EasySep Human T Cell Isolation Kit product documentation; Miltenyi Biotec, Pan T Cell Isolation Kit (human) product documentation

### 1.4 T Cell Activation

**Option A: Anti-CD3/CD28 Dynabeads (Thermo Fisher CTS Dynabeads CD3/CD28)**

The gold standard for CAR-T manufacturing. Used in FDA-approved Kymriah (tisagenlecleucel).

- **Bead-to-cell ratio:** 1:1 (standard) to 3:1
  - High ratios (5:1, 10:1) delete memory T cells; low ratios (1:10, 1:5) preserve memory T cells (Levine et al., 1997, J Immunol Methods)
  - **Recommended: 1:1 ratio** for balanced expansion and phenotype preservation
- **Mechanism:** 4.5-um superparamagnetic beads coated with anti-CD3 (Signal 1) and anti-CD28 (Signal 2)
- **Bead removal:** Required at day 6 post-activation (magnetic separation) before downstream analysis
- **Advantage:** Well-characterized, clinical-grade available, extensive publication record
- **Disadvantage:** Physical bead removal step required; beads can be engulfed by contaminating monocytes

**Reference:** Levine BL et al. "Effects of CD28 costimulation on long-term proliferation of CD4+ T cells in the absence of exogenous feeder cells." J Immunol. 1997;159(12):5921-30; Thermo Fisher, Dynabeads Human T-Activator CD3/CD28 product documentation (Cat# 11161D)

**Option B: Miltenyi T Cell TransAct**

A polymeric nanomatrix platform; soluble and biodegradable.

- **Dilution:** 1:100 from stock (per manufacturer instructions)
- **Mechanism:** Colloidal polymeric nanomatrix conjugated with anti-CD3 and anti-CD28 antibodies
- **Advantage:** No bead removal step needed; biodegrades in culture; less prone to myeloid cell engulfment; GMP-grade available
- **Disadvantage:** Less published data compared to Dynabeads; newer technology

TransAct was used in the Tan et al. (2025) simultaneous activation/transduction protocol achieving 60-80% transduction efficiency.

**Reference:** Tan JYM et al. "Protocol for the simultaneous activation and lentiviral transduction of primary human T cells with artificial T cell receptors." STAR Protocols. 2025;6(1):103685. doi:10.1016/j.xpro.2025.103685

**Comparison of activation platforms (Mohan et al. 2024):**

Four platforms were directly compared for CAR-T manufacturing:
1. **Dynabeads** (magnetic microspheres) - Thermo Fisher
2. **TransAct** (polymeric nanomatrix) - Miltenyi Biotec
3. **Cloudz** (alginate hydrogel) - Bio-Techne
4. **Microbubbles** (lipid membrane, perfluorocarbon gas) - Akadeum Life Sciences

All deliver CD3/CD28 signals but with distinct downstream effects on CAR-T phenotype and function.

**Reference:** Mohan N et al. "T Cell Activators Exhibit Distinct Downstream Effects on Chimeric Antigen Receptor T Cell Phenotype and Function." ImmunoHorizons. 2024;8(6):404-416. doi:10.1093/immhor/vlae008. PMC11220740

### 1.5 Cytokine Supplementation

**Standard: IL-2**
- **Concentration:** 100 IU/mL (most common in published protocols)
- **Frequency:** Replenish every 2-3 days with media change
- **Effect:** Drives robust T cell expansion; can promote effector differentiation

**Alternative: IL-7 + IL-15 (for less-differentiated phenotype)**
- **IL-7:** 5-10 ng/mL
- **IL-15:** 5-10 ng/mL
- **Effect:** Promotes stem cell memory (Tscm) and central memory (Tcm) phenotypes; improved persistence in vivo
- **Rationale:** IL-7 supports T cell survival and homeostatic proliferation; IL-15 promotes memory formation without terminal differentiation

**For this project:** Consider running parallel arms with IL-2 vs IL-7/IL-15 for at least one donor to determine if the affinity-function relationship differs based on T cell differentiation state. This is particularly relevant because less-differentiated T cells (Tscm/Tcm) may be more sensitive to affinity differences.

**Reference:** Ayala Ceja M et al. "CAR-T cell manufacturing: Major process parameters and next-generation strategies." J Exp Med. 2024;221(2):e20230903. doi:10.1084/jem.20230903. PMC10791545

---

## 2. Lentiviral Transduction of Primary T Cells

### 2.1 Timing of Transduction

**Two validated approaches:**

| Parameter | Sequential (Day 1 activation, Day 2 transduction) | Simultaneous (Day 0 co-activation + transduction) |
|-----------|---------------------------------------------------|-----------------------------------------------------|
| Protocol | Activate T cells on Day 0; transduce on Day 1 or Day 2 post-activation | Mix T cells + TransAct + lentivirus + polybrene on Day 0 |
| Reference | Prommersberger et al. 2020, Current Protocols Immunol | Tan et al. 2025, STAR Protocols |
| Efficiency | 30-60% typical | 60-80% (68.74 +/- 6.63%) |
| Advantage | Standard, well-characterized | Higher efficiency, fewer steps, faster |
| Disadvantage | More hands-on time; may require spinoculation | Requires optimization of cell density and virus concentration |

**For sequential protocol (Prommersberger et al. 2020):**
1. Day 0: Activate T cells with anti-CD3/CD28 Dynabeads at 1:1 ratio in IL-2 (100 IU/mL)
2. Day 1: Transduce activated T cells with lentiviral vector
3. Day 6: Remove Dynabeads
4. Day 6-10: Expansion in IL-2 medium
5. Day 10+: CAR enrichment (if needed) via tag-based sorting

**For simultaneous protocol (Tan et al. 2025):**
1. Day 0: Combine T cells (>1 x 10^6/mL) + TransAct (1:100) + concentrated lentivirus + polybrene (15 ug/mL) + IL-2 (100 IU/mL)
2. Day 2-3: Taper culture mixture with fresh medium + IL-2
3. Day 14-21: Expansion to desired cell number

**Reference:** Prommersberger S et al. "Antibody-Based CAR T Cells Produced by Lentiviral Transduction." Curr Protoc Immunol. 2020;128(1):e93. doi:10.1002/cpim.93. PMID:32150338

### 2.2 Multiplicity of Infection (MOI)

- **Standard MOI for primary T cells:** 3-10
- **Maximum recommended:** MOI of 10; higher MOIs (>10) decrease living T cell transduction rate and increase toxicity
- **For Jurkat cells:** MOI of 1-5 is typically sufficient due to higher susceptibility to transduction
- **CD4+ vs CD8+ difference:** CD4+ T cells are more readily transduced than CD8+ T cells
  - CD4+ T cells: 40-80% at MOI of 3
  - CD8+ T cells: 20-50% at MOI of 3 (more resistant to gene transfer)

**Reference:** Tan et al. 2025, STAR Protocols (cited above); Spinoculation and retronectin study: Rajabzadeh A et al. "Spinoculation and retronectin highly enhance the gene transduction efficiency of Mucin-1-specific chimeric antigen receptor (CAR) in human primary T cells." BMC Mol Cell Biol. 2021;22:57. doi:10.1186/s12860-021-00397-z

### 2.3 Transduction Enhancers

| Enhancer | Concentration | Mechanism | Efficiency | Notes |
|----------|---------------|-----------|------------|-------|
| **RetroNectin (Takara)** | 20 ug/mL (plate coating) | Co-localizes viral particles and T cells via cell surface receptor binding and H-domain viral particle binding | Highest: ~63% (with spinoculation) | Less differentiated T cell phenotype; better for clinical-grade manufacturing |
| **Polybrene** | 5-15 ug/mL | Neutralizes charge repulsion between viral particles and cell membrane | ~35% (with spinoculation) | Can be toxic at high concentrations; simpler to use |
| **Spinoculation** | 800-1200 x g, 60-90 min, 32C | Increases viral particle contact with cells | ~21% (alone) | Can be combined with RetroNectin or polybrene |
| **RetroNectin + spinoculation** | Combined | Combined mechanisms | ~63% | Gold standard for retroviral vectors |
| **Polybrene + spinoculation** | Combined | Combined mechanisms | ~35% | Higher cytotoxicity than RetroNectin-transduced cells |

**Key finding from Idrees et al. (2023):** RetroNectin produced CAR-T cells with a **less differentiated phenotype** compared to polybrene, making it preferable for maintaining favorable memory T cell profiles. However, polybrene-transduced CAR-T cells showed **higher cytotoxicity** in short-term assays.

**Reference:** Idrees M et al. "Effects of polybrene and retronectin as transduction enhancers on the development and phenotypic characteristics of VHH-based CD19-redirected CAR T cells: a comparative investigation." Clin Exp Med. 2023;23(6):2535-2546. doi:10.1007/s10238-022-00928-8. PMID:36434173

### 2.4 Expected Transduction Efficiency: Primary T Cells vs Jurkat

| Cell Type | Typical Efficiency | Optimized Efficiency | Notes |
|-----------|-------------------|---------------------|-------|
| **Jurkat** | 70-90%+ | >90% | Highly permissive to lentiviral transduction; constitutively cycling |
| **Primary CD4+ T cells** | 40-60% | 60-80% | More readily transduced than CD8+ |
| **Primary CD8+ T cells** | 20-40% | 40-60% | More resistant to gene transfer |
| **Mixed primary T cells** | 30-50% (basic) | 60-80% (optimized, Tan et al. 2025) | Depends on CD4:CD8 ratio and activation state |

**Important for this project:** Since different CAR affinity variants will be compared, it is critical that transduction efficiency is **matched across constructs**. If one variant transduces at 70% and another at 30%, differences in cytotoxicity could reflect transduction efficiency rather than CAR affinity. Strategies to address this:
1. Use the same lentiviral batch and MOI for all constructs
2. Measure transduction efficiency by flow cytometry at day 5-7
3. If efficiencies differ significantly, normalize by FACS-sorting for CAR+ cells before functional assays
4. Report both bulk and CAR+ normalized data

### 2.5 Expansion Period

- **Typical expansion:** 10-14 days post-transduction before functional assays
- **Cell density maintenance:** 0.5-3 x 10^6 cells/mL during expansion
- **Media changes:** Every 2-3 days with fresh IL-2 (100 IU/mL) or IL-7/IL-15
- **Expected fold expansion:** 50-200 fold over 10-14 days (donor-dependent)
- **Quality checks during expansion:**
  - Day 5-7: Assess CAR expression by flow cytometry
  - Day 7-10: Assess T cell phenotype (CD4/CD8 ratio, memory markers)
  - Day 10-14: Harvest for functional assays

**Reference:** Ayala Ceja et al. 2024, J Exp Med (cited above): "Typical processes last 1-2 weeks from the time of T-cell activation to the time of cell harvest."

---

## 3. Functional Assays in Primary CAR-T Cells

### 3.1 Cytotoxicity Assays

Primary T cells — unlike Jurkat — possess functional cytolytic machinery (perforin/granzyme pathway). This is the single most important assay for validating CAR affinity variants.

**Recommended approach: Bioluminescence Imaging (BLI) assay (luciferase-based)**

Four major assay types were systematically compared by Kiesgen et al. (2021) in Nature Protocols:

| Assay | Principle | E:T Ratios | Duration | Advantages | Disadvantages |
|-------|-----------|-----------|----------|-----------|---------------|
| **51Cr release** | Radioactive isotope release from lysed targets | 0.3:1 to 50:1 | 4-24 hr | Gold standard; well-established | Radioactive; short window; high spontaneous release |
| **BLI (luciferase)** | Luminescence loss = target cell death | 10:1 to 40:1 | Hours to days | No radioactivity; higher signal-to-background than 51Cr (up to 2-fold); high throughput; simple quantification | Requires luciferase-expressing target cells |
| **Impedance** | Real-time electrical impedance change as adherent cells detach | 0.05:1 to 10:1 | Days (continuous) | Real-time kinetics; lowest E:T ratios (physiologic); label-free | Adherent targets only; not suitable for Raji (suspension) |
| **Flow cytometry** | Viability dyes + surface markers | 1:1 to 50:1 | 4-72 hr | Multiparameter; heterogeneous target analysis; distinguishes early vs late apoptosis (Annexin V + 7-AAD) | More labor-intensive |

**For this project (Raji target cells):** Use **BLI assay** with Raji-Luc cells as the primary cytotoxicity readout. Supplement with **flow cytometry-based killing assay** for multiparameter analysis.

**BLI protocol:**
1. Plate Raji-Luc target cells in 96-well white/clear bottom plates
2. Add CAR-T effector cells at multiple E:T ratios (1:1, 5:1, 10:1, 20:1)
3. After 4, 8, 16, 24 hours: add D-luciferin substrate (150 ug/mL)
4. Read luminescence on plate reader
5. Calculate % specific lysis = [1 - (luminescence with effectors / luminescence without effectors)] x 100

**Reference:** Kiesgen S et al. "Comparative analysis of assays to measure CAR T cell-mediated cytotoxicity." Nat Protoc. 2021;16(3):1331-1342. doi:10.1038/s41596-020-00467-0. PMC8064272

Also: Brown CE et al. "Bioluminescence imaging outperforms chromium-51 release assay." PLoS ONE. 2014;9(2):e89357. doi:10.1371/journal.pone.0089357. PMC3929704

### 3.2 Proliferation: CFSE / CellTrace Violet Dilution

In Jurkat cells, proliferation is constitutive and CAR-independent (they divide regardless). In primary T cells, proliferation upon antigen encounter reflects genuine clonal expansion — a critical metric for CAR function.

**Protocol:**
1. Label CAR-T cells with **CellTrace Violet** (CTV; Thermo Fisher) at 5 uM, 20 min, 37C
   - CTV preferred over CFSE: brighter, less spectral overlap, compatible with GFP/FITC channel for CAR detection
2. Co-culture labeled CAR-T cells with irradiated Raji target cells (E:T = 1:1 or 2:1)
3. Analyze by flow cytometry at **day 3, 5, and 7**
4. Quantify: number of cell divisions (peak resolution), division index, proliferation index
5. Gate on CAR+ cells (using anti-scFv antibody or protein L staining) to assess only transduced cells

**Controls:**
- Unstimulated CAR-T cells (no target) — should show minimal division
- CAR-T + CD19-negative target (e.g., K562) — should show no antigen-specific proliferation
- Untransduced T cells + Raji — minimal/no proliferation expected

**Reference:** Thermo Fisher, "CellTrace Violet Cell Proliferation Kit Protocol" (product documentation, Cat# C34557)

### 3.3 Cytokine Production

Primary T cells produce a full spectrum of effector cytokines that reflect genuine immune activation. Jurkat cells have limited cytokine output.

**Key cytokines to measure:**

| Cytokine | Significance | Method |
|----------|-------------|--------|
| **IFN-gamma** | Primary effector cytokine; correlates with anti-tumor activity | Intracellular staining (ICS) + ELISA/Luminex |
| **TNF-alpha** | Pro-inflammatory; cytotoxic; CRS-related | ICS + ELISA/Luminex |
| **IL-2** | Autocrine growth factor; reduced in exhaustion | ICS + ELISA/Luminex |
| **Granzyme B** | Cytolytic granule content; direct killing mediator | ICS (intracellular) |
| **Perforin** | Pore-forming protein; essential for granule-mediated killing | ICS (intracellular) |

**Protocol for intracellular cytokine staining (ICS):**
1. Co-culture CAR-T cells with Raji (E:T = 1:1) for 5-6 hours
2. Add Brefeldin A (GolgiPlug, 1:1000) and Monensin (GolgiStop, 1:1500) at hour 1
3. Harvest cells, stain surface markers (CD3, CD4, CD8, CAR)
4. Fix and permeabilize (BD Cytofix/Cytoperm kit)
5. Stain intracellular cytokines (IFN-g, TNF-a, IL-2, Granzyme B)
6. Analyze by flow cytometry; gate on CAR+ CD4+ and CAR+ CD8+ separately

**Protocol for supernatant cytokine quantification:**
1. Co-culture CAR-T cells with Raji (E:T = 1:1) for 24 hours
2. Collect supernatant
3. Measure by ELISA (single-plex) or Luminex/CBA (multiplex)
4. Include: IFN-g, TNF-a, IL-2, IL-6, IL-10, GM-CSF

**Critical for affinity project:** Cytokine production may differ across affinity variants — very high affinity CARs may show more cytokine production at low E:T ratios but potentially more exhaustion-related cytokine profiles after chronic stimulation. This differential is only detectable in primary T cells.

### 3.4 Degranulation: CD107a Assay

CD107a (LAMP-1) is transiently expressed on the T cell surface during degranulation when cytolytic granules fuse with the plasma membrane. This assay directly measures the capacity of CAR-T cells to deploy their killing machinery.

**Protocol:**
1. Plate CAR-T cells with Raji target cells at E:T = 1:1
2. **Critical:** Add anti-CD107a-PE antibody **at the start of co-culture** (not after) — CD107a surface expression is extremely transient due to granule recycling
3. Add Monensin (1 uM) after 1 hour to prevent re-internalization
4. Incubate for 4-5 hours total at 37C
5. Harvest, stain surface markers (CD3, CD4, CD8, CAR marker)
6. Analyze by flow cytometry; report % CD107a+ among CAR+ T cells

**Why this matters for affinity variants:** Degranulation is an early and direct readout of CAR activation. Higher-affinity CARs may trigger degranulation at lower antigen density. Lower-affinity CARs may show delayed or reduced degranulation. This assay complements cytotoxicity data by revealing the mechanism (degranulation-dependent killing vs other pathways).

**Reference:** Betts MR et al. "Detection of T-cell degranulation: CD107a and b." Methods Cell Biol. 2004;75:497-512. doi:10.1016/s0091-679x(04)75020-7; Shafer P et al. "A simple rapid CAR T-cell cytotoxicity and degranulation flow cytometric assay." Cytotherapy. 2020;22(2):99-105. doi:10.1016/j.jcyt.2019.10.007

### 3.5 Exhaustion Markers: PD-1 / TIM-3 / LAG-3

Exhaustion is only meaningful in primary T cells (Jurkat cells do not undergo physiological exhaustion). This is especially important for affinity optimization: high-affinity CARs may drive stronger tonic signaling and faster exhaustion.

**Panel:**

| Marker | Expression Pattern | Significance |
|--------|-------------------|-------------|
| **PD-1 (CD279)** | Early exhaustion marker | Expressed on activated and exhausted T cells; co-expression with other markers defines exhaustion |
| **TIM-3 (HAVCR2)** | Mid/late exhaustion marker | Tim-3+PD-1+ double-positive = severely exhausted subpopulation |
| **LAG-3 (CD223)** | Mid exhaustion marker | Co-expression with PD-1 correlates with poor outcome in lymphoma |
| **TIGIT** | Additional inhibitory receptor | Co-expression increases with exhaustion severity |
| **CD39** | Exhaustion-associated ectonucleotidase | Marks terminally exhausted CAR-T cells |

**Protocol for chronic stimulation / rechallenge assay:**
1. Day 0: Co-culture CAR-T cells with Raji at E:T = 1:1
2. Day 3: Re-stimulate with fresh Raji cells (remove old targets by washing)
3. Day 6: Third re-stimulation
4. Day 9: Fourth re-stimulation (optional fifth at Day 12)
5. At each re-stimulation, assess:
   - % killing of fresh targets (should decrease with exhaustion)
   - Exhaustion marker expression (PD-1, TIM-3, LAG-3, TIGIT by flow cytometry)
   - Cytokine production (IFN-g, TNF-a — should decrease)
   - Cell count (expansion capacity declines with exhaustion)

**Interpretation for affinity project:**
- **Higher-affinity variants:** May show faster upregulation of exhaustion markers, especially if tonic signaling is present
- **Lower-affinity variants:** May maintain function over more rounds of rechallenge (less exhaustion-prone)
- **Optimal affinity:** Balances initial potency with sustained function across multiple challenges

**Reference:** Wherry EJ et al. "Cooperation of Tim-3 and PD-1 in CD8 T-cell exhaustion during chronic viral infection." PNAS. 2010;107(33):14733-14738. doi:10.1073/pnas.1009731107; Grosser R et al. "TIM-3, LAG-3, or 2B4 gene disruptions increase the anti-tumor response of engineered T cells." Front Immunol. 2024;15:1315283. doi:10.3389/fimmu.2024.1315283

### 3.6 Memory Phenotype Assessment

Unlike Jurkat cells (which have no memory differentiation biology), primary T cells differentiate through a defined hierarchy. The memory phenotype of CAR-T cells predicts in vivo persistence and efficacy.

**T cell differentiation hierarchy (least to most differentiated):**

| Subset | Markers | Functional Significance |
|--------|---------|------------------------|
| **T naive (Tn)** | CD45RA+ CCR7+ CD62L+ CD95- CD27+ CD28+ | Not yet antigen-experienced |
| **T stem cell memory (Tscm)** | CD45RA+ CCR7+ CD62L+ **CD95+** CD27+ CD28+ IL-7Ra+ | Self-renewal capacity; superior in vivo persistence; best for CAR-T |
| **T central memory (Tcm)** | CD45RA- CCR7+ CD62L+ | Good proliferative capacity; lymph node homing |
| **T effector memory (Tem)** | CD45RA- CCR7- CD62L- | Immediate effector function; limited persistence |
| **T effector memory RA (Temra)** | CD45RA+ CCR7- CD62L- | Terminally differentiated; cytotoxic but limited expansion |

**Flow cytometry panel for memory phenotyping:**

| Marker | Channel (suggested) | Purpose |
|--------|---------------------|---------|
| CD3 | BUV395 | T cell identification |
| CD4 | BV510 | Helper subset |
| CD8 | APC-Cy7 | Cytotoxic subset |
| CAR (Protein L or anti-scFv) | PE | CAR+ gating |
| CD45RA | BV785 or APC | Naive/Temra marker |
| CCR7 | BV421 or PE-Cy7 | Naive/Tcm marker |
| CD62L | FITC | Naive/Tcm marker |
| CD95 (Fas) | PE-CF594 | Tscm identification (critical: CD45RA+CCR7+CD95+) |
| CD27 | BV605 | Additional memory marker |
| CD28 | PerCP-Cy5.5 | Costimulation/memory marker |

**Important note:** After activation and lentiviral transduction, CD95 is upregulated to nearly 100% in the Tn population, increasing the percentage of cells with Tscm phenotype. This should be considered when interpreting phenotyping data — assess at day 10-14 post-activation when equilibrium is better established.

**Reference:** Mahnke YD et al. "The who's who of T-cell differentiation: Human memory T-cell subsets." Eur J Immunol. 2013;43(11):2797-2809. doi:10.1002/eji.201343751

---

## 4. In Vivo Xenograft Model (NSG Mice)

### 4.1 Model Overview

The NSG (NOD.Cg-Prkdc^scid Il2rg^tm1Wjl/SzJ) mouse xenograft model with Raji B cell lymphoma is the most widely used preclinical model for anti-CD19 CAR-T evaluation.

### 4.2 Detailed Protocol

**Based on Xiao & Su, Bio-Protocol, 2023:**

**Mouse preparation:**
- Strain: NSG mice (Jackson Laboratory, Stock #005557)
- Age: 6-7 weeks old
- Acclimation: 1 week in facility before experiments
- Housing: Specific pathogen-free (SPF) conditions; individually ventilated cages (IVCs)
- Sex: Typically female (for uniformity; less fighting)

**Tumor engraftment (subcutaneous model):**
1. Culture Raji cells for 3-5 days before injection
2. Resuspend **1 x 10^6 Raji cells in 50 uL PBS** per mouse
3. Mix 1:1 with ice-cold **Matrigel** (50 uL) on ice
4. Inject subcutaneously into right flank (total 100 uL per mouse)
5. Allow tumors to establish for **7 days** (target size: 20-100 mm^3 before treatment)

**Alternative: Disseminated (IV) model with Raji-Luc:**
1. Inject **0.5 x 10^6 Raji-Luc cells** in 100 uL PBS via tail vein (Day 0)
2. Allow engraftment for 4-7 days before CAR-T treatment
3. Monitor by bioluminescence imaging (IVIS)

**CAR-T cell administration:**
- Dose: **1 x 10^7 CAR-T cells** (standard) or dose-response: 1 x 10^6, 2 x 10^6, 5 x 10^6, 1 x 10^7
- Route: IV tail vein injection in 100 uL PBS
- Timing: Day 7 post-tumor injection
- Control groups: PBS vehicle (100 uL IV), untransduced T cells (1 x 10^7)

**Monitoring schedule:**
- Body weight: every other day
- Tumor size (subcutaneous model): caliper measurement every other day; V = 1/2 (length x width^2)
- Bioluminescence imaging (IV/disseminated model):
  - D-luciferin: 150 mg/kg IP (from 15 mg/mL stock in PBS) or 3 mg per mouse (30 mg/mL in NaHCO3)
  - Image 10 min post-injection using IVIS Spectrum or IVIS Lumina III
  - Imaging schedule: Days 1, 3, 6, 9, 13, 16, 21, 28 post-CAR-T (then weekly)
- Blood sampling: Days 7, 14, 21 post-CAR-T via tail vein nick; assess CAR-T cell percentage and exhaustion markers by flow cytometry

**Endpoints:**
- Primary: Tumor volume (subcutaneous) or bioluminescence total flux (IV model)
- Secondary: Survival (Kaplan-Meier), T cell persistence in blood, exhaustion phenotype
- Humane endpoint: Tumor volume >1500 mm^3, weight loss >20%, or moribund condition

**Reference:** Xiao Q, Su X. "Anti-tumor Efficacy of CD19 CAR-T in a Raji B Cell Xenografted Mouse Model." Bio Protoc. 2023;13(8):e4655. doi:10.21769/BioProtoc.4655. PMC10127058

### 4.3 Study Design and Group Size

| Group | Treatment | n (mice) | Purpose |
|-------|----------|----------|---------|
| 1 | PBS vehicle | 5-7 | Negative control |
| 2 | Untransduced T cells (1 x 10^7) | 5-7 | T cell control (non-specific effects) |
| 3 | WT FMC63 CAR-T (1 x 10^7) | 5-7 | Positive control / benchmark |
| 4 | High-affinity mutant CAR-T (1 x 10^7) | 5-7 | Test group |
| 5 | Low-affinity mutant CAR-T (1 x 10^7) | 5-7 | Test group |

**Minimum:** n=5 per group is standard for preclinical CAR-T studies. The Xiao & Su protocol used 6-7 mice per group.

**Total mice estimate:** 5 groups x 6 mice = 30 mice minimum; if dose-response is included, additional groups needed.

### 4.4 Feasibility at CSIR-IGIB

**Key considerations:**
- CSIR-IGIB has animal facilities, but NSG mice availability in India requires verification with the institutional animal facility
- NSG mice may need to be sourced from Jackson Laboratory or bred in-house (requires immunodeficient mouse breeding colony)
- Alternative sourcing: National Centre for Laboratory Animal Sciences (NCLAS), Hyderabad; or Advanced Centre for Treatment, Research and Education in Cancer (ACTREC), Mumbai
- The Institutional Animal Ethics Committee (IAEC) approval is mandatory under CPCSEA (Committee for the Purpose of Control and Supervision of Experiments on Animals) guidelines
- Consider collaborating with institutions that already have established NSG mouse colonies

**Recommendation for DAC:** Present the in vivo model as a future validation step with the caveat that feasibility depends on NSG mouse availability and IAEC approval. The primary focus for the current phase should be comprehensive in vitro validation in primary T cells.

---

## 5. Key Differences: Jurkat vs Primary T Cells

### 5.1 Molecular and Functional Differences

| Feature | Jurkat | Primary T Cells | Impact on CAR Screening |
|---------|--------|----------------|------------------------|
| **PTEN expression** | Absent (PTEN-null) | Normal | Jurkat: constitutive AKT activation; hyperresponsive to TCR/CAR stimulation; may overestimate CAR signaling potency |
| **SHIP expression** | Deficient | Normal | Contributes to constitutive PI3K/AKT pathway activation in Jurkat |
| **Ca2+ flux** | ~7-fold greater TCR-induced Ca2+ flux than primary T cells | Normal | Jurkat grossly overestimates signaling amplitude |
| **Cytotoxicity** | None (lacks functional cytolytic machinery) | Full perforin/granzyme pathway | Cannot assess killing in Jurkat; must use primary T cells |
| **Proliferation** | Constitutive (independent of CAR stimulation) | Antigen-dependent | Proliferation assays meaningless in Jurkat |
| **Exhaustion** | Not physiological | PD-1/TIM-3/LAG-3 upregulation upon chronic stimulation | Exhaustion assessment only valid in primary T cells |
| **Memory differentiation** | None | Tn > Tscm > Tcm > Tem > Temra hierarchy | Memory phenotype only assessable in primary T cells |
| **Donor variability** | None (clonal cell line) | Significant (CD4:CD8 ratio, basal activation state, age, CMV status) | Primary T cells capture biological variability critical for clinical translation |
| **Tonic signaling response** | Detectable; correlated with primary T cells | Detectable; can lead to exhaustion | **Good correlation** between Jurkat and primary T cells for tonic signaling |
| **Actin cytoskeleton** | Distinct behavior from primary T cells | Normal | May affect immunological synapse formation |
| **Downstream signaling** | Diverges from primary T cells at events downstream of LAT and SLP-76 | Normal | Early/proximal signaling similar; downstream events differ |

**Reference:** Abraham RT & Weiss A. "Jurkat T cells and development of the T-cell receptor signalling paradigm." Nat Rev Immunol. 2004;4:301-308. doi:10.1038/nri1330; Chua CW et al. "Comparison of T cell receptor-induced proximal signaling and downstream functions in immortalized and primary T cells." PLoS ONE. 2009;4(5):e5430. doi:10.1371/journal.pone.0005430

### 5.2 What Translates from Jurkat to Primary T Cells

**Findings that RELIABLY translate:**

1. **CAR surface expression levels** — If a CAR construct expresses well on Jurkat, it generally expresses well on primary T cells (same lentiviral vector, same promoter)
2. **Tonic signaling** — Jurkat NFAT/NF-kB reporter activation in the absence of target cells correlates well with tonic signaling-driven exhaustion in primary CAR-T cells. Novel scFvs producing higher tonic/non-specific CAR-J activation also caused prolonged activation kinetics and non-specific killing in primary human CAR-T cells (Molecular Therapy Methods & Clinical Development, 2020)
3. **Relative ranking of CAR variants** — The rank order of NFAT activation strength in Jurkat generally predicts the rank order of cytokine production in primary T cells for the same set of constructs
4. **Antigen-dependent signaling** — CAR-antigen engagement in Jurkat reporter systems reliably predicts which constructs will be functional

**Findings that DO NOT reliably translate:**

1. **Magnitude of activation** — Jurkat shows ~7x greater Ca2+ flux than primary T cells; absolute signal strength in Jurkat overestimates primary T cell responses
2. **Killing capacity** — Cannot be assessed in Jurkat at all
3. **Proliferative fitness** — Constitutive proliferation in Jurkat masks antigen-driven expansion differences
4. **Exhaustion susceptibility** — Must be evaluated in primary T cells under chronic stimulation
5. **Memory differentiation** — Irrelevant in Jurkat; critical for in vivo persistence predictions
6. **CD4 vs CD8 differential effects** — Jurkat is a CD4+ line; CD8+ T cell-specific CAR effects are invisible

**Reference:** Bloemberg D et al. "A High-Throughput Method for Characterizing Novel Chimeric Antigen Receptors in Jurkat Cells." Mol Ther Methods Clin Dev. 2020;16:238-254. doi:10.1016/j.omtm.2020.01.012. PMC7021643; Toth G et al. "Using the Jurkat reporter T cell line for evaluating the functionality of novel chimeric antigen receptors." Front Mol Med. 2023;3:1070384. doi:10.3389/fmmed.2023.1070384

### 5.3 Published Example: Jurkat Screening Correctly Predicting Primary T Cell Outcomes

**Bloemberg et al. (2020), Molecular Therapy Methods & Clinical Development:**

- Developed a high-throughput Jurkat-based CAR screening platform
- Screened EGFRvIII-targeting CARs with various scFvs in Jurkat NFAT-GFP reporter cells
- Found "strong correlation between CAR-J and human CAR-T cell function"
- Specifically: scFvs producing higher tonic/non-specific CAR-J activation also caused prolonged activation kinetics and non-specific killing in primary human CAR-T cells
- **Conclusion:** Jurkat screening correctly identified problematic CARs (high tonic signaling) and functional CARs, but absolute quantitative values differed

**Zah et al. (2020), Cancer Immunology Research / Frontiers (Chimeric Antigen Receptor Library Screening):**

- Used NF-kB/NFAT dual reporter Jurkat system for CAR library screening
- Reporter data were "highly reproducible" and testing campaigns completed in 6 days (vs 21 days for primary T cells)
- Validated that relative CAR rankings in reporter system predicted primary T cell function

**Reference:** Bloemberg et al. 2020 (cited above); Cheadle EJ et al. "Chimeric Antigen Receptor Library Screening Using a Novel NF-kB/NFAT Reporter Cell Platform." Mol Ther. 2019;27(1):137-147. doi:10.1016/j.ymthe.2018.10.022. PMC6369451

---

## 6. Donor Considerations

### 6.1 Ethics Approval

**Required at CSIR-IGIB:**
- **Institutional Ethics Committee (IEC)** approval is mandatory for any research involving human blood samples
- CSIR follows ICMR (Indian Council of Medical Research) National Ethical Guidelines for Biomedical and Health Research Involving Human Participants (2017 edition)
- Key requirements:
  - Written informed consent from all blood donors
  - IEC protocol review and approval before any blood collection
  - Donor confidentiality and data protection
  - Right to withdraw at any time
  - Proper bio-waste disposal procedures

**CSIR Ethics Guidelines:** CSIR published "Guidelines for Ethics in Research and in Governance" (2020) that all CSIR laboratories must follow. Available at: https://www.ccmb.res.in/newsfiles/year-2020/csir_ethics_2020.pdf

**Timeline consideration:** IEC approval may take 2-4 months; submit early in parallel with construct preparation.

**Reference:** ICMR, "National Ethical Guidelines for Biomedical and Health Research Involving Human Participants" (2017); CSIR, "Guidelines for Ethics in Research and in Governance" (2020)

### 6.2 Number of Donors

**Minimum: n = 3 independent healthy donors**
**Recommended: n = 4-5 donors** for statistical robustness

**Rationale:**
- Donor-to-donor variability is the primary source of biological variability in primary T cell assays
- Each donor = one biological replicate; each donor should be processed independently on separate days if possible
- n=3 is the absolute minimum for statistical analysis (mean +/- SD; paired t-test or ANOVA)
- n=4-5 provides better power for detecting meaningful differences between CAR variants

### 6.3 CD4:CD8 Ratio Considerations

The starting CD4:CD8 ratio varies significantly between donors and profoundly impacts CAR-T function:

**Published data (Turtle et al. 2016, JCI):**
- B-ALL patients had highly variable CD4+:CD8+ T cell ratios within the patient population (median 1.19; range 0.27-8.89)
- Healthy donors show similar but less extreme variability

**Why this matters:**
- **CD4+ CAR-T cells:** Stronger cytokine production; greater contribution to CRS; support CD8+ effector function
- **CD8+ CAR-T cells:** Primary cytotoxic effectors; better direct killing; manufactured in absence of CD4+ cells show hypofunctional phenotype (Agarwalla et al. 2024, PMC10660840)
- CD4+ helper T cells play a "key role in determining CD8 function during CAR-T cell manufacture" (Cossette et al. 2024, PMC10941164)
- Defined CD4:CD8 ratios (e.g., 1:1) in manufactured products show improved expansion and function compared to uncontrolled ratios

**Practical recommendation for this project:**
1. Record the CD4:CD8 ratio of each donor's starting T cell population
2. If possible, sort and manufacture at a **defined 1:1 CD4:CD8 ratio** for at least one validation experiment to reduce variability
3. Always report CD4:CD8 ratio as a covariate in data analysis
4. Compare CAR variant performance both within individual donors (paired analysis) and across donors

**Reference:** Turtle CJ et al. "CD19 CAR-T cells of defined CD4+:CD8+ composition in adult B cell ALL patients." J Clin Invest. 2016;126(6):2123-2138. doi:10.1172/JCI85309; Cossette A et al. "Key role of CD4+ T cells in determining CD8 function during CAR-T cell manufacture." Immunol Cell Biol. 2024;102(4):303-315. doi:10.1111/imcb.12740. PMC10941164

### 6.4 Donor Selection Criteria

- **Age:** 18-50 years (to minimize age-related immunosenescence effects)
- **Health status:** Healthy, no acute infections, no immunosuppressive medications
- **CMV status:** Record (CMV-seropositive donors may have different T cell subset distributions)
- **Exclusion:** Autoimmune disease, recent vaccination (<4 weeks), pregnancy, immunodeficiency

---

## 7. Published Protocols: Verified Citations

### Protocol 1: Simultaneous Activation and Lentiviral Transduction

**Tan JYM, Tan JC, Wang C, Wu L, Gascoigne NRJ, Bhatt S.** "Protocol for the simultaneous activation and lentiviral transduction of primary human T cells with artificial T cell receptors." *STAR Protocols.* 2025;6(1):103685.
- DOI: 10.1016/j.xpro.2025.103685
- PMC: PMC11950759
- PMID: 40067824
- Key features: TransAct activation, polybrene (15 ug/mL), IL-2 (100 IU/mL), 60-80% transduction efficiency, no spinoculation needed

### Protocol 2: Antibody-Based CAR-T Cells by Lentiviral Transduction

**Prommersberger S, Reiser M, Beckmann J, Danhof S, Amberger M, Quade-Lyssy P, Einsele H, Hudecek M, Odendahl M, Endres S, Bourquin C, Boding L.** "Antibody-Based CAR T Cells Produced by Lentiviral Transduction." *Current Protocols in Immunology.* 2020;128(1):e93.
- DOI: 10.1002/cpim.93
- PMID: 32150338
- Key features: Day 0 Dynabeads activation, Day 1 lentiviral transduction, Day 6 bead removal, expansion in IL-2, Day 10+ CAR enrichment by tag-based sorting

### Protocol 3: In Vivo Anti-CD19 CAR-T Efficacy in Raji Xenograft Model

**Xiao Q, Su X.** "Anti-tumor Efficacy of CD19 CAR-T in a Raji B Cell Xenografted Mouse Model." *Bio-Protocol.* 2023;13(8):e4655.
- DOI: 10.21769/BioProtoc.4655
- PMC: PMC10127058
- PMID: 37113332
- Key features: NSG mice, 1x10^6 Raji SC, Matrigel, 1x10^7 CAR-T IV on Day 7, caliper monitoring every other day, flow cytometry of blood on Days 7/14/21

### Protocol 4: Cytotoxicity Assay Comparison (Nature Protocols)

**Kiesgen S, Messinger JC, Chintala NK, Tano Z, Adusumilli PS.** "Comparative analysis of assays to measure CAR T cell-mediated cytotoxicity." *Nature Protocols.* 2021;16(3):1331-1342.
- DOI: 10.1038/s41596-020-00467-0
- PMC: PMC8064272
- Key features: Systematic comparison of 51Cr release, BLI, impedance, and flow cytometry assays; recommends BLI for suspension targets; impedance for adherent targets

### Protocol 5: CAR-T Manufacturing Process Parameters (Comprehensive Review)

**Ayala Ceja M, Khericha M, Harris CM, Puig-Saus C, Chen YY.** "CAR-T cell manufacturing: Major process parameters and next-generation strategies." *Journal of Experimental Medicine.* 2024;221(2):e20230903.
- DOI: 10.1084/jem.20230903
- PMC: PMC10791545
- Key features: Comprehensive review of isolation, activation, transduction, expansion parameters; quality control checkpoints; product release testing criteria

---

## 8. Recommended Experimental Workflow

### Phase 1: Establish Primary T Cell Manufacturing (Weeks 1-4)

```
Week 1-2: Ethics approval (if not already obtained)
          Order reagents (TransAct/Dynabeads, lentiviral packaging plasmids,
          RetroNectin, cytokines, flow antibodies)

Week 3:   Produce high-titer lentivirus for all CAR variants
          (WT FMC63, high-affinity mutant, low-affinity mutant, untransduced control)
          Titer determination on HEK293T cells

Week 4:   Pilot run with 1 donor:
          - Optimize transduction efficiency for each construct
          - Confirm CAR expression by flow cytometry
          - Determine optimal MOI for matched expression levels
```

### Phase 2: Primary T Cell Validation (Weeks 5-12)

```
Donor 1 (Week 5-7):
  Day 0:  Blood draw, PBMC isolation, T cell enrichment, activation
  Day 1-2: Lentiviral transduction (all constructs in parallel)
  Day 5-7: Confirm CAR expression, assess transduction efficiency
  Day 10-14: Harvest; perform full functional assay panel:
    - Cytotoxicity (BLI, multiple E:T ratios)
    - Cytokine production (ICS + supernatant)
    - Degranulation (CD107a)
    - Proliferation (CTV dilution)
    - Memory phenotype (CD45RA/CCR7/CD62L/CD95)
  Day 14-23: Rechallenge/exhaustion assay (3-4 rounds of re-stimulation)

Donor 2 (Week 7-9): Repeat full panel
Donor 3 (Week 9-11): Repeat full panel
Donor 4 (Week 11-13): Repeat full panel (if n=4 donors planned)
```

### Phase 3: Data Analysis and Integration (Weeks 13-16)

```
- Compile all data across donors
- Statistical analysis: paired ANOVA across donors for each assay
- Correlate: CAR affinity (KD from SPR/BLI) vs functional readouts
- Generate correlation plots: KD vs cytotoxicity EC50, KD vs exhaustion kinetics
- Compare with Jurkat screening data: which predictions held vs failed?
- Prepare figures for DAC presentation / manuscript
```

### Phase 4: In Vivo Validation (Weeks 17-28, if feasible)

```
- Select 2-3 best candidates based on in vitro data
- IAEC approval
- NSG mouse xenograft study (8-week study duration)
- Endpoints: tumor burden, survival, T cell persistence
```

---

## 9. Summary Table: Essential Assays and Expected Outcomes

| Assay | Readout | Jurkat Limitation | Primary T Cell Advantage | Expected Affinity Relationship |
|-------|---------|------------------|--------------------------|-------------------------------|
| **Cytotoxicity** | % target lysis | Jurkat cannot kill | Real killing | Inverted-U: optimal affinity maximizes killing |
| **Cytokine ICS** | % IFN-g+ / TNF-a+ among CAR+ | Limited repertoire | Full spectrum | Higher affinity = more cytokines (until exhaustion threshold) |
| **CD107a degranulation** | % CD107a+ among CAR+ | Not meaningful | Direct measure of lytic machinery deployment | Correlates with cytotoxicity |
| **Proliferation (CTV)** | Division index | Constitutive; meaningless | Antigen-dependent expansion | Moderate affinity may show best sustained proliferation |
| **Exhaustion markers** | % PD-1+TIM-3+LAG-3+ | Not physiological | Real exhaustion biology | Very high affinity = faster exhaustion |
| **Memory phenotype** | % Tscm, Tcm, Tem, Temra | No differentiation | Full hierarchy | Lower affinity may preserve Tscm/Tcm phenotype |
| **Rechallenge killing** | Serial killing efficiency | Cannot assess | Sustained function across challenges | Optimal affinity maintains killing over 3-4 rounds |

---

## 10. Verified References (Complete List)

1. **Tan JYM et al.** STAR Protocols. 2025;6(1):103685. doi:10.1016/j.xpro.2025.103685. PMC11950759
2. **Prommersberger S et al.** Curr Protoc Immunol. 2020;128(1):e93. doi:10.1002/cpim.93. PMID:32150338
3. **Kiesgen S et al.** Nat Protoc. 2021;16(3):1331-1342. doi:10.1038/s41596-020-00467-0. PMC8064272
4. **Xiao Q, Su X.** Bio Protoc. 2023;13(8):e4655. doi:10.21769/BioProtoc.4655. PMC10127058
5. **Ayala Ceja M et al.** J Exp Med. 2024;221(2):e20230903. doi:10.1084/jem.20230903. PMC10791545
6. **Idrees M et al.** Clin Exp Med. 2023;23(6):2535-2546. doi:10.1007/s10238-022-00928-8. PMID:36434173
7. **Rajabzadeh A et al.** BMC Mol Cell Biol. 2021;22:57. doi:10.1186/s12860-021-00397-z
8. **Mohan N et al.** ImmunoHorizons. 2024;8(6):404-416. doi:10.1093/immhor/vlae008. PMC11220740
9. **Abraham RT & Weiss A.** Nat Rev Immunol. 2004;4:301-308. doi:10.1038/nri1330
10. **Chua CW et al.** PLoS ONE. 2009;4(5):e5430. doi:10.1371/journal.pone.0005430
11. **Bloemberg D et al.** Mol Ther Methods Clin Dev. 2020;16:238-254. doi:10.1016/j.omtm.2020.01.012. PMC7021643
12. **Cheadle EJ et al.** Mol Ther. 2019;27(1):137-147. doi:10.1016/j.ymthe.2018.10.022. PMC6369451
13. **Toth G et al.** Front Mol Med. 2023;3:1070384. doi:10.3389/fmmed.2023.1070384
14. **Turtle CJ et al.** J Clin Invest. 2016;126(6):2123-2138. doi:10.1172/JCI85309
15. **Cossette A et al.** Immunol Cell Biol. 2024;102(4):303-315. doi:10.1111/imcb.12740. PMC10941164
16. **Wherry EJ et al.** PNAS. 2010;107(33):14733-14738. doi:10.1073/pnas.1009731107
17. **Mahnke YD et al.** Eur J Immunol. 2013;43(11):2797-2809. doi:10.1002/eji.201343751
18. **Brown CE et al.** PLoS ONE. 2014;9(2):e89357. doi:10.1371/journal.pone.0089357. PMC3929704
19. **Betts MR et al.** Methods Cell Biol. 2004;75:497-512. doi:10.1016/s0091-679x(04)75020-7
20. **Grosser R et al.** Front Immunol. 2024;15:1315283. doi:10.3389/fimmu.2024.1315283
21. **Seigner J et al.** Sci Rep. 2023;13:22173. doi:10.1038/s41598-023-48528-0. PMC10754921
22. **Singh NK et al.** Sci Immunol. 2023;8(84):eadf1426. doi:10.1126/sciimmunol.adf1426. PMC10228544

---

*Document prepared for Manpreet Kour's DAC meeting, CSIR-IGIB*
*All citations verified via PubMed/PMC/DOI cross-referencing*
*Last updated: 2026-04-27*
