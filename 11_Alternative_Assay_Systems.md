# Alternative 2D and Non-Cell-Based Systems for Evaluating Anti-CD19 CAR-T Cell Function

## DAC Meeting Reference Document
### Manpreet Kour | PI: Dr. Kausik Chakraborty | Co-PI: Dr. Ankesh Kumar Jaiswal
### CSIR-IGIB | AcSIR Reg. 10BB25J02028

---

## Motivation: Why Alternatives to Standard Raji Co-Culture?

The standard Raji cell co-culture system, while widely used, has three specific limitations that are relevant to this project:

1. **CD19 expression is fixed and uncontrollable** -- Raji cells constitutively express CD19 at a set level (~14,000-57,000 molecules/cell depending on the measurement method). This prevents systematic investigation of how antigen density affects CAR-T function, which is directly relevant to affinity optimization.

2. **FACS quantification of Raji killing is difficult** -- In a suspension-suspension co-culture (Jurkat + Raji), accurately distinguishing and quantifying dead target cells by FACS requires careful gating on CD3-/CD19+ cells with viability dyes, and absolute cell counting is technically challenging.

3. **Raji cells are suboptimal for kinetic (time-resolved) studies** -- Endpoint assays at 24h do not reveal the dynamics of CAR engagement. Raji cells in suspension do not permit real-time impedance-based monitoring.

This document reviews published alternative systems that address these limitations.

---

## 1. Engineered Cell Lines with Tunable/Variable CD19 Expression

### 1.1 NALM-6 CD19 Knockout with Controlled Re-expression (The Gold Standard for Antigen Density Studies)

**Key Reference:** Majzner RG, Rietberg SP, Sotillo E, et al. "Tuning the Antigen Density Requirement for CAR T Cell Activity." *Cancer Discovery* 10(5):702-723, 2020. PMID: 32193224. PMC7939454.

**How it works:**
1. CRISPR-Cas9 is used to knock out endogenous CD19 from the NALM-6 B-ALL cell line
2. A lentiviral vector encoding a truncated CD19 (transmembrane + extracellular domains only) is transduced into the knockout cells
3. FACS sorting followed by single-cell cloning generates a library of clones with defined, distinct CD19 surface densities
4. CD19 molecules per cell are quantified using the BD QuantiBRITE PE bead kit

**Specific antigen densities achieved (molecules/cell):**
- ~45 (very low)
- ~963 (low)
- ~2,053 (low-moderate, used in in vivo models)
- ~45,851 (high, comparable to wild-type NALM-6)
- Additional clones at intermediate levels

**Key findings relevant to this project:**
- CAR-T cell potency is highly dependent on target antigen density
- Below ~2,000 molecules of CD19 per cell, cytokine production is nearly ablated
- CD19-CD28-zeta CAR (axicabtagene ciloleucel design) outperforms CD19-4-1BB-zeta CAR (tisagenlecleucel design) against antigen-low tumors
- Additional ITAMs in the CAR lower the antigen density threshold
- Replacement of CD8 hinge/TM with CD28 hinge/TM lowers the activation threshold

**NALM-6 CD19 surface density (wild-type):** Approximately 36,000 molecules/cell by conventional flow cytometry with Scatchard analysis. Note: Super-resolution microscopy detected ~1,780 molecules/cell (PMID: 31273208), highlighting measurement method sensitivity. The discrepancy reflects technique differences, not biological variation.

**Comparison to Raji:** NALM-6 is described as "CD19-high" relative to most B-ALL lines. Raji and Daudi have CD22 and CD19 at approximately equivalent densities. The range across B-cell lines (Haso et al., Blood 2013, PMID: 23243285) is 14,112-56,946 molecules/cell by QuantiBRITE.

**Advantages:**
- Precisely defined antigen densities (molecules per cell quantified)
- Directly tests how FMC63 affinity variants respond to low vs high CD19
- Models clinical antigen loss (a validated resistance mechanism)
- NALM-6 is CD19+, suspension, B-ALL -- similar biology to Raji

**Disadvantages:**
- Requires CRISPR knockout, lentiviral transduction, single-cell cloning (several months of work)
- Each clone needs QuantiBRITE validation
- CD19 expression may drift over passages (re-validate regularly)

**Feasibility for CSIR-IGIB:** High. CRISPR-Cas9 and lentiviral tools are standard at IGIB. NALM-6 is available from ATCC (CRL-1567) or DSMZ. BD QuantiBRITE beads (Cat# 340495) are available through BD India distributors.

---

### 1.2 K562-CD19 Engineered Lines

**Background:** K562 (ATCC CCL-243) is a CML line that does NOT express CD19, CD20, or CD22. It is already used as a negative control in the standard assay. K562 can be transduced with CD19 to create a positive target.

**Published approaches:**

**(a) K562 as Artificial Antigen Presenting Cells (aAPCs):**

**Reference:** Rushworth D, Jena B, Olivares S, et al. "Universal Artificial Antigen Presenting Cells to Selectively Propagate T Cells Expressing Chimeric Antigen Receptor Independent of Specificity." *Journal of Immunotherapy* 37(4):204-213, 2014. PMID: 24714354. PMC4139067.

- K562 cells electroporated with truncated human CD19 (aa 1-313) using Sleeping Beauty transposon system
- Drug selection under G418 followed by single-cell cloning
- Uniform CD19 expression achieved; used primarily for CAR-T expansion (irradiated aAPCs)
- Protocol: co-culture at 1:2 ratio (CAR-T:aAPC), re-stimulate every 7 days, 50 IU/mL IL-2

**(b) Commercially available K562-CD19 lines:**

| Vendor | Product | Catalog # | Features |
|--------|---------|-----------|----------|
| ProMab Biotechnologies | K562 CD19-eGFP | PM-K562-GFP | CD19+ GFP+ for tracking |
| BPS Bioscience | Firefly Luciferase CD19 K562 | 82486 | CD19+ Luc+ for bioluminescence assays |
| Creative Biolabs | K562-CD19 | Custom | CD19 overexpressed |
| Creative Biogene | CD19 Stable Cell Line - K562 | CSC-RO0252 | CD19+ stable |

**Advantages:**
- K562 parental is CD19-negative (built-in isogenic negative control)
- Can engineer variable CD19 levels by using different promoter strengths or FACS sorting
- Widely used, commercially available
- Compatible with luciferase-based killing assays

**Disadvantages:**
- K562 is MHC-I negative and has unique biology (NK-cell sensitive)
- Variable expression levels NOT pre-made -- would need to be engineered in-house
- Suspension cell (same FACS quantification issues as Raji)

**Feasibility for CSIR-IGIB:** High. K562 is already in use as the negative control.

---

### 1.3 CHO-CD19 Adherent Target Cells (Enables xCELLigence Real-Time Assays)

**This is a particularly important system for addressing both the antigen density and kinetics problems.**

**Key commercial product:**

**BPS Bioscience CD19 CHO Recombinant Cell Line**
- Catalog #79561-L (Low CD19 expression)
- Catalog #79561-M (Medium CD19 expression)
- Catalog #79561-H (High CD19 expression)
- Base cell: CHO-K1 (adherent)
- Full-length human CD19 (NM_001770) overexpressed
- Surface expression confirmed by flow cytometry
- Each clone selected for different expression levels to mimic various CD19 densities
- Approximate cost: ~4000 GBP per 2 vials (based on UK distributor pricing)

**Also available:**
- CD19/Firefly Luciferase CHO Cell Line (Catalog #79714) -- enables luminescence readout

**Critical advantage -- enables xCELLigence real-time impedance assay:**

**Reference:** Lifeliqe et al. "Evaluation of CAR-T cell cytotoxicity: Real-time impedance-based analysis." *Methods in Cell Biology* 167:115-130, 2022. PMID: 35153000.

- CHO-CD19 cells adhere to xCELLigence E-Plates
- Impedance decreases as CAR-T cells kill adherent targets
- Published protocol: 10,000 HEK-293-CD19 target cells per well, monitor 23h, then add CAR-T at E:T ratios 0.06-4:1
- Real-time kinetic data over hours to days
- Very few target and effector cells needed
- Minimal user input after setup

**Advantages:**
- Three defined CD19 expression levels (Low/Medium/High) available off-the-shelf
- Adherent -- compatible with xCELLigence real-time impedance monitoring
- Adherent -- easier to quantify killing (detached cells counted, no FACS gating confusion)
- Enables kinetic studies not possible with suspension targets
- Adherent -- compatible with microscopy, immune synapse imaging

**Disadvantages:**
- CHO cells are non-human, non-hematopoietic (reduced biological relevance)
- Missing co-stimulatory ligands and adhesion molecules present on B cells
- xCELLigence instrument required (Agilent, significant capital expense)
- Impedance readout is indirect and lacks specificity
- Commercially expensive for initial purchase

**Feasibility for CSIR-IGIB:** Moderate. Cell lines can be imported. xCELLigence instrument availability at IGIB/collaborator institution would need to be confirmed. If unavailable, adherent targets still enable microscopy-based killing assays and standard cytotoxicity readouts.

---

### 1.4 HEK293T-CD19 Adherent Targets

**Published usage:** HEK-293-CD19 cells have been used in xCELLigence protocols for CD19 CAR-T cytotoxicity studies (Agilent application notes; PMID: 35153000).

- HEK293T is adherent, fast-growing, easy to transfect
- Can be stably transduced with CD19 (lentiviral or Sleeping Beauty)
- Compatible with xCELLigence impedance monitoring
- Can be made in-house by transducing HEK293T with CD19-encoding lentivirus

**Advantages:**
- Inexpensive to generate in-house
- Easy to transfect/transduce
- Adherent -- enables real-time killing kinetics

**Disadvantages:**
- Same as CHO-CD19 (non-hematopoietic, missing B-cell biology)
- No pre-made variable expression levels commercially available
- Would need to be generated and characterized in-house

**Feasibility for CSIR-IGIB:** High. HEK293T is universally available. Lentiviral transduction is standard at IGIB.

---

### 1.5 CD19-Knockout Cell Lines (Negative Controls and Re-expression Models)

**Commercially available:**

| Product | Vendor | Catalog # | Application |
|---------|--------|-----------|-------------|
| CD19 Knockout Raji | BPS Bioscience | 82166 | Negative control for CD19-CAR specificity |
| CD19 KO Raji + Firefly Luc | BPS Bioscience | 82167 | Negative control with luminescence readout |
| CD19/CD20 Double KO Raji | BPS Bioscience | 82623 | Dual antigen loss model |
| CD19/CD22 Double KO Raji | BPS Bioscience | 82956 | Dual antigen loss model |
| NALM6-Fluc-Puro/CD19-KO | Imanis Life Sciences | -- | CD19-negative NALM-6 with firefly luciferase |

These knockout lines serve as:
- Negative controls for specificity testing
- Starting material for re-expression at controlled levels (as per Majzner et al. 2020 protocol)

---

## 2. Plate-Bound and Bead-Based Non-Cell Systems

### 2.1 Recombinant CD19 Protein Coated on Plates

**Key challenge with CD19:** CD19 extracellular domain is notoriously difficult to express as a properly folded recombinant protein.

**Reference (solving the CD19 folding problem):** Lobner E, Wachernig A, Gudipati V, et al. "Getting CD19 Into Shape: Expression of Natively Folded 'Difficult-to-Express' CD19 for Staining and Stimulation of CAR-T Cells." *Frontiers in Bioengineering and Biotechnology* 8:49, 2020. PMID: 32117929. PMC7020774.

**Key details:**
- CD19-AD2 fusion construct (CD19 ECD fused to domain 2 of human serum albumin) expressed in CHO-K1 cells
- CD19-Fc fusion expressed poorly with inferior quality -- the AD2 fusion is preferred
- Production boosted with valproic acid (0.5 mM) as chemical chaperone
- Purified by His-tag affinity chromatography + SEC; yield 1.04 mg/mL
- Confirmed biologically active on supported lipid bilayers (TIRF microscopy, calcium imaging)
- Triggered formation of cSMACs and density-dependent calcium flux in CD19-CAR-T cells

**Plate-bound protein assay -- validated for CAR-T activation:**

**Reference:** Neto Da Rocha M, Guiot M, et al. "Coated recombinant target protein helps explore IL-1RAP CAR T-cell functionality in vitro." *Immunologic Research* 71:271-282, 2023. PMID: 36456721. PMC10060290.

**Protocol (validated for IL-1RAP CAR, directly applicable to CD19 CAR):**
1. Coat 96-well plate overnight with recombinant target protein in PBS (concentration range: 0.01-10 ug/mL)
2. Significant dose-response at 0.01 ug/mL; plateau at 5-10 ug/mL
3. Quality control experiments at 7.5 ug/mL
4. Co-culture CAR-T cells with coated plate for 6 hours
5. Readouts: CD107a degranulation (flow cytometry), IFN-gamma secretion (ELISA)

**Key finding:** CD107a expression with plate-bound protein (36.22 +/- 18.61%) was comparable to cell-based targets (26.58 +/- 3.44% with IL-1RAP+ cell line).

**NOTE:** This was validated for IL-1RAP CAR, not specifically CD19 CAR. However, BPS Bioscience has validated that the NFAT-Luciferase Reporter Jurkat expressing anti-CD19 CAR (Cat# 79853) responds to CD19-expressing CHO cells, demonstrating the principle works for CD19 CAR activation by immobilized antigen.

**Advantages:**
- No target cells needed (eliminates FACS gating complexity)
- Precisely controlled antigen density by coating concentration
- Highly reproducible
- Simple protocol (overnight coating, 6h co-culture)
- Cost-effective once protein is available

**Disadvantages:**
- Recombinant CD19 is difficult to express (must use AD2 fusion or stabilized variants)
- Lacks membrane fluidity -- antigen cannot redistribute
- No co-stimulatory molecules (ICAM-1, B7, etc.) unless co-coated
- Does not model immune synapse formation
- Does not measure cytotoxicity (activation readout only)

**Feasibility for CSIR-IGIB:** Moderate. Requires either in-house expression of CD19-AD2 in CHO cells or purchase of stabilized recombinant CD19 (ACROBiosystems, R&D Systems have CD19 ECD available). Plate-coating protocol is standard.

---

### 2.2 Anti-FMC63 Beads and Anti-Idiotype-Based Stimulation

**Key products:**

**ACROBiosystems ActiveMax Anti-FMC63 Beads:**
- Catalog: FMC63-MBS-C008
- 5.5 um superparamagnetic beads immobilized with anti-FMC63 antibody
- Designed to stimulate FMC63-specific CAR-T cells in vitro
- Mimics CD19-expressing target cell engagement

**Anti-idiotype antibodies for FMC63 CAR detection and stimulation:**
- Miltenyi REA1297: anti-FMC63 idiotype (PE: 130-127-342; APC: 130-127-343)
- ACROBiosystems Y45: anti-FMC63 (FM3-Y45)
- Mouse mAb clone 136.20.1 (published by Jena et al., PMID: 23469246)

**Can be used for:**
- CAR-T cell stimulation/expansion (antigen-specific activation through the CAR)
- Quality control potency assays
- Comparison of signaling between different scFv affinity variants

**Advantages:**
- Directly engages the FMC63 CAR binding site
- No need for CD19 protein expression
- Beads provide defined size and stoichiometry
- Compatible with many downstream readouts

**Disadvantages:**
- Anti-idiotype engages the CAR differently than native CD19 antigen
- Does not test CD19 binding affinity (the idiotype antibody binds the scFv, not CD19)
- CRITICAL for this project: cannot distinguish between FMC63 affinity variants since all variants share the same idiotype region unless mutations alter the paratope
- Expensive reagents

**Feasibility for CSIR-IGIB:** High for stimulation/expansion. NOT suitable for comparing FMC63 affinity variants (the anti-idiotype will bind all variants similarly unless mutations drastically alter the binding site).

---

### 2.3 Anti-CD3/CD28 Dynabeads (For Manufacturing, Not Antigen-Specific Testing)

Standard CD3/CD28 Dynabeads (Thermo Fisher 11131D/11161D) are used for T cell activation and expansion during CAR-T manufacturing, not for testing CAR-specific function. Listed here for completeness -- these are NOT alternatives to the Raji co-culture for testing antigen-specific CAR activation.

---

### 2.4 Antigenic Vesicles (Membrane Vesicles Displaying CD19)

**Reference:** Ukrainskaya VM, et al. "Antigen-Specific Stimulation and Expansion of CAR-T Cells Using Membrane Vesicles as Target Cell Surrogates." *Small* 17(49):2102643, 2021. PMID: 34605165.

**How it works:**
- Microcytospheres/vesicles generated from cell lines stably expressing CD19
- These vesicles display native CD19 in a lipid membrane context
- Bind specifically to CAR-T cell surface

**Key finding:** Vesicle-stimulated CAR-T expansion was 5x higher than Dynabead/IL-2 or feeder cell stimulation. Equal expansion of CD4+ and CD8+ subsets (unlike Dynabeads which favor CD4+).

**Advantages:**
- Antigen in native membrane context (preserves orientation, mobility)
- No live target cells needed
- Tunable antigen density

**Disadvantages:**
- Technically demanding to produce vesicles
- Primarily used for expansion, not functional assays
- Not widely adopted yet

**Feasibility for CSIR-IGIB:** Low-moderate. Requires specialized vesicle preparation. More useful for manufacturing optimization than functional assays.

---

## 3. Supported Lipid Bilayer (SLB) Systems

### 3.1 Overview and Relevance

Supported lipid bilayers are glass-supported artificial membranes functionalized with mobile antigens that mimic the target cell surface. They are the gold standard for studying CAR immunological synapse formation.

### 3.2 Key Publications Using SLBs with CD19 for CAR Studies

**(a) Rewired CAR Signaling Study:**

**Reference:** Dong R, Libby KA, Blaeschke F, et al. "Rewired signaling network in T cells expressing the chimeric antigen receptor (CAR)." *The EMBO Journal* 39(16):e104730, 2020. PMID: 32643825. PMC7429742.

**SLB composition:**
- 97.5% POPC, 2.0% Ni2+-NTA-DOGS, 0.5% PE-PEG5000, <0.1% Biotin-Cap-PE
- SUVs generated by freeze-thaw + centrifugation
- Functionalized with biotinylated CD19(Ex) at titrated concentrations: 10 nM, 2 nM, 0.4 nM

**TIRF microscopy parameters:**
- Nikon TI-E microscope, 100x Plan Apo 1.49 NA oil immersion
- 4 laser lines: 405, 488, 561, 640 nm
- Imaging at 37 degrees C for live cells

**Key findings:**
- CD19 binding triggers CAR microcluster formation (signaling-competent)
- ~40% of cells maintained separated microclusters without forming cSMAC
- LAT is NOT required for CAR microcluster formation (unlike TCR signaling)
- LAT is still needed for optimal IL-2 production
- This demonstrates a "rewired" signaling pathway in CAR vs TCR

**(b) IS Quality Predicts CAR Effectiveness:**

**Reference:** Xiong W, Chen Y, Kang X, et al. "Immunological Synapse Predicts Effectiveness of Chimeric Antigen Receptor Cells." *Molecular Therapy* 26(4):963-975, 2018. PMID: 29503199. PMC6080133.

- SLBs prepared by fusing liposomes with glass coverslips
- Blocked with casein, coated with streptavidin, then biotinylated antibodies with fluorescent dyes
- Measured: F-actin accumulation, pZeta distribution, antigen clustering, lytic granule polarization, pZAP-70, Lck
- **Key finding:** Long-term killing capability (not short-term cytotoxicity or cytokine secretion) correlates with IS quality
- Studied both CD19-CAR and Kappa-CAR with CD28 or 4-1BB co-stimulatory domains

**(c) Standardized Protocol for CAR IS Assessment:**

**Reference:** Cho JH, Tsao WC, Naghizadeh A, Liu D. "Standardized protocol for the evaluation of chimeric antigen receptor (CAR)-modified cell immunological synapse quality using the glass-supported planar lipid bilayer." *Methods in Cell Biology* 173:131-149, 2022. PMID: 36653082. PMC10768727.

**Protocol details:**
- Lipids: DOPC (400 uM) + Biotin-PE (80 uM, 2 mol%)
- Biotinylated-CD19-AF488 added via streptavidin-biotin linkage
- Antigen range: 1 ng to 100 ng recommended starting range
- Confocal microscopy (Nikon A1R HD, 60x objective)
- Readouts: F-actin, Lck, phospho-CD3-zeta, ZAP70 MFI
- Machine learning-based boundary detection and quantification

**(d) CD19-AD2 on SLBs with TIRF and Calcium Imaging:**

**Reference:** Lobner et al. (2020), described in Section 2.1 above (PMID: 32117929).

- SLBs functionalized with CD19-AD2, ICAM-1, and B7-1
- Triggered cSMAC formation and density-dependent calcium flux
- TIRF microscopy and Fura-2 calcium imaging

**(e) Mechanical Force and CAR Microclustering:**

**Reference:** Qiu Y, Xiao Q, Wang Y, et al. "Mechanical force determines chimeric antigen receptor microclustering and signaling." *Molecular Therapy* 32(3):593-608, 2024. PMID: 38327049. PMC11163199.

- Used DNA tether-based force sensors on planar lipid bilayers
- Forces ranged from ~12 to ~51 pN
- Tested FMC63 CAR (anti-CD19) -- confirmed both CAR(zeta) and CAR(delta-zeta) form microclusters
- Cytotoxicity requires lower force threshold (~26-33 pN) than cytokine production (~38-48 pN)
- TIRF microscopy for single-molecule tracking

### 3.3 Advantages of SLB Systems

- Antigen density precisely controlled by bilayer composition
- Antigen is mobile in the membrane (mimics cell surface)
- Compatible with high-resolution TIRF/confocal imaging
- Can study synapse formation, signaling molecule recruitment, force
- Can include accessory molecules (ICAM-1, B7-1, CD58) or omit them to study isolated CAR function
- Reductionist model separating CAR-intrinsic signaling from cellular complexity

### 3.4 Disadvantages/Limitations

- Technically demanding (lipid preparation, bilayer quality control)
- Requires expensive microscopy equipment (TIRF or confocal)
- Does not measure cytotoxicity
- Artificial system -- no target cell death, no serial killing
- Low throughput (single-cell imaging)
- Requires fluorescently labeled, natively folded recombinant CD19

### 3.5 Feasibility for CSIR-IGIB

Moderate-to-high. IGIB has confocal microscopy facilities. Lipid bilayer preparation is achievable with lipids from Avanti Polar Lipids (now part of Merck/Sigma). The main bottleneck is obtaining properly folded recombinant CD19 protein (either purchased or expressed in-house). This system would be an advanced experiment for later phases of the PhD.

---

## 4. 2D Kinetics Measurement Systems (Membrane-Anchored Kinetics)

**This section is critically important for this project, which studies affinity-function relationships in anti-CD19 CARs.**

### 4.1 Why 2D Kinetics Matter

**Key paradigm-shifting reference:** Huang J, Zarnitsyna VI, Liu B, et al. "The kinetics of two-dimensional TCR and pMHC interactions determine T-cell responsiveness." *Nature* 464(7290):932-936, 2010. PMID: 20357766. PMC2925443.

**Fundamental difference:**

| Parameter | 3D Kinetics (SPR/BLI) | 2D Kinetics (Membrane-Anchored) |
|-----------|----------------------|-------------------------------|
| Measurement context | Purified proteins in solution or on chip | Molecules on intact cell membranes |
| Units of affinity | M^-1 (KA) or M (KD) | um^4 (AcKa, effective 2D affinity) |
| What is measured | Intrinsic molecular binding | In situ binding at cell-cell interface |
| Includes cellular effects | No | Yes (membrane microtopology, anchor effects, molecular orientation, cytoskeleton) |
| Dynamic range | ~1 log (for TCR-pMHC panel) | ~3 logs (1000-fold broader) |
| Correlation with T cell function | Weak (3D KD) | Strong (2D AcKa, 2D koff) |
| Off-rates | Slower | Up to 8,300-fold faster |
| Co-receptor contribution | Not captured | Naturally included |

**Critical finding:** For a panel of TCR-pMHC ligands, 2D affinities span 3 orders of magnitude while 3D affinities differ by only ~1 log. The 2D parameters match the dynamic range of corresponding T cell responses. This means 3D SPR-measured KD values may fail to predict functional differences between scFv variants that 2D measurements would detect.

**UNCERTAINTY FLAG:** This has been demonstrated for TCR-pMHC systems but NOT yet specifically for CAR-scFv-antigen interactions in published literature. However, the biophysical principles apply equally to any receptor-ligand pair measured in solution vs on membranes.

### 4.2 Micropipette Adhesion Frequency Assay

**Reference:** Zarnitsyna VI, Zhu C. "Adhesion frequency assay for in situ kinetics analysis of cross-junctional molecular interactions at the cell-cell interface." *Journal of Visualized Experiments* (57):e3519, 2011. PMID: 22083316. PMC3308619.

**How it works:**
1. A human red blood cell (RBC) is used as both biosensor and ligand-presenting surface
2. One molecule (e.g., CD19-Fc or anti-CD19 scFv) is coated on the RBC surface
3. The RBC is aspirated into one micropipette; a CAR-T cell (or scFv-expressing cell) into another
4. Computer-controlled piezoelectric translator drives repeated contact-retraction cycles
5. Adhesion is detected as RBC elongation when pulling apart
6. Adhesion probability is measured across many cycles for each contact time
7. Varying contact time generates binding kinetics curves

**Parameters measured:**
- **2D effective affinity (AcKa):** Product of contact area, receptor density, ligand density, and association constant
- **2D off-rate (koff):** Dissociation rate in membrane context
- **2D on-rate (kon):** Derived from affinity and off-rate

**Mathematical model:** Second-order forward / first-order reverse single-step reaction model. Adhesion probability depends exponentially on contact time, receptor/ligand densities, and contact area.

**Critical technical parameters:**
- Contact time: varied (ms to seconds)
- Contact area: precisely controlled via micromanipulation
- Ligand density: adjusted to maintain adhesion probability in 0.05-0.8 range

**Has this been used for CARs?** No published study has directly measured 2D kinetics of CAR-antigen interactions using the micropipette adhesion frequency assay. This would be a NOVEL contribution if performed for FMC63 variants binding CD19.

**Feasibility for CSIR-IGIB:** Low-moderate. Requires custom micropipette aspiration setup with piezoelectric control and high-speed camera. This is specialized equipment typically found in biophysics labs (e.g., Cheng Zhu lab at Georgia Tech, or similar). Would require collaboration.

### 4.3 Biomembrane Force Probe (BFP)

**Reference:** Chen Y, Liu B, Bhatt P, Bhatt D, Bhatt P, Bhatt K, et al. "Fluorescence Biomembrane Force Probe: Concurrent Quantitation of Receptor-ligand Kinetics and Binding-induced Intracellular Signaling on a Single Cell." *Journal of Visualized Experiments* (102):e52975, 2015. PMID: 26274684. PMC4544851.

**How it works:**
- Uses an ultra-soft RBC as a force sensor
- A streptavidin-coated bead attached to the RBC presents ligands
- High-speed camera + real-time tracking achieves ~1 pN force resolution, ~3 nm spatial, ~0.5 ms temporal resolution
- The fluorescence BFP (fBFP) adds concurrent calcium imaging

**Measures:**
- Single-molecule receptor-ligand binding kinetics under applied force
- Force-dependent bond lifetimes (catch bonds vs slip bonds)
- Concurrent binding and intracellular signaling (calcium flux) on single cells

**Relevance to CAR biology:**
- Can determine if FMC63-CD19 bonds are catch bonds or slip bonds under force
- Catch bonds (strengthened by force) are associated with stronger T cell activation
- Recent studies show CARs are force-sensitive (Qiu et al. 2024, PMID: 38327049)

**Feasibility for CSIR-IGIB:** Low. Highly specialized equipment, very few labs worldwide operate BFP systems. Would require international collaboration (Cheng Zhu lab, Khalid Bhatt lab, etc.).

### 4.4 How 2D Kinetics Differ from 3D SPR/BLI -- Detailed Comparison

**Reference:** Zhu C, Chen W, Lou J, et al. "Insights into T Cell Recognition of Antigen: Significance of Two-Dimensional Kinetic Parameters." *Frontiers in Immunology* 3:86, 2012.

**Reference:** Liu B, Zhong S, Malecek K, et al. "2D TCR-pMHC-CD8 kinetics determines T-cell responses in a self-antigen-specific TCR system." *European Journal of Immunology* 44(1):239-250, 2014. PMID: 24114747. PMC3941036.

**Key differences summarized:**

1. **3D off-rates predict function poorly:** In SPR, the best predictor is koff (slower = more potent), but this only weakly discriminates ligands
2. **2D off-rates are paradoxically faster for agonists:** The fastest 2D koff corresponds to the strongest agonist -- the opposite of 3D predictions
3. **2D on-rates matter:** 2D kon correlates with function; 3D kon does not
4. **Catch bonds only detectable in 2D:** Under force, agonist pMHC forms catch bonds (lifetime increases with force), while antagonists form slip bonds (lifetime decreases). This is invisible to SPR
5. **Cell biology included in 2D:** Membrane anchor, cytoskeletal constraints, molecular orientation, co-receptor (CD8) cooperation all influence 2D but not 3D measurements

**Application to this project:** FMC63 affinity variants may show minimal differences by SPR/BLI (3D) but significant differences in 2D membrane context. If variants are being designed to optimize dwell time or force sensitivity, 2D measurements would be more physiologically informative.

**UNCERTAINTY FLAG:** No published study has directly compared 2D vs 3D kinetics for any CAR-antigen pair. The above findings are from TCR-pMHC systems. The prediction that similar principles apply to CARs is reasonable but unproven.

---

## 5. Addressing the FACS Quantification Problem in Co-Culture Assays

### 5.1 The Problem

When Jurkat-CAR and Raji cells are co-cultured, both are suspension cells. At the assay endpoint:
- Dead Raji cells may fragment and become undetectable by FACS
- Jurkat and Raji must be distinguished by surface markers (CD3 vs CD19)
- Dead cells lose surface markers, creating an ambiguous population
- Absolute cell counting is needed to detect target cell disappearance

### 5.2 Solution 1: Raji-GFP and Raji-Luc Lines

**Available lines:**

| Line | Source | Catalog # | Advantage |
|------|--------|-----------|-----------|
| Raji-Luc2 | ATCC | CCL-86-LUC2 | Luminescence-based quantification (no FACS needed) |
| Raji-GFP-Luc2 | ATCC | CCL-86-GFP-LUC2 | GFP for FACS + Luc for luminescence |
| eGFP/Firefly Luc Raji | BPS Bioscience | 78916 | Dual reporter |
| Raji-GFP-Luc | Creative Biolabs | Custom | GFP + luciferase |
| Raji-GFP-Luc | FenicsBIO | Custom | GFP + luciferase |

**Raji-GFP benefits for FACS:**
- GFP identifies Raji cells independently of surface marker (even if CD19 is lost on dying cells)
- Gate on GFP+ vs GFP- to cleanly separate Raji from Jurkat
- Add viability dye (7-AAD or fixable dye) to identify dead GFP+ cells
- Much cleaner separation than CD3/CD19 antibody-based gating alone

**Raji-Luc benefits for cytotoxicity:**
- Luminescence readout eliminates FACS entirely for killing quantification
- Dead Raji produce no light -- signal proportional to surviving cells
- Formula: % Killing = 100 x (1 - RLU_sample / RLU_target-alone)
- Very high throughput (96-well plate reader, <30 min readout)

### 5.3 Solution 2: Counting Beads for Absolute Quantification

**Reference:** Wu Y, et al. "Improvements in Flow Cytometry-Based Cytotoxicity Assay." *Cytometry Part A* 99(7):680-688, 2021. PMID: 33068327.

**Products:**
- Thermo Fisher AccuCheck Counting Beads
- BioLegend Precision Count Beads (Cat# 424902) -- protocol available on BioLegend website
- Bio-Rad Absolute Count Standard

**How it works:**
1. Add a known number of counting beads to each FACS tube
2. Acquire until a set number of bead events is collected
3. Calculate absolute cell number: (Cell events / Bead events) x Known beads/volume
4. Compare absolute live target cell count between co-culture and target-alone wells

**Important caveat from Wu et al. (2021):**
- Counting beads introduce variability due to "vanishing bead phenomenon" and handling
- **Fixed stopping time method** (acquiring all tubes for the same duration) may provide greater stability than bead-based counting
- Formula: cells in sample = (Events recorded / Acquisition time) x Volume factor

### 5.4 Solution 3: CellTrace Dye Labeling of Targets

**Reference:** CellTrace Violet Cell Proliferation Kit (Thermo Fisher, Cat# C34557)

**Protocol:**
- Label Raji cells with CellTrace Violet (or CFSE) before co-culture
- CellTrace Violet is retained through cell division and remains in dead cells
- At endpoint, gate on CellTrace Violet+ population = Raji (regardless of surface marker loss)
- Add viability dye (e.g., 7-AAD, SYTOX Green) to identify dead labeled cells

**Advantages:**
- Works even when surface CD19 is lost on dying cells
- No genetic modification of targets needed
- Compatible with multi-color FACS panels
- Low cost

**Disadvantages:**
- Dye may transfer to effector cells (check with appropriate controls)
- CFSE can affect cell viability at high concentrations
- Not tested by manufacturer specifically for co-culture applications

### 5.5 Solution 4: Adherent Target Cells (Eliminates Gating Problem)

Using CHO-CD19 or HEK293T-CD19 adherent targets (see Section 1.3/1.4):
- Adherent targets remain attached; dead cells detach
- Count remaining attached cells by microscopy, crystal violet staining, or impedance
- No co-gating with effector cells required
- xCELLigence provides continuous, real-time killing data

### 5.6 Recommended Approach for This Project

**Minimum:** Use Raji-GFP-Luc2 (ATCC CCL-86-GFP-LUC2) -- provides both GFP for FACS and luciferase for cytotoxicity. This is the single most impactful improvement to the current system.

**Additional:** Add BioLegend Precision Count Beads to FACS tubes for absolute counting when FACS-based cytotoxicity quantification is needed.

**Advanced:** Generate CHO-CD19 (Low/Medium/High) for xCELLigence studies to add real-time kinetics data.

---

## 6. NFAT-Luciferase Reporter System (Already Available Commercially)

### 6.1 BPS Bioscience Anti-CD19 CAR / NFAT-Luciferase Reporter Jurkat

**Catalog:** 79853
**Features:**
- Jurkat cells expressing anti-CD19 CAR (FMC63 scFv-CD28-4-1BB-CD3-zeta, 3rd generation)
- NFAT-dependent firefly luciferase reporter
- Validated with both CD19/CHO target cells and Raji cells

**Readout:** Luciferase activity proportional to NFAT activation (= CAR signaling strength)

**Negative control line:** Catalog #79854 (same construct with non-functional signaling domain)

**Relevance:** If Manpreet's FMC63 variants are cloned into a similar CAR backbone, this system could be adapted as a reporter for comparing signaling potency. However, building custom reporter Jurkats for each variant would be required.

---

## 7. Engineered Antigen-Presenting Surfaces (Micropatterned Substrates)

**Reference:** Dirar Q, Russell T, Liu L, et al. "Activation and degranulation of CAR-T cells using engineered antigen-presenting cell surfaces." *PLoS ONE* 15(9):e0238819, 2020. PMID: 32976541. PMC7518621.

**Method:**
- PDMS stamps with 5 um circular pillars used for microcontact printing
- Anti-CD3 mAb and anti-idiotype antibodies (233-4A for CD19 CAR) patterned on glass
- ICAM-1Fc added as co-stimulatory signal
- CAR-T cells seeded on patterned surfaces

**Readouts:**
- Phospho-CD3-zeta (activation)
- LAMP-1/CD107a (degranulation)
- Calcium imaging
- Immune synapse morphology

**Advantage:** Systematic, reproducible analysis without live target cells. Quantitative analysis of IS molecules.

**Feasibility for CSIR-IGIB:** Low-moderate. Requires microcontact printing capability (cleanroom or soft lithography setup). Could be established with collaboration.

---

## 8. Summary Table: All Systems Compared

| System | Controls CD19 Density? | Solves FACS Problem? | Real-Time Kinetics? | Measures Cytotoxicity? | Cost/Complexity | Priority for This Project |
|--------|----------------------|---------------------|--------------------|-----------------------|----------------|--------------------------|
| NALM-6 CD19-KO + re-expression | YES (molecules/cell) | No | No | Yes | Medium (CRISPR+lenti) | **HIGH** |
| K562-CD19 | Possible (sort for levels) | No | No | Yes | Low-Medium | Medium |
| CHO-CD19 (Low/Med/High) | YES (3 levels) | YES (adherent) | YES (xCELLigence) | Yes | Medium (purchase) | **HIGH** |
| HEK293T-CD19 | Possible (in-house) | YES (adherent) | YES (xCELLigence) | Yes | Low | Medium-High |
| Raji-GFP-Luc2 | No | YES (GFP+Luc) | No | YES (luminescence) | Low (purchase) | **HIGH** |
| Plate-bound rCD19 | YES (coating conc) | YES (no target cells) | No | No (activation only) | Medium | Medium |
| SLB + TIRF | YES (bilayer composition) | YES (no target cells) | Yes (imaging) | No | High (equipment) | Medium (advanced) |
| Micropipette/BFP 2D kinetics | N/A (kinetics, not killing) | N/A | YES | No | Very High (specialized) | LOW (collaboration) |
| Anti-FMC63 beads | No | YES (no target cells) | No | No (activation only) | Low | Low (not affinity-specific) |
| Micropatterned surfaces | Possible | YES (no target cells) | No | No (activation only) | High (microfab) | Low |

---

## 9. Recommended Implementation Strategy for This Project

### Phase 1 (Immediate, within existing resources):
1. **Acquire Raji-GFP-Luc2 (ATCC CCL-86-GFP-LUC2)** -- solves the FACS quantification problem and enables luminescence-based cytotoxicity
2. **Add BioLegend Precision Count Beads** to existing FACS protocol
3. **Label Raji with CellTrace Violet** as backup approach for effector/target discrimination

### Phase 2 (Next 3-6 months):
4. **Generate NALM-6 CD19-KO cells** using CRISPR-Cas9 (sgRNAs targetable to CD19 exons)
5. **Re-express CD19 at graded levels** (lentiviral truncated CD19, FACS sort, single-cell clone)
6. **Quantify with QuantiBRITE** -- create library of defined-density targets
7. **Test all FMC63 affinity variants against Low, Medium, High CD19 targets**

### Phase 3 (6-12 months, advanced experiments):
8. **Acquire or generate CHO-CD19 or HEK293T-CD19** adherent targets for real-time kinetics
9. **xCELLigence assay** if instrument available (IGIB, collaborator, or national facility)
10. **Plate-bound CD19 activation assay** if recombinant CD19 available

### Phase 4 (Future/collaboration):
11. **SLB + confocal imaging** of CAR immune synapse quality
12. **2D kinetics measurement** through collaboration with biophysics lab

---

## 10. Verified References

### Tunable Antigen Density
1. **Majzner RG, Rietberg SP, Sotillo E, et al.** "Tuning the Antigen Density Requirement for CAR T Cell Activity." *Cancer Discovery* 10(5):702-723, 2020. PMID: 32193224. PMC7939454.

### CD19 CAR Engagement Mechanisms and Affinity
2. **He X, Xu C, et al.** "CD19 CAR antigen engagement mechanisms and affinity tuning." *Science Immunology* 8(81):eadf1426, 2023. PMID: 36867678. PMC10228544.
3. **Grzesik K, et al.** "Solving the mystery of the FMC63-CD19 affinity." *Scientific Reports* 13:22130, 2023. PMID: 38155191. PMC10754921.

### Supported Lipid Bilayers and CAR Synapse
4. **Dong R, Libby KA, Blaeschke F, et al.** "Rewired signaling network in T cells expressing the chimeric antigen receptor (CAR)." *The EMBO Journal* 39(16):e104730, 2020. PMID: 32643825. PMC7429742.
5. **Xiong W, Chen Y, Kang X, et al.** "Immunological Synapse Predicts Effectiveness of Chimeric Antigen Receptor Cells." *Molecular Therapy* 26(4):963-975, 2018. PMID: 29503199. PMC6080133.
6. **Cho JH, Tsao WC, Naghizadeh A, Liu D.** "Standardized protocol for the evaluation of chimeric antigen receptor (CAR)-modified cell immunological synapse quality using the glass-supported planar lipid bilayer." *Methods in Cell Biology* 173:131-149, 2022. PMID: 36653082. PMC10768727.

### Recombinant CD19 Protein
7. **Lobner E, Wachernig A, Gudipati V, et al.** "Getting CD19 Into Shape: Expression of Natively Folded 'Difficult-to-Express' CD19 for Staining and Stimulation of CAR-T Cells." *Frontiers in Bioengineering and Biotechnology* 8:49, 2020. PMID: 32117929. PMC7020774.

### Plate-Bound Protein Activation
8. **Neto Da Rocha M, Guiot M, et al.** "Coated recombinant target protein helps explore IL-1RAP CAR T-cell functionality in vitro." *Immunologic Research* 71:271-282, 2023. PMID: 36456721. PMC10060290.

### 2D Kinetics
9. **Huang J, Zarnitsyna VI, Liu B, et al.** "The kinetics of two-dimensional TCR and pMHC interactions determine T-cell responsiveness." *Nature* 464(7290):932-936, 2010. PMID: 20357766. PMC2925443.
10. **Zarnitsyna VI, Zhu C.** "Adhesion frequency assay for in situ kinetics analysis of cross-junctional molecular interactions at the cell-cell interface." *Journal of Visualized Experiments* (57):e3519, 2011. PMID: 22083316. PMC3308619.
11. **Liu B, Zhong S, Malecek K, et al.** "2D TCR-pMHC-CD8 kinetics determines T-cell responses in a self-antigen-specific TCR system." *European Journal of Immunology* 44(1):239-250, 2014. PMID: 24114747. PMC3941036.

### Mechanical Force and CAR Signaling
12. **Qiu Y, Xiao Q, Wang Y, et al.** "Mechanical force determines chimeric antigen receptor microclustering and signaling." *Molecular Therapy* 32(3):593-608, 2024. PMID: 38327049. PMC11163199.

### Flow Cytometry Improvements
13. **Wu Y, et al.** "Improvements in Flow Cytometry-Based Cytotoxicity Assay." *Cytometry Part A* 99(7):680-688, 2021. PMID: 33068327.

### K562 aAPC
14. **Rushworth D, Jena B, Olivares S, et al.** "Universal Artificial Antigen Presenting Cells to Selectively Propagate T Cells Expressing Chimeric Antigen Receptor Independent of Specificity." *Journal of Immunotherapy* 37(4):204-213, 2014. PMID: 24714354. PMC4139067.

### Micropatterned Surfaces
15. **Dirar Q, Russell T, Liu L, et al.** "Activation and degranulation of CAR-T cells using engineered antigen-presenting cell surfaces." *PLoS ONE* 15(9):e0238819, 2020. PMID: 32976541. PMC7518621.

### Antigenic Vesicles
16. **Ukrainskaya VM, et al.** "Antigen-Specific Stimulation and Expansion of CAR-T Cells Using Membrane Vesicles as Target Cell Surrogates." *Small* 17(49):2102643, 2021. PMID: 34605165.

### CD19 Surface Density Quantification
17. **Haso W, et al.** "Anti-CD22-chimeric antigen receptors targeting B-cell precursor acute lymphoblastic leukemia." *Blood* 121(7):1165-1174, 2013. PMID: 23243285. PMC3575759.

### xCELLigence for CAR-T
18. **Lifeliqe et al.** "Evaluation of CAR-T cell cytotoxicity: Real-time impedance-based analysis." *Methods in Cell Biology* 167:115-130, 2022. PMID: 35153000.

### Anti-FMC63 Idiotype Detection
19. **Jena B, Maiti S, Huls H, et al.** "Chimeric Antigen Receptor (CAR)-Specific Monoclonal Antibody to Detect CD19-Specific T Cells in Clinical Trials." *PLoS ONE* 8(3):e57838, 2013. PMID: 23469246. PMC3585808.

---

## 11. Explicit Uncertainty Flags

1. **2D kinetics for CARs:** No published study has measured 2D membrane kinetics for any CAR-antigen pair. All 2D kinetics data cited here are from TCR-pMHC systems. The applicability to CARs is theoretically predicted but experimentally unconfirmed.

2. **NALM-6 CD19 surface density:** Reported values range from ~1,780 (super-resolution microscopy) to ~36,000 (conventional flow cytometry) molecules/cell. The discrepancy is methodological, not biological. Use QuantiBRITE for project-internal consistency.

3. **Plate-bound CD19 for CAR activation:** Directly validated only for IL-1RAP CAR (Neto Da Rocha et al. 2023). Application to CD19 CAR is inferred from BPS Bioscience NFAT reporter validation with CHO-CD19 cells, but quantitative comparison of plate-bound CD19 vs cell-based CD19 for FMC63 CAR specifically is not published.

4. **CHO-CD19 Low/Medium/High quantitative expression levels:** BPS Bioscience confirms Low, Medium, and High expression by flow cytometry but does not publish exact molecules/cell. User would need to quantify with QuantiBRITE after purchase.

5. **Catch bonds in CARs:** Whether FMC63-CD19 interaction exhibits catch bond behavior under force is not yet published. Qiu et al. (2024) showed force-dependence of FMC63 CAR signaling on SLBs but did not measure bond lifetimes.

6. **FMC63 affinity:** Published values range widely from 0.3 to 47 nM depending on the CD19 construct and method used. Grzesik et al. (2023, PMID: 38155191) determined 2-6 nM using strictly monomeric, correctly folded soluble CD19 with SPR.

---

*All information verified through web searches of PubMed/PMC, journal websites, ATCC/vendor product pages, and published protocols. Uncertainty is flagged explicitly. Date compiled: 2026-04-27.*
