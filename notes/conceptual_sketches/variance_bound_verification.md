# Variance Bound Verification

**Status:** COMPLETE for Takens regime. Pre-Takens and infinite-lag cases remain open.
**Date:** 2026-04-05
**Claim to verify:** ‖f̂_n^(L) - E[f | 𝒪_h^(L)]‖_{L²(μ)} ≤ C · (L^⌈s⌉ / n)^{1/2}

---

## Setup

We have:
- True target: g* = E[f | 𝒪_h^(L)] — the L²(μ)-projection of f onto L²(X, 𝒪_h^(L), μ)
- Estimator class: 𝒜_h^(L) = {p ∘ Φ_h^(L) : p polynomial of degree ≤ D} for D = ⌈s⌉
- Estimator: f̂_n^(L) = argmin_{g ∈ 𝒜_h^(L)} (1/n) Σᵢ (f(xᵢ) - g(xᵢ))²

The variance bound measures how far f̂_n^(L) is from the best element of 𝒜_h^(L)
(or from g*) due to finite sampling.

**Issue 1:** g* = E[f | 𝒪_h^(L)] need not be in 𝒜_h^(L).

𝒜_h^(L) is polynomials in Φ_h^(L). L²(X, 𝒪_h^(L), μ) is all L²-measurable
functions of Φ_h^(L) — a much larger class (includes nonlinear functions of
delay vectors, not just polynomials).

So f̂_n^(L) is the empirical minimiser over polynomials in Φ_h^(L), NOT over
all 𝒪_h^(L)-measurable functions. The gap between these two is an additional
approximation error we did not account for in the bias bound.

**Revised decomposition:**

‖f - f̂_n^(L)‖ ≤ ‖f - g*‖        (bias: f vs. 𝒪_h^(L)-projection)
              + ‖g* - g_D*‖       (approximation: best L²-function vs. best degree-D polynomial)
              + ‖g_D* - f̂_n^(L)‖  (estimation: best polynomial vs. empirical minimiser)

where g_D* = argmin_{g ∈ 𝒜_h^(L)} ‖f - g‖_{L²(μ)} is the best polynomial approximation.

The first term was handled in the bias bound (≤ 2‖f‖_{L∞} · δ(L)^{1/2}).
The second term is a polynomial approximation error — NEW, not previously accounted for.
The third term is the pure statistical/variance term.

---

## The new term: polynomial approximation error ‖g* - g_D*‖

g* = E[f | 𝒪_h^(L)] is a Borel function of Φ_h^(L)(x) ∈ ℝ^(L+1).
g_D* is the best degree-D polynomial approximation to g* in L²(μ).

**When is g* well-approximated by degree-D polynomials?**

g* = g̃* ∘ Φ_h^(L) where g̃* : ℝ^(L+1) → ℝ is a Borel function.

If g̃* ∈ Hölder(s) on the image Φ_h^(L)(X) ⊆ ℝ^(L+1), then by the
Weierstrass theorem, there exist polynomials p_D of degree D such that:

  sup_{z ∈ Φ_h^(L)(X)} |g̃*(z) - p_D(z)| ≤ C_g · D^{-s/(L+1)}

(Jackson's theorem for polynomial approximation on compact sets in ℝ^m,
with approximation rate D^{-s/m} for Hölder(s) functions in ℝ^m, m = L+1.)

So:

  ‖g* - g_D*‖_{L²(μ)} ≤ C_g · D^{-s/(L+1)}

**Issue 2:** We need D^{-s/(L+1)} to be small. But as L increases (more lags),
the approximation rate WORSENS: the image Φ_h^(L)(X) lives in higher-dimensional
space ℝ^(L+1), and polynomial approximation in ℝ^m gets harder as m grows.

This is the **curse of dimensionality in the lag depth L**.

For fixed D = ⌈s⌉:
  ‖g* - g_D*‖ ≤ C · D^{-s/(L+1)} = C · ⌈s⌉^{-s/(L+1)}

This → 1 as L → ∞ for fixed D. So we cannot fix D and let L grow —
we need D to grow with L to maintain approximation quality.

**To achieve ‖g* - g_D*‖ ≤ ε:** need D ≥ C(ε, s, L)^{(L+1)/s}.

This is exponential in L — a serious problem. The polynomial degree needed
to approximate g* in ℝ^(L+1) grows exponentially with L.

**This is the curse of dimensionality.** Standard polynomial approximation
in ℝ^m requires degree exponential in m for a fixed error tolerance.

---

## Does the curse of dimensionality kill the bound?

Not necessarily. Two potential escapes:

**Escape 1 — Structure of g̃*:**

g̃* = E[f | Φ_h^(L)(x)] as a function of z = Φ_h^(L)(x) ∈ ℝ^(L+1) may
have special structure due to the dynamics T. Specifically:

- The image Φ_h^(L)(X) ⊆ ℝ^(L+1) is NOT all of ℝ^(L+1) — it's a
  lower-dimensional set (the delay embedding of X, which has dimension
  dim(X) ≤ L+1 by the Takens/reconstruction theory).
- If X is a d-dimensional manifold, then Φ_h^(L)(X) is a d-dimensional
  submanifold of ℝ^(L+1) for L ≥ 2d.
- Polynomial approximation on a d-dimensional submanifold of ℝ^(L+1) has
  rate D^{-s/d}, NOT D^{-s/(L+1)}.

**This is the key structural insight:** the intrinsic dimension of the
image is d (the dimension of X), not L+1 (the ambient dimension). So:

  ‖g* - g_D*‖ ≤ C · D^{-s/d}

and to achieve error ε, we need D ~ ε^{-d/s} — polynomial in 1/ε,
independent of L. The curse of dimensionality is broken by the
low-dimensional structure of the delay embedding.

**Escape 2 — Shift structure of 𝒜_h^(L):**

The delay algebra 𝒜_h^(L) has a graded shift structure:
- Degree 1: span{h, h∘T, h∘T², …, h∘T^L} — dimension L+1
- Degree 2: span{(h∘Tⁱ)(h∘Tʲ) : 0≤i≤j≤L} — dimension O(L²)
- Degree D: dimension O(L^D)

The TOTAL dimension of 𝒜_h^(L) at degree ≤ D is O(L^D) = O(L^⌈s⌉).

But the shift invariance of the algebra means many of these monomials
are "the same" modulo the dynamics T. The effective dimension may be
lower than O(L^⌈s⌉) if we account for the algebraic relations imposed
by T. This is the orbit structure.

---

## Revised variance bound using intrinsic dimension

Assuming Escape 1 (intrinsic dimension d, which holds in the Takens regime):

**Dimension of effective estimator class:** O(D^d) (polynomials of degree D
restricted to the d-dimensional image Φ_h^(L)(X)).

NOT O(L^D) as previously stated.

**Revised variance bound:**

  ‖g_D* - f̂_n^(L)‖²_{L²(μ)} ≤ C · D^d / n

(VC dimension of degree-D polynomials on a d-dimensional set is O(D^d).)

**Revised polynomial approximation error (from Escape 1):**

  ‖g* - g_D*‖_{L²(μ)} ≤ C' · D^{-s/d}

**Optimal D:** Balance polynomial approximation and variance:

  D^{-s/d} ~ (D^d/n)^{1/2}
  D^{-s/d} ~ D^{d/2} / n^{1/2}
  D^{-(s/d + d/2)} ~ n^{-1/2}
  D^{(2s+d²)/(2d)} ~ n^{1/2}
  D* ~ n^{d/(2s+d²)}

**Optimal rate:**

  ‖g* - f̂_n^(L)‖ ~ n^{-s/(2s+d²)} · (log terms from L)

Hmm — this has d² in the denominator, which seems wrong. Let me recheck.

---

## Recheck: the standard nonparametric regression rate

Standard result (Yang-Barron, Gyorfi et al.): for estimating a Hölder(s)
function g : ℝ^m → ℝ from n observations, the minimax optimal rate is:

  ‖ĝ_n - g‖²_{L²} ~ n^{-2s/(2s+m)}

where m is the dimension of the input space.

In our case:
- Input space: Φ_h^(L)(X), dimension m = d (intrinsic), not L+1 (ambient)
- Target function: g̃* ∈ Hölder(s) on this d-dimensional set
- Rate: n^{-2s/(2s+d)}   →   ‖g* - f̂_n^(L)‖ ~ n^{-s/(2s+d)}

The d² issue above was an error in my algebra — let me redo.

**Correct balance:** 

Polynomial approximation error: D^{-s/d}
Variance: (D^d / n)^{1/2}

Set equal:
  D^{-s/d} = D^{d/2} · n^{-1/2}
  D^{-s/d - d/2} = n^{-1/2}
  D^{(2s + d²)/(2d)} = n^{1/2}   ← this IS d² in the exponent

So D* = n^{d/(2s+d²)}... but this contradicts the standard rate.

**Where is the discrepancy?**

The standard rate n^{-2s/(2s+d)} uses a different approximation scheme.
The polynomial approximation on a d-dimensional manifold in ℝ^m needs
to be done intrinsically — polynomials in local coordinates on the manifold,
not polynomials in the ambient ℝ^m restricted to the manifold.

If we use intrinsic approximation (e.g. via the eigenfunctions of the
Laplace-Beltrami operator on Φ_h^(L)(X)), then:
- Approximation error: λ_D^{-s/2} where λ_D is the D-th eigenvalue
- For a d-manifold: λ_D ~ D^{2/d} (Weyl's law)
- So approximation error: D^{-s/d} ✓ (same as before)
- Variance: D/n (D basis functions, n observations)

Balance: D^{-s/d} = (D/n)^{1/2}
  D^{-s/d - 1/2} = n^{-1/2}
  D^{(2s+d)/(2d)} = n^{1/2}
  D* = n^{d/(2s+d)}

Rate: D*^{-s/d} = n^{-s/(2s+d)}  ✓

**This recovers the standard rate.** The discrepancy above was using
polynomial degree as a proxy for dimension in the wrong way.

**Conclusion:** With intrinsic approximation on the d-dimensional image:

  ‖g* - f̂_n^(L)‖_{L²(μ)} ~ n^{-s/(2s+d)}

**This is the standard nonparametric regression rate with intrinsic dimension d.**

---

## What this means for the full bound

**Corrected forward finite-sample density bridge:**

‖f - f̂_n^(L)‖_{L²(μ)} ≤ 2‖f‖_{L∞}·δ(L)^{1/2} + C·n^{-s/(2s+d)}

where:
- First term: bias from σ-algebra approximation (δ(L) → 0 iff reconstruction)
- Second term: statistical term at the minimax-optimal nonparametric rate
  with INTRINSIC dimension d (dimension of X, not ambient lag dimension L+1)
- The lag depth L only appears implicitly through δ(L)

**This is a cleaner and more honest statement than before:**
- The L^⌈s⌉/n rate I stated earlier was WRONG — it used ambient dimension
- The correct rate is n^{-s/(2s+d)} with intrinsic dimension d
- The intrinsic dimension d is the key parameter, not L

**The role of L:** L controls δ(L) (the bias). The statistical term is
at rate n^{-s/(2s+d)} regardless of L (once L ≥ 2d, so the delay embedding
is in the Takens regime and the image is d-dimensional).

---

## Conditions required for the corrected bound

1. **Reconstruction holds:** 𝒪_h = ℬ mod μ, so δ(L) → 0 as L → ∞.

2. **X is a d-dimensional manifold** (or more generally, the intrinsic
   dimension of the delay embedding Φ_h^(L)(X) is d for L ≥ L₀).

3. **g* = E[f | 𝒪_h^(L)] is Hölder(s) as a function on Φ_h^(L)(X).**
   This requires smoothness of f and the conditional expectation operator.
   For f ∈ L∞ this is not automatic — need additional regularity.

4. **Intrinsic approximation is used** (eigenfunctions of Laplace-Beltrami
   on the image, or equivalent). For the delay algebra specifically,
   the natural basis is the Koopman eigenfunctions — Koopman modes of T
   pulled back through h. This connects back to Paper II.

**Condition 3 is the most delicate.** If f is not smooth as a function
of the delay coordinates, the rate degrades. For f ∈ L²(μ) only (no
smoothness), the rate would be arbitrarily slow.

---

## Summary

**What is verified:**

The bias bound ‖f - E[f|m]‖ ≤ 2‖f‖_{L∞}·δ(m)^{1/2} is correct (proved
in bias_bound_attempt.md).

The variance bound requires more care:

- The naive bound C·(L^⌈s⌉/n)^{1/2} is WRONG — it uses ambient dimension L+1
- The correct bound uses intrinsic dimension d: C·n^{-s/(2s+d)}
- This requires: (a) X is d-dimensional, (b) delay embedding reaches
  dimension d for L ≥ L₀, (c) g* is Hölder(s) on the image

**The corrected forward finite-sample density bridge:**

  ‖f - f̂_n^(L)‖ ≤ 2‖f‖_{L∞}·δ(L)^{1/2} + C·n^{-s/(2s+d)}   (*)

This is valid for L ≥ L₀ (Takens regime), under conditions 1–4 above.

**What still needs work:**

1. Condition 3 (smoothness of g*) — when does the conditional expectation
   inherit smoothness from f and T? → See Section below.

2. What happens for L < L₀ (pre-Takens regime)? The rate should degrade
   as L increases toward L₀ and then stabilise. Currently (*) has no
   L-dependence in the statistical term once L ≥ L₀.

3. The role of L below L₀: for L < L₀, the image Φ_h^(L)(X) may have
   effective dimension < d (some directions not yet separated), and the
   statistical rate should be n^{-s/(2s+dim_eff(L))} where dim_eff(L)
   increases from 0 to d as L goes from 0 to L₀.

4. The optimal choice of L given n: balance δ(L)^{1/2} against the
   condition L ≥ L₀. For finite systems (Takens regime), L₀ is fixed
   and the optimal L = L₀. For infinite-lag systems (L₀ = ∞), need
   L = L*(n) from the orbit separation rate.

---

## Condition 3: When does g* inherit regularity from f?

**Setup.** We want to know when

  g*(z) := E[f | Φ_h^(L)(x) = z]

is Hölder(s) as a function of z ∈ Φ_h^(L)(X) ⊆ ℝ^(L+1).

g* is the disintegration of f with respect to the map Φ_h^(L): X → ℝ^(L+1).
Explicitly:

  g*(z) = ∫_X f(x) dμ_z(x)

where {μ_z}_{z ∈ ℝ^(L+1)} is the disintegration of μ with respect to Φ_h^(L)
(i.e., μ_z = conditional distribution of x given Φ_h^(L)(x) = z).

---

### Case 1: Takens regime (L ≥ L₀, Φ_h^(L) injective mod μ)

When L ≥ L₀ and reconstruction holds, Φ_h^(L) is injective μ-a.e. (this
is what reconstruction means in the Takens picture: distinct orbits give
distinct delay vectors).

In this case, the disintegration degenerates: μ_z = δ_{Φ^{-1}(z)} (a
point mass at the unique x with Φ_h^(L)(x) = z), so:

  g*(z) = f(Φ_h^(L)^{-1}(z))

where Φ_h^(L)^{-1} : Φ_h^(L)(X) → X is the (μ-a.e.) inverse.

**Regularity of g* = f ∘ Φ^{-1}:**

  - If Φ^{-1} is Hölder(α) (i.e., |x - x'| ≤ C|Φ(x) - Φ(x')|^α), and
  - If f is Hölder(β) on X,
  - Then g* = f ∘ Φ^{-1} is Hölder(αβ) on Φ(X).

**When is Φ^{-1} Hölder?**

This is a question about the inverse map of the delay embedding. In the
Takens setting (X = smooth d-manifold, T = C^r diffeomorphism, h ∈ C^r,
L ≥ 2d+1, generic h), the delay embedding Φ_h^(L) is a C^1 embedding:

  Φ_h^(L) : X → ℝ^(L+1) is a C^1 embedding.

A C^1 embedding of a compact manifold is bi-Hölder: there exist C, α > 0
(in fact α = 1 for smooth embeddings) such that

  C^{-1} |x - x'| ≤ |Φ(x) - Φ(x')| ≤ C |x - x'|

(Lipschitz equivalence between the manifold metric and the induced metric
in ℝ^(L+1)). So Φ^{-1} is Lipschitz (Hölder with α = 1).

**Conclusion for Case 1:**

If X is a C^∞ compact d-manifold, T is C^r, h ∈ C^r (r ≥ s+1), and
f ∈ Hölder(s) on X, then:

  g* ∈ Hölder(s) on Φ_h^(L)(X)

with the same smoothness exponent s.

*Why the same s:* Φ^{-1} is Lipschitz (exponent 1), f is Hölder(s), so
g* = f ∘ Φ^{-1} is Hölder(min(s·1, s)) = Hölder(s). ✓

This is the good news: **in the Takens regime, g* inherits Hölder(s) from f.**

---

### Case 2: Pre-Takens regime (L < L₀, Φ_h^(L) not injective)

When L < L₀, Φ_h^(L) is not injective: some distinct x, x' ∈ X have
Φ_h^(L)(x) = Φ_h^(L)(x'). In this case μ_z is not a point mass — it's
a genuine probability measure on the fiber:

  F_z = {x ∈ X : Φ_h^(L)(x) = z}

and g*(z) = ∫_{F_z} f(x) dμ_z(x) is an average over the fiber.

**Regularity of g* when fibers are non-trivial:**

g* inherits smoothness only if the fiber averages vary smoothly with z.
This depends on how the fibers F_z vary as z moves — the "fiber regularity."

In general, for f ∈ Hölder(s) and the fiber map z ↦ μ_z satisfying
appropriate regularity (e.g., if the fibration is smooth), we get

  g* ∈ Hölder(s') for some s' ≤ s.

The exponent may degrade because averaging over fibers is a smoothing
operation (it contracts the Hölder seminorm), but the result only has
the regularity of the fiber map z ↦ μ_z.

**This case is less clean** — the smoothness of g* depends on the
geometry of the non-injective fibers, which is dynamically complex.

---

### What this means practically

For the bound (*) to hold with rate n^{-s/(2s+d)}, we need Condition 3:
g* ∈ Hölder(s) on Φ_h^(L)(X).

**Case 1 (L ≥ L₀, Takens regime):** Condition 3 holds with the same s
as f, provided f ∈ Hölder(s) on X and T is C^{s+1}. This is the
favorable case — the rate n^{-s/(2s+d)} is achievable.

**Case 2 (L < L₀):** Condition 3 may fail or hold with degraded s' < s.
The rate degrades to n^{-s'/(2s'+d)} for some s' ≤ s. In the worst case
(f not measurable w.r.t. a smooth fiber structure), the rate is
arbitrarily slow.

**For Paper III's purposes:** We should state Condition 3 as an explicit
assumption (f ∈ Hölder(s) on X, T ∈ C^{s+1}), and note that in the
Takens regime it is automatically satisfied. This is analogous to how
standard nonparametric regression assumes the regression function is Hölder.

---

### Revised statement of Condition 3

**Condition 3 (precise):** f ∈ Hölder(s, X) (f is Hölder(s) on the
manifold X) and T ∈ C^{r}(X) for r > s.

**Lemma (Regularity inheritance):** Under Condition 3, in the Takens
regime (L ≥ L₀, Φ_h^(L) a C^1 embedding), g* = E[f | 𝒪_h^(L)] is
Hölder(s) on Φ_h^(L)(X), with Hölder constant C_g ≤ C · ‖f‖_{Hölder(s)}.

**Proof sketch:** g*(z) = f(Φ^{-1}(z)), and Φ^{-1} is Lipschitz (the
inverse of a smooth embedding of a compact manifold is Lipschitz). So:

  |g*(z) - g*(z')| = |f(Φ^{-1}(z)) - f(Φ^{-1}(z'))|
                   ≤ ‖f‖_{Hölder(s)} · |Φ^{-1}(z) - Φ^{-1}(z')|^s
                   ≤ ‖f‖_{Hölder(s)} · (Lip(Φ^{-1}))^s · |z - z'|^s

So ‖g*‖_{Hölder(s)} ≤ C · ‖f‖_{Hölder(s)} where C = (Lip(Φ^{-1}))^s. □

---

### The role of L below L₀ (pre-Takens): effective dimension

Below L₀, the image Φ_h^(L)(X) has effective dimension dim_eff(L) < d
because the delay vectors do not yet separate all directions of X.

More precisely: the map Φ_h^(L) identifies x ~ x' whenever
  h(T^k x) = h(T^k x') for all k = 0, …, L.

The "depth" at which T^k x and T^k x' first separate determines L₀.
For k < L₀ pairs, the fibers are non-trivial.

**How dim_eff(L) grows from 0 to d:**

At L = 0: dim_eff = 1 (just h(x), a scalar).
At L = L₀: dim_eff = d (full embedding achieved).
For 0 < L < L₀: dim_eff = min(L+1, d) approximately,
  but the actual effective dimension depends on T and h.

The statistical rate in the pre-Takens regime is:

  n^{-s/(2s + dim_eff(L))}

which improves as L increases from 0 to L₀. After L₀, dim_eff stabilises
at d and the statistical rate stabilises at n^{-s/(2s+d)}.

**This gives a picture of L as a smoothness parameter for the statistical
problem:** more lags = better representation = faster rate (up to L₀),
but also higher-dimensional image = more bias needed to contract.

The optimal L*(n) balances:
  1. L ≥ L₀ to enter the Takens regime (if possible with available n)
  2. δ(L)^{1/2} ≤ n^{-s/(2s+d)} (bias ≤ statistical rate)

For finite L₀ (Takens regime exists), L*(n) = L₀ for all sufficiently
large n: the bias is 0 and the rate is n^{-s/(2s+d)}.

For L₀ = ∞ (no exact reconstruction), L*(n) must grow with n. The
optimal L*(n) depends on the orbit separation rate — the rate at which
δ(L) → 0 as L → ∞.

---

## Final status of the variance bound

**Condition 3 resolved (for the Takens regime):**

In the Takens regime (L ≥ L₀, Φ_h^(L) a C^1 embedding):
- g* = f ∘ Φ^{-1} is Hölder(s) when f ∈ Hölder(s) and T ∈ C^{s+1}
- The rate n^{-s/(2s+d)} is achievable
- This is the standard nonparametric regression rate with intrinsic dimension d

**Full forward finite-sample density bridge (final corrected form):**

**Theorem** (Forward bridge, Takens regime): Let (X, ℬ, μ, T) be an
ergodic measure-preserving system on a C^∞ compact d-manifold. Let
h ∈ C^r(X) for r > s, and suppose Φ_h^(L) is a C^1 embedding for L ≥ L₀
(Takens regime). For f ∈ Hölder(s) ∩ L∞(X):

  ‖f - f̂_n^(L)‖_{L²(μ)} ≤ 2‖f‖_{L∞} · δ(L)^{1/2} + C · n^{-s/(2s+d)}

where:
- δ(L) = 0 for L ≥ L₀ (exact reconstruction in the Takens regime)
- d = dim(X) is the intrinsic dimension
- C depends on s, d, ‖f‖_{Hölder(s)}, Lip(Φ^{-1})
- f̂_n^(L) uses an intrinsic approximation basis (e.g. Koopman eigenfunctions)

**Corollary** (Takens regime, L ≥ L₀): δ(L) = 0, so the bound reduces to:

  ‖f - f̂_n^(L)‖_{L²(μ)} ≤ C · n^{-s/(2s+d)}   (minimax-optimal rate)

**What remains open:**

1. The pre-Takens regime (L < L₀): dim_eff(L) growth rate and optimal L*(n).
2. The infinite-lag case (L₀ = ∞): quantifying δ(L) → 0 rate for specific
   systems and finding optimal L*(n) = L*(n, T, h).
3. The connection to the edge divergence D(Γ_h ‖ Γ̂_h^(n)) — bridging
   the forward bound to the divergence geometry of Paper II.
4. Whether the rate n^{-s/(2s+d)} is achievable by f̂_n^(L) specifically
   (not just by any estimator) — i.e., whether 𝒜_h^(L) itself achieves
   the minimax rate or whether an additional truncation/regularization is needed.
