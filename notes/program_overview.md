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
`StoneDualityExtension.lean`, `TopologicalQuerySystem.lean` (Prokhorov route
infrastructure), `ProkhorovExtension.lean` (Prokhorov route main theorem),
`DelayEmbedding.lean` (delay query system instantiation)

**LaTeX:** `papers/paper_i/paper_i.tex` (revised draft, 13 pages)

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

**What it shows:** The observer can reconstruct the full state space from
time-delayed measurements alone — precisely when the observable distinctions
are complete. The Stone space of the observable algebra is the state space.

**The central theorem (corrected from earlier drafts):**

For a dynamical system $(X, \mathcal{B}, \mu)$ with $T$ measure-preserving and
$h \in L^\infty(X, \mu)$, define the *observable algebra*
$\mathcal{O}_h = \sigma(\{h \circ T^n : n \in \mathbb{Z}\})$.  The following are
equivalent:

1. $\mathcal{O}_h = \mathcal{B}(X)$ mod $\mu$  (observable distinctions are complete)
2. $\mathrm{alg}\{h \circ T^n : n \in \mathbb{Z}\}$ is dense in $L^2(X, \mu)$  (algebra density)
3. The delay map $\Phi_h : x \mapsto (h(T^n x))_{n \in \mathbb{Z}}$ is a
   measure-theoretic embedding $X \hookrightarrow \mathbb{R}^\mathbb{Z}$

This is the **reconstruction theorem**. It is a theorem about the Boolean algebra
of observable events, not about the spectral theory of $U_T$ directly. The
equivalence of (1) and (2) is the *density bridge*: the $L^2$-closure of the
observable algebra equals $L^2$ of the generated σ-algebra.

**The role of the cyclic vector condition:**

The *cyclic vector* condition — $\overline{\mathrm{span}}\{U_T^n h\} = L^2(X,\mu)$
— is a *sufficient* condition for reconstruction, not an equivalence. Cyclic implies
(1)–(3) because the linear span is contained in the algebra, so cyclicity forces
algebra density. But the converse fails: the algebra can be dense without the linear
span being dense (e.g. $h(x) = x$ under the doubling map on $[0,1]$).

The correct equivalence involving the cyclic vector lives one level up, in operator
algebra language: $h$ is cyclic for $U_T$ iff the von Neumann algebra
$\{U_T^n h\}''$ equals all of $L^\infty(X,\mu)$ as a maximal abelian subalgebra of
$\mathcal{B}(L^2)$ — i.e., iff $T$ has *simple $L^2$-spectrum* and $h$ is a spectral
generator. This is a remark connecting Papers II and III, not the main theorem.

**The Stone duality connection:**

This is where Papers I and III close the loop. The density bridge (1)⟺(2) is exactly
the algebraic side of Stone duality: the Boolean algebra $\mathcal{O}_h$ exhausts
$\mathcal{B}(X)$ iff $\mathrm{St}(\mathcal{O}_h) \cong X$ as measure spaces. The
Stone space that Paper I built as a technical device for measure extension is, under
the reconstruction condition, the state space itself. The programme begins with a
Stone compactification of the sample space and ends by identifying it with the system
being observed.

**Relation to classical Takens:** The classical Takens theorem (1981) requires a
smooth system on a compact $d$-manifold and gives a diffeomorphic embedding using
$2d+1$ delays. The present result requires only measurability, uses all finite delays,
and replaces the dimension count with the algebraic density condition. The role of
the dimension bound in Takens is to ensure the algebra generated by finitely many
delay coordinates already separates points; here that role is played by the density
condition on the infinite algebra. Genericity on compact manifolds recovers the
classical result without differentiability hypotheses.

**Lean formalization:** `DelayEmbedding.lean` (delay query system structure
proved; density bridge and reconstruction theorem not yet formalized)

---

## The Through-Line

Each paper takes the output of the previous as input:

```
Structured observations
    → [Paper I]   → probability measure P on (Ω, σ(CylGen))
                    Stone space St(C) as compact completion of Ω
    → [Paper II]  → dynamics: Koopman operator U_T, semigroup {K_t}
                    cyclic vector condition as spectral sufficient condition
    → [Paper III] → reconstruction: St(O_h) ≅ X when O_h = B(X) mod μ
                    density bridge closes the loop with Paper I
```

The three papers track the same duality from three angles:

- **Paper I** (Boolean / topological): the observable algebra $\mathcal{C}$ dualises
  via Stone to a compact space $\mathrm{St}(\mathcal{C})$. CE forces the measure to
  live on $\Omega \subset \mathrm{St}(\mathcal{C})$.

- **Paper II** (operator / spectral): the Koopman operator $U_T$ on $L^2$ encodes the
  dynamics. The cyclic vector condition — $\overline{\mathrm{span}}\{U_T^n h\} = L^2$
  — is a spectral condition implying reconstruction.

- **Paper III** (algebraic / measure-theoretic): the observable algebra
  $\mathcal{O}_h = \sigma(\{h \circ T^n\})$ exhausts $\mathcal{B}(X)$ iff
  $\mathrm{St}(\mathcal{O}_h) \cong X$. The density bridge connects the Boolean
  algebra level (Paper I) to the $L^2$ level (Paper II): algebra density in $L^2$
  iff $\sigma$-algebra generation.

The Stone space that Paper I built as a tool for measure extension is, under the
reconstruction condition, the state space being recovered. The programme begins with
the observer's distinctions and ends by showing those distinctions — when complete —
are the state space.

---

## What Each Paper Needs

| Paper | Mathematical status | Lean status | LaTeX status | Next action |
|-------|--------------------|-----------|----|---|
| I | All routes proved; bridge written | `QuerySystem.lean` ✅; `DiscriminabilityFoundations.lean` 3 sorrys (Mathlib gaps); `StoneDualityExtension.lean` ✅ (2 intentional Mathlib-gap sorrys); `TopologicalQuerySystem.lean` + `ProkhorovExtension.lean` ✅ (Prokhorov route) | **Revised** — `papers/paper_i/`, 13 pages | Submit |
| II | Core results proved | `PredictiveState.lean` ✅; `PredictiveOperators.lean` ✅ | **Revised** — `papers/paper_ii/`, 8 pages | Submit |
| III | Reconstruction theorem proved; density bridge is the key Lean obligation; cyclic vector is sufficient condition not equivalence | `DelayEmbedding.lean` ✅; `ReconstructionTheorem.lean` ✅ (builds cleanly; 6 intentional sorrys — all Mathlib API gaps, not mathematical gaps) | **First draft** — `papers/paper_iii/`, 6 pages | Close sorrys; submit |

---

## Task List (as of 2026-04-04, updated 2026-04-04)

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
- [x] **Revise Papers I and II** — Done 2026-04-04.
  Paper I: removed contradictory site-theoretic remark; added Stone route Lean
  formalization remark (documenting `StoneDualityExtension.lean` sorry inventory);
  removed stale self-citation to `mahon_paper0`. Paper II: fixed duplicate "Positive"
  item in Prop 5.2 (→ "Contractive"); resolved introduction tension on K_t primacy;
  fixed incorrect cross-reference for predictive kernel; sharpened bridge §8 K_t/U_T
  relationship. Both compile cleanly.
- [x] **Write Paper III (LaTeX)** — Done 2026-04-04. First draft at `papers/paper_iii/`
  (6 pages, compiles cleanly). Sections: setup, density bridge (monotone class proof),
  reconstruction theorem (three-way equivalence), cyclic vector (sufficient condition),
  Stone space identification, Takens comparison. Sketch at
  `notes/conceptual_sketches/cyclic_vector_theorem_sketch.md`.
- [x] **Formalize Paper III skeleton** — Done 2026-04-04. `ReconstructionTheorem.lean`
  builds cleanly on `stone-duality-extension` branch. Proved: `observableAlgebra`
  definitions, `density_bridge` (via `Lp.simpleFunc.dense`), `delayMap_measurable`.
  6 intentional sorrys — all Mathlib API interaction issues, not mathematical gaps.
  Flight log at `notes/lean_flight_log.md`; API reference at
  `notes/reconstruction_lean_flight_plan.md`.

### Current priorities

1. **Close `ReconstructionTheorem.lean` sorrys** — 6 intentional sorrys, all Mathlib
   API interaction issues documented in `notes/lean_flight_log.md` and
   `notes/reconstruction_lean_flight_plan.md`. Priority order:
   - `density_bridge` / `lpMeasSubgroup_dense_in_Lp` — isometric transfer via
     `lpMeasSubgroupToLpTrimIso`; requires section-variable pattern
   - `observableAlgebra_eq_comap` — `MeasurableSpace.comap` vs `pi` API
   - `delayMap_intertwines_shift` — `Int.toNat_add_one` arithmetic
   - `lpMeas_eq_top_of_ae_eq` / `reconstruction_iff_lpMeas` (←) — longer argument
   - `cyclic_implies_dense` — span ≤ Submodule containment

2. **Submit Papers I and II** — mathematically complete, Lean formalized, LaTeX clean.
   Blocking question: target venue? arXiv preprint first, or journal direct?

3. **Connect delay query system to reconstruction** — instantiate
   `ReconstructionTheorem` for `delayQuerySystem`: `delayAlgebra` dense iff shift
   has a generating observation. Requires connecting `DelayEmbedding.lean` to
   `ReconstructionTheorem.lean`.

### Long term / deferred
- `DiscriminabilityFoundations.lean` 3 sorrys — all Mathlib gaps (ultraproduct
  infrastructure); mathematics is correct, low priority.
- `delayQuerySystem.seqUpperDirected` sorry in `DelayEmbedding.lean` — deliberate
  scope note: the full delay system (all lags, all dimensions) is NOT sequentially
  upper-directed. The extension theorem is correctly scoped to bounded subsystems
  (`delayFixedLagBoundedSystem`). No action needed unless the scope is widened.
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
