# Lake physics harness (strongly tied variables): pre-registered 2026-11-05, BEFORE download

reviewed: false. Follows `LAKE_HARNESS.md` (zooplankton: TOOTHLESS; moderate ties keep the triangle slack).
Here the variables are chosen because they are tightly coupled: cold water holds more oxygen.

## Data
NTL-LTER Physical Limnology of Primary Study Lakes (EDI knb-lter-ntl.29 rev 38). Lakes AL, BM, CR, SP and TR, as before.
Variables (the three "groups"): water temperature (wtemp), dissolved oxygen (o2, mg/L) and oxygen saturation (o2sat, %),
at 1 m depth. If 1 m is missing on a date, use the shallowest depth ≤ 1 m; otherwise skip the date. A date needs all three.

## Pipeline: identical to LAKE_HARNESS steps 3–8
Per-lake median binarisation; d_ij; split designs (60), with ε*_split = V/3; the same-lake control; δ_full truth (LP);
the year-mod-3 pseudo-lake null (30); the same outcome rules (INFORMATIVE / LOOSE / TOOTHLESS). Plus, descriptive: the
minimum slack over designs.

## Prediction (in advance)
d(T, O2) high (≈ 0.8–0.9, anti-tied); d(O2, sat) low; d(sat, T) intermediate. So triangles sit near the boundary, and
some designs may give ε*_split > 0. The physics is shared across lakes, though, so nonzero values should be comparable
to the pseudo-lake null. Expected verdict: TOOTHLESS or LOOSE. A rule-defined INFORMATIVE would mean the lakes' coupling
genuinely differs (e.g. productivity driving o2sat away from equilibrium in some lakes).

## Result (2026-11-05): pre-registered verdict TOOTHLESS (prediction held), with one descriptive signal
Script `verification/lake_physics_harness.py` (748–770 dates per lake). The same-lake V was ≤ 3e-17 (float).
- d(T, O2) = 0.78–0.90, d(O2, sat) = 0.53–0.58, d(sat, T) = 0.23–0.34. As predicted, the triangles sit near the boundary.
- Real designs: ε*_split > 0 in 47% of designs; median 0, max 0.049. Pseudo-lake null: median 0, 95th percentile 0.0275,
  max 0.0306, > 0 in 40%. Rule: median 0 ≤ 0.0275, so **TOOTHLESS**. Spearman(ε*_split, δ_full) = 0.14.
  δ_full: real median 0.052; null median 0.045 (95th percentile 0.060).
- **Descriptive (not gated):** 5 of 60 designs exceed the null maximum (0.031). **All 5 take the sat–T pair from
  Allequash (AL)**, whose saturation tracks temperature more closely than in the others (d = 0.226 against 0.28–0.34),
  and whose T–O2 anti-tie is the weakest (0.78). The loop singles out one lake as differing in coupling, without
  comparing the same pair across lakes. Here the full data confirms it directly, since every lake measures every pair.
  A plausible mechanism (lens, unverified): more photosynthetic supersaturation in a more productive lake.
- Reading: strong ties bring the loop to the boundary, where it begins to see between-lake *coupling* differences, but
  only at the edge of the noise (1/12 of designs). Shared physics keeps the median at 0. The harness shows the instrument
  works in the right regime, with the right failure mode, and is weak at n ≈ 750 per lake.
