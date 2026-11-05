# Synthetic gate: does ε*(t) say anything near a critical transition that standard early-warning signals don't?

reviewed: false. Pre-registered 2026-11-04 BEFORE running `notes/open_questions/verification/neuro_eps_synthetic.py`.

## Model
Three coupled regions x₁,x₂,x₃: dx = (−λ(t) x + K x) dt + σ dW, λ decreasing linearly to near 0
(approach to a critical point: critical slowing down). Binarise each region by sign. Contexts = staggered
windows: pair (1,2) from window w, pair (2,3) from window w+Δ, pair (3,1) from window w+2Δ.
ε*(t) = V/3 (binary triangle theorem, exact). Two coupling regimes:
(a) all excitatory (synchrony-like, the seizure picture);
(b) frustrated (one inhibitory link round the loop).

## Comparators
Standard early-warning signals in the same windows: variance, lag-1 autocorrelation (AC1). Plus a plain
non-stationarity control: TV change of one pair's table between window w and w+Δ (pair drift).

## Outcomes (pre-registered)
- **INFORMATIVE:** in some regime, ε*(t) rises before the transition with lead time ≥ AC1/variance and is not
  explained by pair drift (correlation with drift < 0.8).
- **REDUNDANT:** ε*(t) ≈ 0 throughout, or tracks pair drift (corr ≥ 0.8), or rises later than AC1/variance.
- Prediction written in advance: regime (a) gives ε* ≈ 0 (positive correlations round a loop never violate
  a triangle inequality: no frustration); regime (b) may give ε* > 0, but driven by drift.
