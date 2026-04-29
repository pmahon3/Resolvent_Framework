---
name: Lyapunov exponents from the observational framework
description: Future direction — generalized Lyapunov exponents as asymptotic rates of observational distinction/separation, with classical tangent-space exponents as a special case under extra smoothness
type: project
---

# Lyapunov Exponents from the Observational Framework

**Status:** Post-arXiv direction. Framing settled 2026-04-28. Not part of the current
three-paper arc. Most concrete near-term question identified (see Option 1 below).

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

---

## What the framework already has (Papers I–II)

1. Conditional regularity kernel $\kappa_Q$ — forced by the measure, not chosen
2. Time-indexed semigroup $\{\Pi_t\}$ — derived from Chapman–Kolmogorov
3. Canonical factor $Q^*$ — specialises to delay map $\Phi_h$ in the measure-preserving case

These are upstream of any Lyapunov-type quantity. The fork: what plays the role of
"infinitesimal perturbation" in the observational language?

---

## Three natural generalizations

### Option 1 — Observable separation exponent (most concrete)

In the delay-map setting:
$$
\lambda_h(x,y) = \limsup_{n\to\infty} \frac{1}{n} \log d\!\bigl(\Phi_h(T^n x), \Phi_h(T^n y)\bigr)
$$
or its local version as $y \to x$. Measures exponential growth of observable separation,
not tangent expansion. Close in spirit to classical Lyapunov when reconstruction holds.

**Near-term concrete question:** in the delay-embedding setting of Paper II, does option 1
agree with the top Lyapunov exponent when $T$ is smooth and $h$ is generic? This would
be a theorem, not just a philosophical observation. Natural as an appendix or remark in
Paper II or a focused future note.

### Option 2 — Conditional-law divergence exponent (most native to framework)

$$
\lambda_{\mathrm{obs}} = \limsup_{t\to\infty} \frac{1}{t} \log D\!\bigl(\Pi_t(q,\cdot),\, \Pi_t(q',\cdot)\bigr)
$$
for some divergence $D$ between probability laws. Growth rate of how quickly two
initially similar observational states become distinguishable in law.

**The choice of $D$ is not innocent:**
- $D = $ total variation $\to$ recovers something close to the separation defect
- $D = $ KL divergence $\to$ connects to entropy production and Pesin's formula

The choice of $D$ determines which classical exponent you shadow.

### Option 3 — Refinement complexity exponent (already numerically present)

$$
\limsup_{L\to\infty} \frac{1}{L} \log \delta(L)
$$
Rate at which the separation defect decays under lag refinement. Less "local instability,"
more "resolution instability."

**Already in the Cantor notebook (Panel 5):** in the Cantor case $\delta(L) \sim (1/3)^{L+1}$,
giving refinement exponent $-\log 3$ per lag. The fibre-dilution picture (mean occupancy
$= N / 2^{L+1}$, information horizon $L^* \approx \log_2 N$) already encodes this rate.
In a general dynamical system with mixing rate $\beta$, the defect decay rate should encode
something like the Kolmogorov–Sinai entropy.

---

## Conceptual hierarchy

1. **General framework:** observational regularity + semigroup + reconstruction
2. **Generalized Lyapunov quantity:** asymptotic rate of observational separation or
   distinguishability (Options 1–3)
3. **Classical smooth case:** recover standard tangent-space Lyapunov exponents

Extra structure needed to descend to level 3:
- $X$ a smooth manifold, $T$ differentiable
- Semigroup kernels collapse to Dirac kernels ($\Pi_t = \delta_{T^t(\cdot)}$)
- Reconstruction faithful enough to recover local geometry

---

## Connection to Pesin's formula

When $D = $ KL and $T$ is smooth ergodic, option 2 should shadow the metric entropy
$h_\mu(T)$, which equals the sum of positive Lyapunov exponents (Pesin). This is the
route by which the observational framework makes contact with classical smooth ergodic
theory — not through the tangent cocycle directly, but through entropy/information.

---

## Fit with the programme

This direction would let the programme say: Lyapunov exponents are not primitive
geometric data either; they are special cases of asymptotic instability rates of
observational regularity. That fits the programme's general pattern of showing that
classical objects (probability, conditional laws, Koopman operators, Takens embeddings)
are special cases of more primitive observational structures.
