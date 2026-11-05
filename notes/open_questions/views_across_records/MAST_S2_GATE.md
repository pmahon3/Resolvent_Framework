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

## Result (2026-11-05)
Script `verification/mast_s2_gate.py`.
- **F1, Poland within-study:** 120 triples; point S2 > 0 in 81%. **40 Holm-significant** (many at the resolution floor, p = 5×10⁻⁵),
  all among the 84 triples with ≥ 60 common years (40/84 = 48%). Strongest: 008-009-010 (detrended S2 = +4.81). Detrended
  synchrony across Polish beech stands 100–400 km apart **requires a common ancestor in many triples**: regional weather, shared
  history, or the shared monitoring protocol. The prediction ("a majority of n ≥ 60 triples") **narrowly failed** (48%).
- **F2, cross-study far:** 421 triples (n ≈ 30); point S2 > 0 in 17%; **0 significant** (best p = 0.10). The prediction (0–5%) held.
  Power at n ≈ 30 is low (validation: n = 45 already weak), so this is a weak null, not evidence of independence.
- Reading: with S2 and detrending the instrument now shows a widespread common cause *within* a regional programme, which it could not
  before (median split: 0 Holm-significant). Within-study triples cannot separate weather from protocol. A protocol-free test
  needs long cross-study triples, and the data have none longer than ~31 years.
