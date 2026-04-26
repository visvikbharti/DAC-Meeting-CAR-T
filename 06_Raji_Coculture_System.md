# Raji Cell Co-Culture System for CAR-T Functional Assays

## DAC Meeting Reference Document
### Manpreet Kour | PI: Dr. Kausik Chakraborty | Co-PI: Dr. Ankesh Kumar Jaiswal
### CSIR-IGIB | AcSIR Reg. 10BB25J02028

---

## 1. Cell Lines

### 1.1 Raji Cells (Target)

**ATCC Catalog Number:** CCL-86
**Source:** R.J.V. Pulvertaft, 1963

| Parameter | Detail | Source |
|-----------|--------|--------|
| Organism | Human (*Homo sapiens*) | ATCC CCL-86 |
| Disease | Burkitt's lymphoma | ATCC CCL-86 |
| Tissue origin | Left maxilla (jaw) | ATCC CCL-86 |
| Patient | 11-year-old Black male | ATCC CCL-86 |
| Cell type | B lymphocyte / lymphoblast | ATCC CCL-86 |
| Morphology | Lymphoblast, round | ATCC CCL-86 |
| Growth properties | Suspension (single cells + clusters) | ATCC CCL-86 |
| EBV status | Positive (EBV DNA by PCR) | ATCC CCL-86 |
| Doubling time | ~34 hours | ATCC Technical Data Sheet |

**Culture Conditions (ATCC-recommended):**
- **Base medium:** ATCC-formulated RPMI-1640 (ATCC Cat. No. 30-2001)
- **Serum:** 10% FBS (ATCC Cat. No. 30-2020)
- **Temperature:** 37 degrees C
- **Atmosphere:** 5% CO2, humidified incubator
- **Seeding density:** 2-3 x 10^5 viable cells/mL
- **Subculture when:** Cells reach 2-3 x 10^6 viable cells/mL
- **Medium change:** Every 2-3 days
- **Orientation:** Culture flask horizontal

**CD19 Expression:**
- Raji cells constitutively express high levels of CD19, CD20, CD22, and CD38 (verified by ATCC)
- Quantitative CD19 surface density: approximately 14,000-57,000 molecules per cell, measured by antibody binding capacity (ABC) assay using BD PE Fluorescence Quantitation Kit with PE-anti-human CD19 (clone SJ25C1) (Sigma-Aldrich Technical Bulletin)
- **Note:** Exact molecules-per-cell value should be confirmed by the student using QuantiBRITE PE beads + anti-CD19 PE staining on the lab's own Raji stock

**Luciferase-expressing derivatives (for bioluminescence killing assays):**
- Raji-Luc2: ATCC CCL-86-LUC2
- Raji-GFP-Luc2: ATCC CCL-86-GFP-LUC2

### 1.2 Jurkat Cells (Effector)

**ATCC Catalog Number:** TIB-152 (Clone E6-1)

| Parameter | Detail |
|-----------|--------|
| Organism | Human (*Homo sapiens*) |
| Disease | Acute T cell leukemia |
| Cell type | T lymphocyte (CD4+) |
| Growth properties | Suspension |

**Culture Conditions (ATCC-recommended):**
- **Base medium:** ATCC-formulated RPMI-1640 (ATCC Cat. No. 30-2001)
- **Serum:** 10% FBS (ATCC Cat. No. 30-2020)
- **Temperature:** 37 degrees C
- **Atmosphere:** 5% CO2
- **Seeding density:** 2-4 x 10^5 viable cells/mL
- **Maintain between:** 1 x 10^5 and 3 x 10^6 cells/mL
- **pH at seeding:** 7.0-7.6

**Key Jurkat Characteristics Relevant to CAR-T Studies:**

| Feature | Jurkat Cells | Primary T Cells |
|---------|-------------|-----------------|
| Cytolytic activity | Minimal (altered perforin/granzyme pathway) | Full cytolytic capacity |
| IL-2 production | Yes, upon activation | Full cytokine repertoire |
| Primary readout | CD69 upregulation, NFAT reporter | Cytotoxicity, cytokines, proliferation |
| Proliferation | Constitutive (immortalized) | Activation-dependent |
| CD4/CD8 status | CD4+, no CD8 | Mixed CD4+/CD8+ |
| PTEN status | Null (constitutive PI3K/AKT activation) | Wild-type |

### 1.3 K562 Cells (CD19-Negative Control Target)

**ATCC Catalog Number:** CCL-243
- Chronic myelogenous leukemia (CML) line
- Does NOT express CD19, CD20, or CD22
- Standard negative control for anti-CD19 CAR specificity assays
- Culture conditions: RPMI-1640 + 10% FBS, same as Raji

---

## 2. Co-Culture Assay Setup

### 2.1 Standard Co-Culture Medium

**Formulation (commonly abbreviated "R10"):**
- RPMI-1640 base medium
- 10% heat-inactivated FBS
- 1% Penicillin/Streptomycin (100 IU/mL pen + 100 ug/mL strep)
- Optional: 2 mM L-glutamine (or GlutaMAX)
- Optional: 10 mM HEPES buffer

**Important:** No exogenous cytokines (no IL-2, no IL-7) during co-culture — this tests intrinsic CAR-T function.

### 2.2 Plate Format and Seeding Densities

**For flow cytometry-based readouts (CD69, activation, phenotyping):**

| Parameter | Specification | Reference |
|-----------|--------------|-----------|
| Plate format | 96-well round-bottom (U-bottom) | Bloemberg et al., 2020 |
| Target cell density | 5 x 10^3 - 5 x 10^4 cells/well | Foulke et al., 2024 |
| Volume of target cells | 50 uL complete media | Foulke et al., 2024 |
| Volume of effector cells | 50 uL added on top | Foulke et al., 2024 |
| Total volume per well | 100 uL | Standard |
| Replicates | Triplicate per condition | Standard |

**For validated potency assay (flow cytometry):**

| Parameter | Specification | Reference |
|-----------|--------------|-----------|
| Plate format | 24-well plate | Piccinini et al., 2024 |
| E:T ratio | 1:1 | Piccinini et al., 2024 |
| Co-culture duration | 24 hours (validated 23-25h) | Piccinini et al., 2024 |
| Readout | CD3-/CD19+/7-AAD+ dead targets | Piccinini et al., 2024 |

**For bioluminescence killing assay:**

| Parameter | Specification | Reference |
|-----------|--------------|-----------|
| Plate format | 96-well flat-bottom (white/opaque) | Foulke et al., 2024 |
| Target cells | 5 x 10^3 Raji-Luc2 per well | Foulke et al., 2024 |
| E:T ratios | 1:1, 2:1, 5:1, 10:1 | Multiple studies |
| Luminescence reagent | Bright-Glo (Promega) | Standard |
| Read time | Within 10 min of reagent addition | Promega protocol |

### 2.3 Incubation Conditions

| Parameter | Standard |
|-----------|---------|
| Temperature | 37 degrees C |
| CO2 | 5% |
| Humidity | >95% relative humidity |
| Incubator type | Humidified CO2 incubator |

---

## 3. Cytotoxicity Readout Methods

### 3.1 Bioluminescence / Luciferase-Based Killing Assay (Gold Standard for CAR-T)

**Principle:** Target cells express firefly luciferase (Raji-Luc2). Viable targets produce light; dead targets do not.

**Protocol:**
1. Plate Raji-Luc2 cells at 5 x 10^3 per well in 50 uL R10 medium (96-well flat-bottom white plate)
2. Add CAR-Jurkat cells at desired E:T ratios in 50 uL
3. Incubate 24 hours at 37C/5% CO2
4. Add 100 uL Bright-Glo reagent (Promega) per well
5. Incubate 10 minutes at room temperature
6. Read luminescence on plate reader

**Calculation:**
```
% Specific Killing = 100 x (1 - RLU_sample / RLU_target-alone)
```

**Advantages:** High throughput, quantitative, no radioactivity
**Reference:** Kiesgen et al., *Nature Protocols* 16:1331-1342, 2021 (PMC8064272)

### 3.2 Flow Cytometry-Based Live/Dead Discrimination

**Principle:** Distinguish effector (CD3+) from target (CD19+) by surface markers; identify dead cells by viability dye.

**Protocol:**
1. Set up co-culture in 24-well or 96-well round-bottom plates
2. At 24h, harvest cells into FACS tubes
3. Stain with anti-CD3 + anti-CD19 + 7-AAD (or fixable viability dye)
4. Acquire on flow cytometer
5. Gate: CD3- CD19+ population = targets; 7-AAD+ = dead

**Calculation (Piccinini et al.):**
```
% Killing = (% dead targets with CAR-T) - (% dead targets with untransduced T cells)
```

**Advantages:** Simultaneous phenotyping of effector and target; no genetic modification of targets needed
**Reference:** Piccinini et al., *Cancer Immunol Immunother* 73:168, 2024 (PMC11219661)

### 3.3 LDH Release Assay

**Principle:** Lysed cells release lactate dehydrogenase into supernatant.
**Kit:** CytoTox 96 (Promega) or LDH-Glo (Promega)
**Readout:** Colorimetric (absorbance) or luminescence
**Timing:** 24-48 hours
**Limitation:** Both effector and target death release LDH — controls for spontaneous effector death are critical.

### 3.4 CD69 Upregulation Assay (Activation, Primary Jurkat Readout)

**Principle:** CD69 is an early T cell activation marker; measured by flow cytometry on CAR-Jurkat cells after co-culture.

**Protocol (Bloemberg et al., 2020):**
1. Co-culture CAR-Jurkat with Raji at 1:1, 1:10, 1:100 in 96-well round-bottom plates
2. Incubate overnight (~24 hours) at 37C/5% CO2
3. Stain with anti-CD69 (APC, clone FN50) + CAR detection antibody
4. Acquire on flow cytometer
5. Report CD69 MFI within CAR+ (GFP+) population

**Advantages:** High throughput, robust, validated correlation with primary T cell function (R^2 = 0.77-0.93 with primary T cell CD25/cytokine responses)
**Reference:** Bloemberg et al., *Mol Ther Methods Clin Dev* 16:238-254, 2020 (PMC7021643)

### 3.5 NFAT-Luciferase Reporter Assay (Activation, Not Killing)

**Principle:** Jurkat cells carrying NFAT-response element driving luciferase. CAR engagement triggers NFAT, producing luciferase signal.
**Timing:** 6-48 hours co-culture
**Use case:** Screening CAR constructs for signaling potency
**Commercial option:** BPS Bioscience Anti-CD19 CAR/NFAT-Luciferase Reporter Jurkat (Cat. No. 79853)

### 3.6 Cytokine Secretion (Complementary Readout)

- Co-culture supernatant collected at 18-24 hours
- IFN-gamma, TNF-alpha, IL-2 measured by ELISA
- E:T ratio: typically 1:1 for cytokine assays
- Plate: 96-well U-bottom, 200 uL total volume

---

## 4. Recommended Assay Strategy for This Project

Given the Jurkat/Raji system and FMC63 affinity optimization goals, the recommended multi-modal approach is:

### Tier 1: High-Throughput Screening (All Mutants)
- **CD69 activation assay:** Co-culture CAR-Jurkat with Raji at 1:1 in 96-well U-bottom, 24h, CD69 MFI by FACS
- **Purpose:** Rank all mutants by activation potency
- **Throughput:** One 96-well plate per E:T ratio per experiment

### Tier 2: Functional Characterization (Top Hits + Interesting Mutants)
- **Bioluminescence cytotoxicity** (if Raji-Luc2 available): E:T 1:1, 2:1, 5:1, 10:1 at 24h
- **Flow cytometry cytotoxicity:** CD3/CD19/7-AAD at 24h and 72h
- **Cytokine ELISA:** IFN-gamma, TNF-alpha at 24h from 1:1 co-culture
- **Exhaustion/activation FACS panels:** PD-1/TIM-3/LAG-3, CD69/CD25/CD107a at 24h and 48h

### Tier 3: In-Depth Characterization (Final Candidates)
- **Rechallenge assay:** 4 rounds over 7-12 days (see Document 09)
- **Chronic stimulation:** 14+ day protocol for exhaustion profiling
- **SPR/BLI kinetic characterization** of purified scFv
- **Primary T cell validation** (future)

---

## 5. Verified References

1. **Kiesgen S, Messinger JC, Chintala NK, Tano ZE, Adusumilli PS.** "Comparative analysis of assays to measure CAR T-cell-mediated cytotoxicity." *Nature Protocols* 16:1331-1342, 2021. PMID: 33589826. PMC8064272.

2. **Foulke JG, Chen L, Chang H, McManus CE, Tian F, Gu Z.** "Optimizing Ex Vivo CAR-T Cell-Mediated Cytotoxicity Assay through Multimodality Imaging." *Cancers* 16(14):2497, 2024. PMID: 39061136. PMC11274748.

3. **Bloemberg D, Nguyen T, MacLean S, et al.** "A High-Throughput Method for Characterizing Novel Chimeric Antigen Receptors in Jurkat Cells." *Mol Ther Methods Clin Dev* 16:238-254, 2020. PMID: 32083149. PMC7021643.

4. **Piccinini C, Carloni S, Arienti C, et al.** "In vitro CAR-T cell killing: validation of the potency assay." *Cancer Immunol Immunother* 73:168, 2024. PMID: 38953939. PMC11219661.

5. **Jahan F, Koski J, Schenkwein D, et al.** "Using the Jurkat reporter T cell line for evaluating the functionality of novel chimeric antigen receptors." *Front Mol Med* 3:1070384, 2023. PMID: 39086686. PMC11285682.

---

*All information verified through web searches of ATCC product pages, PubMed/PMC full-text articles, and manufacturer documentation. Date compiled: 2026-04-27.*
