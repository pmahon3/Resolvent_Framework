# Characterising Missing Auxiliary Information from κ_Q

**Status: PARKED (2026-05-27).** Phase 2 audit failed. The core
question — can properties of κ_Q alone characterise the *type* of
auxiliary Z that would reduce R*(Q)? — sits in a genuine logical gap
(non-identifiability of existence ≠ non-constrainability of structure),
but every direction to fill the gap either reduces to known mathematics
or requires model-dependent structural assumptions that kill the
claimed advantage over abductive methods (SDR, ICA, causal discovery).
Shah-Peters (2020) impossibility for conditional independence testing
provides the hard upper bound: without structural assumptions on the
joint law, no model-free deductive diagnostic can work.

---

## Why it fails

### The model-dependence trap

To say "Z must have property P" requires specifying how Z enters
(mixture, covariate shift, confounding). Each mechanism defines a
different constraint class. Without fixing the mechanism, "structure
of Z" is vacuous. Restricting to a specific mechanism (to make the
question well-posed) collapses the advantage over abduction — you're
back to SDR/ICA within a parametric model.

### Direction-by-direction disposal

**Direction 1 (shape variation across fibers):**
Already done abductively by Deb, Saha, Guntuboyina & Sen (JASA 2022,
"Two-Component Mixture Model in the Presence of Covariates") —
covariate-dependent π*(x) estimation. Also BifurcatoR (Madaj et al.,
bioRxiv 2025) packages variance heterogeneity as a latent-structure
diagnostic. The estimation step exists; the deductive step (derive
Z-constraints from shape variation) encounters the identifiability
obstruction: large V(κ_Q) is consistent with latent Z, intrinsic
heteroskedasticity, or model misspecification.

**Direction 2 (conditional characteristic function regularity):**
Fiber-by-fiber non-Gaussianity testing is strictly richer than
pooled ICA, but the *deductive* step (deriving Z-constraints from
regularity patterns) is not in the literature and requires structural
assumptions to be non-vacuous. Cai et al. (AAAI 2024) on higher-order
cumulants for latent confounders works from observed data, not from
κ_Q as a functional object.

**Direction 3 (information geometry):**
The parametric version is fully covered: Louis (1982) gives
I_obs = I_complete − I_missing (matrix decomposition of what's
missing), Amari (1982, 2001) gives it geometric meaning via
e/m-projections. But both presuppose a parametric model where the
latent structure is already specified. The model-free version (derive
constraints from Fisher geometry of {κ_Q(·|q)} without specifying
the latent model) is open but encounters Attack 1 — to interpret
curvature reduction, you need a model for how Z enters.

**Direction 4 (disintegration tower):**
The tower μ = ∫∫ κ_{Q'}(·|q') dν'(q'|q) dν(q) gives an integral
equation with two unknowns (κ_{Q'} and ν'). This is the same
deconvolution non-uniqueness that constitutes the identifiability
obstruction, restated one tower level up. Kullback, Keegel & Kullback
(1987) quantifies information loss magnitude to a sub-σ-algebra but
not structural type. Does not add to Rao-Blackwell's monotonicity
(any strict refinement reduces risk unless Q is already sufficient).

### The P1 motivation is post hoc

P1 found hour_of_week by the *abductive method* (pre-specify 5 axes,
test each). The signal was visible in κ_Q's residuals only because
someone stratified by the right variable. "There to be read" ≠
"extractable without the key." The P1 result supports the abductive
method this seed tries to replace.

### The impossibility boundary

Shah & Peters (Ann. Statist. 2020): without structural assumptions on
(X,Y,Z), there is no conditional independence test controlling Type I
error and consistent against all alternatives. Corollary: any
characterisation of Z from κ_Q requires structural assumptions beyond
κ_Q itself. The model-free deductive programme is blocked.

---

## What survives (marginal)

A sharp impossibility theorem — "no functional T of κ_Q constrains
σ(Z) without structural assumption S; here is precisely what S must
provide" — would sharpen existing formulations (Bergna et al. 2026,
Heckman-Singer 1984) into a functional-analytic statement. This is
likely a reformulation rather than a new result. If pursued, it would
be a separate seed, not a continuation of this one.

---

## Key references found in audit

- Deb, Saha, Guntuboyina & Sen (JASA 2022) — covariate-dependent mixture fraction
- Shah & Peters (Ann. Statist. 2020) — CI testing impossibility
- Louis (JRSSB 1982) — I_obs = I_complete − I_missing
- Amari (Ann. Statist. 1982; 2001) — information geometry of EM
- Kullback, Keegel & Kullback (LNS 1987) — discrimination information in sub-σ-algebras
- Cai et al. (AAAI 2024) — higher-order cumulants for latent confounders
- Cinelli & Hazlett (JRSSB 2020) — sensitivity to omitted variable bias
- Torgersen (1991) — comparison of statistical experiments
- Raju, Machta & Sethna (Phys. Rev. E 2018) — information loss under coarse-graining
- BifurcatoR (Madaj et al., bioRxiv 2025) — variance heterogeneity diagnostic

---

## Parent chain

- `disintegration_diagnostic.md` (parked — identifiability obstruction)
- MITACS P1, S11 (empirical; hour_of_week found abductively)
- This note is a rescue attempt for the parent. The rescue fails.
