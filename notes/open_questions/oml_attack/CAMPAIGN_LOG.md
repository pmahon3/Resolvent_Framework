# σ-essential-state research campaign log

Direct research on the OML branch is the active workflow. Iterations are
appended below the baseline; each records question, construction/lemma,
evidence class, gates passed, first failure, obstruction, strategic update,
and next task.

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
