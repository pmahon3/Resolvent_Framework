# Delay-aligned gate on real seizure data (CHB-MIT chb01) — pre-registered 2026-11-04, before download

reviewed: false. Motivation: conduction delays make delay-aligned pairwise views come from different times;
round a loop the delays do not cancel (user, 2026-11-04). Synthetic arbitrary-stagger gate was REDUNDANT.

## Data
PhysioNet CHB-MIT Scalp EEG, case chb01, all recordings that contain a seizure (per `chb01-summary.txt`),
256 Hz, bipolar 10–20 montage. Seizure times from the official summary only.

## Pipeline (fixed now; no changes after seeing results)
1. Channels: the first 8 bipolar channels in the file's order. Loops: all 56 triangles among them.
2. Preprocess: subtract a 1 s moving mean (high-pass); binarise by sign.
3. Delays: for each channel pair, τ_ij = lag in [−200, +200] ms maximising |cross-correlation| on the
   first 10 minutes of the recording (interictal baseline), then frozen for the whole recording.
4. Windows: 10 s, step 5 s. In each window, for a triangle (i,j,k): disagreement d_ij from pairs
   (x_i(t), x_j(t − τ_ij)), and similarly d_jk, d_ki; ε*_delay = V/3 (binary triangle theorem).
   Control: ε*_sim from zero-lag pairs (must be 0: a joint exists within a window).
   Indicator per window = mean ε*_delay over the 56 triangles.
5. Baselines per window, mean over the 8 channels: variance, lag-1 autocorrelation (AC1), mean |zero-lag
   cross-correlation|.
6. Periods: interictal = minutes 0–10 after start (also the delay-estimation period) → excluded from tests
   except as baseline; pre-ictal = the 5 minutes before onset; ictal = onset to end.
   Recordings whose onset is < 16 minutes from the start are used for ictal only.

## Outcomes
- Per seizure: pre-ictal vs interictal Mann–Whitney (one-sided, greater) for each indicator, α = 0.01.
- **INFORMATIVE:** ε*_delay pre-ictal > interictal in a majority of usable seizures AND in more seizures than
  every baseline indicator (i.e. catches seizures the baselines miss).
- **ICTAL-ONLY:** ε*_delay elevated during seizures (ictal vs interictal, majority) but not pre-ictally.
- **REDUNDANT / NULL:** otherwise.
- Sanity: ε*_sim = 0 in every window.
n is small (≈7 seizures, one patient): any outcome is anecdotal, not a result.

## Implementation choices (fixed 2026-11-04 after download, BEFORE any indicator was computed)
The spec left these open; settled here before running:
- τ_ij is estimated on the high-passed *continuous* signal (not the sign), at 1-sample resolution. τ_ji = −τ_ij.
- A window is assigned to a period only if it lies entirely inside it. Pre-ictal = [onset−300 s, onset).
- Variance and AC1 are computed on the high-passed continuous signal. AC1 is at a lag of one sample (1/256 s), as written.
- chb01_21 (onset 327 s): its minutes 0–10 contain the seizure. For its ictal test, interictal = windows in
  0–600 s that do not overlap [onset−60, end+60]. The delays are still taken from minutes 0–10, as written.
- Descriptive only (not a gated outcome): the delay holonomy h = τ_ij + τ_jk + τ_ki per triangle. If h = 0, the
  three shifted pairs come from one shifted triple, so ε*_delay ≈ 0 up to window-edge effects. Only h ≠ 0 can twist.
- The windows overlap (step 5 s < length 10 s), so Mann–Whitney p-values are anticonservative.

## Result (2026-11-04): pre-registered verdict REDUNDANT / NULL
Script `notes/open_questions/verification/neuro_eps_delay_chbmit.py` (9 s, 0.5 GB). Sanity: ε*_sim = 0 exactly in every window of every recording.

Tally of seizures with p < 0.01 (6 usable pre-ictal, 7 ictal):

| indicator | pre-ictal | ictal |
|---|---|---|
| ε*_delay | **0/6** | 3/7 |
| variance | 3/6 | 7/7 |
| AC1 | 5/6 | 2/7 |
| mean \|zero-lag xcorr\| | 3/6 | 2/7 |

- The median ε*_delay is **0 in every period of every recording**. Nonzero windows have magnitude ≤ 3×10⁻³.
  The fraction of nonzero windows rises during seizures (0.17–0.69, against 0.03–0.29 interictal), but at
  these magnitudes this is far below the finite-sample noise floor. With AC1 ≈ 0.98 at 256 Hz, a 10 s window
  holds only ~30 effective samples.
- The holonomy is nonzero in 91–98% of triangles (median |h| = 7–22 samples = 27–86 ms), so the delays
  do *not* cancel round loops. **Nonzero holonomy is present, yet the views still glue.** Holonomy is necessary for a twist, not sufficient.
- The prediction implicit in the design (a twist appears pre-ictally) failed. AC1 is the best pre-ictal indicator here (5/6),
  which does not match Wilkat 2019's population null: n = 1 patient, overlapping windows, anticonservative p.

## Reading
- Why ε* stays at zero: sign-binarised scalp EEG pairs have |ρ| ≈ 0.3, so the disagreement rates are d ≈ 0.4. A
  triangle-inequality violation needs some pair near agreement (d → 0) or near anti-agreement (d → 1).
  Moderate correlations keep d deep in the slack interior.
- ⟦HAND⟧ Gaussian picture (scope: jointly Gaussian pairs, sign binarisation). Sheppard gives d = θ/π with
  θ = arccos ρ. Three unit vectors with pairwise angles θ exist iff the 3×3 matrix [cos θ] is PSD, iff the
  spherical triangle inequalities hold. Those are exactly the metric inequalities on d. So **ε*_delay > 0
  iff the delay-aligned correlation matrix (entries ρ_ij(τ_ij)) is not positive semidefinite.** The question
  "do the delay-aligned views glue?" is then the Higham nearest-correlation-matrix question. Its
  noise-robust form is the minimum eigenvalue of the delay-aligned correlation matrix (≥ 0 ⟺ glue).
- Bearing on WHY.md: here local views with real loop holonomy do add up to one world, to within noise.
  Delay holonomy alone does not make a twist. A twist also needs correlations strong enough to reach the boundary.
- Next probe, if any, is a separate pre-registration. Candidates: the min-eigenvalue indicator on the same files;
  intracranial data (stronger correlations); a surrogate floor (Wilkat protocol). It is not run here.
