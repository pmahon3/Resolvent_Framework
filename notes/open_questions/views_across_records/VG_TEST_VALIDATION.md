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
