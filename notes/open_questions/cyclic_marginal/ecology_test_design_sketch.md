# Design sketch: can ordinary ecological data show a twist that no single community explains?

reviewed: false. 2026-11-04. A sketch, not a plan; no claims. Theory: `heterogeneity_threshold.md`.
Prior art: `ecology_contextuality_prior_art.md`, `ecology_contextuality_prior_art_DEEP.md`.

## The question
Several surveys each see only part of a community. Do their pairwise pictures add up to one community,
*allowing* for the community to differ between surveys by at most what biology permits? If not, the
residue is either genuine non-classical structure or a disturbance channel the design missed.

## Why aim for short loops and visible twists
- On a loop of L pair-views, heterogeneity can hide a twist only up to ε* = V/L (≤ 1/L), so short loops are
  the most sensitive: a triangle tolerates up to 1/3, longer loops less.
- Hidden twists (exact-zero patterns, e.g. the 3×4×4 committees) dissolve at ε ≈ 1/27. Field data will not
  resolve them; look for visible, sign-type twists (agreement / disagreement round a loop).

## Data shape (one natural instance)
Three yes/no variables (e.g. presence of species A, B, C at a site), each pair observed jointly by a
different method, so that no method sees all three:
- method 1 detects A and B (e.g. camera traps), method 2 detects B and C (e.g. eDNA),
  method 3 detects C and A (e.g. visual transects).
- Many sites per method; per method, a 2×2 table of joint presence.
Then d_k = P(the pair disagrees) per method, and V is the largest violation of the triangle inequalities
(d_AC ≤ d_AB + d_BC and permutations; d_AB + d_BC + d_CA ≤ 2). **ε*(data) = V/3** (proved for triangles):
computable by hand from three disagreement rates.

## Calibrating ε (independently, before looking at V)
- **Method shift:** co-located comparisons where two methods detect the same species at the same sites
  (e.g. both detect B): the disagreement of their single-species tables bounds method-induced change.
- **Temporal turnover:** if surveys are not simultaneous, published colonisation/extinction rates or repeat
  surveys bound the community change between dates.
- **Site heterogeneity:** if methods sample different sites, beta-diversity between site sets bounds it.
- ε_cal = upper confidence bound of the sum of applicable shifts. Pre-register it.

## Test
1. Check margin consistency per species across methods (Contextuality-by-Default direct-influence check).
   Inconsistency is itself the heterogeneity signal; it must be within ε_cal, else stop.
2. Compute ε*(data) (= V/3 for the binary triangle; the LP in `verification/eps_star_triangle.py` otherwise),
   with a finite-sample test (Berrett–Samworth 2022 `MCARtest`, adapted to the ε-margin).
3. Outcome: ε* ≤ ε_cal ⇒ a classical community within biological limits explains the data (the expected
   result). ε* > ε_cal ⇒ no such community; then hunt for a missed disturbance channel (method changes
   detection of the *other* species?) before reading anything non-classical into it.

## Honest distance
- No dataset chosen; whether methods with exactly this pairwise detection pattern exist at scale is unknown.
- Detection error (false absences) is itself heterogeneity between methods and will inflate d_k; it must
  enter ε_cal, which may make the test toothless.
- The most likely first result is "inside the ε-ball". That is still a finding: a measured bound on how much
  the surveyed world could be failing to add up.
- Prior art: no ecological contextuality test found (two passes); the machinery (CbD, Berrett–Samworth,
  instrumental inequalities) is owned.
