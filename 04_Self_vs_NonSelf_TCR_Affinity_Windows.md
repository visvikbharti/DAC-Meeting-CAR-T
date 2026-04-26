# Self vs. Non-Self: TCR Affinity Windows and Implications

## A Comprehensive Review for DAC Meeting
### Manpreet Kour | PI: Dr. Kausik Chakraborty | CSIR-IGIB

---

## 1. TCR Affinity Windows in Thymic Selection

### 1.1 The Thymic Selection Paradigm

T cell development in the thymus involves a quality control process that selects for TCRs within a specific affinity window for self-pMHC:

- **No/negligible binding (death by neglect):** Thymocytes whose TCRs fail to bind any self-pMHC die by apoptosis (~95% of all thymocytes)
- **Weak-to-moderate binding (positive selection):** TCRs that bind self-pMHC with sufficient but not excessive affinity receive survival signals and mature
- **Strong binding (negative selection):** TCRs that bind self-pMHC too strongly are deleted (clonal deletion) or diverted to regulatory T cell lineage

### 1.2 Quantitative Affinity Thresholds

Based on verified experimental data:

| Selection Outcome | KD Range | Key Evidence |
|------------------|----------|-------------|
| **Positive selection** | ~100-300 microM | Catnb-Kb (KD ~136 microM) and Cappa1-Kb (KD ~211 microM) promote positive selection of OT-1 thymocytes |
| **Transition zone** | ~20-60 microM | Intermediate affinity; outcome depends on co-receptor (CD4 vs CD8) and avidity |
| **Negative selection** | < ~6-10 microM | OVA-Kb agonist (KD ~8.7 microM) drives negative selection of OT-1 thymocytes |
| **"Danger zone"** | ~6 microM | Approximately the negative selection threshold for autoantigens |

**Key quantitative comparisons from the OT-1 system:**
- Positively selecting peptides: Catnb-Kb has 15.6-fold lower affinity than OVA-Kb; Cappa1-Kb has 24.3-fold lower affinity
- This demonstrates a clear quantitative gap between the affinity of positively selecting (self) and negatively selecting (agonist foreign) ligands

**Key Reference:** Juang J, Ebert PJR, Feng D, et al. "Peptide-MHC heterodimers show that thymic positive selection requires a more restricted set of self-peptides than negative selection." *J Exp Med*. 2010;207(6):1223-1234.

**Key Reference:** Contan C, et al. "Affinity of thymic self-peptides for the TCR determines the selection of CD8+ T lymphocytes in the thymus." *Int Immunol*. 2000;12(9):1353-1364.

### 1.3 CD4 vs. CD8 T Cell Selection Differences

The affinity window differs between CD4+ and CD8+ T cells:

| Parameter | CD8+ T cells (Class I) | CD4+ T cells (Class II) |
|-----------|----------------------|----------------------|
| **Average mature TCR KD for foreign Ag** | 13 +/- 11 microM | 52 +/- 33 microM |
| **Selection window** | Narrower, higher affinity | Broader, lower affinity |
| **CD8/CD4 coreceptor effect** | CD8 enhances binding, narrows window | CD4 provides less enhancement |

CD8+ T cells have TCRs with approximately 4-fold higher average affinity for pMHC than CD4+ T cells, reflecting differences in coreceptor contribution and the structural constraints of MHC Class I vs. Class II recognition.

**Key Reference:** Aleksic M, Liddy N, et al. "Human TCR-Binding Affinity is Governed by MHC Class Restriction." *J Immunol*. 2007;178(9):5727-5734.

---

## 2. Affinity of Mature T Cells for Foreign Antigens

### 2.1 Typical KD Ranges by Antigen Category

| Antigen Category | Typical KD Range | Notes |
|-----------------|-----------------|-------|
| **Viral antigens (acute)** | 1-50 microM | Generally higher affinity; robust negative selection removes only the strongest |
| **Viral antigens (chronic)** | 1-100 microM | Broader range; includes lower affinity clones |
| **Bacterial antigens** | 1-100 microM | Comparable to viral |
| **Tumor-associated antigens (self-derived)** | 50-200+ microM | Low affinity due to thymic tolerance |
| **Tumor neoantigens (mutated)** | 1-50 microM | Higher affinity; not subject to central tolerance |
| **Autoimmune TCRs (escaped tolerance)** | >100-200+ microM | Very low affinity |

### 2.2 Why Tumor Antigen-Specific T Cells Have Lower Affinity

Most tumor-associated antigens (TAAs) are derived from overexpressed or aberrantly expressed self-proteins (e.g., NY-ESO-1, MAGE-A3, gp100, MART-1). Because these peptides are presented in the thymus during T cell development:

1. **High-affinity TCRs are deleted:** T cells with strong binding to self-derived tumor peptides are eliminated by negative selection
2. **Only low-affinity escapees survive:** Peripheral T cells against tumor-associated self-peptides that escape negative selection exhibit lower average affinities --- mean KD values of approximately 100 microM compared to approximately 10 microM for viral antigens
3. **Functional consequence:** These low-affinity T cells often fail to mount effective anti-tumor responses without therapeutic intervention

**The "affinity gap" for tumor immunity:**
- Mean KD for viral antigen TCRs: ~10 microM
- Mean KD for tumor self-antigen TCRs: ~100 microM
- This 10-fold difference in affinity translates to significant differences in T cell functional potency

**Key Reference:** Hoffmann MM, Slansky JE. "T cell receptor affinity in the age of cancer immunotherapy." *Mol Carcinog*. 2020;59(7):862-870.

**Key Reference:** Zhong S, et al. "TCR affinity for p/MHC formed by tumor antigens that are self-proteins: impact on efficacy and toxicity." *Curr Opin Immunol*. 2015;33:16-22.

### 2.3 Specific TCR-pMHC Affinity Examples from the Literature

**Verified quantitative affinity data from published SPR studies:**

| TCR | pMHC | KD (microM) | koff (s-1) | Category | Reference |
|-----|------|-------------|-----------|----------|-----------|
| OT-1 | OVA/H-2Kb | ~8.7 | - | Agonist model | Juang et al., 2010 |
| OT-1 | Catnb/H-2Kb | ~136 | - | Positively selecting self | Juang et al., 2010 |
| OT-1 | Cappa1/H-2Kb | ~211 | - | Positively selecting self | Juang et al., 2010 |
| 2C | dEV8/Kb | ~80 | - | Weak self-reactive | Stone et al., 2009 |
| m6alpha | QL9/Ld | 0.005 (5 nM) | - | Engineered high-affinity | Stone et al., 2009 |
| Ob.1A12 | Self-peptide/MHC | >100 | - | Autoimmune (escaped) | Wucherpfennig lab |
| 3A6 | Self-peptide/MHC | >200 | - | Autoimmune (escaped) | Wucherpfennig lab |

**Note:** The range from 5 nM (engineered) to >200 microM (autoimmune) spans approximately 5 orders of magnitude, illustrating the enormous range of TCR-pMHC binding strengths.

**Key Reference:** Stone JD, Chervin AS, Kranz DM. "T-cell receptor binding affinities and kinetics: impact on T-cell activity and specificity." *Immunology*. 2009;126(2):165-176.

---

## 3. The Affinity Ceiling Concept

### 3.1 Beyond an Optimal Affinity, Function Declines

Increasing TCR affinity does not monotonically improve T cell function. Instead, there exists an "affinity ceiling" beyond which:

1. **Function plateaus:** Additional increases in binding strength do not further enhance cytotoxicity, cytokine production, or proliferation
2. **Function can decrease:** Supraphysiological affinity may actually impair T cell responses through:
   - Loss of peptide specificity (increased cross-reactivity)
   - Impaired serial engagement (too-slow off-rate prevents serial triggering)
   - Enhanced exhaustion susceptibility in chronic antigen settings
   - Activation-induced cell death

### 3.2 The MAGE-A3 Catastrophe: A Cautionary Tale

The dangers of supraphysiological TCR affinity were dramatically illustrated by the fatal outcome of an anti-MAGE-A3 engineered TCR clinical trial:

- An affinity-enhanced TCR targeting MAGE-A3 was engineered for adoptive T cell therapy
- The enhanced affinity broadened cross-reactivity to structurally similar peptides
- The engineered TCR cross-reacted with a peptide from the cardiac protein titin, expressed in heart muscle
- This resulted in fatal cardiac inflammation (cardiomyopathy)
- The tragedy underscored that affinity enhancement beyond the natural range carries risks of loss of specificity

**This demonstrates that the thymic selection window (1-100 microM) is not merely a developmental constraint but reflects an optimized range for balancing sensitivity and specificity.**

### 3.3 Optimal Affinity for Anti-Tumor Responses

Based on accumulating evidence, the optimal affinity for TCR-mediated anti-tumor immunity appears to be:

- **For tumor-associated self-antigens:** A KD of approximately 10 microM has been identified as the optimal affinity threshold --- strong enough for effective function but not so strong as to cause unacceptable autoimmunity
- **For engineered TCRs:** Enhanced-affinity murine TCRs for tumor/self-antigens can be safe despite surpassing the negative selection threshold, but there is a narrow window of safety
- **The "danger zone":** KD of approximately 6 microM, near the negative selection threshold, represents a zone where autoreactivity risk increases sharply

**Key Reference:** Zhong S, et al. "Different affinity windows for virus and cancer-specific T-cell receptors: implications for therapeutic strategies." *Eur J Immunol*. 2012;42(10):2532-2541.

---

## 4. How Affinity Differences Impact Signaling and Function

### 4.1 Cytokine Production

TCR affinity/koff directly impacts the quality and quantity of cytokine production:

| Affinity | IL-2 | IFN-gamma | TNF-alpha | Notes |
|---------|------|-----------|-----------|-------|
| **High (agonist)** | Strong | Strong | Strong | Full effector program |
| **Intermediate** | Moderate | Strong | Moderate | Biased toward cytotoxicity |
| **Low (weak agonist)** | Weak/absent | Weak | Weak | Partial activation |
| **Very low (antagonist)** | None | None | None | May inhibit activation |

Altered peptide ligands that change koff (even when KD is similar) dramatically alter the cytokine production profile, demonstrating that kinetics, not just equilibrium binding, determines functional output.

### 4.2 Proliferation and Clonal Expansion

- Higher affinity TCRs generally drive more robust clonal expansion
- However, very high-affinity interactions can impair proliferation through activation-induced cell death (AICD)
- In chronic antigen settings (tumors, chronic infections), intermediate-affinity TCRs may sustain proliferation better than high-affinity TCRs that exhaust rapidly

### 4.3 Memory Differentiation

TCR affinity influences the balance between effector and memory differentiation:

- **Higher affinity:** Biases toward terminal effector differentiation
- **Lower affinity:** May favor memory precursor differentiation
- This has important implications for durable anti-tumor immunity, where memory formation is critical for preventing relapse

### 4.4 Exhaustion Susceptibility

Higher affinity TCR-pMHC interactions correlate with increased exhaustion susceptibility in chronic antigen settings:

- High-affinity T cells in the tumor microenvironment show enhanced expression of exhaustion markers (PD-1, TIM-3, LAG-3)
- This is likely due to stronger and more sustained signaling that drives the exhaustion transcriptional program
- The paradox: the T cells with the "best" affinity for tumor antigens may exhaust the fastest

---

## 5. Implications for CAR-T and Engineered TCR Therapy

### 5.1 The scFv Affinity vs. TCR Affinity Mismatch

| Parameter | Natural TCR | CAR scFv | Ratio |
|-----------|------------|----------|-------|
| **Typical KD** | 1-100 microM | 0.1-10 nM | 1,000-1,000,000x |
| **Typical koff** | 0.01-1 s-1 | 0.001-0.01 s-1 | 10-100x slower for CAR |
| **Bond type under force** | Catch bond (agonist) | Likely slip bond | Fundamentally different |

This orders-of-magnitude difference in binding strength means that CARs operate in a fundamentally different signaling regime than natural TCRs:

- **Prolonged engagement:** The slow off-rate of nanomolar scFvs means each CAR-antigen interaction persists much longer than a TCR-pMHC interaction
- **Blocked serial engagement:** The prolonged dwell time may prevent serial triggering of multiple CARs by the same antigen molecule
- **Tonic signaling risk:** Even in the absence of antigen, nanomolar-affinity scFvs may mediate weak tonic signaling through low-level cross-linking

### 5.2 Evidence That Reducing CAR Affinity Improves Outcomes

Multiple studies demonstrate that lower-affinity CARs can outperform higher-affinity versions:

**Anti-CD19 CAR (Ghorashian et al.):**
- CAT scFv: 40-fold lower affinity for CD19 than FMC63
- CAT-CAR T cells showed greater in vitro antigen-specific cytotoxicity and proliferation
- Confirmed in vivo with enhanced anti-leukemic effect in pediatric patients
- CAT mAb has similar kon as FMC63 but much higher koff
- The faster off-rate may contribute to memory T cell formation and polyfunctionality
- Commentary: "CD19 affinity --- is lower also better?" (*Nat Rev Clin Oncol*, 2019)

**Anti-ICAM-1 CAR (Park et al., 2017):**
- Micromolar affinity CAR T cells achieved rapid tumor elimination while avoiding systemic toxicity
- Superior anti-tumor efficacy AND safety compared to nanomolar counterparts in a solid tumor mouse model
- Demonstrates that micromolar affinity CARs can function effectively

**Anti-HER2 CAR (Liu et al.):**
- Low-affinity CAR-T cells moved from liver to high HER2-expressing tumor faster than high-affinity cells
- May contribute to better anti-tumor efficacy by improving biodistribution

**The emerging principle:** The dwell time and kinetics of antigen-binding domain engagement may be more important than KD in deciding the outcome of CAR-T therapy. Moderate-affinity CARs may better recapitulate the kinetic regime that natural TCRs operate in.

**Key Reference:** Ghorashian S, et al. discussed in: "CD19 affinity --- is lower also better?" *Nat Rev Clin Oncol*. 2019;16(5):278-281.

**Key Reference:** Park S, et al. "Micromolar affinity CAR T cells to ICAM-1 achieves rapid tumor elimination while avoiding systemic toxicity." *Sci Rep*. 2017;7:14366.

### 5.3 The Affinity Optimization Window for CARs

Based on current evidence, an "affinity optimization window" for CARs is emerging:

```
                   ← Increasing Affinity →

Too Weak        Optimal Range       Too Strong
(>10 microM)    (~100 nM - 1 microM)    (<1 nM)
     |                |                    |
     v                v                    v
Poor target     Efficient killing     Tonic signaling
recognition     Good persistence      Early exhaustion
No killing      Memory formation      Off-tumor toxicity
                Reduced toxicity      Blocked serial killing
```

This window is not absolute and depends on:
- Antigen density on target cells
- CAR design (costimulatory domains)
- Target antigen expression on normal tissues
- The specific disease context

---

## 6. Measuring TCR Affinity: Methods and Caveats

### 6.1 Three-Dimensional Methods (Solution-Phase)

**Surface Plasmon Resonance (SPR) --- Biacore:**
- Gold standard for 3D affinity measurement
- Provides KD, kon, koff
- Requires purified, soluble TCR and pMHC
- Limitation: Measures interactions in solution, not at cell membranes

**Bio-Layer Interferometry (BLI) --- Octet:**
- Label-free, real-time kinetics
- Higher throughput than SPR
- Can use unpurified samples and cell lysates (more native conditions)
- Orthogonal validation of SPR measurements

### 6.2 Two-Dimensional Methods (Membrane-Constrained)

**Micropipette Adhesion Frequency Assay:**
- Measures binding between receptors on live T cells and ligands on opposing cell/bead
- Provides 2D affinity (AcKa) and 2D koff
- Reveals dramatically different kinetics from 3D measurements (Huang et al., 2010)

**FRET-Based 2D Kinetics:**
- Measures TCR-pMHC binding and unbinding in real-time at cell-cell interfaces
- Provides 2D bond lifetimes

### 6.3 Indirect Affinity Measures

**pMHC Tetramer Staining:**
- Widely used in clinical and research settings
- Measures avidity (collective binding strength of multiple TCR-pMHC interactions)
- Influenced by TCR density, co-receptor contribution, and membrane organization
- Not a pure affinity measurement but correlates with it

**NTAmer Dissociation Assay:**
- Allows quantitative assessment of TCR-pMHC dissociation rates on living T cells
- NTAmers (reversibly multimeric pMHC) can be dissociated by imidazole
- Enables real-time koff measurement at the cell surface
- More physiologically relevant than solution-phase SPR

### 6.4 Why 2D and 3D Measurements Differ

The dramatic differences between 2D and 3D measurements arise from:

1. **Membrane confinement:** Restricting molecules to 2D membranes changes the encounter geometry and effective concentrations
2. **Molecular orientation:** Membrane anchoring constrains molecular orientation, affecting binding efficiency
3. **Co-receptors and accessory molecules:** 2D measurements capture the contribution of co-receptors (CD4/CD8) and adhesion molecules (LFA-1) that are absent in 3D SPR
4. **Mechanical forces:** 2D measurements at cell-cell interfaces include the effects of cytoskeletal forces on bond behavior

**The critical paradox:** In 2D, agonist pMHC dissociates the fastest (not the slowest), and the 2D on-rate, not the off-rate, is the best discriminator of agonist potency. This suggests that the "faster scanning and rebinding" of agonist pMHC, facilitated by rapid 2D on-rates, may be more important than prolonged individual bond lifetime.

---

## References

1. Juang J, Ebert PJR, Feng D, et al. Peptide-MHC heterodimers show that thymic positive selection requires a more restricted set of self-peptides than negative selection. *J Exp Med*. 2010;207(6):1223-1234.

2. Hoffmann MM, Slansky JE. T cell receptor affinity in the age of cancer immunotherapy. *Mol Carcinog*. 2020;59(7):862-870.

3. Stone JD, Chervin AS, Kranz DM. T-cell receptor binding affinities and kinetics: impact on T-cell activity and specificity. *Immunology*. 2009;126(2):165-176.

4. Aleksic M, Liddy N, et al. Human TCR-Binding Affinity is Governed by MHC Class Restriction. *J Immunol*. 2007;178(9):5727-5734.

5. Zhong S, et al. TCR affinity for p/MHC formed by tumor antigens that are self-proteins: impact on efficacy and toxicity. *Curr Opin Immunol*. 2015;33:16-22.

6. Zhong S, et al. Different affinity windows for virus and cancer-specific T-cell receptors: implications for therapeutic strategies. *Eur J Immunol*. 2012;42(10):2532-2541.

7. Contan C, et al. Affinity of thymic self-peptides for the TCR determines the selection of CD8+ T lymphocytes in the thymus. *Int Immunol*. 2000;12(9):1353-1364.

8. Ghorashian S, et al. CD19 affinity --- is lower also better? *Nat Rev Clin Oncol*. 2019;16(5):278-281.

9. Park S, et al. Micromolar affinity CAR T cells to ICAM-1 achieves rapid tumor elimination while avoiding systemic toxicity. *Sci Rep*. 2017;7:14366.

10. Huang J, Zarnitsyna VI, Liu B, et al. The kinetics of two-dimensional TCR and pMHC interactions determine T-cell responsiveness. *Nature*. 2010;464(7290):932-936.

11. Hebeisen M, Schmidt J, Guillaume P, et al. TCR-ligand dissociation rate is a robust and stable biomarker of CD8+ T cell potency. *JCI Insight*. 2017;2(14):e92570.

12. Li Y, et al. Structure of a TCR with high affinity for self-antigen reveals basis for escape from negative selection. *Nat Immunol*. 2011;12:381-389.
