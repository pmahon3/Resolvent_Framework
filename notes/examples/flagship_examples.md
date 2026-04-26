# Flagship Examples — Structure from Observation

Three worked examples, one per paper, demonstrating the payoff of the
framework on problems that classical approaches handle poorly or not at all.
A fourth numerical example is reserved for Paper III pending empirical work.

Each example follows the same pipeline:
1. **Sketch** — the construction in prose, objects identified
2. **Verification** — formal proof or numerical simulation as appropriate
3. **Integration** — tex integration into the relevant paper once verified

---

## Example C — Paper I
### A Propositional Theory as a Query System

**Motivation.** CE is not an artifact of empirical observation. The framework
applies wherever structured observation is possible — including purely logical
settings. This example makes that scope explicit and recovers a classical
result (Gaifman/Scott-Krauss) as a consequence.

**The construction.**

- Let $\mathcal{L}$ be a countable propositional language with sentences
  $\{\phi_1, \phi_2, \ldots\}$.
- The **Lindenbaum algebra** $\mathrm{Lind}(\mathcal{L})$ of a consistent
  theory $T$ is the Boolean algebra of equivalence classes of sentences
  under $T$-provable equivalence.
- A **query system** is defined by taking the directed system of finite
  sub-algebras $\{\mathrm{Lind}(\phi_1,\ldots,\phi_n)\}_{n \geq 1}$, with
  refinement maps given by inclusion.
- An **observation** at level $n$ is a truth-value assignment to
  $\{\phi_1,\ldots,\phi_n\}$ consistent with $T$ — a probability charge
  $\nu_n$ on $\mathrm{Lind}(\phi_1,\ldots,\phi_n)$.
- **Compatibility** of the family $\{\nu_n\}$ is the standard coherence
  condition from probability logic (de Finetti/Carnap).

**CE in this setting.**

CE says: if a sentence $\phi$ is not implied by any finite conjunction of
axioms, it cannot carry persistent probability mass. More precisely: if
$\nu_n(\phi) \not\to 0$ along any cofinal sequence, then $\phi$ must be
implied at some finite level. This is a precise bridge between syntactic
unprovability and probabilistic negligibility.

**The Stone space.**

The Stone space of $\mathrm{Lind}(\mathcal{L})$ is the space of
**ultrafilters** of the Lindenbaum algebra — equivalently, the space of
**complete consistent extensions** of $T$, i.e. the space of possible worlds.
The probability measure that emerges from CE + the Carathéodory/Stone route
is a measure on possible worlds.

**Connection to classical results.**

This recovers and generalises the **Gaifman/Scott-Krauss theorem** on
probability logic: a coherent probability assignment on a propositional
language extends to a $\sigma$-additive measure on the space of complete
extensions. In the framework, this is a special case of the Observable
Extension Theorem; CE is the exact admissibility condition.

**What needs verification.**

- [ ] Confirm that the Lindenbaum algebra construction fits the query system
  axioms (Surjective Evaluation, Discriminability, directed refinements)
- [ ] Make the CE condition explicit in terms of the syntactic/semantic
  structure of $T$
- [ ] Identify exactly which classical theorem is recovered and state the
  comparison precisely
- [ ] Check: does CE here reduce to $\omega$-consistency or something weaker?

**Candidate tex home.** A worked example or remark in §4 or §6 of Paper I,
after the CE definition and before or within the bridge section.

---

## Example A — Paper II (Reconstruction side)
### The Cantor Set: Reconstruction Without Smoothness

**Motivation.** Takens's theorem requires a $C^2$ diffeomorphism on a smooth
compact manifold. The reconstruction theorem here requires only measurability.
The Cantor set is the sharpest possible demonstration: it is compact, has no
smooth structure, and has Hausdorff dimension $\log 2/\log 3 \approx 0.63$
(not an integer). Takens is simply inapplicable. The reconstruction theorem
works anyway.

**The construction.**

- State space: $X = \mathcal{C}$ (middle-thirds Cantor set) with the
  standard **Cantor measure** $\mu_{\mathcal{C}}$ (the unique self-similar
  measure with equal weights $1/2$ on each sub-interval).
- Transformation: $T(x) = 2x \mod 1$ restricted to $\mathcal{C}$
  (well-defined since $\mathcal{C}$ is $T$-invariant).
- Observable: $h(x) = x$ (identity on $\mathcal{C} \subset [0,1]$).

**The claim.**

The orbit $\{h \circ T^n : n \geq 0\}$ generates $\mathcal{B}(\mathcal{C})$
modulo $\mu_{\mathcal{C}}$, so reconstruction holds: $\mathcal{O}_h =
\mathcal{B}(\mathcal{C})$ mod $\mu_{\mathcal{C}}$.

**Sketch of argument.**

Points of $\mathcal{C}$ are identified by their ternary expansions using only
digits $\{0, 2\}$. The map $T$ shifts the ternary expansion. The delay
vectors $(h(x), h(Tx), \ldots, h(T^L x))$ record the first $L+1$ ternary
digits of $x$ — so at lag $L$, the delay map distinguishes points that differ
in their first $L+1$ digits. Since $\mu_{\mathcal{C}}$-a.e. pair of distinct
points differs at some finite digit, $\mathcal{O}_h = \mathcal{B}(\mathcal{C})$
mod $\mu_{\mathcal{C}}$.

**The approximation error $\delta(L)$.**

At lag $L$, $\mathcal{O}_h^{(L)}$ is the $\sigma$-algebra generated by the
first $L+1$ ternary digits — equivalently, the $\sigma$-algebra of the
$2^L$ Cantor cylinder sets at generation $L$, each carrying
$\mu_{\mathcal{C}}$-measure $2^{-L}$.

The worst-approximable sets $S$ are those that cut across level-$L$ cylinders
non-trivially. The best approximation error for such $S$ is of order
$\mu_{\mathcal{C}}(\text{one cylinder}) = 2^{-L}$.

So $\delta(L) \sim 2^{-L}$, with no smoothness index required.

**Note:** an earlier sketch claimed $(2/3)^L$, confusing the geometric ratio
of the Cantor construction (middle-thirds removal) with the measure-theoretic
approximation rate, which is governed by cylinder measure under $\mu_{\mathcal{C}}$.
The correct rate is $2^{-L}$. This needs formal verification.

**What Takens cannot say.**

- $\mathcal{C}$ is not a manifold: no $C^2$ structure, no tangent space,
  no dimension in the classical sense.
- The doubling map on $\mathcal{C}$ is not a diffeomorphism.
- Takens's $2d+1$ delay bound is meaningless here ($d$ is not an integer).

**What needs verification.**

- [ ] Confirm $T$-invariance of $\mu_{\mathcal{C}}$ under the doubling map
- [ ] Make the ternary digit argument precise (measurability of the
  separation events)
- [ ] Compute $\delta(L)$ explicitly and verify the $2^{-L}$ decay rate
      (rate is governed by cylinder measure $\mu_{\mathcal{C}}(F_z) = 2^{-L}$,
      not by the $(2/3)^L$ geometric ratio of the Cantor construction)
- [ ] Check: does the delay-polynomial class $\mathcal{A}_h^{(L)}$ give the
  same rate, or is there a gap between polynomial approximation and
  $\sigma$-algebra approximation on $\mathcal{C}$?

**Candidate tex home.** A worked example in §5 of Paper II (Cyclic vectors
and Stone space identification), after the reconstruction theorem and before
the Takens comparison paragraph — or as a stand-alone example environment
in §4.

---

## Example B — Paper II (Dynamics side)
### A Finite Markov Chain: Predictive Kernels Without Determinism

**Motivation.** The classical Koopman picture requires a deterministic
measure-preserving transformation. The predictive kernel framework handles
stochastic systems directly — the kernel is the transition matrix, derived
rather than assumed. This example shows the dynamics side of Paper II in its
most transparent possible setting.

**The construction.**

- State space: $X = \{1, \ldots, k\}$, $\mathcal{B} = 2^X$ (all subsets).
- Transformation: a **finite irreducible aperiodic Markov chain** with
  transition matrix $P = (p_{ij})$ and unique stationary measure $\mu$.
- Observable: $Q_t(x) = x$ (identity — observe the full state at each time).

**The predictive kernel.**

The predictive kernel $\Pi_Q(i, \cdot) = P(i, \cdot)$ is the $i$-th row of
$P$ — the conditional distribution of the next state given the current state.
This is derived, not assumed: it is the unique Markov kernel satisfying the
defining equation of $\Pi_Q$ with respect to the stationary joint
distribution $\mu \otimes P$.

**Chapman-Kolmogorov.**

The kernels $\{\Pi_t\}$ compose as $\Pi_{t+s} = \Pi_t \star \Pi_s$
(matrix multiplication). This is Chapman-Kolmogorov, derived from temporal
coherence. The Markov semigroup $\{K_t\}$ acts on $L^2(\mu)$ as
$K_t f(i) = \sum_j P^t_{ij} f(j)$ — the standard Markov operator.

**Koopman-Perron duality.**

The Koopman-Perron duality $\int K_t g\, d\mu = \int g\, d(\mu \star \Pi_t)$
reduces to $\mu^\top P^t g = \mu^\top g$ for the stationary measure — a
tautology, confirming the framework recovers the classical picture exactly.

**CE in this setting.**

CE is automatically satisfied: irreducibility ensures no mass is lost to
transient states or absorbing subsets. The stationary measure $\mu$ is
the unique $\sigma$-additive probability measure the framework produces.

**Reconstruction.**

$\mathcal{O}_h = \mathcal{B}(X)$ iff the observable $h : X \to \mathbb{R}$
separates states — $h(i) \neq h(j)$ for $i \neq j$. This is a purely
algebraic condition on $h$, independent of $P$.

**What needs verification.**

- [ ] Write out the query system axioms explicitly for the Markov chain setting
- [ ] Confirm CE reduces to irreducibility (or state the precise equivalence)
- [ ] Check whether aperiodicity is needed for CE or only for the stationary
  measure to be unique
- [ ] State the reconstruction condition precisely: does $h$ separating states
  suffice, or is something about the orbit $\{h \circ T^n\}$ needed?

**Candidate tex home.** A worked example in §2 or §3 of Paper II (Prediction
and minimal predictive state / Dynamics and duality), illustrating the
predictive kernel construction in the finite stochastic case.

---

## Example D — Paper III (reserved)
### Oracle-Free Reconstruction Certification: Numerical Study

**Motivation.** The elbow stopping rule $\hat{L}^*$ certifies reconstruction
from finite data without knowing the mixing rate, lag, smoothness index, or
dimension. This example would demonstrate that concretely against a naive
approach (e.g. AIC, cross-validation, or fixed-lag) that requires oracle
inputs or fails to certify.

**Status.** Reserved pending empirical work. Candidate systems:
- Lorenz attractor (chaotic, known ground truth for reconstruction)
- Logistic map at various parameter values (varying mixing rates)
- A system where the naive approach picks the wrong $L$

**Pipeline when ready.**
1. Simulate time series
2. Compute $\hat{\delta}(L, n)$ for increasing $L$
3. Apply elbow rule, record $\hat{L}^*$
4. Compare against oracle lag and naive methods
5. Report convergence rate empirically

---

## Integration workflow (all examples)

1. **Sketch** (this document) — done above
2. **Verification** — formal proof (A, B, C) or simulation (D)
3. **TeX draft** — draft example/remark environment in isolation
4. **Integration** — insert into relevant paper body, compile, check flow
5. **Commit**
