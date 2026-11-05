# Poland beech, all sites: is there a common cause beyond the ΔT cue? Pre-registered 2026-11-05, BEFORE the weather for the 7 new sites or any new statistic

reviewed: false. Follows `MAST_CONDITIONAL_GATE.md`, where triple 008-009-010 VANISHED at n = 72 (residual V +1.27, p = 0.08).
This gate adds power by pooling every triple in the study.

## Sites and years (rule fixed now; metadata only so far)
MASTREE+ study D00013, beech sites with ≥ 30 years: 008–017 (10 sites). Analysis years = years ≥ 1942 in which every included site
has a value. If fewer than 50, repeatedly drop the site with the fewest years until ≥ 50. All triples are then analysed on the
same years, so one joint bootstrap applies.

## Statistics
- Per triple: V (eq. 16, as in MAST_CEILING_GATE) on median-split series. Stage 1 uses the raw values; stage 2 uses residuals after
  per-site OLS on its own ΔT (Kelly cue from ERA5 June–July means, as in MAST_CONDITIONAL_GATE).
- **Primary (one test per stage):** V̄ = the mean of V over all triples. Under "every triple is compatible with pairwise drivers",
  every V ≤ 0, so V̄ ≤ 0. Joint moving-block bootstrap over years (block 3, 10⁵ resamples). One-sided p = P(V̄* ≤ 0); α = 0.05.
- **Secondary:** per-triple p from the same resamples, Holm across triples (10⁵ resamples, so the resolution suffices for ≤ 120 triples).
  Also descriptive: residual V against the triple's minimum pairwise distance.

## Outcomes
- **RESIDUAL COMMON CAUSE:** stage-2 V̄ significant. Something common to the stands remains beyond the ΔT cue: pollen
  history, another weather channel, or protocol.
- **CUE SUFFICES (at this power):** stage-1 V̄ significant, stage-2 not.
- **NO-BASE:** stage-1 V̄ not significant.

## Prediction (in advance)
Stage 1 clearly significant. Stage 2 V̄ significant (RESIDUAL COMMON CAUSE): the triple-level residual synchrony was E ≈ 0.5–0.6,
above √2 − 1, and pooling adds power.

## Result (2026-11-05): NO-BASE (prediction failed)
Script `verification/mast_poland_pooled_gate.py` (80 s). All 10 sites kept, giving **53 common years (1951–2019)**. Site 015's
short record set the common window, down from 72 years in the triple gate.
- **Stage 1 (raw):** V̄ = +0.62, but the bootstrap 5% point is −0.40, p = 0.17. 69% of the 120 triples have point V > 0. Min
  per-triple p = 0.005 (009-012-013, V = +4.48). 0 Holm-significant.
- **Stage 2 (| ΔT):** V̄ = +0.44, p = 0.21. 68% point V > 0. 0 Holm-significant. corr(V, min distance) = −0.21 (stage 1: −0.34).
- **Verdict NO-BASE:** the pooled design cannot even demonstrate the unconditional common cause that the single 72-year triple showed.
- **Why (design lessons, recorded, not patched):**
  1. Requiring every site to share years cost 19 years.
  2. The mean over 120 overlapping triples dilutes the strongly synchronous ones with weak ones.
  3. The bootstrap distribution of a median-split statistic is wide at n ≈ 50.

  Better designs, each needing its own pre-registration: per-triple common years with one pre-chosen triple per sub-region, or
  simultaneous bootstrap lower bounds across a small pre-chosen family (max-type). [Corrected 2026-11-05: an earlier draft proposed
  a circular-shift null. That is wrong here: shifting breaks ALL cross-site dependence, so it tests 'any synchrony', not
  'beyond the pairwise ceiling'. The correct null sits on the ceiling (V = 0), which is what bootstrap lower bounds on V test.]
- Descriptive: point violations stay common after conditioning (68%), and V falls with distance. This is suggestive of a residual,
  distance-dependent common cause (pollen coupling would predict exactly that), but **not demonstrated**.
