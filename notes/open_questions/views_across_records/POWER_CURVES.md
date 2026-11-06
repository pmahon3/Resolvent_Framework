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
