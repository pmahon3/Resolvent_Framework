# Power curves for the pairwise-ceiling (m = 2) test (specified 2026-11-06, before running)

reviewed: false. What a null result can and cannot rule out.

## Test
Levels test as adopted: Spearman + jitter, ε = ∞, Politis–White automatic blocks, no detrend; 500 resamples; α = 0.05.

## Worlds (10 sites; stationary AR(1) components, φ = 0)
x_i = √(1 − λ²)·B_i + λ·F_i, where F is a common factor of **reach r** (shared by r consecutive sites on the ring, independent elsewhere:
F_i = f for sites 0..r−1, else an independent unit noise), and B is a base:
- **Base "boundary":** the pairwise ring at the ceiling (neighbour r = ½, V_G = 0). Any common factor pushes it over.
- **Base "independent":** independent sites. Population V_G = (r − 1)λ² − 1 within the reach, so detection needs λ² > 1/(r − 1).

Grid: reach r ∈ {3, 5, 10}; factor share λ² ∈ {0.05, 0.1, 0.2, 0.3, 0.5}; n ∈ {30, 53, 100}. 100 simulations per cell. Population V_G is reported per cell.

## Output
Power tables per base. Not a hypothesis test; it defines what a null result means. (m ≥ 3 power is not computed here, since the SDP cost is high;
the m = 3 critical value equals that of −λ_min(Z*), so its power is expected to be lower, per the independent check.)

## Result (2026-11-06). Script `verification/power_curves.py`. Power (100 simulations per cell) at n = 30 / 53 / 100
**Base "boundary"** (pairwise ring at the ceiling plus a factor):
| reach | λ² = 0.05 | 0.1 | 0.2 | 0.3 | 0.5 |
|---|---|---|---|---|---|
| 3 | 0 | 0 | 0 | 0 | 0 |
| 5 | 0 | 0 / 0 / .01 | .03 / 0 / .06 | .01 / .08 / .42 | .15 / .74 / 1.00 |
| 10 | .02 / .01 / .07 | .08 / .11 / .39 | .29 / .63 / .96 | .74 / .97 / 1.00 | 1.00 |

**Base "independent"** (the factor alone must clear the ceiling):
| reach | λ² = 0.05–0.2 | 0.3 | 0.5 |
|---|---|---|---|
| 3 | 0 | 0 | 0 |
| 5 | 0 | 0 | .02 / .18 / .56 |
| 10 | 0–.23 | .29 / .75 / .97 | .98 / 1.00 / 1.00 |

- **The test sees only wide-reaching, fairly strong common causes.** At n = 53 it needs reach ≈ 10 with λ² ≳ 0.2–0.3 (≈ 0.6–0.75 power), or
  reach 5 with λ² ≈ 0.5 on a favourable base. **A common cause of reach 3 is invisible** at every strength and n tested (its population V_G is
  near or below 0 unless the base is already at the ceiling).
- **What a null means:** at n ≈ 50, no violation does NOT exclude common causes reaching ≤ 5 sites, nor wide ones explaining ≤ ~20% of variance.
- **Poland in context:** V̂_G ≈ 4.8 sits in the "reach 10, λ² ≈ 0.5" region, far inside the high-power zone. The m̂* = 4 lower bound on reach
  is consistent with the low power for small reach.
