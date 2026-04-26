# Slide Narration & Anticipated Q&A for DAC Meeting

## Manpreet Kour | PI: Dr. Kausik Chakraborty | CSIR-IGIB

---

## PART I: SLIDE-BY-SLIDE NARRATION

---

### Slide 1: Title Slide

**Narration:**
"Good morning/afternoon. I am Manpreet Kour, a PhD scholar at CSIR-IGIB under the supervision of Dr. Kausik Chakraborty and co-supervision of Dr. Ankesh Kumar Jaiswal. I will be presenting my project titled 'Advancing CAR-T Cell Therapy by Understanding the Kinetics of Ag-Ab Interaction Parameters.' This is my first DAC meeting and I will walk you through the background, hypothesis, objectives, and experimental design of my project."

---

### Slide 2: Presentation Outline

**Narration:**
"I will begin with the background of cancer therapeutics leading to CAR-T cells, then discuss the fundamental biology of TCR-pMHC interactions — including binding kinetics, serial engagement, mechanical forces, and affinity windows. This foundational understanding will lead into my hypothesis that binding kinetics determine CAR-T cell signaling outcomes, followed by my experimental approach to test this hypothesis."

---

### Slide 3: Evolution of Cancer Therapeutics

**Narration:**
"Cancer therapeutics have evolved dramatically over the past century — from surgery and chemotherapy to targeted immunotherapies. The landmark approval of Kymriah in 2017 as the first CAR-T cell therapy marked a paradigm shift. However, current CAR-T therapies still face challenges including tumor relapse, immunosuppression by the tumor microenvironment, off-target toxicity, and early T cell exhaustion. My project aims to address some of these challenges by understanding how binding kinetics affect CAR-T cell function."

---

### Slide 4: The T Cell Receptor Complex

**Narration:**
"The TCR is a heterodimer of alpha and beta chains associated with CD3 signaling subunits. The binding interface is formed by six CDR loops. Crucially, CDR1 and CDR2 are germline-encoded and primarily contact the MHC helices, while CDR3 is somatically rearranged and contacts the peptide — this is the primary determinant of antigen specificity. TCR-pMHC binding is characteristically weak — in the micromolar range — which is orders of magnitude weaker than antibody-antigen binding. This weak binding turns out to be functionally important, as I will discuss."

**Source for CDR-MHC contacts:** Garcia et al., 2009, *Nat Immunol*; Rossjohn et al., 2015, *Annu Rev Immunol*.

---

### Slide 5: TCR-pMHC Binding Kinetics

**Narration:**
"Three kinetic parameters define TCR-pMHC binding. KD, the equilibrium dissociation constant, ranges from 1-100 micromolar, with CD8+ T cells averaging 13 micromolar and CD4+ T cells averaging 52 micromolar — this was shown by Aleksic et al. in 2007. The association rate kon is relatively slow, ranging from 600 to 400,000 per molar per second, reflecting the induced-fit conformational adjustment needed for binding. Most importantly, koff — the dissociation rate — is now recognized as the key discriminatory parameter. Hebeisen et al. in their 2017 JCI Insight paper showed that TCR-ligand koff is a robust and stable biomarker of CD8+ T cell potency, correlating with calcium mobilization and target cell recognition better than KD."

**Key point to emphasize:** koff, not KD, is the best predictor of T cell function.

---

### Slide 6: Kinetic Proofreading

**Narration:**
"In 1995, McKeithan proposed that TCR signaling operates through kinetic proofreading — the same mechanism that ensures fidelity in DNA replication. After pMHC binding, the TCR-CD3 complex must undergo multiple sequential phosphorylation steps before transmitting a signal. If the pMHC dissociates too quickly — that is, if koff is too fast — the modifications revert and no signal is produced. The mathematical elegance of this model is that N sequential steps amplify differences in koff exponentially, by a factor of approximately koff to the power of N. This explains how T cells can discriminate between self-peptides with only modestly lower affinity and foreign peptides. This was experimentally validated by Torigoe et al. in 2022 in Nature Immunology."

**Figure source:** Schematic based on McKeithan, 1995, PNAS 92:5042-5046. Validated experimentally by Torigoe et al., 2022, Nat Immunol 23:1045-1056.

---

### Slide 7: Optimal Dwell Time

**Narration:**
"This figure illustrates the 'Goldilocks' concept of optimal dwell time. The bell-shaped curve shows that T cell activation peaks at an intermediate dwell time and declines on either side. Kalergis et al. in their 2001 Nature Immunology paper demonstrated this quantitatively: TCR-pMHC complexes with half-lives less than or equal to 10.3 seconds failed to efficiently kill targets, those with half-lives of 77 seconds also showed impaired function, but complexes with intermediate half-lives of about 34 seconds showed maximum cytotoxic activity. This creates a tension between kinetic proofreading, which needs longer dwell times, and serial engagement, which needs shorter dwell times — the optimal lies in between."

**Figure source:** Bell-shaped curve is illustrative. Quantitative data points (10.3s, 34s, 77s) from Kalergis et al., 2001, Nat Immunol 2:229-234.

---

### Slide 8: Serial Engagement

**Narration:**
"The serial engagement model, proposed by Valitutti, Muller, Cella, Padovan, and Lanzavecchia in their landmark 1995 Nature paper, addresses a paradox: how can a T cell be activated when there are so few pMHC molecules on the APC? Their answer was that a single pMHC can serially engage and trigger up to approximately 200 TCRs. They showed that when T cells interacted with APCs displaying only about 100 pMHC molecules, up to 18,000 TCRs were triggered per T cell. This is possible because the low affinity and fast off-rate of TCR-pMHC allows the pMHC to dissociate from one TCR and bind the next. Huang et al. in their 2010 Nature paper further showed that 2D off-rates are up to 8,300-fold faster than 3D solution measurements, with agonist pMHC paradoxically dissociating the fastest in 2D."

**Figure source:** Schematic based on Valitutti et al., 1995, Nature 375:148-151.

---

### Slide 9: TCR Microclusters

**Narration:**
"TCR molecules are not randomly distributed on the T cell surface. They form organized structures at multiple scales. At the nanoscale, 7-30 TCRs form nanoclusters of 35-70 nm radius, stabilized by cholesterol and sphingomyelin binding to TCR-beta — as shown by Molnar and Schamel in their 2012 JBC paper. At the microscale, upon antigen contact, TCR microclusters of approximately 100 molecules form at the periphery of the immunological synapse — these are the actual signaling units, as demonstrated by Campi, Varma, and Dustin. Crucially, Crites et al. in their 2014 J Immunol paper showed that these microclusters pre-exist before antigen encounter, already contain LAT, and constitutively exclude the inhibitory phosphatase CD45. Active signaling occurs in peripheral microclusters, while the central cSMAC is actually a site of signal termination and TCR degradation."

**Figure source:** Schematic based on Campi et al., 2005; Varma et al., 2006; Crites et al., 2014.

---

### Slide 10: Catch Bonds vs Slip Bonds

**Narration:**
"This is one of the most important slides conceptually. In 2014, Liu, Chen, Evavold, and Zhu from Emory University published a landmark paper in Cell showing that TCR-pMHC interactions are not simple biochemical reactions — they are mechanosensitive. When force is applied to the TCR-pMHC bond, agonist peptides form catch bonds: the bond actually strengthens under force, peaking at about 10 piconewtons. In contrast, antagonist peptides form slip bonds: force weakens the bond monotonically. Using the OT-1 TCR system, they showed that agonists OVA, A2, and G4 all form catch bonds, while antagonists R4 and E1 form only slip bonds. The critical finding is that at zero force, the potency hierarchy was unclear, but at 10 piconewtons, the hierarchy became perfectly clear — force acts as a molecular stress test that reveals the quality of the pMHC-TCR interaction."

**Figure source:** Schematic representation of biphasic catch-slip vs monotonic slip behavior. Based on Liu et al., 2014, Cell 157:357-368. Validated by Pettmann et al., 2023, Nat Commun 14:2346.

---

### Slide 11: TCR Mechanotransduction

**Narration:**
"How does mechanical force get converted into a biochemical signal? The TCR beta chain has a unique structural feature — the Cbeta FG loop — a bulky solvent-exposed loop that acts as a molecular lever. When force is applied to the TCR-pMHC bond, it is transmitted through this loop to the CD3 heterodimers. The horizontal pulling force is converted to a vertical pushing force, with the TCR-beta transmembrane segment acting as a fulcrum. This conformational change exposes the CD3-zeta ITAMs that were previously sequestered in the membrane — a 'safety catch' mechanism. Only after this force-dependent exposure can Lck phosphorylate the ITAMs and initiate signaling. DNA tension probes from the Salaita lab have measured that naive T cells apply 12-19 piconewtons to their TCRs within seconds of binding, even before calcium signaling begins."

**Sources:** Brazin et al., 2015, PNAS; Kim et al., 2009, JBC; Liu et al., 2016, PNAS; Ma et al., 2019, PNAS.

---

### Slide 12: Self vs Non-Self Affinity Windows

**Narration:**
"This diagram shows the TCR affinity windows for different biological contexts. During thymic development, T cells with TCR affinity in the 100-300 micromolar range for self-pMHC are positively selected — data from Juang et al.'s 2010 JEM paper using the OT-1 system, where positively selecting peptides Catnb-Kb and Cappa1-Kb had KD values of 136 and 211 micromolar respectively. T cells with affinity below about 6 micromolar are negatively selected and deleted. In the periphery, viral antigen-specific TCRs average about 10 micromolar KD, while tumor-associated self-antigen TCRs average about 100 micromolar — a 10-fold gap that explains why anti-tumor immune responses are often weak. Hoffmann and Slansky documented these ranges in their 2020 Molecular Carcinogenesis review. Note also where CAR scFvs sit — at nanomolar affinity, orders of magnitude tighter than any natural TCR."

**Figure source:** Data from Juang et al., 2010, JEM 207:1223-1234 and Hoffmann & Slansky, 2020, Mol Carcinog 59:862-870.

---

### Slide 13: Engineering CAR-T Cells

**Narration:**
"CAR-T cells were developed to overcome fundamental limitations of natural T cell anti-tumor immunity — particularly MHC restriction and the low affinity of tumor-specific TCRs. CARs directly recognize surface antigens through their scFv domain, independent of MHC. The choice of costimulatory domain is critical: CD28 provides rapid, potent activation but lower persistence, while 4-1BB provides better persistence and resistance to exhaustion — as shown by multiple studies. For my project, the key design parameter I will focus on is the scFv affinity and its binding kinetics."

---

### Slide 14: CAR vs TCR Synapse

**Narration:**
"An important 2018 PNAS paper by Davenport and colleagues made a striking finding: CAR-T cells form fundamentally different synapses than TCR-activated T cells. Using a dual-receptor system where the same T cell expressed both an OT-I TCR and an anti-HER2 CAR, they showed that while the TCR synapse has the classic bull's-eye pattern with organized Lck and a distinct LFA-1 ring, the CAR synapse shows a disorganized multifocal Lck pattern with no distinct LFA-1 ring. Remarkably, CAR-T cells kill faster and detach from dying targets more quickly, and their killing is unimpaired even when LFA-1 is blocked. This suggests CARs operate through a fundamentally different signaling geometry than TCRs."

---

### Slide 15: The Affinity Mismatch Problem

**Narration:**
"This is central to my project rationale. Natural TCRs operate in the micromolar affinity range, while CAR scFvs typically have nanomolar affinity — a 1,000 to 1,000,000-fold difference. This supraphysiological affinity has consequences: the unnaturally slow off-rate of nanomolar scFvs prevents serial killing, promotes early exhaustion through sustained signaling, and can cause off-tumor toxicity. Strikingly, several studies have shown that reducing CAR affinity can improve outcomes. Ghorashian et al. showed that a CAT scFv with 40-fold lower affinity for CD19 than FMC63 showed greater cytotoxicity and proliferation in pediatric patients. Park et al. showed that micromolar affinity ICAM-1 CARs had superior anti-tumor efficacy and safety. This emerging evidence motivates my project to systematically explore the affinity-function relationship."

---

### Slide 16: Hypothesis

**Narration:**
"Based on the literature I have reviewed, my hypothesis is that specific biophysical features of the antigen-scFv interaction — particularly affinity, kinetic rates, and force-dependent bond stability — determine the mechanical tension applied to the CAR complex. This tension modulates ITAM exposure and controls signaling quality. Therefore, rational tuning of these parameters should yield CARs with optimized signaling. This hypothesis is supported by catch bond studies from the Zhu lab, mechanosensor studies from the Reinherz and Kim labs, affinity optimization evidence from Park and Ghorashian, and the kinetic proofreading framework from McKeithan."

---

### Slide 17: Objectives

**Narration:**
"My project has three objectives. First, to understand which binding parameters — KD, kon, koff, or force-dependent behavior — most affect signal amplitude. Second, to design affinity-optimized CAR constructs through site-saturation mutagenesis of key scFv-antigen interacting residues. Third, to evaluate how different binding kinetics affect CAR-T cell activation, exhaustion, and memory, and to identify the optimal affinity window."

---

### Slide 18: Experimental Workflow

**Narration:**
"This workflow shows the overall experimental strategy. We start with the anti-CD19 CAR constructs, identify key interacting residues through structural analysis, perform site-saturation mutagenesis to create a library of variants, functionally screen each mutant through co-culture assays, select those with desired or distinct phenotypes, clone and purify the scFvs, characterize their binding kinetics by SPR or BLI, and finally correlate kinetics with function to identify generalizable design rules."

---

### Slide 19: CAR Construct & Interacting Residues

**Narration:**
"We are working with the FMC63 anti-CD19 scFv, the same scFv used in the FDA-approved Kymriah and Yescarta. Using the crystal structure of the FMC63-CD19 complex from PDB entry 7URV and molecular visualization in ChimeraX, we identified three key interacting residues with the largest buried solvent-accessible surface area, greater than 35 angstroms: Tyrosine 260, Tyrosine 261, and Serine 214. These residues make the most significant contacts with CD19 and are therefore the most likely to modulate binding affinity when mutated."

---

### Slide 20: Site-Saturation Mutagenesis

**Narration:**
"We will use NNK codon degeneracy for site-saturation mutagenesis at each of the three positions. NNK codons encode all 20 amino acids with only 32 codons, minimizing stop codon frequency. For 95% library coverage, we need to screen at least approximately 98,000 colonies, as calculated by Pines et al. in 2022. We have designed specific forward primers for each position with the NNK degenerate codon replacing the wild-type codon. PCR will use Phusion polymerase for 20 cycles, with Sanger sequencing to verify each mutant."

---

### Slide 21: Functional Screening

**Narration:**
"Each mutant CAR will go through a standardized screening pipeline. After plasmid preparation, transfection optimization, viral production, and transduction of Jurkat cells, we will assess surface CAR expression by FACS using an anti-G4S linker antibody. Functional assays include cytotoxicity with Raji cell co-culture at E:T ratios of 1:1 and 2:1, rechallenge assays for persistence, exhaustion markers including PD-1, TIM-3, and LAG-3, memory markers, and cytokine profiling. Controls include un-transduced Jurkat cells with Raji and CAR-Jurkat cells with K562 as an irrelevant target."

---

### Slide 22: Target Phenotypes

**Narration:**
"We are looking for mutants that show desired cytotoxicity, maximum proliferative capacity, strong memory formation as indicated by CD45RO and CCR7 positivity, and minimal exhaustion markers. Mutants with the best phenotypes AND those with dramatically different phenotypes from the commercial FMC63 CAR will be taken forward for kinetic characterization. This creates a dataset directly linking binding kinetics to functional outcomes."

---

### Slide 23: Kinetic Characterization

**Narration:**
"Selected scFv mutants will be cloned into expression vectors — either the yeast display vector pCT-CON2 or the mammalian expression vector pTT5 — expressed, purified, and characterized by SPR using the Biacore system and/or BLI using the Octet system. These orthogonal methods will provide KD, kon, and koff for each mutant. The goal is to correlate these specific kinetic parameters with the functional phenotypes from the screening assays, ultimately identifying which kinetic parameter best predicts therapeutic efficacy."

---

### Slide 24: Expected Outcomes

**Narration:**
"We expect to generate a comprehensive library of anti-CD19 CAR variants with systematically altered binding kinetics, complete functional characterization correlating binding parameters with activation, exhaustion, and memory phenotypes, and a rational framework for affinity-optimized CAR engineering. This work bridges fundamental TCR-pMHC biology with translational CAR-T design and has the potential to improve CAR-T persistence, reduce exhaustion and toxicity, and identify generalizable design rules applicable beyond CD19."

---

### Slide 25: Thank You

**Narration:**
"Thank you for your time and attention. I would like to acknowledge my PI Dr. Kausik Chakraborty, my co-PI Dr. Ankesh Kumar Jaiswal, and all the DAC members for their guidance. I look forward to your questions and suggestions."

---

---

## PART II: ANTICIPATED Q&A

---

### Q1: Why did you choose these three specific residues (Tyr260, Tyr261, Ser214) for mutagenesis?

**Answer:** These residues were identified through structural analysis of the FMC63 scFv-CD19 complex (PDB: 7URV) using ChimeraX. We selected residues with the largest buried solvent-accessible surface area (SASA > 35 angstroms), indicating they form the most significant contacts with CD19. Tyrosine 260 and 261 are adjacent aromatic residues that likely form critical van der Waals and pi-stacking interactions, while Serine 214 contributes hydrogen bonding. Mutating these major contact residues will produce the widest range of affinity perturbations, from complete loss of binding to potentially enhanced binding, depending on the substituted amino acid.

---

### Q2: Why site-saturation mutagenesis rather than rational point mutations?

**Answer:** Rational point mutations would test only a few pre-selected substitutions, based on our predictions of which amino acids would increase or decrease affinity. Site-saturation mutagenesis with NNK codons is unbiased — it samples all 20 amino acids at each position, allowing us to discover unexpected binding modes that we might not have predicted. This is especially important because the relationship between individual amino acid properties and binding kinetics is non-linear and difficult to predict computationally. The NNK approach also allows us to explore the full dynamic range of affinity perturbations at each position.

---

### Q3: How will you ensure 95% library coverage with site-saturation mutagenesis?

**Answer:** According to the statistical framework from Pines et al. (2022), for NNK codons (32 possible codons) at a single position, 95% library coverage requires screening approximately 3x the number of possible variants. For our single-site libraries, this means screening ~98 colonies per position to be statistically confident that all 20 amino acids are represented. We will use Sanger sequencing to verify individual clones and ensure comprehensive coverage.

---

### Q4: Why use Jurkat cells instead of primary T cells?

**Answer:** Jurkat cells provide a standardized, reproducible system for initial screening of a large mutant library. They are a human T cell leukemia line that expresses the TCR signaling machinery and responds to TCR/CAR stimulation with measurable calcium flux, cytokine production, and activation markers. For a screening campaign with dozens of mutants, Jurkat cells offer consistency that would be difficult to achieve with donor-variable primary T cells. However, key findings from the Jurkat screen — particularly the top candidates — should ideally be validated in primary T cells in future work, as Jurkat cells lack certain features of primary T cells (e.g., they are already proliferating, they lack full effector differentiation capacity).

---

### Q5: What is the rationale for using Raji cells as target cells?

**Answer:** Raji cells are a well-established Burkitt lymphoma B cell line that constitutively expresses CD19 on their surface at physiological levels. They are the standard target cell line used in anti-CD19 CAR-T functional assays across the literature, including in studies from the Brentjens, June, and other leading CAR-T labs. Using Raji cells allows direct comparison of our results with published data. K562 cells (which lack CD19) serve as the negative control to confirm antigen-specific killing.

---

### Q6: If koff is the key parameter, why measure KD and kon as well?

**Answer:** While koff is the best single predictor of T cell activation in the TCR-pMHC system, the CAR-antigen system may operate differently due to the fundamentally different affinity regime (nanomolar vs micromolar). Moreover, Huang et al.'s 2010 Nature paper showed that in 2D membrane-constrained measurements, the on-rate (kon) becomes the better discriminator of agonist potency — suggesting kon may be important for the encounter phase. By measuring all three parameters (KD, kon, koff), we can determine which parameter best correlates with functional outcome specifically in the CAR context, which remains an open question. Additionally, two mutations could have identical KD but different kon/koff profiles, leading to different functional outcomes.

---

### Q7: How does your work differ from existing CAR affinity optimization studies?

**Answer:** Existing studies (Ghorashian, Park, Liu et al.) have compared a small number of affinity variants — typically 2-3 scFvs with different affinities. Our approach is systematic: by performing site-saturation mutagenesis at three key residues, we generate a comprehensive library spanning a wide affinity range. This allows us to map the full affinity-function relationship rather than comparing discrete points. Additionally, we will specifically correlate individual kinetic parameters (KD, kon, koff) with multiple functional outcomes (cytotoxicity, exhaustion, memory), enabling us to identify which kinetic parameter is most predictive and what the optimal window is for each functional outcome.

---

### Q8: What is the expected affinity range of your mutant library?

**Answer:** Based on the literature on antibody-antigen interface mutagenesis, single amino acid substitutions at major contact residues typically perturb affinity by 10-fold to >1000-fold in either direction. The FMC63 KD for CD19 is approximately 5 nM by SPR under optimized conditions (Seigner et al., 2023, *Scientific Reports* 13:23024; Singh et al., 2023, *Science Immunology* 8:eadf1426). Note: earlier literature reported values as low as 0.3 nM, but these were affected by ligand depletion and avidity artifacts. Starting from the corrected KD of ~5 nM, we expect our library to span from sub-nanomolar (enhanced binding) through mid-nanomolar to potentially micromolar affinity (weakened binding). Published data on our exact target residues confirms this range: Y260A shows no detectable SPR binding (>5 µM), while Y261A has KD of 682.5 nM (Singh et al., 2023). This range would encompass the "supraphysiological" CAR regime, the proposed optimal window (~100 nM - 1 µM), and potentially even the natural TCR affinity range (1-100 µM), allowing comprehensive mapping.

---

### Q9: Why do you think mechanical force is relevant to CAR signaling?

**Answer:** T cells generate mechanical forces at receptor-ligand interfaces through their actin cytoskeleton regardless of whether they signal through a TCR or a CAR. Davenport et al. (2018, PNAS) showed that CAR-T cells form active synapses with actin dynamics. The forces generated by actin retrograde flow (measured at 12-19 pN by the Salaita lab) will act on the CAR-antigen bond just as they act on TCR-pMHC bonds. Whether the CAR-antigen bond behaves as a catch bond or slip bond under these forces will affect bond lifetime under physiological conditions, which is different from zero-force measurements by SPR. This is an important conceptual point: SPR/BLI measure zero-force kinetics, but physiological bonds experience piconewton forces. The force-dependent bond behavior may be a better predictor of in vivo CAR-T function than zero-force affinity.

---

### Q10: What if none of your mutants show improved phenotypes compared to FMC63?

**Answer:** This would itself be an informative result, suggesting that FMC63 is already near-optimal for the CD19 target. However, even if no mutant is "better" overall, we expect to see differential effects on specific phenotypes — for example, some mutants may show better memory formation but slightly reduced initial cytotoxicity, or reduced exhaustion at the cost of slower killing. These differential phenotypes, correlated with binding kinetics, would still provide valuable insights into the affinity-function relationship. Additionally, the kinetic data from SPR/BLI would reveal whether there is a kinetic "ceiling" beyond which function plateaus, analogous to the affinity ceiling described in the TCR literature.

---

### Q11: How do you plan to address the issue of tonic signaling in your CAR mutants?

**Answer:** Tonic signaling — antigen-independent signaling from CARs — is influenced by scFv self-aggregation, which can be affected by amino acid substitutions. We will monitor for tonic signaling by comparing CAR-transduced Jurkat cells cultured WITHOUT Raji cells (no antigen) to un-transduced controls. Markers of tonic signaling include baseline expression of activation markers (CD69, CD25), exhaustion markers (PD-1), and basal cytokine production. If certain mutants show increased tonic signaling, this will be factored into the interpretation of their functional data.

---

### Q12: Why not use CRISPR knock-in instead of lentiviral transduction for CAR expression?

**Answer:** Lentiviral transduction is the standard method for CAR delivery in both research and clinical settings — including the FDA-approved products Kymriah and Yescarta. It provides stable integration and sustained CAR expression. CRISPR knock-in to a specific locus (e.g., TRAC) would provide more uniform expression levels, which could reduce experimental variability. However, for a screening campaign with dozens of mutants, lentiviral transduction is more practical and scalable. The trade-off is some variability in expression levels due to random integration, which we will control for by normalizing functional readouts to surface CAR expression levels measured by FACS.

---

### Q13: Can you explain the difference between 2D and 3D affinity measurements and which is more relevant?

**Answer:** 3D measurements (SPR, BLI) measure binding between soluble molecules in solution — one partner immobilized on a chip, the other flowing over it. 2D measurements (micropipette adhesion, FRET) measure binding between molecules anchored on opposing cell membranes or supported bilayers. Huang et al.'s 2010 Nature paper revealed that 2D kinetics are fundamentally different: off-rates are up to 8,300-fold faster in 2D than 3D, and paradoxically, agonist pMHC dissociates fastest in 2D (opposite of 3D). The 2D measurements may be more physiologically relevant because they capture membrane confinement, orientation constraints, co-receptor contributions, and mechanical forces. For our initial characterization, we will use 3D methods (SPR/BLI) for practicality and comparability with published data, but we acknowledge that 2D measurements would provide complementary and potentially more informative data.

---

### Q14: What is the timeline for the project?

**Answer:**
- **Year 1 (current):** Literature review, CAR construct design, interacting residue identification, site-saturation mutagenesis library construction, begin functional screening pipeline optimization
- **Year 2:** Complete functional screening of all mutants, rechallenge assays, exhaustion/memory phenotyping, select candidates for kinetic characterization
- **Year 3:** Clone and purify selected scFvs, SPR/BLI kinetic characterization, correlate kinetics with function, identify generalizable rules
- **Year 4:** Validate key findings in primary T cells (if feasible), manuscript preparation, thesis writing

---

### Q15: What are the potential limitations or risks of this approach?

**Answer:**
1. **Library complexity:** While site-saturation at single positions is manageable (~20 variants per position), combining mutations at multiple positions would create a combinatorial explosion. We focus on single-site mutations first.
2. **Jurkat vs primary T cell gap:** Jurkat cells may not fully recapitulate primary T cell behavior, especially for exhaustion and memory phenotypes.
3. **Zero-force vs physiological kinetics:** SPR/BLI measure zero-force kinetics, which may not predict force-dependent bond behavior. Addressing this fully would require specialized equipment (biomembrane force probes, DNA tension sensors).
4. **Protein expression:** Some scFv mutants may not fold or express properly, reducing the effective library size.
5. **Clinical translation gap:** In vitro findings in Jurkat/Raji may not directly translate to in vivo efficacy.

---

### Q16: How does 4-1BB vs CD28 costimulation interact with the affinity question?

**Answer:** This is an excellent question. 4-1BB costimulation has been shown to counteract exhaustion by activating anti-apoptotic, anti-hypoxic, and metabolic programs, while CD28 provides stronger initial activation but less persistence. The costimulatory domain may interact with affinity in important ways: a high-affinity scFv paired with CD28 might rapidly exhaust, while the same scFv with 4-1BB might persist. Conversely, a low-affinity scFv might need CD28's stronger costimulation to reach activation threshold. In our initial screen, we will use a fixed costimulatory domain to isolate the effect of scFv affinity. Testing the interaction between affinity and costimulation would be an excellent follow-up study.

---

### Q17: Is there any computational validation of your chosen interacting residues?

**Answer:** Yes, the interacting residues were identified from the crystal structure (PDB: 7URV) using ChimeraX molecular visualization. The buried SASA (solvent-accessible surface area) was calculated for each residue at the FMC63-CD19 interface, and residues with buried SASA > 35 angstroms were selected. This is a standard structural biology approach for identifying energetically important interface contacts. Computational alanine scanning or Rosetta-based binding energy calculations could provide additional validation, and we are open to incorporating these as the project progresses.

---

### Q18: What controls will you use to ensure the mutations affect binding rather than protein folding?

**Answer:** Several controls:
1. **Surface expression:** CAR surface expression measured by anti-G4S linker antibody FACS ensures the mutant protein folds and traffics correctly. Mutants that fail to express on the surface likely have folding defects.
2. **Western blot:** Confirmation of full-length CAR protein expression.
3. **Thermal stability:** For purified scFv proteins, differential scanning fluorimetry can assess thermal stability.
4. **SPR binding curves:** Proper one-to-one binding kinetics in SPR rule out aggregation or misfolding artifacts.
5. **Any mutant with no surface expression will be excluded from functional analysis** as likely a folding mutant rather than an affinity mutant.
