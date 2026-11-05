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
