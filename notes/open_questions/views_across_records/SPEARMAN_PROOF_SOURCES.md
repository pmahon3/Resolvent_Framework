# Spearman reach test: proof sources for bootstrap consistency

reviewed: false. 2026-11-05. Methods read (LLM). It closes the open gap in `REACH_TEST_VALIDITY.md` step 2. The shelf had no copula/bootstrap entries, so the PDFs came from arXiv into `~/.claude/jobs/26482d7b/tmp/pdfs_spear/` (not shelved). Scripts are in the same tmp dir.

## 1. Theorem chain

| # | Statement used | Source | Read level |
|---|---|---|---|
| A | Condition 2.1: √n(G_n − C) ⇝ B_C in ℓ^∞([0,1]^d) for the uniform empirical process. It holds under α-mixing (Rio 2000 Thm 7.3). Ex. 2.2: a stationary ARMA/VAR with abs. continuous innovations is **exponentially β-mixing** (Mokkadem 1988). | Bücher–Volgushev, JMVA 120 (2013), arXiv:1111.2778 | text read |
| B | Condition 2.3 (Segers): "∂_pC exist and are continuous on U_p = {u: u_p ∈ (0,1)}". Thm 2.4: the copula map Φ is Hadamard differentiable at C tangentially to D_0. Cor. 2.5: √n(Ĉ_n − C) ⇝ G_C = B_C − Σ_p ∂_pC·B_C(u^(p)). | same | text read |
| C | Ex. 2.7: Spearman's ρ = continuous map of C, so √n(ρ_n − ρ) ⇝ N(0, σ²). | same | text read |
| D | Gaussian copula with **full-rank** R satisfies Condition 2.1 = BV Condition 2.3. It fails to extend to the boundary, but it is not required to. | Segers, Bernoulli 18 (2012), Ex. 5.1 | text read |
| E | **Thm 2 (MBB).** Strictly stationary, Σ_r (r+1)^{16(d+1)} √α(r) < ∞, l_B = O(n^{1/2−ε}), Condition (3) = Segers. Then "the block bootstrap empirical copula process converges weakly conditional on X_1..X_n in probability": √n(Ĉ_n^B − Ĉ_n) ⇝ G_C. Blocks B_{h,l} = {X_{h+1},…,X_{h+l}} with H_i uniform on {0,…,n−l_B}, i.e. MBB without wrap. **Ranks are recomputed in the resample**: Û^B_{j,i} = n^{-1} Σ_k 1{X^B_{k,i} ≤ X^B_{j,i}} (their iid display, carried to blocks). Proof: Bühlmann 1993 Thm 3.1 + BV Cor. 2.11. | Bücher–Ruppert, JMVA 116 (2013), arXiv:1206.1675v1 | Thm 1–2 and §2.2.1 text read |
| F | Cor. 2.11: Conditions 2.3 + 2.8 give √n(C_{n,b} − C_n) ⇝ G_C conditionally (Hoffmann-Jørgensen). Ex. 2.10 checks Condition 2.8 for the block bootstrap: same mixing sum, l_n → ∞, l_n = O(n^{1/2−ε}). Bootstrap delta method: Kosorok 2008 Thm 12.1. | BV 2013 | text read; Bühlmann and Kosorok **not read** (via BV) |
| G | Alternative (Prop. 4.2, dependent multiplier): α_r = O(r^{−a}), a > 3 + 3d/2, ℓ_n = O(n^{1/2−ε}); needs partial-derivative estimators (Cond. 4.1). | Bücher–Kojadinovic, Bernoulli 22 (2016), arXiv:1306.3930 | Prop. 4.2 read; Conds 3.2/3.3/4.1 **not read** |
| H | Residual copula ≈ oracle copula in sup norm (Thm 3, under T1, T2, C1, Z1). §4.2 does a linear regression with **stationary β-mixing random covariates independent of the errors**. **No bootstrap.** A deterministic t is not covered. | Neumeyer–Omelka, arXiv:2303.16260 | Thm 3, §2.1, §4.2 read |
| I | The law of the max of a separable Gaussian process is continuous except possibly at one point a₀. | Tsirel'son, TPA 20 (1975) 847–856 | abstract paraphrase only; secondary |
| J | Bootstrap quantile consistency at a continuity point. | van der Vaart 1998 Lemma 23.3 / 21.2 | from memory |

**Assembly** (d = k sites; the k-dim copula of Y_t).
1. **Joint, all pairs.** Let u^{(ij)} be u with every coordinate except i, j set to 1. Then L(f)_{ij} = 12∫∫ f(u^{(ij)}) du_i du_j − 3 is a bounded linear map ℓ^∞([0,1]^k) → R^{k(k−1)/2}, so it is continuous. Ĉ_n(u^{(ij)}) is exactly the bivariate empirical copula of sites (i, j). By (B)+(E) and continuous mapping (unconditional, and conditional via Kosorok Prop. 10.7, from memory):
   - √n(ρ̃ − R) ⇝ G, with G_{ij} := 12∫∫ G_C(u^{(ij)}) du_i du_j;
   - √n(ρ̃* − ρ̃) ⇝ G conditionally in probability,

   where ρ̃ = L(Ĉ_n) is the plug-in matrix and R = L(C) is the population Spearman matrix, i.e. Corr(F_i(Y_i), F_j(Y_j)). No Hadamard step beyond (B) is needed.
2. **Bridge lemma (plug-in vs computed Spearman) ⟦HAND⟧.**
   - Tie-free sample: ΣR_iR_j enters both forms affinely. Pearson-of-ranks = (n²/(n²−1))·plug + O(1/n), deterministically.
   - Resample: ties come only from duplicated time points, with multiplicity M_t ≤ number of blocks covering t, and max_t M_t = O_p(log n). Midrank vs max-rank then shifts each scaled rank by ≤ max M/n. The midrank-variance tie factor is 1 − Σ(M³−M)/(n³−n) = 1 − O_p(n^{−2}). So √n·gap* → 0 in bootstrap probability.
   - Numerics (`spear_mbb_tie_check.py`, AR(1) φ = 0.5, l = n^{1/3}). The quantity is √n|(Pearson* − Pearson) − (plug* − plug)|; its mean decays like n^{−1/2}:

     | n | 53 | 500 | 5000 | 50000 |
     |---|---|---|---|---|
     | mean | 0.77 | 0.27 | 0.085 | 0.027 |

     ⚠ At n = 53 the two conventions differ materially, so finite size must come from simulation.
3. **V_m.** V_m is 1-Lipschitz (CHECK doc). By continuous mapping, W = V_m(√n(R̂−R)) ⇝ V_m(G), and the bootstrap law of V_m(Z*) ⇝ V_m(G) conditionally.
4. **No atom ⟦HAND⟧** (replaces I as the primary argument).
   - G is Gaussian on its support subspace S, with a Lebesgue density on S.
   - For t > 0, V(x) = t implies V((1+ε)x) > t, so {V = t} ⊂ ∂{V ≤ t}. That set is convex, so its boundary is Lebesgue-null in S, and P(V(G) = t) = 0.
   - At t = 0: G has zero diagonal, so V(G) = 0 iff G = 0, and P(G = 0) = 0 when Σ ≠ 0.
   - So the law of V_m(G) is continuous everywhere, and ĉ → c₁₋α in probability (J).
5. Domination (proved) gives lim sup P(T > ĉ) ≤ lim P(W > ĉ) = α.

## 2. Covered procedure (recipe)
1. Data: Y_t ∈ R^k, t = 1..n, **raw series, no detrending**. log1p does not matter, since ranks are invariant under monotone maps.
2. R̂ = matrix of Spearman correlations, i.e. Pearson correlation of within-series midranks (or the plug-in 12·n^{-1}Σ(1−R_ti/n)(1−R_tj/n) − 3; the two are equivalent by step 2).
3. T = √n·V_m(R̂).
4. MBB: block length l = ⌈n^{1/3}⌉ (any l → ∞ with l = O(n^{1/2−ε}) works), k_b = ⌈n/l⌉ start points uniform on {0,…,n−l}, concatenate and truncate to n. **Re-rank within each resample.** Z* = √n(R̂* − R̂), D* = V_m(Z*), B ≥ 1000 resamples; ĉ = (1−α) quantile of D*.
5. Reject H₀(m) if T > ĉ. Fixed sequence m = 2, 3, …

**Changes from the current pipeline.**
- (i) Normal scores → ranks. Without this, (E) does not apply, because the BBV 2017 weighted metric has no bootstrap.
- (ii) Drop the detrending in the provable version. Keep detrend-then-rank only as a sensitivity run, with trend ratios reported.
- (iii) The MBB scheme itself is unchanged and is covered. A circular variant is not what (E) states.

Option (b), the residual copula, is not provable from what I read:
- (H) needs stationary random covariates;
- re-detrending inside resamples has no theorem;
- resampling residuals breaks (E)'s stationarity hypothesis.

## 3. Proposition (pointwise)
Let m ≥ 2. Assume:
- (a) (Y_t) is strictly stationary with continuous margins, and Σ_r (r+1)^{16(k+1)} √α(r) < ∞. For k = 10 this exponent is 176, so the condition is in effect geometric mixing. It holds for stationary VARs with abs. continuous innovations (A, Ex. 2.2).
- (b) The k-variate copula C of Y_t satisfies Segers' condition (BV Cond. 2.3). It holds for the Gaussian copula with full-rank R (D).
- (c) Σ = Cov(L(G_C)) ≠ 0.

Then, for every such law with R ∈ FW_m (R the Spearman matrix), the §2 test satisfies lim sup_n P(T > ĉ) ≤ α.

Not uniform over the null; see the CHECK doc conditions (i)–(ii).

## 4. Remaining gaps
1. **Smoothness.** "Spearman needs only continuity of C" (no Segers condition) is plausible, by analogy with Hoeffding's U-statistic in the iid case, but **unowned** under mixing. Keep (b).
2. **Unread links.** Bühlmann 1993 Thm 3.1, Kosorok Thm 12.1 / Prop. 10.7 and vdV Lemma 23.3 were used through citations, not read. Tsirelson is at abstract level, but step 4 does not need it.
3. **Detrending under a real trend.** No owned theorem covers residual ranks with a deterministic trend and mixing errors, or the bootstrap of that procedure. Stationarity is therefore an assumption checked by trend ratios, not a theorem.
4. **Bridge lemma** (step 2) and **no-atom** (step 4) are ⟦HAND⟧. Both are elementary and should be checked independently.
5. **Re-run required.** The switch to Spearman changes R̂ and the population R. Poland's m̂* = 4 and the m = 2/3 size checks were all done with normal scores and do **not** transfer. A Spearman re-run (Poland reach sequence plus a size check at n = 53, stationary worlds) must be **declared before running**.
6. **Asymptotic regime.** n = 53, k = 10, with a 176-power mixing sum. The asymptotics are a weak guide, and finite-sample size rests on simulation.
