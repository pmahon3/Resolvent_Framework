# Paper III Outline (revised: honest framing)

## Working title

"Noise Thresholds for Jacobian-Based Embedding Criteria and a
Residual-Whiteness Alternative"

## One-sentence summary

Jacobian-based embedding criteria (including Lyapunov convergence)
have a sharp noise threshold above which they lose all diagnostic
value; residual autocorrelation convergence with embedding
dimension provides a noise-robust alternative for both dimension
and lag selection.

## Core idea

Embedding parameter selection (dimension d, lag L) relies on
diagnostics that implicitly assume the data is clean and
deterministic.  FNN, Jacobian-trace convergence, and prediction-
error minimization all degrade above a noise threshold.  We:

1. Characterize this threshold empirically (~2-5% noise-to-signal
   for Lorenz, confirmed on Rössler)
2. Propose residual autocorrelation convergence with d (and
   U-shaped minimum with L) as an alternative that works across
   the threshold
3. Explain the threshold via a modelling-commitment framework:
   deterministic criteria test for properties that noise destroys;
   residual-based criteria test for properties that survive noise

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

## What's new (honest assessment)

1. **The noise threshold itself.** Nobody has characterized the
   sharp transition where Jacobian-based criteria lose all
   information.  The phase diagram (noise × dimension) is a new
   empirical result.

2. **Residual acf convergence as an embedding criterion.**  Using
   the decrease of residual autocorrelation with d to identify
   sufficient embedding dimension — and the U-shaped minimum with
   L to identify optimal lag — is a new application.  The acf
   itself is standard (Ljung-Box 1978); the application to
   embedding selection is not.

3. **The explanation via modelling commitment.**  Why the threshold
   exists (deterministic criteria assume single-valued dynamics,
   noise violates this) and why residual criteria survive (they
   assume stochastic dynamics, noise is built in).

## What's NOT new

- Residual autocorrelation as a model diagnostic (Ljung-Box 1978)
- Jacobian estimation from time series (Sano-Sawada 1985)
- Local prediction error for embedding selection (Ragwitz-Kantz 2002)
- Lyapunov convergence to validate embedding (standard practice)
- The reverse application (using Lyapunov convergence as embedding
  criterion) is the contrapositive of standard practice — a
  reframing, not a discovery

## Structure

### §1. Introduction

Embedding parameter selection is a central practical problem in
nonlinear time series analysis.  Standard criteria (FNN, mutual
information, Lyapunov convergence, prediction error) work well for
clean data but degrade under observational noise.  We characterize
this degradation, identify a noise threshold, and propose a
residual-based alternative that is robust across the threshold.

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

- The noise threshold is explained by modelling commitment:
  deterministic criteria test for single-valuedness of the
  dynamics, which noise destroys; residual criteria test for
  absence of deterministic structure in the residuals, which
  survives noise
- Connection to FNN: FNN is a deterministic criterion (tests for
  non-injectivity); expected to fail above the same threshold
- Connection to Ragwitz-Kantz: their prediction-error criterion
  is residual-based and should be noise-robust; our acf criterion
  is a complementary residual diagnostic
- Connection to Papers I+II (brief): the algebraic underdetermination
  of reconstruction means embedding selection is necessarily
  empirical — no algebraic criterion can determine d and L.  The
  commitment framework explains why different empirical criteria
  have different operating regimes.
- Open: adaptive bandwidth selection; extending to multivariate
  observables; comparison with FNN degradation under noise

## Key results (confirmed experimentally)

1. Sharp noise threshold at ~2-5% for Jacobian-based criteria (Lorenz)
2. Residual acf convergence identifies sufficient d under 5-20% noise
3. Residual acf U-shaped minimum identifies optimal L under 5% noise
4. Both patterns validated on Rössler (different attractor topology)
5. Phase diagram showing operating regimes of both criteria

## Relation to Paper I+II (brief, in discussion)

Papers I+II establish that the reconstruction problem is
algebraically underdetermined: the observation algebra doesn't
constrain the choice of realization.  Embedding selection is
therefore necessarily empirical.  The noise threshold we identify
is a practical manifestation of this underdetermination: different
empirical criteria have different operating regimes because they
implicitly assume different model classes for the reconstructed
dynamics.

## Target venue

Chaos (AIP) or Physical Review E — applied nonlinear dynamics,
10-15 pages with figures.

## Estimated effort

- Experiment C (stochastic diagnostic): ~3-4 days
- Experiments D-F: ~1 week
- Writing: ~1 week
- Total: ~3 weeks from Experiment C result
