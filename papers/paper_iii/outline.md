# Paper III Outline

## Working title

"Divergence-Based Noise Estimation for Delay-Reconstructed
Dynamical Systems"

## One-sentence summary

The divergence of the locally linearized pushforward in a delay
reconstruction estimates the local noise amplitude, providing a
principled diagnostic for embedding quality and a stochastic
extension of the reconstructed dynamics.

## Motivation (from Papers I+II)

The observation algebra determines a measure on the dual space
unconditionally, but descent to a specific realization is
unconstrained (Paper I).  Distributivity makes this freedom total
for classical observations (Paper II).  In practice, delay
embedding is a choice of realization: it selects which observation-
patterns correspond to "states."  The divergence of the local
pushforward detects how much structure is lost or created by this
choice.

## The algorithm

### Input
A scalar time series {y_t}, t = 1, ..., N.

### Step 1: Delay embedding
Form delay vectors:
  x_t = (y_t, y_{t-L}, y_{t-2L}, ..., y_{t-(d-1)L})

for chosen dimension d and lag L.

### Step 2: Local linearization of the pushforward
For each x_t, identify k nearest neighbours in the reconstructed
space (using tricube or other compactly supported kernel for
weighting).  Fit a local linear model:

  x_{t+1} ≈ A(x_t) · x_t + b(x_t)

where A(x_t) ∈ ℝ^{d×d} is the local Jacobian (linearized
pushforward) and b(x_t) is the local intercept.

### Step 3: Divergence of the pushforward
Compute:

  div F(x_t) = tr(A(x_t))

This is the local expansion rate of the pushforward.  For a
measure-preserving system (e.g., Hamiltonian), div F = 0.  For
a dissipative system, div F < 0.  Deviation from the expected
value signals embedding artefacts or genuine stochastic forcing.

### Step 4: Residual noise estimation
Compute residuals:

  ε_t = x_{t+1} - (A(x_t) · x_t + b(x_t))

The local noise amplitude:

  σ²(x_t) = (1/k) Σ_{j ∈ neighbours} |ε_j|²

This gives position-dependent noise: a local diffusion coefficient.

### Step 5: Stochastic model
The output is a local Langevin model:

  x_{t+1} = A(x_t) · x_t + b(x_t) + σ(x_t) · η_t

where η_t ~ N(0, I).  The pair (A(x), σ(x)) fully characterizes
the local stochastic dynamics in the reconstructed space.

### Step 6: Embedding diagnostic
The embedding is "good" when:
- σ(x) is small and spatially uniform (noise is structureless)
- div A(x) matches the expected Lyapunov spectrum
- ε_t shows no autocorrelation or spatial structure

The embedding is "bad" when:
- σ(x) varies strongly with position (signal leaking as noise)
- Residuals have structure (deterministic component missed)
- div A(x) is anomalous (embedding dimension too low)

## Key insight from the algebraic framework

The noise σ(x) is not "measurement error" — it is the local
signature of the underdetermined descent from St(C) to Ω.  When
the embedding dimension is too low, the projection from the "true"
state space onto the reconstructed space collapses distinct states.
The residual divergence measures this collapse rate locally.

A faithful embedding (in the sense of Paper I: μ̂(pure(Ω)) = 1)
has σ(x) → 0 everywhere.  An unfaithful one has σ(x) > 0 in
regions where distinct states are collapsed by the projection.

## Relation to existing work

### Botvinick-Greenhouse et al. (2025)
"Measure-Theoretic Time-Delay Embedding." Lifts Takens to
probability measures via optimal transport (Wasserstein).  Global,
Eulerian (continuity equation).  Doesn't estimate local noise or
use divergence.  **Complementary**: they give the global measure-
theoretic foundation; we give the local diagnostic and model.

### Classical embedding criteria
- FNN (Kennel-Brown-Abarbanel 1992): tests for false neighbours
  caused by low embedding dimension.  Our divergence diagnostic
  generalizes this — FNN detects dimension insufficiency; residual
  structure detects any embedding deficiency.
- Mutual information (Fraser-Swinney 1986): heuristic for lag
  selection.  Our approach provides a residual-based alternative.

### Noise estimation in dynamical systems
- Lalley-Nobel (2006): consistent estimation of noise in dynamical
  systems from time series.
- Kantz-Schreiber (2004): Practical methods, chapter on noise
  reduction.
- Our contribution: noise estimation *as a byproduct* of the
  local linearization, with algebraic interpretation.

### Diffusion estimation
- Lamouroux-Lehnertz (2009): kernel-based diffusion estimation.
- Lade (2009): finite-time Fokker-Planck estimation.
- Our contribution: connects diffusion estimation to embedding
  quality via the divergence diagnostic.

## Numerical experiments

### Experiment 1: Lorenz-63
Known system, d=3, clean data.  Embed from scalar observable
(x-component) at varying d and L.  Show:
- σ(x) → 0 as d → 3 (correct dimension)
- σ(x) remains large for d = 2 (insufficient dimension)
- div A matches known Lyapunov exponents

### Experiment 2: Lorenz-63 + observational noise
Add Gaussian noise to the scalar time series.  Show:
- σ(x) separates into "embedding noise" (reducible by increasing
  d) and "measurement noise" (irreducible floor)
- The irreducible floor estimates the true noise amplitude

### Experiment 3: Rössler system
Different attractor structure.  Test lag selection via residual
analysis — optimal L minimizes structured residuals.

### Experiment 4: Logistic map (discrete, noisy)
Discrete-time system.  Show σ(x) varies with position (high near
the chaotic attractor boundary, low in the interior).

### Experiment 5: Real data (if available)
Climate time series, financial data, or physiological signal.
Apply the full pipeline and compare with classical criteria.

## What's already implemented

From the archived code (`archive/articles/combined/code/`):
- Tricube kernel: w(u) = (1-u³)³ for compact support
- Local linear regression framework
- Langevin dynamics simulation (scalar tier1)
- Locality validation via edge divergence
- Per-bin residual analysis

From the Cantor notebook (`notes/notebooks/`):
- Delay embedding in ℝ³
- Fibre refinement / reconstruction convergence
- Dimension recovery

**Needs:** Extension to multivariate delay vectors, divergence
computation, noise amplitude mapping, comparison with FNN.

## Target venue

- Chaos (AIP) — applied nonlinear dynamics, 10-15 pages
- Physica D — dynamical systems, allows longer papers
- Nonlinear Dynamics — Springer, applied focus

## Dependencies

- Paper I (cited for algebraic underdetermination framing)
- Paper II (cited for distributivity / VDR connection — optional)
- Botvinick-Greenhouse 2025 (cited for measure-theoretic Takens)
- Existing code base (needs extension, not rewrite)

## Estimated effort

- Theory/framing section: 1-2 days (motivation from Papers I+II
  + position relative to BG2025)
- Algorithm implementation: 1-2 weeks (extend existing code to
  multivariate delay embedding + divergence computation)
- Numerical experiments: 2-3 weeks (Lorenz, Rössler, logistic,
  possibly real data)
- Writing: 1 week
- Total: ~4-6 weeks from start

## Open questions

1. **Bandwidth selection for local linearization.** The tricube
   kernel needs a bandwidth parameter h.  How to choose h
   adaptively? Cross-validation? Residual-based?

2. **Divergence vs trace.** Is tr(A) the right divergence, or
   should we use the full Jacobian determinant det(A)?  For
   volume-preserving flows, det(A) = 1 is the constraint.

3. **Connection to Lyapunov exponents.** The eigenvalues of A(x)
   averaged over the attractor should give the Lyapunov spectrum.
   Does our local estimation agree with standard algorithms
   (Benettin et al.)?

4. **Confidence intervals.** How to quantify uncertainty in σ(x)?
   Bootstrap? Asymptotic normality of local linear regression?

5. **Non-scalar observables.** What if you observe a vector?
   The delay embedding dimension changes; the algebraic framework
   (directed system of observation algebras) still applies.
