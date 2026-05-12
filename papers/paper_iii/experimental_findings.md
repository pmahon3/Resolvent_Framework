# Experimental Findings (2026-05-12)

## Experiment 1: Lorenz dimension sweep (preliminary)
N=50000, L=10, h=3/5/8.

- div becomes more negative with d, stabilizes at d≈5-6
- σ doesn't decrease with d (dominated by nonlinearity at these h)
- div is the cleaner diagnostic

## Experiment 2: Bandwidth stability (d=3, Lorenz)
h = 2, 3, 4, 5, 6, 8, 10, 12.

**Finding: div is NOT h-independent.**
- Small h (2-3): div very negative (-40 to -18), high variance
- Medium h (5-8): div moderate (-5 to -0.5)
- Large h (10-12): div near 0 or positive

σ varies only mildly with h (3.1 to 3.4). So σ is actually
MORE h-stable than div at this embedding dimension.

**Interpretation:** At small h, the local linear fit captures
fine-grained dynamics (rapid contraction/expansion), giving large
|div|. At large h, it averages over the whole attractor, washing
out the dynamics. The "intrinsic" Lyapunov sum sits somewhere in
between — but the delay-coordinate Jacobian has companion structure,
so tr(A) ≠ Lyapunov sum directly.

**Revision needed:** The claim "div is h-independent" fails. The
claim should be: "div stabilization WITH d, AT FIXED h, indicates
sufficient embedding." The h-dependence is a feature of the local
approximation, not the embedding quality.

## Experiment 3: Noise robustness (Lorenz, d=2..6)
Noise fractions: 0%, 1%, 5%, 10%, 20% of signal std.

**Finding: div is sensitive to observational noise.**
- Clean: div at d=5 is -42.5
- 1% noise: div at d=5 is -12.4
- 5% noise: div at d=5 is -1.5 (barely distinguishable)
- 10-20% noise: div is flat, no diagnostic value

σ increases with noise but only slightly (3.87 → 4.20 at d=5).

**Interpretation:** The noise corrupts the local Jacobian estimate.
At 5%+ noise, the Jacobian is too noisy to give a reliable trace.
The method works in the low-noise regime only.

**Operating regime:** Noise-to-signal < ~2% for the div diagnostic
to function on Lorenz with N=50000 and h=5.

## Revised assessment

The original framing ("divergence stabilization as h-independent,
noise-robust embedding diagnostic") is too strong. The honest
framing:

1. **Div stabilization with d at fixed h is a valid criterion for
   sufficient embedding dimension** — this is supported by Exp 1.

2. **Div is NOT h-independent** — it depends on the scale of the
   local linearization. This is expected (the Jacobian trace depends
   on the scale at which you linearize nonlinear dynamics).

3. **Div is NOT noise-robust beyond ~2% noise** — the local
   Jacobian estimation degrades with noise. More data or
   regularization might extend this.

4. **σ is more h-stable than div** — unexpected! At fixed d, σ
   varies less with h than div does. But σ doesn't respond to
   embedding dimension changes, so it's not an embedding diagnostic.

## What the paper should actually claim

**Conservative claim:** For clean or near-clean time series, the
convergence of ⟨tr(A)⟩ with embedding dimension d, at a fixed
bandwidth h, provides a diagnostic for sufficient embedding that
is complementary to FNN. It does not require a distance threshold
and produces the local Jacobian as a byproduct.

**The stochastic model (A(x), σ(x)) is the secondary contribution:**
once sufficient d is established, the local drift-diffusion
decomposition is available. σ(x) is interpretable only when the
embedding is sufficient (div has stabilized).

**The algebraic framing remains valid:** the underdetermined
descent is real, and the diagnostics navigate it. But the
diagnostic is more nuanced than "div is intrinsic" — it's "div
convergence with d flags sufficiency."

## Open questions from experiments

1. Is the h-dependence of div reducible? (Adaptive bandwidth,
   or normalization by n_eff?)

2. Can noise robustness be improved? (Regularized Jacobian,
   total least squares, or larger N?)

3. What is the correct theoretical value of ⟨tr(A)⟩ in delay
   coordinates? (Companion matrix structure means tr(A) ≠
   Lyapunov sum directly.)

4. Does the div convergence pattern differ for attractors with
   different topologies (Rössler, Hénon, etc.)?
