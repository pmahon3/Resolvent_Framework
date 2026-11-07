# Frustration in a real community: zooplankton species within lakes (pre-registered 2026-11-06, before running)

reviewed: false. Theory: `HYPERGRAPH_CENTRES.md` F2 (owned, Boman et al. 2005). A triangle can require a centre beyond pairs only if it is
**frustrated** (product of correlation signs = +1: zero or two negative edges). A triangle with one or three negative edges is **antibalanced**,
and pairwise sources explain it whatever its strength. Competition (A–B negative) inside a shared environment (A–C, B–C positive) gives
antibalanced triangles, which hide the shared driver at correlation level.

**Convention note (added 2026-11-06, terminology pass).** "Frustrated" in this record means **not antibalanced** (frustration of −R). A signed-graph reader calls product −1 "frustrated" (Toulouse 1977; Zaslavsky; Harary 1953 says "unbalanced"), the opposite on triangles. The record is kept as written. "V_G" below is the same quantity as V₂ = ρ(|R − I|) − 1.

## Data
NTL-LTER zooplankton (ntl37 rev 42), lakes AL, BM, CR, SP, TR. Per lake: species-level taxa (codes not ending in 00; excluding nauplii and unknowns)
present (density > 0) in ≥ 80% of years' summer samples. Take the 8 with the highest mean summer density. Series = summer (Jun–Aug) mean
log10(density + 1) per year. Spearman correlations; years with all 8 present only.

## Measures (per lake)
1. Fraction of negative correlations among the 28 pairs.
2. Of the 56 triangles: the fraction frustrated vs antibalanced.
3. The validated V_G test on the 8 species jointly (Spearman, jitter, Politis–White blocks, ε = ∞, 1000 resamples), detrended and raw: is a common
   cause of ≥ 3 species required?
4. Per frustrated triangle: the triangle V₂ point value (descriptive). Antibalanced triangles have V₂ ≤ 0 by theorem (sanity check).

## Predictions
1. Negative correlations 20–40% of pairs.
2. Antibalanced triangles 30–50%: a substantial share of triples where a shared driver is undetectable even in principle.
3. A whole-set common cause is required in ≥ 3 of 5 lakes (shared lake environment), but weakly.

## Result (2026-11-06). Script `verification/frustration_zooplankton.py` (4 s)
| lake | n (yrs) | negative pairs | antibalanced triangles | max triangle V₂ (frustr.) | whole-set test raw / detrended |
|---|---|---|---|---|---|
| AL | 32 | 0.07 | 0.21 | −0.21 | no / no |
| BM | 41 | 0.25 | 0.46 | −0.17 | no / no |
| CR | 32 | 0.43 | **0.00** | +0.04 | no / no |
| SP | 33 | 0.11 | 0.25 | −0.04 | no / no |
| TR | 34 | 0.04 | 0.11 | +0.13 | **REJECT / REJECT** (T 9.8 vs 8.4; 10.2 vs 9.6) |
- Prediction 1 (20–40% negative pairs): **mostly wrong.** Range 4–43%; 3 of 5 lakes below 20%.
- Prediction 2 (antibalanced 30–50%): **wrong** in 4 of 5. Median 0.21; only BM at 0.46.
- Prediction 3 (common cause in ≥ 3 of 5 lakes): **wrong.** Only Trout Lake requires a common cause of ≥ 3 species (raw and detrended).
- **Structural finding (CR):** 43% negative correlations yet **zero** antibalanced triangles. The negatives must split the 8 species into two groups that
  are positively correlated within and negatively correlated between (every triangle has 0 or 2 negative edges). Competition between guilds, not
  between pairs. Guild-level anticorrelation keeps every triangle frustrated, so it does **not** hide shared drivers. Pairwise-scattered competition (BM) does.
- Reading: zooplankton communities carry mostly frustrated triangles (median 79%), so masking by competition is modest in this data. Within-lake
  common drivers are mostly not demonstrable at n ≈ 33, consistent with the power limits (only strong, wide centres are visible).
