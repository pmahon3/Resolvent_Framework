# Model-based route: the linear-Gaussian pairwise ceiling for many sites (specified 2026-11-05, before running)

reviewed: false. Follows `MAST_S2_GATE.md`. Plan agreed with the user: the model-free test establishes *that* a common cause
exists, and a model asks *which*.

## Model and ceiling ⟦HAND⟧
Standardised site values yᵢ = Σⱼ bᵢⱼ Sᵢⱼ + eᵢ, with independent pair-drivers Sᵢⱼ (unit variance) and independent local noise eᵢ.
Then rᵢⱼ = bᵢⱼ bⱼᵢ and Σⱼ bᵢⱼ² ≤ 1. With tᵢⱼ = bᵢⱼ², **R is pairwise-feasible ⟺ ∃ tᵢⱼ > 0 with tᵢⱼ tⱼᵢ = rᵢⱼ² and Σⱼ tᵢⱼ ≤ 1 ∀i.**
Parametrise tᵢⱼ = |rᵢⱼ| e^{w_p}, tⱼᵢ = |rᵢⱼ| e^{−w_p} per pair p; then V_G(R) = min_w max_i Σⱼ tᵢⱼ − 1 (convex in w).
Three equal correlations: feasible iff r ≤ ½. V_G > 0 ⇒ under this model, a common cause of ≥ 3 sites is required.
Prior-art status: not checked (likely related to edge-factor / bi-factor covariance structures). Not claimed.

## Steps
1. **Check of V_G:** confirm the equal-triangle threshold numerically. Compare V_G with direct fits of the linear model.
2. **Robustness to nonlinearity (decides usability):** simulate *pairwise-only* worlds with nonlinear responses (min/AND, max, product,
   heavy-tailed sources, threshold-plus-noise) for 3 and 10 sites. Record how often the sample V_G exceeds 0, and the population
   V_G (n = 10⁶). **If any pairwise-only nonlinear world has population V_G > 0, the Gaussian test is NOT a valid common-cause test**
   for such data, and is reported as model-conditional only.
3. **Poland** (only if step 2 passes, or as explicitly model-conditional): 10 sites, years common to all (≥ 50; same rule as the pooled gate),
   log(x+1), linear detrend; residualise on each site's own ΔT inside the model (y = a + b·ΔT + residual); Jeffreys inverse-Wishart
   posterior for the residual covariance; 20 000 posterior draws. Report P(V_G > 0 | data). **Placebo:** the same pipeline with ΔT
   permuted (one permutation across sites; 200 placebos), giving the distribution of P(V_G > 0). Sensitivity: AR(1) prewhitening per site.

## Prediction (in advance)
Step 1 passes. Step 2: product and threshold worlds may push V_G above 0 (correlations of nonlinear pairwise worlds are not capped by
the linear bound). Step 3: P(V_G > 0) high both with and without ΔT; the placebo will show whether ΔT is special.

## Steps 1–2 results (2026-11-05)
- **Step 1 passes.** Equal triangle: V_G = −0.20 / 0.00 / +0.20 at r = 0.4 / 0.5 / 0.6. Over 200 random linear pairwise models (6 sites),
  max V_G = −0.17. `verification/gaussian_pairwise.py`.
- **Step 2 passes. Prediction WRONG** (I predicted nonlinear worlds might exceed). Population V_G (n = 10⁶) ≤ +0.001 for every pairwise-only
  world: additive, min/AND, max, product, AND indicator, heavy-tailed sums and maxima, rare spikes. This holds on the raw, log1p and
  normal-score scales. `verification/gaussian_pairwise_nonlinear.py`.
- **Why (⟦HAND⟧, not Lean).** For independent pair-sources, use the Hoeffding/Efron–Stein decomposition. Two sites share only Sᵢⱼ, so
  Cov(yᵢ,yⱼ) = Cov(E[yᵢ|Sᵢⱼ], E[yⱼ|Sᵢⱼ]), and Cauchy–Schwarz gives rᵢⱼ² ≤ tᵢⱼ tⱼᵢ with tᵢⱼ = Var E[yᵢ|Sᵢⱼ] / Var yᵢ. The first-order terms
  are orthogonal, so Σⱼ tᵢⱼ ≤ 1; shrinking t to equality keeps the sums ≤ 1. **So V_G ≤ 0 for ANY pairwise-only world** (arbitrary responses,
  local noise; stationarity across years as before). The Gaussian test is therefore model-free for Pearson correlations, under any monotone
  or non-monotone per-site transform.
- **Prior art (owned until checked):** very likely the pairwise case of the covariance/semidefinite tests for latent networks (Kela,
  von Prillwitz, Åberg, Chaves & Gross, "Semidefinite tests for latent causal structures", IEEE Trans. Inf. Theory, ~2020), from memory and
  unread. Not claimed.

## Step 3 amendment (before running step 3)
V_G is model-free, so a **secondary model-free inference** is added: moving-block bootstrap of V_G (b = 3, no wrap, 2000 resamples; lower
bound > 0). Reductions for compute: 2000 posterior draws (not 20 000). The placebo uses the point V_G of the residual correlation matrix per
permutation (200 permutations), compared with the real-ΔT point V_G.
