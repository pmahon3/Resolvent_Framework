# Categorical Foundations: The Classical Picture and Its Inversion

*Working note — 2026-03-19*

---

## Motivation

The Observable Dynamics Program inverts the classical foundational order of probability
theory. The classical picture assumes a probability space and derives observations from it.
The program derives a probability space from the coherence of observations. This note
sketches both pictures in category-theoretic language to make the inversion precise and
to identify the open problems as categorical questions.

The goal is *route-finding*: not to formalize everything categorically, but to use the
categorical language to make visible what structure the classical picture assumes, where
exactly that assumption lives, and what the program is asking in its place.

---

## The classical picture in Meas

Let **Meas** be the category of measurable spaces and measurable functions.

**Step 1 — Sample space.** Start with $(X, \mathcal{X}) \in$ **Meas**. This is posited as
a complete description of all possible states of the world. It precedes any observation.

**Step 2 — The Giry monad.** The functor $\mathcal{P} :$ **Meas** $\to$ **Meas** sends
each measurable space to its space of probability measures, with the evaluation
$\sigma$-algebra. This is a monad with:
- Unit $\eta_X : X \to \mathcal{P}(X)$, $\quad x \mapsto \delta_x$ (Dirac measure)
- Multiplication $\mu_X : \mathcal{P}(\mathcal{P}(X)) \to \mathcal{P}(X)$, $\quad$
  (integration: $\mu_X(\Lambda)(A) = \int \nu(A)\, \Lambda(d\nu)$)

**Step 3 — Choosing a measure.** A probability space is a choice of monad algebra:
a measurable map $\mu : 1 \to \mathcal{P}(X)$ — a point in $\mathcal{P}(X)$. This is
a *free choice*, not forced by anything in the structure of $X$. This is the step that
the program defers.

**Step 4 — Random variables and pushforwards.** A measurable map $f : X \to Y$ induces
$\mathcal{P}(f) : \mathcal{P}(X) \to \mathcal{P}(Y)$ by pushforward. This is the
functorial action of $\mathcal{P}$.

**Step 5 — The Kleisli category.** The Kleisli category $\text{Kl}(\mathcal{P})$ of the
Giry monad has:
- Objects: measurable spaces
- Morphisms $X \to Y$: Markov kernels $K : X \to \mathcal{P}(Y)$
- Composition: $\int K(x, \cdot)\, L(y, \cdot)\, dx$ (Chapman-Kolmogorov)

This is the natural home of stochastic processes. Deterministic maps embed into
$\text{Kl}(\mathcal{P})$ via the unit $\eta$.

**Step 6 — Projective systems and Kolmogorov.** A compatible family of marginals
$\{\nu_i\}$ is a diagram in $\text{Kl}(\mathcal{P})$. The Kolmogorov extension theorem
says this diagram has a limit (the global measure $P$) in **Meas** when the spaces are
Polish. The assumed measure from Step 3 is what this limit produces — or equivalently,
the diagram determines the algebra structure that Step 3 assumed.

---

## Where the assumption lives

The assumed measure appears at **Step 3** as a choice of monad algebra structure. It is:

- **Not forced** by the measurable structure of $X$
- **Not forced** by the diagram of compatible marginals alone (without topological hypotheses)
- A **free parameter** of the construction

Everything downstream — pushforwards, kernels, marginals, stochastic processes — is
just functoriality applied to this free choice. The classical picture is therefore
**algebra-first**: you choose the algebra, then derive its consequences.

---

## The program's inversion

The Observable Dynamics Program asks: **can the monad algebra be derived from the
diagram rather than assumed?**

Concretely:

- A **query system** $(\mathcal{Q}, \preceq)$ is a diagram in $\text{Kl}(\mathcal{P})$:
  objects are queries $Q_i$ (measurable spaces $O_i$), morphisms are the compatible
  marginal kernels $\pi_{ij} : O_j \to \mathcal{P}(O_i)$ (or in the deterministic
  refinement case, measurable maps that factor through $\eta$).

- **Compatible marginals** $\{\nu_i\}$ are a *cocone* over this diagram in
  $\text{Kl}(\mathcal{P})$: each $\nu_i \in \mathcal{P}(O_i)$ is consistent with the
  morphisms.

- The **Observational Extension Theorem** (Paper 1) says this cocone has a canonical
  apex — a probability measure $P$ on $\Omega = \varprojlim O_i$ — under the hypotheses
  of sequential upper-directedness and realizability. This apex is the monad algebra
  structure that the classical picture assumed for free.

In categorical terms: **the forgetful functor from probability spaces to compatible
marginal systems has a left adjoint** (under appropriate hypotheses). The extension
theorem constructs this left adjoint. The philosophical content is that the monad algebra
is *initial* among algebras compatible with the observed structure, not freely chosen.

---

## The Merleau-Ponty correspondence

The categorical picture makes the phenomenological structure precise:

| Classical (Cartesian) | Program (Phenomenological) |
|---|---|
| Probability space assumed as ground | Probability space derived from coherence |
| Monad algebra freely chosen | Monad algebra forced by diagram |
| Observations are projections of the whole | The whole is constituted by coherence of parts |
| View from nowhere | View from the horizon of queries |
| Algebra-first | Diagram-first |

The Kleisli category is a world of *transitions* and *relations* — morphisms are primary,
objects secondary. This is closer to the phenomenological picture where experience is
fundamentally relational (intentional) rather than a collection of static facts.

The monad multiplication $\mu_X : \mathcal{P}(\mathcal{P}(X)) \to \mathcal{P}(X)$ —
collapsing uncertain beliefs about distributions to a single distribution — is classically
a free choice (a prior). The program asks whether the query structure forces this collapse
without a free choice. That is the categorical form of asking whether probability is
query-primitive rather than measure-primitive.

---

## The open problems as categorical questions

**Conjecture 2 (σ-additivity)** asks: what structure on the diagram in
$\text{Kl}(\mathcal{P})$ is sufficient to force the colimit/limit to exist without
Polish/tightness hypotheses? Categorically: under what conditions on a diagram in
$\text{Kl}(\mathcal{P})$ does a canonical monad algebra exist?

**Stopping Point 1 (measurability)** asks: can the objects of the diagram (the measurable
spaces $O_i$) themselves be derived from something more primitive? Categorically: is
there a category more primitive than **Meas** — perhaps of *topological spaces* or
*domains* or *locales* — whose image in **Meas** under a forgetful functor gives the
right objects? This would correspond to deriving $\sigma$-algebras from discriminative
capacity.

**Realizability (Stopping Point 3)** asks: when does the limit $\Omega = \varprojlim O_i$
have surjective projections? Categorically: when is the limit computed in **Meas**
rather than in a subcategory?

**The bridge to computation** (Paper 4 / `observational_probability.tex`) is: the delay
query system is a specific diagram in $\text{Kl}(\mathcal{P})$ built from the shift
maps on $X^{\mathbb{Z}}$. The minimal predictive query $Q_*$ is the image of the
cocone apex under the Giry functor restricted to the predictive sub-diagram. The
Rose condition is the condition that two diagrams are isomorphic in $\text{Kl}(\mathcal{P})$.

---

## Next steps

1. **Make the query system precise as a diagram in $\text{Kl}(\mathcal{P})$.** The
   refinement maps are currently deterministic (measurable functions), which means they
   factor through $\eta$. Are there natural query systems where the refinement maps are
   genuinely stochastic (full Markov kernels)? This would be the fully general
   $\text{Kl}(\mathcal{P})$ picture.

2. **State the extension theorem as an adjunction.** The left adjoint to the forgetful
   functor from probability spaces to compatible marginal systems is the extension
   construction. Making this adjunction precise would give a clean categorical statement
   of Paper 1's main theorem.

3. **Identify the Giry monad algebra structure in Paper 2.** The minimal predictive query
   $Q_* : \Omega \to \mathcal{P}(O_F)$ lands in $\mathcal{P}(O_F)$ — the Giry monad
   applied to the future observable space. The predictive operator $K_t$ is then a
   morphism in $\text{Kl}(\mathcal{P})$. The semigroup property is composition in
   $\text{Kl}(\mathcal{P})$.

4. **Stopping Point 1 via sheaf theory or locale theory.** The derivation of measurable
   structure from primitive discriminability might be expressible as a sheaf condition —
   the $\sigma$-algebra is the sheaf of reportable distinctions on a suitable site.

5. **Conjecture 2 as a cocompleteness condition.** Under what conditions is
   $\text{Kl}(\mathcal{P})$ cocomplete enough to guarantee the existence of the colimit?
   This might connect to Radon measures and tightness via the categorical notion of
   *compactness* in the relevant diagram category.

---

*This note is exploratory. The categorical language is being used for route-finding —
to make visible what the classical construction assumes and where the program's arguments
need to go — not as a commitment to full categorical formalization.*
