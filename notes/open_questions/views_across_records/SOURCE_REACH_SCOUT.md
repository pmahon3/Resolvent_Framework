# Minimum source reach m: scout (owners, method, feasibility)

reviewed: false. 2026-11-05. Scout: Kela PDF read (Prop 1, Prop 3, Sec XI); web searches were snippet-level only. "Not read" means exactly that.

## 1. Owned-region table

| Region | Owner | Read level |
|---|---|---|
| Cov = R + Σ_n C_n, R ⪰ 0 block-diagonal, C_n ⪰ 0 supported on children of latent n (general bipartite DAG, vector-valued features) | Kela, von Prillwitz, Åberg, Chaves, Gross, IEEE TIT 66 (2020), Prop. 1 | PDF read |
| Dual SDP gives a witness X* (tr X·Cov ≥ 0 on the compatible set); one-sided test on tr X Cov(Y) ≤ 0; sample splitting to choose X* | Kela et al., Sec. XI and Fig. 4 | read; **stated as speculation, "details left to future work"** |
| Degree-≤d relaxation: Φ(Cov) ⪰ 0, a necessary condition only | Kela et al. Prop. 3 (from v Prillwitz thesis Thm 4.1) | read |
| m = 2 (pair sources): factor width ≤ 2 = H-matrix, V_G = ρ(\|R−I\|) − 1 | Boman–Chen–Parekh–Toledo LAA 405 (2005) Thm 9; Kela Prop 1 | secondary only (per COVARIANCE_CEILING_CHECK.md) |
| Cone of "sums of PSD matrices on m×m principal blocks" = factor-width-≤m cone FW_m; nested, closed, convex; FW_2 = SDD-scaled (SOCP-representable); m ≥ 3 needs SDP | Boman et al. 2005; Ahmadi–Majumdar (DSOS/SDSOS, arXiv:1706.02586) | snippets |
| Entropic analogue for sources of size > c | Steudel–Ay, Entropy 17 (2015); Fritz 2012; Wolfe–Spekkens–Fritz inflation | not re-read; Steudel–Ay has zero power in the repo's own sims (CEILING_POWER_STATS.md) |
| "Genuine network k-partite" (cannot be made from k-partite sources + local maps) | Navascués–Wolfe–Rosset–Pozas-Kerstjens, GNME, arXiv:2002.02773; Contreras-Tejada–Palazuelos–de Vicente arXiv:2004.01722; arXiv:2105.09380 (N-partite resources) | abstract only. Quantum/probabilistic witnesses, not covariance, not estimation |
| Sparse + low-rank latent graphical models (Chandrasekaran–Parrilo–Willsky 2012) | CPW, arXiv:1008.1290 | snippets. Counts the number of latents (rank), **not their reach** |
| Ecology: scale/extent of synchrony drivers | Bjørnstad–Ims–Lambin 1999; Sheppard et al. 2016; Walter et al. 2017 (wavelet synchrony, `wsyn`) | not read here (see SYNCHRONY_CAUSALITY_METHOD_AUDIT.md) |

## 2. Closest exact statement (Kela Prop. 1)
For a bipartite DAG with latents L_1..L_N and features Y_m into V_m: Cov(Y) = R + Σ_n C_n, R ⪰ 0, C_n ⪰ 0, P^(n) C_n P^(n) = C_n, R = Σ_m P_m R P_m. Direction: **model ⟹ decomposition** (necessary). It is not a converse for arbitrary distributions. For linear-Gaussian models with loading blocks the decomposition is also sufficient (my observation, easy; ⟦HAND⟧ not checked in text). Kela never says "factor width" and never treats minimum reach as a quantity. The degree-d case enters only through the weaker Prop. 3 relaxation. Taking all subsets of size ≤ m as candidate supports is the natural reading of the question and appears in none of the sources I found.

## 3. Established method for minimum reach? NOT FOUND
No estimator or test of "maximal source size" or "order of latent confounding" was found. Candidates searched: latent tree learning (Anandkumar, Choi: tree structure assumed), CPW (rank, not reach), Evans mDAGs (graph-level, not estimation), edge clique cover (counts latents for a given dependence graph; with PSD weights it is not the right object because many overlapping sources can mimic a bigger one). Recipe below is therefore a composition of owned parts, not an established procedure.

## 4. Recipe (proposal; not validated)
Define on the correlation matrix R̂ (unit diagonal; diagonal D absorbs scaling):

V_m(R) = min{ t : R + tI ∈ FW_m }.

- m = 2 gives ρ(\|R−I\|) − 1 (checked against the closed form: H-matrix iff 1+t > ρ). m = k gives −λ_min(R).
- Dual (my derivation, ⟦HAND⟧; check numerically at m = 2 and m = k): V_m(R) = − min{ ⟨X,R⟩ : tr X = 1, every m×m principal submatrix of X ⪰ 0 }. Slater holds (X = I/k; large t), so strong duality.
- Minimum reach m̂ = smallest m with V_m ≤ 0 (V_m nonincreasing in m, since FW_m grows).
- Decide by a test of H0(m): V_m ≤ 0, sequentially from m = 2 upward; each step tests the next level up (fixed-sequence, no multiplicity adjustment needed). Confidence statement: "reach ≥ m+1 is needed" is the rejection of H0(m).
- Alternative linear route (Kela Sec. XI): fix a witness X* from a split sample, then test ⟨X*,R⟩ ≥ 0 with a linear-statistic CI. Valid at level α for the pre-chosen X*; conservative.

## 5. Inference caveats
- V_m is convex and finite everywhere, hence Lipschitz and Hadamard directionally differentiable. By Danskin, V_m'(R;h) = max over the optimal dual set of (−⟨X,h⟩). Fang–Santos (2019) then applies: numerical delta method (Hong–Li 2018) with step ε. **The derivative is linear only when the dual optimum is unique.** At the null boundary V_m = 0 (the case that matters) it is typically a max over a face, so the bootstrap must use the directional derivative (as for m = 2).
- Hong–Li ε = ∞ was validated for m = 2 only. Re-validate for each m (null boundary calibration, weak dependence, n = 30–100). Sample size n ≈ 50 with k = 10 has 45 correlations; power for m ≥ 3 vs m = 2 will be low (cf. "low power for weak factors" in run 4).
- Block bootstrap / temporal dependence handled as in the m = 2 pipeline; the nuisance is the same. Nothing new proved here.
- Model scope: the test is on second moments only. It rejects "all sources ≤ m" only if the sources act linearly or the covariance is the only constraint. Nonlinear sources can mimic a larger-reach covariance only in the direction of fewer rejections (decomposition is necessary, so rejection is valid for any structural model with independent sources of reach ≤ m). The "independent sources" assumption is essential.
- Lag/nonstationary common drivers (Moran effect through weather with spatial gradient) look like a global source; "reach k" is not the same as "a physical driver spanning the region".

## 6. Computation (k = 10)
Primal blocks: C(10,m) blocks of m×m. m=2: 45 (SOCP or closed form); m=3: 120×3×3; m=5: 252×5×5 (about 3.8k scalar vars); m=9: 10×9×9. All small for SCS/Clarabel (seconds). Dual form: one 10×10 matrix X plus C(10,m) m×m PSD constraints. **k = 20, m = 10 gives 184,756 blocks**: needs cutting planes on the dual (lazy principal-submatrix constraints) or restriction of candidate supports. Environment check: scipy 1.13.1 present; **cvxpy, scs, clarabel not installed** (`pip install cvxpy` brings SCS, Clarabel and OSQP). Memory trivial at k = 10, far below the 2 GB cap. A bootstrap needs B × (number of m levels) solves; with warm starts fine.

## 7. Not found / unresolved
- Any statistical test of factor-width membership. Any ecological test of "driver spans all sites vs regional subsets" built on a covariance cone (Walter 2017 clusters synchrony networks, not tested against a reach null; not read).
- Whether FW_m membership has polynomial algorithm beyond SDP (Boman et al. asked; later "factor width rank" arXiv:2405.11556 not read).
- GNME paper (2002.02773) witness construction, Gisin 2020 and the multipartite-depth literature were not read beyond abstracts; a covariance-level analogue may exist there.
- Next owed: (i) numerical check of the dual formula; (ii) read Boman Thm 9 and Kela Sec. XI statement against the repo's m = 2 note; (iii) one pass on "factor width" in statistics/signal processing citations.

## Formal check (main session, 2026-11-05; ⟦HAND⟧ by me, so not independent; numerics via `verification/source_reach.py`)
- H₀(m) "every latent touches ≤ m sites" (covariance version) ⟺ R ∈ FW_m, since diagonal noise terms are 1×1 pieces. V_m ≤ 0 ⟺ H₀(m)
  (if R + tI ∈ FW_m with t ≤ 0, then R = (R + tI) + |t|I ∈ FW_m).
- m = 2: FW₂ = scaled diagonally dominant ⟺ the comparison matrix (1 + t)I − |R − I| is PSD ⟺ V₂ = ρ(|R − I|) − 1 (standard SDD/H-matrix fact).
- m = k: FW_k = PSD, so V_k = −λ_min(R).
- Dual: FW_m* = {X : every m×m principal submatrix PSD}. V_m = max_{X ∈ FW_m*, tr X = 1} −⟨X, R⟩ is convex.
- **ε = ∞ (recession) statistic for inference:** lim_{ε→∞} V_m(R̂ + εZ)/ε = max_X −⟨X, Z⟩ = V_m(I + Z) + 1. For m = 2 this is ρ(|Z|),
  the validated statistic.
- **Numerics (15 random R, k = 4–6):**
  - |primal − dual| ≤ 4×10⁻⁸;
  - |V₂ − (ρ − 1)| ≤ 7×10⁻⁹;
  - |V_k + λ_min| ≤ 1×10⁻⁸;
  - V_m non-increasing in m;
  - equal triangle r = 0.6: V₂ = +0.2, V₃ = −0.4.
  - Timing for k = 10: 0.1–0.25 s per solve.

## Poland minimum-reach run (declared before running)
10 Polish beech sites, 53 years, prep = normal scores plus linear detrend (as validated). For m = 2…9:
- T_m = √n·V_m(R̂).
- Moving-block bootstrap (b = round(n^{1/3}), no wrap, 1000 resamples, full prep inside). Z* = √n(R̂* − R̂). D*_m = V_m(I + Z*) + 1.
- Reject H₀(m) if T_m > the 95% point of D*_m.
- **m̂\* = the smallest m not rejected. It is a lower bound on the true minimum reach,** since power falls with m.
- Inference is validated only for m = 2. For m ≥ 3 the ε = ∞ bracket is justified by theory (convexity), not by our simulations: **provisional**.
- Within one programme, so a shared protocol also has full reach.
- Prediction: H₀(2) rejected (known), and m̂\* = 3 or 4, because power is low.

### Poland minimum-reach result (2026-11-05): m̂\* = 4 (prediction held). Script `verification/source_reach_poland.py` (7 min)
| m | V_m | T = √n V_m | 95% crit | H₀(m) "every latent ≤ m sites" |
|---|---|---|---|---|
| 2 | +4.79 | 34.9 | 8.65 | rejected |
| 3 | +1.90 | 13.8 | 7.65 | **rejected** |
| 4 | +0.93 | 6.8 | 7.65 | not rejected |
| 5 | +0.45 | 3.3 | 7.65 | not rejected |
| 6 | +0.16 | 1.2 | 7.65 | not rejected |
| 7–9 | −0.03 … −0.09 | < 0 | 7.65 | not rejected |
- **Demonstrated:** Polish beech synchrony needs a hidden cause reaching **at least 4 of the 10 stands** (H₀(3) rejected, T = 13.8 against 7.65).
  This is provisional for m ≥ 3 (inference not simulation-validated there).
- **Suggested, not demonstrated:** the point estimates stay positive to m = 6 and cross 0 at m = 7, i.e. a reach of about 7. Point V_m is
  biased upward, so this is an upper-side hint only.
- A shared protocol has full reach (10), so it remains a live explanation. The reach result does not separate it from regional weather.
