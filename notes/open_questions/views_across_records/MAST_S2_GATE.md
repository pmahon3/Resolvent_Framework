# Beech common-cause test with S2 + detrending: pre-registered 2026-11-05, BEFORE any S2 statistic on real data

reviewed: false. Uses the statistic adopted in `CEILING_POWER_STATS.md` (S2 = max over q ∈ {1/3, 1/2, 2/3} of eq.-16 V) and the
detrending fix from the audit (V1). Disclosure: earlier gates have shown point V for these data (median-split, undetrended). S2 values
are unseen.

## Families (fixed now)
- **F1, Poland within-study:** all triples of study D00013 sites with ≥ 30 years, each triple on **its own** common years (≥ 50).
- **F2, cross-study far:** all triples of beech sites (≥ 30 years) from three different Study_IDs, every pair > 100 km apart, on their
  own common years (≥ 30).

## Procedure
Per triple: linear detrend of each site's series on year (OLS, within the triple's window); S2; moving-block bootstrap (b = 3, no wrap,
20 000 resamples). One-sided p = P(S2* ≤ 0). Holm within each family (α = 0.05). The resolution 5×10⁻⁵ suffices for families up to
~1000 at this α.

## Outcomes
- Per family: the number of Holm-significant triples (a common ancestor required: regional driver, shared history, or shared protocol for F1).
- F2 significant triples would show that a common cause links beech stands in different programmes > 100 km apart, where shared protocol
  is excluded and pollen coupling is implausible.

## Prediction (in advance)
F1: a majority of triples with ≥ 60 common years significant. F2: 0–5% significant (cross-study synchrony was weak, median E 0.11).
