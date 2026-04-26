# Controls, Statistical Design, and Quality Control for CAR-T Functional Screening

## DAC Meeting Reference Document
### Manpreet Kour | PI: Dr. Kausik Chakraborty | Co-PI: Dr. Ankesh Kumar Jaiswal
### CSIR-IGIB | AcSIR Reg. 10BB25J02028

---

## 1. Essential Negative Controls

### 1.1 Summary Table

| Control | Cell Setup | Purpose |
|---------|-----------|---------|
| Un-transduced Jurkat + Raji | Jurkat (no CAR) + Raji | Non-specific activation baseline |
| Mock-transduced Jurkat + Raji | Empty vector Jurkat + Raji | Transduction process effect |
| CAR-Jurkat + K562 (CD19-neg) | CAR-Jurkat + K562 | Antigen specificity control |
| CAR-Jurkat alone (no target) | CAR-Jurkat only | Tonic signaling assessment |
| Raji alone | Raji only | Spontaneous target death |
| Irrelevant-scFv CAR + Raji | e.g., anti-HER2 CAR + Raji | Non-specific CAR-mediated effect |

### 1.2 Detailed Rationale

**Un-transduced Jurkat + Raji:** Any activation (CD69+, cytokine secretion) seen here reflects non-CAR-mediated signaling and sets the assay baseline. Used in Bloemberg et al. (2020, PMC7021643) and Chmielewski et al. (2023, PMC11285682).

**Mock-transduced Jurkat (empty vector) + Raji:** Controls for the effect of lentiviral transduction itself, which can alter cell behavior independent of the CAR transgene. Chmielewski et al. used "empty LV (mock)" as a distinct negative control.

**CAR-Jurkat + K562:** K562 cells (ATCC CCL-243) are the standard CD19-negative control. They do not express CD19, CD20, or CD22. Any killing of K562 by anti-CD19 CAR-T cells indicates non-specific toxicity. Confirmed: Hu et al. (*Ann Transl Med* 2020, PMC7290534); Bloemberg et al. (2020).

**CAR-Jurkat alone (no target):** Critical for tonic signaling assessment. Antigen-independent signaling from CARs can be detected as elevated baseline CD69 expression, PD-1 upregulation, or basal cytokine production. Chmielewski et al. calculate a "tonic signaling index" = CD69 MFI / GFP MFI in the absence of target cells.

**Raji alone:** Used to calculate spontaneous target cell death, which is subtracted from experimental conditions: `% Specific Killing = 100 x (1 - RLU_sample / RLU_Raji-alone)`. Standard across all killing assay protocols (Guedan et al., *Sci Transl Med* 2023, PMC10228544).

**Irrelevant-scFv CAR + Raji:** Tests whether any CAR surface expression causes non-specific effects against Raji. Bloemberg et al. tested anti-HER2 CAR against CD19+ Nalm6 to confirm no cross-reactivity.

### 1.3 Signaling-Dead CAR Control (Optional but Recommended)

Truncated EGFR (EGFRt) — lacks the intracellular kinase domain and cannot transmit signals. Originally developed by the Jensen/Riddell group (US Patent US8802374B2). Controls for effects of surface protein expression per se.

---

## 2. Essential Positive Controls

### 2.1 Wild-Type FMC63 CAR (Primary Benchmark)

Every experiment must include WT FMC63 CAR-Jurkat + Raji as the reference against which all affinity variants are compared. Guedan et al. (PMC10228544) used WT FMC63 (KD approximately 2-6 nM by SPR with properly folded monomeric CD19) as the benchmark.

### 2.2 Published FMC63 Affinity Variants as Reference Standards

**Critically relevant to this project:** Guedan et al. (2023) published data on FMC63 variants at the EXACT residues Manpreet is targeting:

| Variant | Mutation | KD (SPR) | Functional Consequence | Reference |
|---------|----------|----------|----------------------|-----------|
| WT FMC63 | None | 2-6 nM (monomeric CD19) | Benchmark cytotoxicity | Guedan et al., 2023 |
| FMC63-Y70A | Tyr70 -> Ala | 275.3 nM (61-fold weaker) | Reduced but detectable function | Guedan et al., 2023 |
| FMC63-Y261A | Tyr261 -> Ala | 682.5 nM (152-fold weaker) | Substantially reduced function | Guedan et al., 2023 |
| FMC63-Y260A | Tyr260 -> Ala | No detectable SPR binding | Modest cytolytic activity at high CD19 density (~27,000 copies/cell); avidity-driven | Guedan et al., 2023 |

**Implication:** Y260A and Y261A mutants are directly at Manpreet's target residues. These published constructs could serve as internal reference standards, and the published data validates the choice of these residues for mutagenesis.

### 2.3 Stimulation Positive Controls

| Control | Concentrations | Purpose |
|---------|---------------|---------|
| PMA + Ionomycin | PMA 10-20 ng/mL + Ionomycin 1 ug/mL | Maximum activation (bypasses CAR/TCR signaling). Confirms detection system works. |
| Anti-CD3/CD28 beads | 2:1 mass ratio (CD3:CD28 antibody) | Physiological-route positive control via TCR signaling |

---

## 3. Flow Cytometry Controls

### 3.1 FMO Controls (Recommended) vs. Isotype Controls

**Current consensus strongly favors FMO (Fluorescence Minus One) controls over isotype controls for gating decisions.**

| Feature | FMO Controls | Isotype Controls |
|---------|-------------|-----------------|
| What they measure | Fluorescence spread from all OTHER channels into the channel of interest | Non-specific antibody binding |
| Account for spectral spillover? | YES | NO |
| Recommended for gating? | YES — the standard | NO — explicitly NOT recommended for gating (Abcam, Bio-Rad, Maecker & Trotter 2006) |
| When to use isotypes | Assessing Fc receptor blocking adequacy | Not for gate-setting |

**Recommendation:** Use FMO controls for setting gates on CD69, CD107a, PD-1, TIM-3, LAG-3, CAR detection, and all continuous markers. Include one isotype control to document Fc blocking sufficiency.

**Reference:** Maecker HT, Trotter J. "Flow cytometry controls, instrument setup, and the determination of positivity." *Cytometry A* 69(9):1037-1042, 2006.

### 3.2 Compensation Controls

- Single-stained compensation beads (e.g., BD CompBeads, UltraComp eBeads from Invitrogen)
- One tube per fluorochrome in the panel
- Must use the SAME fluorochrome-conjugated antibody (or beads of similar brightness)
- Run BEFORE experimental samples; calculate compensation matrix in software (FlowJo, FACSDiva)

---

## 4. Statistical Design

### 4.1 Biological and Technical Replicates

| Replicate Type | Minimum | Standard | Notes |
|---------------|---------|----------|-------|
| Biological replicates | n = 3 | n = 3 independent transductions | Each from separate viral prep + transduction. Provides the "n" for statistical tests. |
| Technical replicates | 2-3 per condition | Triplicate wells | Averaged before statistical analysis. Accounts for pipetting variability. |
| Primary T cell donors (future) | n = 4 | n = 4 separate donors | Bloemberg et al. (2020) used 4 donors. |
| In vivo mice (future) | n = 5 per group | n = 5 per group | Bloemberg et al. (2020) |

### 4.2 Statistical Tests

**For comparing multiple CAR variants to WT FMC63:**

| Test | When to Use | Software |
|------|------------|---------|
| One-way ANOVA + **Dunnett's post-hoc** | Comparing multiple variants to one control (WT) | GraphPad Prism, R |
| One-way ANOVA + Tukey's post-hoc | All pairwise comparisons (if needed) | GraphPad Prism, R |
| Two-way ANOVA | Testing construct AND E:T ratio effects simultaneously | GraphPad Prism, R |
| Two-tailed unpaired t-test | Single variant vs. WT comparison | Standard |

**Why Dunnett's is preferred over Tukey's:** For this experimental design, the primary comparison is each variant vs. WT (many-to-one comparison), not all variants against each other (all-pairwise). Dunnett's test is specifically designed for many-to-one comparisons and provides MORE statistical power than Tukey's for this scenario, while correctly controlling the familywise error rate.

### 4.3 Dunnett's Optimal Allocation Rule

To maximize power with Dunnett's test, allocate MORE observations to the WT control group:

```
Optimal ratio: n_control / n_treatment = sqrt(k)
where k = number of treatment groups (variants)
```

| Number of Variants | Optimal WT:Variant Ratio | Practical Recommendation |
|-------------------|-------------------------|--------------------------|
| 5 | sqrt(5) = 2.2x | WT: n=6, each variant: n=3 |
| 10 | sqrt(10) = 3.2x | WT: n=9, each variant: n=3 |
| 20 | sqrt(20) = 4.5x | WT: n=9-12, each variant: n=3 |

**Reference:** Penn State STAT 503 — "The Optimum Allocation for the Dunnett Test"

### 4.4 Multiple Comparison Correction

- **Dunnett's test** inherently controls familywise error rate (no additional correction needed for variant-vs-WT comparisons)
- **For additional analyses** (e.g., correlating affinity with function): Apply Bonferroni or Benjamini-Hochberg FDR correction
- **For exploratory analyses** with many markers: Consider FDR (Benjamini-Hochberg) rather than stringent Bonferroni

### 4.5 Normalizing for CAR Expression Differences

**This is critical.** Different mutant CARs may express at different levels on the cell surface. If variant A kills 50% more than variant B but also expresses 50% more CAR, the difference may be expression-driven, not affinity-driven.

**Methods (ranked by rigor):**

1. **FACS sort for matched CAR expression** (most rigorous): Sort all variants to equivalent MFI of CAR surface expression before functional assay. Low throughput but eliminates expression as a variable.

2. **Gate on matched MFI populations:** During analysis, gate on cells within the same CAR MFI window across all variants. Requires sufficient events in the matched gate.

3. **ANCOVA with CAR MFI as covariate:** Include CAR expression level as a covariate in statistical analysis. Adjusts for expression differences statistically.

4. **Report and normalize:** At minimum, report CAR MFI for all variants. Calculate normalized functional readout = function / CAR MFI (or per CAR molecule).

5. **Bicistronic vector with reporter:** Use a T2A/P2A-linked reporter (GFP, LNGFR) to monitor expression. Gate on GFP+ population for functional analysis. Guedan et al. used LNGFR; Bloemberg et al. used GFP.

---

## 5. NNK Library Screening Strategy

### 5.1 NNK Codon Coverage

NNK (N = any nucleotide; K = G or T) encodes 32 codons covering all 20 amino acids with one stop codon (TAG, 3.1% frequency).

**Amino acid redundancy in NNK:**
- 3 codons: Leu, Arg, Ser, Val
- 2 codons: Ala, Gly, Pro, Thr
- 1 codon: All others (Asp, Cys, Glu, Phe, His, Ile, Lys, Met, Asn, Gln, Trp, Tyr)

### 5.2 Screening Coverage Requirements

| Position Strategy | Codons | Clones for 95% Coverage | Clones for 99% Coverage |
|------------------|--------|------------------------|------------------------|
| Single position (e.g., Tyr260 only) | 32 | ~94-98 clones | ~148 clones |
| Two positions simultaneously | 32^2 = 1,024 | ~3,144 clones | ~4,840 clones |
| Three positions simultaneously (Y260 + Y261 + S214) | 32^3 = 32,768 | ~98,164 clones | IMPRACTICAL |

**Reference:** Pines et al., "Highly efficient libraries design for saturation mutagenesis." *Synth Biol* 2022, PMC9205323.

### 5.3 Recommended Screening Strategy

**Phase 1: Single-position saturation mutagenesis (TRACTABLE)**
- Mutate one position at a time: Tyr260 only, Tyr261 only, Ser214 only
- Screen ~94-100 clones per position = ~300 clones total
- Use CD69 activation assay in Jurkat/Raji (high throughput, 96-well format)
- Identify the amino acid at each position that gives desired phenotype

**Phase 2: Focused combinatorial library**
- Take top 3-5 amino acids at each position from Phase 1
- Create focused combinatorial library: 3x3x3 = 27 to 5x5x5 = 125 combinations
- Full functional characterization (cytotoxicity, exhaustion, memory, rechallenge)

**Phase 3: Kinetic characterization**
- Express and purify scFv from top functional hits
- SPR/BLI measurement of KD, kon, koff
- Correlate kinetics with function

### 5.4 Computational Pre-Filtering (Optional)

Before wet-lab screening, computational approaches can prioritize mutations:
- **Rosetta or FoldX:** Predict binding energy changes (ddG) for all 20 amino acids at each position
- **Molecular dynamics:** Simulate mutant FMC63-CD19 complexes
- **Structure-based design:** Use PDB 7URV to identify which substitutions maintain vs. disrupt key contacts
- This reduces the number of clones requiring functional characterization

---

## 6. Quality Control Metrics

### 6.1 Transduction Efficiency

| Parameter | Minimum | Target | Method |
|-----------|---------|--------|--------|
| % CAR+ cells (Jurkat) | >20% | >50% | Flow cytometry (anti-FMC63 idiotype) |
| Clinical products (FDA guidance) | N/A (research phase) | >70% viable CD3+ | FDA CBER guidance |
| Electroporation efficiency | >50% | >85% | GFP reporter or CAR staining |

**Reference:** FDA CBER, "Considerations for the Development of Chimeric Antigen Receptor (CAR) T Cell Products" (fda.gov/media/156896/download)

### 6.2 CAR Surface Expression Verification

All mutant CARs must be confirmed for surface expression BEFORE functional assays:
- Mutants that fail to express on the surface likely have folding/trafficking defects
- Detection: Anti-FMC63 idiotype antibody (Miltenyi clone REA1297) or recombinant CD19-Fc binding
- Report MFI for each variant; confirm "similar expression levels" or normalize for differences

### 6.3 Cell Viability Thresholds

| Parameter | Threshold | Reference |
|-----------|-----------|-----------|
| Minimum viability at assay setup | >70% | FDA CBER guidance |
| Clinical release criterion | >=80% | Commercial CAR-T products |
| Discard condition | Viability <70% | Standard |

### 6.4 Mycoplasma Testing

Regular mycoplasma contamination testing of all cell lines (Jurkat, Raji, K562) is essential. Contamination can alter cell surface marker expression and functional responses.

---

## 7. Verified References

1. **Bloemberg D et al.** "A High-Throughput Method for Characterizing Novel Chimeric Antigen Receptors in Jurkat Cells." *Mol Ther Methods Clin Dev* 16:238-254, 2020. PMC7021643.

2. **Chmielewski PJ et al.** "Using the Jurkat reporter T cell line for evaluating the functionality of novel chimeric antigen receptors." *Front Mol Med* 3:1070384, 2023. PMC11285682.

3. **Guedan S et al.** "CD19 CAR antigen engagement mechanisms and affinity tuning." *Sci Transl Med* 2023. PMC10228544.

4. **Pines G et al.** "Highly efficient libraries design for saturation mutagenesis." *Synth Biol* 2022. PMC9205323.

5. **Hu SI et al.** "Pre-clinical assessment of chimeric antigen receptor T cell therapy targeting CD19+ B cell malignancy." *Ann Transl Med* 8(6):349, 2020. PMC7290534.

6. **Wang X et al.** "CAR T cell viability release testing and clinical outcomes." *Bone Marrow Transplant* 2019. PMC6872962.

7. **FDA CBER.** "Considerations for the Development of Chimeric Antigen Receptor (CAR) T Cell Products." fda.gov/media/156896/download.

8. **Maecker HT, Trotter J.** "Flow cytometry controls, instrument setup, and the determination of positivity." *Cytometry A* 69(9):1037-1042, 2006.

---

*All citations verified via PubMed/PMC and web searches. Date compiled: 2026-04-27.*
