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
