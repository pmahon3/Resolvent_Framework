# Covariance ceiling for pairwise-only worlds: independent check

reviewed: false. 2026-11-05. Independent check (hostile to the author) of the ⟦HAND⟧ proof in `GAUSSIAN_PAIRWISE_MODEL.md` § "Why", plus prior art.
Scripts: `~/.claude/jobs/26482d7b/tmp/check_vg.py` (scratch, not tracked).

## Verdict on the proof: CORRECT WITH FIXES (minor). The claim itself is OWNED (below).

- **(a) Cov(yᵢ,yⱼ) = Cov(E[yᵢ|Sᵢⱼ], E[yⱼ|Sᵢⱼ]).** Correct. Given Sᵢⱼ, yᵢ depends on ({Sᵢₗ}ₗ≠ⱼ, eᵢ) and yⱼ on ({Sⱼₗ}ₗ≠ᵢ, eⱼ). These are disjoint and jointly independent of each other and of Sᵢⱼ (this needs *mutual* independence of all sources, not only pairwise independence). So Cov(yᵢ,yⱼ|Sᵢⱼ) = 0, and the law of total covariance gives the identity. Needs finite variances.
- **(b) Σⱼ Var E[yᵢ|Sᵢⱼ] ≤ Var yᵢ.** Correct. gⱼ := E[yᵢ|Sᵢⱼ] − Eyᵢ is the projection of yᵢ − Eyᵢ onto the mean-zero part of L²(σ(Sᵢⱼ)). These subspaces are mutually orthogonal because the sources are independent, so Bessel's inequality gives the bound. The Hoeffding decomposition is more than is needed.
- **(c) Shrinking.** Correct when rᵢⱼ ≠ 0: rescale tᵢⱼ by rᵢⱼ²/(tᵢⱼtⱼᵢ) ≤ 1. **Fix:** when rᵢⱼ = 0, the equality tᵢⱼtⱼᵢ = 0 is impossible with t > 0, as the note's "∃ tᵢⱼ > 0" requires. Allow t ≥ 0 and set tᵢⱼ = tⱼᵢ = 0. (The script's `+1e-12` hides this numerically.) Also require Var yᵢ > 0.
- **(d) Equivalence with V_G.** Correct once (c) is fixed. Write tᵢⱼ = |rᵢⱼ|e^{w}, tⱼᵢ = |rᵢⱼ|e^{−w}. The max-load is convex and coercive in w, so the minimum is attained, and V_G ≤ 0 ⟺ feasible. **Closed form (new to the note; ⟦HAND⟧, verified numerically to optimiser error 5·10⁻³ on 160 random R):**
  **V_G(R) = ρ(|R − I|) − 1**, where ρ is the Perron root of the matrix of |rᵢⱼ| (diagonal zeroed).
  - Upper bound: put tᵢⱼ = |rᵢⱼ|vⱼ/vᵢ, with v the Perron vector. Every row sum is then ρ. If |R−I| is reducible, do this per irreducible component; ρ is then the max over components.
  - Lower bound: for any admissible T, ρ(|R−I|) = ρ(T^{∘½}∘(Tᵀ)^{∘½}) ≤ ρ(T)^{½}ρ(Tᵀ)^{½} = ρ(T) ≤ max row sum. The middle step is the geometric-symmetrisation (Schwenk) case of Elsner–Johnson–Dias da Silva, LMA 24 (1988) 1–13 (statement confirmed via secondary sources, not read).
  - So the SDP or optimiser is unnecessary: one eigenvalue suffices.
- **(e) Equal triangle.** Correct, and sharper: |r| ≤ ½. Proof: AM-GM gives Σ(tᵢⱼ+tⱼᵢ) ≥ 6|r|, and the rows give Σ ≤ 3. The bound is sharp on both signs. For r = +½ take y₁ = S₁₂+S₁₃ and so on. For r = −½ take y₁ = S₁₂+S₁₃, y₂ = −S₁₂+S₂₃, y₃ = −S₁₃−S₂₃.
- **Converse (also true):** every feasible R is the correlation matrix of a *linear* pairwise world (aᵢⱼ = √tᵢⱼ with signs, plus noise). So the ceiling is exact: nonlinearity can never exceed it. That is why step 2 found nothing.

## Scope pitfalls for the empirical use
1. **Dependent pair sources.** If Sᵢⱼ and Sᵢₖ are dependent, (a) and (b) fail. In DAG terms that dependence *is* a latent reaching ≥ 3 sites, so V_G > 0 reads as "pair sources not independent or a ≥3-site cause". Say so explicitly.
2. **Per-site transforms g(yᵢ):** preserved, including non-monotone and random-with-local-noise transforms (Kela et al. §VIII, local-operations monotonicity). **Residualising on ΔT** tests a different null, and the theorem covers that null directly: "εᵢ = yᵢ − bᵢΔTᵢ is pairwise-only". So the Poland +4.46 does mean that a ≥3-site cause remains beyond linear ΔT. There are two gaps. (i) The estimated b̂ adds a shared term (b̂ᵢ−bᵢ)ΔTᵢ of order 1/√n, which is small next to +4.46. (ii) A nonlinear ΔT effect survives linear adjustment (already noted).
3. **Years as samples.** The theorem is about one joint law. Under strict stationarity plus ergodicity, the sample correlation converges to it, and serial dependence affects only the inference (block bootstrap is right). **Under nonstationarity**, the pooled correlation is the correlation of a mixture over the year index τ. Then τ is a latent shared by *all* sites (trends, regime shifts, drifting variances), and it alone can force V_G > 0. Detrending removes only the linear part of this.
4. **Measurement error.** Independent per-site error is local noise: it is preserved and only attenuates. Error correlated across sites (shared protocol, a common lab or observer, a calibration drift) is a ≥3-site common cause and is flagged as one. That is consistent with the note's candidate list.
5. **Small-sample upward bias (not in the note).** ρ(|R̂−I|) is biased upward because |·| rectifies noise. Simulated values at k = 10, n = 53:
   - Independent sites: mean V̂_G = +0.05, 95th percentile +0.25.
   - Pairwise world exactly on the boundary (population V_G = 0): mean +0.35, 95th percentile **+0.71**.
   - That +0.71 is for an equal-load boundary world. Independent sites shift by about +1.05 from population (−1 → +0.05), so sparser boundary worlds may run near +1.
   - So sample V̂_G > 0 is not evidence by itself. The moving-block bootstrap lower bound does not correct this bias. Poland's +4.95 / +4.46 is far above +0.71, so **the conclusion stands**, but report the null-boundary calibration.

## Prior art: OWNED
- **Kela, von Prillwitz, Åberg, Chaves & Gross, "Semidefinite tests for latent causal structures"**, IEEE Trans. Inf. Theory 66(1):339–350 (2020), doi:10.1109/TIT.2019.2935755; arXiv:1701.00652. Read in full text (arXiv v1, §§II–IV, VII–VIII). arXiv has only v1 (2017). The numbering below is v1's; the IEEE numbering is unchecked.
  - **Proposition 1:** for any bipartite DAG (independent latents → observables) and any feature maps, "Cov(Y) = R + Σₙ Cₙ, R ≥ 0, Cₙ ≥ 0" (eq. 16). Here R is block-diagonal and Cₙ is supported on ch(Lₙ). Lemma 1 proves it by iterated total covariance, which is the same mechanism as (a) and (b).
  - Fig. 3 is precisely the triangle with pair sources.
  - **Reduction:** take scalar features yᵢ, sources = pairs, and correlation scaling. Then Cᵢⱼ = [[tᵢⱼ, rᵢⱼ],[rᵢⱼ, tⱼᵢ]] ⪰ 0 ⟺ rᵢⱼ² ≤ tᵢⱼtⱼᵢ, and the unit diagonal minus R gives Σⱼ tᵢⱼ ≤ 1. **This is exactly the claim.**
  - Proposition 2 gives the converse (realisability).
  - §VIII gives monotonicity under local operations (pitfall 2).
  - The explicit "|r| ≤ ½" for the triangle was not found in the paper; it is a one-line instance.
- **Matrix side (owned):** "R = diagonal + Σ PSD 2×2-supported" means R has **factor width ≤ 2**. Boman, Chen, Parekh & Toledo, LAA 405 (2005) 239–248, Thm 9 (from secondary sources, not read): factor width ≤ 2 ⟺ symmetric H-matrix with nonnegative diagonal. For unit diagonal this is ρ(|R−I|) ≤ 1, matching the closed form. The boundary convention (singular H) is unchecked.
- **Same test applied to networks:** Åberg, Nery, Duarte & Chaves, "Semidefinite tests for quantum network topologies", PRL 125 (2020), arXiv:2002.05801. Also Tavakoli et al. review, arXiv:2104.10700.
- Steudel–Ay (Entropy 17, 2015) is an entropic analogue (cited as [29] in Kela et al.), not the covariance result.
- **Nothing in the pairwise-world bound is novel.** The closed form for V_G is a routine consequence of owned facts.
- Not searched: bi-factor/edge-factor models, Gisin-type inequalities, trek separation. The OWNED verdict does not depend on them.
- Kela et al. is not on the shelf (`SHELF_INDEX.json` has only Fritz–Chaves 2013).

## How the note should cite it
Replace "very likely … unread" with: *"The ceiling is the pairwise-source case of Kela et al. (2020), Prop. 1 (arXiv v1 numbering): covariance = block-diagonal + PSD parts supported on each source's children. For pair sources this is factor width ≤ 2 (Boman et al. 2005), i.e. V_G = ρ(|R−I|) − 1. Our hand proof re-derives it. Not claimed."* Add the r = 0 fix, the closed form, and the null-boundary calibration (pitfall 5). State pitfalls 2 and 3 as the scope of the Poland result.
