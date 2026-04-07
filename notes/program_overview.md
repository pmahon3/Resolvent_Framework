# Observable Dynamics Program — Overview

## The Central Question

When an observer makes structured observations of a system — querying it at
increasing levels of refinement, recording outcomes, building a picture of the world
through measurement — what does coherence require of them?

The program shows that coherence, pursued to its conclusion, requires probability,
dynamics, and reconstruction. Not as additional assumptions, but as what the
structure of observation already contains.

---

## The Four Papers

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

---

### Paper IV — Finite-Sample Reconstruction: Rates, Witnesses, and the Honest Bridge

**What it asks:** Paper III establishes the reconstruction equivalence theoretically.
Paper IV asks: what does it look like empirically, at what rate, and with what
witnesses?

**Three honest theorems:**

1. **(Algebra theorem):** The σ-algebra approximation error δ̂(L,n) — computable from
   data alone — concentrates around the true δ(L), and the δ̂ stopping rule achieves
   the minimax-optimal rate n^{-s/(2s+d)} for f ∈ Hölder(s) without oracle inputs.

2. **(Dynamics theorem):** Under separation-stability of the predictive kernel Π_h
   (verified by Hölder regularity when T ∈ C^r), the estimated edge law Γ̂_h^(n)
   converges to Γ_h at rate n^{-β/(2β+d)}.

3. **(Conjunction theorem):** Under reconstruction ∧ separation-stability, both
   witnesses (δ̂ and d̂_L) certify the same object. The Markov structure of the delay
   vector is the honest bridge between them.

**Key insight:** δ̂ operates upstream of the rate — it measures reconstruction quality
in the σ-algebra sense without requiring knowledge of s, d, or the mixing rate. The
geometry shows up in the analysis of why δ̂ works, not in the procedure that computes it.

**Proof obligation register:** All 12 obligations closed (2026-04-06).
Obs. 1–8 closed under exponential mixing + ‖h‖_∞ ≥ 1/2.
Obs. 9–12 closed 2026-04-06 (details in sketch).

**Status:** Complete. LaTeX written 2026-04-06; bridge note integrated 2026-04-06.

**LaTeX:** `papers/paper_iv/paper_iv.tex` — 17 pages, 8 sections, bibliography
resolved, all references clean. Sections: Introduction, Setup, Bias Bound and
Algebra Side, Concentration of the Empirical Witness, The Algebra Theorem,
The Dynamics Theorem, The Conjunction Theorem, Discussion.

**Key results:**
- Lemma 3.1 (Conditional Variance Identity: E[Var(1_S|𝒪_L)] = ½∫_{R_L}|1_S(x)-1_S(x')|² d(μ⊗μ))
- Corollary 3.2 (Easy direction: δ(L) ≤ ½(μ⊗μ)(R_L), unconditional)
- Lemma 5.1 (dim_eff step function via Sard–Smale)
- Theorem 5.7 (Algebra Theorem: L̂* achieves minimax rate n^{-s/(2s+d)} without oracle inputs)
- Corollary 5.12 (Entropy characterisation: δ(L)→0 ⟺ H₂(ν_L)→∞ under fibre mixing)
- Theorem 6.4 (Dynamics Theorem: bi-Lipschitz delay map + empirical separation under (SS))
- Lemma 7.1 (algebra separation = metric separation for deterministic T — algebraic identity, not correlation)
- Theorem 7.3 (Conjunction Theorem with three-part failure-mode analysis; Markov bridge)

**Three computable witnesses (§1.3):**
1. δ̂(L,n) — algebraic witness
2. d̂_L(x,x') — delay-map separation
3. Ĥ₂(ν_L^(n)) — collision entropy (new; computationally simpler: no optimisation over sets)

**Companion note:** `papers/notes/bridge_note.tex` — standalone 4-page note proving
the conditional variance identity and the entropy characterisation (δ(L)→0 ⟺ H₂→∞)
in full detail. Cited as `mahon_bridge` in Paper IV.

**Open (named in §8):** polynomial mixing, d≤2s via localised Rademacher, (SS)
from first principles (Anosov case), stochastic T, sharp rates for L̂*,
concentration of entropy witness Ĥ₂ (most immediate extension).

**Lean formalization:** Not started.

---

## The Through-Line

Each paper takes the output of the previous as input:

```
Structured observations
    → [Paper I]   → probability measure P on (Ω, σ(CylGen))
                    Stone space St(C) as compact completion of Ω
    → [Paper II]  → dynamics: Koopman operator U_T, semigroup {K_t}
                    predictive kernels Π_t; dynamics = prediction structure
    → [Paper III] → reconstruction: St(O_h) ≅ X when O_h = B(X) mod μ
                    density bridge closes the loop with Paper I
    → [Paper IV]  → finite-sample: δ̂ stopping rule achieves minimax rate
                    three witnesses certify reconstruction from data alone
```

The four papers track a single object from four angles:

- **Paper I** (Boolean / topological): CE decides whether σ-additivity is possible.
  The Stone space of the observable algebra is the canonical compact completion of
  the sample space.

- **Paper II** (operator / spectral): the Koopman operator $U_T$ and semigroup $\{K_t\}$
  are derived from prediction structure, not assumed. Koopman–Perron duality connects
  function-space dynamics to measure-on-states dynamics.

- **Paper III** (algebraic / measure-theoretic): the density bridge connects Boolean
  algebra generation (Paper I) to $L^2$ density (Paper II). The Stone space built as
  a technical tool in Paper I reappears here as the object being reconstructed.

- **Paper IV** (statistical / information-theoretic): the conditional variance identity
  connects the algebraic error $\delta(L)$ to the geometry of unseparated pairs $R_L$
  and to the collision entropy $H_2(\nu_L)$. All three witnesses measure the same
  failure of separation.

The unifying object across all four papers is **observational indistinguishability**,
made precise at each layer:
- Paper I: events that never separate across refinements (failure of CE)
- Paper II: identical predictive laws ($\Pi_t(x,\cdot) = \Pi_t(x',\cdot)$)
- Paper III: same delay orbit ($\Phi_h(x) = \Phi_h(x')$)
- Paper IV: same delay vector at lag $L$ ($(x,x') \in R_L$)

The programme is complete when $(\mu\otimes\mu)(R_L) \to 0$: indistinguishability
vanishes at all layers simultaneously.

### The chain of bridges

The four papers are connected by a chain of equivalences:

```
Boolean ↔ Measure ↔ Function space ↔ Geometry ↔ Information
```

| Bridge | Paper | Identity |
|--------|-------|----------|
| Boolean → Measure | I | CE makes σ-additivity possible (Carathéodory / Stone) |
| Boolean → $L^2$ | III | Density bridge: σ-algebra generation ↔ $L^2$ density |
| $L^2$ → Geometry | III/IV | $\sigma(\Phi_h^{(L)}) = \mathcal{O}_h^{(L)}$ (Markov bridge) |
| Geometry → Information | IV | Conditional variance identity (Lemma 3.1 + bridge note) |

### The three obstructions

Each paper identifies a single obstruction:

| Paper | Obstruction | Status |
|-------|------------|--------|
| I | Lack of CE | Proved irreducible (Łoś + finite-cofinite counterexample) |
| III | Lack of density ($\mathcal{O}_h \neq \mathcal{B}$ mod $\mu$) | Characterised by density bridge |
| IV | Lack of fibre mixing | The Paper IV analogue of CE; irreducibility open |

Fibre mixing is to Paper IV what CE is to Paper I: the minimal condition under which
the algebraic and information-theoretic witnesses are comparable. Both are strictly
weaker than ergodicity. Whether fibre mixing is irreducible (not derivable from any
structural condition) is the deepest open question in the programme.

---

## What Each Paper Needs

| Paper | Mathematical status | Lean status | LaTeX status | Next action |
|-------|--------------------|-----------|----|---|
| I | All routes proved; bridge written | `QuerySystem.lean` ✅; `DiscriminabilityFoundations.lean` 3 sorrys (Mathlib gaps); `StoneDualityExtension.lean` ✅ (2 intentional Mathlib-gap sorrys); `TopologicalQuerySystem.lean` + `ProkhorovExtension.lean` ✅ (Prokhorov route) | **Revised** — `papers/paper_i/`, 13 pages | Submit |
| II | Core results proved | `PredictiveState.lean` ✅; `PredictiveOperators.lean` ✅ | **Revised** — `papers/paper_ii/`, 8 pages | Submit |
| III | Reconstruction theorem proved; density bridge is the key Lean obligation; cyclic vector is sufficient condition not equivalence | `DelayEmbedding.lean` ✅; `ReconstructionTheorem.lean` ✅ (2 sorrys — Mathlib gaps only) | **arXiv ready** — `papers/paper_iii/`, 7 pages | Upload |
| IV | Complete. All 12 proof obligations closed. Three main theorems: Algebra (Thm 5.7), Dynamics (Thm 6.4), Conjunction (Thm 7.3). Entropy characterisation (Cor 5.12) integrated from bridge note. | Not started | **Complete** — `papers/paper_iv/`, 17 pages | Submit |

---

## Task List (updated 2026-04-06 — programme complete, arXiv upload next)

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
- [x] **Close `delayMap_intertwines_shift` sorry** — Done 2026-04-05. Fixed by indexing
  `delayMap` and `unilateralShift` by `ℕ` (not `ℤ`). Proof: one-line
  `simp only [delayMap, unilateralShift, Function.iterate_succ_apply]`. 5 sorrys remain.
- [x] **Close `observableAlgebra_eq_comap` sorry** — Done 2026-04-05. Key: unfold `pi` as
  `iSup` via `simp [MeasurableSpace.pi, comap_iSup, comap_comp]`, then `iSup_le` +
  `measurable_iff_comap_le`. 4 sorrys remain.
- [x] **Close `cyclic_implies_dense` sorry** — Done 2026-04-05. Key: `aestronglyMeasurable_congr
  coeFn_toLp` + `Submodule.topologicalClosure_mono` + `dense_iff_topologicalClosure_eq_top`.
  3 sorrys remain (all Round 4: lpMeas instance refactor).
- [x] **Connect `DelayEmbedding.lean` to `ReconstructionTheorem.lean`** — Done 2026-04-05.
  Added `section ReconstructionBridge` to `DelayEmbedding.lean`: `delayObservableAlgebra`
  (wraps `observableAlgebra`), `delayObservableAlgebra_eq_comap`, `delayMap_shift_intertwining`,
  `delay_cyclic_implies_reconstruction` (fully proved, zero sorrys). One documented sorry:
  `delay_reconstruction_iff` — two-MeasurableSpace-instance elaboration prevents calling
  `reconstruction_iff_lpMeas` from `DelayEmbedding.lean`; marked with explanation.
  Also fixed 3 pre-existing errors in `DelayEmbedding.lean` (linarith → omega; map_map
  pattern mismatch; rw unsolved goals).
- [x] **Add Lean formalization remark to Paper III** — Done 2026-04-05. Added
  `\begin{remark}[Lean formalization]` at end of §5 (Takens comparison), documenting
  4 proved theorems and 2 documented Mathlib-gap sorrys (updated from 3 after
  `lpMeasSubgroup_dense_in_Lp` deleted).
- [x] **Remove `lpMeasSubgroup_dense_in_Lp`** — Done 2026-04-05. Deleted from
  `ReconstructionTheorem.lean` (unused; FALSE for general `m ≤ m0`). Now at 2 sorrys.
- [x] **Revise Paper III** — Done 2026-04-05. Stone identification proof (§4)
  strengthened with explicit injectivity mod μ argument; stale "Proposition 5.5"
  reference fixed; Lean remark corrected (cross-refs, unilateral/bilateral shift
  distinction, Mathlib cite). Compiles cleanly.

### Current priorities

1. **arXiv upload of Papers I, II, III, IV** — all LaTeX complete and clean (17 pages
   for Paper IV after bridge note integration). Also upload bridge note as companion.
   Remaining tasks tracked in `notes/arxiv_prep.md`:
   - Upload Paper I source files; then backfill `mahon_paper1` arXiv ID in Papers II–IV
   - Upload Paper II source files
   - Upload Paper III source files; then backfill `mahon_paper3` arXiv ID in Papers I, II, IV
   - Upload Paper IV source files (including bridge note `mahon_bridge`); then backfill arXiv IDs

### Long term / deferred

**Lean:**
- `DiscriminabilityFoundations.lean` — 3 Mathlib-gap sorrys (ultraproduct
  infrastructure); mathematics is correct, low priority.
- `delayQuerySystem.seqUpperDirected` sorry in `DelayEmbedding.lean` — deliberate
  scope note: the full delay system is NOT sequentially upper-directed. No action
  needed unless scope is widened.
- Paper IV Lean formalization — not started; no timeline.

**Open mathematical frontiers** (see `notes/program_synthesis.md` for full discussion):
1. **Fibre mixing irreducibility** — is fibre mixing derivable from any structural
   condition, or is it irreducible like CE? This is the deepest open question.
2. **Entropy witness concentration** — finite-$n$ McDiarmid bound for
   $\hat{H}_2(\nu_L^{(n)})$; most immediate technical extension; no new structural
   theory needed.
3. **Paper 0 direction** — separation system + coherent charges as a primitive
   foundation; CE and fibre mixing as instances of charge-coherence conditions.
   Not to be developed until after arXiv upload.

---

### Paper 0 — Topology from Observation (provisional)

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
vector condition. Paper 0 asks whether the *relevant* topology on the state
space is the Stone topology, or something derived from the measure-weighted
separation structure. If the latter, the programme begins and ends with the
observer's distinctions — the topology, like the measure, would be something
the observer's query system already contains.

**Status:** Conceptual sketch only. Papers I–IV are now complete; this direction
can be developed after arXiv upload.

**Reference:** `notes/conceptual_sketches/philosophy/topology_from_vanishing_distinction.md`

---

## What Is Not in the Program

- Computational implementation (data-driven dynamics, EDMD, etc.) — this is a
  natural sequel but is treated as a separate project
- Infinite-dimensional state spaces beyond $L^2$ — deferred
- Non-stationary / non-ergodic generalizations — deferred
