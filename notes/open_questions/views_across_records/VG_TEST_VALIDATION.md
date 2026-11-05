# Size and power of the V_G bootstrap test (specified 2026-11-05, before running)

reviewed: false. Gap 1 from the "is the model-free method nailed down" review.

## Test
V_G (`gaussian_poland.py` FastVG) on the sample Pearson correlation matrix after linear detrending. Reject when the 5% point of a
moving-block bootstrap (b = 3, no wrap) is > 0.

## Worlds (all pair-sources AR(1) with coefficient φ, independent across pairs)
- **W1 (boundary, 3 sites, linear):** yᵢ = (Sᵢⱼ + Sᵢₖ)/√2, so r = ½ and V_G = 0.
- **W2 (boundary, 10 sites, all pairs):** yᵢ = Σⱼ Sᵢⱼ/3, so r = 1/9 and every load = 1.
- **W3 (boundary, 10 sites, ring):** sources only between ring neighbours; yᵢ = (S_{i−1,i} + S_{i,i+1})/√2, so neighbour r = ½ and loads = 1.
- **W4 (nonlinear boundary, 3 sites):** rare spikes, yᵢ = 10·[Sᵢⱼ > 2.5] + 10·[Sᵢₖ > 2.5]; population V_G ≈ 0. Pearson, and normal scores (W4ns).
- **P1, P2 (power, 10 sites):** W2 rescaled by √(1−λ²) plus λ·F with a common AR(1) factor F. λ² = 0.05 gives V_G = 0.4; λ² = 0.1 gives V_G = 0.8.
- Grid: φ ∈ {−0.5, +0.5}; n ∈ {30, 53}. Three-site cells: 300 simulations × 1000 resamples. Ten-site cells: 100 × 300.

## Pass rule (fixed now)
Size ≤ 0.07 in every boundary cell (with 100 simulations a true 0.05 can read up to ~0.09; 0.07 is the working bar). Otherwise
report which world fails and do not use the test unmodified for such data.

## Run 1 stopped (2026-11-05) after one cell; amendment before run 2
- Run 1 (optimiser V_G): W1, n = 30, φ = −0.5 gave **size 0.12** (fails the 0.07 bar). This is consistent with the upward small-sample bias
  found by the independent check. Stopped to switch to the exact closed form.
- **Run 2:** V_G = ρ(|R − I|) − 1 (Perron root), the same statistic to within 1.5×10⁻³ and much faster. Full counts in every cell: 300 simulations, 1000
  resamples. Two variants, declared before run 2:
  - **(P) percentile:** reject if the 5% point of V_G* is > 0 (as specified);
  - **(B) basic / bias-corrected:** reject if 2·V̂_G − (95% point of V_G*) is > 0.
- Same worlds, grid and pass rule (size ≤ 0.07 in every boundary cell).

## Run 2 result (2026-11-05): BOTH bootstrap variants FAIL. Do not use them.
| world | P (percentile) | B (basic) |
|---|---|---|
| W1 (3 sites) | 0.07–0.11 | 0.10–0.15 |
| W4 rare spikes, raw | 0.32–0.40 | 0.01–0.04 |
| W4 normal scores | 0.00 | 0.00 |
| **W2 (10 sites, all pairs)** | **1.00** | 0.18–0.42 |
| **W3 (10-site ring)** | **1.00** | 0.87–0.89 |

Cause: V̂_G sums |r̂| through the Perron root. Every true-zero or small correlation contributes |noise| ≈ n^{-1/2}, so V̂_G is biased far above 0
when k is large and many r are small. The bootstrap resamples the inflated estimate and cannot correct it.
**Consequence: the Poland V_G results (`GAUSSIAN_PAIRWISE_MODEL.md` step 3) are UNVALIDATED.** The magnitude (+4.95 against a bias of
order +1) makes the conclusion plausible, but not shown.

## Run 3 (declared before running): calibrated boundary test (C)
1. Per site: normal scores (rank → Φ⁻¹), then linear detrend. Valid: the ceiling holds under per-site transforms.
2. R̂ = sample correlation. If ρ(|R̂ − I|) ≤ 1, do not reject. Otherwise R₀ = I + (R̂ − I)/ρ(|R̂ − I|). That is on the boundary
   (V_G = 0) and PSD, as a convex combination of R̂ and I.
3. Simulate 1000 datasets of the same n from a stationary Gaussian VAR with correlation R₀ and common lag-1 coefficient φ̄ (the mean
   of the sites' lag-1 autocorrelations). Apply step 1 to each and compute V̂_G.
4. Reject if V̂_G(data) > the 95th percentile of the simulated values.
- Validate on W1–W4, P1, P2 (n = 30/53, φ = ±0.5; 300 simulations). Pass rule as before (size ≤ 0.07 in boundary cells). Caveat:
  Gaussian boundary worlds are not proven least favourable, so the non-Gaussian W4 is the check.

## Run 3 result (2026-11-05): calibrated boundary test (C) FAILS for 10 sites
W1 (3 sites) 0.04–0.05 ✓; W4 0.00 ✓; W2 0.05–0.13 ✗ (borderline); **W3 ring 0.30–0.67 ✗**; power P1 0.12–0.30, P2 0.30–0.44 (partial).
Cause: proportional shrinkage to the boundary is not least favourable. True-zero correlations inflate most under noise, and shrinkage
leaves small nonzero values instead. The 3-site calibrated test is valid on this grid. **Next (per the new workflow rule): no further
ad-hoc fixes. Read and implement the established method for non-differentiable functionals / moment inequalities (Fang–Santos 2019;
Andrews–Soares 2010; Chernozhukov–Chetverikov–Kato 2019), then validate on the same grid.**

## Run 4 (declared before running): Hong–Li numerical delta method (recipe in `VG_INFERENCE_METHODS.md`)
- Per dataset: prep = per-site normal scores, then linear detrend on year. R̂ from prep; T = √n (ρ(|R̂ − I|) − 1).
- Moving-block bootstrap of years (no wrap; block b = round(n^{1/3}); 1000 resamples), re-running the full prep inside each resample (years
  carried with rows). Z* = √n (R̂* − R̂).
- For each step ε ∈ {1/√n, √(ln n / n), n^{−1/6}, ∞}: D*(ε) = [ρ(|R̂ + εZ* − I|) − ρ(|R̂ − I|)]/ε, with D*(∞) = ρ(|Z*|) (Z* has zero
  diagonal). Reject if T > the 95% quantile of D*(ε).
- Worlds: W1, W2, W3, W4 (boundary); W0 = independent sites (R = I, interior); WD = degenerate Perron root (two disjoint 5-site rings);
  P1, P2 (power). n ∈ {30, 53}, φ ∈ {−0.5, +0.5}; 300 simulations per cell.
- **Selection rule (from the methods note, fixed now):** the smallest ε whose size is ≤ 0.07 in every boundary cell (W1–W4, WD). If none
  passes, ε = ∞ is the conservative fallback, and if even ∞ fails, the 10-site test is not usable.
- Expected (methods note): 1/√n reproduces run B's failure.
