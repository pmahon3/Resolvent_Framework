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
