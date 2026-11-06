# Reach test validity: independent check

reviewed: false. 2026-11-05. Independent check. The checker is hostile to the author, but this is still an LLM check.
Scripts are in `~/.claude/jobs/26482d7b/tmp/` (`chk.py`, `trend.py`, `pl_order.py`).

## Step 1 (exact domination): CORRECT, and simpler than stated
- V_m(R) = max_{X∈C} −⟨X,R⟩, with C = {X ∈ FW_m*, tr X = 1}. This makes V_m a **support function**, hence sublinear.
  - For m ≥ 2, C is compact: the 2×2 minors give |X_ij| ≤ √(X_ii X_jj), and ‖X‖_F ≤ tr X = 1.
  - So V_m is finite and 1-Lipschitz in the Frobenius norm.
  - At m = 1, V_1 ≡ +∞ off the diagonal matrices. "Every m" must read **m ≥ 2**.
- Because ⟨X,I⟩ = 1 on C, h_m(Z) = V_m(I+Z) + 1 = V_m(Z). **The recession function is V_m itself.** Checked numerically on 3 random 7×7 matrices, m = 2…7: the two sides agree to 10⁻⁴.
- Domination is plain subadditivity: V_m(R̂) ≤ V_m(R) + V_m(R̂−R), and V_m(R) ≤ 0 under H₀. No general convex-recession lemma is needed; it is the standard σ(x+y) ≤ σ(x) + σ(y) for support functions.
  - Primal proof: if R + tI ∈ FW_m and S + sI ∈ FW_m, the sum lies in FW_m because FW_m is a convex cone.
  - Signs are correct. Numerics: V₂(R+Z) = 1.92 ≤ 2.41 = V₂(R) + V₂(Z); V(3Z)/3 = V(Z).
- Zero diagonals do no harm. Both sides use zero-diagonal Z, and `Z − diag(Z)` in the code is a no-op (correlation diagonals are exactly 1).
- Useful fact: if Z has zero diagonal, then V_m(Z) ≥ 0 (take X = I/k), with equality iff Z = 0.
  - Reason: a zero-diagonal element of FW_m is a sum of PSD blocks with zero diagonals, so it is 0.

## Step 2 (bootstrap and quantile): CORRECT WITH FIXES
- Continuous mapping holds unconditionally and for the bootstrap (h_m is Lipschitz and does not depend on R).
- The quantile step is valid **iff the law of h_m(G) has no atom at c₁₋α**. Strict increase is not needed: 1 − F(c−) ≤ α requires F to be continuous at c.
- h_m(G) = sup_{X∈C} ⟨−X, G⟩ is the supremum of a centred Gaussian process over a compact set.
  - **Tsirelson (1975)**: such a law is continuous except possibly at the left end of its support. *Cited from memory, not re-read.*
  - By the fact above, that end is 0 and P(h_m(G) = 0) = P(G = 0).
  - So **there is no atom whenever Σ = Cov(G) ≠ 0**, even if G is degenerate in some directions.
- Σ = 0 under H₀(m) with m < k would need |r_ij| = 1 for every pair. That makes R a rank-one sign matrix of factor width k, which is not in H₀. **R = I does not give G = 0**: correlations still fluctuate at the √n scale. The edge case is therefore empty in practice, but it should still be stated as an assumption.
- **The result is pointwise.** Because ĉ does not depend on R, uniformity reduces to two conditions, neither of which is proved:
  - (i) bootstrap consistency uniform over the null class 𝒫;
  - (ii) uniform anti-concentration of h_m(G_P), e.g. λ_min(Σ_P) ≥ σ² > 0. This is the Hong–Li Thm 3.5 template.
- The test is conservative at almost every boundary point too. The exact limit there is max over the optimal face of −⟨X,G⟩, which is ≤ V_m(G).
- **Power observation.** For generic zero-diagonal Z, V_m(Z) = −λ_min(Z) for every m ≥ 3; this held numerically in all 3 trials.
  - That explains why the Poland critical value is 7.65 for every m = 3…9: the ε = ∞ test of H₀(m ≥ 3) uses the same critical value as the PSD null.
  - This is maximal slack. It does not affect validity, but power for m ≥ 3 is the price.

## Step 3 (bootstrap consistency for this pipeline): NOT COVERED BY ANY SINGLE THEOREM
| Source | What it gives | Read level |
|---|---|---|
| Berghaus–Bücher–Volgushev, Bernoulli 23 (2017), Thm 2.2, Thm 3.3, Ex. 3.5 | **CLT** for the van der Waerden (normal-scores) rank correlation under stationary, **exponentially** α-mixing data with C¹ copula partial derivatives (Condition 2.1); needs a weighted metric because Φ⁻¹ is unbounded | PDF text grepped; theorem statements read. **The word "bootstrap" appears 0 times.** |
| Bücher–Ruppert, JMVA (2013; arXiv:1206.1675), Thm 2 | Moving-block bootstrap of the empirical copula, conditional weak convergence in **sup norm only**; Σ(r+1)^{16(d+1)}√α(r) < ∞; block length ℓ = O(n^{1/2−ε}) (n^{1/3} qualifies); rests on Bühlmann (1993) | first 100k chars via fetch summary |
| Künsch 1989; Lahiri 2003 | Block bootstrap for smooth functions of means (raw Pearson) | not re-read; standard |
| Fitzenberger, J. Econometrics 82 (1998) | MBB for least squares with nonstochastic (Grenander-type) regressors | abstract only |

**Consequences:**
- The sup-norm bootstrap plus the functional delta method covers **bounded-score** functionals such as Spearman. It does not cover normal scores: the bootstrap in the weighted metric under mixing was not found.
- **Switching to Spearman (or truncated scores) closes this gap with owned theorems.**
- Detrending: if **Y is stationary**, OLS on (1, t) changes each correlation by O_p(1/n) = o_p(n^{-1/2}). This holds in the sample and in the resample.
  - In the resample, t* is block-permuted but still has Σ(t*−t̄*)² ≍ n³ and a weighted sum of O_p(n^{3/2}), so the correction is O_p(1/n).
  - So under stationarity the nuisance is asymptotically void, and the non-monotone t* is harmless. ⟦HAND⟧
- **Where it breaks: rank first, detrend second.** If Y has a real linear trend, the scores Φ⁻¹(rank/n) carry a nonlinear residue in t that linear OLS cannot remove, and that residue is shared across sites.
  - Counterexample (`trend.py`: 10 independent sites plus a trend, n = 53). Mean off-diagonal r̂ after preprocessing, by trend-SD/noise-SD ratio:

    | trend/noise ratio | mean off-diagonal r̂ |
    |---|---|
    | 0.3–0.8 | 0.000 |
    | 3.1 | +0.047 |
    | 15 | +0.74 |

    For k = 10, a uniform shift c moves V₂ by ≈ 9c, so the ratio-3 case is already material near the boundary.
  - So the stated assumption "stationarity after detrending" is **wrong for this pipeline**. What is needed is that Y is stationary, or that the order is changed to detrend first, then rank.
  - Leads for the residual empirical copula: Chen–Fan 2006; Rémillard 2017; Neumeyer–Omelka–Hudecová 2019. Not read.
- **Poland is unaffected** (`pl_order.py`).
  - Trend/residual SD ratios: ≤ 0.28 on the scores, ≤ 0.33 on raw Y.
  - Swapping the order changes r̂ by at most 0.082.
  - T for m = 2/3/4 moves from 34.9/13.8/6.8 to 35.8/14.25/7.08, against a critical value of 7.65. m̂* = 4 is unchanged.
- Minor: an MBB without wrap underweights the end years. The centring bias is O(b/n), negligible at √n but present at n = 53; a circular bootstrap is cleaner. Mid-ranks from duplicated blocks are fine.

## What is actually proved
For m ≥ 2, suppose:
- (a) Y is strictly stationary and α-mixing;
- (b) √n(R̂−R) ⇝ G, Gaussian with Cov(G) ≠ 0;
- (c) the MBB is consistent for it, conditionally in probability.

Then the following holds pointwise for every P with R_P ∈ FW_m:

lim sup_n P(√n V_m(R̂) > ĉ) ≤ α.

Condition (b) is owned (BBV 2017) under exponential mixing and Condition 2.1. Condition (c) is **assumed** for normal scores and owned (Bücher–Ruppert) for Spearman. Uniform size needs (i) and (ii) from Step 2. The fixed-sequence m̂* is valid because the nulls are nested.

## Required fixes
1. State m ≥ 2. Replace the recession-function wording with "V_m is sublinear (a support function); h_m = V_m".
2. Add "law of h_m(G) continuous at c₁₋α", justified by Tsirelson (re-read it) and Σ ≠ 0. Say **pointwise**.
3. Replace "stationarity after detrending" with "Y stationary", or switch to detrend-then-rank. Report trend ratios with every run.
4. Mark bootstrap consistency as **unproved for normal scores** (owned for Spearman). Optionally rerun with Spearman.
5. Note that the critical values for m ≥ 3 coincide with the PSD (m = k) critical value, so power is low by construction.
