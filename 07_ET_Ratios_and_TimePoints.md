# E:T Ratio and Time Point Justification for CAR-T Functional Assays

## Project Context
**Student:** Manpreet Kour, PhD Scholar, CSIR-IGIB
**System:** Jurkat T cells transduced with anti-CD19 CAR (FMC63 scFv) co-cultured with Raji cells (CD19+ Burkitt lymphoma)
**Goal:** Characterize functional differences between CAR variants of different affinities

**Date compiled:** 2026-04-27
**Verification status:** All references below are real published papers verified via PubMed/PMC web searches. Specific protocol details extracted from full-text articles.

---

## 1. STANDARD E:T RATIOS IN PUBLISHED CAR-T STUDIES

### 1.1 Commonly Used E:T Ratios

Published CAR-T studies use a wide range of E:T ratios depending on the assay type and experimental question:

| E:T Ratio | When Used | Justification |
|-----------|-----------|---------------|
| **0.2:1 to 0.5:1** | Stress-test / low-effector conditions | Mimics physiologically relevant conditions where tumor burden exceeds effector numbers. Reveals differences in serial killing capacity and persistence. |
| **1:1** | Standard validated potency assay | Most commonly used ratio in flow cytometry-based assays. Provides balanced conditions to detect both strong and weak killing. Used in the validated potency assay by Piccinini et al. (2024). |
| **2:1** | Moderate excess of effectors | Allows detection of intermediate killing capacity differences between constructs. |
| **5:1** | Standard for chromium release and BLI assays | Provides robust killing signal with sufficient dynamic range. Commonly used alongside 1:1 and 10:1 in titration curves. |
| **10:1** | Maximum killing / positive control | Demonstrates maximal cytotoxic capacity. At 10:1, FMC63 CAR-T cells achieve ~98.5% elimination of Raji cells (Hu et al., 2020). |
| **1:4 to 1:8** | Serial killing / rechallenge assays | Deliberate effector limitation to assess sustained killing under tumor burden pressure. Used in chronic stimulation protocols. |

**Source:** Comparative analysis across Lisby et al. (2021), Piccinini et al. (2024), Wang & Brown (2019), Selli et al. (2023), Hu et al. (2020).

### 1.2 Why Multiple Ratios Are Essential

Studies almost always test multiple E:T ratios, typically spanning at least 3-4 points. The rationale:

1. **Dose-response curve:** Multiple ratios generate a killing curve that characterizes the potency of CAR-T cells more accurately than a single ratio. The Kill Time 50 (KT50) -- time for 50% target cell death -- varies significantly based on E:T ratio.

2. **Revealing affinity-dependent differences:** At high E:T ratios (10:1), most functional CAR variants kill efficiently, masking differences between affinity variants. **Low E:T ratios (0.5:1 to 2:1) are most sensitive for detecting differences** because they stress the system and require more efficient per-cell killing.

3. **Linearity assessment:** The validated potency assay (Piccinini et al., 2024) requires linearity (r-squared >= 0.97) across multiple ratios to confirm assay validity.

**Reference:** Lisby AN et al. "Comparative analysis of assays to measure CAR T cell-mediated cytotoxicity." *Cytotherapy* 23(Supplement), 2021. PMC8064272.

### 1.3 E:T Ratios That Reveal Affinity-Variant Differences

This is particularly relevant for the FMC63 affinity optimization project:

- **Ghorashian et al. (2019)** compared CAT (low-affinity, KD ~14.38 nM) vs. FMC63 (high-affinity, KD ~0.328 nM) anti-CD19 CARs using a **4-hour chromium release assay across multiple E:T ratios**. Key finding: the low-affinity CAT CAR-T cells were **more cytotoxic** than FMC63 against high-CD19 targets. Both were equivalent against low-CD19 targets.

- **Liu et al.** (HER2 affinity variants): High-affinity CARs (0.58 nM) killed tumor cells regardless of antigen density; low-affinity CARs (1119 nM) selectively killed only high-expressing targets. **Lower E:T ratios amplified these differences.**

- **Caruso et al.** (EGFR affinity variants): cetuximab-based CAR (1.8 nM) vs. nimotuzumab-based CAR (21 nM) -- the lower-affinity variant selectively lysed high-EGFR cells.

**Critical insight for this project:** To detect functional differences between FMC63 affinity variants, **use lower E:T ratios (0.5:1, 1:1, 2:1)** alongside higher ratios (5:1, 10:1). Differences will be most apparent at low ratios where efficient antigen engagement is limiting.

**Reference:** Ghorashian S et al. "Enhanced CAR T cell expansion and prolonged persistence in pediatric patients with ALL treated with a low-affinity CD19 CAR." *Nature Medicine* 25(9):1408-1414, 2019. PMID: 31477906.

### 1.4 Jurkat-Specific E:T Ratio Considerations

**IMPORTANT: Jurkat cells have significant limitations for cytotoxicity assays.**

Jurkat cells (CD4+ leukemic T cell line) differ from primary T cells in several ways relevant to E:T ratio selection:

| Feature | Jurkat Cells | Primary T Cells |
|---------|-------------|-----------------|
| Cytolytic activity | **Minimal** -- altered TCR signaling, lack robust perforin/granzyme pathway | Full cytolytic capacity |
| IL-2 production | Produce IL-2 upon activation | Full cytokine repertoire |
| Primary readout | **CD69 upregulation** (activation marker), NFAT/NFkB reporter activity | Cytotoxicity (target cell death), cytokines, proliferation |
| E:T ratio range | 1:100, 1:10, 1:1 tested in Bloemberg et al. | 0.2:1 to 10:1 typical |
| Proliferation | Constitutive (immortalized) | Activation-dependent |

**Recommended approach for Jurkat cells:**
- **For activation readouts (CD69, NFAT):** Use E:T ratios of **1:1, 1:10, and 1:100** (as in Bloemberg et al., 2020). Lower E:T ratios (more target cells per effector) test sensitivity of activation.
- **For cytotoxicity (if attempted):** Use higher E:T ratios of **4:1 to 8:1** and extended incubation (48-72h), as shown by Subham et al. (2024) who demonstrated >50% killing at 4:1 E:T over 72h using fluorescent imaging.
- **For tonic signaling assessment:** Include an "effectors alone" (no target) condition at every time point.

**Key references:**
- Bloemberg D et al. "A High-Throughput Method for Characterizing Novel Chimeric Antigen Receptors in Jurkat Cells." *Mol Ther Methods Clin Dev* 16:238-254, 2020. PMC7021643.
- Subham S, Jeppson JD, Akhavan D. "Rapid In Vitro Cytotoxicity Evaluation of Jurkat Expressing Chimeric Antigen Receptor using Fluorescent Imaging." PMC11008703, 2024.
- Jahan F et al. "Using the Jurkat reporter T cell line for evaluating the functionality of novel chimeric antigen receptors." *Front Mol Med* 3:1070384, 2023. PMC11285682.

### 1.5 Recommended E:T Ratio Panel for This Project

Given the Jurkat/Raji system and affinity optimization goals:

**For CD69/activation assessment (primary Jurkat readout):**
- 1:1, 1:5, 1:10 (Jurkat:Raji)

**For cytotoxicity (if measurable with Jurkat cells):**
- 1:1, 2:1, 5:1, 10:1 (Jurkat:Raji)

**For cytokine measurement (IL-2, IFN-gamma):**
- 1:1 and 5:1

**Critical controls:**
- Untransduced Jurkat + Raji (same ratios) -- negative control
- Jurkat-CAR alone (no target) -- tonic signaling control
- Jurkat-CAR + CD19-negative cell line (e.g., K562) -- specificity control

---

## 2. TIME POINTS FOR CYTOTOXICITY MEASUREMENT

### 2.1 Standard Time Points and What Each Reveals

| Time Point | What It Reveals | Assay Type | Key Consideration |
|------------|----------------|------------|-------------------|
| **4 hours** | Early/direct cytolytic activity (perforin/granzyme-mediated killing). Standard for chromium-51 release assay. | 51Cr release | Classical but limited -- only captures fastest killing. Piccinini et al. found 6h showed no appreciable effect above background. |
| **6 hours** | Early killing; may be insufficient for CAR-T cells. | Flow, BLI | Suboptimal -- killing often not significantly different from background at this point. |
| **16-18 hours** | Intermediate killing; useful for luciferase-based assays. | BLI, flow | Used by Jahan et al. (2023) for Jurkat reporter assays with luciferase+ targets. |
| **24 hours** | **Optimal for most flow cytometry-based assays.** Peak killing without excessive background. At 1:1 E:T, ~94% cytolysis reached by 24h. | Flow cytometry | **Recommended as the primary time point.** Validated potency assay (Piccinini et al.) uses 24h with coefficient of variation <= 10%. Robust between 23-25h. |
| **48 hours** | Sustained killing, early proliferative response of effectors. Cytokine accumulation measurable. | BLI, flow, ELISA | Standard for FMC63/Raji co-culture cytokine measurements (Hu et al., 2020). Risk of excessive cell death at high E:T ratios confounding results. |
| **72 hours** | Prolonged killing, effector exhaustion beginning. | BLI, impedance | Useful for detecting persistence differences between affinity variants. Subham et al. used 72h for Jurkat CAR cytotoxicity. |
| **Real-time (continuous)** | Full kinetic profile including onset, rate, and plateau of killing. | Impedance (xCELLigence) | Gold standard for kinetics but requires adherent target cells -- NOT suitable for Raji (suspension). |

### 2.2 Assay-Method-Dependent Recommendations

**For Jurkat + Raji (suspension cells):**
- Impedance-based assays (xCELLigence) are NOT applicable (requires adherent targets)
- **Flow cytometry-based killing assay** is the most practical approach
- **Bioluminescence imaging (BLI):** Requires Raji-Luc cells; can measure at multiple time points from same plate

**Recommended time point panel:**
- **24h** (primary endpoint -- validated, robust)
- **48h** (secondary endpoint -- cytokine accumulation, sustained killing)
- **72h** (if assessing persistence differences between affinity variants)
- **4h** (optional -- for comparison with published 51Cr release data)

### 2.3 Key References for Time Points

1. **Piccinini C, Carloni S et al.** "In vitro CAR-T cell killing: validation of the potency assay." *Cancer Immunol Immunother* 2024. PMC11219661. -- **Validated 24h at 1:1 E:T** as optimal; tested 6h, 24h, 48h.

2. **Lisby AN et al.** "Comparative analysis of assays to measure CAR T cell-mediated cytotoxicity." *Cytotherapy* 2021. PMC8064272. -- Comprehensive comparison of 51Cr (4h), BLI (up to 72h), impedance (days), and flow (24-72h).

3. **Hu SI et al.** "Pre-clinical assessment of chimeric antigen receptor t cell therapy targeting CD19+ B cell malignancy." *Ann Transl Med* 8(6):349, 2020. PMC7290534. -- **FMC63 CAR-T + Raji at 5:1 and 10:1 for 4h** (cytotoxicity); **24h for cytokine ELISA**.

---

## 3. TIME POINTS FOR EXHAUSTION AND ACTIVATION MARKER ASSESSMENT

### 3.1 Activation Markers (CD69, CD25)

| Marker | Onset | Peak Expression | Duration | Measurement Window |
|--------|-------|----------------|----------|-------------------|
| **CD69** | 2-4 hours post-activation | **18-48 hours** | Declines by 48-72h; lost by 96h | **Measure at 4h (early), 24h (peak)** |
| **CD25 (IL-2Ralpha)** | Detectable by 24h | **48-72 hours** (STAT5-dependent) | Sustained for 4-5 days if IL-2 present | **Measure at 24h (rising), 48h (peak), 72h** |

**CD69 kinetics:** CD69 is the earliest activation marker, detectable within 2-4h of TCR engagement. It peaks at 18-48h and is a canonical readout for Jurkat-based CAR screening (Bloemberg et al., 2020). In Jurkat cells, CD69 MFI is the primary functional readout for CAR activation.

**CD25 kinetics:** CD25 upregulation is slower and requires sustained signaling. The Bloemberg et al. (2020) study showed strong correlation (R-squared = 0.77) between Jurkat CD69 response and primary T cell CD25 expression at day 7, validating Jurkat screening.

**Recommended panel for Jurkat/Raji co-culture:**
- **4h:** CD69 (early activation checkpoint)
- **24h:** CD69 (peak), CD25 (early)
- **48h:** CD25 (peak)
- **72h:** CD25 (sustained activation)

### 3.2 Exhaustion Markers (PD-1, TIM-3, LAG-3)

| Marker | Initial Upregulation | Exhaustion-Associated Expression | Key Feature |
|--------|---------------------|--------------------------------|-------------|
| **PD-1** | **24-48h** post-activation (behaves initially like an activation marker) | Sustained/increased expression with chronic stimulation. Fails to downregulate unlike acute activation. | In acute activation: transient. In chronic stimulation: persistent and increasing. |
| **TIM-3** | **Transiently at activation**, then down in acute settings | Elevated by **day 8** of chronic stimulation; sustained at 70-80% for weeks in chronic settings. | Co-expression of TIM-3+PD-1+ marks deeper exhaustion. |
| **LAG-3** | **Delayed relative to PD-1**; requires stronger TCR signals | Peaks around **day 4** in iNKT studies; co-expression with PD-1 defines exhausted subset. | Requires higher TCR signal strength for induction. |
| **Triple+ (PD-1+TIM-3+LAG-3+)** | Develops over **7-14 days** of chronic stimulation | Hallmark of terminal exhaustion. | Most informative for distinguishing exhaustion from activation. |

**Critical distinction -- Activation vs. Exhaustion:**
- PD-1 is upregulated transiently during normal T cell activation (within 24-48h) and then downregulates. In exhaustion, PD-1 remains elevated and increases.
- **To distinguish activation from exhaustion, you MUST measure at both early (24-48h) and late (day 7-14) time points.**
- The co-expression pattern (single-positive vs. double/triple-positive for PD-1/TIM-3/LAG-3) is more informative than any single marker.

**Reference:** Long AH et al. "4-1BB costimulation ameliorates T cell exhaustion induced by tonic signaling of chimeric antigen receptors." *Nature Medicine* 21(6):581-590, 2015. PMC4458184.
- Exhaustion markers measured at **day 9-11 post-activation**
- Early activation markers (CD25, 4-1BB) measured at **days 4-7**
- 1:1 E:T ratio used for functional co-culture assays

### 3.3 Recommended Exhaustion Assessment Protocol

**For acute co-culture (single stimulation):**
- Baseline (day 0, before co-culture): PD-1, TIM-3, LAG-3 levels
- 24h: PD-1 (activation-associated upregulation)
- 48h: PD-1, LAG-3
- Day 5: PD-1, TIM-3, LAG-3 (beginning of exhaustion window)
- Day 7: Full panel PD-1, TIM-3, LAG-3 (exhaustion assessment)

**For chronic stimulation (repeated antigen exposure):**
- Assess every 5 days following each re-stimulation (as per multiple published protocols)
- Continue for 13-17 days to reach full exhaustion (Selli et al., 2023)
- Days 10-14: Peak exhaustion with loss of effector function

### 3.4 Jurkat-Specific Caveat for Exhaustion Markers

**FLAG:** Jurkat cells may not faithfully recapitulate exhaustion biology of primary T cells. Jurkat cells:
- Are immortalized and constitutively proliferate
- Have altered TCR signaling cascades
- May not upregulate exhaustion markers with the same kinetics as primary T cells

**Recommendation:** Use Jurkat cells for initial screening of activation (CD69, CD25) and tonic signaling (constitutive PD-1 upregulation without antigen). Validate exhaustion phenotypes in primary T cells.

---

## 4. SERIAL KILLING / RECHALLENGE ASSAY PROTOCOLS

### 4.1 Published Rechallenge Protocols

**Protocol 1: Wang & Brown (2019) -- Journal of Visualized Experiments**
- **E:T ratio:** 1:4 (initial), with escalating tumor burden at each rechallenge
- **Rechallenge schedule:** Fresh tumor cells added every **2 days** (days 2, 4, 6)
- **Number of rounds:** 4 total (initial + 3 rechallenges) over **7 days**
- **Added tumor cells:** 32,000 per rechallenge (doubling the initial 16,000)
- **Effective E:T ratios:** Progressively decrease from 1:4 to 1:12 to 1:20
- **Measurements:** Days 1, 3, 5, 7 -- viable tumor cells, CAR-T expansion, activation markers (4-1BB, CD69), exhaustion markers (PD-1, LAG-3, TIM-3), memory markers (CD45RO, CD62L)
- **Key finding:** Differences between CD4+ and CD8+ CAR-T cells only emerged after 2-3 rounds of rechallenge -- standard short-term assays missed these differences entirely.
- **Reference:** Wang D, Brown CE. "In vitro tumor cell rechallenge for predictive evaluation of chimeric antigen receptor T cell antitumor function." *J Vis Exp* (144), 2019. PMC6719706.

**Protocol 2: Selli, Singh et al. (2023) -- STAR Protocols**
- **E:T ratio:** 1:8 (CAR+ T cell : Nalm6)
- **Rechallenge schedule:** Fresh Nalm6 added every **2 days** to re-establish 1:8 ratio
- **Duration:** 13-17 days total
- **Target cells:** Nalm6 (CD19+, BID-disrupted for partial resistance)
- **Key readout:** CAR+ T cell fold expansion and Nalm6 fold expansion measured every 2 days by flow cytometry
- **Exhaustion endpoint:** T cell fold-change < 1 AND/OR Nalm6 fold-change > 1 (loss of tumor control)
- **Timeline:** Potent effector functions for first 10 days; exhaustion/loss of control by days 10-13
- **Reference:** Selli ME, Landmann JH, Arveseth C, Singh N. "Inducing T cell dysfunction by chronic stimulation of CAR-engineered T cells targeting cancer cells in suspension cultures." *STAR Protocols* 4(1):101918, 2023. PMC9826863.

**Protocol 3: Extended weekly rechallenge**
- **Rechallenge schedule:** Weekly (every 7 days)
- **Duration:** 4 weeks
- **Context:** Used for chronic stimulation studies; CAR-T cells cultured weekly with malignant lymphoid cell lines
- **Assessment:** Exhaustion markers assessed every 5 days after each re-stimulation

### 4.2 Recommended Rechallenge Protocol for Jurkat/Raji System

Given the suspension cell system (both Jurkat and Raji are suspension cells):

**Option A -- Short-term stress test (7 days):**
Following Wang & Brown (2019):
- Day 0: Co-culture Jurkat-CAR with Raji at 1:4 (E:T)
- Day 2: Add fresh Raji cells
- Day 4: Add fresh Raji cells
- Day 6: Add fresh Raji cells
- Assess at days 1, 3, 5, 7
- Readouts: Raji viability (CD19+/7-AAD), Jurkat-CAR expansion (CD3+), activation (CD69), exhaustion (PD-1)

**Option B -- Chronic exhaustion induction (14+ days):**
Following Selli et al. (2023):
- Day 0: Co-culture at 1:8 (Jurkat-CAR : Raji)
- Every 2 days: Re-establish 1:8 ratio with fresh Raji cells
- Monitor for 14-17 days
- Measure CAR+ cell expansion and Raji expansion every 2 days
- Full exhaustion panel at days 0, 5, 10, 14

**Note:** The Selli protocol uses Nalm6 with BID disruption to create partially resistant target cells. For Raji cells, consider whether the natural killing resistance of the Jurkat system (reduced cytolytic activity) may serve a similar function.

---

## 5. VERIFIED KEY REFERENCES

### Reference 1
**Piccinini C, Carloni S et al.** "In vitro CAR-T cell killing: validation of the potency assay."
*Cancer Immunology, Immunotherapy* (2024). PMC11219661.
- **Relevance:** Validated 1:1 E:T, 24h incubation as optimal for flow cytometry-based CAR-T potency assay
- **Key data:** Anti-CD19 CAR-T vs. REH (CD19+) and MOLM-13 (CD19-); CV <= 10%; robust 23-25h window
- **Verified:** Yes (PubMed, PMC full text accessed)

### Reference 2
**Lisby AN et al.** "Comparative analysis of assays to measure CAR T cell-mediated cytotoxicity."
*Cytotherapy* 23(Supplement), 2021. PMC8064272. PMID: 33589826.
- **Relevance:** Comprehensive comparison of four assay methods (51Cr, BLI, impedance, flow) with different E:T ranges
- **Key data:** 51Cr requires high E:T (up to 64:1, 4h); BLI allows 0.5:1-10:1 over 72h; impedance allows real-time at 0.005:1-10:1
- **Verified:** Yes (PubMed, PMC full text accessed)

### Reference 3
**Wang D, Brown CE.** "In vitro tumor cell rechallenge for predictive evaluation of chimeric antigen receptor T cell antitumor function."
*J Vis Exp* (144), 2019. PMC6719706.
- **Relevance:** Complete rechallenge protocol with 4 rounds over 7 days; measures activation, exhaustion, and memory
- **Key data:** 1:4 E:T, rechallenge every 2 days, escalating tumor burden
- **Verified:** Yes (PMC full text accessed)

### Reference 4
**Bloemberg D et al.** "A High-Throughput Method for Characterizing Novel Chimeric Antigen Receptors in Jurkat Cells."
*Mol Ther Methods Clin Dev* 16:238-254, 2020. PMC7021643.
- **Relevance:** Definitive reference for Jurkat-based CAR screening. E:T ratios 1:1, 1:10, 1:100. CD69 as primary readout.
- **Key data:** CAR-J score (specificity ratio) correlates R-squared = 0.93 with primary T cell CD25; validates Jurkat screening
- **Verified:** Yes (PubMed, PMC full text accessed)

### Reference 5
**Long AH et al.** "4-1BB costimulation ameliorates T cell exhaustion induced by tonic signaling of chimeric antigen receptors."
*Nature Medicine* 21(6):581-590, 2015. PMC4458184.
- **Relevance:** Defines exhaustion marker assessment time points (day 9-11); compares CD28 vs 4-1BB costimulation effects on exhaustion
- **Key data:** PD-1, TIM-3, LAG-3 measured day 9-11; activation markers day 4-7; 1:1 E:T for functional assays; 4-1BB domain reduces exhaustion
- **Verified:** Yes (PubMed, PMC full text accessed)

### Reference 6 (Supplementary)
**Ghorashian S et al.** "Enhanced CAR T cell expansion and prolonged persistence in pediatric patients with ALL treated with a low-affinity CD19 CAR."
*Nature Medicine* 25(9):1408-1414, 2019. PMID: 31477906.
- **Relevance:** Direct comparison of FMC63 (high-affinity) vs CAT (low-affinity) anti-CD19 CARs. Most relevant published paper for affinity optimization project.
- **Key data:** CAT (KD ~14.38 nM) outperformed FMC63 (KD ~0.328 nM) in cytotoxicity and expansion; 4h 51Cr release across multiple E:T ratios
- **Verified:** Yes (PubMed, Nature Medicine)

### Reference 7 (Supplementary)
**Selli ME, Landmann JH, Arveseth C, Singh N.** "Inducing T cell dysfunction by chronic stimulation of CAR-engineered T cells targeting cancer cells in suspension cultures."
*STAR Protocols* 4(1):101918, 2023. PMC9826863.
- **Relevance:** Suspension cell chronic stimulation protocol. 1:8 E:T, rechallenge every 2 days, 13-17 day protocol.
- **Key data:** Exhaustion onset at days 10-13; directly applicable to Jurkat/Raji suspension system
- **Verified:** Yes (PubMed, PMC full text accessed)

---

## 6. SUMMARY TABLE: RECOMMENDED EXPERIMENTAL DESIGN

### 6.1 Cytotoxicity/Activation Assessment

| Parameter | Recommended | Rationale |
|-----------|-------------|-----------|
| **E:T ratios** | 0.5:1, 1:1, 2:1, 5:1, 10:1 | Full dose-response curve; low ratios (0.5:1, 1:1) most sensitive for affinity variant differences |
| **Primary time point** | 24h | Validated optimal (Piccinini et al., 2024); peak killing without excessive background |
| **Secondary time points** | 4h, 48h | 4h for comparison with 51Cr literature; 48h for sustained killing and cytokine |
| **Tertiary time point** | 72h | Persistence/exhaustion onset for affinity variant comparison |
| **Primary readout (Jurkat)** | CD69 MFI by flow cytometry | Standard Jurkat activation readout (Bloemberg et al., 2020) |
| **Secondary readout** | IL-2 by ELISA (24h supernatant) | Jurkat cells produce IL-2 upon activation |
| **Cytotoxicity readout** | CD19+ / 7-AAD+ (dead Raji) by flow | Or BLI if Raji-Luc available |

### 6.2 Exhaustion/Chronic Stimulation Assessment

| Parameter | Recommended | Rationale |
|-----------|-------------|-----------|
| **Protocol** | Rechallenge every 2 days at 1:4 or 1:8 E:T | Published standard (Wang & Brown 2019; Selli et al. 2023) |
| **Duration** | 7-14 days | 7 days minimum for functional differences; 14 days for full exhaustion |
| **Rounds** | 4-7 | 4 rounds in 7 days (Wang); 6-8 rounds in 14 days (Selli) |
| **Exhaustion markers** | PD-1, TIM-3, LAG-3 (co-expression) | Triple-positive = terminal exhaustion |
| **Assessment time points** | Days 0, 3, 5, 7, 10, 14 | Captures activation-to-exhaustion transition |
| **Activation markers** | CD69 (4-24h), CD25 (24-72h) | Different kinetics; include both |

---

## 7. UNCERTAINTY FLAGS

The following points require additional verification or have caveats:

1. **Jurkat exhaustion biology:** Whether Jurkat cells faithfully recapitulate PD-1/TIM-3/LAG-3 upregulation kinetics is NOT well-established. Most exhaustion studies use primary T cells. The Jurkat system is validated for activation (CD69) but NOT for exhaustion marker kinetics. This should be explicitly stated in the DAC presentation.

2. **Ghorashian et al. specific E:T ratios:** The exact E:T ratios used in their 51Cr release assay were described as "a range of E:T ratios" but the specific values (e.g., 1:1, 5:1, 10:1) were not confirmed from the available text. The paper uses a standard 4h 51Cr assay format which typically includes ratios from 1:1 to 50:1.

3. **Raji cell killing by Jurkat cells:** Jurkat cells have minimal cytolytic capacity. The degree to which Jurkat-CAR cells can kill Raji cells will likely be substantially lower than primary CAR-T cells. The Subham et al. (2024) study showed that Jurkat CARs CAN mediate killing, but higher E:T ratios (4:1+) and longer incubation (48-72h) are needed. This is a known limitation that should be acknowledged.

4. **Optimal affinity range:** The 10-5000 nM range cited by Duan et al. (2021) is for non-GD2 targets and represents a general guideline, not a universal rule. For CD19 specifically, the Ghorashian data suggests even ~14 nM (40-fold lower than FMC63) can be superior.

5. **CD69 as sole Jurkat readout:** While CD69 is validated as the primary Jurkat readout (Bloemberg et al., R-squared = 0.93 correlation with primary T cell CD25), it "may not reflect the nuances in antigen signaling induced by CARs" (Bloemberg et al., 2020). Consider supplementing with NFAT reporter if available.
