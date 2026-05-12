# Positioning: What's New

## The landscape

| Approach | Level | Method | Output | Noise? |
|----------|-------|--------|--------|--------|
| Takens (1981) | Point | Generic embedding | Diffeomorphism | No |
| SYC (1991) | Point | Prevalent embedding | Injective map | No |
| Stark (1999) | Point | Forced/stochastic | Embedding with noise | Partially |
| BG (2025) | Measure | Optimal transport | Pushforward of density | Implicit |
| **This paper** | **Local** | **Kernel regression** | **(A(z), σ(z))** | **Yes — explicit** |

## What Botvinick-Greenhouse does

- Lifts Takens from points to probability measures
- Uses Wasserstein geometry (optimal transport)
- Proves embedding theorem at the measure level
- Computational: forecasts full state from lagged observations
- Global: works with the entire distribution ρ(z)
- Noise: handled implicitly through the Eulerian description

## What we do differently

- Works **locally**: at each point z, estimates the drift A(z)
  and diffusion σ(z) separately
- Uses **kernel regression** (not optimal transport)
- Produces a **stochastic dynamical model** as output:
  z_{t+1} = A(z)·z + b(z) + σ(z)·η
- The divergence tr(A(z)) is a **diagnostic** for embedding
  quality — not just a property of the dynamics
- Explicitly **separates** embedding-induced noise from genuine
  stochastic forcing
- Computationally lighter: no Wasserstein computation, just
  local linear algebra

## What we share

- Both generalize Takens to handle noise/stochasticity
- Both work with the pushforward (they globally, we locally)
- Both are motivated by the limitation of classical Takens to
  deterministic, noise-free systems
- Both can reconstruct from partial observations

## The genuine novelty

1. **The divergence diagnostic.** Using tr(A(z)) to distinguish
   genuine noise from embedding-induced noise. Nobody has
   proposed this specific criterion. FNN detects dimension
   insufficiency; our diagnostic detects any embedding deficiency
   including lag problems.

2. **Position-dependent Langevin model as output.** The pipeline
   doesn't just embed — it produces a stochastic model (A(z), σ(z))
   that can be simulated, analysed for stability, etc.

3. **The algebraic framing.** σ(z) as the local signature of the
   underdetermined descent from St(C) to Ω. This connects the
   applied method to the foundational framework of Papers I+II.

4. **Noise decomposition.** Explicit separation of:
   - Embedding-induced noise (reducible by better embedding)
   - Genuine stochastic forcing (irreducible)
   via the divergence diagnostic.

## What we need to verify experimentally

- That σ(z) decreases as embedding dimension d increases
  (expected: yes, by Takens)
- That div(z) converges to the true Lyapunov sum as d increases
  (expected: yes, if local linear fit is good)
- That the stabilization point (where both plateau) agrees with
  FNN's estimate of sufficient dimension
- That the method works on standard benchmarks (Lorenz, Rössler)
- That it degrades gracefully with observational noise

## Risk assessment

| Risk | Severity | Mitigation |
|------|----------|-----------|
| Bandwidth sensitivity | High | Adaptive h, stability plots |
| Local linear assumption fails | Medium | Use in smooth regions; detect via condition number |
| Not novel enough vs existing noise estimation | Medium | Emphasize divergence diagnostic + algebraic framing |
| Lorenz is "too easy" | Low | Include real data or harder systems |

## What this paper does NOT need from Papers I+II

- No orthomodular lattices
- No Kochen-Specker
- No Stone duality machinery
- No formal measure theory

It needs only the **framing**: "the reconstruction problem is
algebraically underdetermined; the divergence measures the cost
of the choice." One paragraph in the introduction, citing Papers
I and II. The paper stands on its computational contribution.
