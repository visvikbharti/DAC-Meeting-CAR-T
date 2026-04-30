# Experimental Design — Expert Review and Confounder Audit

## For Manpreet Kour's PhD Thesis Plan
### Anti-CD19 CAR-T Affinity Optimization (FMC63 scFv variant library)
### CSIR-IGIB | PI: Dr. Kausik Chakraborty
### Date: 2026-05-01

---

## 0. Citation discipline statement

Every PMID below was directly verified against PubMed during preparation of this document. Where I could not verify, the entry is explicitly tagged **[needs primary verification]** rather than guessed. Three citations carried over from earlier sessions are wrong and are corrected in §8 — the most consequential is that the cryo-EM PDB 7URV / *Sci Immunol* 2023 paper has first author **Changhao He**, not "Singh." This needs to be corrected in 16 repo documents and the slide deck before any DAC presentation.

---

## 1. Proposed experimental design (as understood)

```
                  ┌────────────────────────────────────────────────────────┐
                  │   FMC63 scFv NNK saturation library                    │
                  │   Positions: S214, Trp212 (primary, novel)             │
                  │              Y260, Y261 (secondary, beyond Singh Ala)  │
                  │   ~94 codons × 4 positions = ~376 single-position vars │
                  └────────────────────────────────────────────────────────┘
                                            │
                          ┌─────────────────┴────────────────────┐
                          │                                       │
              ┌───────────▼───────────┐               ┌──────────▼─────────┐
              │   IN VIVO ARM         │               │   IN VITRO ARM     │
              │ "Humanized" mouse +   │               │ NALM-6 with graded │
              │ NALM-6-luciferase     │               │ CD19 expression    │
              └───────────┬───────────┘               └──────────┬─────────┘
                          │                                       │
                          ▼                                       ▼
              Sample T cells day 1, 2,                Co-culture with low/med/high
              until first deaths (1° pressure)         CD19 NALM-6 → identify variants
              21-day rest in survivors                 differing from WT
              Rechallenge with NALM-6                          │
              Sample day 1, 2, 4 post-rechallenge              │
              Sacrifice → spleen / LN / BM                     │
              Sort memory T cells → bulk NGS                   │
                          │                                    │
                          └─────────────────┬──────────────────┘
                                            │
                                            ▼
                          ┌─────────────────────────────────────┐
                          │  BIOPHYSICS ARM (top hits only)     │
                          │  scFv in Expi293F + CD19 in HEK293S │
                          │  SPR + 2D micropipette adhesion freq│
                          │  KD, kon, koff, dwell time          │
                          └─────────────────────────────────────┘
```

**Bottom line up front:** the design is ambitious and contains several novel and defensible elements (S214/Trp212 are unstudied; pooled in vivo scFv variant screen has no clear published precedent; 2D kinetics for any CAR is novel). However, **five issues are first-order and must be addressed before the DAC presentation**:

1. **Citation correction** — the recurring "Singh 2023" attribution is wrong (first author is He). 16 documents and the slide deck need updating.
2. **Sampling-timing clarity** — day 1, 2, 4 is appropriate for **activation/exhaustion kinetics** (CD69, CD25, PD-1, TIM-3, LAG-3, TOX); the **memory pool readout comes from terminal sacrifice** (end of 21-d rest, and/or post-rechallenge). Do NOT sort "memory subsets" at day 1-4 post-rechallenge — those are recall effectors, not memory.
3. **"Humanized mouse" terminology** — for adoptive CAR-T transfer to NALM-6, a PBMC- or HSC-humanized mouse is the wrong model (xeno-GvHD masks readout); the right model is plain NSG (or NSG-MHC-DKO for rest periods >4 wk).
4. **Pre-injection library NGS is mandatory** — without sequencing the input library, no enrichment ratio is interpretable. The plan does not currently mention this.
5. **HEK293S vs HEK293F** for CD19 production — HEK293S in the field means GnTI⁻ (high-mannose only); for functional kinetics matching in vivo CD19 glycosylation, Expi293F or HEK293-6E is correct. Confirm what was meant.

The remainder of this document goes through each arm in detail with verified confounders, mitigations, and citations.

---

## 2. In vivo arm — humanized mouse + NALM-6 + pooled CAR-T library

### 2.1 "Humanized mouse" terminology — clarify before DAC

The phrase "humanized mouse" is being used loosely. It conventionally refers to mice carrying a human haematolymphoid system (PBMC-, HSC-, or BLT-engrafted). For adoptive transfer of human CAR-T cells against a human B-ALL line (NALM-6), full immune reconstitution is **not required** and is usually counterproductive — the additional human immune compartments introduce confounders.

| Strain | Genotype | Use case | Suitability for this design | Citation |
|---|---|---|---|---|
| **NSG** | NOD.Cg-*Prkdc*^scid^ *Il2rg*^tm1Wjl^/SzJ | Standard adoptive CAR-T xenograft | **Recommended** for short windows (≤21 d rest) | Shultz et al. 2012 *Nat Rev Immunol* PMID **23059428** |
| **NSG-MHC-DKO** | NSG + B2M⁻/⁻ + IA/IE⁻/⁻ | Long-window CAR-T xenograft | **Recommended** if rest extends >4 wk; xeno-GvHD substantially delayed | Brehm et al. 2019 *FASEB J* PMID **30383447** |
| **NSG-SGM3** | NSG + tg human SCF, GM-CSF, IL-3 | HSC-humanized myeloid studies | Not needed; predisposes to mast cell/HLH pathology in HSC-engrafted | Wunderlich et al. 2018 *PLoS One* PMID **30586420** |
| **PBMC-humanized hu-PBL-NSG** | NSG + IV PBMC | Human T cell biology | **Inadequate** — xeno-GvHD onset at ~28 d will mask memory readout | King et al. 2009 *Clin Exp Immunol* PMID **19426570** |
| **BLT** | NSG/NOG + human fetal thymus + HSC | HLA-restricted T cell biology | Not needed; T cells educated on autologous HLA, mismatched to NALM-6 | Lan et al. 2006 *Blood* PMID **16778179** |

**Recommendation**: Use **NSG** (or **NSG-MHC-DKO** if any rest period exceeds 4 weeks) for adoptive CAR-T transfer to NALM-6-luc. State explicitly in the methods that "humanized mouse" in this thesis means "human-CAR-T-engrafted immunodeficient mouse" — not a fully reconstituted human immune system.

### 2.2 NALM-6 model — verified parameters

| Parameter | Value | Source |
|---|---|---|
| Origin | Pre-B ALL, 19-yr-old male, Caucasian | Cellosaurus CVCL_0092; DSMZ ACC-128 |
| Phenotype | CD3-, CD10+, CD19+, HLA-DR+, cyIgM+, sIgM- | DSMZ ACC-128 |
| HLA class I | A*01:01, A*02:01; B*08:01, B*15:01; C*04:01, C*07:01 | DSMZ four-digit typing |
| HLA class II | DRB1*03:01, DRB1*07:01 | DSMZ |
| Standard IV dose (NSG xenograft) | 0.5–1.0 × 10⁶ cells, tail vein | Brentjens et al. 2007 *Clin Cancer Res* PMID **17855649**; Milone et al. 2009 *Mol Ther* PMID **19384291** |
| Median survival untreated NSG | ~21–25 d at 1 × 10⁶ dose | (preclinical convention; multiple sources) |
| Disease distribution | Liver/BM (d 7–14) → spleen (wk 1–2) → CNS (late) | (multiple) |
| Standard CAR-T dose | 2–5 × 10⁶ CAR+ cells, IV, day 3–7 post-tumor | Brentjens 2007 PMID 17855649; Milone 2009 PMID 19384291 |
| Luciferase | Firefly luciferase (Fluc) standard; D-luciferin 150 mg/kg IP | Imanis NALM6-Fluc CVCL_RA36 |
| Antigen escape (clinical) | 10–20% of CART19 relapses are CD19-loss | Sotillo et al. 2015 *Cancer Discov* PMID **26583447**; Orlando et al. 2018 *Nat Med* PMID **30275570** |

**Important historical clarification**: Brentjens 2003 (PMID 12579196) used NALM-6 in **SCID-Beige**, not NSG. The transition to NSG/NOG xenografts is in Brentjens 2007 (PMID 17855649) and Milone 2009 (PMID 19384291). Cite the specific paper for the dose/strain you actually use.

### 2.3 Pooled in vivo scFv variant screening — does precedent exist?

This is the most consequential question for whether the design is publishable as stated. **Verified precedent for pooled CAR-T variant screens**:

| Paper | Year | Library type | Library size | Pooled phase | In vivo? | PMID |
|---|---|---|---|---|---|---|
| Daniels et al. *Science* | 2022 | CAR signaling motif library, ML-driven | ~2300 designs | Pooled in vitro on NALM-6 | Validation only | **36480602** |
| Goodman / Roybal *Sci Transl Med* ("CAR Pooling") | 2022 | CAR signaling domains | 40 | Mostly in vitro | Per-construct validation | **36350984** |
| Castellanos-Rueda *Nat Commun* (speedingCARs) | 2022 | Signaling domain shuffling + scRNA-seq | 180 | In vitro | – | **36323661** |
| Rios *Mol Ther* | 2023 | Barcoded CAR domain combinations (hinge/costim/activation) | 360 | In vitro | Per-construct validation | **37705245** |
| LaFleur *Nat Commun* (CHIME) | 2019 | CRISPR knockout (NOT CAR variants) | ~900 genes | Pooled | Yes (in vivo CRISPR) | **30971695** |

**Finding**: I found **no published precedent for a fully in vivo pooled scFv variant screen at the binding interface in a single mouse with NGS readout.** All published CAR pooled screens run the pooled phase **in vitro** with in vivo work limited to per-construct validation. This is either a genuine novelty opportunity or a sign that nobody has yet solved the technical bottlenecks. The DAC will probably ask both interpretations.

**The most defensible alternative** (fallback if pooled in vivo is too risky for a thesis): pooled in vitro screen against tunable-CD19 NALM-6 (Daniels/Rios style) + arrayed in vivo validation of the top 5–10 hits. This matches the published precedent and is far easier to defend.

### 2.4 In vivo arm — comprehensive confounders

| # | Confounder | Mechanism | Magnitude | Mitigation | Citation |
|---|---|---|---|---|---|
| 1 | Library bottleneck at engraftment | Only 1–10% of injected human T cells engraft long-term in NSG → effective per-variant founder reduced 10–100× | At 5 × 10⁶ CAR-T input × 5% engraftment ÷ 376 variants ≈ 660 founders/variant/mouse | Reduce library size; ≥10 mice per arm; high-redundancy barcoding | Wunderlich 2018 PMID **30586420**; Alcantar-Orozco 2013 PMID **23931270** |
| 2 | Day 1, 2, 4 sampling — appropriate for activation/exhaustion kinetics, NOT for memory phenotyping | Day 1, 2, 4 is the standard window for activation (CD69 24 h, CD25 48 h) and early exhaustion onset (PD-1, TIM-3, LAG-3, TOX). Memory phenotyping should come from terminal sacrifice (post-rest or post-rechallenge), NOT from these early timepoints. | Memory contraction 30–60 d in immunocompetent; ~21–28 d in NSG before xeno effects | **Use day 1, 2, 4 for activation/exhaustion kinetic profiling** (see §3a). **Use end-of-rest sacrifice (day 21+) for memory phenotype + variant NGS readout.** Do not sort "memory subsets" at day 1-4 post-rechallenge — those are recall effectors. | Long et al. 2015 *Nat Med* PMID **25939063**; Gattinoni & Restifo 2011 *Nat Med* PMID **21926977**; Xu et al. 2014 *Blood* PMID **24782509** |
| 3 | Survival selection bias (effectors over memory) | Surviving mice were rescued by aggressive effector CARs; memory-prone (less acute) variants may be lost with their hosts | Conceptual but biologically intuitive | Multi-arm design: Arm A sacrificed at day 21 for memory pool; Arm B rechallenged for recall functional test | Gattinoni 2017 *Nat Med* PMID **28060797**; Krishna 2020 *Science* PMID **33335196** |
| 4 | Antigen escape (CD19-low/null) | Selection pressure → CD19 splice variants and point mutations emerge | 10–20% of clinical CART19 relapses | Confirm CD19 surface on residual tumor at each sample; CD19-KO NALM-6 control arm; sequence tumor CD19 if rechallenge fails | Sotillo 2015 PMID **26583447**; Orlando 2018 PMID **30275570** |
| 5 | Xeno-GvHD masking memory phenotype | Human T cells attack mouse MHC → non-specific activation/memory differentiation | xeno-GvHD onset ~4 wk in NSG-PBMC; minimal in NSG-MHC-DKO | Use NSG-MHC-DKO for rest >4 wk; baseline non-tumor + CAR-T-only control mice | Brehm 2019 PMID **30383447**; King 2009 PMID **19426570** |
| 6 | Mouse-to-mouse variant composition drift | Stochastic founder effect → each mouse samples library differently | CV per variant 50–200% at low founders | n ≥ 10 mice; pre-injection input library reference; spike-in synthetic barcodes | LaFleur 2019 PMID **30971695** |
| 7 | Multiple lentiviral integrations per cell | At MOI > 0.5 some cells carry ≥2 variants → mixed phenotypes | ~30% of transduced cells at MOI 5 carry ≥2 copies | MOI ≤ 0.3; sort low-MFI singlets; qPCR vector copy number on representative sample | Milone 2009 PMID **19384291** |
| 8 | Variant-dependent CAR surface expression | Some scFv mutations destabilize folding → lower surface CAR independent of binding | Up to 10× variation across variants | Sort by surface CAR (CD19-Fc tetramer or anti-idiotype) before NGS; report DNA-level vs protein-level enrichment separately | (general antibody folding literature) |
| 9 | Lentiviral integration site bias | Same variant at different integration sites → 10–100× different surface expression | Standard for lentivirus | Site-directed integration via TRAC knock-in (CRISPR/AAV6 HDR) eliminates this | Eyquem 2017 *Nature* PMID **28225754**; Roth 2018 *Nature* PMID **30022017** |
| 10 | Trafficking differences between variants | High-affinity variants may home to BM faster, masking intrinsic memory bias | Documented for affinity-tuned CARs in solid-tumor models | Sample blood/spleen/LN/BM at each timepoint; trafficking-corrected enrichment | He 2023 PMID **36867678** |
| 11 | Rechallenge dose mismatch | Too low → underestimates memory; too high → overwhelms competent memory | Standard rechallenge ≥ initial dose | Pilot dose-titration in CAR-T-naïve survivors; lock dose | Brentjens 2007 PMID 17855649 |
| 12 | 21-day rest may be too short | In NSG, memory contraction kinetics are compressed but poorly characterized | xeno-GvHD ≤4 wk in NSG; 75–125 d possible in NSG-MHC-DKO | Extend to 28–35 d; use NSG-MHC-DKO; verify Tscm/Tcm markers (CCR7+, CD62L+, CD45RA+, CD27+, CD95+) at multiple timepoints | Brehm 2019 PMID **30383447**; Gattinoni 2011 PMID **21926977** |
| 13 | Firefly luciferase immunogenicity | In immunocompetent or HSC-humanized mice, Fluc is a CD8 immunogen; non-issue in NSG | – | Use NSG (no T cells); if shifting to humanized, switch to Renilla or NanoLuc | Day et al. 2014 *Mol Ther* PMID **24449212** |
| 14 | Conditioning (lymphodepletion) | NSG has no host T cells, so Cy/Flu conditioning is irrelevant; sub-lethal irradiation can shift NALM-6 distribution | Modest | Match conditioning across all arms; report explicitly | Brehm 2019 PMID **30383447** |

### 2.5 In vivo arm — recommendations (prioritized)

**Tier 1 (must-do):**
1. Use **NSG** (or **NSG-MHC-DKO** for any rest >4 wk). Drop "humanized mouse" terminology unless PBMC/HSC engraftment is intentional.
2. **Move memory phenotyping timepoints** to days 14, 21, 28 of primary cycle and day 4–7 (effector recall) and 14, 21 post-rechallenge, but always pair with a separate **end-of-rest sacrifice cohort** that is the primary memory-pool readout.
3. **n ≥ 10 mice per arm**, pre-defined mixed-effects statistical model.
4. **Pre-inject library NGS** + post-expansion infusion-product NGS + tissue harvest NGS — three reference timepoints minimum.
5. **MOI ≤ 0.3** at lentiviral transduction; sort CAR-low MFI singlets; qPCR vector copy number on a sample.
6. **Single-clone-cloned, low-passage NALM-6-Fluc** working stock; refresh every 5 passages and re-validate CD19 surface by FACS.
7. **CD19-KO NALM-6 control arm** to dissect antigen-escape vs CAR-engagement contributions.

**Tier 2 (strongly recommended):**
8. Consider **TRAC knock-in** (CRISPR + AAV6 HDR) to eliminate integration-site confound (Eyquem 2017, Roth 2018).
9. Sample blood + spleen + bone marrow + lymph node at each tissue timepoint.
10. Run a parallel **in vitro repeat-stim arm** (NALM-6 antigen restim ×4 cycles) as in vitro proxy for in vivo memory pressure; compare variant rankings.

**Tier 3 (defensive):**
11. **Pilot 8 known-good and known-bad CAR variants** (FMC63 WT + Y260A from He et al. + a few others) through the entire workflow before running the full library.
12. **Arrayed (one-mouse-per-construct) validation** for top hits identified from pooled screen — required for any candidate destined for further development.

**Tier 4 (alternative if pooled in vivo is too risky):**
13. **Pooled in vitro + arrayed in vivo validation** — matches all published precedent (Daniels 2022, Rios 2023) and is the safest scope-management option for a thesis.

---

## 3. Memory phenotyping + NGS variant tracking

### 3.1 Human memory T cell subsets — markers (verify panel)

This is a humanized model with **human** CAR-T cells, so use human (not mouse) markers.

| Subset | Phenotype | Defining paper | PMID |
|---|---|---|---|
| Naive (Tn) | CD45RA+ CD45RO- CCR7+ CD62L+ CD27+ CD28+ CD95**low/neg** | Sallusto et al. 1999 *Nature* | **10537110** |
| Tscm (stem cell memory) | CD45RA+ CCR7+ CD62L+ CD27+ CD28+ **CD95+** IL-7Rα+ | Gattinoni et al. 2011 *Nat Med* | **21926977** |
| Tcm (central memory) | CD45RA- CD45RO+ CCR7+ CD62L+ CD27+ | Sallusto 1999 | **10537110** |
| Tem (effector memory) | CD45RA- CD45RO+ CCR7- CD62L- | Sallusto 1999 | **10537110** |
| Temra (terminal effector) | CD45RA+ CD45RO- CCR7- CD62L- (often CD57+, KLRG1+) | Mahnke et al. 2013 *EJI* | **24258910** [needs verification] |
| Trm (tissue-resident) | CD69+ CD103+/- (CD8); CD49a+, CXCR6+ | Mackay et al. 2013 *Nat Immunol* | **24162776** |

**CD95 is the discriminating marker for Tscm vs Tn** — both are CD45RA+ CCR7+ CD62L+ CD27+ CD28+, but only Tscm are CD95+ (Gattinoni 2011 PMID 21926977). Without CD95 in the panel, Tscm are scored as Tn — a frequent error. Standard sorting protocol is Lugli et al. 2013 *Nat Protoc* DOI 10.1038/nprot.2012.143 [PMID 23222456 needs verification].

### 3.2 The memory-timing flaw — fundamental

The plan as written sorts memory subsets on **days 1, 2, 4 post-rechallenge**. This is biologically incorrect for the stated goal:

- **TCR/CAR engagement at rechallenge converts memory cells to effectors within hours.** CCR7 and CD62L are downregulated immediately upon activation (Sallusto 1999 PMID 10537110). By day 1–2, what you sort as "Tcm" is no longer a memory cell.
- Days 1–4 post-rechallenge measure the **recall effector response**, not the pre-existing memory pool. These are different scientific questions and require different sampling windows.
- **The relevant memory pool is at end of 21-day rest, BEFORE rechallenge.**

**Recommended two-arm correction:**

| Arm | Timepoint | Readout | Question answered |
|---|---|---|---|
| A — Memory pool | Sacrifice **end of day 21 rest, before rechallenge** | Sort Tn/Tscm/Tcm/Tem (CAR+ gated) → NGS | Which scFv variants enrich in resting memory? |
| B — Recall response | Day 4 (effector peak) and/or day 7 post-rechallenge | Sort total CAR+ and CAR+Ki67+ → NGS | Which variants drive strongest recall? |
| C (optional) — Recall exhaustion | Day 7–10 post-rechallenge | PD-1 / TIM-3 / LAG-3 / TOX on CAR+ | Which variants resist exhaustion at recall? |

If mouse-budget forces a single sacrifice, **sacrifice at end of 21-day rest, before rechallenge** for the memory question; use **non-invasive bioluminescence imaging** in a separate intact rechallenged cohort for recall functional readout.

### 3.3 NGS readout — barcoding vs amplicon

**Critical first step**: map S214, Trp212, Y260, Y261 onto the FMC63 VL-Whitlow218-VH sequence. Confirm whether all four positions fit within a single 300-bp Illumina paired-end read. *This determines whether one amplicon suffices or whether barcoding is mandatory.* Use the published FMC63 sequence (Addgene FMC63-218-CAR vectors; cross-reference the He 2023 PDB 7URV chain definitions) to verify.

| Feature | Amplicon-seq of mutated region | DNA barcoding (5'/3'-UTR) |
|---|---|---|
| Cloning effort | Low | High (variant-to-barcode lookup) |
| Sequencing | Single MiSeq run if positions in 300 bp | Trivial |
| Errors near NNK | Confounding (need UMIs) | Eliminated |
| Chimeric reads | Risk | Negligible |
| Long-read needed if positions >250 bp apart | Yes (PacBio/Nanopore) | No |
| Recommended for 376 vars | OK if single amplicon | **Preferred** if any pair >250 bp apart |

**Recommendation**: DNA barcode the library upfront. The 2–3 weeks of cloning effort eliminates four classes of confounder simultaneously: (a) chimeric reads, (b) NNK base-call errors, (c) PCR error-driven double-mutants, (d) need for long-read sequencing. Add UMIs to gene-specific PCR primers regardless (Kivioja et al. 2011 *Nat Methods* PMID **22101854**).

### 3.4 NGS depth and statistics

- Rule of thumb: ≥1000 reads per variant per condition for confident log2-fold-change with replicates.
- 376 variants × 6 conditions × 5 mice × 1000× = ~11 M reads minimum per pool — within a single MiSeq v3 (25 M) or NextSeq run.
- **Pre-injection library NGS is non-negotiable.** Without input counts, no enrichment ratio is interpretable.
- Statistical framework: **MAGeCK MLE** (Li et al. 2014 *Genome Biol* PMID **25476604**) is designed for pooled-screen enrichment problems; Belk et al. 2022 *Cancer Cell* PMID **35750052** is a useable in vivo CRISPR-screen template.

### 3.5 Memory + NGS confounders

| # | Confounder | Mitigation | Citation |
|---|---|---|---|
| 1 | No pre-injection library reference | Sequence plasmid library + post-expansion infusion product | Li 2014 PMID **25476604** |
| 2 | PCR jackpotting / amplification bias | UMIs on gene-specific primers | Kivioja 2011 PMID **22101854** |
| 3 | NNK codon bias (R/L/S 3× over W/Y/M/F; 3% stop) | Filter stop reads; scale by NNK theoretical freq | (NNK theoretical) |
| 4 | Sequencing error near NNK | UMI consensus + Q30 filter; barcoding bypasses | Kivioja 2011 |
| 5 | Memory subset gating impurity | ≥95% post-sort purity; CD45RA depletion bead pre-enrichment | Lugli 2013 *Nat Protoc* |
| 6 | Tscm vs Tn confusion if CD95 missing | Always include CD95 in panel | Gattinoni 2011 PMID **21926977** |
| 7 | Cell death during dissociation biases robust subsets | Cold processing, low-protease, viability stain | (general methods) |
| 8 | Multi-mouse pooling loses biological replicate | Per-mouse processing where cell numbers permit; pool only Tscm if forced | (general statistics) |
| 9 | TCR/CAR activation downregulates CCR7/CD62L | Sort BEFORE rechallenge or use markers that persist (CD27, CD95, IL-7Rα) | Sallusto 1999 PMID **10537110** |
| 10 | CAR internalization upon CD19 binding | Stain with CD19-Fc tetramer at saturating concentration | (CAR biology) |
| 11 | Tscm cell-number feasibility | Pilot one mouse before committing; expect 1–2 × 10⁶ Tscm per spleen → adequate but tight | Sabatino 2016 PMID **27226436** |

### 3.6 Memory + NGS recommendations

1. **Move primary memory sampling to end of 21-day rest, before rechallenge.** Use rechallenge as separate functional readout in a paired cohort.
2. **DNA-barcode the library** unless residue mapping confirms all four positions fit in a single 300-bp read.
3. **Pre-inject library NGS, post-expansion infusion-product NGS, tissue NGS** — three reference timepoints.
4. **n ≥ 5 mice per arm**; per-mouse processing for Tcm/Tem; pool 2–3 mice for Tscm if cell numbers tight.
5. **MAGeCK MLE** for enrichment statistics; report log-fold-change vs input library, not absolute counts.
6. **CD95 in every memory panel** for Tscm vs Tn distinction.
7. **Confirm CAR detection reagent** (CD19-Fc tetramer preferred over surrogate transduction marker unless intentionally included).
8. **Pilot with 8 known-controls** before full-library deployment.

---

## 3a. Activation / exhaustion kinetics (day 1, 2, 4 sampling)

### 3a.1 Rationale (clarified)

Day 1, 2, 4 sampling is intended for **activation and exhaustion kinetic profiling across CAR mutants**, NOT for memory phenotyping. Memory phenotyping comes from terminal sacrifice (end of 21-d rest, and/or post-rechallenge — see §3.2). The two readouts answer different questions and use different timepoints.

**Marker kinetics in standard CAR-T activation / exhaustion** (verify with primary panel optimization):

| Day | Activation markers | Effector function | Early exhaustion |
|---|---|---|---|
| Day 1 (~24 h) | CD69 peak (~24 h, CD25 ramping, ICOS/OX40 induction | IFN-γ, TNF-α, IL-2 production initiating | PD-1 mRNA induction; protein begins to rise |
| Day 2 (~48 h) | CD25 plateau, CD69 declining, ICOS/OX40 sustained | Granzyme B / perforin granule loading | PD-1 surface protein clearly elevated; TIM-3 / LAG-3 emerging |
| Day 4 | Effector differentiation | IFN-γ / TNF-α / cytotoxicity peak | PD-1, TIM-3, LAG-3 sustained; TOX accumulating; T-bet/EOMES dynamics |

References for kinetics: **Long et al. 2015** *Nat Med* 21:581-590, PMID **25939063** (4-1BB ameliorates tonic-signaling-driven CAR-T exhaustion — verified). For TOX as exhaustion master regulator, Khan et al. 2019, Scott et al. 2019, Alfei et al. 2019 (all *Nature*) — flag **[needs primary verification]** before final use.

### 3a.2 Pooled-library sort-then-NGS strategy

A single bulk FACS readout averages activation across all variants and loses per-variant resolution. The informative design is:

```
At each timepoint (day 1, 2, 4):
    Stain CAR+ cells with full activation/exhaustion panel
    Sort into bins:
        e.g., CD69+ vs CD69-
        e.g., PD-1^hi vs PD-1^lo
        e.g., TOX+ vs TOX- (intracellular)
    Extract DNA from each bin → variant amplicon-seq or barcode-seq
    Compute log2-fold-change of variant frequency in CD69+ vs CD69- (etc.)
    → identifies which scFv variants enrich in each phenotype
```

This sort-then-NGS approach is the same logic as cytometry-based fitness-screen designs in pooled CRISPR work and gives per-variant phenotype assignments without arrayed analysis.

### 3a.3 Recommended FACS panel (CAR+ gated)

| Category | Markers | Notes |
|---|---|---|
| Live/dead, lineage | LIVE/DEAD (Zombie/DAPI), CD45, CD3, CD8, CD4 | First three steps of any CAR-T panel |
| CAR detection | **CD19-Fc tetramer** (preferred) or anti-idiotype / surrogate transduction marker | Confirm what's in Manpreet's vector |
| Activation (surface) | **CD69, CD25, ICOS, OX40 (CD134)** | CD69 is earliest (24 h); ICOS/OX40 sustained 48-72 h |
| Exhaustion (surface) | **PD-1, TIM-3, LAG-3, TIGIT, CD39, 2B4** | All co-expressed in terminal exhaustion (Wherry & Kurachi 2015 review) |
| Exhaustion (intracellular) | **TOX, NR4A1** | Master regulators; require fix/perm |
| Effector function (intracellular) | **IFN-γ, TNF-α, IL-2, granzyme B, perforin** | Need brief stim + protein transport block before fix |
| Differentiation TFs (intracellular) | **T-bet, EOMES, BLIMP-1, TCF1/TCF7** | TCF1 marks stem-like / progenitor exhausted |
| Proliferation | **Ki67** | Intracellular |
| Apoptosis | Annexin V (or active caspase-3) | Surface stain pre-fix |

Realistically split across 3-4 separate panels because of fluorochrome limits — each panel internally normalized to CAR+ live singlets.

### 3a.4 Sampling strategy — blood vs tissue

| Sample | Pros | Cons | Use |
|---|---|---|---|
| **Peripheral blood serial sampling** (retro-orbital or tail vein) | Same mouse multiple timepoints; non-terminal | Limited blood volume (~100 µL × 2 in mouse); reflects circulating cells, may miss tissue-infiltrating | Day 1, 2, 4, 7 kinetic profiling |
| **Spleen** (terminal) | High cell numbers; major secondary lymphoid organ for CAR-T | Sacrifice required | Cohort sacrificed at each timepoint |
| **Bone marrow** (terminal) | Where NALM-6 colonizes first; key for tumor-infiltrating CAR-T | Sacrifice required; lower cell yield | Cohort sacrificed at each timepoint |
| **Liver** (terminal) | NALM-6 also colonizes liver | Sacrifice required | Optional |

**Recommended hybrid design**: serial blood at day 1, 2, 4, 7 (kinetic resolution) + cohort sacrifices at day 4 and day 14 (tissue infiltration + intracellular markers). Mouse budget: blood-only kinetics minimal extra burden; terminal cohorts add ~5 mice × 2 timepoints × n arms.

### 3a.5 Confounders — activation/exhaustion arm

| # | Confounder | Mitigation |
|---|---|---|
| 1 | Trafficking incomplete by day 1 (CAR-T may still be in lung/circulation) | Blood sampling captures circulating; tissue sampling at day 4+ for engrafted; do not over-interpret day 1 tissue numbers |
| 2 | Co-expression of activation + exhaustion markers (CD69+PD-1+ effector vs CD69-PD-1+ exhausted) | Boolean gating; use UMAP / FlowSOM for unbiased phenotype clusters |
| 3 | Pooled-library: variants compete for antigen, may cross-feed cytokines | Pilot variant comparisons in arrayed format; pool size limited to ≤80 variants for cleanest interpretation |
| 4 | Library bottleneck → some variants undetectable | Spike-in synthetic barcodes for normalization; pre-injection library NGS reference |
| 5 | Activation marker dynamics (CD69 peaks 24 h then declines) | Day 0.5 / day 1 / day 2 to bracket the peak; do not assume linear progression |
| 6 | TCR-mediated bystander activation (xeno) confounds | Use NSG-MHC-DKO if budget allows; baseline control with no-tumor + CAR-T-only mice |
| 7 | Cell death during dissociation differentially affects exhausted vs non-exhausted | Cold processing; viability gating; report viability per sample |
| 8 | CAR internalization upon CD19 engagement → CAR-staining artifact | CD19-Fc tetramer at saturating concentration; or T2A-fluorescent reporter co-expression |
| 9 | Mouse-to-mouse variability dominates pooled signal | n ≥ 5 mice per timepoint per arm; mixed-effects model |
| 10 | Tissue compartment differences not captured | Sample blood, spleen, BM separately; do not pool tissues |

### 3a.6 Integration with the rest of the design

| Time after CAR-T injection | Sampling | Readout | Question answered |
|---|---|---|---|
| Day 1, 2, 4 (blood serial) | All mice, light bleed | FACS panel (activation/exhaustion); aliquot for variant NGS by sort | Activation/exhaustion KINETICS per variant |
| Day 4 (terminal cohort) | Spleen + BM | Same panel + tissue infiltration count | Tissue distribution of activation/exhaustion phenotypes |
| Day 7-14 (terminal cohort, optional) | Spleen + BM | Late effector / contraction phase | Persistence of activation/exhaustion phenotype |
| **End of day 21 rest (terminal cohort)** | Spleen + LN + BM | **Memory phenotype panel + variant NGS** | **Memory pool composition per variant** |
| Rechallenge day 1, 2, 4 | Blood serial | Activation/exhaustion panel | Recall response kinetics |
| Rechallenge day 7 (terminal cohort) | Spleen + LN + BM | Recall effector + late activation/exhaustion | Recall functional phenotype |

This sequence cleanly separates **kinetic profiling** (day 1-4, blood + early tissue) from **memory characterization** (end-of-rest sacrifice, tissue) from **recall response** (post-rechallenge), with each timepoint matched to its biologically appropriate readout.

---

## 4. In vitro arm — antigen density + co-culture

### 4.1 Tunable CD19 NALM-6 systems (verified)

The repo already has this in document 11 (Alternative Assay Systems). Briefly:

| System | Method | Best use | Citation |
|---|---|---|---|
| **NALM-6 CD19-KO + graded re-expression** | CRISPR knockout, then transduce with titrated CD19 lentivirus | Gold standard for antigen-density studies | Majzner et al. 2020 *Cancer Discov* PMID **32193224** |
| K562-CD19 (parental K562 is CD19-) | Transduce K562 with CD19 at varied levels | Alternative myeloid background | Multiple |
| CHO-CD19 (Low/Med/High) | Stable CHO lines used for xCELLigence | Adherent cytotoxicity readout | Multiple |
| Imanis NALM6-CD19-low/Fluc | Pre-built reagents | Off-the-shelf | Imanis catalog |

**Recommendation**: NALM-6 CD19-KO + graded re-expression (Majzner 2020 system) is the published gold standard. The functional threshold for CART19 is ~2,000 CD19 molecules/cell — below this, even high-affinity CARs lose function. For affinity-tuning experiments, CD19 levels at 500, 2,000, 10,000, 50,000 molecules/cell give the right dynamic range.

### 4.2 In vitro repeat-stimulation arm (recommended addition)

The plan describes a single-pass co-culture with different CD19 levels. A more informative complement is **repeat-stimulation co-culture** that simulates chronic antigen exposure:

- Re-add fresh NALM-6 every 2 days × 4 cycles
- Sort CAR+ cells at end of cycle 4 → NGS
- Identifies variants resistant to exhaustion under chronic stimulation
- Already in repo doc 09 (rechallenge protocols)

### 4.3 In vitro confounders

Many of the in vivo confounders apply (library bottleneck, MOI, integration bias, surface expression). Additional in vitro-specific:

| # | Confounder | Mitigation |
|---|---|---|
| 1 | NALM-6 outgrowth heterogeneity | Single-clone working stock; re-validate every 5 passages |
| 2 | Cytokine gradient consumption in 96-well | Use 24-well plates for repeat-stim; refresh media |
| 3 | Effector death in late co-culture | Account for by viability gating + adjust E:T over time |
| 4 | Cross-feeding of cytokines from high-affinity variants rescuing low-affinity variants | Limit pool size if signal is concerning; arrayed validation of top hits |
| 5 | Antigen density drift in NALM-6-CD19-titrated lines | Re-FACS each batch; freeze working stocks |

### 4.4 In vitro arm recommendations

1. Use **NALM-6 CD19-KO + graded re-expression** (Majzner 2020 system) — five CD19 levels including CD19-null negative control.
2. Add a **repeat-stimulation arm** as in vitro proxy for in vivo memory pressure.
3. Pilot with same 8 known-control variants before full library.
4. NGS readout same as in vivo (barcoded library, pre-input reference, MAGeCK MLE).

---

## 5. Biophysics arm — protein production, SPR, 2D kinetics

### 5.1 scFv production in Expi293F

- **Expi293F is a reasonable choice** but is *not* the literature precedent for FMC63 scFv.
- **He et al. 2023** produced FMC63-scFv in **Sf9 insect cells** (GP67 secretion peptide, HRV-3C cleavage, 8×His).
- **Seigner et al. 2023** produced FMC63-scFv in **HEK293-6E** (not Expi293F, not HEK293S; transient suspension HEK with truncated EBNA-1).

Either Expi293F or HEK293-6E will work; the student should justify the choice.

**Format options for SPR:**

| Format | Pros | Cons | Fit for SPR |
|---|---|---|---|
| scFv-Avi-His monomer | Site-specific biotinylation; oriented capture | ~20% diabody fraction in FMC63 (Seigner 2023) | **Optimal** (matches Seigner 2023 protocol) |
| scFv-His monomer | Simple | Same diabody issue | Adequate; SEC pre-cycle |
| scFv-Fc | High yield, easy Protein A | **Bivalent → invalidates monovalent KD** | Unsuitable as analyte |
| Fab | True monovalent, native disulfides | More complex prep | **Gold standard** for orthogonal validation; recommend for top 3 mutants |

**Critical FMC63-specific issue**: Seigner 2023 (PMID 38155191) reports that FMC63-scFv exhibits a dynamic monomer–diabody equilibrium (~20% dimer at equilibrium) and that **SEC purification of pure monomer fails** because the equilibrium re-establishes on the timescale of SEC. This is the leading explanation for the 0.3–47 nM (~150-fold) spread in published FMC63-CD19 KD values. **Mitigations:**
- SEC-MALS QC every batch
- Use SEC-monomer fraction within ~1 h of purification
- **Fab format as orthogonal validation** — Fabs do not domain-swap to diabodies

### 5.2 CD19 production — definitive recommendation

**Use Expi293F + SF-CD19 (Laurent 2021).**

#### Why this is the right choice (decision matrix)

| Cell line | Glycoform | Yield (ECDs) | Monomer stability | CAR field use | Verdict |
|---|---|---|---|---|---|
| **Expi293F + SF-CD19** | **Full complex (matches in vivo)** | **High (10-50 mg/L)** | **Excellent (engineered)** | **Standard** | **PRIMARY RECOMMENDATION** |
| HEK293-6E + SF-CD19 | Full complex | Moderate-high | Excellent | Used by Seigner 2023 | Equivalent fallback (NRC license needed) |
| HEK293F (FreeStyle) | Full complex | Moderate | WT aggregates | Less common | OK if Expi293F unavailable |
| HEK293S GnTI⁻ | **Man₅ only — wrong glycoform** | Moderate | – | Crystallography only | **Avoid** unless crystallizing |
| CHO | Slightly different (LacdiNAc, no α2,6-sialic acid) | High | – | Less preferred | Avoid for kinetics |
| Sf9 insect | Paucimannose (wrong) | High | – | He 2023 used for FMC63-scFv (NOT CD19) | Avoid for CD19 |
| E. coli + refold | None | n/a | Severe refold issues (CD19 has 2 disulfides) | – | Do not attempt |

**The HEK293S point is critical**: "HEK293S" in the field universally means the **GnTI⁻ line** (Reeves et al. 2002 *PNAS* PMID **12370423** — verified) which produces only high-mannose Man₅GlcNAc₂ glycans. He 2023 used this for the cryo-EM structure (PDB 7URV) because crystallography needs glycoform homogeneity. **For SPR/BLI binding studies of FMC63 mutants**, you want CD19 with the same glycoform B cells display in patients — full complex sialylated N-glycans — which means **Expi293F or HEK293-6E**, not HEK293S.

#### Why SF-CD19 specifically
WT human CD19-ECD aggregates badly when expressed solubly (multiple groups report this). **Laurent E et al. 2021** *ACS Synth Biol* 10(5):1184-1198, PMID **33843201** used yeast-display directed evolution to identify "SuperFolder" stabilizing mutations that produce a soluble monomer (>99% by SEC-MALS). Seigner 2023 used this construct in HEK293-6E + Biacore T200 with a monomer-monomer protocol and got the converged KD = 5.1 nM. **Without SF-CD19, you will fight aggregation for months** before getting clean SPR data. The exact stabilizing mutations are published in Laurent 2021 supplementary data.

#### Construct design checklist

| Element | Specification | Source / verification |
|---|---|---|
| ECD boundaries | Met1 to ~Lys291 (remove TM + cytoplasmic) | UniProt P15391 (human CD19) |
| Stabilizing mutations | SF-CD19 set from Laurent 2021 | PMID 33843201 supplementary |
| Affinity tag | Cleavable C-terminal His₁₀ + HRV-3C site (or Avi-tag if site-specific biotinylation desired) | Standard |
| Fc fusion (optional, removed before SPR) | Cleavable hIgG1-Fc for Protein A purification step, then HRV-3C cleaved off; **never run kinetics with Fc still attached** (avidity inflates KD 100-1000×) | Multiple |
| Vector | pcDNA3.4 / pcDNA3.1+ / pCAGGS — all compatible with Expi293F transient | Thermo Fisher protocols |
| Signal peptide | Native CD19 SP or IgG-κ leader | Standard |

#### Production protocol skeleton (Expi293F)

```
1. Transient transfection: ExpiFectamine 293, 1 µg DNA / mL culture
2. Day 0: 3 × 10⁶ cells/mL Expi293F suspension, 37 °C, 8% CO₂, 125 rpm
3. Day +1: enhancer addition (provided in kit)
4. Day +5 to +7: harvest supernatant; centrifuge + 0.22 µm filter
5. Affinity purification: HisTrap (or Protein A if Fc-fusion), elute with imidazole gradient
6. (If Fc) HRV-3C cleavage overnight, 4 °C, 1:50 protease:protein
7. Reverse-IMAC to remove cleaved Fc + uncut material
8. SEC polishing (Superdex 200 Increase, PBS pH 7.4) — keep monomer peak only
9. Concentrate to 1-2 mg/mL; spin 15,000 g × 10 min before flash freezing aliquots
10. SEC-MALS QC every batch — target >99% monomer
```

#### Yields to expect
- Expi293F + SF-CD19 (cleaved final): 5-15 mg/L of culture is realistic; 50 mL test scale → 0.25-0.75 mg per prep
- For SPR with 10 mutants × 5 concentrations × triplicate: <1 mg total CD19 needed
- Therefore one good Expi293F prep covers an entire SPR campaign

#### Storage and handling
- Aliquot 50-100 µg per tube in PBS pH 7.4 + 0.02% NaN₃
- Flash freeze in liquid N₂; store -80 °C
- Single freeze-thaw only; spin 15,000 g × 10 min before each SPR injection
- Verify activity with FMC63 WT in every chip cycle as positive control

#### Fallbacks
- **If Expi293F not accessible**: HEK293-6E (Seigner 2023's exact system) — requires NRC Canada license (free for academic use). Same yields, same SF-CD19 construct.
- **If only HEK293F (FreeStyle) available**: works but lower yields than Expi293F — SF-CD19 still mandatory.

#### Common pitfalls to avoid
- Using HEK293S GnTI⁻ for kinetics → wrong glycoform → not directly comparable to in vivo
- Using WT CD19-ECD without SF mutations → aggregation, multimodal SEC, biphasic SPR
- Keeping Fc fusion on for SPR → bivalent → KD apparently 100-1000× tighter than monovalent (Seigner 2023 directly demonstrates this)
- Skipping SEC-MALS QC → undetected aggregates in some batches → SPR drift between runs
- E. coli refold → broken disulfides, multimodal mixture, do not attempt

### 5.3 SPR for FMC63-CD19 — published parameters (verified)

| Source | KD | kon (M⁻¹s⁻¹) | koff (s⁻¹) | Instrument | PMID |
|---|---|---|---|---|---|
| Seigner 2023 | **5.1 nM** (range 2–6) | **1.0 × 10⁵** | **5.3 × 10⁻⁴** | Biacore T200, Biotin CAPture S | **38155191** |
| He et al. 2023 | **4.5 nM** | – | – | Biacore 8K, NTA | **36867678** |

The two datasets agree to within 2-fold despite different instruments, capture chemistry, and CD19 sources. Field consensus: KD ≈ 4–6 nM is the true monovalent affinity once avidity is excluded.

**Recommended SPR protocol skeleton (built from Seigner 2023):**
```
Chip:           Biotin CAPture S Series (Cytiva), re-loadable
Ligand:         Biotinylated FMC63-Avi-His scFv (or mutant), ~1000 RU
Analyte:        SF-CD19 monomer; 5 conc. (0.5, 4, 20, 100, 500 nM); single-cycle kinetics
Buffer:         PBS + 0.1% BSA + 0.05% Tween-20, pH 7.4 (or HBS-EP+)
Temperature:    25 °C
Flow rate:      30 µL/min
Association:    600 s
Dissociation:   1200 s (because koff ~5×10⁻⁴ s⁻¹ → t½ ~22 min; need ≥3 t½)
Regeneration:   3 M GuHCl + 1 M NaOH, 120 s @ 10 µL/min (validate scFv stability across cycles)
Fitting:        1:1 Langmuir
Replicates:     n ≥ 3 independent runs
```

For mutants with predicted very-slow koff (<10⁻⁴ s⁻¹), single-cycle kinetics is mandatory.

### 5.4 SPR confounders

| # | Confounder | Mitigation |
|---|---|---|
| 1 | Avidity from scFv-Fc or CD19-Fc analyte | Use only monomeric forms |
| 2 | Mass transport limitation (high ligand density) | ≤1000 RU; vary flow rate (10/30/100 µL/min) — koff should be flow-independent |
| 3 | Diabody contamination of scFv (20% of FMC63) | SEC-MALS QC; Fab format as orthogonal validation |
| 4 | Non-specific binding for charged mutants (S214D etc.) | Reference channel subtraction; Tween-20; 0.1% BSA |
| 5 | Rebinding at low koff | Higher flow, lower ligand density, longer dissociation |
| 6 | Regeneration damage | Re-loadable Biotin CAPture; monitor WT KD across cycles |
| 7 | Buffer sensitivity (pH, salt) for charged mutants | Run physiological NaCl; for S214D test pH 6.5 endosomal mimic |
| 8 | Aggregation on injection | SEC monomer + spin 15,000 g 10 min |
| 9 | Reproducibility variance (literature spans 0.3–47 nM) | Adopt Seigner 2023 monomer-monomer protocol; benchmark WT every chip cycle |

### 5.5 2D micropipette adhesion frequency assay

**Origin**: Chesla, Selvaraj, Zhu 1998 *Biophys J* 75:1553–1572 PMID **9726957** (verified). Output: 2D kon (µm⁴/s, NOT M⁻¹s⁻¹) and 2D koff. Bell-Dembo small-system kinetic fit.

**Has anyone published 2D kinetics for any CAR-antigen system?** Verified search: **No.** TCR-pMHC has extensive 2D literature (Huang 2010 *Nature* PMID **20357766**; Huppa 2010 *Nature* — verify PMID); **CAR-CD19 has none in adhesion frequency or BFP**. Two 2025 bioRxiv preprints (2025.10.22.683904 and 2025.10.23.684052) measure FMC63-CART19 forces (8–19 pN) using **DNA tension probes**, not adhesion frequency — they do not extract 2D kon/koff. **This means a proper 2D analysis of FMC63-CD19 mutants is genuinely novel** and strengthens the project's novelty argument.

**Practical concerns:**
- **Apparatus is custom-built** (Zhu lab Georgia Tech, Selvaraj Emory, Liu Utah, a few European groups, Hai Qi at Tsinghua). I am not aware of a 2D adhesion rig at CSIR-IGIB. **Requires external collaboration.**
- **Throughput**: ~5–10 mutants per month at best. Not compatible with 80–376 variants. **Reserve 2D for top 2–3 mutants** identified by SPR + functional assays.
- **Operator training**: 6–12 months of mentored work before independent data.
- **Trainee-feasible alternatives**: acoustic force spectroscopy (Lumicks z-Movi — verify availability at NCBS Bangalore), DNA tension probes (Salaita lab style), single-molecule TIRF FRET (Huppa 2010).

### 5.6 Catch bond detection

**Adhesion frequency at zero force does NOT detect catch bonds.** Catch-bond identification requires force-clamp methods:
- BFP (biomembrane force probe): Liu et al. 2014 *Cell* PMID **24725404**
- Optical tweezers: Sibener et al. 2018 *Cell* PMID **30053426**
- AFM force-clamp / magnetic tweezers

**For CARs**: the 2025 bioRxiv preprints establish CAR forces but do not reconstruct catch-vs-slip profiles. **No peer-reviewed catch-bond data exists for any CAR.** Defer this to **Phase 2 collaboration** (likely with Zhu/Liu/Qi labs); not realistic to include as initial PhD scope.

### 5.7 Biophysics — tiered strategy (recommendation)

| Tier | Method | # mutants | Purpose | Throughput |
|---|---|---|---|---|
| 1 | Functional screens (in vivo + in vitro) | 50–100 | Identify functionally interesting variants | – |
| 2 | BLI / Octet | 20–30 | Rapid kinetic triage | 24/run |
| 3 | SPR (Biacore T200/8K) | 6–10 | Primary 3D kinetic dataset | 6–8/day on T200, 25–30/day on 8K |
| 4 | 2D adhesion frequency (collaboration) | 2–3 | Membrane-context kinetics; novelty | 5–10/month |
| 5 | BFP catch bond (Phase 2 collaboration) | 1–2 | Mechanobiology; secondary novelty | 1–2/quarter |

### 5.8 Biophysics — recommended changes to plan

1. **Switch CD19 production from "HEK293S" to Expi293F-produced SF-CD19** (Laurent 2021 stabilized monomer) for SPR. Keep HEK293S GnTI⁻ only if structural work is planned.
2. **Add Octet/BLI as a triage tier** before committing Biacore time.
3. **Add Fab format orthogonal validation** for top 3 mutants — directly addresses the FMC63 diabody artifact.
4. **Add z-Movi cellular avidity** as bridge between monomeric SPR KD and functional T-cell killing (verify NCBS Bangalore availability).
5. **Defer 2D micropipette to top 2–3 mutants only** via external collaboration.
6. **Defer catch-bond / BFP to Phase 2** with named collaborator; do not promise as initial PhD scope.

---

## 6. Cross-cutting issues — power, statistics, scope

### 6.1 Power analysis (high-level estimate)

For a pooled screen with 376 variants × 5–10 mice × 3–4 sample types × 4 timepoints, the dominant variance is mouse-to-mouse drift in variant composition. With **n = 5 mice per arm and ≥1000 reads/variant/condition**, 2-fold enrichment changes are detectable at MAGeCK-MLE-defined FDR < 0.1 in pooled screens (Li 2014; Belk 2022). For 4-fold changes, n = 3 may suffice. **A formal pre-registered power calculation is needed before DAC.**

### 6.2 Total mouse count budget

Conservative scope estimate:
- Primary pool screen, NSG: 5 mice × 4 arms (CD19+ NALM-6, CD19-KO NALM-6 control, no-tumor CAR-T-only baseline, untransduced T cell control) × 2 sacrifice timepoints (day 21 memory, day 21+rechallenge) = **40 mice minimum**
- Validation of top 5 hits: 5 mice × 5 hits × WT comparator = **25 mice**
- **Total ≥65 mice minimum for in vivo arm.** Add IACUC overhead.

### 6.3 Timeline reality-check (4-yr PhD)

- **Year 1**: Library construction (NNK cloning, barcoding, MOI titration); pilot 8 control variants through full workflow; in vitro repeat-stim screen.
- **Year 2**: Full in vitro pooled screen (CD19-graded NALM-6); top 50 hits in arrayed in vitro validation; begin scFv/CD19 protein production.
- **Year 3**: In vivo pooled screen OR arrayed in vivo validation of top hits; SPR on top 6–10 mutants; begin 2D collaboration.
- **Year 4**: 2D kinetics on top 2–3; manuscript writing; thesis writing; reserve catch-bond / BFP for postdoc.

This timeline assumes a single PhD student with technical support. It is achievable but not slack-filled. **A staged plan (in vitro pooled → in vivo arrayed) is far more defensible than a single in vivo pooled screen as Year 1 work.**

---

## 7. Summary recommendations table (for the DAC slide)

| Issue | Current plan | Recommended change | Priority |
|---|---|---|---|
| "Humanized mouse" terminology | Ambiguous; could mean PBMC/HSC | NSG (or NSG-MHC-DKO if rest >4 wk); explicit terminology | **Critical** |
| Memory sampling timing | Day 1, 2, 4 post-rechallenge | Sacrifice at end of 21-d rest, BEFORE rechallenge; rechallenge as separate readout | **Critical** |
| Pre-injection library NGS | Not mentioned | Sequence plasmid library + post-expansion infusion product as references | **Critical** |
| Library tracking | Not specified | DNA-barcode the library (or confirm single-amplicon coverage) | High |
| MOI control | Not specified | MOI ≤ 0.3; sort low-MFI singlets; qPCR VCN | High |
| CD19-KO NALM-6 control | Not in plan | Add as antigen-escape internal control | High |
| HEK293S for CD19 | As stated | Switch to Expi293F-produced SF-CD19 (Laurent 2021) for SPR | High |
| 2D micropipette in-house | As planned | External collaboration (Zhu/Liu/Qi); top 2–3 mutants only | Medium |
| Catch bond / BFP | Not specified | Defer to Phase 2 collaboration | Medium |
| Pooled in vivo as primary screen | As planned | Consider pooled in vitro + arrayed in vivo as fallback | Medium-High |
| Mouse n per arm | Not specified | n ≥ 5 per arm; pre-registered mixed-effects model | High |
| Fab orthogonal SPR | Not in plan | Add for top 3 mutants (eliminates FMC63 diabody artifact) | Medium |
| Octet/BLI triage tier | Not in plan | Add before Biacore commitment | Medium |

---

## 8. Citation corrections — applied 2026-05-01

The following corrections have been **applied** to the repo via `.fix_citations.py` (84 replacements across 16 markdown files). Each was verified against PubMed.

| Wrong (previous repo) | Correct | Status |
|---|---|---|
| "Singh et al. 2023" *Sci Immunol* (PDB 7URV) | **He C et al. 2023** *Sci Immunol* 8:eadf1426, **PMID 36867678** (full author list: He, Mansilla-Soto, Khanra, Hamieh, Bustos, Paquette, Garcia Angus, Shore, Rice, Khelashvili, Sadelain, Meyerson) | ✅ Applied (84 replacements, 16 files) |
| "Singh N, Frey NV, Engels B, et al." (hallucinated authors in `14_Computational_Validation.md`) | He C, Mansilla-Soto J, Khanra N, Hamieh M, et al. | ✅ Applied |
| "Singh NK et al." (wrong initials in `16_Primary_T_Cell_Validation.md`) | He C et al. | ✅ Applied |
| Drent 2019 cited correctly as *Clin Cancer Res* in repo | (no change) | — |
| Nicholson 1997 PMID in earlier session memory | **PMID 9566763** (Nicholson IC et al., *Mol Immunol* 34:1157–65, 1997) | ✅ Applied to memory file |
| "Zajc 2021" for SF-CD19 (wrong first author from agent draft) | **Laurent E et al. 2021** *ACS Synth Biol* 10:1184–1198, PMID 33843201 | ✅ Already correct in this doc |

**Files NOT modified (intentional):**
- `07_ET_Ratios_and_TimePoints.md` — contains a *different* paper "Selli ME, Landmann JH, Arveseth C, Singh N." 2023 *STAR Protocols* (PMC9826863) where Singh N is **senior author**, not first author. This is a real, verified, separate paper.
- `18_Experimental_Design_Expert_Review.md` — this document, which intentionally discusses the Singh→He correction.

**Slide deck (.pptx)**: not yet modified — slides created from scratch in `Experimental_Design_Reviewer_Slides.pptx` use correct attribution. The original `DAC_Presentation_v2.pptx` and `Computational_Validation_Presentation.pptx` may still contain "Singh" references and need manual correction or rebuild from the corrected build script.

---

## 9. Master verified reference list (alphabetical)

All citations below have been directly web-verified against PubMed in this session, except where tagged **[needs verification]**.

- **Alcantar-Orozco EM** et al. *Hum Gene Ther Methods* 24(5):310–20, 2013. PMID **23931270**. NSG limitations for CAR-T.
- **Belk JA** et al. *Cancer Cell* 40(7):768–786, 2022. PMID **35750052**. In vivo CRISPR T-cell screens; MAGeCK template.
- **Biasco L** et al. *Nat Cancer* 2:629–642, 2021. PMID **34345830**. Tisagenlecleucel Tscm clonal tracking.
- **Brehm MA** et al. *FASEB J* 33(3):3137–3151, 2019. PMID **30383447**. NSG-MHC-DKO no xeno-GvHD.
- **Brentjens RJ** et al. *Nat Med* 9(3):279–86, 2003. PMID **12579196**. NALM-6 in SCID-Beige (NOT NSG).
- **Brentjens RJ** et al. *Clin Cancer Res* 13(18):5426–35, 2007. PMID **17855649**. NALM-6 / SCID-Beige; primary FMC63 19-28z preclinical reference.
- **Castellanos-Rueda R** et al. *Nat Commun* 13:6555, 2022. PMID **36323661**. speedingCARs.
- **Chesla SE, Selvaraj P, Zhu C.** *Biophys J* 75(3):1553–1572, 1998. PMID **9726957**. Origin of 2D adhesion frequency assay.
- **Daniels KG** et al. *Science* 378(6625):1194–1200, 2022. PMID **36480602**. CAR signaling motif library + ML.
- **Davila ML, Kloss CC, Gunset G, Sadelain M.** *PLoS One* 8(4):e61338, 2013. PMID **23585867**. Immunocompetent mouse CD19 CAR; **not** NALM-6.
- **Davila ML** et al. *Sci Transl Med* 6(224):224ra25, 2014. PMID **24553386**. Clinical 19-28z CAR Phase I.
- **Day CP** et al. *Mol Ther* 22(8):1395–1403, 2014. PMID **24449212**. Bioluminescent imaging caveats.
- **Drent E** et al. *Clin Cancer Res* 25(13):4014–4025, 2019. PMID **30979735**. Combined CD28+4-1BB; affinity-tuned CAR.
- **Eyquem J** et al. *Nature* 543(7643):113–117, 2017. PMID **28225754**. TRAC knock-in CAR-T.
- **Gattinoni L** et al. *Nat Med* 17(10):1290–7, 2011. PMID **21926977**. Tscm definition (CD95+).
- **Gattinoni L** et al. *Nat Med* 23(1):18–27, 2017. PMID **28060797**. T memory stem cells review.
- **Goodman DB** et al. *Sci Transl Med* 14(670):eabm1463, 2022. PMID **36350984**. CAR Pooling.
- **He C** et al. *Sci Immunol* 8(81):eadf1426, 2023. PMID **36867678**. **CD19 CAR engagement / PDB 7URV / KD = 4.5 nM** — first author **He**, NOT Singh.
- **Huang J** et al. *Nature* 464(7290):932–936, 2010. PMID **20357766**. 2D TCR-pMHC kinetics.
- **Huppa JB** et al. *Nature* 463(7283):963–967, 2010. PMID **20164930**. TCR-pMHC in situ kinetics (verified).
- **Kawalekar OU** et al. *Immunity* 44(2):380–390, 2016. PMID **26885860**. 4-1BB Tcm/OXPHOS vs CD28 Tem/glycolysis.
- **King MA** et al. *Clin Exp Immunol* 157(1):104–18, 2009. PMID **19426570**. NSG-PBMC xeno-GvHD model.
- **Kivioja T** et al. *Nat Methods* 9(1):72–74, 2011. PMID **22101854**. UMIs.
- **Krishna S** et al. *Science* 370(6522):1328–1334, 2020. PMID **33335196**. Stem-like CD8 T cells in adoptive cell therapy.
- **LaFleur MW** et al. *Nat Commun* 10:1668, 2019. PMID **30971695**. CHIME in vivo CRISPR.
- **Li W** et al. *Genome Biol* 15(12):554, 2014. PMID **25476604**. MAGeCK.
- **Liu B, Chen W, Evavold BD, Zhu C.** *Cell* 157(2):357–368, 2014. PMID **24725404**. TCR catch bonds (BFP).
- **Lugli E** et al. *Nat Protoc* 8(1):33–42, 2013. DOI 10.1038/nprot.2012.143. PMID **23222456**. Tscm sorting protocol (verified).
- **Mackay LK** et al. *Nat Immunol* 14(12):1294–1301, 2013. PMID **24162776**. CD8 Trm developmental pathway.
- **Mahnke YD** et al. *Eur J Immunol* 43(11):2797–2809, 2013. DOI 10.1002/eji.201343751. PMID **24258910**. Memory T cell consensus markers (verified).
- **Majzner RG** et al. *Cancer Discov* 10(5):702–723, 2020. PMID **32193224**. CD19 antigen density threshold; CD28>4-1BB at low antigen.
- **Milone MC** et al. *Mol Ther* 17(8):1453–64, 2009. PMID **19384291**. 4-1BB CAR + NALM-6 NSG.
- **Nicholson IC** et al. *Mol Immunol* 34(16-17):1157–65, 1997. PMID **9566763**. Original FMC63 scFv.
- **Orlando EJ** et al. *Nat Med* 24(10):1504–1506, 2018. PMID **30275570**. CD19 antigen escape genetics.
- **Reeves PJ** et al. *PNAS* 99(21):13419–13424, 2002. PMID **12370423**. HEK293S GnTI⁻ origin.
- **Rios X** et al. *Mol Ther* 31(11):3210–3224, 2023. PMID **37705245**. Barcoded CAR pooled screen.
- **Roth TL** et al. *Nature* 559(7714):405–409, 2018. PMID **30022017**. Non-viral CRISPR T-cell engineering.
- **Sabatino M** et al. *Blood* 128(4):519–528, 2016. PMID **27226436**. Clinical-grade CD19 CAR Tscm.
- **Sallusto F** et al. *Nature* 401(6754):708–712, 1999. PMID **10537110**. Tcm/Tem original definition.
- **Seigner J** et al. *Sci Rep* 13:23024, 2023. PMID **38155191**. **FMC63-CD19 KD = 5.1 nM (Biacore T200, monomer-monomer)**. PMCID PMC10754921.
- **Shultz LD** et al. *Nat Rev Immunol* 12(11):786–98, 2012. PMID **23059428**. Humanized mouse review.
- **Sibener LV** et al. *Cell* 174(3):672–687, 2018. PMID **30053426**. TCR signaling-affinity uncoupling.
- **Sotillo E** et al. *Cancer Discov* 5(12):1282–95, 2015. PMID **26583447**. CD19 splice-variant resistance.
- **Wunderlich M** et al. *PLoS One* 13(12):e0209034, 2018. PMID **30586420**. NSGS reconstitution.
- **Xu Y** et al. *Blood* 123(24):3750–9, 2014. PMID **24782509**. Tscm correlate with CAR-T expansion + persistence.
- **Laurent E** et al. *ACS Synth Biol* 10(5):1184–1198, 2021. PMID **33843201**. SF-CD19 stabilized monomer for monovalent CAR interaction studies. Senior author Traxlmayr (same group as Seigner 2023). **(Note: this paper is sometimes misattributed to "Zajc"; first author is Laurent.)**

**All previously [needs verification] PMIDs were verified 2026-05-01**: Huppa 2010 → PMID 20164930; Lugli 2013 → PMID 23222456; Mahnke 2013 → PMID 24258910. Authors and titles confirmed against PubMed.

---

## 10. Open questions for Manpreet / PI

1. **Confirm "humanized mouse" intent**: PBMC/HSC engrafted, or plain immunodeficient host for adoptive CAR-T?
2. **Confirm "HEK293S" intent**: GnTI⁻ specifically, or generic HEK293/Expi293 by reflex?
3. **CAR-detection reagent**: which surrogate marker is in the construct (CD19-Fc tetramer? truncated CD34? EGFRt?) — this drives FACS panel design.
4. **Single Biacore on-site**: is T200 or 8K accessible at CSIR-IGIB, or does the work require collaborative access (NCBS, IISc, IIT-B)?
5. **z-Movi (Lumicks)**: confirm availability in India.
6. **2D / BFP collaborator**: which lab is plausible (Zhu Georgia Tech / Liu Utah / Qi Tsinghua)?
7. **Library complexity at infusion**: pilot data on what fraction of variants survive lentiviral transduction + 1-week expansion?
8. **Pre-registered statistical plan**: required before any DAC review of results.
9. **Mouse budget approval**: ≥65 mice for the in vivo arm — is this within IACUC capacity?
10. **Decision: pooled in vivo screen vs pooled in vitro + arrayed in vivo validation** — which is the primary plan for thesis defense?

---

## 11. What this review IS and IS NOT

**This review IS:**
- An expert critique of the proposed experimental design with verified PubMed citations.
- A confounder audit listing first-order risks per arm.
- A prioritized list of changes recommended before DAC presentation.
- A list of citation corrections needed in existing repo documents.

**This review IS NOT:**
- A primary literature review (already in documents 01–05).
- A protocol document (some specifics deferred to documents 06–16).
- An IACUC application or statistical pre-registration.
- A decision document — final scope is the PI's call.

---

*Prepared by expert review of three independent specialist agents (in vivo arm, memory + NGS, biophysics) with verified citations cross-checked against PubMed. Date: 2026-05-01.*
