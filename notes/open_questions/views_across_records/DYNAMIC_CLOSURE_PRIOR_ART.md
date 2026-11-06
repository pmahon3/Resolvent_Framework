# Dynamic closure: prior art (hostile, cross-field)

reviewed: false. 2026-11-06. Checks `DYNAMIC_CLOSURE.md`. Shelf grep (`SHELF_INDEX.json`): no hits on trek, Sullivant–Talaska–Draisma, Eichler,
Lütkepohl, Moran, Lande, Ripa, Kendall, Bjørnstad, Liebhold, Diebold, Forbes, Malinsky, Swanson. Shelf hit: Sullivant 2006, which is unrelated.
Read levels: **PDF** = text read here; **snip** = abstract or search snippet; **mem** = from memory, not checked.

## (a) The closure proposition: **OWNED (routine corollary)**
- **Identity.** S = Σ_k Bᵏ Q Bᵏᵀ is the discrete Lyapunov (Stein) solution, S = BSBᵀ + Q. Textbook for stable VAR(1): Lütkepohl, *New Introduction to Multiple Time
  Series Analysis* (2005) §2.1 [mem].
- **Support claim.** Each term Bᵏ C_S Bᵏᵀ is PSD and supported on N_k(S)×N_k(S). That is one line, and it is the trek rule (Wright's path tracing). Its graphical forms:
  - Sullivant, Talaska & Draisma, *Ann. Stat.* 38 (2010) [mem] for DAG/SEM covariances (a sum over treks with a common top);
  - Hansen, "A trek rule for the Lyapunov equation", *Algebraic Statistics* 16(2) 2025, arXiv:2407.21223 [snip]: a power series in the drift and volatility, for the
    continuous-time steady state.
  The discrete VAR case is the same expansion on the time-unrolled DAG, where every trek has its top at a shock ε_{t−k} on S. No paper was found stating it
  in FW_H (factor-width) language. The restatement is a translation, not a contribution.
- **The ecological content is owned.** "Level synchrony = shock correlation spread by dispersal, amplified when persistence is high":
  - Lande, Engen & Sæther, *Am. Nat.* 154 (1999) 271–281 [snip]. The synchrony scale combines the environmental-correlation scale with the dispersal scale,
    and dispersal's contribution is magnified by (dispersal rate)/(strength of density regulation). Weakly regulated populations get long-range synchrony from
    short dispersal. This is the note's "small centres + ρ(B) near 1 ⇒ large level reach".
  - Ripa, *Oikos* 89 (2000) 175–187 [snip]. Linearised spatial model. Environmental correlation sets the baseline. Dispersal synchronises effectively only when
    local dynamics are close to unstable.
  - Kendall et al., *Am. Nat.* 155 (2000) 628 [snip]: the two mechanisms interact. Synchrony falls as regulation strengthens.
  - Moran 1953 / Royama 1992 [mem]: identical linear dynamics ⇒ population correlation = noise correlation (Q = S correlation when B = aI).
- **Corrections to the note.**
  1. **The membership statement is vacuous as stated.** H* is a union over all k. If G_B is strongly connected (as in world Lc: ring dispersal d = 0.15), then
     N_k(S) = all sites for k ≥ diam, so FW_{H*} = PSD and the proposition says nothing. The content is **quantitative**: a truncated version, e.g.
     S = (Σ_{k<K} terms ∈ FW_{H*_K}) + tail with ‖tail‖ ≤ ‖Q‖ Σ_{k≥K} ‖Bᵏ‖², hence V_{H*_K}(S) ≤ ‖Q‖ Σ_{k≥K}‖Bᵏ‖² ⟦HAND⟧. The note should state this form.
  2. "Reach-k weight scales like ‖Bᵏ‖²" is an **upper bound**, not a scaling. A large closure reach needs ρ(B) near 1 **or non-normal transient growth**
     (‖Bᵏ‖ ≫ ρ(B)ᵏ). Spectral radius alone does not control it.
  3. Change "likely owned as the time-series trek rule" to "owned: trek rule (Wright; STD 2010; Hansen 2025), ecology: Lande et al. 1999, Ripa 2000".

## (b) Innovations vs levels as a method: **OWNED (standard), with a narrow residue**
- **Econometrics.** Contemporaneous structure lives in the reduced-form residual covariance Σ_u, and dynamics live in the lag matrices. This is the basis of
  structural VAR identification: Lütkepohl 2005 Ch. 9; Kilian & Lütkepohl, *Structural VAR Analysis* (CUP 2017) [mem]. Graph search on the VAR residuals:
  - Swanson & Granger, *JASA* 92 (1997) 357–367 [snip]: PC-type search on residual partial correlations to order contemporaneous causes;
  - Demiralp & Hoover, *Oxf. Bull. Econ. Stat.* 65 (2003) [snip]; Moneta (2008) [mem].
  Factors vs propagation:
  - Stock & Watson (2005), "Implications of dynamic factor models for VAR analysis" [mem];
  - Forni–Hallin–Lippi–Reichlin GDFM (common vs idiosyncratic components) [mem];
  - Krampe & Margaritella, arXiv:2402.02482 [snip]: they split Diebold–Yilmaz connectedness into **common-component shocks** vs **idiosyncratic sparse-VAR
    spillovers**. This is the closest match to "centre in space vs propagation in time".
  - Known caveat: Diebold–Yilmaz generalized FEVD (Pesaran–Shin) counts correlated same-time shocks as "spillover" [snip]. Forbes & Rigobon, *J. Finance*
    57 (2002) [mem] is a heteroskedasticity correction, so it is tangential.
- **Graphical time series / causal discovery.**
  - Eichler (arXiv:math/0610654; AISTATS 2010 dMAGs) [snip]: directed edges = Granger links, undirected/bidirected edges = contemporaneous (innovation)
    dependence, including latent confounding.
  - SVAR-FCI, Malinsky & Spirtes 2018 [mem]; tsFCI, Entner & Hoyer 2010 [mem]; LPCMCI, Gerhardus & Runge 2020 [mem]: contemporaneous latent confounders as
    bidirected same-time edges, separated from lagged effects.
- **Ecology.** MAR(1)/MARSS: x_t = B x_{t−1} + u + w_t, w ~ N(0, Q), with Q read as shared environmental forcing and B as interactions (Ives, Dennis,
  Cottingham & Carpenter, *Ecol. Monogr.* 73 (2003) [mem]). Ward et al., *J. Appl. Ecol.* 47 (2010) 47–56 [PDF, methods]: they compare Q structures
  (diagonal-equal, diagonal-unequal, unconstrained) and subpopulation groupings by AIC, with B diagonal (estimate 0.983), i.e. **no dispersal in B**.
- **Hostile caveats the note omits (owned).**
  1. **Temporal aggregation.** Propagation faster than the sampling interval (annual counts; within-season pollen or weather) shows up as *same-time*
     residual correlation. It looks like a common cause. Breitung & Swanson, *Oxf. Bull. Econ. Stat.* 64 (2002), "Temporal aggregation and spurious
     instantaneous causality" [mem]; Gong et al. ICML 2015, subsampled VAR [mem]. For Poland, "regional same-time driver" therefore also covers
     "within-year propagation".
  2. **Observation error.** Observed = state + noise makes the observed process VARMA. OLS VAR residuals are then not the innovations and keep lagged
     structure. MARSS (state-space) exists for exactly this reason.
  3. **Misspecification of the restricted VAR** (two-neighbour lags, linear) leaves unmodelled propagation in ε̂. It biases toward finding a centre.
- **Residue (looks unowned):** testing a **hypergraph-cone hypothesis** (FW_H: inequality-only, arbitrary-rank blocks) on VAR innovations, with a bootstrap
  that re-fits the VAR. The literature tests rank/factor-number, sparsity of Σ_u, or a finite list of parametric Q by AIC. None tests a reach or
  radius bound. This is the step-2 residue (`HYPERGRAPH_CENTRES_PRIOR_ART.md`, Q4) carried over to innovations. It is a composition, not new theory.

## (c) Ecology's Moran vs dispersal separation: **PARTLY OWNED**
- **Tools:**
  - Synchrony–distance decay compared with environmental correlation–distance (Lande et al. 1999; Bjørnstad, Ims & Lambin, *TREE* 14 (1999) 427 [mem]; Koenig 1999 [mem]).
  - Lagged vs unlagged cross-correlation as a dispersal signature [snip; the source, a field-population study, was not pinned down].
  - Swanson & Johnson, *Oikos* 86 (1999) 265 [snip]: AR fits per population. Dispersal is inferred from negative synchrony–distance plus heterogeneous
    density-dependent structure. Homogeneous structure only *permits* Moran.
  - Ripa 2000 / Ranta et al. 1995–97 [mem] for the interaction.
  - Wavelet Moran attribution to *measured* drivers: Sheppard et al., *Nat. Clim. Change* 6 (2016) [mem]; Walter et al. 2017 (already on file).
  - MARSS Q hypotheses (Ward et al. 2010).
  - Reviews: Liebhold, Koenig & Bjørnstad, *Annu. Rev. Ecol. Evol. Syst.* 35 (2004) 467 [mem].
- **Do they test a common-cause *requirement*?** **NOT FOUND.** Ecology attributes synchrony by comparing model fits (AIC), matching distance profiles, or
  regressing on measured drivers. No paper was found that tests, model-free, that **no** configuration of local/pairwise shocks plus local dispersal can
  produce the observed same-time correlation. The repo's reach and radius tests on innovations sit in that gap. The gap is a matter of method framing: the
  mechanisms themselves are owned.

## Bearing on the question (WHY.md)
Composition, not circle: separating a centre in space (common shock) from a centre in time (propagation) is classical in ecology (Moran vs dispersal) and
in econometrics (common factor vs spillover). The repo's addition is the necessity form ("a centre this wide is *required*"). Hidden idealisation: the
"same-time" reading assumes propagation is slower than the sampling interval.
