# Min-eigenvalue gate (noise-robust form of the delay gate), CHB-MIT chb01: pre-registered 2026-11-04, before running

reviewed: false. Follows `DELAY_GATE.md`, whose result was REDUNDANT/NULL. Its ⟦HAND⟧ Gaussian reading: delay-aligned
views glue iff the delay-aligned correlation matrix is PSD.

## Indicator
- Same files, preprocessing (1 s moving mean removed), frozen delays τ_ij (from minutes 0–10), and 10 s / 5 s windows.
- Per window: R_ij = corr(Y_i(t), Y_j(t − τ_ij)) on the continuous high-passed signal, with R_ii = 1, symmetrised as
  (R + Rᵀ)/2. Indicator g = −λ_min(R). g > 0 means "does not glue".
- Channels 1–7, not 1–8. The bipolar chains satisfy (ch1+ch2+ch3+ch4) − (ch5+ch6+ch7+ch8) = FP1−O1 − (FP1−O1) = 0
  exactly. That makes the zero-lag matrix singular, and delays would turn it negative mechanically, as a montage
  artefact. Dropping ch8 removes this one exact relation.
- Control: g_sim from the zero-lag matrix, which must be ≤ 0 (a sample correlation matrix is PSD).
- Same baselines, periods, tests (one-sided Mann–Whitney, α = 0.01) and verdict rule as DELAY_GATE.

## Prediction (written in advance)
g < 0 in most windows: weak correlations make R diagonally dominant. If g rises before onset, it will most likely
track the zero-lag |xcorr| baseline (both grow with synchrony), so the expected verdict is REDUNDANT.
