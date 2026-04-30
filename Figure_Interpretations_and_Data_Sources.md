# Figure Interpretations and Data Sources

## DAC Meeting — Complete Figure Guide
### Manpreet Kour | PI: Dr. Kausik Chakraborty | CSIR-IGIB

---

**IMPORTANT NOTE:** All figures in this presentation are **schematic illustrations** created to communicate published concepts and data trends. They are NOT direct reproductions of published figures. The specific data points, numerical values, and conceptual frameworks depicted are drawn from the peer-reviewed sources cited below. Where exact published values are used, they are noted. Where curve shapes are illustrative of reported trends, this is explicitly stated.

---

## Figure 1: Catch Bond vs Slip Bond Behavior in TCR-pMHC Interaction

**File:** `figures/catch_vs_slip_bond.png`

### What the Figure Shows
Two force-lifetime curves for TCR-pMHC bonds:
- **Blue solid line (Catch Bond — Agonist):** Bond lifetime first increases with applied force, reaches a peak at ~10 pN, then decreases. This biphasic behavior is the defining characteristic of a catch bond.
- **Red dashed line (Slip Bond — Antagonist):** Bond lifetime monotonically decreases with increasing force. This is the conventional/intuitive bond behavior.

### Data Source and Basis

**Primary source:** Liu B, Chen W, Evavold BD, Zhu C. "Accumulation of dynamic catch bonds between TCR and agonist peptide-MHC triggers T cell signaling." *Cell*. 2014;157(2):357-368.

**What Liu et al. actually measured:**
- Used a biomembrane force probe (BFP) to apply defined forces (0-20+ pN) to individual TCR-pMHC bonds on live OT-1 T cells
- Measured bond lifetime (time until dissociation) at each force level
- Tested a panel of altered peptide ligands of varying potency presented by H-2Kb MHC:
  - **OVA** (SIINFEKL): Strong agonist → formed catch-slip bonds (biphasic lifetime curve, peak at ~10 pN)
  - **A2**: Intermediate agonist → formed catch-slip bonds (smaller peak)
  - **G4**: Weak agonist → formed catch-slip bonds (even smaller peak)
  - **R4**: Antagonist → formed slip-only bonds (monotonic decrease)
  - **E1**: Antagonist → formed slip-only bonds (monotonic decrease)

**What is illustrative vs exact in our figure:**
- **ILLUSTRATIVE:** The exact curve shapes are schematic representations of the biphasic (catch) and monotonic (slip) behaviors. They are not plotted from the raw numerical data in Liu et al.
- **FROM THE DATA:** The peak force of ~10 pN is directly from the paper. The qualitative distinction between biphasic (agonist) and monotonic (antagonist) curves faithfully represents the published findings.
- **FROM THE DATA:** The annotations "Force STRENGTHENS agonist bonds" and "Force WEAKENS antagonist bonds" are direct conclusions from the paper.

### Interpretation

This figure demonstrates that TCR-pMHC is not a simple lock-and-key interaction — it is a mechanosensitive bond whose behavior changes under force. The mechanical environment of the T cell-APC interface (where actin-generated forces of ~10 pN are applied) acts as a "quality control" mechanism: agonist peptides that drive productive T cell activation form catch bonds that are reinforced by force, while antagonist peptides that should NOT activate T cells form slip bonds that are disrupted by force. This provides an elegant mechanism for antigen discrimination that operates on top of the zero-force kinetic discrimination provided by kinetic proofreading.

**Additional supporting reference:** Pettmann J, et al. "Catch bond models may explain how force amplifies TCR signaling and antigen discrimination." *Nat Commun*. 2023;14:2346.

---

## Figure 2: TCR Affinity Windows — Thymic Selection and Antigen Categories

**File:** `figures/affinity_windows.png`

### What the Figure Shows
A horizontal bar diagram showing TCR-pMHC affinity (KD) on a log scale, divided into functional zones:
- **Gray (>300 microM):** Death by neglect — TCRs too weak to bind self-pMHC
- **Green (100-300 microM):** Positive selection — TCRs that survive thymic development
- **Yellow (20-100 microM):** Transition zone — outcome depends on context
- **Orange (~6-20 microM):** Negative selection zone
- **Red (<6 microM):** Strong agonist / deletion — TCRs deleted in thymus

Below, arrows indicate where different antigen categories fall on this scale.

### Data Source and Basis

**Thymic selection thresholds:**
- **Primary source:** Juang J, Ebert PJR, Feng D, et al. "Peptide-MHC heterodimers show that thymic positive selection requires a more restricted set of self-peptides than negative selection." *J Exp Med*. 2010;207(6):1223-1234.
- **What they measured:** Using the OT-1 TCR system (specific for OVA/H-2Kb), they measured KD values for positively selecting self-peptides:
  - Catnb-Kb: **KD = 136 microM** (positively selecting)
  - Cappa1-Kb: **KD = 211 microM** (positively selecting)
  - OVA-Kb: **KD = 8.7 microM** (negatively selecting agonist)
  - These are EXACT values from the paper

**"Danger zone" threshold (~6 microM):**
- **Source:** Hoffmann MM, Slansky JE. "T cell receptor affinity in the age of cancer immunotherapy." *Mol Carcinog*. 2020;59(7):862-870.
- They describe KD of ~6 microM as approximately the negative selection threshold for autoantigens

**Antigen category positions:**
- **Viral Ag (~10 microM):** Mean KD for TCRs recognizing viral antigens. Source: Hoffmann & Slansky, 2020 (same paper), stating "mean KD values of about 10 microM" for anti-microbial TCRs
- **Tumor Self-Ag (~100 microM):** Mean KD for TCRs against tumor-associated self-antigens. Source: Hoffmann & Slansky, 2020, stating "mean KD values of about 100 microM" for tumor self-antigen TCRs
- **Autoimmune (>200 microM):** Based on measured affinities of autoimmune TCRs like Ob.1A12 (KD >100 microM for MBP-DR2a). Source: Hahn M, et al. "Unconventional topology of self peptide-MHC binding by a human autoimmune T cell receptor." *Nat Immunol*. 2005;6(5):490-496.
- **CAR scFv (~1-10 nM):** Typical scFv affinity range. Source: Stone et al., 2009; Park et al., 2017

**What is illustrative vs exact:**
- **EXACT:** The KD values for Catnb-Kb (136 microM), Cappa1-Kb (211 microM), and OVA-Kb (8.7 microM) are directly from Juang et al., 2010
- **EXACT:** The mean KD values (~10 microM for viral, ~100 microM for tumor) are from Hoffmann & Slansky, 2020
- **ILLUSTRATIVE:** The exact boundaries of the colored zones are approximate, reflecting the continuum nature of thymic selection. The transition zone boundaries are not precisely defined in any single paper.

### Interpretation

This figure illustrates that TCR affinity is not a single value but a spectrum with distinct functional zones. The thymic selection window (100-300 microM for positive, <6-10 microM for negative) creates a "permitted range" of ~10-100 microM for mature T cells recognizing foreign antigens. Tumor-associated antigen TCRs have ~10-fold lower affinity than viral TCRs because high-affinity self-reactive clones were deleted in the thymus. The enormous gap between natural TCR affinity (micromolar) and CAR scFv affinity (nanomolar) highlights the "affinity mismatch problem" central to this project.

---

## Figure 3: The Optimal Dwell Time ("Goldilocks") Concept

**File:** `figures/optimal_dwell_time.png`

### What the Figure Shows
A bell-shaped curve showing T cell activation (y-axis) as a function of TCR-pMHC dwell time/half-life (x-axis), with three colored zones:
- **Red zone (<10 s):** Too short — kinetic proofreading incomplete
- **Green zone (~20-50 s):** Optimal — peak activation
- **Orange zone (>60 s):** Too long — serial engagement blocked

### Data Source and Basis

**Primary source:** Kalergis AM, Boucheron N, Cardenas MA, et al. "Efficient T cell activation requires an optimal dwell-time of interaction between the TCR and the pMHC complex." *Nat Immunol*. 2001;2(3):229-234.

**What Kalergis et al. actually measured:**
- Used a panel of TCR-pMHC complexes with different measured half-lives
- Assessed CD8+ T cell cytotoxic function (granule secretion, tumor killing) in vivo
- Key quantitative findings:
  - **t1/2 ≤ 10.3 seconds:** Did NOT induce efficient cytotoxic granule secretion or tumor killing
  - **t1/2 = 34 seconds:** MAXIMUM cytotoxic activity — optimal dwell time
  - **t1/2 = 77 seconds:** IMPAIRED function — too long
  - These three data points are EXACT values from the paper

**What is illustrative vs exact:**
- **EXACT:** The three data points (10.3s = poor, 34s = optimal, 77s = impaired) are directly from Kalergis et al., 2001
- **ILLUSTRATIVE:** The smooth bell-shaped curve connecting these points is schematic. The paper reports discrete data points, not a continuous function. The curve is drawn as a Poisson-like distribution peaking at 34s to illustrate the concept.
- **EXACT:** The green dashed line at x=34 and the annotation "Optimal t1/2 ≈ 34 s" are from the paper

### Interpretation

This figure demonstrates that T cell activation is NOT a simple monotonic function of binding strength. Both too-weak and too-strong binding impair function. This bell-shaped relationship arises from the tension between two requirements: kinetic proofreading (which needs sufficient dwell time to complete sequential phosphorylation steps) and serial engagement (which needs the pMHC to dissociate and engage additional TCRs). The optimal dwell time of ~34 seconds represents the best compromise between these two competing demands. This concept is directly relevant to CAR-T design: supraphysiological scFv affinity may push the dwell time far to the right of the optimum, impairing function.

**Additional reference:** Colf LA, et al. "The Goldilocks Model for TCR — Too Much Attraction Might Not Be Best for Vaccine Design." *PLoS Biol*. 2010;8(9):e1000482.

---

## Figure 4: Experimental Design Workflow

**File:** `figures/experimental_workflow.png`

### What the Figure Shows
An 8-step experimental workflow flowchart:
Step 1 → Step 2 → Step 3 → Step 4 → Step 5 → Step 6 → Step 7 → Step 8

### Data Source and Basis

This figure is **entirely project-specific** — it depicts the experimental plan designed for this PhD project. It is not based on any external published data.

**The steps are derived from the project proposal (projectproposal.pptx) and refined based on the literature review:**
- Steps 1-3: CAR construct design, residue identification, mutagenesis (from project proposal slides 30-39)
- Steps 4-5: Functional screening with Raji co-culture (from project proposal slides 51-56)
- Steps 6-7: Cloning, purification, kinetic characterization (from project proposal slides 57-61)
- Step 8: Data integration (novel contribution of this project)

### Interpretation

The workflow shows the systematic approach: start with structural information, create a comprehensive mutant library, screen for functional phenotypes, then correlate function with binding kinetics. The key innovation is the final step — creating a quantitative link between specific kinetic parameters (KD, kon, koff) and specific functional outcomes (cytotoxicity, exhaustion, memory) — which has not been done systematically for anti-CD19 CARs.

---

## Figure 5: Affinity Comparison — Natural TCR vs CAR scFv

**File:** `figures/car_vs_tcr_affinity.png`

### What the Figure Shows
A bar chart comparing KD values (on a log scale) for four receptor-antigen systems:
1. Natural TCR for foreign Ag: ~10 microM
2. Natural TCR for tumor self-Ag: ~100 microM
3. FMC63 scFv (anti-CD19 CAR): ~1 nM (0.001 microM)
4. Optimal CAR affinity window: ~500 nM (0.5 microM)

### Data Source and Basis

**Bar 1 — Natural TCR for foreign Ag (~10 microM):**
- Source: Stone JD, Chervin AS, Kranz DM. "T-cell receptor binding affinities and kinetics." *Immunology*. 2009;126(2):165-176.
- Specifically: "TCRs have relatively low affinities for their pepMHC ligands" with values spanning "1-100 microM." The mean for CD8+ TCRs recognizing foreign Ag is ~13 microM (Aleksic et al., 2007). We use ~10 microM as a round representative value.

**Bar 2 — Natural TCR for tumor self-Ag (~100 microM):**
- Source: Hoffmann MM, Slansky JE. *Mol Carcinog*. 2020;59(7):862-870.
- Directly states: "mean KD values of about 100 microM" for tumor self-antigen TCRs

**Bar 3 — FMC63 scFv (~1 nM):**
- Source: The FMC63 antibody has a reported affinity for CD19 in the sub-nanomolar to low nanomolar range. The exact KD varies by measurement method and conditions. We use ~1 nM as a representative value based on published BLI/SPR data.
- Supporting source: Ghorashian S, et al. "Enhanced CAR T cell expansion and prolonged persistence in pediatric patients with ALL treated with a low-affinity CD19 CAR." *Nat Med*. 2019;25:1408-1414. (Describes FMC63 as "high-affinity" with the comparison CAT scFv having "40-fold lower affinity")

**Bar 4 — Optimal CAR affinity window (~500 nM):**
- Source: Park S, et al. "Micromolar affinity CAR T cells to ICAM-1 achieves rapid tumor elimination while avoiding systemic toxicity." *Sci Rep*. 2017;7:14366.
- The emerging literature suggests that the optimal CAR affinity may be in the high nanomolar to low micromolar range (~100 nM - 1 microM). The 500 nM value is a representative mid-point of this proposed window.
- **CAVEAT:** This "optimal window" is still under investigation and is not firmly established. We present 500 nM as illustrative of the emerging consensus, not as a definitive value.

### Interpretation

The dramatic affinity gap between natural TCRs (micromolar) and CARs (nanomolar) is at the heart of this project. Natural TCR affinity evolved under selection pressure to balance sensitivity, specificity, and serial engagement. CARs bypass this selection and operate with 1,000-1,000,000-fold higher affinity, which may actually impair function by blocking serial engagement, promoting exhaustion, and enabling off-tumor toxicity. The "optimal CAR window" (emerging evidence) suggests that reducing CAR affinity toward the micromolar range may improve therapeutic outcomes.

---

## Figure 6: Kinetic Proofreading in TCR Signal Transduction

**File:** `figures/kinetic_proofreading.png`

### What the Figure Shows
A linear cascade of 5 boxes representing sequential steps in TCR signal transduction:
TCR+pMHC Binding → CD3zeta ITAM Phosphorylation → ZAP-70 Recruitment → LAT/SLP-76 Phosphorylation → SIGNAL OUTPUT

Red arrows from each box pointing upward represent pMHC dissociation (resetting the signal to zero).

### Data Source and Basis

**Primary source:** McKeithan TW. "Kinetic proofreading in T-cell receptor signal transduction." *Proc Natl Acad Sci USA*. 1995;92(11):5042-5046.

**What McKeithan proposed:**
- The TCR complex undergoes multiple modifications (tyrosine phosphorylation steps) after ligand binding but before transmitting a signal
- Each step acts as a checkpoint: if the pMHC dissociates before completion, ALL modifications revert to the unmodified state
- N sequential steps amplify differences in koff exponentially by a factor of approximately koff^N
- This is analogous to the kinetic proofreading in DNA replication (Hopfield, 1974; Ninio, 1975)

**The specific signaling molecules shown (CD3zeta, ZAP-70, LAT, SLP-76):**
- These represent the known proximal TCR signaling cascade
- Source: Shah K, et al. "T cell receptor signaling in health and disease." *Signal Transduct Target Ther*. 2021;6:412.

**Experimental validation:**
- Source: Torigoe C, et al. "Kinetic proofreading through the multi-step activation of the ZAP70 kinase underlies early T cell ligand discrimination." *Nat Immunol*. 2022;23:1045-1056.
- They demonstrated that the discrimination power (ability to distinguish agonist from non-agonist) increases progressively from receptor proximal (TCR phosphorylation) to more distal events (DAG generation), exactly as predicted by kinetic proofreading.

**What is illustrative vs exact:**
- **FROM THE MODEL:** The concept of sequential steps with dissociation-reset is directly from McKeithan, 1995
- **FROM KNOWN BIOLOGY:** The specific molecules at each step are established signaling components
- **ILLUSTRATIVE:** The linear arrangement and equal-sized boxes are schematic; the actual signaling cascade involves branching, feedback, and spatial organization

### Interpretation

Kinetic proofreading explains the extraordinary specificity of T cell antigen discrimination. By requiring multiple sequential steps before signal transmission, the system exponentially amplifies small differences in binding kinetics between self-peptides (which dissociate quickly) and foreign peptides (which remain bound longer). This model also predicts the importance of koff over KD — it is the rate of dissociation, not the equilibrium binding strength, that determines whether the proofreading cascade can be completed before the ligand dissociates.

---

## Figure 7: TCR Organization at the Immunological Synapse

**File:** `figures/tcr_synapse_organization.png`

### What the Figure Shows
A top-down (en face) schematic of the immunological synapse showing three concentric rings:
- **Outer ring (green, dSMAC):** Distal SMAC, actin-rich
- **Middle ring (orange, pSMAC):** Peripheral SMAC, LFA-1/ICAM-1 adhesion
- **Inner circle (red, cSMAC):** Central SMAC, TCR accumulation and signal termination

Blue dots in the pSMAC region represent TCR microclusters with arrows showing centripetal movement.

### Data Source and Basis

**SMAC organization:**
- Source: Monks CR, Freiberg BA, Kupfer H, Sciaky N, Kupfer A. "Three-dimensional segregation of supramolecular activation clusters in T cells." *Nature*. 1998;395(6701):82-86.
- They first described the bull's-eye SMAC organization of the immunological synapse

**Microcluster dynamics:**
- Source: Campi A, Varma R, Dustin ML. "Actin and agonist MHC-peptide complex-dependent T cell receptor microclusters as scaffolds for signaling." *J Exp Med*. 2005;202(8):1031-1036.
- Source: Varma R, Campi A, Yokosuka T, Dustin ML. "T cell receptor-proximal signals are sustained in peripheral microclusters and terminated in the central supramolecular activation cluster." *Immunity*. 2006;25(1):117-127.
- Key findings used in the figure:
  - Microclusters form at the periphery (represented by blue dots in the pSMAC)
  - Active signaling occurs in peripheral microclusters, NOT in the cSMAC
  - Microclusters move centripetally (shown by gray arrows) via actin retrograde flow
  - cSMAC is a site of signal termination and TCR degradation

**Microcluster composition:**
- Source: Crites TJ, et al. "TCR Microclusters Preexist and Contain Molecules Necessary for TCR Signal Transduction." *J Immunol*. 2014;193(1):56-67.
- Each microcluster contains ~100 TCR molecules (range 50-300)

**What is illustrative:**
- The specific positions and number of blue dots are schematic — actual synapse images show variable microcluster distributions
- The concentric ring boundaries are idealized; real synapses show more irregular borders

### Interpretation

The immunological synapse is not simply a "connection point" between T cell and APC — it is a highly organized signaling platform with spatial regulation. The critical insight is that active signaling occurs in peripheral microclusters, while the cSMAC serves to terminate signaling and internalize TCRs. This means sustained T cell activation depends on the continuous formation of new peripheral microclusters, not on the cSMAC. This spatial organization is directly relevant to CAR-T cells, which form a disorganized, "nonclassical" synapse (Davenport et al., 2018) that lacks the canonical SMAC organization.

---

## Figure 8: From pMHC Binding to T Cell Function (Signaling Cascade)

**File:** `figures/signaling_cascade.png`

### What the Figure Shows
A vertical cascade of 8 sequential steps from pMHC binding at the top to functional outcomes at the bottom, with four functional outcome boxes at the base.

### Data Source and Basis

This is a **composite model** integrating findings from multiple published sources:

| Step in Figure | Source |
|---------------|--------|
| pMHC binds TCR (KD, kon, koff) | Stone et al., 2009, *Immunology* |
| Mechanical force (~10 pN) | Liu Y et al., 2016, *PNAS* 113:5610 (DNA tension probes) |
| Catch bond vs slip bond | Liu B et al., 2014, *Cell* 157:357 |
| Cbeta FG loop change | Brazin et al., 2015, *PNAS* 112:E4228 |
| ITAM exposure | Kim et al., 2009, *JBC* 284:31028 |
| ZAP-70 → LAT → SLP-76 → PLCgamma | Shah et al., 2021, *Signal Transduct Target Ther* |
| Kinetic proofreading | McKeithan, 1995, *PNAS* 92:5042 |
| Ca2+, NFAT, NF-kappaB, AP-1 | Standard immunology textbooks; Hogan et al., 2003 |
| Functional outcomes | Composite from multiple CAR-T studies |

**What is illustrative:**
- The entire figure is a conceptual model showing the logical flow from binding to function
- The specific ordering of steps reflects current understanding but the actual signaling cascade involves extensive branching, feedback, and parallel pathways
- The 10 pN force value is from Liu et al., 2016

### Interpretation

This figure provides a conceptual framework for understanding how binding parameters ultimately determine T cell functional outcomes. Each step in the cascade represents a point where the binding kinetics of the TCR/CAR-pMHC/antigen interaction can influence the outcome. The key message is that binding kinetics do not simply determine "on or off" activation — they determine the quality and magnitude of signaling, which then determines whether the functional outcome is cytotoxicity, memory formation, or exhaustion.

---

## Figure 9: Serial Engagement Model

**File:** `figures/serial_engagement.png`

### What the Figure Shows
A time-series schematic showing a single pMHC molecule (red triangle) on the APC surface sequentially engaging multiple TCRs (blue triangles) on the T cell surface. Green lines show active engagements, and red dashed arrows show the pMHC moving to the next TCR.

### Data Source and Basis

**Primary source:** Valitutti S, Muller S, Cella M, Padovan E, Lanzavecchia A. "Serial triggering of many T-cell receptors by a few peptide-MHC complexes." *Nature*. 1995;375(6527):148-151.

**What Valitutti et al. actually showed:**
- When T cells interacted with APCs displaying ~100 pMHC molecules, up to 18,000 TCRs were triggered (downregulated) per T cell
- This implies each pMHC serially engaged ~200 TCRs (18,000/100)
- The serial engagement was possible because of the low affinity (fast koff) of TCR-pMHC interactions
- TCR downregulation was used as a proxy for triggering
- **EXACT values from paper:** ~100 pMHC per APC, up to 18,000 TCRs triggered, ~200 TCRs per pMHC

**Review/update of the model:**
- Source: Valitutti S. "The Serial Engagement Model 17 Years After." *Front Immunol*. 2012;3:272.
- Discusses refinements, criticisms (TCR co-modulation overestimation), and the relationship with kinetic proofreading

**What is illustrative:**
- The figure shows 4 sequential engagements for visual clarity; the actual number is ~200
- The APC and T cell "surfaces" are simplified flat lines; actual interfaces are complex 3D structures with microvilli
- The spacing and timing of engagements are schematic

### Interpretation

The serial engagement model elegantly explains how a T cell can be activated by as few as 1-10 pMHC molecules on an APC — a remarkable sensitivity problem. The key insight is that the "weakness" of TCR-pMHC binding (fast koff) is actually a feature, not a bug: it allows each pMHC to serially trigger many TCRs, amplifying the signal. This creates the optimal dwell time concept: too-fast koff means no single TCR completes proofreading, but too-slow koff means serial engagement is blocked. For CARs with nanomolar affinity (very slow koff), serial engagement may be severely impaired, potentially explaining why lower-affinity CARs can outperform higher-affinity ones.

---

## Summary Table: Figure Type Classification

| Figure | Type | Primary Data Source | Quantitative Values Used |
|--------|------|-------------------|--------------------------|
| 1. Catch vs Slip Bond | Schematic of published trend | Liu et al., 2014, Cell | Peak force ~10 pN; OT-1 system peptide panel |
| 2. Affinity Windows | Data-based schematic | Juang et al., 2010; Hoffmann & Slansky, 2020 | KD: 136, 211, 8.7 microM (exact); ~10, ~100 microM (means from review) |
| 3. Optimal Dwell Time | Schematic of published data | Kalergis et al., 2001, Nat Immunol | t1/2: 10.3, 34, 77 seconds (exact from paper) |
| 4. Experimental Workflow | Project-specific design | Original (this project) | N/A |
| 5. CAR vs TCR Affinity | Data-based comparison | Stone et al., 2009; Hoffmann & Slansky, 2020; Park et al., 2017 | KD values from cited reviews |
| 6. Kinetic Proofreading | Conceptual model | McKeithan, 1995, PNAS | Model concept; signaling molecules from standard immunology |
| 7. TCR Synapse | Schematic of published model | Campi et al., 2005; Varma et al., 2006; Crites et al., 2014 | ~100 TCRs per microcluster; SMAC organization |
| 8. Signaling Cascade | Composite conceptual model | Multiple sources (see table above) | 10 pN force from Liu et al., 2016 |
| 9. Serial Engagement | Schematic of published model | Valitutti et al., 1995, Nature | ~200 TCRs per pMHC, ~18,000 TCRs triggered (exact) |

---

## Key Distinction for the PI

**These figures are NOT reproductions of published figures.** They are original schematic illustrations created to communicate concepts and data from the cited papers. When presenting:

1. **Always state:** "This is a schematic representation based on data from [Author] et al., published in [Journal] in [Year]"
2. **For specific numbers:** "The value of [X] is taken directly from [Author] et al."
3. **For curve shapes:** "The curve shape is illustrative of the [biphasic/monotonic/bell-shaped] behavior reported by [Author] et al."
4. **Never claim** these are reproductions or direct data plots from the cited papers

If the PI asks to see the original figures, refer to the cited papers directly — all are available through PubMed Central or journal websites.

---

## Session 2 Figures (Added 2026-04-27)

### Figure 10: fmc63_variant_affinities.png
**What it shows:** Bar chart comparing published KD values for FMC63 wild-type and three alanine mutants at key contact residues.
**Data source:** He et al., 2023, *Science Immunology* 8:eadf1426 (PMC10228544). WT KD confirmed by Seigner et al., 2023, *Sci Rep* 13:23024 (PMC10754921).
**Exact values plotted:**
- FMC63 WT: KD = 5.1 nM (Seigner) / 4.5 nM (He) — plotted as 5.1 nM
- FMC63-Y70A: KD = 275.3 nM (54-fold weaker)
- FMC63-Y261A: KD = 682.5 nM (134-fold weaker)
- FMC63-Y260A: No detectable SPR binding — plotted as >5000 nM (lower bound)
**Status:** Bar heights are EXACT published values. Y260A is a lower-bound estimate since no binding was detected.

### Figure 11: antigen_density_threshold.png
**What it shows:** Antigen density (CD19 molecules/cell) vs relative CAR-T function for CD28ζ and 4-1BBζ CARs.
**Data source:** Majzner RG et al., *Cancer Discovery* 10(5):702-723, 2020 (PMC7939454).
**Exact values from paper:** CD19 densities of 45, 963, 2,053, and 45,851 molecules/cell were generated by CRISPR-KO + graded re-expression of NALM-6. The ~2,000 molecules/cell activation threshold is directly reported.
**Status:** Bar heights are SCHEMATIC representations of the relative functional differences reported — NOT exact numerical reproductions. The trend (CD28ζ > 4-1BBζ at low density; both high at max density; threshold ~2,000 mol/cell) is directly from the paper.

### Figure 12: platform_comparison.png
**What it shows:** Side-by-side comparison table of 5 biophysical platforms (SPR, BLI, MST, ITC, flow cytometry).
**Data sources:** Cytiva Biacore product specs, Sartorius Octet specs, NanoTemper Monolith specs, Malvern MicroCal specs. Cost estimates from Excedr.com blog, NIH S10 equipment grants, vendor documentation.
**Status:** All values are factual specifications from manufacturer documentation. Cost ranges are estimates from multiple sources, not exact quotes.

### Figure 13: facs_panel_summary.png
**What it shows:** Four FACS panel configurations with specific antibody clones, fluorochromes, and vendors.
**Data sources:** All antibody clones and catalog numbers verified via vendor product pages — BioLegend (biolegend.com), Miltenyi Biotec (miltenyibiotec.com), Thermo Fisher/eBioscience (thermofisher.com).
**Verified catalog numbers:** PD-1 PE EH12.2H7 (329906), CD107a PE H4A3 (328608), TOX PE TXRX10 (12-6502-82), anti-FMC63 REA1297 PE (130-127-342).
**Status:** All information is factual and vendor-verified.

### Figure 14: screening_strategy.png
**What it shows:** Three-phase NNK library screening workflow — single-position → combinatorial → kinetic characterization.
**Data source:** Coverage calculations from Pines et al., 2022, *Synth Biol* (PMC9205323). The ~94 clones for 95% coverage of 20 amino acids from a single NNK position is a direct calculation from the paper.
**Status:** Workflow is the project's planned experimental approach. Clone numbers are calculated, not fabricated.

---

**SVG versions:** All figures from both sessions are now available in SVG format in the figures/ directory for future editing. Python generation scripts (gen_batch1.py, gen_batch2.py, gen_batch3.py, gen_new_figures.py) are included for reproducibility.
