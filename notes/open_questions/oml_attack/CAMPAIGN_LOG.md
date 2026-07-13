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
  A = ctble/coctble(ω₁) FAILS admissibility (quotient = Boolean P(4)) —
  caught before it could contaminate later work;
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
