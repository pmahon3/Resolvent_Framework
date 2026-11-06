# Frustration in a real community: zooplankton species within lakes (pre-registered 2026-11-06, before running)

reviewed: false. Theory: `HYPERGRAPH_CENTRES.md` F2 (owned, Boman et al. 2005). A triangle can require a centre beyond pairs only if it is
**frustrated** (product of correlation signs = +1: zero or two negative edges). A triangle with one or three negative edges is **antibalanced**,
and pairwise sources explain it whatever its strength. Competition (A–B negative) inside a shared environment (A–C, B–C positive) gives
antibalanced triangles, which hide the shared driver at correlation level.

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
