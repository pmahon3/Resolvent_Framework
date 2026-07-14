# σ-essential-state research campaign log

Direct research on the OML branch is the active workflow. Iterations are
appended below the baseline; each records question, construction/lemma,
evidence class, gates passed, first failure, obstruction, strategic update,
and next task.

## Continuation baseline (2026-07-13, finite-core resolution campaign)

- **Actual start:** branch `oml-descent-sigma-essential-reduction`, commit
  `baac957507303a04ea20f36cd3ea75cb6ed181f8`, clean worktree, tracking
  `origin/oml-descent-sigma-essential-reduction`. The nine commits after
  baseline `a49a44a` were inspected in order; they are exactly the coarse
  anatomy, cyclic no-go, review repair, type-partition theorem, rotating
  specification, local certificate, splicing reduction, metadata sync, and
  typed decorated-form invariant recorded below. No hidden Gate-N pass occurs.
- **Problem:** decide whether every concrete σ-complete OML satisfies Φ,
  equivalently whether `St_σ(L)` is product-topology dense in `St_fa(L)`;
  pursue both a fully gated counterexample and a structural positive theorem.
- **Evidence ledger at entry:** Lean verifies the blockwise/Stone-density,
  pointed/fine-block, two-block-rescue, T4-necessity, and compact-transport
  infrastructure named in `CURRENT_STATE.md`; hand proofs establish the
  coarse defect anatomy, fully visible cyclic no-go, finite type-partition
  obstruction, one-graph lemma, countable dependence, fibre morphism,
  same-type polarity, transversal invariant, intended collector meet, and
  scoped graph-network restriction theorem; executable certificates give 24
  local traces and balanced core sizes 88, 180, 700, 4428. The balanced-core
  verifier separately recomputes closure but shares the producer's cell
  encoding, so it is not an encoding-independent proof.
- **Strategy A established:** every event uses countably many local generators;
  outside their columns each fibre lies in the certified 24-trace class; on
  any same-type pair the traces are either equal proper traces or the two
  binary corners; every three-type transversal belongs to the finite relation
  `Q`. Consequently nonzero W-supported events, `Σ_i∩Σ_j`, unintended
  singleton collectors, and collector restrictions with uncountable
  variation modulo countable support are excluded. The intended `G_ij` is the
  greatest generated lower bound of `Σ_i,Σ_j`.
- **Exact splicing gap:** these are upper invariants. Given a countable
  disjoint family of countable-column core modifications, fibrewise collapse
  leaves finitely many proper modes plus a binary tail, but it is unproved
  that the coupled three-type result is one globally parameterized finite core
  (or that every locally `Q`-admissible support assignment has such a core).
  Transversal membership in `Q` is not simultaneous realizability.
- **Gate status:** N **open**, reduced to finite-core splicing; L **not
  opened** (only the collector-meet sublemma); M, C, Z, F, and Φ **open and
  unavailable**. No candidate counterexample is claimed.
- **Strongest construction route:** the rotating small-piece graph triple,
  conditional first on N and ultimately on coherent column-free f.a. gluing.
  **Strongest theorem route:** the scoped finite-typed graph restriction
  theorem, then a rectangularity/splicing dichotomy; beyond it B′(i)/T4 and
  non-countable-type coarse coherence remain the principal residues.
- **Stale metadata corrected before entry:** the registry now reports 76 OML
  entries and the finite-core frontier; `CURRENT_STATE.md`, `frontier_map.md`,
  and `program_overview.md` agree. No further stale summary was found in the
  nine-commit diff. The older embedded baselines remain historical records.
- **First task:** reconstruct `Q` independently, classify every fixed-proper
  mode stratum on its binary coordinates, and use the resulting exact
  rectangularity or missing-corner data to decide the splicing lemma.

## Continuation baseline (2026-07-13, decorated-form campaign)

- **Actual start:** branch `oml-descent-sigma-essential-reduction`, commit
  `64138e5fbd314a7a85eee103e9c86abb2bc5ec45`, clean worktree. The five
  commits since the original campaign baseline add iterations 1--7, the
  rotating candidate, its fixed-column certificate, the type-partition and
  cyclic-visibility obstructions, the one-graph lemma, and synchronized
  frontier metadata; no later Gate-N result is hidden in Git history.
- **Exact Gate N:** determine the smallest concrete Dynkin/σ-class on
  `ω₁×ω₁` containing every full cylinder, the three `Σ_i`, every column
  piece and resolution singleton, and the three collectors `G_ij`; prove a
  complement/countable-disjoint-union normal form covering arbitrary
  cylinder parameters, or explicitly derive an indispensable forbidden
  event. No compatibility, meet, maximal-block, σ-completeness, centre, or
  state-gluing conclusion is part of Gate N.
- **Established partial closure:** the one persistently fibre-splitting graph
  plus full cylinders generates only cylinders and the graph/complement pair
  (**hand proved**); the three disjoint collectors force their total, the
  residuals `H_i=Σ_i\(G_ij⊍G_ik)`, and decorations of any form by a cylinder
  supported on its zero-fibre types (**hand proved**); the one-column
  six-cell closure has exactly 24 traces and omits nonzero `W`, `W` itself,
  and all unintended singleton resolutions (**exhaustive finite evidence,
  producer plus independent verifier**). None implies an arbitrary-base
  normal form.
- **Known forbidden-event mechanisms:** finite measurable type partitions;
  central common bases; boundary saturation; independent point replacement;
  common-point pullback extension; compact simultaneous selection; trivial
  or gauge-trivial monodromy; mixed closure adding maximal blocks; graph
  restrictions; and incoherent f.a. gluing. Fully visible cyclic coupling
  additionally fails at latticehood, while one-graph cylinder restriction is
  explicitly *not* a valid mechanism (**hand proved**).
- **Unresolved operations:** complements of decorated multi-forms; exact
  disjointness conditions with independently varying cylinder parameters;
  finite and countable disjoint splicing; migration of parameters between
  zero-fibre types and collector supports; residual/collector coincidence;
  graph-form coincidence; and whether countable unions increase restriction
  rank or expose `W`, `Σ_i∩Σ_j`, or an uncountable `G_ij` restriction.
- **First selected task:** compute the finite typed fibre-trace algebra of all
  primitive global labels, derive the exact parameterized complement and
  disjoint-union rules, and use an independent semantic verifier to test the
  proposed decorated grammar before attempting the arbitrary-base induction.

## Campaign continuation baseline (2026-07-13, Gate N restart)

- **Actual start:** branch `oml-descent-sigma-essential-reduction`, commit
  `609a8da16d0ef031a9e97a231cb17bf175bf7f8c`, clean worktree.
- **Open gate:** Gate N for the rotating small-piece graph triple: determine
  the global Dynkin/σ-class generated by the full cylinder algebra, the three
  graph events and their column pieces, all resolution singletons, and the
  three meet collectors. No later gate is available until this is settled.
- **Established since the original baseline:** coarse blocks occur in
  essentially irreducible examples and countable-type defects are classified
  (**hand proved, conditional only where the earlier arbitrary-base inflation
  theorem is invoked**); the club field supplies a non-countable-type coarse
  example (**hand proved using Ulam's theorem**); fully visible cyclic coarse
  coupling is closed by the visibility/latticehood rescue and its rich closure
  loses a meet (**hand proved, adversarially reviewed**); finite measurable
  kill-type partitions also kill the finitely additive witness (**hand proved,
  adversarially reviewed after the atom-cover repair**); the rotating
  candidate is specified but all global claims remain **conditional/open**;
  its fixed-column six-cell trace has 24 events and the stated exclusions
  (**exhaustive finite evidence with an independently recomputing executable
  verifier**), with no implication for global closure.
- **Banked infrastructure rechecked:** Stone density, blockwise σ-additivity,
  two-block rescue, pointed/Dirac results for countably generated blocks, and
  the cited compact-transport/block facts are **Lean verified** in
  `formalization/QuerySystem/`; cluster reduction, compact eligible-slice
  selection, and the boundary/gluing formulations are **hand proved**.
- **Stale state/metadata:** `notes/taxonomies_index.json` says the OML taxonomy
  has 68 entries although its own headline says 77, and its OML status still
  describes the pre-campaign five-block/twist frontier;
  `notes/open_questions/oml_attack/CURRENT_STATE.md`, `frontier_map.md`, and
  `program_overview.md` retain older “current next step” language. The root
  has no `CURRENT_STATE.md`; the retained compact index is the one under
  `oml_attack/`. These require synchronization once Gate N warrants a verdict.
- **Selected next iteration:** construct a typed fibre-trace/support algebra
  for the *global* generated σ-class, beginning with the exact Dynkin-system
  effect of adjoining one graph to a full cylinder algebra, then add the
  finite graph/collector forms and test whether arbitrary cylinder parameters
  force a forbidden collector restriction or a nonzero W-supported event.

## Baseline (2026-07-13, campaign start)

- **Branch:** `oml-descent-sigma-essential-reduction`
- **Starting commit:** `565c8b8258d18b659e0f0cc05985c6036472cd0d`
  (working tree clean; legacy `.agent-relay/` machinery already removed in
  this commit; its mathematical outputs are integrated in the notes cited
  below).

### Problem of record

> Does every concrete σ-complete orthomodular lattice satisfy finite-trace
> σ-liftability Φ: every finite trace realized by a global finitely
> additive two-valued state is realized by some global σ-additive
> two-valued state? Equivalently (Lean, `phi_iff_dense`): is St_σ(L) dense
> in St_fa(L) in the product topology?

Conjectured YES for the admissible class 𝒞 (concrete, σ-complete,
non-Boolean, essentially irreducible OMLs); no proof and no counterexample.
Both directions are pursued without prejudice.

### Established results (by evidence class)

**Lean-verified (axiom-free, `formalization/QuerySystem/`):**
blocks/overlaps are σ-fields (A1, A2, L0); blockwise ⟺ global σ
(`isSigmaOn_carrier_iff_maxBlocks`); Dirac realization on countably
generated blocks (T3); pointed ⟺ σ on fine blocks (P⁼); two-block rescue
(2BR); Φ ⟺ Stone density (`phi_iff_dense`); B′(i) ⟹ T4 necessity; T1
singleton quarantine; Marczewski compact-transport criterion + ω₁
cocountable coarse-state bank; inner-regularity theorem-lets R, P;
finite raw-overlap quarantine (`BoundaryDescent.lean`); finite-trace
Dirac/independent-trace/gluing steps.

**Hand-proved (adversarially proof-read):** cluster normal form (open
locus = clusters of m ≥ 3 pairwise-incompatible, pairwise-intersecting,
empty-kernel value-1 events); GSD ⟺ Φ exact boundary reformulation;
Theorem 4.2 boundary surgery; finite-interface quarantine (generated
form); compact eligible slices ⟹ face σ-lifts; conditional finite-atlas
boundary localization (needs face-image relative openness); Maharam (8.2)
excluded as repointing engine; FS demoted; single-pullback tameness under
common σ-extension / common-point hypothesis; repeated-common-block
lemma; joint-generation collapse lemma; arbitrary-base q0 inflation of
the 44-event survivor (concrete OML, exactly five blocks, σ-complete,
centre-free, proper C01 boundary, noncompact slice, Φ-tame) with global
60-form compatibility audit; (5,11) non-atomic pullback completion
(147,592-event finite control; arbitrary-base seven-shape model,
single-edge, Φ-tame by common-point extension).

**Exhaustive finite evidence:** 44-event five-block survivor census
(127 subfamilies); P(n) fibre approximants n=2,3,4; 60-form obstruction
census (47,070 comparisons); eight P(2) whole-interface triangle twists
(odd = nonfaithful, even = gauge-trivial); pentagon relay censuses
(sessions 24–33: two-port 4,050→0; k=3 two-cell Exit B; k≥6 vacuous;
one-port three-cell 10⁶→0 unconditional; two-port design class
2.08×10⁷→0); 7-loop removable-face censuses (sessions 35–38: period 1
widths ≤4, period 2 widths ≤2, period 3 width 1 — all zero operative
survivors); O2/O3 duplicate-edge audit; four-point transverse-overlap
collapse.

### Closed architectures / mechanism exclusions

1. Whole-interface P(2) triangle twists (nonfaithful or gauge-trivial).
2. Two-common-block duplicate edges (O2/O3): same selector pair in two
   blocks = one pullback (repeated-common-block lemma).
3. Jointly generating transverse overlaps: force block equality
   (collapse lemma).
4. Independent lattice-atom interval substitutions (two-fibre monodromy:
   disjoint supports, full-product relation, identity monodromy).
5. Common-base inflations (restore a central factor).
6. Pentagon relays: binary (§21), ternary essential triggers (§25),
   two-port removable-state (§26), k≥3 two-cell and three-cell bounded
   classes (§27); 7-loop face bounded port classes (§§28–31).
7. Fine-rigidity/singleton mechanisms (T1); Maharam (8.2); FS; finite
   compatible carrier certificates and affine shared-tail cancellation
   (§§16–17); four-loop gadgets (not lattices, §18); direct fan-out (§19).

### Known tameness mechanisms (do not re-walk without a structural
distinction)

central common-base decomposition; full-boundary saturation; independent
point replacement; common-point pullback extension; compact simultaneous
selection; trivial monodromy; gauge-trivial whole-interface twists.

### Unresolved claims / owed items

- B′(i) (fine-block conjecture) and T4 (its finitary shadow): open.
- B′(ii) coarse-block coherence: open, needs precise restatement.
- Two-port three-cell relays OUTSIDE the s_*-preserving design class:
  open (not closed by s33).
- 7-loop faces other than {a0,a3,a11}, widths/periods beyond the censused
  bounds, two-pentagon higher-slack cells: open.
- Strong-state-equation kill for census survivors: exploratory, open.
- σ-liftable-locus openness for actual OML overlaps (Theorem 9.1
  hypothesis): open.

### Best construction route (Lane A)

The named next gate (survivor note §5, inflation review §6, taxonomy
headline): a **proper shared-subalgebra twist or a second inequivalent
coarse coordinate** on the inflated five-block survivor — more generally,
an architecture whose coupling defeats independent replacement. Structural
constraints discovered by the closures: pairwise block constraints are
single pullbacks over the overlap; twists need ≥3 blocks with three
*distinct* proper overlaps around a cycle; couplings must be realized by
actual event overlaps. The first campaign candidate is a cyclic
order-coupled coarse triple (three coarse coordinates on ω₁ with the
three cyclic order events S12, S23, S31 pairwise incompatible: empty
triple intersection at point level, pairwise intersections uncountable) —
it evades Dirac rescue by construction and tests whether coarse σ-states
can be trapped by cyclic coupling.

### Best theorem route (Lane B)

Mine each failure for the strongest honest general lemma. Standing
targets: (i) a unique-coarse-trace gluing theorem (boundary traces of
f.a. states on cocountable-type coarse atlases are unique, hence
σ-liftable per block, hence Φ via Theorem 4.2); (ii) acyclic quotient
networks with compatible endpoint extension imply Φ; (iii) coarse
boundary-defect anatomy (T^fa ∖ T^σ on non-countably-generated overlaps =
free-concentrated-on-countable traces for ctble/coctble type); (iv) a
structural liveness/separation theorem replacing further relay brute
force; (v) the vacuity question of §10d: does 𝒞 ∩ OML contain genuinely
coarse blocks at all (decides whether B′(ii) can be dodged).

### Primary navigation

`notes/open_questions/oml_attack/oml_lattice_taxonomy.json` (68 entries),
`oml_lattice_regularity_attack.md` (§§1–31),
`relational_boundary_descent.md`, `oml_exhaustive_boundary_survivor.md`,
`oml_arbitrary_base_inflation_review.md`,
`oml_nonatomic_pullback_completion.md`, `CURRENT_STATE.md`.

---

## Iterations

### Iteration 1 (2026-07-13) — coarse inhabitation, countable-type defect anatomy, irreducibility fence

- **Question tested:** §10d's vacuity exit — does 𝒞 ∩ OML contain
  state-coarse blocks at all? — plus the exact σ-defect of the tractable
  coarse class.
- **Results** (note: `oml_coarse_inhabitation_and_defect.md`):
  (a) classification of two-valued σ- and f.a. states on σ-fields of
  countable type over an atom partition: σ = atom-principal ∪
  {co-atom-countable}; defect = exactly free-on-countable concentration —
  unifies the P(ℕ) relay master and the ω₁ coarse bank in one lemma;
  (b) corollary: trapping at countable-type boundaries reduces to one
  cheap co-atom-countable exclusion + the countable atom-killing (relay)
  problem, so countable-type coarseness buys a witness nothing new;
  (c) **fence:** a one-interval inflation is essentially irreducible iff
  its fibre survives the countable quotient; the natural instantiation
  A = ctble/coctble(ω₁) FAILS admissibility (quotient = the four-element
  Boolean algebra over the realized crossed traces; ✎ corrected from
  P(4) by the iteration-3 review) — caught before it could contaminate
  later work;
  (d) **inhabitation:** the ℵ₁-piece fibre A* passes all gates; L* ∈
  𝒞 ∩ OML has three state-coarse blocks and a global non-principal
  σ-state, so B′(ii) is a real inhabited factor (vacuity exit closed,
  negatively). L* is Φ-tame.
- **Evidence class:** hand (a–c self-contained; d conditional on the
  audited arbitrary-base inflation theorem). No executable content
  (uncountable claims).
- **Gates:** L* passes concreteness, σ-completeness, five-block
  classification, trivial centre, essential irreducibility,
  state-extension, order-separation; fails (as expected) at Φ-hardness —
  tame by the banked point replacement.
- **Strategic update:** B′(ii) splits: countable-type coarse locus
  re-fine-ifies to the relay engine; the genuinely open coarse residue is
  non-countable-type state-coarse σ-fields. Taxonomy updated
  (coarse_toy settled-inhabited; new anatomy + fence entries; B′(ii)
  restated).
- **Next lemma-sized task:** either exhibit a concrete non-countable-type
  state-coarse σ-field of sets with a defect class beyond
  free-on-countable, or prove countable-type anatomy is universal for
  state-coarse σ-fields of sets. Deferred behind the Lane A cyclic
  candidate (iteration 2).

### Iteration 2 (2026-07-13) — cyclic order-coupled coarse triple: closed (fully visible form)

- **Question tested:** can three coarse coordinates on κ³, coupled by the
  cyclically unsatisfiable order events S₁₂ = {x<y}, S₂₃ = {y<z},
  S₃₁ = {z<x}, carry a σ-essential cluster? (The first genuinely cyclic
  Lane A candidate beyond the closed one-coordinate and P(2) classes.)
- **Construction/lemma** (note: `oml_cyclic_order_coupling.md`):
  (a) **Lemma A (no-Fubini/splitting freeness):** an event persistently
  splitting a countably closed dichotomy base is σ-value-free over that
  marginal; corollary: order events over the coarse box filter cannot be
  value-forced — the Sierpiński/Fubini intuition does not transfer to
  two-valued σ-states;
  (b) **Theorem B (trichotomy):** full transverse visibility (all fibre
  rectangles compatible with the transverse order event) + latticehood
  forces the pair compatible via banked T1 second form, and then 2BR
  kills the f.a. witness; so any realization is invisible, degenerate,
  or a non-lattice — the fully visible class is CLOSED;
  (c) **exemplar:** the piecewise (germ) closure L_rich is a concrete
  σ-class realizing full visibility in which S₁₂ ∧ S₂₃ fails by an
  ω₁-chain of countable-support lower bounds — the product-Ulam
  meet-destruction anatomy, now derived rather than assumed.
- **Evidence class:** hand (Lemma A self-contained; Theorem B over banked
  T1/L0/2BR/A2; L_rich normal-form proofs). No executables possible
  (uncountable content).
- **Gates:** the candidate dies at gate 4/interaction of gates 3–4
  (latticehood vs. realized coupling) before any state-selection gate is
  reached; the failure is architecture-wide (any box-splitting coupling
  with pointwise-resolved intersections), not example-specific.
- **Strategic update:** two reusable exclusions banked (no-Fubini
  forcing; pointwise-resolved overlaps). A witness must force values by
  in-block countable disjoint-union geometry (relay engine) — coarse
  marginal structure alone provably cannot trap. Taxonomy +3 entries.
- **Next lemma-sized task:** adversarial review of iterations 1–2 (the
  campaign's review checkpoint), then the partial-visibility residue or
  the countable-type-universality question from iteration 1.

### Iteration 3 (2026-07-13) — adversarial review checkpoint: both notes CLEARED with repairs

- **Question tested:** refutability of every claim in iterations 1–2
  (two independent fresh-context hostile reviewers, instructed to
  refute, with the banked dependencies and primary definitions in
  hand; one reviewer machine-checked the crossed-block traces against
  the labelled block tables).
- **Verdicts:** NO load-bearing claim refuted in either note. Repairs
  demanded and applied in place:
  - coarse note: the trivial-fibre quotient is the four-element Boolean
    algebra over the realized crossed traces {∅, h, h^c, q0}, NOT P(4)
    (A10 and A11 cut q0 the same way — machine-checked); the A*
    partition example was wrong (ω-th-predecessor classes are
    countable) and replaced by bijection fibres; Corollary 3's T^fa/T^σ
    now defined locally with the f.a.-coherence hypothesis explicit;
    σ-ideal reading caveat added.
  - cyclic note: Lemma A's ν⁺-agreement step reconstructed (was
    garbled); the self-contradicted "all-three σ-consistent" clause
    struck from Corollary A1 (freeness is exactly pairwise); Theorem
    B's visibility hypothesis restated as X_α ∈ L with κ = ω₁ pinned
    for the P₃-internal reading; §4 gained the previously missing
    countable-refinement lemma (false for general σ-fields, true here
    by the countable-atom structure) and the corrected fibre
    degeneration (two of three families per fibre, not all three),
    with the Z = Y ∪ X membership argument rerun accordingly.
- **Evidence class:** review receipts = the two reports (verdicts
  quoted in the notes' status lines); all conclusions of iterations 1–2
  stand at their stated evidence classes after repair.
- **Strategic update:** none forced by review. The failed chunked-column
  design explorations between iterations already yielded a general
  obstruction statement; writing and proving it is iteration 4.

### Iteration 4 (2026-07-13) — type-partition obstruction; club-field anatomy; Fodor residue named

- **Question tested:** can the σ/f.a. asymmetry a witness needs be
  produced by per-atom pairwise disjointness over a coarse localizer
  (the natural Ulam/coarse trap design, attempted in three variants)?
- **Results** (note: `oml_type_partition_obstruction.md`):
  (a) **Theorem 1 (type-partition obstruction), block-free on any
  concrete σ-class:** if finitely many disjoint cells T_t ∈ L cover a
  forced K and each cell has a pattern pair disjoint on it, no
  two-valued f.a. state charges {K, Σ_1..Σ_k} — the trap kills its own
  witness. Corollary 2: uniform per-atom disjointness kills are void
  whenever the atom family is countable or the base is locally full
  (type cells become events).
  (b) **Club-field classification:** 𝒜_club is state-coarse but NOT
  countable-type — σ-states = Diracs + club state (via Ulam 1930);
  defect = free-on-nonstationary with no uniform countable witness.
  This answers iteration 1's universality question NEGATIVELY. Fence:
  𝒜_club is locally full below nonstationary sets, so Corollary 2 still
  applies; club blocks must be cylinderized (T1).
  (c) Three failed trap designs recorded as instances (full power set;
  countable localizer; ω₁-chunk tower — the last dies by recursion:
  each diffuse-exclusion event is a countable localizer one level up).
- **Evidence class:** hand (Theorem 1/Corollary 2 self-contained;
  Proposition 3 uses Ulam, ZFC); design deaths = instances; the tower
  recursion and Fodor direction ledgered as strategic readings only.
- **Gates:** the three construction attempts each died at the
  f.a.-coherence gate (gate 9/12 territory) — by the new theorem, not
  by accident; failure is architecture-wide.
- **Strategic update:** witness asymmetry can only come from countable
  disjoint-union geometry (relay engine) or Ulam-type completeness
  failure; the first genuinely untouched mechanism is
  **regressive/Fodor rigidity over stationary localizers** (no finite
  type partition to become measurable) — named as the coarse-side Lane
  A residue. Taxonomy +2 entries.
- **Next lemma-sized task:** probe Fodor rigidity: design the minimal
  regressive-kill architecture and test whether Fodor's pressing-down
  forces a stationary constant witness that contradicts... (i.e., decide
  whether the mechanism kills σ-lifts without a measurable type
  partition), or refute it with a splitting-freeness argument.

### Iteration 5 (2026-07-13) — the rotating small-piece candidate specified

- **Question tested:** is there ANY architecture that simultaneously
  threads every banked obstruction (type-partition, T1 pointwise
  resolution, no-Fubini, 2BR, ω₁-chain meet failure)? The iterative
  design search (probing Ulam-base kills against each banked theorem in
  turn; five intermediate designs died against the banked mechanisms
  during iteration 4's exploration and this one) converged on ONE
  surviving shape.
- **Result** (note: `oml_rotating_small_piece_candidate.md`): the
  **rotating small-piece graph triple over an Ulam base** — carrier
  ω₁×ω₁; B = full first-coordinate cylinder field; three graph events
  with per-column-type rotating two-point small pieces; resolution
  singletons; meet-collector graphs G_mn deliberately incompatible with
  uncountable cylinder restrictions. σ-kill: Ulam column-localization +
  finite small-piece splitting (proved modulo the closure normal form);
  f.a. escape: column-freeness, with every banked death threaded BY
  DESIGN (no disjoint pattern pair anywhere → Theorem 1 silent; W-regions
  unresolved → T1 blocked; resolved parts collected into designed meets
  → ω₁-chain blocked; m = 3 cluster normal form exact).
- **Evidence class:** design specification; per-column kill logic hand,
  conditional on Gate N; NOTHING banked as a theorem about the candidate.
- **Gates:** staged as N (closure normal form — critical), L, M, C, Z
  (quotient audit per iteration 1's fence), F (f.a. coherence — the
  crux), Φ. None passed; the spec is frozen so Gate N can be attacked
  against a fixed target.
- **Strategic update:** this replaces the generic "proper-interface
  twist" as the priority construction target (taxonomy headline
  updated); Fodor rigidity demoted to backup. If Gate N or F fails, the
  failure is to be converted into the next obstruction theorem — the
  campaign's Lane B pattern.
- **Next lemma-sized task:** Gate N — exhibit the ⊍/c-closure normal
  form and verify the §2 exclusions survive closure.

### Iteration 6 (2026-07-13) — obstruction review repaired; local column trace certified

- **Questions tested:** does the type-partition obstruction survive a
  fresh hostile reading, and does the rotating candidate's fixed
  six-cell column trace already manufacture its forbidden W-event?
- **Review result:** Theorem 1 remains sound. Corollary 2 now states
  that its listed atoms are all atoms and proves their cover using its
  countability/local-fullness hypotheses; atomicity alone would not
  suffice. Proposition 3 now includes the successor ordinals as an
  explicit ZFC witness. The claimed death of coarse design 3 was
  downgraded to plausibility-grade because persistent splitting, joint
  σ-consistency, and global extension were not established.
- **Executable result:** the producer
  `verification/census_2026-07-13_campaign_it6/column_trace_audit.py`
  exhausts the 64 subsets of the six fibre cells. Its generated
  24-event certificate is independently recomputed by
  `verify_column_trace.py`. No nonzero trace event lies below W,
  r_i ∩ r_j = W is absent, exactly g and h are isolated, and
  r_k = {g} ⊍ {h} is present.
- **Evidence boundary:** this passes only the fixed-column finite
  subcheck. It does not control coincidences involving multiple
  columns, uncountable cylinders, graph collectors, or countable
  disjoint unions, and therefore does not pass Gate N.
- **Strategic update:** retain the rotating candidate, but attack the
  global normal form next. Design 3 remains live unless one of its
  three missing extension checks is settled.
- **Next lemma-sized task:** derive a global support/trace normal form
  for generated events and decide whether countable disjoint unions or
  complements force W-regions, pairwise intersections, or uncountable
  restrictions of a meet collector.

### Iteration 7 (2026-07-13) — cylinder restriction fallacy isolated; first global forms derived

- **Question:** does adjoining a graph to the full cylinder algebra already
  force its arbitrary cylinder restrictions, and what multi-collector forms
  are forced before any normal-form induction?
- **Lemma/construction:** Lemma 7.1 in the candidate note proves that one
  graph which persistently splits every fibre generates only the cylinders
  and the graph/complement pair. Thus full cylinders alone do not force graph
  restrictions. For the actual three-collector incidence, pairwise
  disjointness forces the total collector and permits subtraction of the two
  incident collectors from each `Σ_i`, producing residual forms `H_i` whose
  pairwise set intersections are exactly the unresolved `W` regions on the
  third type. Empty collector fibres also force decorated forms
  `G_ij ⊍ cyl(A)` for arbitrary `A` in the missing type.
- **Evidence class:** hand proved. The earlier 24-event receipt confirms only
  that the residual subtraction does not expose `W` at one fixed column
  (**exhaustive finite evidence**).
- **Gates passed:** none. Gate N remains open.
- **First failure:** the one-graph grammar ceases to be closed once several
  disjoint global forms have type-dependent empty fibres; arbitrary cylinder
  decorations must be tracked.
- **Obstruction mechanism:** any forced restriction must arise from
  multi-form disjointness/complement identities, not from the availability of
  the cylinder algebra by itself.
- **Adversarial review:** CLEARED the partial algebra after requiring an
  explicit collector-incidence table, the correction “residual event/form”
  (not graph), and explicit tracking of the residuals' zero-fibre types.
  Those repairs are incorporated. The reviewer found no short forced
  forbidden event and warned that compatibility claims belong to Gate L,
  not to the Gate-N generator specification.
- **Strategic update:** reduce Gate N to a finite typed form algebra carrying
  arbitrary cylinder parameters on the zero-fibre support of each form.
- **Next task:** close or refute that decorated-form grammar and test whether
  two decorated forms can manufacture `G_ij∩cyl(A)` or a nonzero `W`-form.

### Iteration 8 — countable dependence of generated events

- **Question/result:** does one event use uncountably many local generators?
  No: every member of a σ-class generated by `S` lies in the σ-class of a
  countable subset of `S`. The union of all countably generated sub-σ-classes
  is itself a σ-class. **Evidence: hand proved.**
- **Consequence:** column pieces and resolution points affect only countably
  many columns of any one event. Gate N remains open; next task was the local
  trace invariant.

### Iteration 9 — fibre-trace obstruction

- **Result:** fibre restriction is a morphism for complement and countable
  disjoint union. Every global event therefore has one of the certified 24
  local traces on every column. **Evidence: hand proved over executable-
  verified finite trace algebra.**
- **Forbidden events:** no nonzero event supported in the union of the `W`
  regions; no `Σ_i∩Σ_j`; no `H_i∩H_j`. This is arbitrary-base, not a finite
  surrogate inference. Next: track relations between columns.

### Iteration 10 — same-type pair relation

- **Result:** outside a countable exceptional set, two fibres of one type
  have either equal proper traces or are the two whole/empty corners. The
  relation `R_k=diag(D_k)∪{(0,U),(U,0)}` is closed under complement and
  disjoint union. **Evidence: hand proved.**
- **Obstruction:** a proper graph trace cannot be multiplied by a cylinder
  parameter which splits one type into two uncountable pieces. Next: derive
  the full per-type decorated grammar.

### Iteration 11 — upper decorated-form grammar and exact operations

- **Result:** modulo countably many columns each type is in binary mode
  (arbitrary whole/empty support) or one fixed proper-trace mode. Complements
  swap the binary support/complement or trace/complement. In a countable
  disjoint union, binary supports union; the presence of a proper trace
  annihilates binary support and at most six proper summands survive.
  **Evidence: hand proved.**
- **Operations checked:** complement, finite/countable disjoint union,
  comparable subtraction, cylinder decoration, residualization, countable
  modification. Intersection remains unavailable unless separately proved.

### Iteration 12 — split-support collector restrictions excluded

- **Result:** `G_ij∩cyl(A)` is absent whenever `A` and its complement both
  meet a support type uncountably, since it produces `(q,0)∉R_k` outside
  every countable exception. **Evidence: hand proved.**
- **Remaining case:** restrictions constant modulo countable sets on each
  type; next task was the transversal algebra.

### Iteration 13 — three-type transversal algebra

- **Result:** the closure of the six global trace triples and eight cylinder
  corners on one representative of each type has 88 profiles. A global event
  has a countable exception outside which every transversal triple lies in
  this algebra: a disjoint countable family has at most 18 nonempty profile
  triples. **Evidence: hand proof plus executable verification of `|Q|=88`.**
- **Forbidden profiles:** the only singleton-valued profiles are zero and the
  intended collectors; deleting either whole support type is absent. Thus
  collector restrictions with uncountable variation modulo countable support
  and unintended singleton/diagonal collectors are excluded. Proper
  co-countable restrictions are generated and harmless. Gate N still awaits
  equality.

### Iteration 14 — balanced finite-core census

- **Question:** do longer mixed closures reveal a missed finite splicing
  identity? Exhaustive core quotients on type words `123`, `123123`,
  `123^3`, `123^4` have respectively 88, 180, 700, 4428 events. All contain
  `H_i`; none contains a proper collector restriction, graph/residual
  intersection, or nonzero W-supported event. **Evidence: exhaustive finite
  evidence, stable JSON, separately recomputing verifier.**
- **Boundary:** local generators are omitted because on a finite base their
  finite union spuriously turns countable restrictions into arbitrary ones.

### Iteration 15 — intended collector is the graph-pair meet

- **Result:** any generated lower bound of `Σ_i,Σ_j` has empty unresolved
  sections by the local trace obstruction and singleton-bounded resolved
  sections, hence lies below `G_ij`; the collector is therefore their actual
  greatest lower bound. **Evidence: hand proved.**
- **Gate:** a Gate-L sublemma only. General latticehood is not established and
  Gate L is not opened.

### Iteration 16 — exact lower grammar reduced to finite-core splicing

- **Grammar attempted:** countable-column modifications of the finite global
  core `K`. Every proposed modification is generatable once its core is
  known. Countable disjoint unions collapse fibrewise to finitely many proper
  modes and a binary tail. **Evidence: conditional/open.**
- **First failed step:** the fibrewise collapsed coupled three-type profile
  has not been proved to be represented by one `K` element; removing the
  countably supported overlaps does not supply that finite identity.
- **Strategic update:** Gate N is sharply reduced to the finite-core splicing
  lemma, not passed. Next: hostile review and either prove the core identity
  from `Q` or find a `Q`-admissible non-core profile.

### Iteration 17 — scoped graph-network theorem

- **Result:** for any full-cylinder system with finitely typed global forms
  and column-local generators, every event has countably many exceptional
  columns and obeys the same-type Dynkin relation generated by the local
  diagonal and cylinder corners. When that relation is diagonal plus the two
  corners, no proper trace admits an uncountable within-type restriction.
  **Evidence: hand proved.**
- **Scope:** closure theorem only; it does not assert state selection or the
  target broad dichotomy. It closes the corresponding restriction mechanism
  for future finite typed graph systems. Hostile review is next.

### Iteration 18 — hostile review and quantifier repair

- **Review:** a fresh hostile pass found no flaw in countable dependence,
  fibre-trace obstruction, `R_k`, transversal `Q`, or the collector-meet
  corollary. It refuted the phrase “every uncountable proper restriction”:
  deleting countably many generated resolution points leaves a proper
  uncountable restriction. **Evidence: refuted wording; repaired theorem.**
- **Repair:** the invariant excludes exactly restrictions with uncountable
  variation modulo countable support, including the candidate's uncountable
  co-uncountable threat. Proper co-countable restrictions are generated and
  explicitly allowed. The certificate now checks the four singleton profiles;
  the verifier path is repository-root safe; “independent verifier” was
  downgraded to the accurate “separate recomputation” because the bit encoding
  is shared.
- **Gate status:** Gate N remains unresolved at finite-core splicing. All
  later gates remain closed. **Next single task:** decide whether every
  `Q`-admissible fibrewise collapse is a finite core profile; a counterexample
  refutes the exact grammar, while a proof closes the only identified equality
  gap.

### Iteration 19 — exact reconstruction and classification of Q

- **Question:** what are the mode strata and projections of the transversal
  relation? **Result:** `|Q|=88`; coordinate projections have size 24 and
  pair projections size 78. The binary-coordinate distribution is
  `44,36,0,8` for zero through three binary coordinates. **Evidence:
  executable verified**, stable explicit-profile certificate and separate
  declarative verifier. Runtime: producer 0.3824s, verifier 0.3835s.
- **Consequence:** there are 18 one-binary strata, all full unary relations;
  the all-binary stratum is the full cube; no two-binary/one-proper stratum
  exists. Every nonempty fixed-proper stratum is rectangular.

### Iteration 20 — automorphisms and minimal named generators

- **Result:** the incidence automorphism group has exactly six elements and
  is `S₃`. There are exactly three inclusion-minimal named generating sets,
  each of size eight: all six global forms plus any two type cylinders.
  Deleting a type cylinder preserves size 88; deleting a `Σ_i` leaves 68;
  deleting a collector leaves 44. **Evidence: exhaustive finite evidence,
  executable verified.** This classifies the finite relation but alone says
  nothing about arbitrary-base synthesis.

### Iteration 21 — semantic core parameterization

- **Question:** what is the previously ambiguous `K`? **Result:** `K` is a
  parameterized family: lift finite `Q` expressions uniformly across types,
  then decorate their zero types by arbitrary cylinder supports. A profile
  expression lifts because every profile-disjoint union is fibrewise
  disjoint on every column. **Evidence: hand proved.** `K` is not a finite
  set; the earlier wording was materially ambiguous and is repaired.

### Iteration 22 — anchor synthesis closes finite-core splicing

- **Result:** outside one countable exception, same-type polarity gives a
  fixed proper or binary mode. Choose a zero-valued representative from each
  genuinely varying binary type and arbitrary representatives otherwise.
  Universal transversal membership supplies one `q∈Q`; lift its expression,
  then add one cylinder carrying all varying binary supports. This core
  agrees with the event off the exception. **Evidence: hand proved.** The
  proof uses universal transversal admissibility, not pairwise projections or
  an inference from rectangularity.

### Iteration 23 — exact countable patching lemma

- **Result:** old and desired sections on the exceptional columns lie in the
  local `D_k`. Countably union the old supported sections `S`, subtract by
  `(K^c⊍S)^c`, and disjointly add the desired supported union `T`. Thus every
  upper-admissible description is generated, and conversely every
  countable-column core modification is generated. **Evidence: hand proved.**
  Arbitrary cylinder parameters and local generators are fully covered.

### Iteration 24 — exhaustive finite saturation census

- **Universe:** every ordered almost-disjoint core pair and every exceptional
  column subset in the exact 3-, 6-, and 9-column closures; success asks for a
  core with the prescribed union off the exception. **Result:** 735,
  103,565, and 26,770,371 type-surviving cases, respectively, with zero
  failures. Type-erasing exceptions have explicit failures (first masks
  1, 9, 73). **Evidence: exhaustive finite evidence with producer, JSON, and
  independently reconstructing verifier.** The census corroborates but does
  not prove the arbitrary-base theorem.

### Iteration 25 — Gate-N hostile reviews and verdict

- **Reviews:** two fresh-context audits independently reconstructed the
  candidate incidence, expression lifting, anchor quantifiers, and countable
  patch. One first identified the undefined-`K` defect; after repair neither
  found a remaining material gap. The uncountability-minus-countability
  hypothesis is essential and explicit.
- **Verdict:** **Gate N passes** by Theorem 8 of
  `oml_typed_graph_closure_calculus.md`. This is an exact upper membership
  theorem, not canonical uniqueness. Gates L, M, C, Z, F, and Φ remain open.
- **Strategic consequence:** proceed immediately to arbitrary-core
  latticehood while finite quotients search for the smallest mixed-core meet
  obstruction.

### Iteration 26 — exhaustive finite Gate-L census

- **Universe/result:** exact core quotients on 3, 6, and 9 balanced columns
  have 3,916, 16,290, and 245,350 unordered pairs. Exactly 18, 54, and 126
  pairs lack a meet, and the same counts lack a join. **Evidence: exhaustive
  finite evidence**, stable certificate and independently rebuilding verifier.
  This decisively selects a witness but is not the infinite proof.

### Iteration 27 — minimal missing-join witness

- **Result:** `A=cyl(T₁)` and `B=G₁₂` have upper bounds
  `U=cyl(T₁∪T₂)` and
  `V=(G₂₃⊍Σ₁)^c⊍(G₁₃⊍G₁₂)`. Both unions are legally disjoint. Any join
  profile lies between `(U,{g},0)` and `(U,{g,V_j,R},0)`, but `Q` contains
  no such profile. **Evidence: executable verified finite interval plus hand
  arbitrary-base proof.**

### Iteration 28 — profile-interval obstruction theorem

- **Theorem:** in any finite-typed concrete σ-class with a universal
  transversal invariant `Q`, generated `A,B` with upper bounds `U,V` have no
  join whenever `Q` misses the coordinatewise interval from `A∪B` to
  `U∩V`. A putative join's profile on representatives outside its countable
  exception gives the contradiction. **Evidence: hand proved.** This is a
  scoped graph-network closure/lattice dichotomy, not a sufficiency theorem.

### Iteration 29 — Gate L fails; rotating route closed

- **Verdict:** **Gate L fails** by Iteration 27. The rotating generated
  σ-class is not a lattice and hence not an OML. Gates M, C, Z, F, and Φ are
  not entered; no state-gluing claim is needed. The intended collector-meet
  result remains true but does not control mixed cores.
- **Auxiliary theorem:** every concrete complement/disjoint-union logic that
  is a lattice is automatically orthomodular: for `A⊆B`,
  `B\A=(A⊍B^c)^c=A^c∧B`. **Evidence: hand proved.** σ-closure is unnecessary.
- **Strategic pivot:** apply the finite-profile interval theorem to the
  broader typed graph architecture, then move to the highest-information
  theorem residue rather than modifying the failed rotating construction.

### Iteration 30 — finite cut-saturation theorem

- **Result:** for a universally realized finite profile relation `Q`,
  latticehood forces every finite cut `[⋁A,⋀B]` between uniform lower and
  upper profile families to meet `Q`. For finite `Q` with top and bottom this
  is equivalent to `Q` being a lattice under inherited coordinatewise order.
  **Evidence: hand proved.** It is necessary, not sufficient, for the
  arbitrary-base event poset to be a lattice.

### Iteration 31 — rectangularity/T4 inference refuted

- **Counterexample:** `{(0,0),(1,1)}` is a complemented two-element inherited
  lattice and cut-saturated, but nonrectangular. Thus latticehood's finite CSP
  condition does not force the rectangularity used in support splicing.
  Moreover event profiles contain no principal-state data, so no T4 inference
  follows without a state-side hypothesis. **Evidence: hand refutation.**

### Iteration 32 — state-side anchor analogy refuted

- **Counterexample:** in the compact space
  `C={0}∪{e_m:m∈ℕ}⊂2^ℕ`, let `G_n={e_m:m≥n}`. Every finite subfamily of the
  `G_n` intersects and all finite projections have the neutral anchor zero,
  but `⋂_nG_n=∅`; each good locus is nonclosed and accumulates at the bad
  anchor. **Evidence: hand proved/refuted.** Event-side cylinder decoration
  therefore has no automatic state-side analogue.
- **Reduction:** a positive boundary theorem needs either closed/compact good
  loci or an arbitrary-support coherent patching polymorphism, not finite
  projection consistency alone.

### Iteration 33 — countable fine-atlas T4 sufficiency

- **Theorem:** if the set of maximal blocks is at most countable and every
  maximal block is countably generated, then T4At implies Φ. On a nonempty
  finite face the non-σ restriction locus of each block is closed. A
  hypothetical absence of global σ-states gives a countable closed cover;
  Baire traps a finite-cylinder refinement at one block. T4At inserts a block
  atom, whose charged ultrafilter is principal and σ-additive, contradiction.
  **Evidence: hand proved, two independent hostile audits.** Zero-valued
  cylinder constraints are explicitly translated to complements.

### Iteration 34 — exact countable-atlas equivalence and residue

- **Result:** combining Iteration 33 with Lean theorem `t4At_of_phi` gives
  `Φ ⇔ T4At` for countable fine atlases. **Evidence:** reverse implication
  hand proved; forward implication Lean verified (axiom-free apart from
  standard classical/propext receipts already recorded). Any B′(i)
  counterexample must therefore have uncountably many maximal blocks and a
  genuinely distributed nowhere-dense cover of every bad finite face.
- **Narrow residue:** prove T4At for arbitrary fine OMLs, or control the
  uncountable atlas by a coherent arbitrary-support patching/compactness
  principle. Countable block generation alone does not reduce the atlas
  cardinality.

## Endgame continuation baseline (2026-07-13)

- **Starting branch/commit/worktree:** `oml-descent-sigma-essential-reduction`,
  `5a412563f7c1c348c3fbf0e261650a54cb7f452b`, clean.
- **Admissible class:** concrete sigma-complete non-Boolean OMLs, essentially
  irreducible in the programme's countable-ideal quotient sense, with
  sigma-additive two-valued states separating order.
- **Property:** `Phi(L)` says every finite trace of a global finitely additive
  two-valued state is reproduced by a global sigma-additive two-valued state;
  equivalently `St_sigma(L)` is finite-coordinate dense in `St_fa(L)`.
- **Evidence lock:** GSD and boundary surgery are hand-reviewed; finite raw
  interface quarantine is Lean verified; the countable-atlas converse is hand
  proved and its `Phi=>T4At` direction is Lean verified; Gate N is hand proved
  over executable local/Q/splicing certificates; Gate L is hand proved over
  an executable empty-interval certificate.
- **Closed classes:** finite boundaries; compact eligible local slices;
  common-base, one-interval, independent-fibre, trivial-monodromy and audited
  small-twist inflations; fully visible cyclic order coupling; the rotating
  typed-graph class (not a lattice).
- **Fine/coarse split:** fine defects are closure defects of point shadows;
  coarse countable-type defects are free-on-countable and the residual
  non-countable-type field is live. The full-block loci `N_B` and boundary
  defects `D_B` remain distinct, with `D_B subseteq N_B` only.
- **T4/T4At:** necessary in general fine OMLs; sufficient exactly for the
  proved countable fine-atlas theorem. Arbitrary-atlas sufficiency open.
- **Positive route:** hereditary boundary escape plus an OML-specific
  simultaneous-section theorem. **Negative route:** a distributed boundary
  trap with transported interfaces that passes latticehood, centre and
  sigma-state separation.
- **First task:** decide whether hereditary T4At escape implies countable
  support or whether a genuine Boolean boundary relation already refutes it.

### Iteration 35 — repository and certificate lock

- **Question:** do the post-baseline claims and receipts reproduce?
- **Result:** clean start recorded above. Verifiers reproduce local trace 24,
  core sizes 88/180/700/4428, `|Q|=88`, 19 strata, six automorphisms, all
  splicing saturation counts, and the Gate-L missing interval. `lake build`
  completes 2480 jobs. **Evidence: executable verified / Lean verified.**
- **Repair:** the local-trace verifier is CWD-sensitive; it passes from its
  certificate directory. This is a tooling defect, not a mathematical one.

### Iteration 36 — hereditary boundary escape from T4At

- **Theorem:** T4At implies one-block full and boundary escape on every
  coherent finite refinement: insert a block atom, take the witnessing global
  f.a. state, and restrict its atom-principal ultrafilter to the block.
- **Evidence:** hand proved; independent proof-first review cleared.
- **Consequence:** Question B is positive, but only locally; witnesses depend
  on the block/refinement and do not give GSD.

### Iteration 37 — topology-only countable support refuted

- **Counterexample:** on Cantor space, defects `{x}` indexed by all points
  cover the face; every countable subfamily is escapable; every defect is
  closed nowhere dense; every nonempty clopen refinement escapes each one.
- **Evidence:** hand proved, independently found by two agents.
- **Consequence:** compactness, Baire, point-countability and hereditary escape
  cannot prove Question A or arbitrary-atlas T4 sufficiency.

### Iteration 38 — singleton defects realized by fine Boolean blocks

- **Construction:** `A=Clop(2^N)` embeds in
  `B_x=Borel(2^N\{x})`. Sigma traces are exactly points other than `x`, while
  Boolean ultrafilter extension gives an f.a. lift of `x`; the defect is the
  singleton `{x}`. Each `B_x` is countably generated.
- **Evidence:** hand proved; a competing finite-cofinite formulation was
  hostile-reviewed and corrected because it is not a sigma-field overlap.
- **First OML failure:** the naive common-interface paste makes every
  nontrivial boundary event central and has no global sigma-state.

### Iteration 39 — abstract distributed trap classified at its first OML gate

- **Result:** the requested uncountable fine defect cover exists already at
  genuine local Boolean-boundary level. Its least possible closed-defect
  cardinal is `cov(M)`; the continuum singleton construction is ZFC.
- **Gate:** it is not an OML counterexample. Distributed transported copies
  must remove the common centre, after which binary cuts/latticehood are the
  first indispensable realization test; order separation is also absent in
  the naive paste. **Evidence: hand proved / construction rejected at gates.**

### Iteration 40 — coarse inverse limit and failure of naive countable determination

- **Theorem:** a boundary trace sigma-lifts iff its sigma-lifts over all
  countably generated block subalgebras can be chosen coherently under
  restriction. The union proof checks nonnested choices in a common generated
  subalgebra and countable additivity in one countably generated envelope.
- **Counterexample:** for the nonstationary/co-nonstationary field
  `A_club subset P(omega_1)`, every countably generated restriction of the
  club state has a point sigma-lift, but the full state has none: an extension
  would be a nonprincipal countably complete ultrafilter on `omega_1`, ruled
  out by Ulam's ZFC theorem.
- **Evidence:** hand proved; hostile definition check distinguishes the club
  filter on the power set from the ultrafilter on `A_club`.
- **Consequence:** Question E is negative in its naive form and positive only
  with a load-bearing coherence clause. Fine and coarse lanes now meet at
  OML-specific compactness of the compatible inverse system.

## Linked Campaign 1 — formalize ODBC exactly (2026-07-13)

### Iteration 41 — common-witness section spaces

- **Result:** for every coherent finite pattern and block subsystem `J`,
  defined `X_p(J)` to retain one full global f.a. witness `mu` and one
  boundary-matching eligible local sigma-lift per block. Restriction forgets
  lifts but retains `mu`. **Evidence: hand proved definition audit.**

### Iteration 42 — inverse-limit identification

- **Theorem:** `X_p(I)` is canonically the inverse limit over all finite, or
  all countable, block subsystems. A compatible family across subsystems is
  therefore already a global section. **Evidence: hand proved.**

### Iteration 43 — three quantifiers separated

- **Refutation:** pointwise local nonemptiness, objectwise finite/countable
  subsystem sections, and a compatible family of subsystem sections are
  distinct. In particular witnesses for different subsystems may use
  different global f.a. states. **Evidence: hand quantifier audit.**

### Iteration 44 — suppressed antecedent found and repaired

- **Hostile objection:** conditional globalization (CODBC) cannot imply
  `Phi` without proving whole-subsystem section existence. Finite event-face
  satisfiability does not solve infinitely many overlap equations in even
  two blocks. **Verdict: objection sustained.** ODBC was repaired to the
  conjunction ODBC-S plus CODBC.

### Iteration 45 — ODBC consequence of GSD

- **Theorem:** ODBC-S plus CODBC gives `X_p(I)`, exactly GSD, hence `Phi` by
  reviewed boundary sigma-surgery. Conversely GSD supplies both clauses, so
  the package is extensionally equivalent to `Phi` while exposing two
  separate proof obligations. **Evidence: hand proved over banked GSD.**

### Iteration 46 — fine and coarse specializations

- **Result:** fine eligible lifts are equivalently charged block atoms;
  coarse eligible lifts are coherent families over every countably generated
  block subalgebra. Mere local coarse nonemptiness is excluded by the club
  control. **Evidence: hand proved using banked block-Dirac and coarse-union
  theorems.**

### Iteration 47 — failure skeleton gates

- **Result:** failure inside an actual admissible OML is already a `Phi`
  counterexample. Only an abstract atlas failure remains a skeleton and must
  pass concreteness, lattice, maximal-block, sigma-completeness, centre,
  essential-irreducibility, state-separation, and lift-identification gates.
  **Evidence: hand proved classification.**

### Iteration 48 — Lean abstract section core

- **Result:** `ODBCSections.lean` verifies finite/countable/global compatible
  section definitions, countable-to-finite implication, the compactness
  wrapper, and `phi_of_odbc_sections` with the GSD extraction explicit.
  **Evidence: Lean verified.** Axiom receipts are
  `[Quot.sound]`, none, and `[propext, Classical.choice, Quot.sound]`.

### Campaign-1 hostile review and verdict

- The reviewer found the ODBC-S omission, prohibited calling objectwise
  nonempty subsystem spaces a compatible family, corrected the variance of
  restriction maps, and separated actual OML failure from abstract skeleton.
  All material objections were repaired in the focused note.
- **Campaign result:** exact ODBC is complete; ODBC itself remains open.
  Automatic pivot: Campaign 2, beginning with cut-saturation and the
  two-block full-boundary upgrade.

## Linked Campaign 2 — lattice cut-saturation (2026-07-13)

### Iteration 49 — finite profile cut-saturation

- **Definition/result:** PCS and DM-PCS formalize inherited profile intervals;
  finite DM-PCS is inherited latticehood. Scoped typed concrete latticehood
  implies DM-PCS by the banked interval theorem. **Evidence class: hand
  proved.**

### Iteration 50 — bare abstract cut-saturation implication refuted

- **Countermodel:** two eligible fibres demand opposite values of one common
  witness while the independent event relation is the cut-saturated diagonal
  two-element lattice. Singleton sections exist; the pair does not.
  **Evidence class: refuted.** Abstract only; the OML-coupled implication
  remains open.

### Iteration 51 — complete Boolean cut control

- **Result:** in `P(N)` a nonprincipal ultrafilter is finitely matched by
  point states but has no whole-boundary sigma lift, despite complete cuts and
  sigma-state order separation. **Evidence class: hand proved.** Its
  non-Boolean product control is centrally reducible.

### Iteration 52 — exact two-block positive theorem

- **Theorem:** an OML with exactly two maximal blocks and literal trivial
  centre has trivial boundaries, hence satisfies finite-interface quarantine,
  Phi, and ODBC. **Evidence class: hand proved.**

### Iteration 53 — finite-interface graph classes closed

- **Theorem:** finite generated boundaries imply ODBC for arbitrary incidence
  graphs, including trees, acyclic atlases, cycles and typed overlaps.
  **Evidence class: hand proved.** The raw-overlap core is Lean verified.

### Iteration 54 — finite-atlas quantifier correction

- **Result:** for a countable full atlas CODBC is tautological because its
  antecedent includes the full atlas; ODBC-S is already Phi. A proper finite
  subatlas must retain overlaps with outside blocks. **Evidence class: hand
  proved.**

### Iteration 55 — tree and cycle induction refuted

- **Result:** graph acyclicity glues independently selected traces, not one
  global f.a. witness matching whole boundaries. No unconditional coarse
  tree, acyclic, cycle or finite-typed theorem follows. **Evidence class:
  refuted.**

### Iteration 56 — relative closed-eligibility compactness

- **Theorem:** closed eligible relations in the compact product of the global
  f.a. face and block ultrafilter spaces, plus finite subsystem solvability,
  imply a global section by FIP. Surjectivity is unnecessary. **Evidence
  class: hand proved.**

### Iteration 57 — generic closedness route refuted

- **Counterexample:** `St_sigma(P(N))=N` is dense nonclosed in `beta N`.
  Eligible sigma loci therefore need not be compact or closed. **Evidence
  class: hand proved.**

### Iteration 58 — ML, fibre compactness, and softness audit

- **Result:** Cantor singleton sections `X(J)=C\J` have CSS without GS,
  nonsurjective restrictions, no Mittag--Leffler stabilization, and only
  empty/singleton fibres. Flabbiness or softness assumes the missing
  extension theorem. **Evidence class: hand proved.**

### Iteration 59 — three-block section-gate residue

- **Reduction:** the next full-atlas cardinal after the exact centre-free
  two-block theorem is a coarse three-block atlas. Singleton, pair, and
  triple intersection of its eligible common-state loci are separate gates;
  none is generically proved. **Evidence class: open.**

### Campaign-2 hostile review and verdict

- Hostile review corrected the countable-atlas quantifier, rejected
  centrality plus order separation for a fixed trace, and found no valid bare
  tree/cycle induction. These objections are incorporated.
- **Campaign result:** cut-saturation compactness is refuted abstractly;
  finite-interface, exact two-block and relative-closedness theorems are
  banked. Automatic pivot: Campaign 3 minimal countermodel.

## Linked Campaign 3 — minimal ODBC countermodel (2026-07-13)

### Iteration 60 — compact CSS-without-GS system

- **Construction:** `C=2^N`, `I=C`, and `X(J)=C\J`. Every countable
  subsystem has continuum many sections and the global system has none.
  **Evidence class: hand proved.**

### Iteration 61 — hereditary finite-coordinate escape

- **Theorem:** every nonempty finite-coordinate Cantor cylinder retains
  continuum many witnesses after deletion of any countable constraint set.
  **Evidence class: hand proved.**

### Iteration 62 — cardinal and finite-gate controls

- **Result:** singleton-cover CSS failure requires uncountably many indices;
  `aleph_1` is abstractly sufficient, while the Cantor version supplies the
  compact homogeneous refinement property. Singleton, pair, and conditional
  Helly-3 controls are explicit. **Evidence class: hand proved.**

### Iteration 63 — standard-Borel relation realization

- **Theorem:** for `B_R=Borel(R)` with coordinate clopen boundaries, the
  sigma-state trace relation is `R` and the f.a. trace relation is
  `closure(R)`. **Evidence class: hand proved.**

### Iteration 64 — singleton-exposure obstruction

- **Theorem:** a countably generated point-separating sigma-field contains
  every singleton, so restriction after deleting one point is noninjective.
  The singleton trap cannot be an overlap of that kind. **Evidence class:
  hand proved.**

### Iteration 65 — invertible transport identifies boundary ranges

- **Theorem:** a homeomorphic deterministic transport embeds its two clopen
  boundaries with the same range; a coherent connected cocycle network
  recreates one common boundary. **Evidence class: hand proved.**

### Iteration 66 — repeated-selector obstruction

- **Theorem:** blocks containing the same `e,f` contain the same intrinsic
  four-region Boolean subalgebra, so repeated selector containment cannot
  create inequivalent quotient edges or monodromy. **Evidence class: hand
  proved.**

### Iteration 67 — lattice completion comparison

- **Result:** raw crossed three-block unions fail closure; the 56-event
  completion saturates boundaries, but the 44-event centre-free OML retains
  a proper boundary and refutes universal completion-saturation. Its
  one-coordinate inflation is Phi-tame. **Evidence classes:** finite gates
  are exhaustive finite evidence; arbitrary-base tameness is hand proved.

### Iteration 68 — nondeterministic realization residue

- **Reduction:** a viable trap must use nonclosed nondeterministic
  correspondences with proper coordinate subalgebras and survive mixed OML
  completion. The first concrete test is a two-coordinate inflation in the
  44-event survivor. **Evidence class: open.**

### Campaign-3 verdict

- The compact-ambient abstract countermodel and local Boolean relations are
  complete; the eligible subsystem spaces are noncompact.
  Common-boundary, invertible-copy, repeated-selector, and raw-union routes
  fail exact gates. No admissible OML counterexample exists yet.
- Automatic pivot: Campaign 4 fine/coarse specializations, using the
  nondeterministic realization theorem as the persistent adversary.

## Linked Campaign 4 — fine and coarse ODBC (2026-07-13)

### Iteration 69 — fine bad-locus topology

- **Result:** under fine blocks and T4At, every full-block non-sigma locus
  `N_B(p)` is closed nowhere dense on each coherent finite face.
  **Evidence class: hand proved.**

### Iteration 70 — fine locally-countable-defect theorem

- **Theorem:** local countability of the nonempty `N_B(p)` reduces them to a
  countable family by compactness; Baire gives a global sigma-state.
  **Evidence class: hand proved.**

### Iteration 71 — fine countable-subcover theorem

- **Theorem:** it suffices that any covering family of block-bad loci admit a
  countable subcover. **Evidence class: hand proved.**

### Iteration 72 — point-countability refuted

- **Countermodel:** Cantor singleton defects are point-one yet cover the
  face. Point-countability, atomic fibres, and topology alone do not imply
  fine ODBC. **Evidence class: refuted.**

### Iteration 73 — finite-face transfinite repair scheme fails

- **Failure:** this scheme preserves finitely many atoms at successors, but
  limit stages accumulate an infinite face outside T4At's finite-face scope.
  It does not exclude every transfinite method. **Evidence class: refuted.**

### Iteration 74 — coarse CIR theorem

- **Theorem:** countable-intersection reflection turns separately solvable
  countably generated envelopes into one common point and coherent Dirac
  coarse lift. **Evidence class: hand proved.**

### Iteration 75 — club control identifies CIR failure

- **Result:** intersections of countable chosen subfamilies contain a club, while the
  total chosen family does not. The club field violates CIR and refutes
  objectwise coarse lifting. **Evidence class: hand proved.**

### Iteration 76 — coarse equivalence correction

- **Theorem:** coherent envelope families are exactly full block sigma-states,
  so coarse ODBC is ordinary ODBC/Phi rather than a logically weaker
  specialization. **Evidence class: hand proved.**

### Iteration 77 — joint state-separation audit

- **Result:** local point-state separation does not imply global OML
  sigma-state order separation; maximal-block enlargement can also move a
  Borel component out of the fine regime. **Evidence class: hand proved.**

### Campaign-4 verdict

- Unconditional fine and coarse ODBC remain open. The strongest exact
  specializations are fine countable-subcover reflection and coarse CIR.
  Campaign 5 is not entered because no candidate survived OML realization.
- Automatic pivot: Campaign 6 global integration.

## Linked Campaign 6 — global integration (2026-07-13)

### Iteration 78 — exact equivalence chain

- **Theorem:** `Phi iff GSD iff [ODBC-S and CODBC] iff coarse ODBC`.
  **Evidence class: hand proved.**

### Iteration 79 — stable positive-region ledger

- **Result:** finite boundaries, exact trivial-centre two-block atlases,
  countable fine atlases with T4At, fine CSR with T4At, and closed relative
  eligibility are the proved positive regions. **Evidence class: hand
  proved.**

### Iteration 80 — fine/coarse exhaustiveness not established

- **Result:** fine CSR and coarse CIR are sufficient conditions but no
  admissible-class theorem proves they are exhaustive; coarse ODBC is already
  the full conjecture. **Evidence class: open.**

### Iteration 81 — realization asymmetry

- **Result:** successful nondeterministic realization may give a
  counterexample after every gate, but failure closes only that class and
  does not prove Phi. **Evidence class: hand proved.**

### Iteration 82 — stopping-condition audit

- **Verdict:** stopping condition 3 is not met. ODBC is tautologically
  equivalent to Phi, and the current construction theorem lacks a
  completeness/normalization direction. **Evidence class: hand proved.**

### Iteration 83 — BOC normal form

- **Definition:** boundary-obstruction completeness consists of failure
  normalization plus realization-or-class-level-mixed-cut-collapse
  completeness. Both clauses are explicit. **Evidence class: open.**

### Iteration 84 — conditional Lean regime integration

- **Result:** `ODBCRegimes.lean` proves two conditional implication packages
  with explicit regime cover, ODBC, subsystem sections, and GSD hypotheses.
  **Evidence class: Lean verified.** Both report
  `[propext, Classical.choice, Quot.sound]`.

### Campaign-6 verdict

- Phi remains open; no complete counterexample or legitimate final decisive
  theorem exists. BOC is the next programme, not a claimed solution.
- Automatic pivot: Campaign 7 final hostile audit.

## Linked Campaign 7 — hostile audit (2026-07-13)

### Iteration 85 — positive implication audit

- **Verdict:** the hand chain, fine CSR, coarse CIR, and compactness/Baire
  uses survive at their exact hypotheses. **Evidence class: hand proved.**

### Iteration 86 — Lean quantifier mismatch isolated

- **Result:** the Lean atlas fixes the outer f.a. state, while note-level
  subsystem sections existentially choose a common `mu_J` that may vary with
  `J`. Lean verifies only abstract sufficient packaging. **Evidence class:
  hand proved.**

### Iteration 87 — negative realization audit

- **Verdict:** no abstract, Boolean, finite, or inflated construction passes
  the admissible OML and state gates. **Evidence class: hand proved.**

### Iteration 88 — two-coordinate status correction

- **Result:** the proposed two-coordinate inflation is unconstructed and has
  passed zero structural or state gates. **Evidence class: open.**

### Iteration 89 — BOC completeness gap

- **Result:** BOC must cover both a sectionless countable subsystem and
  CSS-without-GS; its finite-degree standard-Borel normalization may omit
  coarse/nonstandard failures. **Evidence class: open.**

### Iteration 90 — formal receipt audit

- **Result:** both Lean files compile without sorry/admit; all five axiom
  receipts reproduce exactly. **Evidence class: Lean verified.**

### Iteration 91 — iteration and stopping audit

- **Result:** Campaigns 1/2/3/4/6 contain 44 meaningful iterations. No
  stopping condition is met and the 60-iteration requirement prohibits
  completion. **Evidence class: executable verified.**

### Campaign-7 verdict

- No mathematical retraction is required, but scope and Lean-quantifier
  repairs were applied. Automatic pivot: Campaign 8 BOC normalization and
  two-coordinate testing.

## Linked Campaign 8 — BOC normalization and two-coordinate tests (2026-07-13)

### Iteration 92 — locally countable component theorem

- **Theorem:** finite-arity, countable-incidence constraint components are
  countable; CSS sections assemble componentwise to GS. **Evidence class:
  hand proved.**

### Iteration 93 — countable-witness corollary

- **Theorem:** every failure in that class has a sectionless countable
  component and is N-S, never N-G. **Evidence class: hand proved.**

### Iteration 94 — N-G cardinal lower bound

- **Theorem:** finite-arity N-G requires an uncountable-incidence variable,
  or else an infinite-arity/global constraint. **Evidence class: hand
  proved.**

### Iteration 95 — hidden-hub control audit

- **Result:** Cantor singleton uses an uncountably incident witness; any
  faithful finite-arity encoding of the club defect must expose a highly
  incident coherence coordinate. Ignoring such hidden coordinates gives a
  false finite-degree classification. **Evidence class: hand proved.**

### Iteration 96 — finite-degree N-S inhabitant

- **Construction:** the nonclosed standard-Borel descending-ray relation on
  `N times R` is finitely satisfiable and countably unsatisfiable at degree
  two. **Evidence class: hand proved.**

### Iteration 97 — exhaustive selector-pair proxy

- **Result:** among 496 pairs of 32 non-atomic selectors, 28 have distinct
  overlapping nonnested supports and exactly 24 also pass joint-state and
  three-region gates. **Evidence class: exhaustive finite evidence.**

### Iteration 98 — independent proxy verification

- **Result:** a direct-subset verifier reproduces 44 events, 10 atoms, 496
  pairs, 485 joint-state pairs, 135 three-region pairs, 28 support pairs, and
  24 qualifiers. **Evidence class: executable verified.**

### Iteration 99 — explicit independent selector normal form

- **Result:** selectors `0x000f` and `0x3300` are disjoint, have distinct
  supports meeting only in `A01`, give injective two-coefficient E/F/G
  forms, and avoid repeated-selector invariance. **Evidence class: hand
  proved.**

### Iteration 100 — finite simultaneous-inflation lattice gates

- **Result:** `P2xP2` has 24 points/116 events; `P2xP3` has 28/196;
  `P3xP2` has 28/212. All pass exhaustive closure, unique extrema,
  orthomodularity, exact five blocks, and centre two. **Evidence class:
  exhaustive finite evidence.**

### Iteration 101 — independent inflation and state audit

- **Result:** independent bit-mask reconstruction matches all counts and
  hashes. Finite concreteness, sigma-completeness, essential irreducibility,
  and global point-state order separation follow; all models are Phi-tame.
  **Evidence classes:** certificate is executable verified; state audit is
  hand proved.

### Campaign-8 verdict

- The chain has 61 meaningful linked iterations. The finite candidate passes
  every structural/state gate but is Phi-tame. Arbitrary-base latticehood,
  maximal blocks, and state relation remain open.
- Automatic pivot: Campaign 9 arbitrary-base two-coordinate theorem.
