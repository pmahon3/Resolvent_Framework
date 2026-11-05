# Does synchrony need a common cause? A model-free test for three or more sites

reviewed: false. 2026-11-05. Methods note (draft). **Unaudited:** run `/audit full` before sharing (claimed types:
7 methodology, 6 translation). Collection: `cyclic_marginal/views_across_records_taxonomy.json`.

## 1. A worked case
Three ponds. Each pair shares its own stream, each stream independently has good and bad years, and nothing is shared by all
three. Each pond responds only to its two streams. How often can all three ponds agree (all frogs, or all none) if each has frogs
half the time?

Best arrangement: a pond has frogs only when both of its streams are good, with each stream good with probability 1/√2.
- All three have frogs when all three streams are good: (1/√2)³ ≈ 0.354.
- All three are empty when at least two streams are bad: ≈ 0.207.
- Total agreement: (3√2 − 2)/4 ≈ **0.561**.

Independent ponds give 0.25. **No arrangement of pairwise drivers beats 0.561, whatever the mechanism** (Gisin et al. 2020, below).
Anything more coordinated needs something common to all three.

## 2. The test
For each site, split its annual series at the site's own median ("high" vs "low" year). For each pair of sites, E = (fraction of
years they agree) − (fraction they disagree).

- **Bound** (Gisin, Bancal, Cai, Remy, Tavakoli, Zambrini Cruzeiro, Popescu & Brunner 2020, *Nat. Commun.* 11:2378, ineq. 13; the
  general-margin form is their eq. 16). If each pair of sites shares only its own independent driver, then for every pair k:
  (1 − |E_k|)² ≥ sum of the squared E of the other two pairs.
- **Violation ⇒** some common ancestor of all three sites exists. That holds under any mechanism of response, including any local
  randomness, and in any physics with independent sources.
- **No violation ⇒** nothing. Pairwise drivers can explain the data, but so can a weak common one.
- **Where it bites:** for equal pairs, only when E > √2 − 1 ≈ 0.41, i.e. sites agree in more than ~70% of years.

## 3. The pipeline
1. **Detect.** Compute V = (largest left-minus-right excess of the bound). Test V > 0 with a moving-block bootstrap over years.
2. **Name a candidate centre.** Choose a driver measured at each site (e.g. a weather cue). Residualise each site's series on it and
   re-test. If the violation disappears, the candidate accounts for the common cause, as far as the data can show. If it persists,
   something else is common.
3. **Centre in space or in time.** A violation means a common ancestor, which can be a regional driver (sites respond at once)
   or shared history through dispersal (a site's past influences its neighbours' present). Lags along dispersal paths separate them.
4. **Rule out measurement centres.** A shared observer, lab, protocol or calibration is also a common cause. Prefer triples from
   independent programmes, and report same-programme triples separately.

## 4. Worked results (NTL-LTER lakes, MASTREE+ beech; pre-registered gates in this folder)
- **Lake summer water temperature** (5 Wisconsin lakes, ~45 years): E = 0.73–0.91, 10/10 triples violate. Regional weather is the
  centre, as expected: the control works at n ≈ 45.
- **Lake zooplankton** (Daphnia, copepods, rotifers): 0/10 triples per group. The isolated lakes' biology keeps its own time,
  consistent with the known low "temporal coherence" of biological variables.
- **Beech masting:** sites from different programmes 300–900 km apart do not violate (median E 0.11). Within regional programmes
  (100–400 km) synchrony is strong (E 0.7–0.86).
- **Poland, three beech sites** (1951–2022): a clear violation (V = 2.97, p = 0.008). After conditioning on the Kelly ΔT cue (last
  summer's warmth minus the summer before), V drops to 1.27, p = 0.08. The cue explains only 5–9% of each site's own variation,
  yet removes most of what the sites share. A weak signal every stand hears is what a centre looks like.
- **Pooled test over all 10 Polish sites:** NO-BASE (p = 0.17 even unconditionally). The all-sites common window cut n to 53, and the mean
  over 120 triples diluted the signal. Point violations persist after conditioning (68% of triples) and weaken with distance:
  suggestive of a residual, distance-dependent common cause (pollen?), not demonstrated. `MAST_POLAND_POOLED_GATE.md`.

## 5. Design rules learned
- Only strongly synchronised sets are testable (E > ~0.41). Weak synchrony is never evidence against a common cause.
- **Bootstrap resolution must beat the multiple-testing threshold.** With B resamples the smallest p is 1/B, so B must exceed about
  20 × (number of tests)/α. One gate here was unable to detect anything for this reason.
- Prefer one pre-chosen triple per region, or a pooled statistic (mean V over triples; under the null every V ≤ 0).
- Same-programme triples mix real and protocol common causes.
- Don't pool by averaging over many overlapping triples, and don't force a common year window across many sites: both cost
  more power than pooling gains. A better null for many triples: circularly shift whole series to break cross-site alignment.

## 6. What is owned and what is new
- **Owned:**
  - the bound (Gisin et al. 2020; the triangle-network literature: Fritz 2012, Wolfe–Spekkens–Fritz inflation, Rosset–Gisin–Wolfe);
  - common-ancestor inference (Steudel–Ay);
  - synchrony science (Moran 1953; Liebhold–Koenig–Bjørnstad 2004; Sheppard et al. 2016; Walter et al. 2017; Reuman et al. 2023);
  - masting cues (Kelly et al. 2013);
  - temporal coherence of lakes (Magnuson, Kratz et al.).
- **New, as far as two scouts found:** carrying a network causal-compatibility bound into ecology, as a model-free test that
  synchrony *requires* a common cause; the condition-on-a-named-centre step; and the space/time reading of a violation. In ecology,
  concordance between data sources is currently checked only inside fitted models (Goldstein et al. 2026, *J. Anim. Ecol.*, who
  list model-free tests as future work).

## 7. Limits
- Binarisation discards magnitude. Conditioning is linear. Years are treated as exchangeable within blocks.
- Three sites at a time. Larger networks need inflation-type bounds.
- A violation says that a common cause exists, never which one. Naming it takes step 2, one candidate at a time.
