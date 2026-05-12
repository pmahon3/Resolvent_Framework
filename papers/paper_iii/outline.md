# Paper III Outline (revised after initial experiments)

## Working title

"Divergence Stabilization as an Embedding Diagnostic for
Delay-Reconstructed Dynamical Systems"

## One-sentence summary

The trace of the locally linearized pushforward in a delay
reconstruction converges to the Lyapunov sum as embedding
dimension increases; stabilization indicates sufficient
embedding, providing a diagnostic independent of bandwidth
and robust to local nonlinearity.

## Motivation (from Papers I+II)

The observation algebra determines a measure on the dual space
unconditionally, but descent to a specific realization is
unconstrained (Paper I).  In practice, delay embedding is a
choice of realization.  The divergence of the local pushforward
detects whether this choice is sufficient.

## The algorithm

### Input
A scalar time series {y_t}, t = 1, ..., N.

### Step 1: Delay embedding
Form delay vectors:
  x_t = (y_t, y_{t-L}, y_{t-2L}, ..., y_{t-(d-1)L})

for chosen dimension d and lag L.

### Step 2: Local linearization of the pushforward
For each x_t, identify neighbours within radius h (via KDTree).
Fit a local linear model using tricube-weighted least squares:

  x_{t+1} ≈ A(x_t) · (x_t - x₀) + b(x_t)

where A(x_t) ∈ ℝ^{d×d} is the local Jacobian.

### Step 3: Two diagnostics

**Primary: divergence stabilization.**

  div F(x_t) = tr(A(x_t))

Average over the attractor: ⟨div F⟩ ≈ Σ λᵢ (sum of Lyapunov
exponents).  As embedding dimension d increases, ⟨div F⟩
converges to the true Lyapunov sum.  Stabilization indicates
sufficient embedding.

This diagnostic is:
- Independent of bandwidth h (the Lyapunov sum is intrinsic)
- Robust to local nonlinearity (tr(A) captures the leading
  linear term, which gives the correct Lyapunov contribution)
- Cheaper than FNN (no pairwise distance comparisons)

**Secondary: residual noise amplitude.**

  σ²(x_t) = tr(Σ(x_t)) / d

where Σ is the weighted residual covariance.  σ measures total
residual = nonlinearity + noise + embedding artefacts.  It does
NOT decrease cleanly with d at fixed h because nonlinearity
dominates at coarse bandwidths.

σ becomes informative when combined with div:
- div stable + σ large → genuine noise or nonlinearity
- div unstable + σ large → embedding insufficient
- div stable + σ small → faithful deterministic reconstruction

### Step 4: Stochastic model (when div is stable)
Once sufficient d is identified via div stabilization, the
output is a local Langevin model:

  x_{t+1} = A(x) · x + b(x) + σ(x) · η_t

The pair (A(x), σ(x)) characterizes the local stochastic
dynamics.  σ(x) is now interpretable as genuine noise (not
embedding artefact) because div has stabilized.

## Key insight (revised from experiments)

The original hypothesis was: σ(z) decreases as embedding
dimension increases, and σ → 0 indicates faithful embedding.

The experiments show: **div stabilizes before σ does.**  This is
because σ captures all sources of residual (nonlinearity + noise +
embedding artefacts) while div captures only the volume change,
which converges to the Lyapunov sum once the embedding is
sufficient.

**The divergence is the intrinsic diagnostic; the residual
amplitude is the composite one.**  The paper's contribution shifts
from "noise estimation" to "divergence stabilization as embedding
criterion," with noise estimation as a secondary output once
sufficiency is established.

## Algebraic framing (one paragraph in intro)

From Papers I+II: the reconstruction problem is algebraically
underdetermined — the observation algebra doesn't constrain
realization.  The divergence diagnostic detects whether a
*specific* realization (choice of d, L) has captured the
dynamical content.  Stabilization = the descent from St(C) to Ω
has succeeded; the remaining residual is genuine, not structural.

## Relation to existing work

### Botvinick-Greenhouse et al. (2025)
Global measure-theoretic Takens (Wasserstein/OT).  We give the
local complement: drift + diffusion at each point.  They don't
compute divergence or distinguish embedding noise from genuine
noise.

### Classical embedding criteria
- FNN (Kennel-Brown-Abarbanel 1992): detects dimension
  insufficiency via false neighbours.  Our div diagnostic
  detects it via Lyapunov sum convergence — no pairwise distance
  computation, no threshold parameter.
- Mutual information (Fraser-Swinney 1986): lag selection.
  We can test lag via div stability across L values.
- Cao (1997): practical alternative to FNN.  Our approach is
  related but uses the Jacobian trace rather than nearest-
  neighbour ratios.

### Lyapunov exponent estimation
- Benettin et al. (1980): standard QR-based Lyapunov estimation.
- Sano-Sawada (1985): Jacobian-based estimation from time series.
- Our div computation is closely related to Sano-Sawada but framed
  as an *embedding diagnostic* rather than a dynamical invariant.
  The key difference: we track convergence WITH d, not just
  compute at fixed d.

### Noise estimation
- Lalley-Nobel (2006), Kantz-Schreiber (2004), Lamouroux-Lehnertz
  (2009).  Our σ(x) is a byproduct of the local linear fit;
  the novelty is using div to determine when σ is trustworthy.

## Numerical experiments (revised)

### Experiment 1: Lorenz-63 dimension sweep (DONE — preliminary)
N=50000, L=10, d=2..6, h=3,5,8.
Result: div converges, σ doesn't decrease cleanly.
**Need:** Larger N, finer h grid, comparison with known
Lyapunov sum (-13.66 continuous-time).

### Experiment 2: Bandwidth stability
Fix d=3 (correct for Lorenz).  Sweep h from 1 to 15.
Show: ⟨div⟩ is approximately h-independent while ⟨σ⟩ varies
strongly with h.  This demonstrates div's robustness.

### Experiment 3: Lorenz + observational noise
Add Gaussian noise with amplitude ε = 0.1, 0.5, 1.0 to the
scalar time series.  Show:
- div still converges (robust to moderate noise)
- σ has an irreducible floor (= true noise level)
- At high noise, div convergence degrades

### Experiment 4: Rössler (different attractor topology)
R ossler has a simpler folding structure.  Show div
converges at d=3 with a different Lyapunov sum.

### Experiment 5: Logistic map (discrete time)
Discrete dynamics.  σ(x) should vary with position (high near
the boundary of the chaotic attractor).

### Experiment 6: Lag selection via div
Fix d=3 for Lorenz.  Sweep L=1..30.  Show div is approximately
L-independent for good lags and degrades for L too small or
too large (oversampling or undersampling of the dynamics).

### Experiment 7: Comparison with FNN
Compute FNN percentage as a function of d alongside our div.
Show: div stabilization agrees with FNN threshold for
sufficient d, but div requires no distance threshold parameter.

## What's implemented

- ✅ delay_embed
- ✅ local_pushforward (KDTree-accelerated, tricube kernel)
- ✅ map_attractor (KDTree built once, serial loop)
- ✅ dimension_sweep
- ✅ lorenz63, rossler, logistic_map generators
- ✅ Preliminary Lorenz results

## What's needed

- Experiment harness for bandwidth sweep (easy)
- Noise-added versions of generators (easy)
- FNN implementation (moderate — standard algorithm)
- Lag sweep (easy — reuse dimension_sweep with L varying)
- Plotting infrastructure for paper figures (moderate)
- Continuous-time Lyapunov sum reference values

## Target venue

Chaos (AIP) — the divergence diagnostic is a practical tool for
the nonlinear dynamics community.  8-12 pages with figures.

## Estimated effort

- Remaining experiments: ~1-2 weeks
- Writing: ~1 week
- Figures: ~3-4 days
- Total: ~3-4 weeks from now
