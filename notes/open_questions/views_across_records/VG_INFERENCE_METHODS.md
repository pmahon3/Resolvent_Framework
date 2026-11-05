# Established inference methods for the V_G ceiling test

reviewed: false. 2026-11-05. Methods reading for `VG_TEST_VALIDATION.md` (runs 2–3 failed). Nothing here has been run yet.

## 0. Structural fact that selects the method ⟦HAND⟧
|R−I| is entrywise nonnegative, so φ(R) := ρ(|R−I|) = max over unit x ≥ 0 of Σ_{i≠j} |r_ij| x_i x_j.
Equivalently φ(R) = max over witnesses W (W_ij = s_ij x_i x_j, x ≥ 0 a unit vector, s a sign pattern) of ⟨W, R−I⟩.
- **Convex:** a max of linear functions of R.
- **Lipschitz:** constant 1 in the Frobenius norm, since ‖xxᵀ‖_F = 1 (Cauchy–Schwarz).
- **H₀ = {φ ≤ 1} is a closed convex set.** This puts the problem inside Fang–Santos §4 (testing membership of a convex set) and Hong–Li §3.2 (uniform validity for a convex, Lipschitz φ).
- Directional derivative (Danskin) ⟦HAND⟧: φ'_R(h) = max over the nonnegative unit maximisers x of Σ_{i≠j} d_ij(h) x_i x_j. Here d_ij = sgn(r_ij)·h_ij if r_ij ≠ 0, and d_ij = |h_ij| at the kink r_ij = 0.
  - When |R−I| is reducible, the maximisers are the nonnegative part of the top eigenspace.
  - Numerically checked on the 10-ring only (simple root); 2×10⁴ random pairs gave no convexity violation.

## 1. Methods read

**Fang & Santos, "Inference on directionally differentiable functions", REStud 86 (2019); arXiv:1404.3763v2.**
Read: key sections §2–4 and the simulations. Numbering is arXiv's and may differ from the journal version.
- **Result.** √n(φ(θ̂)−φ(θ₀)) ⇝ φ'_{θ₀}(G₀). The standard bootstrap is consistent iff φ is fully differentiable (Thm 3.1; Dümbgen 1993 earlier). The remedy is the law of φ̂'_n(√n(θ̂*−θ̂)) (Thm 3.2, Cor 3.2).
- **Derivative estimator.** φ̂'_n must be consistent for φ'_{θ₀} on δ-enlarged compacts (Ass. 3.3). They warn that the plug-in φ'_{θ̂} usually fails this.
- **Tests and size control.** The test of H₀: φ ≤ 0 rejects if r_n φ(θ̂) > ĉ_{1−α}. This gives pointwise size, plus local size control along contiguous null sequences when φ'_{θ₀} is subadditive (Thm 3.3; subadditive ⇔ convex). For convex sets, subadditivity always holds (Prop 4.2(ii)).
- **Tuning.** Selection and step parameters must satisfy ε_n → 0 and √n·ε_n → ∞ (eq. 39, Prop 4.2(i)). Simulations use ε_n = C·n^{−κ} with C ∈ {0.01, 1} and κ ∈ {1/4, 1/3}. C = 1 was conservative and C = 0.01 close to nominal (n = 200, 500).
- **Dependence.** They say the results apply to dependent data. The only requirement is a consistent bootstrap for √n(θ̂*−θ̂) (Ass. 3.1). No specific time-series bootstrap is given.
- GMS is a special case (Remark 4.3).

**Hong & Li, "The numerical delta method", J. Econometrics 206 (2018) 379–394.** Read: key sections §2–3 and §5 (NSF PAR copy).
- **Estimator.** φ̂'_n(Z*) = [φ(θ̂ + ε_n Z*) − φ(θ̂)]/ε_n, with Z* any consistent draw (bootstrap, N(0, Σ̂), subsampling).
- **Pointwise validity.** Requires φ Lipschitz, ε_n → 0 and r_n ε_n → ∞ (Thm 3.2).
- **Uniform validity.** Thm 3.5: for φ convex and Lipschitz, ε_n → 0, r_n ε_n → ∞, uniform tightness and bootstrap consistency over the class P (their Ass. 3.1–3.2), lim sup_n sup_P P(reject) ≤ α.
  - Their prose (not the theorem) adds that ε_n → 0 is not needed for conservative uniform validity.
  - The mechanism is that for convex φ the difference quotient is nondecreasing in ε (their eq. 15).
- **No selection step.** Kinks and degenerate roots are handled by evaluating φ directly.
- **Simulations.** They use ε_n ∈ {log n/√n, n^{−1/6}, n^{−1/3}, n^{−1/2}}. Size distorts upward as ε_n approaches n^{−1/2}.
- **Dependence.** Not treated beyond "Z* can be any consistent approximation". Uniform bootstrap consistency for dependent data is assumed, not proved.

**Andrews & Soares, Econometrica 78 (2010) 119–157.** Read: Cowles DP 1631 (2007), at grep level only.
- **Guarantee.** GMS is uniformly asymptotically valid and not asymptotically conservative. It covers "i.i.d. and dependent observations", and the block bootstrap is allowed in time series.
- **Tuning.** The working paper uses κ_n = (2 ln ln n)^{1/2}. It lists BIC κ_n = (ln n)^{1/2} as a model-selection analogue. Hong–Li attribute the step √(ln n)/√n to AS 2010 (journal version; not checked here).
- **Not read:** Andrews–Barwick (2012) refinements.

**Kela, von Prillwitz, Åberg, Chaves, Gross, IEEE TIT 66 (2020) §XI (on the shelf).** Read: the section in full. It is a sketch; details are left to future work.
- Split the sample. Fit a dual witness W on part 1. On part 2, test the single linear inequality ⟨W, Cov⟩ ≤ c.

**Not read; one line each on why they are not the route:**
- *t_ij reformulation with nuisance parameters* (Bugni–Canay–Shi 2017): 90 nuisance parameters, and the r² moments have zero gradient at r = 0 (first-order degeneracy).
- *Many moment inequalities* (Chernozhukov–Chetverikov–Kato 2019; time-series Gaussian approximation by Zhang–Wu 2017): the witness family has 2^45 sign patterns times a continuum of x, and the statistic is not a max of means.
- *Spiked-eigenvalue tests* (Johnstone 2001, Onatski): the null is not sphericity, and the entrywise |·| breaks the random-matrix link.

## 2. Diagnosis of the earlier failures (from the theory)
- **Run-2 (B) is Hong–Li with ε = 1/√n.**
  - In that case the quotient equals √n(V*−V̂), so the rule "√nV̂ > q₉₅" is the same as "2V̂ − q₉₅(V*) > 0".
  - It violates r_n ε_n → ∞, since √n·ε = 1. At a kink, the quotient then sees |r̂_ij + Z*/√n| − |r̂_ij| instead of |Z*|.
- **Run-2 (P) is the standard bootstrap.** It is inconsistent because φ is not differentiable (FS Thm 3.1).
- **Run-3 (C) used a plug-in, non-least-favourable base point.** FS warn that this fails Ass. 3.3.

## 3. Recommended recipe: Hong–Li numerical delta method
1. **Prep.** Per site, rank → Φ⁻¹ → linear detrend. Set R̂ = Pearson correlation and T = √n·(φ(R̂) − 1).
2. **Z* (dependence).**
   - Use a circular (Politis–Romano 1992) or moving block bootstrap on the raw multivariate series, resampling time blocks jointly across sites.
   - In each resample, rerun the full prep, then compute Z*_b = √n(R̂*_b − R̂), for b = 1…B with B ≥ 1000.
   - Block length: b ≈ n^{1/3} (3–4 at n = 30–80), or Politis–White (2004) automatic selection with the Patton–Politis–White (2009) correction.
3. **Statistic per draw.** D_b(ε) = [φ(R̂ + ε Z*_b) − φ(R̂)]/ε. Use the exact eigenvalue: φ(A) = λ_max(|A − diag A|). No kink or eigenvalue selection is needed.
4. **Decision.** Reject H₀ if T > q_{0.95}{D_b(ε)}.
5. **Choice of ε.**
   - **Monotonicity.** For each draw, D_b(ε) is nondecreasing in ε, so the rejection regions are nested. One set of draws gives the whole ε-curve.
   - **Pre-registered grid:**
     - ε = 1/√n: equals run B; a regression check.
     - ε = √(ln n/n): ≈ n^{−1/3} here (0.34 vs 0.32 at n = 30), so √n·ε ≈ 1.8–2.1. Expect residual oversize at k = 10.
     - ε = n^{−1/6}: ≈ 0.5, so √n·ε ≈ 3.1–4.
     - ε = ∞: D → λ_max(|Z*|). Every entry is treated as at the kink, the "all moments binding" bracket. This is conservative.
   - **Selection rule:** take the smallest grid ε whose size is ≤ 0.07 in every boundary cell of the validation grid. If none passes, use ε = ∞.
   - Validation picks ε; theory only gives the rate.
6. **Optional diagnostic (FS analytic).**
   - Kink set: |r̂_ij| ≤ κ_n·σ̂_ij/√n, with κ_n = √(ln n) and σ̂_ij from the block bootstrap.
   - Maximise over nonnegative near-top unit eigenvectors (eigenvalues within κ_n/√n of the top).
   - Misclassifying toward the kink or the degenerate case is conservative, because it enlarges the max.
   - This shares Z* and the asymptotics with HL, so it is no independent protection.

**Second choice: split-sample witness test (Kela §XI), which fails differently.**
- On the first contiguous half: fit x̂ = the Perron vector of |R̂₁ − I| and ŝ = sgn(R̂₁).
- On the second half: compute L̂ = Σ_{i≠j} ŝ_ij x̂_i x̂_j r̂₂,ij − 1. Every R ∈ H₀ has L ≤ 0 for any fixed (x, s), so L is a valid one-sided target.
- Test L ≤ 0 with a one-sided block-bootstrap or HAC z-test. Size rests on a scalar CLT for a smooth statistic, with no kink.
- Costs:
  - The halving of n (15–40 per half) costs power.
  - The two halves are dependent at the seam. One remedy is to drop ~b observations there.

## 4. Failure modes at k ≤ 10, n = 30–80
- **√n·ε is small.** Separating step from noise is weak, √n·ε ≤ 4 throughout. Size control will lean on convexity, which makes it conservative, so power is the price.
- **Bias at many near-zero correlations.**
  - Many near-zero r_ij each add about |Z|·x_i x_j to the statistic. The test reproduces this bias rather than removing it, so the critical value is large.
  - So expect low power for P1/P2-type alternatives (diffuse weak correlations with a weak common factor).
- **The block bootstrap may understate the variance** at n = 30 (b = 3), as it did for run B. Asymptotic guarantees assume Z* is consistent, and here Z* is the weak link.
- **Normal scores and detrending inside the bootstrap.** Ties from duplicated blocks perturb the ranks. A mid-rank convention is needed.
- **No finite-sample guarantee:** uniformity is asymptotic and assumes uniform bootstrap consistency.

## 5. What validation should check
1. **Z* first.** For true-zero pairs (W3 non-neighbours), compare the bootstrap Var(√n r̂*_ij) with the Monte Carlo value and with Bartlett's (1+φ²)/(1−φ²) ≈ 1.67 at |φ| = 0.5. Do this for b ∈ {3, 4, 6}.
2. **The ε-curve** on W1–W4, at n ∈ {30, 53} and φ = ±0.5, from one set of draws per dataset.
   - Pass: size ≤ 0.07.
   - The Monte Carlo standard error is ≈ 0.013 at 300 simulations.
3. **Interior null R = I (V_G = −1).** The plug-in V̂_G there is about +0.3–0.7 at n = 30. The test must not reject.
4. **The regression check:** ε = 1/√n must reproduce run B's failure.
5. **Power** on P1/P2 at the selected ε, and for the split-sample test.
6. **A non-Gaussian boundary** (W4) and a reducible boundary (two disjoint triangles, so the Perron root is degenerate).
