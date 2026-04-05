# Observable Dynamics Program — Overview

## The Central Question

When an observer makes structured observations of a system — querying it at
increasing levels of refinement, recording outcomes, building a picture of the world
through measurement — what does coherence require of them?

The program shows that coherence, pursued to its conclusion, requires probability,
dynamics, and reconstruction. Not as additional assumptions, but as what the
structure of observation already contains.

---

## The Three Papers

### Paper I — Probability from Observation

**What it shows:** A coherent family of observations determines a unique probability
measure on the observable σ-algebra.

**The argument has three routes, each illuminating a different facet:**

1. **Discriminability route** (Papers −1/0 consolidated): Bounded discriminability
   forces the observable distinctions to have σ-algebraic structure. Collective
   exhaustion (CE) — the condition that mass does not persist in events the completed
   observation sees as empty — is the irreducible condition that bridges structural
   coherence and probability. CE cannot be derived from any structural condition; it
   is a commitment the observer makes about the infinite, not a consequence of finite
   consistency. Given CE, compatible marginals extend uniquely to a global measure via
   Carathéodory.

2. **Stone duality route** (Paper 0′): The same extension theorem, approached from
   the other direction. Finite additivity on the cylinder algebra, combined with the
   compactness of the Stone space, yields σ-additivity without assuming it. CE
   reappears here not as an algebraic condition but as a support condition: the measure
   concentrates on the principal ultrafilters — on the image of the sample space inside
   its Stone compactification. The two routes illuminate the same theorem from opposite
   sides.

3. **The bridge**: The Stone space of the observable algebra is the natural compact
   completion of the sample space. This observation connects Paper I to Paper III:
   when reconstruction holds, the Stone space *is* the state space.

**Lean formalization:** `DiscriminabilityFoundations.lean`, `QuerySystem.lean`,
`StoneDualityExtension.lean`

**LaTeX:** `papers/paper_i/paper_i.tex` (integrated draft, 13 pages)

---

### Paper II — Dynamics from Probability

**What it shows:** Given a probability measure on the observable σ-algebra, the
dynamics of the system — the temporal evolution of predictive states — is uniquely
determined.

**The argument:**

The Koopman operator $U_T$ acts on $L^2(\Omega, P)$ by composition with the dynamics.
The predictive content of any measurable map $Q : \Omega \to \alpha$ is read off from
the spectral structure of $U_T$: the minimal predictive state map $Q_*$ is not chosen
by the observer but determined by $(Q, P)$. The semigroup law $K_{t+s} = K_t \circ K_s$
is derived, not assumed — temporal coherence of prediction follows from the same
observable compatibility that determined $P$.

Koopman-Perron duality: the observable-layer dynamics ($K_t$, acting on predictive
states) and the state-space dynamics (Koopman operator $U_T$, acting on functions) are
dual under $L^2(P)$. Neither is primary.

**Lean formalization:** `PredictiveState.lean`, `PredictiveOperators.lean`

---

### Paper III — Reconstruction from Observation

**What it shows:** Under a spectral condition on the observation function, the
observer can reconstruct the full state space from time-delayed measurements alone.
The Stone space of the observable algebra is the state space.

**The argument:**

For a dynamical system $(X, T, \mu)$ with observation $h \in L^\infty(X, \mu)$, the
time-delay Boolean algebras $\{B_S\}$ (indexed by finite sets of times $S$) form a
directed system. By Paper I's Stone duality route, the compatible charges on $\{B_S\}$
extend to a σ-additive measure on $\sigma(B_\infty)$ — the observable algebra of all
finite delay-coordinate information.

**Reconstruction theorem:** $\sigma(B_\infty) = \mathcal{B}(X)$ mod $\mu$ if and only
if $h$ is a *cyclic vector* for the Koopman operator $U_T$ — i.e., the orbit
$\{h \circ T^n : n \in \mathbb{Z}\}$ spans a dense subspace of $L^2(X, \mu)$.

This is a purely spectral condition. When it holds, the map
$x \mapsto (h(T^n x))_{n \in \mathbb{Z}}$ is a measure-theoretic embedding
$X \hookrightarrow \mathbb{R}^\mathbb{Z}$, factoring through the inverse limit of
Stone spaces. The Stone space of the observable algebra is the state space.

**Relation to classical Takens:** The classical Takens theorem (1981) requires a
smooth system on a compact $d$-manifold and gives a diffeomorphic embedding using
$2d+1$ delays. The present result requires only measurability, uses all finite delays,
and replaces the dimension count with the cyclic vector condition. Genericity on compact
manifolds recovers the classical result without differentiability hypotheses.

**Lean formalization:** `DelayEmbedding.lean` (partial)

---

## The Through-Line

Each paper takes the output of the previous as input:

```
Structured observations
    → [Paper I]  → probability measure P on (Ω, σ(CylGen))
    → [Paper II] → dynamics: Koopman operator U_T, semigroup K_t
    → [Paper III]→ reconstruction: state space X ≅ St(observable algebra)
```

The Stone duality route in Paper I anticipates Paper III: the Stone space that appears
as a technical tool in the measure extension argument reappears at the end as the
object being reconstructed. The program begins and ends with the same compact space,
seen from different angles.

---

## What Each Paper Needs

| Paper | Mathematical status | Lean status | LaTeX status | Next action |
|-------|--------------------|-----------|----|---|
| I | All routes proved; bridge written | `QuerySystem.lean` ✅; `DiscriminabilityFoundations.lean` 3 sorrys (Mathlib gaps); `StoneDualityExtension.lean` ✅ (2 intentional Mathlib-gap sorrys) | **First draft done** — `papers/paper_i/`, 13 pages | Revise and hone |
| II | Core results proved | `PredictiveState.lean` ✅; `PredictiveOperators.lean` ✅ | **First draft done** — `papers/paper_ii/`, 8 pages | Revise and hone |
| III | Delay structure proved; cyclic vector theorem open | `DelayEmbedding.lean` 1 sorry (open mathematics) | Not started | Develop cyclic vector theorem |

---

## Task List (as of 2026-04-04)

Ordered by priority. Cross off as completed.

### Done
- [x] **Revise Paper A introduction and abstract** — Done 2026-04-02.
- [x] **Integrate Papers −1 and 0 into Paper I** — Done 2026-04-02. First draft at
  `papers/paper_i/` (13 pages, compiles cleanly). Plan at
  `notes/paper_i_integration_plan.md`.
- [x] **Revise Paper I draft** — Done 2026-04-02. Fixed: §3 notation inconsistency
  (abstract $\mathcal{E}_i$/$\ell_i$ vs query-system $B_i$/$\mu_i$) with transition
  paragraph; $\pi_{ij}^{-1}$ direction error in CE definition and sp1 proof; Stone
  theorem missing common coarsenings hypothesis; uniqueness argument in Stone theorem
  cleaned up; coincidence paragraph tightened; density claim in §6.3 made precise.
- [x] **Write Paper II (LaTeX)** — Done 2026-04-02. First draft at `papers/paper_ii/`
  (8 pages, compiles cleanly). Sections: setup, predictive kernel, minimal predictive
  state map, factorization, semigroup, Koopman-Perron duality, deterministic
  specialization, observable dynamical system, bridge to Paper III.
- [x] **Strip query system vocabulary from Papers I and II** — Done 2026-04-03.
  Paper II: Q and F are plain measurable maps throughout; "minimal predictive query"
  renamed "minimal predictive state map". Paper I abstract: formal tuple removed,
  structure described in one sentence; vestigial Paper 0 notation remark removed.

### Done (continued)
- [x] **Lean formalization of Paper I Stone route** — Done 2026-04-04.
  `StoneDualityExtension.lean` builds cleanly on `stone-duality-extension` branch.
  Task 0′-A/C/E proved; B/D intentional sorrys (Mathlib gaps: clopen charge → Borel
  measure; Choksi's theorem). `stone_agrees_with_caratheodory` proved with no sorry.

### Current priorities
1. **Revise Papers I and II** — both first drafts exist; need sharpening before
   submission. Paper I: tighten the bridge section and Stone route narrative now that
   the Lean formalization is complete. Paper II: sharpen the Koopman-Perron duality
   section.

2. **Develop cyclic vector theorem for Paper III** — the one place where mathematics
   is still genuinely open. Delay embedding structure is proved (`DelayEmbedding.lean`);
   the Takens generalization needs the cyclic vector characterization written properly.

3. **Write Paper III (LaTeX)** — once the cyclic vector theorem is settled.

### Long term / deferred
- `DiscriminabilityFoundations.lean` 3 sorrys — all Mathlib gaps (ultraproduct
  infrastructure); mathematics is correct, low priority.
- Paper IV — conceptual sketch only; not to be developed until Papers I–III complete.

---

---

### Paper IV — Topology from Observation (provisional)

**The question:** Can the topology of the state space be *derived* from the
query system and its charges, rather than assumed as input or inherited from
the Stone compactification?

**Seed idea:** In an ordinary Boolean cylinder refinement system, any two
distinct points are eventually and permanently separated (monotone observability
+ discriminability forces this). But when separation is *weighted by the
measure*, a third regime appears: pairs that are formally separated at every
level but whose separating events have vanishing measure. This is *vanishing
distinction* ($\asymp$), the proposed primitive for proto-nearness. The
conjecture is that CE (on the valuation side) and measure-weighted $\asymp$ (on
the separation side) are two faces of a single coherence condition — and that
topology emerges from the organized failure of stable separation rather than
being imposed from outside.

**Relation to Papers I–III:** Paper I constructs the Stone space
$\mathrm{St}(\mathcal{C})$ whose topology is generated by the clopen cylinder
sets. Paper III identifies that Stone space with the state space under the cyclic
vector condition. Paper IV asks whether the *relevant* topology on the state
space is the Stone topology, or something derived from the measure-weighted
separation structure. If the latter, the programme begins and ends with the
observer's distinctions — the topology, like the measure, would be something
the observer's query system already contains.

**Status:** Conceptual sketch only. Not to be developed until Papers I–III are
complete.

**Reference:** `notes/conceptual_sketches/philosophy/topology_from_vanishing_distinction.md`

---

## What Is Not in the Program

- Computational implementation (data-driven dynamics, EDMD, etc.) — this is a
  natural sequel but is treated as a separate project
- Infinite-dimensional state spaces beyond $L^2$ — deferred
- Non-stationary / non-ergodic generalizations — deferred
