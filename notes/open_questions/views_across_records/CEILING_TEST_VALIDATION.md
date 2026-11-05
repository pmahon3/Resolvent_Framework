# Validating the ceiling test: size and power by simulation (specified 2026-11-05, before running)

reviewed: false. Responds to audit defect V3 (`SYNCHRONY_CAUSALITY_METHOD_AUDIT.md`): it is unknown whether the bootstrap
lower-bound test has honest error rates near the boundary, at small n, with autocorrelation.

## Test under study
V = eq.-16 excess (as in `mast_ceiling_gate.py`) on median-split series. Reject "no common cause of all three" when the one-sided
95% bootstrap lower bound of V is > 0. Moving-block bootstrap **without wrap-around**, block length b ∈ {1, 3, 5}; 1000 resamples.

## Worlds
Each year, three pair-sources S_AB, S_BC, S_CA are AR(1) Gaussian (coefficient φ), independent across pairs. Site A = 1 iff
S_AB > τ_AB and S_CA > τ_CA (the AND rule), and similarly for B and C.
- **Boundary (size), symmetric:** all thresholds at P(S > τ) = 1/√2. This is the AND point, where V_pop = 0.
- **Boundary-near (size), asymmetric:** source probabilities (0.62, 0.71, 0.80). Pairwise-only, so V_pop ≤ 0.
- **Power:** each year, with probability ρ, all three sites copy one common coin (a common cause); otherwise the symmetric AND
  world. ρ ∈ {0.1, 0.2, 0.3, 0.5}.
- Grid: φ ∈ {−0.5, 0, 0.5}; n ∈ {45, 72}; 400 simulated datasets per cell.

## Outputs
- Rejection rates: size should be ≤ 0.05; power, by cell.
- A block-length rule: the smallest b that holds size at φ = −0.5 and φ = +0.5.
- Not a hypothesis test, so no verdict rule. It decides whether and how the instrument can be used.
