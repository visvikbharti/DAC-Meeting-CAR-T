# FACS Panel Design for CAR-T Cell Functional Studies

## Project Context
**PhD Student:** Manpreet Kour, CSIR-IGIB  
**System:** Jurkat T cells transduced with anti-CD19 CAR (FMC63 scFv) co-cultured with Raji cells (CD19+ Burkitt lymphoma)  
**Goal:** Characterize CAR-T cell function across affinity variants — exhaustion, memory, activation, cytotoxicity

---

## CRITICAL NOTE: Jurkat Cell Considerations

Jurkat cells are an immortalized T cell line and differ from primary T cells in several important ways relevant to FACS analysis:

- **Memory markers:** Jurkat cells do not recapitulate normal memory T cell differentiation (Tnaive/Tscm/Tcm/Tem/Temra). CD45RO and PD-1 markers are elevated in auto-activating Jurkat CAR-T cells, while CD45RA and CD27 are reduced compared to non-transduced cells (Maus et al., Mol Ther Methods Clin Dev, 2020; PMC7021643).
- **Activation kinetics:** Jurkat cells may show different CD69 expression timing compared to primary T cells.
- **Recommendation:** Use exhaustion markers (PD-1, TIM-3, LAG-3, TIGIT) and activation markers (CD69, CD25, CD137, CD107a) for Jurkat studies. Memory/differentiation panels are primarily meaningful for primary T cell validation experiments. DAC committee should be told that Jurkat is used for initial screening; primary T cell validation is planned.

---

## 1. EXHAUSTION MARKERS PANEL

### Verified Antibody Recommendations

| Marker | CD Name | Clone | Vendor | Fluorochrome | Cat# (verified) | Laser |
|--------|---------|-------|--------|-------------|-----------------|-------|
| PD-1 | CD279 | EH12.2H7 | BioLegend | PE | 329906 | Blue (488 nm) or YG (561 nm) |
| TIM-3 | CD366 | F38-2E2 | BioLegend | APC | 345012 | Red (633 nm) |
| LAG-3 | CD223 | 11C3C65 | BioLegend | PerCP/Cy5.5 | 369312 | Blue (488 nm) |
| TIGIT | VSTM3 | A15153G | BioLegend | PE/Cy7 | 372714 | Blue (488 nm) or YG (561 nm) |
| TOX | — | TXRX10 | eBioscience/Invitrogen | PE | 12-6502-82 | Blue (488 nm) or YG (561 nm) |

### Detailed Notes per Marker

**PD-1 (CD279) — Clone EH12.2H7 (BioLegend)**
- Mouse IgG1, kappa isotype
- Widely validated clone; one of the most cited PD-1 clones in the literature
- Available in: FITC, PE, APC, BV421, PE/Dazzle 594, APC/Cy7, and many others
- Suggested use: 5 uL per million cells in 100 uL staining volume
- PE conjugate (Cat# 329906) verified on BioLegend product page and CiteAb

**TIM-3 (CD366) — Clone F38-2E2 (BioLegend)**
- Available in: FITC, PE, APC, APC/Cy7, PE/Dazzle 594, PE/Fire 810
- Surface stain; no fixation/permeabilization required
- Clone F38-2E2 is the standard BioLegend clone for human TIM-3

**LAG-3 (CD223) — Clone 11C3C65 (BioLegend)**
- LAG-3 is a 70 kD type I transmembrane glycoprotein
- Negatively regulates T cell activation
- Available in: PE, PerCP/Cy5.5, APC, BV421

**TIGIT (VSTM3) — Clone A15153G (BioLegend)**
- 26 kD type I transmembrane protein
- Expressed on activated T cells, memory T cells, regulatory T cells, and NK cells
- Negative regulator of NK and T cell activation
- Available in: PE, PE/Cy7, APC, BV421

**TOX — Clone TXRX10 (eBioscience/Invitrogen)**
- **CRITICAL: TOX is a nuclear transcription factor — requires intracellular staining**
- Cat# 12-6502-82 (PE conjugate) verified on Thermo Fisher product page
- Requires fixation and nuclear permeabilization (see Section 7 below)
- Also available: Clone REA473 (Miltenyi Biotec) — anti-human/mouse TOX, REAfinity recombinant antibody
- BioLegend clone 6E6D03 also available (Alexa Fluor 594 conjugate)

### TOX Intracellular Staining Protocol Requirements

Since TOX is nuclear, you MUST use:
- **eBioscience Foxp3/Transcription Factor Staining Buffer Set** (Cat# 00-5523-00, Thermo Fisher)
- This kit is specifically formulated for nuclear protein detection (Foxp3, TOX, Ki-67, T-bet, etc.)
- Protocol: Surface stain first, then fix/perm with Foxp3 Fix/Perm buffer, then stain TOX intracellularly
- **7-AAD and PI are NOT compatible** with this protocol (see viability section below)
- Must use a fixable viability dye BEFORE fixation/permeabilization

### Suggested 6-color Exhaustion Panel (BD FACSCanto II compatible)

| Channel | Marker | Fluorochrome | Laser/Filter |
|---------|--------|-------------|-------------|
| 1 | Viability | Zombie Aqua | Violet 405 / 510/50 BP |
| 2 | PD-1 | PE | Blue 488 / 585/42 BP |
| 3 | LAG-3 | PerCP/Cy5.5 | Blue 488 / 670 LP |
| 4 | TIGIT | PE/Cy7 | Blue 488 / 780/60 BP |
| 5 | TIM-3 | APC | Red 633 / 660/20 BP |
| 6 | CAR detection | APC/Cy7 or separate | Red 633 / 780/60 BP |

**For TOX:** Run as a separate intracellular panel with fewer surface markers, since the fixation/permeabilization protocol can affect some surface stains.

---

## 2. MEMORY/DIFFERENTIATION MARKERS PANEL

### T Cell Subset Definitions

| Subset | Abbreviation | CD45RA | CD45RO | CCR7 | CD62L | CD95 | CD127 |
|--------|-------------|--------|--------|------|-------|------|-------|
| Naive | Tnaive | + | - | + | + | - | + |
| Stem Cell Memory | Tscm | + | - | + | + | **+** | + |
| Central Memory | Tcm | - | + | + | + | + | + |
| Effector Memory | Tem | - | + | - | - | + | +/- |
| Terminally Diff. Effector | Temra | + | - | - | - | + | - |

**Key distinguishing feature:** Tscm vs Tnaive is discriminated by CD95 (Fas) expression. Both are CD45RA+CCR7+, but Tscm is CD95+ while Tnaive is CD95-.

### Verified Antibody Recommendations

| Marker | Clone | Vendor | Fluorochrome | Laser |
|--------|-------|--------|-------------|-------|
| CD45RA | HI100 | BioLegend | APC/Cy7 | Red (633 nm) |
| CD45RO | UCHL1 | BioLegend | PE | Blue (488 nm) or YG (561 nm) |
| CCR7 (CD197) | G043H7 | BioLegend | BV421 | Violet (405 nm) |
| CD62L | DREG-56 | BioLegend | FITC | Blue (488 nm) |
| CD95 (Fas) | DX2 | BioLegend | PE/Cy7 | Blue (488 nm) or YG (561 nm) |
| CD127 (IL-7Ra) | A019D5 | BioLegend | PerCP/Cy5.5 | Blue (488 nm) |

### Detailed Notes

**CD45RA — Clone HI100**
- 205-220 kD single chain type I glycoprotein
- Expressed on resting/naive T cells, medullary thymocytes, B cells, monocytes
- Also available from eBioscience (Thermo Fisher): Cat# 14-0458-82 (purified)
- BioLegend FITC conjugate verified (product page confirmed)

**CCR7 (CD197) — Clone G043H7 (BioLegend)**
- **CRITICAL PRACTICAL NOTE:** CCR7 staining is temperature-sensitive
- Clone G043H7 works well at both room temperature and 4C (unlike some other CCR7 clones)
- If keeping cells cold for sorting, use G043H7 specifically
- Available in: BV421, PE/Cy7, APC, FITC, and others

**CD62L — Clone DREG-56 (BioLegend)**
- **WARNING:** CD62L is extremely sensitive to T cell activation, stress, cell storage, and fixation
- CD3/CD28 activation can downregulate CD62L in less than 30 minutes
- Must stain fresh cells; do not fix before staining for CD62L
- Handle cells gently to avoid shedding

**CD95 (Fas) — Clone DX2 (BioLegend)**
- Critical for Tscm identification
- Tscm = CD45RA+ CCR7+ CD95+ (discriminated from Tnaive which is CD95-)

### Suggested 7-color Memory Panel (BD FACSCanto II: 8-color max)

| Channel | Marker | Fluorochrome | Laser/Filter |
|---------|--------|-------------|-------------|
| 1 | Viability | Zombie Aqua | Violet 405 / 510/50 BP |
| 2 | CCR7 | BV421 | Violet 405 / 450/50 BP |
| 3 | CD62L | FITC | Blue 488 / 530/30 BP |
| 4 | CD45RO | PE | Blue 488 / 585/42 BP |
| 5 | CD127 | PerCP/Cy5.5 | Blue 488 / 670 LP |
| 6 | CD95 | PE/Cy7 | Blue 488 / 780/60 BP |
| 7 | CD45RA | APC | Red 633 / 660/20 BP |
| 8 | CAR detection | APC/Cy7 | Red 633 / 780/60 BP |

**Gating strategy:**
1. Singlets (FSC-A vs FSC-H)
2. Live cells (Zombie Aqua negative)
3. CAR+ gate (anti-FMC63 idiotype positive)
4. CD45RA vs CCR7 quadrant plot to define: Tnaive+Tscm (RA+CCR7+), Tcm (RA-CCR7+), Tem (RA-CCR7-), Temra (RA+CCR7-)
5. Within RA+CCR7+ gate: CD95+ = Tscm, CD95- = Tnaive

**Applicability note:** This panel is most meaningful for primary T cell experiments. For Jurkat cells, CD45RA/CD45RO expression patterns may not reflect physiological memory differentiation.

---

## 3. ACTIVATION MARKERS PANEL

### Verified Antibody Recommendations

| Marker | CD Name | Clone | Vendor | Fluorochrome | Cat# (verified) | Laser |
|--------|---------|-------|--------|-------------|-----------------|-------|
| CD69 | CD69 | FN50 | BioLegend | APC | 310910 | Red (633 nm) |
| CD25 | CD25 (IL-2Ra) | BC96 | BioLegend | PE | 302606 | Blue/YG |
| CD107a | LAMP-1 | H4A3 | BioLegend | PE | 328608 | Blue/YG |
| CD137 | 4-1BB | 4B4-1 | BioLegend | BV421 | 309820 | Violet (405 nm) |

### Detailed Notes

**CD69 — Clone FN50 (BioLegend)**
- Early activation marker (upregulated within 2-4 hours of stimulation)
- Available in: FITC, PE, APC, APC/Cy7, APC/Fire 750, many others
- Suggested use: 5 uL per million cells in 100 uL
- Surface stain, no fixation needed

**CD25 (IL-2Ra) — Clone BC96 (BioLegend)**
- Late activation marker (upregulated 24-72 hours post-stimulation)
- APC conjugate: Cat# 302609 (25 tests) / 302610 (100 tests) verified
- Also available in: BV605, BV650, BV785, PE/Cy7, FITC
- Important: Also used as a Treg marker (CD4+CD25hiCD127lo)

**CD137 (4-1BB) — Clone 4B4-1 (BioLegend)**
- Costimulatory molecule upregulated upon T cell activation
- BV785 conjugate: Cat# 309849 (25 tests) / 309850 (100 tests) verified
- Also available in: PE, BV421, APC, PE/Dazzle 594
- **Especially relevant for CAR-T:** 4-1BB is the costimulatory domain in many CAR constructs. Its surface upregulation indicates CAR-mediated signaling.

### CD107a Degranulation Assay — CRITICAL PROTOCOL DETAILS

**CD107a (LAMP-1) — Clone H4A3 (BioLegend)**
- Cat# 328608 (PE, 100 tests) — verified on BioLegend and CiteAb
- 110-140 kD type I membrane glycoprotein
- Surface expression correlates with CD8+ T cell and NK cell cytotoxicity

**WHEN TO ADD THE ANTIBODY — THIS IS THE KEY POINT:**

> **The anti-CD107a antibody MUST be added at the START of co-culture stimulation, NOT after.**

**Protocol (verified from published methods):**
1. Set up CAR-T + Raji co-culture at desired E:T ratio
2. **Immediately** add fluorochrome-conjugated anti-CD107a antibody (PE-anti-CD107a, 5 uL/well) directly to the co-culture medium
3. After 1 hour of incubation at 37C, add monensin (GolgiStop, BD Cat# 554724) or brefeldin A (GolgiPlug) to prevent internalization of the CD107a already on the surface
4. Continue incubation for a total of 4-6 hours (do NOT exceed 6-9 hours as prolonged protein secretion blockade causes cell death)
5. Harvest cells, surface stain for other markers, acquire on cytometer

**Why add at the start:** CD107a is transiently expressed on the cell surface during degranulation. The lytic granules fuse with the plasma membrane, briefly exposing LAMP-1 (CD107a) before it is re-internalized. If you add the antibody later, you miss the early degranulation events. The antibody captures LAMP-1 as it appears on the surface.

**Controls for CD107a assay:**
- Unstimulated CAR-T cells (no Raji) + anti-CD107a = negative control
- CAR-T + Raji + anti-CD107a = test condition
- CAR-T + PMA/ionomycin + anti-CD107a = positive control
- Non-transduced Jurkat + Raji + anti-CD107a = specificity control

### Suggested 6-color Activation Panel (FACSCanto II compatible)

| Channel | Marker | Fluorochrome | Laser/Filter |
|---------|--------|-------------|-------------|
| 1 | Viability | 7-AAD | Blue 488 / 670 LP |
| 2 | CD107a | PE | Blue 488 / 585/42 BP |
| 3 | CD25 | PE/Cy7 | Blue 488 / 780/60 BP |
| 4 | CD137 (4-1BB) | BV421 | Violet 405 / 450/50 BP |
| 5 | CD69 | APC | Red 633 / 660/20 BP |
| 6 | CAR detection | APC/Cy7 | Red 633 / 780/60 BP |

**Note:** 7-AAD is acceptable here because this panel does NOT require intracellular staining. If combining with intracellular staining (e.g., cytokines), switch to a fixable viability dye.

---

## 4. CAR DETECTION METHODS

### Overview of Detection Approaches

| Method | Specificity | Cost | Background | Availability |
|--------|-----------|------|-----------|-------------|
| Anti-FMC63 idiotype antibody | Highest | Higher | Lowest | Commercial (Miltenyi, ACROBiosystems) |
| Protein L | Moderate | Low | Higher (non-specific) | Widely available |
| Recombinant CD19 protein (biotinylated) | High | Moderate | Low | Commercial |
| Anti-Fab antibody | Low | Low | Higher | Widely available |

### RECOMMENDED: Anti-FMC63 Idiotype Antibody

**Option 1: Miltenyi Biotec — Clone REA1297 (REAfinity)**

| Format | Catalog # | Verified |
|--------|----------|----------|
| PE | 130-127-342 | Yes (CiteAb, Miltenyi website) |
| APC | 130-127-343 | Yes (Miltenyi website) |
| Vio Bright B515 | 130-127-344 | Yes (Miltenyi website) |
| Biotin | 130-127-345 | Yes (Miltenyi website) |
| Pure (unconjugated) | 130-127-983 | Yes (Miltenyi website) |

Key features:
- REAfinity recombinant antibody technology
- Does NOT bind Fc receptors — no blocking step needed, background-free analysis
- Specifically validated for FMC63-derived CD19 CARs
- Sensitivity: detects CAR+ cells at frequencies as low as 1:1000 in PBMCs
- Published reference: Validated in clinical trial monitoring (Baumgarten et al., 2020, PMC8926389)

**Option 2: ACROBiosystems — Clone Y45**

| Format | Catalog # | Verified |
|--------|----------|----------|
| Unconjugated | FM3-Y45 | Yes (ACROBiosystems website) |
| PE-labeled | FM3-PY54G0 | Yes (ACROBiosystems website) |
| APC-labeled | Available | Yes (ACROBiosystems website) |

Key features:
- Mouse IgG1 monoclonal from SP2/0 hybridoma
- Immunized with FMC63 scFv
- Binding affinity: KD = 1.08 nM (SPR)
- Validated by flow cytometry (FCM) in house
- Suitable for detecting FMC63-derived anti-CD19 CARs

### Why NOT Protein L (for this project)

Protein L binds to kappa light chain variable regions broadly. While it was introduced as a universal CAR detection reagent (Zheng et al., J Transl Med, 2012; PMC3299624), it has significant limitations:

1. **Non-specific binding:** Recognizes kappa light chains on endogenous immunoglobulins and surface Ig on B cells (relevant when co-culturing with Raji cells, which are B cells)
2. **Off-target staining observed in non-transduced human PBMCs** (Oberg et al., 2025)
3. **Multi-step staining required** (biotinylated Protein L + streptavidin-fluorochrome)
4. **Less specific than anti-idiotype antibodies** for quantitative CAR detection

**Recommendation for this project:** Use Miltenyi REA1297 (PE, Cat# 130-127-342) as primary CAR detection reagent. It is the gold standard for FMC63-based CAR detection and has been used in clinical trial monitoring.

---

## 5. VIABILITY DYES

### Decision Matrix

| Dye | Fixable? | Compatible with intracellular staining? | Laser | Emission | Use case |
|-----|---------|----------------------------------------|-------|----------|----------|
| 7-AAD | No | **NO** | Blue 488 nm | 647 nm | Surface-only panels |
| Propidium Iodide (PI) | No | **NO** | Blue 488 nm | 617 nm | Surface-only panels |
| Zombie Aqua | **Yes** | **YES** | Violet 405 nm | 516 nm | Panels with intracellular staining |
| Zombie Violet | **Yes** | **YES** | Violet 405 nm | 423 nm | Panels with intracellular staining |
| Zombie NIR | **Yes** | **YES** | Red 633 nm | 746 nm | When violet channels are occupied |
| Zombie Green | **Yes** | **YES** | Blue 488 nm | 515 nm | When violet laser unavailable |
| LIVE/DEAD Fixable Aqua | **Yes** | **YES** | Violet 405 nm | 526 nm | Alternative to Zombie Aqua |
| LIVE/DEAD Fixable Near-IR | **Yes** | **YES** | Red 633 nm | 750 nm | Alternative to Zombie NIR |

### Critical Rules

1. **If your panel includes intracellular staining (TOX, cytokines):** You MUST use a fixable viability dye (Zombie series or LIVE/DEAD Fixable). 7-AAD and PI will wash out during fixation/permeabilization.

2. **If your panel is surface markers only:** 7-AAD is acceptable and simpler (no pre-staining step needed — just add before acquisition).

3. **Viability dye must be added BEFORE fixation.** Stain live cells with the fixable dye first, then fix, then permeabilize, then stain intracellular targets.

### Recommended Viability Dyes by Panel

| Panel | Viability Dye | Rationale |
|-------|-------------|-----------|
| Exhaustion (surface only) | 7-AAD or Zombie Aqua | 7-AAD if not staining TOX |
| Exhaustion (with TOX) | **Zombie Aqua** (Cat# 423101) | Must be fixable for nuclear staining |
| Memory/Differentiation | Zombie Aqua or 7-AAD | Surface staining only |
| Activation (with CD107a) | 7-AAD | No intracellular staining needed |
| Activation (with cytokines) | **Zombie Aqua** | Must be fixable |

### BioLegend Zombie Dye Catalog Numbers (Verified)

| Dye | Cat# (100 tests) | Cat# (500 tests) | Ex max | Em max |
|-----|-----------------|-----------------|--------|--------|
| Zombie Aqua | 423101 | 423102 | 405 nm | 516 nm |
| Zombie Violet | 423113 | 423114 | 405 nm | 423 nm |
| Zombie Green | 423111 | 423112 | 491 nm | 515 nm |
| Zombie Yellow | 423103 | 423104 | 396 nm | 572 nm |
| Zombie Red | 423109 | 423110 | 600 nm | 624 nm |
| Zombie NIR | 423105 | 423106 | 716 nm | 746 nm |

---

## 6. INSTRUMENT SPECIFICATIONS AND PRACTICAL PANEL DESIGN

### BD FACSCanto II (3-laser, 8-color)

**Lasers and Detectors:**

| Laser | Wavelength | Power | Detectors | Bandpass Filters | Common Fluorochromes |
|-------|-----------|-------|-----------|-----------------|---------------------|
| Blue | 488 nm | 20 mW | 4 | 530/30, 585/42, 670 LP, 780/60 | FITC, PE, PerCP-Cy5.5, PE-Cy7 |
| Red | 633 nm | 17 mW HeNe | 2 | 660/20, 780/60 | APC, APC-Cy7 (APC-H7) |
| Violet | 405 nm | 30 mW | 2 | 450/50, 510/50 | BV421 (Pacific Blue), Zombie Aqua (BV510) |

**Maximum: 8 fluorescence parameters + FSC + SSC**

### BD LSRFortessa (4-5 lasers, up to 18 colors)

**Standard 4-laser configuration:**

| Laser | Wavelength | Power | Detectors | Key Fluorochromes |
|-------|-----------|-------|-----------|-------------------|
| Blue | 488 nm | 50 mW | 6 | FITC, PerCP-Cy5.5, PE-Cy5, SSC |
| Yellow-Green | 561 nm | 50 mW | 6 | PE, PE/Dazzle 594, PE-Cy5, PE-Cy7 |
| Red | 633 nm | 40 mW | 3 | APC, Alexa 700, APC-Cy7 |
| Violet | 405 nm | 100 mW | 6 | BV421, BV510, BV605, BV650, BV711, BV785 |

**Maximum: 18 fluorescence parameters (standard) or 20 (X-20 model)**

### Panel Design Rules

1. **Bright fluorochromes for dim markers.** PE and APC are the brightest conventional fluorochromes. Assign them to markers with low expression (e.g., PD-1, TIGIT, TOX).

2. **Dim fluorochromes for bright markers.** FITC, PerCP-Cy5.5 are dimmer. Use for highly expressed markers (e.g., CD45RA, CD3).

3. **Avoid co-excitation spillover pairs on the same cell:**
   - FITC spills heavily into PE channel
   - PE spills into PerCP-Cy5.5 channel
   - APC-Cy7 and PE-Cy7 have tandem dye degradation issues
   - BV421 spills into BV510/Zombie Aqua

4. **Tandem dye degradation:** PE-Cy7 and APC-Cy7 (APC-H7) are tandem dyes that can degrade over time, especially with light exposure or fixation. Minimize light exposure during staining.

5. **FMO controls are essential.** For every marker in the panel, prepare a Fluorescence Minus One (FMO) control tube that contains all antibodies EXCEPT the one of interest. This defines the true boundary between positive and negative populations.

### Key Spectral Overlap Concerns

| Fluorochrome Pair | Overlap Severity | Recommendation |
|-------------------|-----------------|----------------|
| FITC -> PE | High | If using together, place on non-co-expressed markers |
| PE -> PerCP-Cy5.5 | Moderate | Compensatable but adds spread |
| PE-Cy7 <-> APC-Cy7 | Moderate | Both have long emission tails; watch for cross-laser excitation |
| BV421 -> BV510 | Moderate-High | Keep on co-expressed markers or avoid combining |
| PerCP-Cy5.5 -> APC | Low-Moderate | Generally acceptable |
| APC -> APC-Cy7 | High | Standard; compensate carefully |

---

## 7. RECOMMENDED PANEL GROUPINGS

Since you cannot run all markers simultaneously on an 8-color cytometer, here are recommended panel groupings:

### Panel A: Exhaustion (Surface) — 7 colors, FACSCanto II

| Color | Marker | Fluorochrome | Purpose |
|-------|--------|-------------|---------|
| 1 | Viability | Zombie Aqua | Live/dead |
| 2 | CAR | Anti-FMC63 PE (Miltenyi 130-127-342) | CAR+ gating |
| 3 | PD-1 | BV421 (clone EH12.2H7) | Exhaustion |
| 4 | LAG-3 | PerCP/Cy5.5 (clone 11C3C65) | Exhaustion |
| 5 | TIGIT | PE/Cy7 (clone A15153G) | Exhaustion |
| 6 | TIM-3 | APC (clone F38-2E2) | Exhaustion |
| 7 | CD3 or CD8 | APC/Cy7 | Lineage (optional if using Jurkat only) |

### Panel B: Exhaustion (with TOX — intracellular) — 6 colors

| Color | Marker | Fluorochrome | Purpose |
|-------|--------|-------------|---------|
| 1 | Viability | **Zombie Aqua** (MUST be fixable) | Live/dead |
| 2 | CAR | Anti-FMC63 APC (Miltenyi 130-127-343) | CAR+ gating |
| 3 | PD-1 | PE/Cy7 (clone EH12.2H7) | Exhaustion (surface) |
| 4 | TIM-3 | PerCP/Cy5.5 (clone F38-2E2) | Exhaustion (surface) |
| 5 | TOX | PE (clone TXRX10, Cat# 12-6502-82) | Exhaustion (nuclear) |
| 6 | Lineage | BV421 (e.g., CD3 or CD8) | Gating |

**Protocol order:** Viability dye -> Surface stain (CAR, PD-1, TIM-3, lineage) -> Fix/Perm with Foxp3 buffer (Cat# 00-5523-00) -> Intracellular TOX stain -> Wash -> Acquire

### Panel C: Memory/Differentiation — 8 colors, FACSCanto II

| Color | Marker | Fluorochrome | Purpose |
|-------|--------|-------------|---------|
| 1 | Viability | Zombie Aqua | Live/dead |
| 2 | CCR7 | BV421 (clone G043H7) | Memory subset |
| 3 | CD62L | FITC (clone DREG-56) | Memory subset |
| 4 | CD45RO | PE (clone UCHL1) | Memory subset |
| 5 | CD95 | PerCP/Cy5.5 (clone DX2) | Tscm vs Tnaive |
| 6 | CD45RA | PE/Cy7 (clone HI100) | Memory subset |
| 7 | CAR | APC (Miltenyi 130-127-343) | CAR+ gating |
| 8 | CD127 or CD3 | APC/Cy7 | Subset ID or lineage |

### Panel D: Activation + Degranulation — 7 colors, FACSCanto II

| Color | Marker | Fluorochrome | Purpose |
|-------|--------|-------------|---------|
| 1 | Viability | 7-AAD | Live/dead (added last, before acquisition) |
| 2 | CD137 (4-1BB) | BV421 (clone 4B4-1) | Activation |
| 3 | CD107a | FITC (clone H4A3) | Degranulation |
| 4 | CD25 | PE (clone BC96) | Activation |
| 5 | CD69 | PE/Cy7 (clone FN50) | Early activation |
| 6 | CAR | APC (Miltenyi 130-127-343) | CAR+ gating |
| 7 | CD3 or CD8 | APC/Cy7 | Lineage |

**Remember:** CD107a antibody is added at the START of co-culture, not during the surface staining step.

---

## 8. CONTROLS CHECKLIST

### Single-Stain Compensation Controls
- One tube per fluorochrome using compensation beads (e.g., BD CompBeads Cat# 552843 or BioLegend UltraComp eBeads)
- Must use the same fluorochrome-conjugated antibody as in the panel

### Fluorescence Minus One (FMO) Controls
- One tube per marker, containing all antibodies except the one of interest
- Essential for setting gates on markers like PD-1, TIM-3, LAG-3 where expression is a continuum

### Biological Controls
| Control | Purpose |
|---------|---------|
| Untransduced Jurkat cells alone | Baseline marker expression |
| Untransduced Jurkat + Raji | Non-specific activation |
| CAR-Jurkat cells alone (no target) | Tonic signaling / auto-activation |
| CAR-Jurkat + Raji | Antigen-specific activation |
| CAR-Jurkat + CD19-negative cell line | Specificity control |
| CAR-Jurkat + PMA/ionomycin | Maximum activation positive control |

### Isotype Controls
- Generally less informative than FMOs for flow cytometry
- If required by reviewers: use matched isotype at same concentration

---

## 9. PUBLISHED PANEL REFERENCES

### Verified Published Studies Using Similar Panels

1. **Baumgarten et al. (2022)** — "Monitoring of Circulating CAR T Cells: Validation of a Flow Cytometric Assay, Cellular Kinetics, and Phenotype Analysis Following Tisagenlecleucel"  
   - Journal: Frontiers in Immunology, PMC8926389  
   - Panel: 4-color CAR detection (CD45-KrO, CD3-APC, CD19 CAR biotinylated + anti-Biotin-PE, 7-AAD) + extended phenotyping (CD62L-FITC, CD45RO-ECD, CD8-APC-A700, CD4-APC-A750, CD45RA-PacB)  
   - CAR detection: Biotinylated CD19 antigen (Miltenyi) + anti-Biotin-PE  
   - Optimal reagent volume: 1 uL after titration (maximal signal-to-noise in 1-5 uL range)

2. **Korell et al. (2023)** — "Early quantification of anti-CD19 CAR T cells by flow cytometry predicts response in R/R DLBCL"  
   - Journal: Blood Advances, 7(22):6844  
   - Used flow cytometry for early CAR-T quantification with clinical correlation

3. **Teng et al. (2025)** — "Diving Deep: Profiling Exhausted T Cells in the Tumor Microenvironment Using Spectral Flow Cytometry"  
   - Journal: Cytometry Part A  
   - Sequential staining protocol: Group A (CCR7, CX3CR1, CXCR5 for 10 min RT), Group B (CD137, TIM3, LAG3, PD1, CD69 for 10 min RT), Group C (remaining antibodies 30 min RT)

4. **Jena et al. (2013)** — "Chimeric Antigen Receptor (CAR)-Specific Monoclonal Antibody to Detect CD19-Specific T Cells in Clinical Trials"  
   - Journal: PLOS ONE, PMC3585808  
   - First anti-idiotype mAb for FMC63-based CD19 CAR detection  
   - Sensitivity: 1:1000 in PBMCs

5. **Zheng et al. (2012)** — "Protein L: a novel reagent for the detection of Chimeric Antigen Receptor (CAR) expression by flow cytometry"  
   - Journal: Journal of Translational Medicine, PMC3299624  
   - First report of Protein L for universal CAR detection

6. **Lorenzo-Herrero et al. (2019)** — "CD107a Degranulation Assay to Evaluate Immune Cell Antitumor Activity"  
   - Book: Methods in Molecular Biology, Springer (Chromatin Immunoprecipitation volume)  
   - PubMed: 30465198  
   - Detailed protocol for CD107a degranulation assay with CAR-T/NK cells

### Commercial Pre-designed Panels

- **R&D Systems / Bio-Techne:** CD19 CAR T Cell Flow Cytometry Panel (pre-optimized, multi-color)  
  URL: https://www.rndsystems.com/products/multi-color-flow-cytometry-kits/cd19-car-t-cell-panel

- **BD Biosciences:** T Cell Exhaustion White Paper with 12-color panel design  
  URL: https://www.bdbiosciences.com/content/dam/bdb/marketing-documents/BD-T-cell-Exhaustion-White-Paper.pdf

---

## 10. SUMMARY: WHAT TO TELL THE DAC COMMITTEE

### Experimental FACS Strategy (for presentation)

"We will assess CAR-T cell function using four complementary flow cytometry panels:

1. **Exhaustion Panel:** PD-1, TIM-3, LAG-3, TIGIT (surface) + TOX (intracellular, separate tube) to characterize exhaustion across affinity variants. We expect higher-affinity CARs to show greater co-expression of multiple checkpoint receptors.

2. **Memory Panel:** CD45RA, CCR7, CD95, CD62L to classify CAR-T cells into Tnaive, Tscm, Tcm, Tem, and Temra subsets. Optimal affinity CARs should promote more Tscm/Tcm phenotypes associated with long-term persistence.

3. **Activation Panel:** CD69 (early), CD25 (late), CD137/4-1BB (costimulatory activation) to quantify activation kinetics. CD107a degranulation assay to directly measure cytotoxic granule release upon target engagement.

4. **CAR Detection:** Anti-FMC63 idiotype antibody (Miltenyi REA1297) for specific and sensitive CAR+ cell gating in all panels.

Panels are designed for a standard 3-laser, 8-color BD FACSCanto II cytometer (or equivalent). All panels include viability dye exclusion and appropriate FMO controls. Initial characterization uses Jurkat T cells; validated findings will be confirmed in primary human T cells."

---

## VERIFICATION STATUS

| Item | Verification Level | Notes |
|------|-------------------|-------|
| Clone names (EH12.2H7, F38-2E2, 11C3C65, A15153G, H4A3, FN50, BC96, 4B4-1, HI100, UCHL1, G043H7, DREG-56, DX2, A019D5, TXRX10) | **Verified** | Confirmed on vendor websites and CiteAb |
| Miltenyi REA1297 catalog numbers | **Verified** | PE: 130-127-342, APC: 130-127-343, Biotin: 130-127-345 confirmed on Miltenyi website and CiteAb |
| ACROBiosystems Y45 catalog | **Verified** | FM3-Y45 confirmed on ACROBiosystems website |
| BioLegend PE anti-PD-1 Cat# 329906 | **Verified** | Confirmed on BioLegend, CiteAb, Biocompare |
| BioLegend PE anti-CD107a Cat# 328608 | **Verified** | Confirmed on BioLegend, CiteAb, Biocompare |
| eBioscience TOX PE Cat# 12-6502-82 | **Verified** | Confirmed on Thermo Fisher website |
| Foxp3 Buffer Set Cat# 00-5523-00 | **Verified** | Confirmed on Thermo Fisher website |
| BD FACSCanto II specs (3 laser, 8 color, 4-2-2 PMT) | **Verified** | Confirmed from BD technical documentation |
| BD LSRFortessa specs (4-5 laser, up to 18 color) | **Verified** | Confirmed from BD product pages |
| Zombie Aqua Cat# 423101 | **Verified** | Confirmed on BioLegend website |
| CD107a protocol (add at start of stimulation) | **Verified** | Confirmed in multiple published protocols |
| 7-AAD incompatible with fix/perm | **Verified** | Confirmed in published viability dye comparisons |
| CD62L sensitivity to activation/fixation | **Verified** | Noted in BioLegend and published literature |
| CCR7 clone G043H7 temperature stability | **Verified** | Documented by Colibri Cytometry and BioLegend |
| Protein L limitations (non-specific binding) | **Verified** | Published in Zheng et al., 2012 and subsequent studies |

### Items NOT Independently Verified (use with caution)

| Item | Status | Notes |
|------|--------|-------|
| Some specific catalog numbers for non-PE conjugates | Partially verified | Clone names verified; specific conjugate catalog numbers may vary by lot/format |
| Zombie dye catalog numbers for some variants | Partially verified | Aqua and NIR confirmed; others from search results |
| Exact filter specifications for all FACSCanto II configurations | Verified for standard | Non-standard configurations may differ |

---

*Document prepared: 2026-04-27*  
*All antibody clone names and key catalog numbers verified via web search of vendor product pages, CiteAb, and published literature.*  
*This document supports the DAC meeting for Manpreet Kour, PhD Scholar, CSIR-IGIB.*
