# Spearman reach test: independent check

reviewed: false. 2026-11-05. Independent check by a hostile LLM checker. Sources were re-read from the arXiv full texts (1111.2778, 1206.1675) and from the shelf Kela PDF. Scripts: `~/.claude/jobs/26482d7b/tmp/chk_ties2.py`.

## Headline: the proposition holds, but Poland is outside its hypothesis (A2)
- The Poland inputs actually used (study D00013, 10 sites, n = 53) are **integer-valued** ("% individuals reproducing").
- Per site, **58–79% of the observations are tied**. The largest tie group has 5–16 members, with 21–33 distinct values in 53.
- So the marginals have atoms and (A2) fails. Tie groups then grow **linearly in n**, which breaks four things:
  - The bridge fails **at the level of the target, not just the rate**. Midrank-Pearson converges to Corr(F^mid_i(Y_i), F^mid_j(Y_j)), where F^mid = (F + F₋)/2. The generalized-inverse plug-in converges to a different limit.
  - Bücher–Volgushev and Bücher–Ruppert assume continuous margins, so neither applies.
  - Segers' condition is not even defined, because the copula is not unique.
- **Consequence:** V3(a) is **not** "the provable version" for Poland.
  - **MUST-NOTE:** `CEILING_TEST_VALIDATION.md:28` says "Real beech seed counts are continuous". That is false for Poland.
- **Null validity survives discreteness.** F^mid is a per-site transform, and the Spearman matrix equals D^{-1/2} Cov(F^mid(Y)) D^{-1/2}. A diagonal congruence preserves FW_m, so the Kela step below still holds. Only the asymptotics break.

## 1a. Bridge lemma: CORRECT WITH FIXES (continuous margins, and no sample ties)
- **Read of BV.** BV's estimator is C_n = F_n(F_n^−(u)), the generalized inverse. Their bootstrap copula is C_{n,b} = F_{n,b}(F_{n,b}^−(u)), so ties in the resample are handled natively.
- **Key fact.** The rank-based copula (max-ranks, re-ranked in the resample) differs from C_{n,b} in sup norm by at most d·max_t M_t/n.
  - Reason: X ≤ F^−(u) and F(X) ≤ u differ only at atoms, and an atom has mass ≤ M/n.
- **Chain to midranks.**
  - Midrank vs max-rank: each scaled rank moves by ≤ M/n.
  - The mean of the ranks moves by O(1/n).
  - The variance tie factor is 1 − O_p(n^{-2}). This holds because M_t ~ Bin(⌈n/l⌉, l/(n−l+1)) ≈ Poisson(1), so Σ(M³−M) = O_p(n).
- **Gap bound.** In total, |R̂* − ρ̃*| ≤ C·max_t M_t/n with C deterministic, and max_t M_t = O_p(log n). M depends **only on the block draws, not on the data**, so the bound holds conditionally, uniformly over samples.
- **Conditional step (missing from the source doc; add it).**
  - o_p(n^{-1/2}) in the joint probability (data × resample) gives conditional-in-probability smallness, by Markov's inequality.
  - Then |E* f(Z*) − E* f(Z*_plug)| ≤ E* min(2, |Δ*|) → 0 for every f ∈ BL₁. This bounded-Lipschitz Slutsky step transfers the Hoffmann-Jørgensen conditional convergence.
- So o_p(n^{-1/2}) is enough.
- **Caveat.** Continuous marginals do not exclude **sample** ties: P(Y_{i,s} = Y_{i,t}) > 0 is possible, e.g. for a process that "stays put". Add (A2′): P(Y_{i,s} = Y_{i,t}) = 0 for s ≠ t. An alternative is to require sample tie groups of size o_p(√n).
- **Minor slip in BR's own proof.** BR claim the rank-vs-inverse gap is O(n^{-1/2}). With duplicated blocks it is actually O_p(log n/√n). The slip is harmless.

## 1b. No atom: CORRECT
- **Setting.** G is Gaussian with mean zero and has a density on S = range(Σ). For t > 0, {V = t} ⊂ rel∂{x ∈ S : V(x) ≤ t}, and the boundary of a convex set is null in S.
- **t = 0.** V(G) = 0 iff G = 0, because G has zero diagonal and V_m(Z) ≥ ⟨I/k, −Z⟩ = 0, with equality only at Z = 0. P(G = 0) = 0 when Σ ≠ 0.
- **Degenerate directions** are handled by restricting to S.
- **Linear-on-S case: empty.** V ≥ 0 and V vanishes only at 0, so a V linear on S forces S = {0}.
- So the law is atomless everywhere, and the Tsirelson reference is not needed.
- **Add one line for ĉ → c.** F is also strictly increasing on [0, ∞): V(S) = [0, ∞), each set {a < V < b} is a nonempty open subset of S, and the density on S is positive. That gives ĉ → c₁₋α. Even without it, continuity alone gives lim sup ≤ α by the usual x_δ argument.

## 2. Cited theorems: CORRECT (statements match)
- **BV:** Cond. 2.1, Cond. 2.3 (∂_pC continuous on {u_p ∈ (0,1)}), Thm 2.4, Cor. 2.5, Ex. 2.7 and Ex. 2.10 / Cor. 2.11 all match the quotes. Ex. 2.10 rests on Bühlmann 1993 Cor. 3.1 (unread).
- **BR Thm 2:** d-dimensional; Σ_r (r+1)^{16(d+1)} √α(r) < ∞; l_B = O(n^{1/2−ε}).
  - No wrap (H uniform on {0,…,n−l_B}).
  - Re-ranks: the proof evaluates C_{n,b} at the resample's own marginal inverses.
  - Gives conditional weak convergence in probability (Hoffmann-Jørgensen, BL₁) in ℓ^∞([0,1]^d).
  - Truncating the last block is asserted, not proved. It is an O(l/√n) perturbation, so harmless.
- **Segers' condition:**
  - Holds for full-rank Gaussian copulas (Segers Ex. 5.1).
  - Plausible but **unchecked** for linear latent models with smooth, positive local-noise densities.
  - **Fails** for singular mechanisms: |r_ij| = 1, min/max or threshold rules, Marshall–Olkin types. These are relevant to masting, and thresholds also create ties.
  - Keep it as an assumption, and check it for each non-Gaussian world.

## 3. Null validity (Kela Prop. 1 on grades): CORRECT WITH A SCOPE NOTE
- **What Prop. 1 gives.** It applies to any finite-variance feature maps; grades are bounded scalars. It yields Cov(U) = D + Σ_n C_n, with D diagonal ⪰ 0 and C_n ⪰ 0 supported on ch(L_n), where |ch(L_n)| ≤ m.
- **Membership.** Each term lies in FW_m, and so does the cone sum. Scaling by 12 (continuous margins) or by D^{-1/2}·D^{-1/2} (midranks) preserves FW_m. So R_S ∈ FW_m.
- **Time series.** The marginal at a single t suffices, and **independence across time is not needed**. What is needed:
  - the latent sources are mutually independent **as whole processes**, since a lagged copy of a driver is the same latent;
  - each site-local noise process is independent of all the latents and of the other sites' noise;
  - for every t, the observations are conditionally independent given all the latents.
- **Couplings.** Direct site-to-site coupling, such as dispersal or pollen, counts as a latent touching both sites.

## 4. Other threats to pointwise size ≤ α
- Discrete margins (headline) are the only material break.
- Minor items:
  - Finite B gives Monte-Carlo error; B = 1000 is fine.
  - A constant resampled series (possible under heavy ties) makes R̂* undefined.
  - A zero long-run variance is possible, so keep (A3).

## Exact statement proved
For m ≥ 2, assume (A1), (A2) continuous margins with (A2′) no sample ties, Segers' condition, and (A3). Then for every law with R_S ∈ FW_m, the §2 procedure (MBB without wrap, re-ranking, l = ⌈n^{1/3}⌉) satisfies lim sup_n P(T_m > ĉ_m) ≤ α. This is **pointwise**, with B → ∞. The modules taken on trust are Bühlmann 1993 and Kosorok Thms 10.8 / 12.1.

## Fixes
1. Add (A2′) and the bounded-Lipschitz Slutsky line to the bridge. Add the strict-increase line to the quantile step.
2. **Poland, option (a): smooth jitter.** Add i.i.d. **Gaussian** jitter per site and per time, at a scale of about the grid spacing, then run the provable test.
   - Do **not** use uniform-on-cell jitter: the piecewise-constant density makes ∂C jump at the grid lines, so Segers' condition fails.
   - The direction of inference is sound. Jitter is site-local noise, so H₀(m) for the original data implies H₀(m) for the jittered data, and a rejection carries back.
   - Stationarity and mixing are preserved.
   - The test becomes randomized: pre-declare the jitter seed(s).
3. **Poland, option (b): keep V3(a) as is.** Then drop the "provable" label, and add to V2 a quantized world matching Poland's tie structure (integer scores, about 70% tied).
4. Genest–Nešlehová–Rémillard (the multilinear empirical copula) is a **lead only**. It is unread, so do not cite it for mixing or the bootstrap.
5. **MUST-NOTE:** `CEILING_TEST_VALIDATION.md:28` (stated in the headline). Also qualify the "provable version" wording in `REACH_TEST_SPEARMAN.md` §V3(a) and in `SPEARMAN_PROOF_SOURCES.md` §2.
