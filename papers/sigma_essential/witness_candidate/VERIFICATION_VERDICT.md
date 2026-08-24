# Verification Verdict — Product Ulam Carrier (2026-07-06)

> **UPDATE (2026-07-06, later the same day): the construction is now
> MACHINE-CHECKED end-to-end.** `psiAmended_ZFC` (Theorem 7.1 → Ψ amended, in
> ZFC) compiles with **zero sorries** and axioms exactly
> `[propext, Classical.choice, Quot.sound]` — no cited axioms, no large
> cardinals. Chain: `SigmaEssentialAmended.lean` (encoding fix) →
> `UlamWitnessCore/Omega1/Invariant/State/Main.lean` (§2–§7 complete) +
> `Omega7Counterexample.lean` (Rem 1.5 — the amendment-forcing example —
> machine-checked) + `UlamWitnessReceipts.lean` (`#print axioms` receipts).
> **Gate α below is superseded** (Lean = the programme's ground truth; strictly
> stronger than a hand-pass for correctness). The remaining trust surface is
> **definitional fidelity only**: read the Lean definitions (`LocalState`,
> `FinAddState`, `TwoValuedState.val_iUnion`, `IsSigmaEssentialL`, `carrier`,
> `coreBlock`, `corePattern`, `PsiAmended` — ~15 minutes) against paper v2
> Defs 1.2–1.4. Gate β (prior-art book check) still stands — novelty, not
> correctness. One encoding note, checked and harmless: `LocalState` encodes
> only complement-additivity inside `B` (weaker than full Def 1.2 on `B`), but
> clause (0) coherence forces full statehood — any coherent local pattern is
> the restriction of a finitely additive state, hence fully additive on `B`.

⟦HAND — verified at LLM-adversarial level⟧ → upgraded same day to
⟦LEAN — 0-sorry end-to-end, standard axioms⟧ (definitional-fidelity read owed)

**Verdict: outcome (i), qualified — per statement:**

| Statement | Status |
|---|---|
| Ψ on σ-classes/OMPs, coherence-amended, irreducible **mod the countable ideal** | **RESOLVED in ZFC** (correct at LLM-adversarial level; gates α–β below before "SOLVED") |
| Ψ on orthomodular **lattices** (the form the programme's prose and memory name) | **OPEN** — conjectured to go the *other* way (latticehood ⟹ Φ, candidate §9.1) |
| Ψ with **literal** irreducibility (necessarily a no-singletons carrier) | **OPEN** — the candidate literally fails Def σ-essential's irreducibility clause (centre = ctble/co-ctble); mitigations §2.3 |
| [M] rem:technology ("no Boolean-ambient import") | **Not an amendment — a heuristic with a located hole**, half survived, half fell (§2.4) |

The candidate resolves the statement the programme *operated* on: [M]'s displayed
Def 1.1 is the σ-class (OMP), and the repo's Lean spine formalized the carrier as
`DynkinSystem` — when the programme's words ("OML") and its operational artifacts
disagree, the artifacts govern. The words' problem (lattice form) stays open.

Verifying session: 2026-07-06. Discipline: two independent adversarial proof
passes, mechanical enumeration of the finite core, devils-advocate on both cruxes,
hostile cross-field prior-art scout, thesis-advisor gate before this verdict.

---

## 1. The proofs are correct

Two fully independent passes (this session's hand pass; a fresh-eyes hostile-referee
agent with no access to the first pass) re-derived every load-bearing step:

- Lem 2.1 (Ulam matrix; column disjointness is EXACT — load-bearing in Thm 5.1,
  where the union of two same-column cells must lie in L);
- Lem 3.2 (representation rigidity, both cases exhaustive);
- Lem 3.3 (all four coordinate translations; all ten unordered cases; the case-(IV)
  coordinate-pair multiset re-derived by hand for each of the three coset pairs);
- Lem 3.4 (trichotomy: exhaustive; third-complementary-member exclusion correct);
- Thm 3.5 (normal form; the least-σ-class induction is valid; the ξᵢ* trimming is
  unnecessary but harmless);
- Cor 4.1–4.5 (incl. both inclusions of the centre computation);
- Thm 5.1 (rigidity; monotonicity/at-most-one legitimately derived, not assumed);
- Def 6.1 + Lem 6.2 + Thm 6.3 (ultrafilter facts; vote well-definedness under both
  representation changes; additivity in every table case);
- Cor 6.4 (all twelve cross-intersections are full fibers — s₀ is a state on B
  independently of m);
- Rem 6.5 (polarity check passed: m itself provably FAILS σ-additivity — the
  construction does not accidentally exhibit a rescuer);
- Thm 7.1, Prop 7.2, and the amended baseline Prop 1.6.

Mechanical check (`parity_core_check.py`, this directory — **scope: the finite
parity core ONLY**; the set-theoretic joints (3.4/3.5 induction, Ulam pigeonhole)
have no mechanical check yet): Ŝ is a transversal of the four complement pairs of
E₄; the 3.3(IV) multiset for all three coset pairs; A∩B unrepresentable; vote
well-definedness across ALL representations of all 128 finite-model sets;
additivity of m over 266 disjoint pairs × 5 ultrafilters. All pass.

**No mathematical error was found by any pass.** Four prose-level defects to fix
before promotion (none affects correctness):

1. **Cor 4.4**: proof text is literally garbled/unfinished mid-sentence; the correct
   inline argument (coords 2,3,4 exactly empty kills all three weight-2 cosets) is
   present and verified — rewrite it.
2. **Cor 4.2**: the case analysis swaps ξ/ξ′ against §0's convention E_f ≈ ξ^(κ_f)
   (conclusions invariant under the swap).
3. **Thm 3.5**: complement clause mislabels the normalized partner — the normalized
   rep of E^⊥ is (ξ′, κ), not "(ξ′, κΔ1111)". §6 computes it correctly.
4. **Cor 4.5 / Prop 7.2**: "the quotient has trivial centre" is asserted, not proved
   (a quotient's centre can exceed the centre's image). The transfer argument was
   checked and works — write the half page. This clause is part of amended Adm, so
   it is owed, not optional.

## 2. Crux A — the amendments, graded separately

Four deviations from [M]'s letter, not the three the author lists:

### 2.1 Global finite coherence (Def 1.3) — **FORCED (a repair [M] needs regardless)**
The Ω₇ example genuinely refutes [M, Prop 2.1] *as literally stated* (verified
independently twice: s₀ ≡ 1 on the three coordinate events IS a two-valued state on
B under [M]'s literal definition — only complement pairs constrain it — with empty
kernel, on a finite Boolean carrier where every state is Dirac). The broken step in
[M]'s proof: "s₀ extends to a finitely additive state on B₀" is false for sparse
sub-orthoposets. Independently corroborated: the repo's own Lean baseline proof
needed an extra hypothesis (`hBinter`/`BooleanLocal`) the paper doesn't have.
The literal reading also trivializes Wright's finite-witness bar and breaks the
Derr–Williamson interface (DW coherence IS global/de Finetti — under the literal
reading Ω₇ would "refute" DW too). **Erratum to [M] owed either way.**

### 2.2 OMP, not lattice — **nomenclature repair (defensible); headline must say OMP**
[M]'s displayed definition and every formal artifact (Q:bare, `DynkinSystem`, the
DW interface) are OMP-native; [M]'s "equivalently a σ-class" is false — this
construction is itself the counterexample (**second [M] erratum**). The OMP form is
resolved; the OML form — what every prior programme document names — remains open,
now with a sharp conjecture attached (latticehood ⟹ Φ; if true, the OMP/OML
boundary is exactly the boundary of σ-essential contextuality).

### 2.3 Irreducibility mod the countable ideal — **genuine weakening, METHOD-forced**
Literal irreducibility is provably impossible for any carrier containing all
singletons (every countable set is central — verified). But nothing proves a
witness must contain singletons; "forced by the method" ≠ forced by the problem.
A literally-irreducible reading (no-singletons regime, different rigidity
mechanism) is consistent and OPEN — hence the third table row. Mitigations,
verified: centre computed exactly (Cor 4.5); m annihilates it; the pattern survives
the quotient, whose centre is trivial (modulo prose fix §1.4); the clause's PURPOSE
(excluding segregated carriers) is preserved and v2 upgrades rem:segregated to a
proved lemma (lem:horizontal). Structural residue, honestly: the irreducible
contextual core lives in the quotient, which is not concrete (St_σ(quotient) = ∅
while concrete σ-classes always carry Diracs).

### 2.4 rem:technology — a heuristic with a located hole, NOT an amendment to Ψ
The formal sentence Ψ never contained an intrinsic-ness clause; rem:technology is a
prose constraint whose supporting argument ("in a Boolean ambient the pattern
globalises") addressed importing INCOMPATIBILITY and never addressed importing
RIGIDITY. Split verdict: **"the incompatibility must be intrinsic" SURVIVED** — the
candidate's incompatibility is native to the fiber parity code, and does necessary
work (Prop 1.6: no Boolean carrier hosts a coherent empty-kernel pattern);
**"therefore nothing can be imported from the Boolean ambient" FELL** — rigidity is
imported from P(ω₁) (Ulam), and v2's rem:coherence-location states the division of
labour openly. The frontier's "native non-distributive skeleton" demand was met for
the incompatibility half, deliberately not for the rigidity half.

## 3. Crux B — genuine, not the degenerate sibling (with one honest asterisk)

- The "Dirac-only ⟹ degenerate" framing (tree-incidence detector) was calibrated to
  the coherence-FREE reading, where "witness" collapses to clause (i) alone. Under
  the amended (= repaired, §2.1) definition, a Dirac-only witness additionally
  requires a globally coherent empty-kernel pattern — precisely what
  horizontal-σ-sum/segregated carriers provably cannot host (v2 lem:horizontal) and
  what the parity code newly achieves (Lem 3.3(IV): the additivity certificate that
  would link the three cores cannot form). Total σ-rigidity is the *maximal*, not
  degenerate, satisfaction of clause (ii): Navara–Pták failed as a witness because
  it supplied its own rescuer; this carrier provably admits none. That is [M] §2's
  own blueprint ("break (a) while leaving no repair available") executed.
- **The asterisk**: relative to [M]'s *other* gloss of the core — a non-principal
  coherent σ-ADDITIVE selection existing across incompatible blocks (Q:bare (a)–(d)
  as literally worded) — the candidate certifies that object's ABSENCE on its
  carrier; the σ-level killing power is Ulam's theorem, imported. Both glosses
  coexist in [M] because Q:bare has a polarity muddle (already flagged in the
  repo's Lean BareForm notes). Whether some admissible carrier hosts the positive
  selection object remains open — that sub-question, not Ψ, is where
  large-cardinal strength may still live. Keep the two statements distinct in the
  record: "candidate cardinal = measurable" was about the literal Ψ's bounds;
  "ZFC, no strength" is a property of the amended OMP form. Two different
  sentences, two different statuses — not an oscillation.
- The in-repo Lean "certificate" cited by the handoff for crux B is **vacuous** and
  disqualified from evidence in BOTH directions (§4).

## 4. Independent finding: the Lean witness-encoding is broken

`SigmaEssentialLocalization.lean` types the pattern s₀ as a global `TwoValuedState d`
(σ-additive by definition). Hence `Extends s₀ s₀ B` holds trivially,
`IsSigmaEssential` is unsatisfiable, the formalized `Psi` is **provably false as
encoded**, and `diracOnly_with_clause_i_gives_witness` has jointly contradictory
hypotheses. Machine-checked: `QuerySystem/EncodingDefectCheck.lean` (compiles clean)
proves `extends_refl`, `isSigmaEssential_unsatisfiable`, `psi_false`,
`diracOnly_certificate_vacuous`. Consequences:
- The handoff's crux-B premise ("our Lean already proves this path is a valid
  witness of the formalized definition") is void — as are the tree-incidence
  "degeneracy" theorems built on the same predicate. Neither side of crux B may
  cite the current Lean layer.
- `formalization_status.md` / MEMORY.md / taxonomy `lean` fields citing the
  witness-predicate theorems need downgrading: theorems true as compiled, but the
  predicate they quantify is degenerate. (Unaffected: `dirac_iff`, derived
  monotonicity/at-most-one, the FIP content of `boolean_not_sigma_essential`.)
- This correction should land as a **standalone commit** (record hygiene
  independent of the candidate's fate).
- Fix: re-encode the pattern as a LOCAL state (values on `B.sets` with
  complement-additivity inside B), then re-prove localization. Compatible with the
  candidate's §8 encoding plan.

## 5. Prior art (hostile scout, web, 2026-07-06)

**ADJACENT — apparently empty at the exact statement.** Every component is
classical; the conjunction was not found under any vocabulary tried:
- Boolean skeleton = Ulam 1930 (P(ω₁)/ctble has f.a. 2-valued states, no σ-additive
  ones) — textbook.
- The empty-kernel triple gadget is in **Navara–Pták 1983's own example** (on ℚ×ℚ,
  used in the OPPOSITE direction — a non-concentrated σ-additive state). Credit
  lineage (they credit Dravecký–Šipoš) when writing up.
- Diracs-only two-valued state spaces on concrete logics: Burešová–Pták 2023
  (arXiv:2401.13798) — finitely-additive side, representation theorem, no f.a./σ gap.
- Ulam-measurability ↔ σ-additive singular states: Kornell (arXiv:1607.08505),
  Farah–Weaver line, Dzhenzher 2026 — B(H) carrier, opposite side of the dial.
- Derr–Williamson 2023: the candidate sits exactly in the cell their hypotheses
  exclude — complementary, not contained.
Honest novelty framing: **"a new assembly of classical parts closing the
beyond-Polish cell left open by Derr–Williamson"** — not a new mechanism.
Assembly-rediscovery is the modal risk: hand-check Pták–Pulmannová 1991 (examples
chapters) and Navara's "Existence of states" survey (Handbook of Quantum Logic,
2007) — the scout had no MathSciNet/zbMATH; Russian school (Mushtari/Matvejchuk)
only surface-scanned.

## 6. Gates before "SOLVED" (in this order)

1. **(α) User hand-verifies the §8 top joints** (hours; highest safety/hour;
   correlated-LLM-error is this programme's documented failure mode): Lem 3.3(IV)
   multisets, Lem 3.4→Thm 3.5 induction incl. third-complementary-member exclusion,
   Lem 3.2 — plus the Ω₇ refutation of [M] Prop 2.1, which the author must own
   regardless of the candidate's fate.
2. **(β) Prior-art book check** (days): Pták–Pulmannová 1991 + Navara's Handbook
   survey.
3. **Lean, last, two stages**: (3a) commit the §4 encoding-defect correction now,
   standalone; (3b) after gates α–β, formalize **Theorem 7.1 end-to-end**
   (3.3→3.4→3.5→5.1→6.3 chained) — not a sub-lemma; the countable-additivity note
   died by Lean-ing a true sub-lemma of a false theorem.
4. The four prose fixes (§1) and the two [M] errata (§2.1, §2.2). **Do NOT let v2
   replace `sigma_essential.tex` before gates α–β pass** — freeze v1; exception:
   the Ω₇/Prop 2.1 erratum lands in v1 regardless.
5. Then Phase-2 `/audit full` (Type-1 bar; the scout report is the starting
   dossier).

## 7. The terminus (anti-oscillation record)

The 2026-07-02 terminus decomposes; do not rewrite it in place — append this:
- **Mathematical content STANDS**: every wall proven for the walked routes and for
  the literal lattice form is unrefuted. The candidate goes *around* (a two-layer
  design: Boolean rigidity layer ⊗ native parity incompatibility, coupled only
  through the countable ideal), not through.
- **Strategic judgment FALSIFIED**: "not close; every importable object bottoms at
  Wall A" was an inductive generalization from 13 carriers whose sample contained
  no two-layer design. That is the located hole; the induction is not relitigated.
- **Why this is not swing #5**: the four prior swings were evidence-free
  reinterpretations of one proposition; this update is evidence-typed (a new
  object) and splits the proposition (amended form resolved / literal-OML form
  still walled).
- **Reversal trigger (binding)**: a future downgrade of this verdict is licensed
  only by (a) a located error in the object, or (b) a prior-art hit — never by
  re-reading.
