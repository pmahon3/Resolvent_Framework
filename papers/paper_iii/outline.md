# Paper III Outline (revised: commitment-indexed diagnostics)

## Working title

"Commitment-Indexed Diagnostics for Delay-Reconstructed
Dynamical Systems"

## One-sentence summary

The appropriate diagnostic for a delay reconstruction depends on
the modelling commitment: deterministic embeddings require
Jacobian-trace convergence, stochastic embeddings require residual
whiteness, and mismatching commitment to diagnostic produces
unreliable assessments.

## Core idea

The delay reconstruction problem is algebraically underdetermined
(Paper I): the observation algebra doesn't determine the
realization.  Practitioners navigate this underdetermination by
making a modelling commitment — an assumption about the structure
of the reconstructed dynamics.  Each commitment has a natural
diagnostic; applying the wrong diagnostic (commitment mismatch)
gives misleading results.

This is not one diagnostic but a taxonomy:

| Commitment | Assumes | Natural diagnostic |
|---|---|---|
| Deterministic embedding | z_{t+1} = F(z_t) | Jacobian-trace convergence with d |
| Stochastic embedding | z_{t+1} = F(z) + σ(z)η | Residual whiteness + σ uniformity |
| Measure-preserving | det(A) = 1 | Volume conservation test |

Matching commitment to diagnostic is the practitioner's art.
The framework makes this explicit.

## Antecedents

- **Casdagli (1991):** deterministic-vs-stochastic continuum via
  prediction error as function of smoothing parameter.  The
  philosophical ancestor of commitment-indexed analysis.
- **Ragwitz-Kantz (2002):** local prediction error minimized
  over (d,τ) for stochastic/Markov embedding selection.  Closest
  existing work — one commitment, one diagnostic.
- **Theiler et al. (1992):** surrogate methods.  Template for
  commitment/diagnostic pairs: null hypothesis (linear stochastic)
  defines the commitment; discriminating statistic is diagnostic.
- **Sano-Sawada (1985):** Jacobian estimation for Lyapunov exponents.
  Uses Jacobian after embedding — we use it to assess embedding.

## What's new

1. **Systematic taxonomy** of commitments and their natural
   diagnostics (deterministic → tr(A), stochastic → whiteness).
   Nobody has formalized this.

2. **Jacobian trace as embedding diagnostic** (not just dynamical
   invariant).  tr(A) convergence with d determines sufficient
   embedding for deterministic data.

3. **Demonstration that commitment mismatch degrades diagnostics.**
   Applying the deterministic diagnostic (div) to stochastic data
   gives garbage — explained by the framework.

4. **The stochastic diagnostic (residual whiteness) works where
   the deterministic one fails** — and vice versa for clean data.

## Structure

### §1. Introduction

The reconstruction problem is underdetermined (cite Papers I+II).
Practitioners choose embedding parameters (d, L) via heuristic
criteria (FNN, mutual information, prediction error).  These
criteria implicitly assume a modelling commitment.  We make this
explicit: different commitments require different diagnostics.

### §2. Framework: commitments and diagnostics

**Definition.** A *modelling commitment* C is a class of dynamics
on the reconstructed space: C = {z_{t+1} = G(z_t) : G ∈ F} for
some function class F.

**Definition.** A *diagnostic* for commitment C is a test statistic
whose value indicates whether the data, at embedding (d, L), is
consistent with some G ∈ F.

Three levels:

**Level 1: Deterministic.** F = smooth maps.  The delay map Φ is
an embedding (Takens).  The diagnostic tests whether the local
dynamics are well-defined (single-valued):
  - Jacobian trace tr(A(z)) averaged over the attractor
  - Convergence of ⟨tr(A)⟩ with d indicates sufficient embedding
  - Rationale: if Φ is injective, the dynamics are single-valued,
    and the Jacobian is well-defined; instability of tr(A) with d
    signals non-injectivity

**Level 2: Stochastic.** F = drift + diffusion (Langevin).  The
delay map need not be injective — noise captures the multi-
valuedness.  The diagnostic tests whether the residuals are
structurally noise:
  - Residual autocorrelation: ε_t should be uncorrelated
  - Spatial uniformity of σ(z): σ shouldn't depend on position
    (or if it does, it should be smooth, not erratic)
  - Normality: ε_t ~ N(0, Σ) locally
  - Rationale: if the Langevin model captures all deterministic
    structure, the residual IS noise

**Level 3: Measure-preserving.** F = volume-preserving maps
(Hamiltonian dynamics).  Additional constraint: det(A) = 1.
  - Diagnostic: |det(A) - 1| averaged over the attractor
  - Convergence with d indicates sufficient embedding + volume
    preservation

### §3. Algorithm

For each commitment level, the pipeline is:

1. Delay embed y → Z at (d, L)
2. Build KDTree on Z
3. At query points, fit local linear model (tricube WLS)
4. Extract A(z), b(z), residuals ε(z)
5. Compute commitment-specific diagnostic:
   - Deterministic: tr(A) convergence with d
   - Stochastic: residual whiteness (Ljung-Box on ε, spatial σ)
   - Volume-preserving: det(A) ≈ 1

### §4. Experiments

**Experiment A: Commitment match (deterministic data, deterministic diagnostic).**
Lorenz-63, clean. tr(A) converges with d. Diagnostic works. [DONE]

**Experiment B: Commitment mismatch (stochastic data, deterministic diagnostic).**
Lorenz + noise. tr(A) does NOT converge — diagnostic fails. [DONE]
The framework explains: you applied the wrong diagnostic.

**Experiment C: Commitment match (stochastic data, stochastic diagnostic).**
Lorenz + noise. Apply residual whiteness test.  Does it correctly
identify sufficient d where tr(A) failed?  [TO DO — key experiment]

**Experiment D: Bandwidth dependence explained.**
tr(A) depends on h because the local linear approximation is
scale-dependent.  At commitment Level 1, this is a nuisance
parameter.  At Level 2, h is part of the model (kernel regression
bandwidth).  The framework explains why h matters differently at
each level.  [TO DO]

**Experiment E: Rössler (different topology).**
Same taxonomy, different attractor.  Validates generality.  [TO DO]

**Experiment F: Logistic map (discrete, stochastic).**
Position-dependent σ(x).  Level 2 diagnostic should detect it.
[TO DO]

### §5. Discussion

- The art of reconstruction is navigating the underdetermined
  descent from St(C) to Ω (Papers I+II)
- The commitment determines which aspects of the descent you're
  testing
- Mismatching commitment to diagnostic is a category error —
  not a failure of the diagnostic itself
- Connection to surrogate methods (Theiler): one instance of the
  general taxonomy
- Connection to Ragwitz-Kantz: their prediction-error criterion
  is Level 2 (stochastic commitment)
- Connection to FNN: Level 1 (deterministic commitment — tests
  for non-injectivity)
- Open: formalizing the commitment/diagnostic mapping categorically
  (Fritz's Markov categories may be the right language)

## Key experimental question

**Experiment C is the make-or-break.** If the residual whiteness
diagnostic correctly identifies sufficient d for noisy Lorenz
where tr(A) failed, the paper has its punchline: commitment match
succeeds where mismatch fails.

If Experiment C also fails, the paper is weaker — it explains
failure (diagnostic mismatch) but doesn't prescribe success.

## Relation to Paper I+II

- Paper I: descent requires σ-additivity; the algebra doesn't
  constrain Ω → the reconstruction is underdetermined
- Paper II: distributivity controls which realism positions are
  available → different commitments have different scope
- Paper III: different commitments require different diagnostics →
  the art has structure

This is the "colour theory" paper: it doesn't tell you what to
paint, but it tells you which pigments work with which medium.

## Target venue

Chaos (AIP) or Physical Review E — applied nonlinear dynamics,
10-15 pages with figures.

## Estimated effort

- Experiment C (stochastic diagnostic): ~3-4 days
- Experiments D-F: ~1 week
- Writing: ~1 week
- Total: ~3 weeks from Experiment C result
