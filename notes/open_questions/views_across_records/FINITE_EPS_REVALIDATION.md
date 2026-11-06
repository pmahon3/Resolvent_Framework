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

## Result (2026-11-06): finite ε still FAILS. ε = ∞ kept
| world | √(ln n/n) | n^{−1/6} | ∞ |
|---|---|---|---|
| W1 (3 sites, no kinks) | 0.08–0.12 | 0.08–0.11 | 0.02–0.05 |
| W2 | 0.05–0.09 | 0.01–0.04 | 0.00 |
| W3 ring | 0.32–0.44 | 0.11–0.18 | 0.01 |
| WD | 0.32–0.42 | 0.12–0.21 | 0.00–0.01 |
| P1 / P2 power | 0.18–0.20 / 0.43–0.49 | 0.07–0.09 / 0.31–0.32 | 0.01 / 0.05–0.08 |
- No finite ε passes (W1 fails even at n^{−1/6}, and it has no kinks). Automatic blocks did not cure the small-sample variance underestimation for
  correlations at n = 30–53. Prediction "n^{−1/6} may pass" was wrong. **The rule keeps ε = ∞.** Its low power stands.
- Power for weak common causes must come from more data (longer series, more sites) or from a model, not from a less conservative bootstrap.
