---
name: Lyapunov exponents from the observational framework
description: Future direction — generalized Lyapunov exponents as asymptotic rates of observational distinction/separation, with classical tangent-space exponents as a special case under extra smoothness
type: project
---

# Lyapunov Exponents from the Observational Framework

**Status:** Post-arXiv direction. Framing settled 2026-04-28. Not part of the current
three-paper arc. Most concrete near-term question identified (Option 1 below).

---

## Core thesis

Classical Lyapunov exponents are not primitive geometric data; they are special cases
of asymptotic instability rates of observational regularity. The framework already
contains the upstream ingredients to define a more general notion.

**Slogan:** Classical Lyapunov exponents measure how fast the *geometry forgets initial
conditions*; the observational framework measures how fast the *observable algebra
resolves them*. These are dual directions — Lyapunov is about divergence of trajectories,
the observational version is about convergence of the observable partition to the point.
In smooth ergodic systems they are related by Pesin's formula.

The direction fits the programme for the same reason the earlier papers do: it does not
deny the classical object, it relocates it as a special case of a more primitive
observational structure.

---

## What the framework already has (Papers I–II)

1. Conditional regularity kernel $\kappa_Q$ — forced by the measure, not chosen
2. Time-indexed semigroup $\{\Pi_t\}$ — derived from Chapman–Kolmogorov
3. Canonical factor $Q^*$ — specialises to delay map $\Phi_h$ in the measure-preserving case

These are upstream of any Lyapunov-type quantity. The fork: what plays the role of
"infinitesimal perturbation" in the observational language?

---

## Three options, ordered by conceptual ambition

### Option 1 — Observable separation exponent

**Best first theorem target.** Lives directly in the delay-map setting of Paper II.

In the delay-map setting:
$$
\lambda_h(x,y) = \limsup_{n\to\infty} \frac{1}{n} \log d\!\bigl(\Phi_h(T^n x), \Phi_h(T^n y)\bigr)
$$
or its local version as $y \to x$. Measures exponential growth of observable separation,
not tangent expansion. Close in spirit to classical Lyapunov when reconstruction holds.

**The theorem-shaped question:** when $T$ is smooth and $h$ is generic, does the
observable separation exponent recover the top Lyapunov exponent? To pressure-test
this, the key choice is which metric on $\Phi_h(X) \subset \mathbb{R}^{L+1}$ gives
the right chance of matching the top exponent in the smooth reconstructed case.
In the Euclidean metric on $\mathbb{R}^{L+1}$, the delay map measures separation
through the derivative of the finite-lag embedding $\Phi_h^{(L)}$. Under genericity
and faithful reconstruction, one expects the resulting observable separation rate to
reflect the fastest expanding tangent direction, but making this precise requires a
theorem comparing the induced metric on $\Phi_h^{(L)}(X)$ with the ambient Riemannian
geometry as $L \to \infty$ — this is where Takens-type genericity arguments would enter,
and where the claim earns its theorem status rather than resting on intuition.

Natural as a focused future note or appendix to Paper II.

### Option 2 — Conditional-law divergence exponent

**Most native to the full framework.** Requires no metric on the state space.

$$
\lambda_{\mathrm{obs}} = \limsup_{t\to\infty} \frac{1}{t} \log D\!\bigl(\Pi_t(q,\cdot),\, \Pi_t(q',\cdot)\bigr)
$$
for some divergence $D$ between probability laws. Growth rate of how quickly two
initially similar observational states become distinguishable in law.

**The choice of $D$ is not innocent:**
- $D = $ total variation $\to$ recovers something close to the separation defect
- $D = $ KL divergence $\to$ connects to entropy production and Pesin's formula

The choice of $D$ determines which classical exponent you shadow. Option 2 is the
right setting for the Pesin bridge (see below).

### Option 3 — Refinement complexity exponent

**Most immediately computable; conceptually furthest from classical Lyapunov.**
Better understood as a resolution or entropy exponent than an instability exponent.

$$
\limsup_{L\to\infty} \frac{1}{L} \log \delta(L)
$$
Rate at which the separation defect decays under lag refinement.

**Already in the Cantor notebook (Panel 5):** $\delta(L) \sim (1/3)^{L+1}$ gives
refinement exponent $-\log 3$ per lag. The fibre-dilution picture (mean occupancy
$= N/2^{L+1}$, information horizon $L^* \approx \log_2 N$) already encodes this.
In a general dynamical system, the defect decay rate connects to Kolmogorov–Sinai
entropy rather than to pointwise Lyapunov exponents. Closest in language to
Paper III's certification framework.

---

## Conceptual hierarchy

1. **General framework:** observational regularity + semigroup + reconstruction
2. **Generalized Lyapunov quantity:** asymptotic rate of observational separation or
   distinguishability (Options 1–3 above, ordered by conceptual ambition)
3. **Classical smooth case:** recover standard tangent-space Lyapunov exponents

The hierarchy prevents two bad confusions: that the current papers already prove
a Lyapunov theory, and that the generalized observational exponent is merely a
loose metaphor for the classical one.

Extra structure needed to descend to level 3:
- $X$ a smooth manifold, $T$ differentiable
- Semigroup kernels collapse to Dirac kernels ($\Pi_t = \delta_{T^t(\cdot)}$)
- Reconstruction faithful enough to recover local geometry

---

## Connection to Pesin's formula

When $D = $ KL and $T$ is smooth ergodic, Option 2 should shadow the metric entropy
$h_\mu(T)$, which equals the sum of positive Lyapunov exponents (Pesin). This is the
route by which the observational framework makes contact with classical smooth ergodic
theory — not through the tangent cocycle directly, but through entropy/information.

---

## Fit with the programme

Classical objects already relocated by the programme: probability (Paper I),
conditional laws and Koopman operators (Paper II), Takens embeddings (Paper II/III).
Lyapunov exponents would be the next: not primitive geometric data, but special cases
of asymptotic instability rates of observational regularity under extra smoothness.
