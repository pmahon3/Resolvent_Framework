# Finite-ε Hong–Li re-validated with automatic blocks (pre-registered 2026-11-06, before running)

reviewed: false. Run 4 (`VG_TEST_VALIDATION.md`) rejected finite ε because the size failed even without kinks (W1: 0.11–0.17), which was traced to
fixed n^{1/3} blocks underestimating variance. Politis–White blocks fixed a similar failure in `SPACE_TIME_DYNAMICS.md`. This re-tests finite ε.

## Test
Spearman (continuous worlds, no jitter needed), no detrend, Politis–White automatic blocks (`arch`, circular column, max over sites, clipped
[2, n/3]), 1000 resamples. Hong–Li: D*(ε) = [V(R̂ + εZ*) − V(R̂)]/ε with V = ρ(|R − I|) − 1 (m = 2), ε ∈ {√(ln n/n), n^{−1/6}, ∞}.
Reject if √n·V(R̂) > the 95% quantile of D*(ε).

## Worlds and rule
- Boundary worlds (as run 4): W1, W2, W3, WD, at n ∈ {30, 53}, φ ∈ {−0.5, +0.5}.
- Power: P1, P2 (n = 53, φ ±0.5).
- 300 simulations.
- **Rule (fixed now):** adopt the smallest finite ε whose size is ≤ 0.07 in every boundary cell. Otherwise keep ε = ∞.
- Prediction: √(ln n/n) still fails on W3/WD (kinks at many zeros); n^{−1/6} may pass with automatic blocks.
