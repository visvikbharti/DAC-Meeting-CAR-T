# Aims and Objectives — Critique and Proposed Reframing

## For Manpreet Kour's PhD Thesis | CSIR-IGIB | Date: 2026-05-01

This is a concise companion to `18_Experimental_Design_Expert_Review.md`. Goal: tighten the PhD aims so they are defensible to the DAC, accurately reflect the experimental plan, and capture the genuine novelty of the project.

---

## 1. Current state — what Manpreet has framed

### Question 1
> Can tuning the affinity affect the amplitude of the CAR-T signal?
>
> **Objective 1**: To determine CAR-T cell efficacy in vivo and in vitro using scFv mutant CAR library.

### Question 2
> Is there any affinity window for CAR-T cells having better therapeutic outcomes?
>
> **Objective 2**: To do biophysical characterization of scFv mutants which performed better in vivo as well as in vitro.

---

## 2. Issues a DAC reviewer will raise

### Q1 + Objective 1

| Issue | Why it matters |
|---|---|
| Q1 is binary (can/can't) | Already answered "yes" by published literature: Liu 2015, Caruso 2015, Park 2017, Drent 2019, Ghorashian 2019, He 2023. The DAC will ask, "what is the open question?" |
| "Amplitude of the CAR-T signal" is ambiguous | Could mean proximal signaling (CD3ζ phosphorylation), transcriptional output (NFAT/NFκB), effector function (cytotoxicity/IFN-γ), expansion, persistence, or exhaustion — each different. The objective must specify. |
| Q1 ↔ Objective 1 mismatch | Q1 asks about *signal amplitude*. Objective 1 measures *efficacy*. Different concepts. |
| "Efficacy" undefined | Killing? Tumor clearance? Survival? Memory? — needs operational definition. |
| Doesn't reflect what's measured | Activation kinetics, exhaustion (PD-1/TIM-3/LAG-3/TOX), memory subsets (Tn/Tscm/Tcm/Tem), antigen-density dependence — all in the experimental plan but absent from the objective. |
| Library readout method not specified | Sort-then-NGS, MAGeCK MLE — not in objective. |

### Q2 + Objective 2

| Issue | Why it matters |
|---|---|
| Q2 is partially answered already | Mao 2022 *Front Immunol* (in repo) identified clinical optimal window 10–60 nM. Ghorashian 2019 *Nat Med* showed low-affinity CAT CAR clinically outperformed FMC63. The novelty is *refining and explaining* the window for FMC63-CD19 specifically. |
| "Therapeutic outcomes" undefined | Cytotoxicity? Persistence? Memory durability? Tumor-free survival? |
| Misses genuine novelty | Doesn't capture **dwell time / koff** as a separate axis from KD; **2D vs 3D kinetics** (no published CAR data); **catch bonds** (no published CAR data). |
| Logical sequence problem in Objective 2 | "Mutants which performed better" — but you cannot define what "performed better" means without first correlating biophysics with function. The biophysics IS what defines the affinity window. Restricting biophysics to good performers is circular. |
| Should include underperformers + intermediates | Without the full functional range, you cannot define a *window* — only a list of good mutants. |

---

## 3. Reformulated Q + O

### Question 1 (reformulated)
> **How does FMC63 scFv binding affinity quantitatively shape CAR-T cell activation, effector function, exhaustion, and memory formation, and does this relationship depend on antigen density?**

### Objective 1 (reformulated)
> To map activation kinetics (CD69, CD25, IFN-γ at 24/48/96 h), exhaustion trajectory (PD-1, TIM-3, LAG-3, TOX), cytotoxic function, and memory formation across a panel of FMC63 scFv affinity variants in NALM-6 co-culture (with graded CD19 density) and NALM-6/NSG xenograft models, with sort-then-NGS readout to identify variants enriched in each phenotypic state.

### Question 2 (reformulated)
> **Within the FMC63-CD19 binding spectrum, which kinetic parameter (KD, kon, koff, dwell time, 2D koff, catch-bond lifetime) best predicts CAR-T cell function, and what is the optimal kinetic window that maximizes durable anti-tumor activity while preserving memory formation?**

### Objective 2 (reformulated)
> To biophysically characterize a representative panel of FMC63 scFv variants spanning the full functional spectrum (high-performers, intermediates, low-performers, near-WT controls) by SPR (3D KD, kon, koff, dwell time) and 2D micropipette adhesion frequency (membrane-context kinetics; novel for any CAR system), and statistically correlate each kinetic parameter with in vitro and in vivo functional readouts to identify the parameter and the window that best explain therapeutic efficacy.

---

## 4. Proposed 3–4 aim structure (covers everything she's actually doing)

| Aim | Title | Maps to |
|---|---|---|
| **Aim 1** | Library design and computational validation: identify and computationally validate critical scFv contact residues at the FMC63-CD19 interface (PDB 7URV, He et al. 2023) using structural analysis and mCSM-AB2 ΔΔG predictions; design an NNK saturation mutagenesis library at four positions (primary: **S214, Trp212** — novel; secondary: **Y260, Y261** — beyond He et al.'s single Ala) yielding ~376 variants spanning the full affinity spectrum. | *Already largely done — the computational work in `14_Computational_Validation.md` and `17_Novelty_Strategy_and_Residue_Selection.md` fits here.* |
| **Aim 2** | Functional mapping in vitro and in vivo: characterize activation kinetics, effector function, exhaustion trajectory, and memory formation across the affinity variant library in NALM-6 co-culture (with graded CD19 density via NALM-6 CD19-KO + graded re-expression, Majzner 2020) and NALM-6/NSG xenograft models, using sort-then-NGS to identify variants enriched in each phenotypic state. | Q1 / Objective 1 (reformulated) |
| **Aim 3** | Biophysical characterization and kinetic–functional correlation: kinetically characterize a representative panel of variants (spanning the full functional range) by SPR (3D kinetics) and 2D micropipette adhesion frequency (membrane-context kinetics; novel for any CAR-antigen system); statistically correlate kinetic parameters with functional readouts to define the optimal window for anti-CD19 CAR-T therapy. | Q2 / Objective 2 (reformulated) |
| **Aim 4** (optional, translational) | Validate top-performing affinity variants in primary human T cells (multiple allogeneic donors); assess in vivo persistence and memory recall in NSG-MHC-DKO xenograft models for translational relevance. | Stretch goal; defends to thesis-defense level |

---

## 5. What this restructure achieves

| Concern | Before | After |
|---|---|---|
| Open question identifiable | Both Qs partially closed by literature | Both Qs reframed as quantitative mapping problems with clear novelty |
| Q ↔ Objective alignment | Mismatched (signal vs efficacy; biophysics vs performance) | Tightly aligned |
| Computational validation visible | Not in objectives despite being done | Aim 1 |
| Memory formation visible | Hidden | Explicit in Aim 2 |
| Antigen density visible | Hidden | Explicit in Aim 2 |
| 2D kinetics novelty visible | Hidden | Explicit in Aim 3 |
| Correlation analysis visible | Implied | Explicit in Aim 3 |
| Full affinity range | "Mutants which performed better" — circular | "Spanning the full functional spectrum" |
| Translational stretch | Absent | Aim 4 (optional) |

---

## 6. One-paragraph executive pitch (for the DAC opening)

> "Most published CAR-affinity studies test 2–5 variants and a single readout (cytotoxicity). My thesis builds the first systematic quantitative dataset linking ~376 FMC63 scFv variants to a full functional matrix — activation, exhaustion, memory, persistence — across in vitro and in vivo models, and to a multi-parameter kinetic dataset (3D + 2D + force-dependent), to define which kinetic parameter best predicts CAR-T cell function and the optimal window for anti-CD19 therapy. Two of the four mutated positions (S214, Trp212) have never been mutated in any published study; the 2D adhesion frequency and catch-bond data have never been published for any CAR-antigen system."

---

## 7. Action items

1. **Replace stated Q1, Q2, Objective 1, Objective 2** with reformulated versions (above) in DAC slides and thesis proposal.
2. **Add Aim 1 (computational validation)** as a separate aim — work is already done, it just needs to be visible.
3. **Add Aim 4 (primary T cell + NSG-MHC-DKO)** if scope allows — strengthens translational defense.
4. **Update DAC outline slide** to reflect 3–4 aims rather than 2 questions.

---

## 8. Verified literature cited above

- **Caruso HG** et al. "Tuning Sensitivity of CAR to EGFR Density Limits Recognition of Normal Tissue While Maintaining Potent Antitumor Activity." *Cancer Res* 75:3505-3518, 2015. PMID **26330164** (verified). EGFR (not EGFRvIII) — low-affinity (nimotuzumab) vs high-affinity (cetuximab) CAR.
- **Drent E** et al. *Clin Cancer Res* 25(13):4014-4025, 2019. PMID **30979735**. (Combined CD28+4-1BB; affinity-tuned CAR.)
- **Ghorashian S** et al. "Enhanced CAR T cell expansion and prolonged persistence in pediatric patients with ALL treated with a low-affinity CD19 CAR." *Nat Med* 25(9):1408-1414, 2019. PMID **31477906** (verified). (CAT CAR clinical superiority.)
- **He C** et al. *Sci Immunol* 8(81):eadf1426, 2023. PMID **36867678**. (FMC63-CD19 cryo-EM, PDB 7URV, KD = 4.5 nM.)
- **Liu X** et al. "Affinity-Tuned ErbB2 or EGFR Chimeric Antigen Receptor T Cells Exhibit an Increased Therapeutic Index against Tumors in Mice." *Cancer Res* 75:3596-3607, 2015. PMID **26330166** (verified). ErbB2/EGFR — note: journal is *Cancer Research*, not *Cancer Immunol Res* as some secondary sources state.
- **Majzner RG** et al. *Cancer Discov* 10(5):702-723, 2020. PMID **32193224**. (CD19 antigen density threshold.)
- **Mao R, Kong W, He Y.** "The affinity of antigen-binding domain on the antitumor efficacy of CAR T cells: Moderate is better." *Front Immunol* 13:1032403, 2022. PMID **36325345** (verified — corrected from earlier draft). Clinical review of 38 solid-tumor CART trials: high-affinity ABDs gave 5.7% response rate; moderate-affinity gave 35%.
- **Seigner J** et al. *Sci Rep* 13:23024, 2023. PMID **38155191**. (FMC63-CD19 KD = 5.1 nM; monomer-monomer protocol.)

**Note on Park 2017 ROR1 affinity**: a "Park 2017 *Mol Ther*" reference for ROR1 CAR affinity could not be verified against PubMed in this session and may have been a memory error. The verified primary reference for ROR1 CAR affinity is **Hudecek M et al.** "Receptor affinity and extracellular domain modifications affect tumor recognition by ROR1-specific chimeric antigen receptor T cells." *Clin Cancer Res* 19(12):3153-64, 2013. PMID **23620405** — use this instead.

---

*This document supplements `18_Experimental_Design_Expert_Review.md`. All claims about published literature have been web-verified against PubMed where indicated; uncertain entries are flagged.*
