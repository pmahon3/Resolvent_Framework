# Step 3: testing hypergraph hypotheses (method + validation), pre-registered 2026-11-06, before running

reviewed: false. Conditioned on step 2 (`HYPERGRAPH_CENTRES_PRIOR_ART.md`): there is no established test (Q4), so we use the repo's V_H with
the validated bootstrap. Minimal sufficient hypergraphs are not unique (Q2), so the output is a *set*. Frustrated short cycles carry the
signal (the odd-cycle excess is sec(π/L) − 1). Correlation-level limits are as stated (Evans).

## Test for one hypothesis H
T_H = √n·V_H(R̂), with R̂ = jittered Spearman, no detrend. Critical value: the 95% quantile of V_H(Z*) over moving-block resamples (Politis–White
automatic blocks; re-ranking in each resample). Reject ⇒ H does not suffice: a centre outside H is needed. Validity: identical proof to the reach
test (V_H is the support function of the closed convex cone FW_H ⊇ PSD diagonals). Pointwise asymptotic.

## Hypothesis family: local centres of radius d
H(d) = pairs ∪ {all sets of sites whose pairwise distances are all ≤ d}. This is nested in d. **d̂ = the smallest d with H(d) not rejected**: a
lower-bound-style estimate of the spatial reach of the centre (power falls as d grows, as for m̂*). Reported with the set of non-rejected d.
Synthetic geometry: 10 sites on a ring, adjacent-site distance 1, so H(1) = pairs and H(2) = pairs + consecutive triples, and so on.

## Validation (synthetic, 10-site ring)
- **Size at the H(2) boundary:** sources on consecutive triples (the ring-of-triples world), rescaled so that V_{H(2)} = 0 (bisection on V_{H(2)}).
  Test H(2); expected rejection ≤ 0.10.
- **Discrimination:**
  - world **Poly:** the same triple sources at moderate strength (inside H(2));
  - world **Mono:** a single factor on all 10 sites plus independent noise, matched so V₂ is the same as Poly's (within 10%).
  Test H(2) in both. Expected: Poly rejection ≤ 0.10, Mono rejection clearly higher.
- n = 53, φ = 0; 50 simulations × 200 resamples per cell (SDP cost).

## Step 4 (conditional on step 3 passing)
Poland, 10 sites, H(d) with d over the observed inter-site distances (km), giving d̂ km. Prediction to be written after step 3.
