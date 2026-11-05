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

## Result (2026-11-04): pre-registered verdict ICTAL-ONLY (by the letter); in substance not beyond baselines
Sanity: g_sim < 0 in every window (zero-lag matrices PSD). Prediction "g < 0 in most windows" held (fraction g > 0
was 0.06–0.36, with chb01_21 at 0.64 because its baseline contains the seizure).

| indicator | pre-ictal (of 6) | ictal (of 7) |
|---|---|---|
| g_delay | 1/6 | 4/7 |
| variance | 3/6 | 7/7 |
| AC1 | 5/6 | 2/7 |
| \|xcorr0\| | 3/6 | 4/7 |

The ICTAL-ONLY rule did not require beating baselines. g ties |xcorr0| ictally and loses to variance (7/7), and
corr(g, |xcorr0|) = 0.34–0.64. As a seizure detector it is redundant.

## Descriptive (not gated): where the non-gluing lives
- Windowed (10 s): when the 7×7 matrix is non-PSD, usually **no 3×3 principal submatrix is**. "Full non-PSD, every
  triangle PSD" holds in 5–46% of windows, against 1–19% for any triangle failing. This explains DELAY_GATE's
  null: the triangle test looked in the wrong place.
- Long windows, over the whole period: every 3×3 submatrix is PSD in every period of every recording, with min
  λ_min(3×3) ≥ +0.012. The full 7×7 λ_min:

  | | 03 | 04 | 15 | 16 | 18 | 21* | 26 |
  |---|---|---|---|---|---|---|---|
  | minutes 0–10 | −0.034 | +0.187 | +0.212 | +0.109 | +0.110 | −0.140* | +0.137 |
  | ictal | −0.131 | −0.046 | +0.165 | +0.090 | −0.036 | −0.250 | −0.037 |

  (*21's minutes 0–10 contain its seizure.) Ictal λ_min < 0 in 5/7 seizures, and drops below the baseline in 7/7.
- Reading (lens, ⟦HAND⟧ Gaussian scope): during seizures the delay-aligned pairwise views **fail to fit one Gaussian world as a
  whole, while every three of them fit**. The obstruction is global rather than local, like a long cycle rather than a
  triangle. Delays round loops (holonomy) make it possible, and ictal synchrony pushes the lagged correlations far enough.
- **Not established:** a noise floor. The ictal periods are 27–101 s with high autocorrelation, so the eigenvalue
  fluctuation may be comparable to the effect. Needed: a surrogate that keeps each channel's spectrum and the lagged
  cross-covariance (multivariate phase randomisation). It answers "beyond linear-stationary?", not "beyond noise?",
  because a stationary linear process with these lags can be non-PSD in population too. A separate bootstrap is
  needed for noise. Also needed: more patients, and a check that frozen interictal delays are not the whole story
  (re-estimate the delays ictally).

## Noise floor, part 1 (descriptive, 2026-11-04): same-length baseline windows
For each seizure: λ_min of the whole ictal period, against λ_min over windows of the same length slid (step 5 s) through
minutes 0–10 (for 21, only windows ending ≥ 60 s before onset).

| | 03 | 04 | 15 | 16 | 18 | 21 | 26 |
|---|---|---|---|---|---|---|---|
| ictal λ_min | −0.131 | −0.046 | +0.165 | +0.090 | −0.036 | −0.250 | −0.037 |
| baseline median | −0.071 | +0.137 | +0.192 | +0.069 | +0.082 | −0.187 | +0.119 |
| frac baseline ≤ ictal | 0.12 | 0.01 | 0.06 | 0.60 | 0.00 | 0.00 | 0.00 |

- In 4/7 seizures (04, 18, 21, 26) the ictal λ_min lies below ≥ 99% of same-length baseline windows.
- The non-gluing is **not seizure-specific**: in chb01_03 and chb01_21 the baseline windows are already non-PSD at
  the median. Delay-aligned views fail to fit one Gaussian world in ordinary background EEG too, depending on the recording.
- Honest status: an anecdote from one patient. It is not shown to beat |xcorr0| or variance, and this "null" is a
  baseline distribution, not a surrogate. Descriptive scripts: `verification/neuro_eig_desc_{where,longwin,samelen_null}.py` (args: path to `neuro_eig_delay_chbmit.py`, data dir); they use
  `neuro_eig_delay_chbmit.py`'s `wcorr`/`shift` and `dg.shifted` helpers.
