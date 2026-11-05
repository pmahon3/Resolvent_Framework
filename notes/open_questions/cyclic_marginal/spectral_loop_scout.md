# Spectral loop scout: cross-spectra from separate campaigns, closure phase, epsilon-relaxation

reviewed: false. 2026-11-05.

Scope: web scout, standard-mode searches only (about 20), no extended mode. Shelf checked first (grep of SHELF_INDEX, taxonomies, cyclic_marginal/*.md): no entry for Robinson sheaf radius, Grone-Johnson-Sa-Wolkowicz, Barrett-Johnson-Loewy, Georgiou covariance completion, Jennison closure phase. "Contextual fraction" and Higham/Georgescu appear in cyclic_marginal files (already known). Not re-reported as new: CbD/DKC 2020, Capotorti-Vantaggi, Vorob'ev, BFMY, Berrett-Samworth, Goldstein et al. 2026.

## 1. Verdict table

| | Question | Verdict | Decisive source (read level) |
|---|---|---|---|
| a | PSD / completion test for cross-spectra from separate records | PARTLY OWNED. The matrix mathematics is OWNED (chordal and cycle completion); fitting-type applications exist (aeroacoustics); an explicit "does any common process exist?" test on real cross-spectra NOT FOUND | Grone-Johnson-Sa-Wolkowicz 1984; Barrett-Johnson-Loewy, Memoirs AMS 122(584), 1996 [abstract/catalogue only]; non-synchronous CSM completion, HAL hal-01296491 + IEEE Access 2021 [abstract] |
| b | Closure phase as consistency check outside interferometry | PARTLY OWNED. InSAR phase linking uses closure phase on coherence matrices (as a bias/quality diagnostic); no use as a "common process exists" test across separate campaigns | arXiv 2510.24512 [abstract]; MIRIAD closure doc [skim] |
| c | epsilon-relaxed version | PARTLY OWNED. Robinson's consistency radius is the nearest object but it is a different quantity (section 3); nearest-correlation-matrix repair (Higham 2002) is the standard epsilon-relaxation of (a) in a Frobenius metric | Robinson, arXiv 1805.08927 [definitions read]; Higham 2002 [known] |
| d | Nonlinear / embedding: one attractor across separately recorded series | NOT FOUND as a test. EDM pools replicates (multispatial CCM, hierarchical DS reconstruction) under the assumption of a shared attractor | multispatialCCM docs [skim]; arXiv 2410.04814 [abstract]; CalCOFI EDM slides [skim] |
| e | Ecological / hydrological application | NOT FOUND for compatibility test. Hydrology does vine-copula infilling of ungauged sites (type (i), assumes a joint) | Ahn 2021 HESS 25:4319 [abstract]. Ecology: already in ecology_owner_scout_DEEP.md (Tenan 2017, Goldstein 2026) |

## 2. Per area

**Matrix completion (a).**
- Grone, Johnson, Sa, Wolkowicz, LAA 58 (1984): PD completion exists iff every clique block is PD, for chordal graphs. [known, not re-read]
- Barrett-Johnson-Loewy 1996 Memoir: for a graph whose chordal-reduction is by cycles, completability is decided cycle by cycle. [abstract]. The real 3-cycle condition is the classical correlation-triple bound; the complex/Hermitian version gives exactly cos(Phi) >= (3c^2-1)/(2c^3) at equal coherences. I did not locate a printed statement of the complex-phase 3-cycle formula (the 3x3 determinant reproduces it; the derivation is routine, so likely folklore). Type (ii) as mathematics. Gap: nobody frames it per frequency for cross-spectra from separate campaigns.
- Dreyer-Koehler-Streuer, arXiv 2111.12640: correlation completion via the graph of known entries, PSD if chordal. [abstract/summary]. Type (i) (constructs a completion). Finance context.
- Zare-Chen-Jovanovic-Georgiou, arXiv 1412.3399 and Georgiou 1987: covariance completion for LTI systems; fills unknown covariance entries via nuclear norm. [abstract]. Type (i). Different missing-data pattern (known covariance lags vs. known channel pairs).
- Aeroacoustics "non-synchronous measurements" (HAL hal-01296491; Yu et al., IEEE Access 2021; Bayesian cyclic CSM completion): a moved sub-array gives a block-diagonal cross-spectral matrix, cross-blocks missing, completed by low rank + Hermitian + continuity. [abstract]. This IS the data shape (separate campaigns, pair/block cross-spectra) but the task is type (i) reconstruction under low-rank source models; PSD feasibility and the phase-holonomy obstruction are not stated in the abstracts. Largest unread risk for (a).
- Dahlhaus 2000 (Biometrika / Metrika 51), Eichler: graphical models via partial coherence; assume full multivariate record. [abstract]. No pairwise-compatibility result found.

**Closure phase (b).**
- Jennison 1958 / radio interferometry: closure invariant to antenna-based errors (the holonomy reading is standard there). [skim]
- InSAR phase linking (arXiv 2510.24512; Molan et al. 2020; De Zan et al.): closure phases of the sample coherence matrix; nonzero closure signals estimation error or model violation, and depends on statistics of multilooked pixels. [abstract]. The coherence matrix there comes from ONE joint record (PSD automatic), so closure phase is a model-misfit signal, not a joint-existence test.
- Bispectrum/biphase (EEG): phase sum of three frequency components, a different triple. Not the same holonomy.
- Time sync / lag cycles: pairwise lag network estimation (Liao-Barooah; Wang-Jeske-Serpedin) fits offsets by least squares; no cycle-sum test found.
- Not searched in depth: Singer angular synchronization, Huang-Guibas cycle consistency applied to time-lag estimation (flagged unread).

**epsilon-relaxation (c).** See section 3. Further: Higham nearest correlation matrix (Frobenius, not TV); Abramsky-Barbosa-Mansfield contextual fraction (already on file); CbD (already on file).

**Embedding (d).**
- Deyle-Sugihara 2011 and Ye-Sugihara 2016 take multiple series from one system. I found no source testing that separately recorded series are generated by one attractor. [abstract-level via search summaries only; not read]
- multispatialCCM pools spatially replicated series assuming common dynamics; surrogate nulls test shared seasonality, not attractor compatibility. [skim]
- arXiv 2410.04814 hierarchical DS: shared structure with site-specific variation; type (i).
- Clark 2015 (spatial CCM) and Hsieh 2008 (dewdrop) NOT retrieved by search; unread.

## 3. Robinson consistency radius vs. epsilon*

Robinson (arXiv 1805.08927, Def. 7, Prop. 1): for an assignment a to a sheaf of pseudometric spaces,
c(a) = sup over U subset V of d_U( S(U<=V) a(V), a(U) ).
It compares each value pushed down by the restriction maps with the assignment's own value on the smaller open set. It is a purely LOCAL, overlap-wise inconsistency of a given assignment, with no search over candidate global sections. Prop. 1: if restrictions are K-Lipschitz, D(a,s) >= c(a)/(1+K) for every global section s, D the sup-metric over opens.

epsilon* = min over joint laws P of max over contexts of TV(P|_context, observed marginal) = inf_s D(a,s) (with D = sup of per-context TV).

Relation: DIFFERENT, with a one-way inequality. Robinson's Prop. 1 gives c(a) <= (1+K) * epsilon*; for marginalisation, TV is 1-Lipschitz (K=1), so c <= 2 epsilon*. The converse fails: c(a)=0 only says pairs agree on overlaps (here: single-variable marginals), and the triangle with compressed-failure (cyclic obstruction) has c=0 yet epsilon*>0. So epsilon* is the "distance to nearest global section" that c only lower-bounds; it is not a special case or equal. Caveat: the sheaf of distributions on a cover is a presheaf whose gluing (sheaf) axiom FAILS exactly where there is no joint, so Robinson's global sections would be assignments of compatible local data, not joint laws. Her consistency filtration (maximal eps-consistent sub-covers) is a coarser invariant than epsilon*. Robinson's own papers name D(a,s) as distance to the nearest section only as a bound. I did not read the final 20k characters of the paper nor the sensor-integration paper (1603.01446) beyond summary; a later section may define a "distance to global section" that matches epsilon* (see section 5).

## 4. Search terms used

Robinson "consistency radius" sheaf sensor integration; cross-spectral matrix completion separately recorded; closure phase time series coherence triplet; non-synchronous measurements cross-spectral matrix completion; covariance completion Georgiou Zorzi Ferrante Pavon; convergent cross mapping separately recorded same attractor; pairwise correlation matrices different studies not PSD; Barrett Johnson Loewy cycle completability; dewdrop/hierarchical EDM multiple sites; Completing correlation matrices; lag cycle consistency sensors; Dahlhaus Eichler partial coherence; hydrology non-simultaneous gauges vine copula; bispectrum biphase closure.

## 5. Unread sources that could flip verdicts

1. Aeroacoustic non-synchronous CSM papers (HAL hal-01296491 and follow-ups): if any states PSD feasibility or phase-closure inconsistency across blocks, (a) becomes OWNED in application. Highest risk.
2. Barrett-Johnson-Loewy 1996 full text: if it states the complex/Hermitian cycle condition, the formula is OWNED as mathematics.
3. Robinson 1603.01446 and the last 20k characters of 1805.08927: could contain a minimizing-distance-to-global-section notion equal to epsilon* (flips (c) toward SAME in the local-section reading).
4. Singer angular synchronization / Huang-Guibas applied to inter-sensor time lags: closure-phase-like consistency outside interferometry.
5. Clark 2015 spatial CCM, Hsieh 2008 dewdrop, Ye-Sugihara 2016 methods: any between-series attractor compatibility check.
6. Atmospheric/geophysical "ambient noise" interferometry (triplet or loop closure of travel times/phases between station pairs): not searched; plausible owner for (b).
7. Johnson et al. on Hermitian PSD completion with prescribed phases (e.g. "completion of partial Hermitian matrices"); not searched.
