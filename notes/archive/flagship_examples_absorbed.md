> **ARCHIVED 2026-04-29.** Examples A (Cantor set, Paper II §5) and C
> (Propositional query system, Paper I §3) are integrated into the papers.
> Example B (pedagogical dynamics) was not flagshipped. Example D (numerical,
> Paper III) remains reserved pending empirical work — see
> `notes/future/finite_sample/interaction/discrimination_direction.md` for the post-arXiv
> empirical direction.

---

# Flagship Examples — Structure from Observation

Three worked examples, one per paper, demonstrating the payoff of the
framework on problems that classical approaches handle poorly or not at all.
A fourth numerical example is reserved for Paper III pending empirical work.

Each example follows the same pipeline:
1. **Sketch** — the construction in prose, objects identified
2. **Verification** — formal proof or numerical simulation as appropriate
3. **Integration** — tex integration into the relevant paper once verified

---

## The profinite observational template

Examples A and C are technically analogous at a deep level. Both instantiate
the same underlying scheme:

> **Finite Boolean quotient observations → direct-limit algebra → Stone/inverse-limit
> completion → global object recovered from coherent finite prefixes.**

More precisely: in both examples the state (a possible world, or a point of
the Cantor set) is not primitive. What is primitive is a countable family of
sharp binary distinctions. At each finite stage only a finite prefix is
visible; the global object is the coherent completion of all finite prefixes —
the Stone space of the direct-limit Boolean algebra, equivalently the inverse
limit of the finite discrete quotient spaces.

This is a **profinite observational scheme**. Both examples are dual exemplars
of it, applied at different layers of the programme:

| | Example C | Example A |
|---|---|---|
| **Basic observables** | Propositional sentences $\phi_1, \phi_2, \ldots$ | Ternary digits of $x$ via delay orbit |
| **Finite stage** | Lindenbaum subalgebra of $\{\phi_1,\ldots,\phi_n\}$ | Cylinder $\sigma$-algebra at lag $L$ |
| **Global point** | Complete consistent extension / ultrafilter | Coherent digit sequence / point of $\mathcal{C}$ |
| **Clopen sets** | Cylinder sets over finite propositional prefixes | Cantor cylinder sets at generation $L$ |
| **Full space** | Stone space of Lindenbaum algebra | Cantor set as inverse limit |
| **Layer** | Probability / admissibility (Part I) | Reconstruction / state-space (Part II) |
| **Key theorem** | CE → σ-additive measure on possible worlds | O_h = B mod μ → state-space recovery |

**Why the analogy holds.** The Stone space of any countable atomless Boolean
algebra is homeomorphic to the Cantor space. If the Lindenbaum algebra of the
propositional theory is countable and atomless, its Stone space is
Cantor-like. Example A is explicitly Cantor-coded from the start. So C is the
logical/semantic realisation of a Cantor-type Stone space; A is the
dynamical/geometric realisation of the same.

**Where the analogy breaks.**
1. *Dynamics*: A has a transformation $T$ and a reconstruction question tied
   to orbit structure. C is static.
2. *Admissibility*: C is about CE and the passage from finite additivity to
   σ-additivity. A is about whether the observable algebra recovers the full
   Borel structure. The key theorems are different.

**Consequence for presentation.** Examples A and C should be explicitly
cross-referenced so a reader who sees C in Paper I already has the profinite
template in mind when they encounter A in Paper II. In the combined document,
a brief framing note can name the template once before the first example
appears. In standalone papers, each carries a one-sentence pointer to the
other. The drafting goal is: build both examples toward this unified
presentation from the start.

---

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

**Query system axiom verification.**

- **Index set and outcome spaces.** Take $\iota = \mathbb{N}$ ordered by $\leq$.
  At level $n$, the outcome space $O_n$ is the set of atoms of
  $\mathrm{Lind}(\phi_1,\ldots,\phi_n)$ — equivalently, the set of maximal
  consistent truth-value assignments to $\{\phi_1,\ldots,\phi_n\}$ (those
  consistent with $T$). Each $O_n$ is finite (at most $2^n$ atoms).

- **Refinement maps.** For $n \leq m$, the map $\pi_{nm} : O_m \to O_n$ sends
  a truth-value assignment to $\{\phi_1,\ldots,\phi_m\}$ to its restriction to
  $\{\phi_1,\ldots,\phi_n\}$. This is surjective (by $T$-consistency) and the
  refinement maps compose correctly.

- **Surjective Evaluation.** The instantiation $\Omega$ = space of complete
  consistent extensions of $T$ (ultrafilters of $\mathrm{Lind}(\mathcal{L})$).
  Every atom of $\mathrm{Lind}(\phi_1,\ldots,\phi_n)$ is extended to a complete
  consistent extension by Zorn's lemma applied to $T$, so $\mathrm{eval}_n :
  \Omega \to O_n$ is surjective. ✓

- **Directed refinements.** The index $\mathbb{N}$ with $\leq$ admits sequential
  common refinements (upper bounds) trivially. Common coarsenings: $\mathbb{N}$
  is totally ordered, so any $n, m$ have lower bound $\min(n,m)$. ✓

- **Discriminability / separating points.** Two distinct $\omega, \omega' \in
  \Omega$ are distinct complete extensions, so they disagree on some $\phi_k$,
  and hence $\mathrm{eval}_k(\omega) \neq \mathrm{eval}_k(\omega')$. ✓

*All query system axioms are satisfied.*

**CE in this setting — precise formulation.**

Each $\mathcal{E}_n = \mathrm{Lind}(\phi_1,\ldots,\phi_n)$ is a *finite* Boolean
algebra, so any decreasing sequence within a single level stabilizes. CE is
therefore trivially satisfied for sequences within a fixed level.

The substantive condition arises from the cylinder algebra $\mathcal{C}$ across
levels. A decreasing sequence of cylinders $\mathrm{Cyl}(n_k, A_k)$ with
$A_k \in \mathcal{E}_{n_k}$ and $n_k \nearrow \infty$ has empty intersection in
$\Omega$ iff no complete consistent extension satisfies all the $A_k$. Writing
$\alpha_k$ for a representative formula of the equivalence class $A_k$:

> **Infinitary inconsistency:** $T \cup \{\alpha_1, \alpha_2, \ldots\}$ is
> inconsistent (no world satisfies all $\alpha_k$).

CE requires: if the $\alpha_k$ are jointly unsatisfiable over $T$, then
$\nu_{n_k}(\alpha_k) \to 0$.

Equivalently: **the probability charge family is tight on the Stone space** —
no persistent mass can concentrate on events that collectively vanish. In
topological terms, CE is exactly inner regularity of $\hat{\nu}$ with respect to
the compact open sets (cylinder sets) of the Stone space
$\mathrm{St}(\mathrm{Lind}(\mathcal{L}))$.

**CE is not ω-consistency — they are orthogonal.**

ω-consistency is a condition on an *arithmetic theory* $T$ (not $\mathcal{L}$):
$T$ is ω-consistent if it does not prove $\exists x \neg P(x)$ while separately
proving $P(\bar{n})$ for every numeral $\bar{n}$. This is a syntactic condition
on first-order arithmetic theories, and has no direct analogue in propositional
probability logic (propositional logic has no quantifiers, no numerals, no
natural-number structure).

CE is a condition on the *charge family* $\{\nu_n\}$, not on $T$. It does not
say anything about what $T$ proves. A consistent propositional theory $T$
can be held fixed while the charge family $\{\nu_n\}$ satisfies or fails CE
independently.

The *closest* syntactic analogue: CE is to probability logic what
$\omega$-completeness is to arithmetic (every instance provable implies the
universal statement) — both are "no mass escapes to infinity" conditions —
but the exact structural parallel is to **tightness**, not ω-consistency.

**Precise connection to tightness.**

Let $S = \mathrm{St}(\mathrm{Lind}(\mathcal{L}))$ be the Stone space (= space
of complete consistent extensions, with cylinder sets as a basis of clopen sets).
The charge family $\{\nu_n\}$ determines a Baire measure $\hat{\nu}$ on $S$ via
the Stone route. Then:

> **CE ⟺ $\hat{\nu}$ is supported on $\mathrm{pure}(\Omega)$
> ⟺ $\hat{\nu}$ is tight on $S$
> ⟺ the purely finitely additive part of the charge vanishes.**

In the propositional setting, $\mathrm{pure}(\Omega)$ = the set of principal
ultrafilters = the set of complete consistent extensions themselves (since
$\Omega$ embeds into $S$ as the principal ultrafilters). CE says: no mass lives
on non-principal ultrafilters, i.e., no mass "escapes to the boundary" of the
compactification.

This is exactly the **Gaifman/Scott-Krauss tightness condition**.

**Connection to classical results — attribution and comparison.**

**Attribution note (important).** The label "Gaifman/Scott-Krauss theorem" used
earlier in these notes is not well-sourced and should not appear in the paper.
Specifically:

- Gaifman (1964, *Israel J. Math.*) addresses coherent probabilities on
  **first-order** quantifier-free sentences — a different setting.
- Scott–Krauss (1966) assigns probabilities to logical formulas but does not
  appear to state the propositional extension theorem in the form we need.
- The companion note (§1) cites Hoover (1978), Keisler (1985), and
  Fagin–Halpern–Megiddo (1990) as treating non-axiomatizability of σ-additivity
  as background knowledge — these are the actual probability logic sources in the
  bib. The extension theorem itself (coherent charge extends to σ-additive measure
  on complete extensions iff tight) is implicit in this literature but not stated
  as a single theorem with a single owner.

**The correct framing for the paper.** Rather than attributing to Gaifman/Scott-Krauss
the example should be framed as follows:

> The extension theorem recovered is a propositional instance of a standard
> result in probability logic — that a coherent charge on a propositional language
> extends to a σ-additive measure on the space of complete consistent extensions
> exactly when it is tight on that space (see Hoover 1978, Keisler 1985). In the
> framework, this is a special case of the CE Characterisation Theorem: CE is the
> admissibility condition, identified precisely and shown to be non-derivable.

The payoff of the example is not "we recover Theorem X due to Y." It is:

> **CE reclassifies a classical condition.** What the probability logic literature
> imposes as a standing hypothesis (tightness / coherence on complete extensions)
> or derives by a compactness argument is here named, isolated as the sole
> admissibility condition, and shown to be logically unavoidable.

This is the stronger and more accurate claim.

**The framework result, spelled out.**

The CE Characterisation Theorem (Theorem 4.3 of Paper I) specialises as follows
in the propositional setting:

> **Propositional Extension Theorem.** Let $\mathcal{L}$ be a countable
> propositional language, $T$ a consistent theory, and $\{\nu_n\}$ a compatible
> family of probability charges on the finite Lindenbaum subalgebras
> $\{\mathrm{Lind}(\phi_1,\ldots,\phi_n)\}$. Then $\{\nu_n\}$ extends to a unique
> $\sigma$-additive probability measure on $(\Omega, \sigma(\mathcal{C}))$ — where
> $\Omega$ is the space of complete consistent extensions of $T$ — if and only if
> the family satisfies CE.

Under the Stone identification, $(\Omega, \sigma(\mathcal{C}))$ is identified with
the space of complete consistent extensions equipped with the Baire $\sigma$-algebra
generated by the cylinder sets (= the clopen sets of $\mathrm{St}(\mathrm{Lind}(\mathcal{L}))$
restricted to the principal ultrafilters). CE is the tightness condition.

**One subtlety about compactness.** The Stone space $S =
\mathrm{St}(\mathrm{Lind}(\mathcal{L}))$ is compact, so every regular Borel
measure on $S$ is automatically tight. The issue is that a finitely additive
charge $\nu$ on $\mathcal{C}$ does *not* automatically correspond to a regular
Borel measure on $S$: it may have a non-zero purely finitely additive component
$\nu_p$, which sits on non-principal ultrafilters and cannot be captured by any
regular Borel measure on $\Omega$. CE rules out $\nu_p \neq 0$. Once CE holds,
$\nu$ is $\sigma$-additive, the corresponding Borel measure on $S$ is regular,
and compactness gives tightness for free — but CE is logically prior to that
conclusion, not a consequence of it. Compactness of $S$ cannot substitute for CE,
because compactness operates on the extension $S$, not on the canonical
instantiation $\Omega$.

**Principal ultrafilters — a precision note for the paper.** The notes have
written "$\mathrm{pure}(\Omega)$ = the set of principal ultrafilters = the set of
complete consistent extensions." In paper prose, this identification needs one
careful sentence: $\Omega$ embeds into $S$ via $\omega \mapsto \{A \in \mathcal{C}
: \omega \in A\}$, sending each realised state to its principal ultrafilter; the
image of this embedding is $\mathrm{pure}(\Omega)$. CE says the measure is
supported on this image — i.e., on realised states, not ideal limit points. The
identification is then a homeomorphism from $\Omega$ (with the subspace topology
from $\sigma(\mathcal{C})$) onto $\mathrm{pure}(\Omega) \subset S$.

**What needs verification.**

- [x] Confirm Lindenbaum construction fits query system axioms — done above ✓
- [x] CE explicit form in propositional setting — done above: cross-level
  cylinder sequences, joint unsatisfiability, tightness ✓
- [x] CE vs. ω-consistency — orthogonal; CE is a condition on the charge family,
  not the theory ✓
- [x] Attribution — "Gaifman/Scott-Krauss" dropped; correct framing is Hoover
  (1978) / Keisler (1985) for the background; our contribution is naming CE as
  the admissibility condition and proving non-derivability ✓
- [ ] **Remaining:** verify Hoover (1978) §2–3 states something that our theorem
  subsumes, or confirm the extension theorem is genuinely implicit rather than
  explicit in that literature — this determines whether the paper says "recovers"
  or "supplies an explicit proof of" the propositional extension result.

**Candidate tex home.** End of §4 (Collective Exhaustion), after the metatheorem
subsection (§4.4), before §5 (Stone realization). This positions the example to
ground the abstract CE machinery in a concrete logical setting immediately after
the non-derivability result, and before the Stone route is developed. The Stone
identification then feels earned when it arrives in §5.

---

## Example A — Paper II (Reconstruction side)
### The Cantor Set: Reconstruction Without Smoothness

**Motivation.** Takens's theorem requires a $C^2$ diffeomorphism on a smooth
compact manifold and gives a delay embedding bound $2d+1$ where $d$ is the
manifold dimension. The Cantor set violates every hypothesis: it is not a
manifold, it has no smooth structure, and its Hausdorff dimension
$\log 2/\log 3 \approx 0.63$ is not an integer. Takens is simply inapplicable —
not merely non-optimal but without a domain of application here. The
reconstruction theorem of Paper II works anyway, because it is built on
measurable observable algebras rather than differential geometry.

---

### Paper-ready form

**Move 1 — Setup.**

- State space: $\mathcal{C}$ (middle-thirds Cantor set), with the **Cantor
  measure** $\mu_\mathcal{C}$ — the pushforward of the fair-coin product
  measure $\nu = (\frac{1}{2}\delta_0 + \frac{1}{2}\delta_2)^\mathbb{N}$ under
  the ternary coding map $\pi(d_1,d_2,\ldots) = \sum_{k \geq 1} d_k/3^k$.
- Transformation: the **shift map** $S : \mathcal{C} \to \mathcal{C}$,
  \[
    S(x) = \begin{cases} 3x & x \in \mathcal{C} \cap [0,\tfrac{1}{3}], \\ 3x-2 & x \in \mathcal{C} \cap [\tfrac{2}{3},1]. \end{cases}
  \]
  The system $(\mathcal{C}, \mu_\mathcal{C}, S)$ is measurably conjugate to
  the Bernoulli shift $(\{0,2\}^\mathbb{N}, \nu, \sigma)$ via $\pi$; in
  particular $S$ is $\mu_\mathcal{C}$-invariant and ergodic.
- Observable: $h(x) = x$.

**Move 2 — Symbolic interpretation.**

For $x = \pi(d_1,d_2,\ldots)$, the shift gives $S^n x = \pi(d_{n+1},d_{n+2},\ldots)$.
Since every point of $\mathcal{C}$ lies in $[0,\frac{1}{3}] \cup [\frac{2}{3},1]$,
\[
  d_{n+1} = 0 \iff S^n x \in \bigl[0,\tfrac{1}{3}\bigr], \qquad
  d_{n+1} = 2 \iff S^n x \in \bigl[\tfrac{2}{3},1\bigr],
\]
so $h \circ S^n$ recovers the $(n+1)$-st ternary digit of $x$. The delay
vector $\Phi_h^{(L)}(x) = (x, Sx, \ldots, S^L x)$ reads off digits
$d_1,\ldots,d_{L+1}$. Its fibres are exactly the generation-$(L+1)$ cylinder
sets
\[
  F_z = \{x \in \mathcal{C} : d_k(x) = z_k,\; 1 \leq k \leq L+1\},
  \quad z \in \{0,2\}^{L+1},
\]
each carrying $\mu_\mathcal{C}(F_z) = 2^{-(L+1)}$, so
\[
  \mathcal{O}_h^{(L)} = \sigma(\Phi_h^{(L)}) = \sigma\{F_z : z \in \{0,2\}^{L+1}\}.
\]

**Move 3 — Reconstruction.**

Since $\mu_\mathcal{C}$-a.e. pair of distinct points differs at some finite
digit, the algebras $\mathcal{O}_h^{(L)}$ separate points $\mu_\mathcal{C}$-a.e.
as $L \to \infty$, giving
\[
  \mathcal{O}_h = \sigma\!\Bigl(\bigcup_{L \geq 0} \mathcal{O}_h^{(L)}\Bigr)
  = \mathcal{B}(\mathcal{C}) \quad \text{mod } \mu_\mathcal{C}.
\]
Reconstruction holds, and the finite-lag observable algebras refine to the
full Borel structure at exponential rate.

**Move 4 — Contrast with Takens.**

$\mathcal{C}$ is not a smooth manifold: it is compact and zero-dimensional,
with Hausdorff dimension $\log 2/\log 3 \approx 0.63$. The differential-geometric
hypotheses of Takens's theorem — $C^2$ ambient dynamics, integer dimension $d$,
embedding bound $2d+1$ — are unavailable before one even asks about regularity
of $S$. Takens has no domain of application here. The reconstruction theorem
applies because it requires only that the observable algebra be measurably
generated; smoothness plays no role.

**Candidate tex home.** End of §5 of Paper II (Cyclic vectors and Stone space
identification), after the Stone space identification proposition. The example
grounds the abstract reconstruction theorem in a concrete fractal setting where
the classical approach is simply inapplicable — not merely non-optimal but
without a domain of application.

---

## Example B — Paper II (Dynamics side)
### A Finite Markov Chain: Predictive Kernels in the Transparent Case

**Role.** Not a flagship. A **pedagogical dynamics example** for §3 of Paper II
(Dynamics and duality). Its job is to make the predictive kernel, Chapman-Kolmogorov,
and Koopman-Perron duality concrete in the finite stochastic case, where all the
abstract objects collapse to familiar matrix algebra. CE and reconstruction each
get one honest sentence — no more.

---

**Setup.**

- State space: $X = \{1, \ldots, k\}$, $\mathcal{B} = 2^X$.
- Dynamics: a finite irreducible Markov chain with transition matrix $P = (p_{ij})$
  and unique stationary measure $\mu$ ($\mu P = \mu$). Aperiodicity is not
  needed for any of the three structural claims below.
- Observable: full-state observation, $Q_t = X_t$ (equivalently $h = \mathrm{id}_X$).

**The three structural claims.**

**(i) Predictive kernel = transition matrix.**

The predictive kernel is $\Pi_h(i, \cdot) = P(i, \cdot)$ — the $i$-th row of $P$.
This is derived, not assumed: $\Pi_h$ is the unique Markov kernel satisfying
\[
  \mathbb{E}_\mu[f(X_1) \mid X_0 = i] = \sum_j p_{ij} f(j)
  \qquad \text{for all bounded } f.
\]

**(ii) Chapman-Kolmogorov = kernel composition = matrix multiplication.**

Temporal coherence gives $\Pi_h^{(t+s)} = \Pi_h^{(t)} \star \Pi_h^{(s)}$,
which is $P^{t+s} = P^t P^s$. The Markov semigroup acts on $L^2(\mu)$ as
$K_t f(i) = \sum_j p^t_{ij} f(j)$.

**(iii) Koopman-Perron duality = stationarity identity.**

\[
  \int K_t g\, d\mu = \int g\, d(\mu \star \Pi_h^{(t)})
  = \mu^\top P^t g = \mu^\top g,
\]
using $\mu P^t = \mu$. This is the stationary-measure identity: the duality
reduces exactly to the fixed-point property of $\mu$.

**CE and reconstruction — one sentence each.**

*CE:* In the finite-state setting every charge is automatically $\sigma$-additive,
so the admissibility issue does not arise.

*Reconstruction:*
\[
  \mathcal{O}_h = \sigma(h) = \mathcal{B}(X)
  \quad \text{iff} \quad h \text{ separates points of } X;
\]
for the identity observable this holds at lag $0$, independent of $P$.

**What aperiodicity is for.** Irreducibility + aperiodicity gives
$P^t \to \mathbf{1}\mu^\top$ as $t \to \infty$ (convergence to stationarity).
Needed only if the example illustrates long-run mixing; not needed for (i)–(iii).

**Candidate tex home.** §3 of Paper II (Dynamics and duality), as a short example
after the predictive kernel and Chapman-Kolmogorov definitions, before the general
Koopman-Perron duality theorem. Its job: show that in the finite stochastic case
all the abstract machinery collapses to matrix algebra the reader already knows.

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
