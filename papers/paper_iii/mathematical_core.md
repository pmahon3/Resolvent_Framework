# Mathematical Core: Divergence and Noise

## Setting

A discrete-time dynamical system on a state space M ⊆ ℝ^m:

  x_{t+1} = F(x_t) + σ(x_t) · η_t,   η_t ~ N(0, I)

where F : M → M is the (unknown) deterministic drift and
σ : M → ℝ^{m×m} is the (unknown) position-dependent diffusion.

We observe a scalar function h : M → ℝ. The time series is
y_t = h(x_t).

## Delay reconstruction

Form delay vectors:

  z_t = (y_t, y_{t-L}, ..., y_{t-(d-1)L}) ∈ ℝ^d

This defines a map Φ : M → ℝ^d, the delay map:

  Φ(x) = (h(x), h(F^{-L}(x)), ..., h(F^{-(d-1)L}(x)))

If Φ is an embedding (Takens: generically, for d > 2·dim(M)),
then Φ is injective and the dynamics on M push forward to
dynamics on Φ(M) ⊆ ℝ^d:

  z_{t+1} = G(z_t) + ξ_t

where G = Φ ∘ F ∘ Φ^{-1} is the pushforward dynamics and ξ_t
is the transformed noise.

## The local linearization

At a point z in the reconstructed space, the linearized dynamics:

  z_{t+1} ≈ A(z) · (z_t - z) + G(z) + ξ_t

where A(z) = DG(z) is the Jacobian of the pushforward map at z.

In practice, A(z) is estimated by local linear regression:
minimize Σ_j w(||z_j - z|| / h) · ||z_{j+1} - A·z_j - b||²
over (A, b), with w a compactly supported kernel.

## Divergence of the pushforward

The divergence:

  div G(z) = tr(A(z)) = Σ_i ∂G_i/∂z_i (z)

This measures the local rate of volume change under the dynamics.

**For a deterministic measure-preserving system:**
  div G = 0 everywhere (Liouville theorem)

**For a deterministic dissipative system:**
  div G < 0 (volume contracts; = sum of Lyapunov exponents)

**For a stochastic system:**
  div G ≠ 0 even if the underlying deterministic part is
  volume-preserving, because the noise introduces apparent
  volume change in the reconstruction.

## The noise-divergence connection

### Key observation

Consider the Fokker-Planck equation for the stationary density
ρ(z) of the reconstructed dynamics:

  0 = -∇·(G(z)·ρ(z)) + (1/2)∇²(D(z)·ρ(z))

where D(z) = σ(z)·σ(z)^T is the diffusion tensor.

Rearranging:

  ∇·(G·ρ) = (1/2)∇²(D·ρ)

The left side involves div G (among other terms). The right
side involves the diffusion D. So div G and D are linked through
the stationary density.

### The practical version

More directly: the residuals from the local linear fit ARE the
noise samples:

  ε_t = z_{t+1} - (A(z_t)·z_t + b(z_t))

If the local linear model is exact (faithful embedding, linear
dynamics in the neighbourhood), then ε_t = ξ_t = the noise.

The local noise covariance:

  D(z) ≈ (1/k) Σ_{j: z_j ∈ B(z,h)} ε_j · ε_j^T

And the noise amplitude:

  σ²(z) ≈ tr(D(z)) / d = mean squared residual per dimension

### What div G tells you that residuals alone don't

The residuals give σ(z) — the noise amplitude at each point.
But div G tells you something additional: whether the noise is
"real" (genuine stochastic forcing) or "embedding-induced"
(artefact of insufficient embedding dimension).

**Argument:** If the embedding is faithful and the true system
is deterministic, then:
- G is well-defined (Φ is injective)
- div G = sum of Lyapunov exponents (known from the system)
- Residuals should be zero (no noise)

If the embedding is UNfaithful:
- Φ is not injective; multiple states map to the same z
- The "dynamics" z_{t+1} = G(z_t) is not well-defined (multi-valued)
- Local linear fit averages over the multi-valuedness
- Residuals capture the spread = the "induced noise"
- div G deviates from the true Lyapunov sum

So: **div G deviating from the expected Lyapunov sum ↔ embedding
is unfaithful ↔ noise is embedding-induced, not genuine.**

This is the diagnostic:
- Compute div G from local linearization
- Compare to expected Lyapunov sum (if known) or to the value
  obtained at higher embedding dimension
- If div G changes as d increases, the embedding was insufficient
- If div G stabilizes, the embedding is faithful and remaining
  noise is genuine

## Three regimes of σ(z)

1. **σ(z) large, div G anomalous:** Embedding insufficient.
   Increase d or change L. The noise is embedding-induced.

2. **σ(z) large, div G matches Lyapunov sum:** Embedding
   faithful, genuine stochastic forcing. The system is inherently
   noisy. The Langevin model (A(z), σ(z)) is the right output.

3. **σ(z) small, div G matches:** Embedding faithful, system
   nearly deterministic. Classical reconstruction succeeded.

## Connection to Paper I/II

In Paper I's language:
- The delay embedding Φ is a choice of realization Ω ⊆ St(C)
- σ(z) > 0 at a point z means: the local fibre Φ^{-1}(z) in
  state space is not a singleton — multiple states map to z
- This is mass on "non-principal ultrafilters" locally: the
  observation z doesn't determine a unique state
- div G anomaly = the descent from St(C) to Ω is lossy at z

In Paper II's language:
- The reconstruction problem is algebraically underdetermined
- σ(z) measures the LOCAL cost of the underdetermined choice
- A faithful embedding has σ(z) → 0: the choice becomes
  essentially unique (the fibre collapses to a point)

## What this ISN'T

This is not:
- A new embedding theorem (we use Takens as given)
- A global optimality result (we diagnose, not optimize globally)
- A replacement for FNN/MI (we complement them with residual
  analysis and the divergence diagnostic)
- A theorem about when embeddings exist (that's Takens/SYC)

This IS:
- A local, position-dependent characterization of embedding quality
- A principled noise estimator that distinguishes genuine from
  embedding-induced noise
- A stochastic extension that produces (A(z), σ(z)) as output
- A diagnostic for the practitioner: is my embedding sufficient?
