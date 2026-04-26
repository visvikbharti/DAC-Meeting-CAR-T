# TCR Clustering and the Serial Engagement Model

## A Comprehensive Review for DAC Meeting
### Manpreet Kour | PI: Dr. Kausik Chakraborty | CSIR-IGIB

---

## 1. The Serial Engagement Model

### 1.1 Original Discovery

The serial engagement (or serial triggering) model was proposed by Salvatore Valitutti, Stefan Muller, Marina Cella, Elisabetta Padovan, and Antonio Lanzavecchia in 1995, published in *Nature*.

**Core observation:** When T cells interacted with antigen-presenting cells (APCs) displaying low antigenic pMHC densities (approximately 100 pMHC per APC), a surprisingly large number of TCRs were triggered --- up to 18,000 per T cell. This was far more than the number of pMHC molecules available, implying that each pMHC molecule must sequentially engage and trigger multiple TCRs.

**Estimated serial engagement capacity:** A single pMHC complex can serially engage and trigger approximately **~200 TCRs** over the course of a T cell-APC interaction.

**Key Reference:** Valitutti S, Muller S, Cella M, Padovan E, Lanzavecchia A. "Serial triggering of many T-cell receptors by a few peptide-MHC complexes." *Nature*. 1995;375(6527):148-151. PMID: 7753171.

### 1.2 Mechanism of Serial Engagement

The serial engagement model operates as follows:

1. A pMHC molecule on the APC surface binds to a TCR on the T cell
2. The bound TCR initiates intracellular signaling (phosphorylation cascades)
3. After a characteristic dwell time (determined by koff), the pMHC dissociates from the triggered TCR
4. The now-free pMHC binds to a new, un-triggered TCR nearby
5. This cycle repeats, with the same pMHC molecule serially triggering multiple TCRs
6. The triggered TCRs are internalized and degraded (TCR downregulation)

**Time per engagement cycle:** The dwell time of individual TCR-pMHC interactions has half-lives measured in seconds (in 3D: 1-75 seconds depending on the pMHC; in 2D: substantially faster). Two-dimensional off-rates are up to 8,300-fold faster than those measured in 3D solution phase, with agonist pMHC dissociating the fastest in 2D (Huang et al., 2010).

### 1.3 Relationship with Kinetic Proofreading

The serial engagement model and the kinetic proofreading model (McKeithan, 1995) are complementary but create a tension:

- **Kinetic proofreading demands longer dwell time:** Each TCR must remain bound to pMHC long enough to complete multiple sequential phosphorylation steps.
- **Serial engagement demands shorter dwell time:** pMHC must dissociate quickly to engage more TCRs.

This creates the "optimal dwell time" (Goldilocks) window:

```
Too Short             Optimal              Too Long
|------ No signal ------|--- Max signal ---|--- Blocked serial engagement ---|
koff too fast           koff just right      koff too slow
(<< 1 sec dwell)        (~1-30 sec dwell)    (>> 30 sec dwell)
```

**Key evidence:** Kalergis et al. (2001) demonstrated that neither low (less than or equal to 10.3 sec) nor high (77 sec) half-life TCR-pMHC interactions, but only intermediate (34 sec) half-life interactions induced efficient cytotoxic function in vivo.

**Key Reference:** Kalergis AM, et al. "Efficient T cell activation requires an optimal dwell-time of interaction between the TCR and the pMHC complex." *Nat Immunol*. 2001;2(3):229-234.

### 1.4 Criticisms and Refinements

The serial engagement model, while influential, has faced several criticisms over its 30-year history:

1. **TCR downregulation overestimation:** Some of the original evidence relied on TCR downregulation as a proxy for triggering. However, TCR co-modulation (bystander downregulation of un-triggered TCRs) may cause overestimation of the number of serially engaged TCRs.

2. **2D vs 3D kinetics discrepancy:** The 2D off-rates measured on cell membranes are dramatically faster than 3D solution measurements, which complicates quantitative predictions of serial engagement rates.

3. **Mechanosensing challenges the model:** The discovery that TCR-pMHC forms catch bonds under force (Liu et al., 2014) suggests that force may prolong bond lifetimes beyond what solution kinetics predict, potentially reducing the rate of serial engagement.

4. **Single-molecule studies:** Direct single-molecule measurement of TCR triggering showed that individual agonist pMHC remain bound to the same TCR for at least several seconds (for the 5c.c7 TCR) and for approximately one minute (for the AND TCR) in living primary T cells (O'Donoghue et al., 2013).

**Key Reference:** Valitutti S. "The Serial Engagement Model 17 Years After: From TCR Triggering to Immunotherapy." *Front Immunol*. 2012;3:272.

**Key Reference:** O'Donoghue GP, et al. "Direct single molecule measurement of TCR triggering by agonist pMHC in living primary T cells." *eLife*. 2013;2:e00778.

---

## 2. TCR Microclusters

### 2.1 Discovery and Definition

TCR microclusters are small, discrete aggregations of TCR molecules and associated signaling proteins that form at the T cell-APC contact interface. They were first described in detail by Alfredo Campi, Rajat Varma, and Michael Dustin in seminal studies published in 2005-2006.

**Definition:** TCR microclusters are submicron-scale signaling units containing TCR, CD3 chains, and associated signaling molecules (ZAP-70, SLP-76, LAT) that form at the periphery of the immunological synapse and serve as the primary sites of TCR signal initiation.

**Key Reference:** Campi A, Varma R, Dustin ML. "Actin and agonist MHC-peptide complex-dependent T cell receptor microclusters as scaffolds for signaling." *J Exp Med*. 2005;202(8):1031-1036.

**Key Reference:** Varma R, Campi A, Yokosuka T, Dustin ML. "T cell receptor-proximal signals are sustained in peripheral microclusters and terminated in the central supramolecular activation cluster." *Immunity*. 2006;25(1):117-127.

### 2.2 Number of TCR Molecules per Microcluster

Quantitative measurements of TCR molecules per microcluster:

| Parameter | Value | Method | Reference |
|-----------|-------|--------|-----------|
| **TCR per microcluster** | ~50-300 | Fluorescence intensity | Yokosuka & Saito, 2010 |
| **Typical estimate** | ~100 TCR molecules | Fluorescence intensity calibration | Dustin et al., various |
| **Microcluster area** | 0.35-0.5 micrometer^2 | Microscopy | Various |
| **Microcluster diameter** | ~0.5-1 micrometer | TIRFM/confocal | Yokosuka et al., 2005 |

The number of TCRs within a microcluster remains remarkably constant regardless of ligand potency --- the size and TCR content of a microcluster are not a function of the pMHC potency. Instead, potency affects the number of microclusters formed and the signaling output per cluster (Crites et al., 2014).

**Key Reference:** Crites TJ, Padhan K, Muller J, et al. "TCR Microclusters Preexist and Contain Molecules Necessary for TCR Signal Transduction." *J Immunol*. 2014;193(1):56-67.

### 2.3 Molecular Composition of Microclusters

TCR microclusters contain a defined set of signaling molecules:

**Constitutively present (even before antigen engagement):**
- TCR-CD3 complexes
- LAT (linker for activation of T cells) --- partitions into microclusters constitutively and independently
- Grb2 --- present at basal levels

**Recruited upon activation:**
- ZAP-70 (phosphorylated)
- SLP-76
- phospho-CD3zeta
- Phospholipase C-gamma (PLC-gamma)
- Vav1

**Constitutively excluded:**
- **CD45** --- excluded from TCR microclusters under all stimulation conditions. This exclusion is a fundamental feature that facilitates signaling by removing the inhibitory phosphatase from the vicinity of activating kinases (Crites et al., 2014).

### 2.4 Formation Kinetics

- **Pre-existing microclusters:** TCR microclusters preexist in unstimulated T cells. The density of pre-existing microclusters is approximately 0.2-0.35 microclusters per micrometer^2, remaining constant over time (Crites et al., 2014).
- **Upon antigen contact:** Microclusters increase in absolute number following engagement, particularly with low-potency ligands.
- **Formation is F-actin dependent:** Whether triggered by physiological pMHC or anti-CD3 antibody (Campi et al., 2005).
- **Rapid formation:** Microclusters form within seconds to minutes of T cell contact with antigen-presenting surfaces.

### 2.5 Signaling from Microclusters vs. the cSMAC

A critical conceptual advance from microcluster research: **Active signaling occurs in peripheral microclusters, NOT in the cSMAC.**

- **Peripheral microclusters (pSMAC region):** Sites of active TCR phosphorylation, ZAP-70 recruitment, and downstream signaling initiation
- **Centripetal transport:** Microclusters move inward toward the center of the synapse via actin retrograde flow
- **Central SMAC (cSMAC):** Microclusters coalesce at the center where signaling is terminated and TCRs are internalized for degradation

This means that sustained signaling depends on the continuous generation of new peripheral microclusters, not on the cSMAC. Disruption of new microcluster formation --- not cSMAC disruption --- terminates signaling.

**Key Reference:** Varma R, Campi A, Yokosuka T, Dustin ML. "T cell receptor-proximal signals are sustained in peripheral microclusters and terminated in the central supramolecular activation cluster." *Immunity*. 2006;25(1):117-127.

---

## 3. Total Number of TCRs on a T Cell Surface

### 3.1 Quantitative Estimates

A typical mature T cell expresses approximately **20,000-30,000 TCR-CD3 complexes** on its surface. This number varies based on:

| T Cell State | Approximate TCR Number | Notes |
|-------------|----------------------|-------|
| **Naive T cell** | ~20,000-30,000 | Resting state |
| **Recently activated** | Reduced (downregulated) | Active TCR internalization |
| **Effector T cell** | Variable | Depends on ongoing stimulation |
| **Memory T cell** | ~20,000-30,000 | Returns to baseline |

### 3.2 TCR Density and Sensitivity

Despite having tens of thousands of TCR molecules on their surface, T cells are capable of detecting as few as 1-10 agonist pMHC molecules on an APC:

- **1 pMHC:** Can trigger calcium signaling in both CD4+ and CD8+ T cells (Irvine et al., 2002; Purbhoo et al., 2004)
- **3 pMHC:** Can lead to functional cell killing in CD8+ cytotoxic T cell blasts
- **10 pMHC:** Sufficient for full immunological synapse formation
- **90-140 pMHC/micrometer^2:** Required for minimal density-dependent activation on planar surfaces

This extraordinary sensitivity --- detecting 1 pMHC among potentially hundreds of thousands of self-pMHC molecules --- is enabled by the combination of serial engagement, kinetic proofreading, TCR pre-clustering, and mechanical force amplification.

**Key Reference:** Purbhoo MA, et al. "T cell killing does not require the formation of a stable mature immunological synapse." *Nat Immunol*. 2004;5(5):524-530.

---

## 4. TCR Pre-clustering and Nanoclusters

### 4.1 Evidence for TCR Pre-clustering Before Antigen Encounter

Before encountering antigen, TCRs are not randomly distributed on the T cell surface. Instead, they exist in pre-formed nanoclusters:

- **Nanocluster size:** 7-30 TCR molecules per nanocluster, with an average radius of 35-70 nm
- **Detection methods:** Super-resolution microscopy (PALM/STORM), electron microscopy, Blue Native PAGE
- **Functional significance:** Pre-clustering enhances sensitivity by increasing local TCR density and enabling cooperative signaling

### 4.2 Lipid and Protein Requirements

**Cholesterol:**
- Required for TCR nanoclustering in T cells
- Specifically binds to the TCR-beta subunit
- Results in recruitment of sphingomyelin to stabilize TCR dimers and nanoclusters

**Cholesterol-sphingomyelin mechanism:**
1. Monomeric TCR localizes in the non-raft (liquid-disordered) phase
2. Cholesterol specifically binds the TCR-beta subunit
3. This recruits sphingomyelin
4. When TCR forms dimers, cholesterol and sphingomyelin are shielded from the liquid-disordered phase
5. This stabilizes the TCR dimer/nanocluster

**Not classical lipid rafts:** Despite the cholesterol dependence, nanoclusters of the resting TCR localize to non-raft domains. The resting TCR localizes in the disordered domain of giant plasma membrane vesicles.

**Key Reference:** Molnar E, Deswal S, Schamel WW. "Nanoclusters of the resting T cell antigen receptor (TCR) localize to non-raft domains." *Biochim Biophys Acta*. 2015;1853(4):958-966.

**Key Reference:** Molnar E, et al. "Cholesterol and sphingomyelin drive ligand-independent T-cell antigen receptor nanoclustering." *J Biol Chem*. 2012;287(51):42664-42674.

### 4.3 The Protein Island Model

Studies using super-resolution microscopy have revealed that the T cell surface is organized into "protein islands" --- nanoscale domains (50-200 nm) containing specific sets of membrane proteins:

- **TCR islands** and **LAT islands** are strongly segregated in resting T cells
- Upon activation, these islands merge and reorganize to form signaling-competent microclusters
- This spatial organization provides an additional layer of regulation for signal initiation

### 4.4 Functional Role of Pre-clustering

Schamel et al. demonstrated that antigen-independent TCR nanoclustering serves two key functions:

1. **Increased avidity:** Nanoclusters increase avidity for multimeric pMHC ligands (such as those on APCs), enhancing sensitivity to low antigen densities
2. **Cooperativity:** TCR molecules within a nanocluster can signal cooperatively, where engagement of one TCR facilitates signaling by neighboring TCRs in the same cluster

**Key Reference:** Kumar R, et al. "Functional role of T-cell receptor nanoclusters in signal initiation and antigen discrimination." *PNAS*. 2016;113(37):E5454-E5463.

---

## 5. Number of Clusters per T Cell Surface

### 5.1 During Immunological Synapse Formation

During the formation of a mature immunological synapse, multiple microclusters form simultaneously at the T cell-APC interface:

**Temporal dynamics:**
1. **Initial contact (0-30 seconds):** Multiple TCR microclusters form at the periphery of the contact zone. Dozens to hundreds of microclusters can form across the contact area.
2. **Sustained signaling (30 sec - minutes):** New microclusters continuously form at the periphery while older ones migrate centripetally.
3. **Centripetal transport (minutes):** Microclusters move inward via actin retrograde flow at rates of ~0.01-0.1 micrometer/second.
4. **cSMAC coalescence (5-30 minutes):** Microclusters merge at the center to form the cSMAC, where signaling is terminated.

### 5.2 Pre-existing Nanoclusters

In unstimulated T cells:
- **Density:** ~0.2-0.35 nanoclusters per micrometer^2 (Crites et al., 2014)
- For a typical T cell surface area of ~300 micrometer^2, this translates to approximately **60-100 pre-existing nanoclusters**
- Each containing 7-30 TCR molecules

---

## 6. Relationship Between Clustering and Affinity

### 6.1 How pMHC Affinity Affects Cluster Formation

- **Higher affinity pMHC:** Generally leads to more robust microcluster formation and stronger signaling output per cluster
- **Lower affinity pMHC:** Can still form microclusters but with reduced signaling intensity; the number of TCRs per microcluster remains constant regardless of ligand potency (Crites et al., 2014)
- **Very weak ligands:** Increase the number of pre-existing microclusters without necessarily triggering productive signaling

### 6.2 Cooperativity in TCR-pMHC Binding Within Clusters

TCR pre-clustering creates conditions for cooperative binding:
- A pMHC that engages one TCR in a nanocluster may facilitate conformational changes that increase the accessibility of neighboring TCRs
- Multivalent pMHC engagement within a cluster generates stronger signals than equivalent monovalent engagement
- This cooperativity contributes to the ability of T cells to discriminate between agonists and weak ligands

---

## References

1. Valitutti S, Muller S, Cella M, Padovan E, Lanzavecchia A. Serial triggering of many T-cell receptors by a few peptide-MHC complexes. *Nature*. 1995;375(6527):148-151.

2. Valitutti S. The Serial Engagement Model 17 Years After: From TCR Triggering to Immunotherapy. *Front Immunol*. 2012;3:272.

3. Campi A, Varma R, Dustin ML. Actin and agonist MHC-peptide complex-dependent T cell receptor microclusters as scaffolds for signaling. *J Exp Med*. 2005;202(8):1031-1036.

4. Varma R, Campi A, Yokosuka T, Dustin ML. T cell receptor-proximal signals are sustained in peripheral microclusters and terminated in the central supramolecular activation cluster. *Immunity*. 2006;25(1):117-127.

5. Crites TJ, Padhan K, Muller J, et al. TCR Microclusters Preexist and Contain Molecules Necessary for TCR Signal Transduction. *J Immunol*. 2014;193(1):56-67.

6. Molnar E, Deswal S, Schamel WW. Nanoclusters of the resting T cell antigen receptor (TCR) localize to non-raft domains. *Biochim Biophys Acta*. 2015;1853(4):958-966.

7. Molnar E, et al. Cholesterol and sphingomyelin drive ligand-independent T-cell antigen receptor nanoclustering. *J Biol Chem*. 2012;287(51):42664-42674.

8. Kumar R, et al. Functional role of T-cell receptor nanoclusters in signal initiation and antigen discrimination. *PNAS*. 2016;113(37):E5454-E5463.

9. O'Donoghue GP, et al. Direct single molecule measurement of TCR triggering by agonist pMHC in living primary T cells. *eLife*. 2013;2:e00778.

10. Huang J, Zarnitsyna VI, Liu B, et al. The kinetics of two-dimensional TCR and pMHC interactions determine T-cell responsiveness. *Nature*. 2010;464(7290):932-936.

11. Kalergis AM, et al. Efficient T cell activation requires an optimal dwell-time of interaction between the TCR and the pMHC complex. *Nat Immunol*. 2001;2(3):229-234.

12. McKeithan TW. Kinetic proofreading in T-cell receptor signal transduction. *Proc Natl Acad Sci USA*. 1995;92(11):5042-5046.

13. Yokosuka T, Saito T. The immunological synapse, TCR microclusters, and T cell activation. *Curr Top Microbiol Immunol*. 2010;340:109-122.

14. Purbhoo MA, et al. T cell killing does not require the formation of a stable mature immunological synapse. *Nat Immunol*. 2004;5(5):524-530.
