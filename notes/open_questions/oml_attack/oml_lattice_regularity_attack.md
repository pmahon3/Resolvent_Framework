# Theorem 2 attack — the OML-lattice case at the regularity transition

**Non-atomic pullback outcome:** [`oml_nonatomic_pullback_completion.md`](oml_nonatomic_pullback_completion.md)
completes `(5,11)` as a centre-free nonrectangular but `Phi`-tame one-edge
inflation; the next gate is two inequivalent quotient edges.

*Opened 2026-07-10 (session 8), per `shovel_plan.md` §2 + §Execution-order.
This is the attack-opening note the frontier map prescribes: collect the three
meet-destruction mechanisms into one frame; say what a unified
liftability-from-latticehood argument needs; find where it first breaks.
Yield = sharpened conjectures + named obstruction, not a proof.*

*Status of §§1–8: ⟦HAND⟧ framing over verified corpus pointers; no new
theorem claimed there. §7c (s9), §9 (s11), §10 (s13), and §11 (s15) DO
bank theorem-lets — ⟦HAND⟧, machine- or adversarially corroborated,
fresh-context proof-read (s10/s12/s14; §11's s12-standard proof-read
OWED), not Lean; see each section's own status line.*

*2026-07-12 centre-removal follow-up:* see
[`oml_irreducible_boundary_test.md`](oml_irreducible_boundary_test.md).
Two blocks cannot carry a noncentral common interface; the smallest
three-block crossed-interface paste fails raw closure but has a 56-event
centre-free concrete OML completion. Its seven maximal-block boundaries all
saturate. The remaining fork is infinite coarse inflation and finite-face
exposure, not finite completion.

*2026-07-12 seven-block inflation update:* see
[`oml_seven_block_inflation.md`](oml_seven_block_inflation.md). The direct
common-base class preserves the seven blocks, saturated boundaries, and
coarse dense-nonopen topology but restores the base as a central factor.
The then-next gate was a genuinely distributed-base substitution; the
following update records its one-interval resolution.

*2026-07-12 one-interval outcome:* see
[`oml_distributed_sigma_selection.md`](oml_distributed_sigma_selection.md).
The fibre below `q_0` propagates through `B,D0,D1`; the completed arbitrary-
base family has seven blocks, trivial centre, saturated boundaries, and a
face-exposed noncompact eligible slice. It is `Phi`-tame because the inverse
system has only one coarse coordinate. The next construction must couple at
least two inequivalent fibres around a skeleton cycle.

*2026-07-12 two-fibre atom-selector outcome:* see
[`oml_two_fibre_monodromy.md`](oml_two_fibre_monodromy.md). The smallest
jointly coherent pair `(q0,2)` occupies a five-cycle, and its finite
approximants close as centre-free seven-block OMLs. However the propagation
supports are disjoint, the induced relation is the full product, and
monodromy is identity. This closes independent lattice-atom interval
substitutions; the residual class must use non-atomic intervals or proper
shared subalgebras that create a block seeing both coordinates.

---

## 1. Statement of record

**Question (Ψ_OML).** Does a concrete σ-complete non-Boolean essentially
irreducible orthomodular **lattice** carry a σ-essential state — i.e. is
there `L ∈ Adm ∩ OML` with `¬Φ(L)`? (Φ, Adm as in
`papers/sigma_essential/sigma_essential_body.tex` §Discussion.)

**Conjecture: NO** (latticehood ⟹ Φ). Either exit completes the crossing
(shovel plan §2): tame ⟹ *the phenomenon lives strictly between orthomodular
poset and orthomodular lattice*, non-latticehood certified as the
discriminator; a lattice witness ⟹ strictly bigger theorem than
`psiAmended_ZFC`.

Guard: MO₂ is a lattice and the disjointification identity
`(a∨b)∧a⊥ = b∧a⊥` already fails on it. So latticehood does **not** restore
distributive/equational transfer — any proof of the conjecture must be
structural (representation- or block-theoretic), not identity-based. The
wall (`wall.disjointification`) is not the lever here.

## 2. The decomposition (this session's first sharpening)

Non-segregation and non-Polish-representability are *consequences* of
witnesshood (lem:horizontal + Derr–Williamson), so the honest prior class is
`𝒞 = {concrete, σ-complete, non-Boolean, essentially irreducible OMLs}`.
The conjecture splits:

- **(2a) Inhabitation / representability.** Is every `L ∈ 𝒞`
  Polish-representable? If YES, Theorem 2 follows outright via
  Derr–Williamson (Polish ⟹ Φ). *(s13: FALSE as stated — D.6 carries a
  binding third leg, blockwise inner regularity; see §10d(i).)* Call this
  the **representability form**:

  > **Conjecture 2a.** Every concrete σ-complete essentially irreducible
  > non-Boolean orthomodular *lattice* is Polish-representable.

  All the corpus's meet-destruction evidence (§3) is really evidence for 2a:
  every known escape from Polish-representability destroyed a meet.

- **(2b) Direct tameness.** If 𝒞 has non-Polish inhabitants, prove Φ on them
  directly (engines in §4), or hunt the witness there (the realization-push,
  §5 falsification side).

2a is the right first target: it is a structure-theory question about
concrete OMLs (variety by Godowski 1981; finite-basis OPEN, Harding 2004),
not a state-extension question, and its literature is the Czech-school
corpus already mapped (`../sigma_essential/czech_school_prior_art_sigma_essential.md`).

## 3. The three meet-destruction mechanisms, collected

The frontier map asserts "three independent meet-destruction mechanisms"
with no enumeration anywhere in the repo. Collected here for the first time,
one per transition:

1. **σ-class trace-rigidity** *(regularity — the witness's own anatomy).*
   In the product Ulam carrier the lower bounds of {A₁,A₂} are exactly the
   countable subsets of M×{1}, an ω₁-chain with no maximum: A₁∧A₂ does not
   exist (Cor. "incompatibility; not a lattice",
   `sigma_essential_body.tex:713`). σ-classes close under complements and
   countable *disjoint* unions only; the rigidity normal form forbids any
   element from serving as maximal lower bound. Witnesshood and meet-failure
   have a common cause.

2. **Pasting/loop mechanism** *(pasting).* Greechie/finite pastings of
   Boolean blocks generically produce OMPs that are not lattices (loop
   lemma; Jenča 2001 Ex. 5.7: the Wright-triangle sharp skeleton is a
   non-lattice OMP — `../sigma_essential/sharp_skeleton_RDP_subroute_verdict.md`). Where
   pasting does give concrete lattices the results are confined to
   finitary Kalmbach-type K(L) (Mayet–Navara 1995) — no σ. The located
   literature gap: *no paper realizes a non-simplex state space on an OML
   simultaneously concrete AND σ-complete*
   (`../sigma_essential/czech_school_prior_art_sigma_essential.md` §POSITIVE).

3. **RDP/center collapse** *(sharpness).* Any lifting engine bought via
   Riesz decomposition forces sharp = central = Boolean (Jenča 2001
   Cor. 4.3 + Greechie–Foulis–Pulmannová 1995); a non-Boolean sharp
   skeleton *witnesses* RDP failure. Meets survive the tame engine only by
   going Boolean.

**The one frame.** Each mechanism is an instance of: *the known
non-segregated non-distributivity sources at σ-scale live off the lattice
locus, and the known tame engines (RDP, Polishness) collapse or bypass
non-Boolean latticehood.* The conjecture says this is not an accident of
the walked sample.

**New synthesis ⟦HAND⟧ (block-overlap observation).** In any OML, block
overlaps are automatically **meet-closed**: for a,b in blocks B₁∩B₂,
compatibility puts a∧b in each Bᵢ (Boolean operations of compatible
elements coincide with the lattice operations — standard). But the 5-axis
gluing map (`fact.gluing_axis_map`, taxonomy) pins axis 2 for witnesshood
to *disjoint-union-closed ONLY*, with meet-closed → Floor/Boolean recorded
as a death. So **latticehood forces every gluing presentation onto axis
2's dead value**. Caveat, honestly: the axis-2 death is an *empirical
pattern over walked carriers*, not a theorem. Upgrading it to a theorem in
the lattice case *is* one full proof skeleton for Theorem 2 (Skeleton B,
§4).

## 4. What a liftability-from-latticehood argument needs

Named engine slots, in decreasing directness. The obstruction (§6) is that
the two *proved* engines bracket the conjecture without touching it.

- **Skeleton A (representability → DW).** Prove Conjecture 2a; DW finishes.
  *(s13: DEMOTED — DW finishes only with the blockwise inner-regularity
  leg, which fails on coarse-riding states; §10d.)*
  Needs: a representation theorem for concrete σ-complete irreducible
  non-Boolean OMLs. Known inputs: concrete = full 2-valued state set
  (Godowski 1981); concrete OMLs a variety, finite basis OPEN (Harding
  2004); K(L)-concreteness finitary (Mayet–Navara 1995). First probe: is
  there ANY known member of 𝒞 that is infinite? (MO₂-type irreducibles are
  finite; products/horizontal sums are reducible/segregated; projection
  lattices fail concreteness by KS.) If 𝒞's infinite locus is itself
  unpopulated in the literature, 2a may be open-but-unasked — a good sign
  for a contribution either way.

- **Skeleton B (block-overlap dichotomy).** Make the axis-2 death a
  theorem for lattices: rich-but-partial **meet-closed** overlaps at
  σ-scale force a Boolean/segregation dichotomy (overlap trivial →
  horizontal-sum-like → lem:horizontal lifts; overlap full → Boolean →
  Prop-boolean lifts). MO₂ is the toy confirmation: it *is* the horizontal
  sum of two 4-element blocks. The work: exclude the middle at σ-scale
  when overlaps are meet-closed. *(Session 11: structural form REFUTED
  at finite scale — the Greechie pentagon is in 𝒞 and is neither Boolean
  nor a horizontal sum; the surviving form is Φ-level. Cold-attack record,
  partial theorem-lets, and sharpened Conjecture B′: §9.)*

- **Skeleton C (Jauch–Piron forcing) — the candidate "idea".** A 2-valued
  state s is JP (lattice form) iff s(a)=s(b)=1 ⟹ s(a∧b)=1. On the OMP
  witness this is not even statable at {A₁,A₂} — the meet is absent;
  latticehood makes it statable everywhere, and the witness's vote state
  would flatly violate it (m(A₁)=m(A₂)=1 while every lower bound is
  countable, hence m-null). So a theorem of the shape *"on a concrete
  σ-complete OML, σ-additive 2-valued states are JP"* + *"JP + concrete +
  σ ⟹ extension"* would kill any lattice witness at the anatomical level.
  Literature to pull: Bunce–Wright (JP automatic on vN projection
  lattices), Navara–Pták JP papers, Müller 1993 (non-Boolean concrete
  logic with all states JP — *finite-flavored*, so not a counterexample to
  the σ-form; `../sigma_essential/czech_school_prior_art_sigma_essential.md` §4).
  **SWEPT session 9 — REFUTED as stated (MO₂ counterexample; §7c(ii)).**
  Survives only via PP1994 σ-unitality (§7b) or with MO₂-excluding
  wildness hypotheses.

- **Reduce-to-Dirac probe (feeds A and C).** rem:strength: reduce-to-Dirac
  is a σ-*algebra* theorem unavailable on σ-classes. Is it available on
  σ-complete concrete OM *lattices*? If yes, the Ulam import that powers
  the witness becomes self-defeating on lattices.

## 5. Falsification side (kept honest)

The only live constructive route to ANY fourth-cell object is the
realization-push (Navara–Rogalewicz 1988 / Harding–Navara 2000 pasting
machinery pushed to concrete + σ simultaneously; import sweep closes
everything else). A lattice witness needs that push to ALSO preserve
latticehood — the conjunction gap now has **three legs: concrete, σ,
lattice** — while the pasting machinery generically breaks all three
(axis-3/axis-5 tension; loop lemma). Anyone attempting the witness side
should attack the three legs jointly, not sequentially.

## 6. The named obstruction

**The engine gap.** The two proved lifting engines bracket the conjecture:
RDP is *too strong* (forces Boolean — Jenča; nothing non-Boolean left to
lift on) and Polish/inner-regularity is *not known to apply* (needs
representability, which is exactly 2a — *s13: and more; even given 2a the
inner-regularity leg fails on coarse-riding states, §10*). No theorem occupies the gap, and
the identity-based route is closed by MO₂ (§1 guard). Every corpus death
is consistent with the conjecture but none proves it; the axis-2 death is
empirical. The missing mathematics is one of: a representability theorem
(A), a meet-closed-overlap dichotomy (B), or a σ-JP forcing theorem (C).

## 7. Entry reading, mapped to this attack

Per `sigma_essential_skill_plan.md` (START = Kechris Ch. 12–14 + Phase-0
re-read), with the thm-2-specific "read it for" question attached:

- **Phase 0 re-read** (bounds §3f, §3j; Lean polarity gate
  `builds_state_implies_not_witness`): keep definability-vs-existence
  straight before touching DW.
- **Kechris Ch. 12–14** (standard Borel spaces): what Polish-representability
  actually buys — on Polish Ω, Borel probability measures are Radon, so
  DW's inner-regularity is near-automatic (`../sigma_essential/sigma_essential_prior_art_verdict.md`).
  *(s13 correction: NOT near-automatic — Radon compacts live in Borel, not
  in the block; the leg is binding, §10d(ii).)*
  Read for: which step could *latticehood* conceivably re-supply.
- **DW 2023 Thm D.6 + Maharam 1972 §8**: locate the load-bearing
  inner-regularity line (skill-plan primary-source question, verbatim);
  then ask it for Skeleton A.
- **New pulls for this attack** (not in the skill plan): Harding 2004
  (in-hand, `harding_2004_concrete_oml.pdf`) re-read for the variety/basis
  question; Müller 1993 (in-hand) for the JP landscape; Bunce–Wright JP
  papers (to fetch); Kalmbach 1983 textbook (still to fetch, block/commutator
  theory for Skeleton B).

## 7b. Scout results (2026-07-10, same session — sonnet scout, web)

The JP line and the inhabitation probe were scouted before any hand
investment. Verbatim-grade findings (citations triangulated from full texts
of Tkadlec 1997, Müller–Pták–Tkadlec 1992, Navara 1996 unless flagged):

- **Skeleton C is live and partially pre-built.**
  - *Tkadlec 1997* (Tatra Mt. Math. Publ. 10, 55–62), Prop 3.3(A): **every
    OML automatically has the "property of maximality"** ([0,a]∩[0,b] has a
    maximal element — trivial, infima exist); Thm 4.2: weakly-Boolean +
    maximality ⟹ Boolean. Latticehood buys one hypothesis of a
    Booleanness-forcing theorem for free.
  - *Pták–Pulmannová 1994* (Comment. Math. Univ. Carolin. 35, 205–208):
    an **OML with a unital set of subadditive probability measures is
    Boolean** — lattice-level, and 2-valued JP states are subadditive
    (Tkadlec 1997 Lemma 1.3). So a lattice witness must have either a
    non-JP σ-state or (what actually fails at wildness) a **non-unital
    family of σ-additive 2-valued states**. Proof-shaping: the witness
    hunt and the JP engine meet exactly at σ-unitality.
  - *Bunce–Hamhalter 2000*, "Jauch–Piron states and σ-additivity", Rev.
    Math. Phys. 12(6), 767–777 — **title-exact for the σ-JP forcing
    question, vN-projection-lattice scope, content unverified (paywalled,
    no preprint located)**. Pull this.
  - **Negative finding:** no theorem of shape "σ-additive 2-valued state on
    a σ-complete OML ⟹ JP" located for general (non-operator-algebraic)
    OMLs. The σ-JP forcing question appears open-but-unasked at our level.

- **The critical citation gap: BNPW 1985.** Bunce–Navara–Pták–Wright,
  "Quantum logics with Jauch–Piron states", Quart. J. Math. Oxford (2) 36
  (1985), 261–271: constructs a non-Boolean concrete logic **all of whose
  σ-additive states are JP** (the "no" to Müller–Pták–Tkadlec 1992
  Question 5.4 in the σ-case). So "all-states-JP ⟹ Boolean" fails at the
  concrete-*poset* level even σ-additively. **Lattice-vs-poset status of
  the BNPW construction unverified** (paywalled; every citing source says
  only "concrete logic"; pattern-inference says poset). If BNPW's object
  were a σ-complete *lattice* it would gut Skeleton C's second half; if a
  poset, the lattice conjecture is untouched and BNPW becomes another
  every-wild-object-a-non-lattice data point. **Pull the primary source
  before any Skeleton-C hand-work.**

- **Q3/inhabitation: explicit negative.** No example located, anywhere, of
  an infinite concrete σ-complete non-Boolean irreducible orthomodular
  **lattice** (Polish or not). Every infinite non-Boolean concrete JP-type
  witness in the literature (BNPW 1985, Müller 1993, Navara 1996 Ex. 5.2
  kernel logics) is described only as a "concrete logic"/OMP, never
  asserted a lattice. Conjecture 2a is consistent with the entire located
  literature and plausibly **open-but-unasked**. Unexamined leads:
  arXiv:2308.08508 (completely hereditarily atomic OMLs); PP1991 + DP2000
  book chapters on set-representable σ-lattices (tables of contents not
  accessible to the scout); "On Set-Representable Orthocomplemented
  Difference Lattices", Order 2020 (ODLs, adjacent only).

- Also confirmed tame-side special cases (evidence FOR the conjecture, all
  with countability/finiteness hypotheses): Müller–Pták–Tkadlec 1992
  Thm 4.1 (concrete + all-states-JP + countable dense set ⟹ Boolean),
  Thm 4.2/Cor 4.3 + Rogalewicz 1991 (finitely many blocks ⟹ Boolean),
  Müller 1993 Thm 3.5 (per Tkadlec's citation, under complete additivity).

**Paywalled pulls now owed (join the standing two):** BNPW 1985 (decisive,
first priority); Bunce–Hamhalter 2000; PP1991/DP2000 chapter scans.
*(Session 9 update: BNPW pull DEMOTED to confirmation-only — resolved by
derivation, §7c. B–H 2000 still owed. Skeleton C's first half REFUTED as
stated — see §7c.)*

## 7c. Session 9 (2026-07-10): MPT 1992 primary text pulled — BNPW resolved by derivation; Skeleton C's first half refuted

The scout's decisive source, Müller–Pták–Tkadlec 1992 (IJTP 31, 843–854),
was pulled and read directly (PDF now in-hand:
`notes/literature_review/literature/muller_ptak_tkadlec_1992_covering_properties.pdf`,
from Tkadlec's page). Verified verbatim:

- **Definition (p. 10).** A concrete logic (X, L) is **downward-directed**
  if for every A, B ∈ L with A∩B ≠ ∅ there is C ∈ L\{∅} with C ⊂ A∩B.
- **Prop 4.4 (with elementary proof, checked).** Every downward-directed
  concrete logic which is a lattice is a Boolean algebra. (Proof: if
  A∧B ⊊ A∩B, the sets A\(A∧B), B\(A∧B) ∈ L meet, so some nonempty
  C ∈ L sits inside; C ∪ (A∧B) ∈ L is a strictly larger lower bound —
  contradiction.)
- **Q5.2 parenthetical.** A concrete logic with a full set of 2-valued JP
  states is downward-directed.
- **Q5.4 + note.** "Does every concrete logic each state of which is JP
  have to be a Boolean algebra? … in the σ-additive case the answer to
  this question is no [2 = BNPW 1985]."

**(i) Theorem-let ⟦HAND — elementary glue over primary-verified
propositions⟧: no non-Boolean concrete σ-class OML has all its σ-additive
states JP.** (Irreducibility not needed.) Chain: on a σ-class, disjoint
countable sups are set unions, so every point-carried (Dirac) state is
2-valued and σ-additive; all-Dirac-states-JP ⟺ Ccard (MPT Prop 3.2,
proof verified — this step is *theirs*, not hand-work) ⟹
downward-directed (MPT p.10 parenthetical, trivial); downward-directed +
lattice ⟹ Boolean (Prop 4.4, proof verified). Note Adm's σ-completeness
IS the σ-class sense (`sigma_essential_body.tex` q:bare clause (b) +
lem:sigma-class-basics — disjoint countable *unions*), so the theorem-let
applies verbatim to Adm ∩ OML.

**Consequence for BNPW (audited form — the session-9 first draft
overstated this as an unconditional "not a lattice").** MPT 1992's default
"concrete logic" is only *finitely* closed (Def 1.1, verified), and
whether BNPW's object is σ-closed — and whether its σ-additivity is
union- or sup-based — is not determined by the Q5.4 note. The honest
statement is a disjunction, and both horns protect Skeleton C: either
BNPW's object is a concrete σ-class (what "the σ-additive case" naturally
suggests) — then by the theorem-let it is **not a lattice**; or it is not
σ-closed — then it is not an Adm-style carrier at all. **Under every
reading, BNPW's object is not a member of Adm ∩ OML and cannot gut
Skeleton C's second half.** The ILL pull resolves which horn (and remains
confirmation-grade, not a gate).

**(ii) Skeleton C's first half is REFUTED as stated (the ⚠-unswept
question is now swept — negative).** The hoped-for theorem "on a concrete
σ-complete OML, σ-additive 2-valued states are JP" is false: **MO₂** (4-point
representation X = {1,2,3,4}, L = {∅, X, {1,2}, {3,4}, {1,3}, {2,4}}) is a
concrete σ-complete irreducible non-Boolean OML whose Dirac state at 1 has
s({1,2}) = s({1,3}) = 1 but s({1,2}∧{1,3}) = s(∅) = 0 — not JP. More
generally, the Dirac chain of (i) shows all-Dirac-states-JP ⟹
downward-directed ⟹ (lattice) Boolean: **on concrete OMLs, σ-JP-forcing IS
Booleanness-forcing — there is no middle theorem.** MO₂ kills the naive JP
route exactly as it killed the identity route (§1 guard). What survives of
Skeleton C: the PP1994 unital-subadditive engine (σ-unitality locus,
§7b) and restatements with wildness hypotheses that exclude MO₂-type
members (e.g. no finite blocks) — unexplored.

**(iii) New verified lever for Skeleton B.** Prop 4.4 is a finitary,
σ-free cousin of the meet-closed-overlap dichotomy: contrapositively,
**every concrete non-Boolean OM lattice fails downward-directedness** —
it has a pair A, B with A∩B ≠ ∅ set-wise containing no nonzero element of
L ("intersection-poor pair"), and (by (i)'s chain) a non-JP Dirac state.
Any lattice member of 𝒞 carries this anatomy. Skeleton B hand-work should
start from Prop 4.4's proof pattern.

**(iii-b) Audit record (same session, on request).** Every step re-checked
against the MPT 1992 text: Def 1.1 (finite closure — the gap source),
Def 3.1 (state, JP, point-carried, full — all match usage here), Prop 3.2
+ proof, Prop 4.4 + proof (line-by-line: A\M, B\M ∈ L by the Def 1.1
remark; C∪M a strictly larger lower bound — sound), Ccard ⟹
downward-directed. MO₂ counterexample machine-checked
(`notes/open_questions/verification/mo2_jp_check.py`, committed s10:
concrete-logic axioms, lattice/meets, non-Boolean, trivial centre, Dirac@1
non-JP with witness A={1,2}, B={1,3} — all seven pass; the s9 audit line
originally credited a "scratchpad script" that as committed only covered
additivity + non-homomorphism — the full seven-property check is now the
committed script above). Corroboration: MPT Prop 3.3 second half + Prop 3.4
independently exhibit non-JP (two-valued) states on concrete logics.
Result of the audit: (ii) and (iii) stand as written; (i) weakened to the
theorem-let + disjunction above.

**(iii-c) Fresh-context adversarial review (s10, 2026-07-10 — clears the
§7c ⟦HAND⟧-glue check owed under shovel plan item 5).** Independent
reviewer, no prior context, MPT 1992 PDF read in full
(`muller_ptak_tkadlec_1992_covering_properties.pdf`). **VERDICT: SOUND.**
Every link verified against the primary text: the glue (σ-class disjoint-
union axiom ⟹ ∪ is the join ⟹ Dirac states σ-additive, unconditional);
Prop 3.2 quoted verbatim p.6, no side conditions (no unitality/
separability/irreducibility — confirmed by full-text grep); Prop 4.4
quoted + proof-checked p.10, hypotheses exactly downward-directed +
lattice; MPT's own σ-logic notion (Prop 4.6, p.11) matches the corpus's
union-based sense — no definitional mismatch. One caution for paraphrasers:
Prop 3.2's characterization of C_card is per-point ("∀x∈A∩B ∃C∋x"), which
implies downward-directedness strictly (not an iff); §7c's inline "⟹,
trivial" already uses only the correct direction. Sole finding (cosmetic,
fixed in (iii-b) above): the s9 provenance line overcredited a scratchpad
script; the seven-property MO₂ check is now committed. Corroborating
receipt: MPT Q5.4 note (p.12) states the σ-additive answer is "no" citing
BNPW 1985 — consistent with §7c(i)'s horn analysis.

**(iv) Closed leads.** arXiv:2308.08508 = Harding–Kornell, "Completely
hereditarily atomic OMLs" (algebraicity/covering property/Kalmbach+Keller
constructions) — no JP or σ-additivity content; irrelevant to this attack
(background only for 2a construction techniques). Bunce–Hamhalter 2000:
scout could not access full text or any substantive secondary description
(Springer/WorldSci/zbMATH/ResearchGate all blocked); scope unknown —
**cite nothing from it; ILL pull stands**, now first in the queue.
*(s9b, user directive — relax the rules, keep the tasks: the pulls stay
owed but are no longer user-only; Claude keeps hunting alternative access,
physical ILL remains the fallback. The attack proceeds treating B–H as
unknown. Frontier, any order: Skeleton B cold (⟦HAND⟧, Prop 4.4 pattern);
Skeleton A read via `derr_williamson_2023.pdf` + `maharam_1972.pdf`, both
in library; Skeleton C surviving branch via `ptak_pulmannova_1994.pdf`,
in library.)*

## 8. Exit criteria for the attack

- **Sharpened-conjecture exit (expected):** 2a and/or the σ-JP question
  stated precisely with the literature swept — an open problem with stakes.
- **Kill exit:** a located theorem or construction settling Ψ_OML either
  way (scout the JP line before investing hand-work).
- **Proof exit (unexpected this session per frontier map):** one of
  Skeletons A–C closes.

*Tooling note: `../sigma_essential/rigor_guard_scope.md` (parked 2026-07-06) names this
problem as its surviving use case — a Lean-detector screen for proposed
mechanisms; would need lattice-aware definitions before any build.*

## 9. Skeleton B cold attack (2026-07-10, session 11)

*Everything here is ⟦HAND⟧ — elementary arguments over the σ-class
axioms, plus two standard OML citations. Finite-scale instances
machine-checked: `notes/open_questions/verification/loop5_greechie_oracle.py`
(Greechie 5- and 6-cycles, 13 checks each, all pass).
Fresh-context adversarial proof-read 2026-07-10 s12: **SOUND**, all
findings cosmetic (applied in place, marked ✎ in the receipt); both
standard citations pinned to primary-grade sources. Receipt:
`PROOF_READ_2026-07-10_attack_s9.md`; independent from-scratch scripts
(118/118) in `../verification/proof_read_2026-07-10_s11/`.
✎s17–s18 (2026-07-11): the ENTIRE §9 layer is now LEAN-VERIFIED,
AXIOM-FREE — `formalization/QuerySystem/QuerySystem/ConcreteOMLBlocks.lean`:
A1(a)–(c), L0 (both directions), C1′, T1 (both forms), P1, A2 in full
(blocks AND overlaps are σ-fields), the composite "σ-states are Dirac
on countably generated blocks", and T3 (on abstract countably generated
σ-fields — no circularity). The Foulis–Holland step needed NO citation
axiom: on a concrete carrier the required commutant-closure instance
follows from a three-line **meet squeeze** (the meet of X, S contains
every carrier subset of X∩S, so a pointwise carrier cover of X∩S
forces meet = X∩S ∈ L; apply with the cover {A∩B, A∩C} of A∩(B∪C) —
set distributivity supplies what orthomodular calculus supplies
abstractly, and complements descend to all four cells). The
Bruns–Harding/Kalmbach citations now support only the ABSTRACT theorem;
nothing in this note's chain rests on them. All `#print axioms`
receipts = [propext, Classical.choice, Quot.sound]. Awaits user
ratification (= accept the build).
Setting throughout: L a concrete σ-class on Ω (∅ ∈ L, complement-closed,
closed under countable disjoint unions; order = ⊆, ⊥ = disjointness);
"lattice" = the poset (L, ⊆) has all binary meets. "Block" = maximal
pairwise-compatible subset of L (Zorn); compatibility is the concrete
test A∩B ∈ L (which suffices: A\(A∩B) ∈ L by orthomodular difference).*

### 9a. Two corrections to the record

**(i) 𝒞's infinite locus is inhabited — §4's first probe was miscast.**
MO_ω is an infinite member of 𝒞: on Ω = 2^ω take
L = {∅, Ω, A_i, A_iᶜ : i ∈ ω}, A_i = {x : x_i = 0}. Any two distinct
non-complementary members intersect, so the only disjoint families are
{A_i, A_iᶜ}: L is a σ-class (vacuously), a lattice (all off-block meets
are 0), σ-complete even in the lattice sense, non-Boolean, centre {∅,Ω}.
It is a horizontal σ-sum (def:horizontal holds: trivial pairwise block
overlaps, no cross-block disjointness), hence Φ by lem:horizontal, and it
is Polish-representable (clopen sets in Cantor space) — consistent with
Conjecture 2a. So the Q3 scout negative and §4's probe must be read as:
**no infinite *non-segregated* member of 𝒞 is known.** §4's parenthetical
"products/horizontal sums are reducible/segregated" conflates the two
disqualifications: horizontal sums are irreducible members of 𝒞 — they
are merely tame.

**(ii) The structural dichotomy is false at finite scale.** The Greechie
pentagon (5 three-atom blocks pasted in a 5-cycle, adjacent blocks
sharing one atom; an OML by the loop lemma) is **concrete** — its 11
two-valued states are order-determining (machine-checked) — and its
canonical representation on X = St(L) is a 22-element concrete σ-class
lattice, non-Boolean (100 intersection-poor pairs), centre trivial, and
**not a horizontal sum** (adjacent blocks share a nonzero proper
element). So a finite member of 𝒞 sits squarely in "the middle"
(irreducibility read as trivial centre — the essential-irreducibility
quotient by the σ-ideal of countable sets degenerates at finite scale). Since
Φ is trivially true on finite carriers (St_fa = St_σ), the pentagon does
not threaten Theorem 2; it shows the Skeleton B dichotomy **cannot be
structural** (Boolean-vs-horizontal-sum) — the surviving claim is
Φ-level, and σ-scale must carry the whole proof.

### 9b. The gluing reduction (any concrete σ-class — no latticehood)

**Lemma A1 (confinement + blockwise reduction).** (a) Disjoint elements
are compatible, so every pairwise-orthogonal family extends to a block.
(b) Every block Bl is ⊥-closed, contains ∅ and Ω, and is closed under
countable disjoint unions (for u = ⊍cₙ with cₙ ∈ Bl and any b ∈ Bl:
u∩b = ⊍(cₙ∩b) ∈ L, and u\b, b\u ∈ L likewise, so u is compatible with
all of Bl, hence in Bl by maximality). (c) Consequently a two-valued
function μ on L is a σ-additive state **iff** μ↾Bl is one for every
block Bl: every countable orthogonal family, with its union, lives
inside a single block. So St_σ(L) = coherent families of blockwise
σ-states, verbatim — q:bare's selection framing is exact for *every*
concrete σ-class, and ¬Φ is always an overlap-coherence failure.
*(Machine: C8.)*

### 9c. What latticehood buys (the T-series)

**L0 (compatible = commuting; compatible meets are intersections).** If
A∩B ∈ L then A∩B is the meet (any lower bound is ⊆ A∩B) and A,B commute.
Conversely if A = (A∧B)∨(A∧Bᶜ) then, the two parts being disjoint and
their ⊍ being an upper bound below the join, A = (A∧B) ⊍ (A∧Bᶜ), whence
A∩B = A∧B ∈ L. (Uses ⊍-closure. So on σ-class OMLs the concrete and
lattice compatibility notions coincide.)

**A2 (blocks are σ-fields; the axis-2 upgrade).** In an OML the
commutant of any element is closed under ∧ — indeed under all existing
joins/meets (Bruns–Harding 2000 Props 2.2–2.4; Foulis–Holland =
Kalmbach 1983 Thm 5 p. 25; originals Foulis 1962 / Holland 1964) — so
for A,B in a block Bl, A∧B is compatible with all of Bl, hence
A∧B ∈ Bl; by L0, A∧B = A∩B. With complement- and ⊍-closure (A1b) and
countable decreasing intersections (∩ₙFₙ = F₁ \ ⊍ₙ(Fₙ\Fₙ₊₁), all pieces
in Bl), **every block of a concrete σ-class OML is a σ-field of sets on
Ω, and every pairwise block overlap is a σ-field**. Likewise every
pairwise-compatible subset — of any cardinality — generates a Boolean
subalgebra (Bruns–Harding 2000 Prop 2.8, stated for arbitrary subsets
via the commutant argument; blocks Prop 3.1; OMP contrast = Ramsay 1966
/ Pool 1963 via Pulmannová 1981 p. 393) and so lies in a block. **The §3 block-overlap
observation is now a theorem**: on a lattice, every block presentation
has meet-closed (indeed σ-field) overlaps — the witness's
disjoint-union-only overlap type (taxonomy axis 2, the live value) is
structurally unavailable. On σ-class OMPs, by contrast, maximal
compatible sets need not be ∩-closed (the regularity-failure locus).
*(Machine: C6, C7.)*

**Corollary (pattern dichotomy — witnesses need incompatibility).** Let
(B, s₀) be a pattern with global f.a. extension μ. If B is pairwise
compatible it lies in a single block Bl (A2); μ restricted to the finite
subfield of Bl generated by B concentrates on a nonempty atom a of that
subfield, and δ_ω for any ω ∈ a is a global σ-additive extension of s₀.
**So on a concrete σ-class OML every pairwise-compatible pattern is
rescued**, and a lattice witness pattern must contain an incompatible
pair — after complement normalisation (B is ⊥-closed; compatibility is
complement-invariant), an incompatible pair A,B with s₀ = 1 on both,
hence A∩B ≠ ∅ (incompatibility alone forces this: A∩B = ∅ ∈ L would
make the pair compatible).

**T1 (singleton quarantine).** If {ω} ∈ L for every ω ∈ A∩B, then every
such {ω} is a lower bound of {A,B}, so A∩B ⊆ A∧B ⊆ A∩B: A∧B = A∩B ∈ L
and A ↔ B. Same conclusion if merely every point of A∩B lies in *some*
member of L contained in A∩B (each such member is a lower bound, hence
⊆ A∧B; the union over points gives A∩B ⊆ A∧B — no exhaustion
hypothesis needed) — in particular if all countable subsets of A∩B are
in L. Contrapositives: **on a lattice, every incompatible
overlap contains a point resolved by no member of L inside the
overlap**; a concrete σ-class OM lattice containing all singletons of Ω
is a Boolean σ-field. **Consequence: the product-Ulam kill mechanism —
a rigid block whose fine (singleton) structure sits below the pattern's
incompatible overlap, collapsing all global σ-states to Diracs, plus a
pattern with K(s₀) = ∅ — is provably unavailable on lattices.** This
upgrades q:oml's hedge ("the rigidity method appears to require
singletons, which … break the meet") to a theorem *for that mechanism*;
other rigidity mechanisms are not excluded (see 9d). It is exactly
cor:incompat run in reverse. *(Machine: C9, trivially — the pentagon's
L contains no singletons.)*

**T3 (Dirac realization on countably generated blocks — latticehood
re-supplies inner regularity).** Let Bl be a block of a concrete σ-class
OML that is countably generated as a σ-field, by {Gₙ}. Let ν be any
two-valued σ-additive state on Bl. Put Fₙ = the intersection of the
first n generators' ν-value-1 sides (∈ Bl by A2; ν(Fₙ) = 1 by the
Boolean argument), and D = ∩ₙFₙ ∈ Bl. Then ν(D) = 1 by σ-continuity
from above (F₁ = D ⊍ ⊍ₙ(Fₙ\Fₙ₊₁), each difference ν-null), so
**D ≠ ∅**; and {A ∈ Bl : D ⊆ A or D∩A = ∅} is a σ-subfield containing
the generators, hence all of Bl. So ν = δ_ω↾Bl for **every** ω ∈ D.
Both hypotheses are load-bearing: without latticehood the Fₙ need not
lie in L (σ-classes lack countable non-disjoint intersections — this is
where the proof dies on the product Ulam carrier); without countable
generation the countable/co-countable σ-field on ω₁ carries its
non-principal co-countable state. **This answers §7's DW entry question
("which step could latticehood conceivably re-supply") affirmatively for
countably generated blocks: the only output of inner regularity the
blockwise theory needs — two-valued σ-measures are point-realized — is
re-supplied intrinsically, with no topology.** The Skeleton A read now
has a sharp target: check whether DW Thm D.6's inner-regularity step
factors through exactly this blockwise statement, i.e. whether
Polish-representability in Conjecture 2a can be traded for a
countable-generation or coarse-block hypothesis. *(Machine: C10.)*

**P1 (poor-region σ-anatomy, for later use).** Poorness is hereditary
(any nonempty subregion of a poor region is poor where nonempty); meets
are σ-superadditive over disjoint decompositions (⊍ₙ(Cₙ∧B) ≤ (⊍Cₙ)∧B,
the left side being in L by ⊍-closure), so if A∧B = 0 and A = ⊍Aₙ then
Aₙ∧B = 0 for all n while some Aₙ∩B ≠ ∅: poor pairs propagate down every
σ-decomposition (the "some Aₙ∩B ≠ ∅" clause uses poorness — A∩B ≠ ∅ —
not just A∧B = 0). Poor pairs are incompatible and lie in no common
block; poor regions are singleton-free (immediately from poorness).

### 9d. The reduced picture, and Conjecture B′

Post-9b/9c a lattice witness must: (1) carry a pattern with an
incompatible 1–1 pair whose overlap is singleton-gapped (T1) — with
somewhere in L a fully poor pair (Prop 4.4); (2) kill every coherent
blockwise-σ selection extending s₀ (A1c). On countably generated blocks
every blockwise σ-state is pointed (T3), so the *only* non-pointed
blockwise resources are **coarse blocks** — σ-fields that are not
countably generated, carrying non-principal two-valued σ-measures of
countable/co-countable type (precisely the pattern of the witness's
centre). The named residual obstruction, sharpening §6's engine gap:

> **Rigidity without fine structure.** A lattice witness must destroy
> non-Dirac σ-states without singletons (or any L-structure) below its
> incompatible overlaps, and must dodge Diracs (K(s₀) = ∅) using only
> coarse blocks. The Ulam engine is the fine-structure engine par
> excellence; no coarse-block rigidity engine is on the corpus's books.

This converges with q:cardinality (the countable-witness question
already demands a rigidity mechanism "necessarily without all
singletons"): **one new rigidity mechanism would feed both open
questions; conversely, a proof that no coarse-block mechanism exists
closes the lattice case.** Sharpened conjecture, replacing the
structural dichotomy:

- **Conjecture B′(i) (countably generated case — the next
  theorem-shaped target).** Every concrete σ-class OML all of whose
  blocks are countably generated satisfies Φ. *(Plausible route:
  lem:horizontal's glue with σ-field overlaps + T3 atoms; the open
  work is cross-block coherence — T3 points the fibers but does not
  glue them.)*
- **Conjecture B′(ii) (general).** Coarse blocks cannot simultaneously
  support the finitely additive coherence of a K(s₀) = ∅ pattern and
  kill every coherent blockwise selection. (= Theorem 2 modulo B′(i),
  by the reduction above. Precision caveat, proof-read s12: killing
  every selection is a whole-carrier property, phrased here as a
  coarse-block property — fine as a slogan, must be sharpened into a
  precise statement before an attack.)

### 9e. Exit status (per §8)

Sharpened-conjecture exit achieved: B′(i)/(ii) + the named obstruction,
with the axis-2 observation and the singleton-mechanism exclusion
upgraded to theorem-lets (⟦HAND⟧, machine-corroborated at finite scale,
not Lean). Proof exit not claimed: cross-block coherence untouched.
Historical menu at this exit: (1) attempt B′(i) directly; (2) Skeleton A
read (`derr_williamson_2023.pdf` Thm D.6 + `maharam_1972.pdf` §8) with
the T3-specific question; (3) hunt a coarse-block toy: a concrete
σ-class OM lattice with one countable/co-countable-type block and one
incompatibility — even a failed construction will name the next wall.
*Historical exit menu; items (1)–(2) were executed in §§10–13. The live
frontier is §15's fibre-to-signature-atom gap plus the coarse-block toy.*

## 10. Skeleton A read (2026-07-10, session 13): DW Thm D.6 + Maharam §8 — the T3 question answered

*✎s18 (2026-07-11): §10b's theorem-lets are LEAN-VERIFIED, axiom-free —
`formalization/QuerySystem/QuerySystem/InnerRegularity.lean`: R in full
(`dirac_forcing`, honest field-of-sets hypotheses, FIP step
machine-checked, plus the cofinite-topology red-flag counterexample AND
`not_t2Space_cofiniteTopology` derived from R itself); P's two-valued
instance at the specific F = X∖{x} on uncountable SECOND-COUNTABLE
Hausdorff spaces (strengthened from Polish — condensation-point route
replaces Cantor–Bendixson), and the s14 all-Hausdorff strengthening
(two-valued instance) by reduction to R. The real-valued diffuse-mass
decomposition and the DW/Maharam source-readings stay hand.*

*⟦HAND⟧ reading results + two elementary theorem-lets (R, P). No machine
oracle — the claims are topological/measure-theoretic, not finitely
instantiable. Fresh-context adversarial check run same-session on R, P,
and every reading claim, primary PDFs read by the checker: **no
refutation found, all SOUND** (receipt:
`SKELETON_A_READ_2026-07-10_receipt.md`). **S12-standard proof-read
CLEARED 2026-07-10 s14** — two independent fresh-context reviewers
(math re-derivation from statements alone + verbatim source re-check,
primary PDFs), from-scratch scripts for every finitely instantiable
component, 11,686/11,686 (`../verification/proof_read_2026-07-10_s13/`);
ALL SOUND, edits marked ✎s14 applied in place (one scope fix, §10d(i));
receipt `PROOF_READ_2026-07-10_attack_s10.md`. Awaits user
ratification.*

### 10a. Anatomy of the DW engine (reading result)

Thm D.6 = Prop D.4 (blockwise split — their Thm D.1 is literally A1 in
Dynkin dress: Dynkin systems are unions of maximal σ-algebras) +
**Maharam 1972 Thm 8.1** + Carathéodory. Maharam 8.1 has exactly two
layers:

1. **F.a. glue — topology-free.** Her Thm 6.1 (Hahn–Banach on partially
   ordered linear spaces): a consistent family of blockwise states has a
   common *finitely additive* extension to the generated field iff the
   gamble-positivity condition (her (8.2) = D.6's RHS). No topology, no
   regularity, no σ. This layer is the corpus's f.a. layer (A1c /
   q:bare's selection framing) — nothing the intrinsic theory lacks.

2. **σ-upgrade — the ONLY place regularity enters.** Inner regularity
   (8.1) — with *in-block* compact approximants, K ∈ 𝔉_α, verbatim in her
   statement — is consumed at the cross-block step: for F = A₁∩…∩Aₙ with
   the Aᵢ from different blocks, per-block compacts give K = ∩Kᵢ, again
   compact (and the open approximants are (8.1)-compacts of the
   *complements* turned open via compact ⟹ closed — Hausdorff is
   load-bearing twice); the compact-class sandwich forces σ-additivity of
   the glued μ on the generated field. The load-bearing property is that
   **compactness is intersection-stable across blocks**: (8.1) is a
   cross-block σ-coherence-transport device, not a per-block one. No
   point-realization statement appears anywhere in the proof.

Also on the record from the read: (i) Maharam §8.1's preamble — a
topology-free σ-extension always exists on the *enlarged* Stone space
(phantom points); consistent with the prior-art verdict's 2026-06-20
block. (ii) Her Remark to 8.1: (8.1) alone already forces each blockwise
state σ-additive. (iii) Her §8.3: Kellerer 1964 — finitely many
σ-additive marginals always glue (signed case).

### 10b. Two theorem-lets: what inner regularity IS

**Theorem-let R (Dirac forcing) ⟦HAND — adversarially checked s13+s14⟧.**
Let 𝒜 be a field of subsets of a Hausdorff space X and ν a two-valued
*finitely additive* state on 𝒜 satisfying (8.1). Then
𝒦₁ := {K ∈ 𝒜 : K compact, ν(K) = 1} is nonempty, D := ∩𝒦₁ ≠ ∅, and ν is
a Dirac restriction: ν = δ_ω↾𝒜 for every ω ∈ D. (✎s14: both nonemptiness
claims stated as conclusions — the old "(nonempty) intersection"
parenthetical misparses under the ∩∅ = X convention.) *Proof.* 𝒦₁ is
nonempty ((8.1) at X; ν two-valued, so the sup over {0,1}-values is
attained), and K∩K′ ∈ 𝒦₁ for K, K′ ∈ 𝒦₁ (compact ⟹ closed in Hausdorff;
closed subset of a compact is compact; ν(K∩K′) = 1 by finite additivity).
So 𝒦₁ is a filter base of compacts: D ≠ ∅ (FIP — fix K₀ ∈ 𝒦₁; the
K∩K₀ are closed in the compact K₀ ✎s14). For ω ∈ D and any
F with ν(F) = 1, (8.1) gives K_F ∈ 𝒦₁, K_F ⊆ F, so ω ∈ F; two-valuedness
finishes. ∎ (No σ-additivity used anywhere.)

**Theorem-let P (coarse diffuse components fail (8.1) on Polish) ⟦HAND —
adversarially checked s13+s14⟧.** Let X be an uncountable Polish space, 𝒜 the
ctble/co-ctble σ-field, μ a σ-additive probability on 𝒜 with diffuse mass
c > 0 (every σ-additive probability on 𝒜 is Σᵢ aᵢδ_{xᵢ} + c·ν with ν the
co-countable state: the non-atomic remainder is 0 on countable sets,
constant on co-countable ones). Take x in the perfect kernel P of X
(Cantor–Bendixson) and F = X∖{x}. Any compact K ∈ 𝒜 with K ⊆ F is
countable — a *closed* co-countable set contains P, since (X∖K)∩P is a
countable relatively open subset of the perfect Polish space P, hence
empty — so μ(K) ≤ μ(F) − c. Inner regularity fails at F. ∎ (Localizes to
a coarse block living on an uncountable Borel B ⊆ Ω via a Cantor subset
of B — perfect set property for Borel sets ✎s14. The c = 1 case also
follows from R — ν is no Dirac restriction — though the R route gives
failure of (8.1) *somewhere*, not at the specific F ✎s14.)

### 10c. The T3 question answered — a two-part verdict

§9c/T3 closed with: *does DW's inner-regularity step factor through
blockwise Dirac realization — can 2a's Polish hypothesis be traded for
countable generation?* The read splits this cleanly:

- **Blockwise: YES, and more.** By R, for two-valued states D.6's
  hypothesis *is* blockwise Dirac realization — **with a compact
  witness** (a value-1 compact filter base). The blockwise half of DW's
  hypothesis is exactly T3's conclusion, which T3 re-derives
  intrinsically (countable generation, no topology).
- **Cross-block: NO.** Maharam's proof consumes the compact *witness*,
  not the pointedness: intersection-stability of compacts across blocks
  IS the σ-upgrade. T3 supplies no intersection-stable class. **Polish
  cannot be traded for countable generation**; the honest intrinsic
  surrogate for "Polish" is a countably compact class in the Marczewski
  sense (measure-theoretic compact classes), not a
  cardinality-of-generation hypothesis.

### 10d. Consequence: Skeleton A demoted — 2a does not finish Theorem 2

Corrections to the record (pattern of §9a):

**(i) §2/§4's "2a ⟹ Theorem 2 outright via DW (Polish ⟹ Φ)" is FALSE as
stated.** D.6 carries a third leg — blockwise inner regularity — and by
R + P that leg fails on the locus the intrinsic theory already
isolated (§9d): coarse blocks carrying non-principal blockwise σ-states
(two-valued case by R's contrapositive; diffuse-component case by P).
(✎s14 scope: *among σ-states on coarse blocks* the failure is exact —
purely atomic states satisfy (8.1) there, finite in-field
atom-truncations being compact witnesses on any Hausdorff topology; on
general blocks the containment is one-way, since a compact-poor block
fails (8.1) even at a Dirac restriction: δ_ω↾{∅, irrationals, ℚ, ℝ},
ω irrational — the only in-field compact is ∅.) A
candidate state with any non-principal blockwise restriction escapes
D.6 — D.6 is *silent*, its hypothesis unmet — **on every Polish
representation** (R uses only Hausdorff). The sufficient form is
2a⁺ = Polish + Borel-generation + blockwise-(8.1); the added leg is the
coarse-block problem in topological dress, not a bypass of it.

**(ii) The prior-art verdict's "inner-regularity is secondary /
near-automatic (Radon)" gloss is corrected** (dated addendum in
`../sigma_essential/sigma_essential_prior_art_verdict.md`; settles that note's banner
sub-question (b): inner regularity IS binding). Radon-ness of Borel
measures on Polish Ω supplies compact approximants *in Borel*, not in
the block; Maharam's (8.1) is in-block — and D.6's footnote-29
definition, which omits K ∈ 𝒜ᵢ, does not typecheck for μᵢ (μᵢ(K)
undefined off-block); cite D.6's hypothesis in the (8.1) sense. The
kill-zone box (Polish + Borel-gen + inner-regular blocks) was always
three-legged; what changes is the accounting: the third leg is
load-bearing and fails generically on the coarse locus. NOT a verdict
swing.

**(iii) rem:dw's residue is two conditions, not one.** A witness escapes
DW iff (non-Polish-representable) OR (some blockwise restriction
non-principal / coarse-riding — an escape available even on
Polish-representable carriers). Caveat added to `oml_onboarding.tex`
rem:dw.

**Three-front convergence, sharpened.** q:cardinality, B′(i)/(ii), and
now the DW inner-regularity leg all bottom out at the same object:
non-principal two-valued σ-states on coarse σ-fields with no internal
approximating structure. *Rigidity without fine structure* (§9d) is also
the exact content of D.6-hypothesis failure. Theorem 2 factors as
**B′(i) + (coarse-block question: no coarse blocks in 𝒞 ∩ OML, or
B′(ii))**, and no representability route avoids the second factor. The
coarse-block toy hunt (§9e item 3) is promoted: it decides whether the
second factor is vacuous.

### 10e. What Skeleton A still buys; B′(i) proof shape; pulls

- The one reusable engine is **compact-class gluing**. B′(i)'s missing
  lemma now has a name and a shape: a countably compact class 𝒦,
  intersection-stable across blocks, Marczewski-approximating the
  blockwise states in-block (✎s16: "refining the value-1 filters" was
  too weak — singleton classes refine every ultrafilter; the value-1
  inner witness D ⊆ K is load-bearing, see §11e) (T3 kernels D_ν are
  the canonical candidates;
  cross-block kernel FIP = cross-block coherence restated *(✎s15: the
  parenthetical is wrong in both halves — kernel FIP is strictly
  stronger than coherence (reduced-pentagon machine witness), and on
  ctbly generated blocks the σ-side needs no compact class at all;
  see §11c. The compact-class engine's real target is the coarse
  factor.)*). Pulls:
  Marczewski 1951 (Fund. Math. 38, measures in almost independent
  fields — Maharam's ref [7]); Marczewski–Ryll-Nardzewski 1953 (Fund.
  Math. 40, compactness and direct products — her ref [8]); Kellerer
  1964 (already listed).
- Skeleton A's residual value: 2a stays a good structure-theory question
  (MO_ω-type evidence stands), but it is now a *conditional* route (2a⁺),
  not an independent one.

### 10f. Exit status

Skeleton A read DONE (§9e menu item 2). T3 question answered (10c);
Skeleton A demoted (10d(i)); prior-art accounting corrected, no swing
(10d(ii)–(iii)). Historical menu at this exit: (1) B′(i) with the
kernel-FIP shape + Marczewski pulls; (2) coarse-block toy hunt
(promoted — decides Theorem 2's second factor); (3) Skeleton C surviving
branch (PP1994). Owed: ~~s12-standard proof-read of §10~~ CLEARED
2026-07-10 s14 (receipt `PROOF_READ_2026-07-10_attack_s10.md`).
*Historical exit menu; superseded by §§11–13.*

## 11. B′(i) direct attempt (2026-07-11, session 15): the cluster reduction, the Stone-density reframe, and the Marczewski read

*✎s18 (2026-07-11): §11's banked layer is LEAN-VERIFIED, axiom-free —
`ConcreteOMLPatterns.lean`: 2BR, cluster machinery (Φ ⟺ cluster form,
cluster extension), P⁼ in full (backward leg formally needs NO
countable generation and NO latticehood), Φ-density on the Cantor cube
(+ St_fa closed and compact — gap 4.2(a)/(b)), B′(i) and T4 as named
open Props with the necessity direction B′(i) ⟹ T4 PROVED (the T3
kernel is an atom); the crux is deliberately NOT stated as a theorem.
`MarczewskiTransport.lean`: the corrected (✎s16) compact-transport
criterion is a THEOREM (approximation hypothesis structural), and the
ω₁ scoping bank is certified end-to-end (σ-additive, non-Dirac,
non-countably-generated, countably compact class + approximation).
Marczewski attribution reads (11e bullets 2–3) stay source-reading.*

*⟦HAND⟧ theorem-lets, machine-corroborated at finite scale
(`../verification/b_prime_i_s15_oracle.py`, 10 checks PASS — pentagon in
canonical AND reduced representations; the reduced rep is the load-bearing
one for 11c/11d, see below). Marczewski 1951 + Marczewski–Ryll-Nardzewski
1953 + Marczewski "On compact measures" 1953 pulled into the library this
session (`marczewski_1951_almost_independent.pdf`,
`marczewski_ryll_nardzewski_1953_compactness_products.pdf`,
`marczewski_1953_on_compact_measures.pdf` — the third is where the
compact-class machinery actually lives; the cited "Remarks" is a 6-page
follow-up). No proof of B′(i) claimed; yield = a reduction ladder ending
in a FINITARY selection principle, plus a corrected picture of where the
compact-class engine belongs. Proof-read CLEARED 2026-07-11 s16, edits
✎s16 in place (receipt `PROOF_READ_2026-07-11_attack_s11.md`).*

### 11a. Two-block rescue (any concrete σ-class OML — no countable generation)

**Theorem-let 2BR ⟦HAND⟧.** Let L be a concrete σ-class OML on Ω, B a
finite ⊥-closed pattern, s ∈ St(B) with a f.a. extension μ ∈ St_fa(L),
and suppose V := {A ∈ B : s(A) = 1} is covered by two blocks, V ⊆ Bl₁ ∪
Bl₂. Then s is Dirac-rescued. *Proof.* E := ∩(V∩Bl₁) and F := ∩(V∩Bl₂)
are elements of Bl₁, Bl₂ (A2: blocks are ∩-closed — this is the ONLY use
of latticehood) with μ(E) = μ(F) = 1 (in-block multiplicativity: μ↾Blᵢ is
a two-valued f.a. state on a field, hence an ultrafilter). If E∩F = ∅
then E ⊥ F, E⊍F ∈ L (σ-class), and μ(E⊍F) = 2 — absurd. Take ω ∈ E∩F:
δ_ω is σ-additive on any concrete σ-class (exactly one summand of a
disjoint union contains ω), δ_ω = 1 on V (each A ∈ V contains E or F as
sets), and value-0 elements of B are handled by ⊥-closure (Aᶜ ∈ V). ∎
*(Machine: D1, 110 cases × 2 reps.)*

Consequences. (i) **B′(i)'s open locus is patterns whose value-1 part
needs ≥ 3 blocks.** (ii) On σ-class OMPs the rescue dies exactly at A2
(blocks not ∩-closed) — and the product-Ulam witness's pattern indeed has
THREE value-1 sets in three pairwise-incompatible blocks; for |V| ≤ 2 no
meets are even needed (E, F are the pattern sets themselves), so **every
concrete σ-class — OMP included — Dirac-rescues patterns with ≤ 2 value-1
elements**, and the witness's |V| = 3 is optimal. (iii) Latticehood's
contribution to Φ is, so far, exactly: in-block finite meets exist and
are intersections.

### 11b. Cluster reduction (normal form for the frontier)

**Monotonicity lemma ⟦HAND⟧.** Two-valued f.a. states on an OML are
monotone: E ≤ A ⟹ μ(E) ≤ μ(A), via orthomodularity (A = E ∨ (A∧Eᶜ), an
orthogonal join, and A∧Eᶜ = A∩Eᶜ by compatibility of comparable
elements). *(Machine: D2.)* *(✎s16: the OML hypothesis is superfluous —
on any concrete σ-class, E ⊆ A with μ(E) = 1, μ(A) = 0 gives μ(Aᶜ) = 1
and E ⊍ Aᶜ ∈ L, so μ(E ⊍ Aᶜ) = 2; two lines, no orthomodularity. The
OM route stands; the general route is banked.)*

**Cluster normal form.** Given any f.a.-coherent pattern (B, s, μ),
group V by blocks and take in-block meets: the pattern reduces to a
**cluster** E₁,…,Eₘ ∈ L with μ ≡ 1, WLOG pairwise incompatible (a
compatible pair lies in a common block — Bruns–Harding, as in A2 — and
merges to its intersection, decreasing m; μ-value 1 by in-block
multiplicativity), pairwise intersecting (2BR argument), with m ≥ 3 and
∩ᵢEᵢ = ∅ in the open case (else Dirac). Any σ-state ν ≡ 1 on the cluster
extends s on B (monotonicity + ⊥-closure). So **Φ(L) ⟺ every
f.a.-coherent cluster admits a σ-state ≡ 1 on it.**

### 11c. On countably generated blocks the σ-side is FREE: pointed ⟺ σ

Countably generated blocks are **atomic** σ-fields: the signature cells
A(ω) = ∩{Gₙ or Gₙᶜ, whichever contains ω} are countable intersections,
hence in the block, and partition Ω. **Theorem-let P⁼ ⟦HAND⟧.** For L
with all blocks ctbly generated, a two-valued f.a. state ν is σ-additive
**iff** for every block Bl its kernel D_Bl := ∩{A ∈ Bl : ν(A) = 1} is
nonempty (equivalently: ν charges an atom of every block). *Proof.* (⟹)
T3's argument, run on a countable generating family. (⟸)
Atom-concentrated states are σ-additive per block (of a disjoint union
covering the atom, exactly one member absorbs it), and blockwise σ ⟹
global σ by A1c. ∎ *(Machine: D5, both reps.)* Hence St_σ(L) = coherent
atomic selections, and **B′(i) is a pure selection problem: no compact
class is needed on the σ-side at all.** The Maharam/Marczewski σ-upgrade
machinery belongs to the coarse factor (Theorem 2's second factor /
B′(ii)), not to B′(i).

**Correction to §10e's slogan (✎s15 there).** Cross-block kernel FIP is
NOT "cross-block coherence restated" — it is strictly stronger. Machine
witness: on the pentagon represented on a proper order-determining subset
Ω′ ⊊ St(L) (10 of 11 states — ✎s16: the *unique* valid reduced rep,
drop the all-odd state; exhaustive over all 2046 proper subsets), some
σ-additive state has three
block-kernels pairwise intersecting with EMPTY triple intersection
*(D3-reduced)*. Coherence constrains kernels only through shared
elements, not through set intersections.

**Representation-dependence bank (new, cheap, load-bearing).** On the
canonical representation Ω = St(L) every state is Dirac-at-itself, so
coherent patterns NEVER have empty kernel there *(D3/D4-canon:
impossible, verified)*; on Ω′ the dropped state becomes a non-Dirac
σ-state and an empty-kernel f.a.-coherent 3-set pattern appears, rescued
non-Dirac-ly *(D4-reduced)*. **K(s) = ∅ is a property of the
representation — it measures the gap between the point set Ω and
St_σ(L)**, not a property of the abstract logic. (Concrete-σ-class reps
have Ω → St_σ(L) via ω ↦ δ_ω — injective only when L separates points,
✎s16; σ-classhood is what ties points to σ-states.) The ≥3-block frontier is thus inhabited already at finite
scale — B′(i) cannot be proved by Dirac density, and any proof must
produce non-Dirac selections.

### 11d. Stone-density reframe of Φ

St_fa(L) ⊆ {0,1}^L is closed in the product topology, hence compact; its
nonempty basic clopens are exactly the f.a.-coherent finite patterns (a
finite value assignment with an f.a. witness ⊥⊍-closes to a finite
⊥-closed sub-orthoposet without leaving the clopen). **Theorem-let
Φ-density ⟦HAND⟧: Φ(L) ⟺ St_σ(L) is dense in St_fa(L).** For
B′(i)-hypothesis carriers, by P⁼: **B′(i) says the blockwise-pointed
states are dense among the two-valued f.a. states** — the exact OML
analogue of "Diracs are dense in the Stone space" for fields of sets
(there, value-1 finite intersections are nonempty field elements; on
OMLs 2BR is the fragment that survives, and it stops at two blocks).
Feeds q:phi: Φ is a topological (density) property of the state space,
not an extension property per se.

### 11e. The Marczewski read (what the pulls actually say)

Definitions (M 1953, §§2–4): a class 𝒦 is *compact* if every countable
subfamily with the finite-intersection property has nonempty total
intersection; 𝒦 *approximates* a field M w.r.t. μ if every E ∈ M is
η-sandwiched D ⊆ K ⊆ E with D ∈ M, K ∈ 𝒦, μ(E∖D) < η (✎s16 source
fix: the quantifier runs over ALL of M — null sets included, so 𝒦 must
contain small sets, ∅ suffices; for two-valued μ this reduces to the
value-1 sandwich D ⊆ K ⊆ A with μ(D) = 1, plus ∅ ∈ 𝒦); μ is a
*compact measure* if some compact class approximates it. Then:

- **4(i) compact ⟹ countably additive.** Two-valued in-block form
  (inline, for our use): if E = ⊍ₙEₙ in Bl with μ(E) = 1, μ(Eₙ) ≡ 0, the
  tails Fₙ = E∖(E₁⊍…⊍Eₙ) are value-1, their sandwich compacts have the
  FIP (finite in-block value-1 intersections are value-1, hence
  nonempty), so ∅ ≠ ∩Kₙ ⊆ ∩Fₙ = ∅ — absurd. **Compact-transport
  criterion, OML form: ONE countably compact class
  Marczewski-approximating every block in-block makes a two-valued
  f.a. state σ-additive** (per-block 4(i) + A1c). (✎s16: was "refining
  every block's value-1 filter" — too weak, and inequivalent: the class
  of ALL SINGLETONS of Ω is countably compact and refines every
  ultrafilter, which would make every two-valued f.a. state σ-additive;
  the value-1 *inner* witness D ∈ Bl, μ(D) = 1, D ⊆ K is what powers
  the FIP step above.) This is the intrinsic engine for
  the coarse factor; B′(i) doesn't need it (11c).
- **5(iii)/(iv) independence gluing (✎s16 scope fix).** The clean
  statement is 5(iv): if the generating subfields are countably
  independent *σ-fields* and each partial measure is compact, the
  measure on the generated field is compact. 5(iii) puts its
  hypotheses on the *approximating classes* (compact + countably
  multiplicative + countably pseudo-independent) — compactness of the
  partial measures alone is explicitly insufficient there ("and, what
  is more"). Both are compactness-*transfer* theorems for a measure
  already given on the generated field, not extension-existence (that
  is M 1951 Thm I). Independence is what substitutes for
  cross-block intersection-stability; OML blocks are precisely NOT
  independent (σ-field overlaps, A2), so no direct transfer — the
  theorem marks what overlap-coherence must replace.
- **M–RN 1953.** §1(i): a (non-direct) product of a σ-additive and a
  COMPACT measure is σ-additive; §1(ii): two σ-additive measures whose
  product is not (Bernstein-type decomposition, m_e(Z) = m_e(Z′) = 1) —
  compactness is essential already for TWO factors; §3(ii): purely
  atomic σ-measures are compact (the abstract home of s14's "atomic
  states satisfy (8.1) via finite atom-truncations"); §4: the
  converse-false example (a non-compact measure whose minimal
  σ-extension is purely atomic, hence compact) — the positive half,
  minimal σ-extensions of compact measures are compact, is M 1953
  4(ii), quoted there as "C 4 (ii)" (✎s16 credit fix).
- **Scoping bank (new).** The co-countable filter on ω₁, with ∅
  adjoined (✎s16 — approximation must cover null sets too; the sandwich
  for co-countable E is E ⊆ E ⊆ E), IS a countably compact class, so
  the coarse killer state is a **compact measure in Marczewski's
  sense** — consistently with its being σ-additive (corroboration: the
  state is purely atomic, ω₁ a single atom, hence compact by M–RN
  §3(ii) directly). Marczewski compactness ≠ (8.1): the coarse state
  kills the TOPOLOGICAL in-block leg (DW, on every Polish rep — §10) and
  cross-block intersection-stability, not abstract compactness per se.
  (A union of per-block compact classes need not be compact — exactly
  what 5(iii)'s independence hypothesis buys back.) So even a
  "Marczewski-2a⁺" (abstract compact classes replacing Polish) bottoms
  at the same cross-block wall; three-front convergence unchanged, but
  the coarse factor's wall now has an intrinsic statement: *no
  countably compact class simultaneously Marczewski-approximates
  interlocking coarse blocks in-block* (✎s16: "approximates" — with the
  value-1 inner witness — not mere filter refinement; the two are
  inequivalent as conjecture targets, singleton-class counterexample
  above, and only approximation is the true criterion's hypothesis).

### 11f. The reduction ladder, the crux, and exit

**Ladder.** B′(i) ⟺ every f.a.-coherent cluster (m ≥ 3) admits a
blockwise-pointed f.a. extension (11b + 11c) ⟺ pointed states are dense
(11d). Zorn frame: partial pointings (finitely many blocks pointed at
chosen atoms, f.a.-coherently with the cluster) give closed nonempty
subsets of the compact St_fa(L); chains are fine by FIP. Everything
reduces to the successor step (✎s16 scope: at *finite* support as
boxed; the Zorn run needs the step at arbitrary 𝒮 — a block may have
infinitely many atoms, so "point Bl₀ somehow" is an infinite union of
closed conditions, not closed, and compactness alone does not close
the limit stage; the parenthetical after the box already concedes
this. T4, the 𝒮 = ∅ instance, is unaffected):

> **Crux (one-block repointing).** Given a f.a.-coherent configuration
> (cluster + finitely many pointed blocks) and a further block Bl₀, is
> there an atom D of Bl₀ such that the enlarged configuration is still
> f.a.-coherent?

(Failure of a GREEDY run does not refute B′(i) — bad early atom choices
are possible — but the 𝒮 = ∅ instance is a NECESSARY consequence of
B′(i), since a σ-extension points every block. It is purely finitary, no
σ anywhere in its statement:)

> **T4 (finitary shadow of B′(i)).** For every f.a.-coherent cluster
> E₁,…,Eₘ and every block Bl₀ of L, some atom D of Bl₀ makes
> {E₁,…,Eₘ, D} f.a.-coherent (some two-valued f.a. state is 1 on all of
> them).

T4 holds automatically on finite carriers (every state is σ there, and
a σ-extension is pointed everywhere) and is the sharpest cheap
falsification target for B′(i): a T4-violating configuration kills
B′(i) outright. Conversely T4 + a completion principle (the crux for
general 𝒮, or a compactness argument replacing it) proves B′(i).

### 11g. Exit status

No proof, no refutation. Banked: 2BR (open locus = ≥ 3 blocks; witness's
|V| = 3 optimal), cluster normal form, P⁼ (pointed ⟺ σ; B′(i) = pure
selection problem; compact classes reassigned to the coarse factor),
kernel-FIP correction to §10e, representation-dependence of K(s) = ∅,
Φ-as-density, Marczewski read + intrinsic wall statement for the coarse
factor, T4 + crux ladder. Historical menu at this exit: (1)
block-restriction openness/interpolation (§13), sharpened by §§14–15 to
the fibre-to-signature-atom charge problem; (2) coarse-block toy hunt
(unchanged, decides the second factor — with 11e's intrinsic wall
statement as its target); (3) B′(ii) precise restatement; (4) Skeleton C
surviving branch (PP1994). ~~Owed: s12-standard proof-read of THIS
section (§11)~~ CLEARED 2026-07-11 s16: two fresh-context reviewers —
(1) all twelve claim-statements re-derived/refutation-attempted from
statements only, then line-checked; 424,509/424,509 from-scratch
machine checks (`../verification/proof_read_2026-07-11_s15/`, 6 scripts,
orchestrator re-run exit 0); (2) verbatim source re-check of every
§11e attribution against all three Marczewski PDFs. VERDICT: SOUND, no
wrong step; three substantive wording fixes applied in place (✎s16:
compact-transport criterion + intrinsic wall "refines" →
"Marczewski-approximates in-block"; 5(iii)/(iv) hypothesis scope; M–RN
§4 credit), plus ∅-adjunction, crux-box finite-𝒮 scope, ↪ → →, and the
banked monotonicity strengthening. Receipt
`PROOF_READ_2026-07-11_attack_s11.md`.

## 12. Maharam (8.2) test of the repointing crux (2026-07-11, session 19)

**Verdict: excluded as a proof engine on the open locus.** Maharam's
positive-extension condition (8.2) is strictly stronger than f.a.
coherence on the non-Boolean carrier and already fails for every cluster
in the normal form, before a candidate atom of the new block is chosen.

Indeed, let $E_1,\ldots,E_m$ be a cluster with
$\bigcap_iE_i=\varnothing$, and prescribe value $1$ to every $E_i$.
On the Boolean field generated by $E_i$, put
$f_i=1_{E_i^c}$, and take the constant function $f_0=-1$ from any
one of the fields. Pointwise,

\[
f_0+\sum_{i=1}^m f_i=-1+\sum_{i=1}^m1_{E_i^c}\geq0,
\]

because the total intersection is empty. But the prescribed integral is

\[
\int f_0+\sum_{i=1}^m\int f_i=-1+0=-1,
\]

contradicting (8.2). Thus Theorem 6.1 cannot even positively glue the
original cluster's Boolean measures as set-field measures. This is
consistent with the cluster's f.a. state on $L$: cross-block pointwise
linear relations are not additivity relations in the non-Boolean
Dynkin carrier.

Consequently, adding a block atom $D$ and checking (8.2) cannot decide
T4: the test has already rejected the input. The live fine-block route
must use the OML's intrinsic finite geometry (or a genuinely weaker
positivity notion), not classical positive extension on the generated
set field. This is a mechanism exclusion, not evidence for or against
B′(i). Next: direct T4/repointing analysis, alongside the coarse-block
toy hunt and a precise B′(ii).

## 13. Stone projection form of T4 (2026-07-11, session 19)

Fix a countably generated block $M$. Let $X=\Stfa(L)$, let
$U(M)$ be the Stone space of ultrafilters of the underlying Boolean
algebra of $M$, and let

\[
r_M:X\longrightarrow U(M),\qquad r_M(\mu)=\mu|_M.
\]

For a coherent cluster $\mathcal C$, its face
$C_{\mathcal C}=\{\mu\in X:\mu(E)=1\ (E\in\mathcal C)\}$ is a nonempty
clopen subset of $X$. Its image under $r_M$ is compact, hence closed.
Let $P_M\subseteq U(M)$ be the point ultrafilters $\delta_\omega|_M$.
They are dense: every nonempty Stone basic open is represented by a
nonempty set $A\in M$, and any $\omega\in A$ supplies a point in it.
Because $M$ is countably generated, each point ultrafilter charges its
signature atom. Therefore

\[
\text{T4 for }(\mathcal C,M)
\quad\Longleftrightarrow\quad
r_M(C_{\mathcal C})\cap P_M\ne\varnothing.
\]

This isolates both sides of the problem. A T4 counterexample is exactly
a nonempty cluster face whose restriction image is contained in the
nonprincipal remainder $U(M)\setminus P_M$. Conversely, any condition
making $r_M(C_{\mathcal C})$ have nonempty interior proves T4, since
$P_M$ is dense. In particular, openness of the restriction map (or the
weaker local statement that every nonempty cluster face has restriction
image with interior) implies T4.

The local-interior statement has an algebraic interpolation form: there
must be a nonempty $A\in M$ such that every block ultrafilter charging
$A$ lifts to a global f.a. state charging the cluster. As §14 records,
on a countably generated block this is actually equivalent to T4, not a
stronger route to it: a lifted point ultrafilter is isolated by its
signature atom. Density of point ultrafilters alone remains
insufficient because a closed restriction image may lie in the dense
set's remainder; the extra fact used in the reverse direction is that
the point ultrafilters are isolated.

## 14. Local interior collapses to T4 on a fine block (2026-07-11, session 20)

**Proposition (fine-block interior equivalence).** Let $M$ be a
countably generated block and $\mathcal C$ a f.a.-coherent cluster. The
following are equivalent:

1. T4 holds for $(\mathcal C,M)$;
2. $r_M(C_{\mathcal C})$ contains a point ultrafilter;
3. $r_M(C_{\mathcal C})$ has nonempty Stone interior;
4. there is a nonempty $A\in M$ such that every ultrafilter of $M$
   charging $A$ lifts to a global f.a. state charging $\mathcal C$.

*Proof.* The equivalence of (1) and (2) is §13. Write a countable
generating family as $(G_n)$. For $\omega\in\Omega$, its signature cell

\[
D_\omega=\bigcap_n\begin{cases}G_n,&\omega\in G_n,\\
G_n^c,&\omega\notin G_n,
\end{cases}
\]

belongs to $M$ and is a nonempty Boolean atom. The point ultrafilter
$u_\omega$ is the unique ultrafilter charging $D_\omega$, so the Stone
basic open $[D_\omega]$ is the singleton $\{u_\omega\}$. Thus (2)
implies (3), and taking $A=D_\omega$ gives (4). Conversely, (3) contains
some nonempty basic open $[A]$; choosing $\omega\in A$ puts the point
ultrafilter $u_\omega$ in the image, giving (2). The same choice proves
(4) implies (2). ∎

**Finite-algebra translation.** T4 is therefore exactly the assertion
that the restriction image reaches one principal Boolean atom:

\[
\exists D\in\operatorname{At}(M)\quad
\exists\mu\in C_{\mathcal C}\quad \mu(D)=1.
\]

The proposed interpolation theorem supplies no independent leverage:
once such a $D$ is found, “every ultrafilter charging $D$ lifts” concerns
the single ultrafilter already found. Lattice meets enter only upstream,
in making blocks σ-fields and hence closing the countable signature
intersection inside $M$; no new cross-block meet identity appears in
the equivalence.

**Exit of the first s20 sub-attack.** The implication “local interior
forces T4” does not expose a stronger carrier property on fine blocks;
local interior, the preferred interpolation form, and T4 are the same
atomic-reachability problem. The live Priority 1 target must therefore
be stated intrinsically as **principal-atom reachability**: prove that a
three-block cluster face reaches some atom of every further fine block,
or realize a nonempty face whose entire restriction image avoids all
principal atoms. General openness of $r_M$ is still a genuinely stronger
global condition, but proving it only on cluster faces through nonempty
interior is not.

## 15. Finite-generator tree test: the σ-completion gap reappears (2026-07-11, session 21)

Fix a coherent finite cluster $\mathcal C$, a countably generated block
$M=\sigma(G_1,G_2,\ldots)$, and let $M_n$ be the finite Boolean algebra
generated by $G_1,\ldots,G_n$. Define

\[
T_n=\{A\in\operatorname{At}(M_n):
      \mathcal C\cup\{A\}\text{ is f.a.-coherent}\}.
\]

Join $A'\in T_{n+1}$ to the unique $A\in\operatorname{At}(M_n)$ with
$A'\subseteq A$. This is a finitely branching tree: every level is
nonempty because any witness $\mu\in C_{\mathcal C}$ charges exactly one
atom of $M_n$, and feasibility descends under refinement by monotonicity.

Every state in the cluster face determines a branch by charging the
unique atom at each level. Conversely, for a branch put

\[
F_n=\{\mu\in C_{\mathcal C}:\mu(A_n)=1\}.
\]

Each $F_n$ is nonempty by feasibility, clopen in the compact state
space, and $F_{n+1}\subseteq F_n$. Compactness gives a state in
$\bigcap_nF_n$ selecting the branch on the finite generator algebra.
This much is correct but does **not** identify the branch with a unique
element of $r_M(C_{\mathcal C})$, and a nonempty
$D=\bigcap_nA_n$ does **not** force that state to charge $D$.

The failed step is important: $M$ is generated from the $G_n$ as a
σ-field, whereas a f.a. ultrafilter need not respect countable unions or
intersections. Agreement on $\bigcup_nM_n$ therefore need not determine
an ultrafilter on $M$. Model case: $\mathcal P(\mathbb N)$ is countably
generated by the singletons; all free ultrafilters agree on the
finite–cofinite algebra generated at finite stages, but differ on the
full σ-field. Likewise, an ultrafilter may charge every $A_n$ while not
charging their nonempty countable intersection $D$.

**Correct tree statement.** Branches parametrize nonempty compact
fibres of cluster-face states having the same finite-generator trace.
T4 asks for some branch with signature atom $D=\bigcap_nA_n\ne\varnothing$
whose fibre contains a state charging $D$. Neither nonempty levels,
existence of a branch, nor $D\ne\varnothing$ alone supplies the last
condition. Thus the tree exposes rather than removes the σ-completion
gap.

This also blocks a cluster-blind repair. Requiring every descending
nonzero chain of finite-stage atoms to have nonzero meet forces all
generator traces to have carrier points, but still does not force a f.a.
state in the corresponding fibre to charge that meet. Requiring the
charge is precisely the missing principal-atom reachability. Cross-block
coherence gives no automatic bridge: for incompatible $E$ and $A$,
$\mu(E)=\mu(A)=1$ need not imply $E\wedge A\ne0$ or that the meet is
charged. This weakest bridge already fails in the finite Greechie
pentagon used by the §11 oracle: state
$(0,0,1,0,0,0,1,0,0,1)$ charges the incompatible abstract atoms
$a_2,a_6$, while their only common lower bound is $0$ (the existing
oracle model reports 460 ordered coherent incomparable meet-zero
pairs). Thus no proof may convert cross-block value-one coherence into
nonzero lattice meet without an additional carrier hypothesis.

**Construction obstruction (three-colour attempt).** Suppose the atoms
$D_k$ of a countably atomic $M$ are assigned so that each lies in two
cluster sets and is disjoint from the third, thereby making every
$D_k$ incoherent with the cluster. For each pair put
$U_{ij}=\bigcup\{D_k:D_k\subseteq E_i\cap E_j\}$. Countability and
σ-closure give $U_{ij}\in M\subseteq L$; the proposed colouring gives
$U_{ij}=E_i\cap E_j$, so $E_i\cap E_j\in L$. In a concrete σ-class OML
this makes $E_i,E_j$ compatible, contradicting the normal form. Hence
the canonical atomwise-disjointness construction of an all-remainder
image is impossible. Subtler global state constraints remain open.

## 16. Fibre saturation and the finite-certificate obstruction (2026-07-11, session 22)

The corrected tree picture yields a genuine sufficient condition. For a
feasible branch $(A_n)$ write $D=\bigcap_nA_n$.

> **FS (finite-stage fibre saturation).** If $D\ne\varnothing$, then for
> some $n$ the family $\mathcal C\cup\{A_n\setminus D\}$ is
> f.a.-incoherent.

Pair FS with:

> **BC (branch carrier).** The feasibility tree has some branch with
> nonempty signature atom $D=\bigcap_nA_n$.

**Proposition.** BC + FS implies T4 for $(\mathcal C,M)$.

*Proof.* Choose the BC branch. The nested nonempty compact faces
$F_n=\{\mu\in C_{\mathcal C}:\mu(A_n)=1\}$ have a common state $\mu$.
At the FS stage, $A_n=D\mathbin{\dot\cup}(A_n\setminus D)$ inside the
Boolean block $M$. If $\mu(D)=0$, two-valued finite additivity and
$\mu(A_n)=1$ force $\mu(A_n\setminus D)=1$, contradicting the FS
incoherence certificate. Hence $\mu(D)=1$. ∎

FS is real extra content, not T4 or tree compactness restated: it
uniformly removes the nonprincipal side of an entire branch fibre at one
finite stage. Failure of FS at every stage compactly produces a
remainder state in that branch fibre, but not necessarily an
all-remainder fibre and hence not by itself a T4 counterexample. BC is
also nontrivial: generator signatures can have empty carrier cells.

The falsification side has a broader carrier obstruction. Let a
countably atomic block $M$ have atoms $D_n$ with $\bigvee_nD_n=1$.
Suppose a construction kills each atom on the cluster face using
carrier certificates

\[
D_n\le H_n^\perp,
\qquad \mu(H_n)=1\quad(\mu\in C_{\mathcal C}).
\]

If all $H_n$ dominate one nonzero $H$, then
$D_n\le H_n^\perp\le H^\perp$ for every $n$, so σ-completeness gives
$1=\bigvee_nD_n\le H^\perp$, whence $H=0$, impossible for a value-one
carrier. More generally, if the $H_n$ range over finitely many jointly
compatible certificates $H^1,\ldots,H^r$, put
$U_j=\bigvee_{n:H_n=H^j}D_n$. Then $U_j\le(H^j)^\perp$ and
$\bigvee_jU_j=1$, while compatibility and value one force
$\mu(\bigwedge_jH^j)=1$; but

\[
\bigwedge_jH^j\le\bigwedge_jU_j^\perp
=\left(\bigvee_jU_j\right)^\perp=0,
\]

a contradiction. Thus a genuine all-remainder construction cannot use
one reused carrier or finitely many compatible carrier colours. It must
use infinitely many genuinely incompatible certificates, or affine
state equations with no orthogonality/carrier witness.

## 17. FS demoted; countable certificates and affine cancellation (2026-07-11, session 23)

For a fixed branch with $D=\bigcap_nA_n\ne\varnothing$, put
$F_n=\{\mu\in C_{\mathcal C}:\mu(A_n)=1\}$ and
$F_\infty=\bigcap_nF_n$. Then the following are equivalent:

1. FS holds on the branch;
2. for some $n$, every state in $F_n$ charges $D$;
3. every state in $F_\infty$ charges $D$.

The first equivalence uses
$A_n=D\mathbin{\dot\cup}(A_n\setminus D)$. For (3)⇒(2), if no finite
stage works, the nested compact sets
$F_n\cap\{\mu:\mu(D)=0\}$ are all nonempty and have a common point,
contradicting (3). Thus FS is exactly **universal principality of the
whole branch fibre**, whereas T4 requires only one principal state.

FS cannot follow from latticehood or σ-completeness alone. Let
$L=M=\mathcal P(\mathbb N_0)$, generated as a σ-field by
$G_n=\{n\}$ for $n\ge1$, and take the trivial cluster. The branch

\[
A_n=\{0\}\cup\{n+1,n+2,\ldots\},\qquad D=\{0\},
\]

contains the principal state $\delta_0$, but also every free ultrafilter
on $\{1,2,\ldots\}$; each charges $A_n\setminus D$ at every stage.
Hence FS fails even in a complete Boolean algebra satisfying Φ. The
BC+FS proposition remains correct as a sufficient condition, but this
route is demoted: any derivation must use a special cross-block cluster
hypothesis strong enough to remove all remainder states from a fibre.

The §16 finite-certificate obstruction is sharp in cardinality. In
$M=\mathcal P(\mathbb N)$, put $D_n=\{n\}$ and $H_n=D_n^c$. A free
ultrafilter has $u(D_n)=0$ and $u(H_n)=1$ for every $n$, even though
$\bigvee_nD_n=1$ and $\bigwedge_nH_n=0$. Countably many jointly
compatible certificates therefore evade the finite argument; finite
additivity is exactly what permits this.

One natural affine realization nevertheless collapses. Suppose two
exact-one partition equations use a common tail:

\[
x(H_n)+\sum_jx(R_{nj})=1,
\qquad
x(C_i)+\sum_jx(R_{nj})=1.
\]

In a concrete σ-class these are partitions of the same carrier, so
$H_n=\Omega\setminus\bigcup_jR_{nj}=C_i$ as sets, not merely in every
state. Chains of such shared-tail cancellations again give $H_n=C_i$.
If $D_n\le H_n^\perp$ for all $n$, then
$1=\bigvee_nD_n\le C_i^\perp$, contradicting the cluster value one.
Thus fresh auxiliaries connected by cancellable shared partition tails
cannot realize all-remainder trapping. A viable affine construction
must be genuinely contextual/cyclic: its implication $H_n=1$ cannot
come from equality after cancelling a common partition tail.

## 18. Cyclic gadget census: four-loop kill, five-loop cell (2026-07-11, session 24)

The smallest separated cyclic exact-one implication gadget has four
contexts:

\[
\begin{aligned}
C_1+a+b&=1,& C_2+b+c&=1,\\
C_3+c+d&=1,& H+d+a&=1.
\end{aligned}
\]

Setting $C_1=C_2=C_3=1$ forces $a=b=c=d=0$ and $H=1$. Exhaustive
enumeration gives exactly seven supports:

\[
\{b,d\},\{a,c\},\{C_3,H,b\},\{C_2,C_3,a\},
\{C_1,H,c\},\{C_1,C_2,d\},\{C_1,C_2,C_3,H\}.
\]

All incidence columns are distinct. Their canonical set
representation has 18 events, is complement-closed and closed under
every available disjoint union, hence is a finite concrete σ-class OMP.
But it is not a lattice: $a,c$ have the incomparable minimal upper
bounds $b^\perp,d^\perp$, so $a\vee c$ does not exist. More generally,
an incidence-faithful linear gadget whose pruned core is an induced
four-cycle has the same obstruction: opposite intersection atoms have
no common proper upper bound, while the meet of the complements of the
other opposite pair would have to supply one. Pendant contexts and
shared-tail pairs do not repair it. This class is now closed.

The next girth is already inhabited by an OML gadget. In the Greechie
pentagon with blocks

\[
B_i=\{a_{2i},a_{2i+1},a_{2i+2\bmod10}\},
\]

the pairwise-incompatible cluster
$\mathcal C=\{a_0,a_3,a_5^\perp\}$ forces $a_7=0$ by unit propagation:
$a_0=1$ gives $a_1=a_2=0$; $a_3=1$ then gives $a_4=0$;
$a_5^\perp=1$ gives $a_5=0$; $B_2$ gives $a_6=1$; and $B_3$ gives
$a_7=a_8=0$. The §11 state enumeration confirms this is the unique
state charging the cluster and that $a_7$ is incompatible with each
cluster element. Thus a finite OML can perform the desired genuinely
contextual atom kill; latticehood does not obstruct one cell.

The naive countable assembly fails. Repeating pentagon cells while
identifying the three cluster inputs across copies creates induced
inter-copy four-loops—for example the two copies' contexts incident at
the shared $a_3$ and shared $a_5$ close through their private
intermediate atoms. The four-loop obstruction then destroys
latticehood. Consequently the live construction question is no longer
whether an OML atom-killing gadget exists, but whether countably many
such kills can be propagated from one finite cluster through a
**globally high-girth network**, or whether every carrier completion of
the unavoidable short loops restores a principal cluster-face state.

## 19. Pentagon gluing geometry: direct fan-out and serial relay (2026-07-11, session 25)

Two otherwise private pentagon cells sharing input vertices $x,y$
contain an inter-copy Berge cycle of length $2d$, where $d$ is the
shorter block-distance between $x,y$ inside one cell. For the §18 inputs
(sharing $a_5^\perp$ means sharing $a_5$),

\[
d(a_0,a_3)=2,qquad d(a_3,a_5)=2,qquad d(a_0,a_5)=3.
\]

Hence sharing either distance-two pair creates an induced four-loop;
sharing only $\{a_0,a_5\}$ creates a six-loop, and one shared input
creates no inter-copy cycle. Directly sharing all three inputs across
copies necessarily contains four-loops. More generally, finite-source
parallel fan-out through a repeatedly reused distance-two pair is
impossible in an incidence-faithful OML construction. This is sharp:
linearity and girth at least five alone do not forbid serial cactus
assemblies sharing at most one vertex between consecutive cells.

The natural serial pentagon relay fails more strongly. Write the cell
as $B_i=\{x_i,y_i,x_{i+1}\}$ cyclically. The propagation core uses

\[
y_1=1, y_2=0
\quad\Longrightarrow\quad
x_3=1, y_3=x_4=0.
\]

Identifying $(x_3^n,y_3^n)$ with $(y_1^{n+1},y_2^{n+1})$ produces a
three-loop

\[
B_3^n-B_1^{n+1}-B_2^{n+1}-B_3^n,
\]

through the two shared ports and the next cell's intermediate atom.
Using $x_4^n$ as the zero output is identical because the one and zero
outputs cohabit $B_3^n$. If instead the killed targets form the zero
rail and all lie in the master block $M$, then
$M,B_2^{n+1},B_3^{n+1}$ form another three-loop via consecutive targets
and the forced-one atom. Thus this serial architecture fails at
incidence girth before latticehood, σ-completeness, or state-space
separation become live.

The precise next design constraint is a relay with spatially separated
forced-one and forced-zero output ports. Ordinary one-cell pentagon
propagation does not provide it. A multi-cell repeater may still evade
the obstruction; any such design must also keep master-block atoms out
of adjacent relay contexts.

## 20. A composable pentagon repeater and the spaced-master candidate (2026-07-11, session 26)

The separated-port repeater exists already in one pentagon. With blocks
$B_i=\{x_i,y_i,x_{i+1}\}$ modulo $5$,

\[
(x_0,y_1)=(1,0)\quad\Longrightarrow\quad(x_2,y_4)=(1,0).
\]

Indeed $x_0=1$ forces $x_1=y_0=x_4=y_4=0$, and then
$x_1=y_1=0$ forces $x_2=1$. Exhaustive enumeration of the eleven
pentagon states confirms the input has the unique support
$\{x_0,x_2,y_3\}$. The input ports have block-distance two and the
output ports distance three. Serial composition identifies
$x_2^n=x_0^{n+1}$ and $y_4^n=y_1^{n+1}$. The resulting inter-cell cycle
has length $2+3=5$; explicit twofold composition is linear and has only
five-cycles. Thus the relay propagates indefinitely without a three- or
four-loop.

This locates the scope of a no-cloning theorem. In a finite linear
exact-one incidence forest, with blocks of size at least three and seeds
$x=1,y=0$, unit propagation creates at most one fresh value-one vertex.
A new one merges at least two prior zero-components. Initially only the
$x$-component and singleton $y$-component exist, so the first merge
joins them; a second would join zeros already connected and close a
cycle. Cycles are necessary for repeatable propagation, but the
pentagon shows girth five is sufficient.

Attaching a target from every relay cell to one master block creates
short loops. Direct block-distance calculation gives master-cycle
lengths at most four for every available forced-zero atom in consecutive
cells. Spacing the targets repairs this finite incidence defect: choose

\[
D_n=y_2^{\,3n}.
\]

Between consecutive chosen targets the relay-chain block-distance is
five, so adjoining one master block containing all $D_n$ closes a
six-cycle. The root cluster can be
$\{x_0^0,(y_1^0)^\perp,y_3^0\}$; its elements are pairwise incompatible
in the root pentagon and force the unique root relay state. Propagation
then forces every $D_n=0$.

This is a concrete candidate architecture, not yet a witness. If the
countable paste plus master block is a σ-complete OML and its σ-additive
two-valued states order-determine it, represent it on those states. A
free master ultrafilter coheres with the relay pattern and cluster while
killing every $D_n$; σ-additivity on the countable atomic master block
forces some $D_n=1$, so no σ-state charges the cluster. The remaining
checks are exactly:

1. the infinite high-girth paste is an orthomodular lattice;
2. it is σ-complete, including cross-block orthogonal families;
3. the relay/master partial state assignments extend globally; and
4. σ-additive states excluding the cluster are order-determining, giving
   an admissible concrete σ-class representation.

Finite girth and state propagation are verified; checks 1–4 remain
open.

## 21. Spaced-master candidate killed: σ-state separation forces an essential ternary trigger (2026-07-11, session 27)

At the block-equation level, check 3 succeeds. Assign every relay cell
the unique state with support $\{x_0^n,x_2^n,y_3^n\}$ and give the
intended complete master block $\mathcal P(\mathbb N)$ any free
ultrafilter. Both assignments kill every $D_k$ and agree on all pasted
overlaps $D_k,D_k^\perp$, so they define a global f.a. state on the
block paste. Extension through any further lattice/σ-completion would
still require proof.

Check 4 fails before that issue. Every σ-additive master restriction is
principal and charges exactly one $D_k$. Compatible relay paths with a
chosen $D_k=1$ do exist, so σ-states are not absent. But the root
pentagon's absorbing relay state is the unique local state satisfying

\[
\mu(x_0^0)=\mu(x_2^0)=1.
\]

It forces every later $D_k=0$, so no global σ-state realizes this
two-element trace. Consequently all σ-states satisfy

\[
\mu(x_0^0)\le\mu((x_2^0)^\perp),
\]

although incidence-faithfully
$x_0^0\not\le(x_2^0)^\perp$. Thus σ-states introduce a false order and
do not order-determine the candidate. Representation on σ-states is not
an embedding; any completion that instead forces the displayed order
has destroyed the root pentagon. The spaced-master architecture is
therefore **killed**, independently of the unresolved σ-completeness of
the completed master paste.

There is also a bookkeeping correction. A bare infinite Greechie block
on atoms $D_k$ normally supplies only the finite–cofinite Boolean
algebra, which is not σ-complete (the even atoms have no join). Section
20 intended the complete block $\mathcal P(\mathbb N)$; that substitution
must be explicit and its lattice/σ-completeness rechecked in any future
candidate. The standard finitary paste has no three- or four-loops and
is an OML, but fails σ-completeness.

The failure names a necessary design condition. A viable concrete
counterexample needs an **essential ternary trigger**:

1. the full three-block cluster forces the all-remainder regime;
2. no one- or two-piece subtrace already forces that regime; and
3. enough σ-states escaping through the omitted cluster piece remain to
   separate every non-order pair.

The §20 relay violates (2): its third cluster element is redundant for
absorption. This is the state-separation counterpart of 2BR and explains
why a merely binary propagation gadget cannot live in an admissible
concrete representation. The next construction search must begin with
a finite OML ternary trigger whose full input forces an output but every
proper input subpattern admits both output values; only then should it
be repeated or attached to a master block.

## 22. Essential ternary trigger exists in the pentagon (2026-07-11, session 28)

The pentagon census succeeds. Among 240 pairwise-incompatible triples
of nontrivial elements, 215 are jointly chargeable; there are 1,970
triple-to-output implications, and exactly **45** pass the full
proper-subset separation screen. Thus essential ternary forcing is
already a girth-five OML phenomenon.

One transparent trigger is

\[
(C_1,C_2,C_3,H)=(a_1,a_3,a_5^\perp,a_9).
\]

The full input forces successively
$a_0=a_2=a_4=a_5=0$, $a_6=1$, $a_8=0$, and $a_9=1$.
Its full-input state has support $\{a_1,a_3,a_6,a_9\}$. Every proper
input subset admits both $H$ values; it is enough to display pair
witnesses:

| charged pair | $H=0$ support | $H=1$ support |
|---|---|---|
| $C_1,C_2$ | $\{a_1,a_3,a_5,a_8\}$ | $\{a_1,a_3,a_5,a_7,a_9\}$ |
| $C_1,C_3$ | $\{a_1,a_4,a_8\}$ | $\{a_1,a_3,a_6,a_9\}$ |
| $C_2,C_3$ | $\{a_0,a_3,a_6\}$ | $\{a_1,a_3,a_6,a_9\}$ |

The input elements are pairwise incompatible. The implication is not a
carrier equality: the full input selects one state, while $a_9$ is
charged by five pentagon states.

For master-block use, the complementary-output variant is better:

\[
(C_1,C_2,C_3,H)=(a_1,a_3^\perp,a_7^\perp,a_9^\perp).
\]

Here the killed target $D=H^\perp=a_9$ is an atom. Propagation is

\[
a_1=1\Rightarrow a_0=a_2=0,quad
a_3=0\Rightarrow a_4=1,quad
a_4=1\Rightarrow a_5=a_6=0,quad
a_7=0\Rightarrow a_8=1,quad
a_8=1\Rightarrow a_9=0.
\]

The unique full-input support is $\{a_1,a_4,a_8\}$. Proper-pair
witnesses for target values $a_9=1/0$ are supplied by supports
$\{a_1,a_4,a_7,a_9\}/\{a_1,a_4,a_8\}$,
$\{a_1,a_3,a_6,a_9\}/\{a_1,a_4,a_8\}$, and
$\{a_2,a_6,a_9\}/\{a_2,a_5,a_8\}$ (with the pair order
$(C_1,C_2),(C_1,C_3),(C_2,C_3)$). Exhaustive state-table checking
confirms all singleton and empty-subset screens as well.

This repairs the finite separation defect of §21: no proper input trace
already forces the killed atom. It does not yet solve the countable
problem. The next task is to find separated relay ports or a high-girth
composition of these ternary cells that preserves essentiality under
iteration and permits σ-state escapes for every proper finite trace.

## 23. Essential composition and an indirect two-overlap relay (2026-07-11, session 29)

For any finite composite with external inputs $E$, output $h$, and state
relation $R$, full proper-subset escape is equivalent to the maximal
proper checks

\[
\forall i\in E\ \forall e\in\{0,1\}\quad
\exists r\in R:\ r_j=1\ (j\ne i),\ r_h=e. \tag{*}
\]

This yields a tree-composition lemma: essential ternary cells glued
along one output/input Boolean pair per edge, with a tree cell graph and
no extra state constraints, preserve essentiality from their external
leaves to the root output. The proof follows the unique omitted-leaf
path, choosing opposite-output witnesses there and full rows off the
path. Two cells expose five leaves, however, so this does not itself
give a fresh ternary relay.

The exact-three-port two-pentagon class is negative. Of 126
value-compatible maps into the next canonical atom pattern
$(a_1,a_3,a_7)=(1,0,0)$, the 24 maps using three fresh old ports have no
girth-five essential instance. The tempting
$(a_8,a_2,a_5)\mapsto(a_1,a_3,a_7)$ map is essential but contains an
induced four-loop.

Widening to arbitrary two-atom identifications produces a winner. Glue
successive pentagons by

\[
a_3^n=a_7^{n+1},qquad a_8^n=a_4^{n+1}. \tag{R}
\]

The full state of cell $n$ has $a_3^n=0,a_8^n=1$, hence in cell $n+1$
we have $a_7=0,a_4=1$. Exact-one propagation then gives
$a_3=0$, $a_8=1$, $a_0=a_2=a_5=a_6=a_9=0$, and finally $a_1=1$.
Thus (R) regenerates the fresh canonical ternary input and kills the
fresh target $a_9^{n+1}$.

Exhaustive two-cell enumeration gives 36 states. The full root triple
uniquely fixes the root state and forces the next target zero; every
proper root subset permits the next target both values, so (*) holds.
There are exactly three essential girth-five two-overlap maps among
4,500 ordered maps; (R) has the best target geometry. Self-chains through
six cells remain linear of girth five. Distances between targets in
cells separated by gaps $1,2,3,4$ are $4,4,6,6$, so adjoining one
complete atomic master block makes the shortest master cycle length
five.

This is a stronger candidate than §20: the absorbing regime is
essentially ternary at every verified finite composition, removing the
explicit two-trace nonseparation that killed the binary relay. It is not
yet a witness. The infinite chain plus complete master block must now
pass:

1. latticehood and σ-completeness after Boolean completion of the master;
2. extension of the free master state;
3. existence of enough principal-master σ-state escape paths; and
4. full order separation by those σ-states, not merely proper-root-trace
   escape on finite truncations.

## 24. Indirect relay killed: finite escape is not ω-live (2026-07-11, session 30)

The candidate passes the structural half. Replacing the master by the
literal complete Boolean algebra $\mathcal P(\mathbb N)$ yields a
complete OML, provided the periodic no-three/four-loop claim is proved
globally (the finite-witness Greechie lattice argument then applies).
Every proper non-master upper interval is finite; master intervals are
complete Boolean intervals, with only a finite wing below each
$D_n^\perp$. Families with a proper upper bound therefore have a least
one, and families without one join to $1$. The full relay pattern plus a
free master ultrafilter glues blockwise to the intended non-σ f.a. state.

Principal-master paths also exist: the relay state automaton admits an
infinite path with target word $0^k10^\infty$ for every $k$. But these
paths do **not** order-determine the root pentagon. All σ-states satisfy

\[
\mu(a_2^0)\le\mu(a_9^0),
\]

although $a_2^0,a_9^0$ are distinct atoms and
$a_2^0\not\le a_9^0$. The proof is finite-state. A local state with
$a_2=1$ is one of three possibilities. Two already have $a_9=1$. The
third has $a_9=0$ but transitions to the absorbing full-trigger state,
which then forces every future target to zero. It cannot lie on a path
with principal master restriction. Thus the only abstract witness to
$a_2\not\le a_9$ is not σ-extendable.

The indirect relay is therefore **killed at check 4**. Its finite
proper-trace escape certificate was genuine but insufficient: the
opposite-target witness exists on every finite truncation and only dies
at the infinite continuation boundary.

This sharpens the design criterion from essentiality to
**ω-live separation**. For a relay transition automaton, call a local
state σ-live if it lies on some infinite path whose master-target word
has exactly one $1$. A viable candidate must satisfy at minimum:

1. σ-live states order-determine every cell OML;
2. compatible σ-live paths separate cross-cell non-orders; and
3. the full cluster state lies outside the σ-live set and has a free
   master continuation.

Finite essentiality says only that both target values occur locally; it
does not imply the witnesses are σ-live. This screen is computationally
cheap and must be applied before any further infinite completion work.
The two other essential girth-five two-overlap maps from §23 remain
uncertified and are the immediate next candidates.

## 25. ω-live census: ternary route killed, removable-state relay found (2026-07-11, session 31)

The two remaining §23 maps fail locally. For
$(a_3,a_8)\mapsto(a_5',a_8')$, the σ-live root states force the false
atom order $a_1\le a_9$. For
$(a_4,a_9)\mapsto(a_4',a_7')$, they force $a_0\le a_3$. Thus all three
known essential ternary relays die before cross-cell testing.

This is structural for the pentagon's 45 essential ternary triggers.
The canonical eleven-state representation has exactly one individually
removable state while retaining order determination: the all-odd state

\[
s_*:\quad\operatorname{supp}(s_*)=\{a_1,a_3,a_5,a_7,a_9\}.
\]

Every other state is the unique witness to some non-order. The full
fibres of all 45 essential ternary implications exclude $s_*$ and
contain at least one indispensable state. If such a full fibre is made
the nonprincipal all-target-zero basin, σ-states necessarily lose that
order witness. Hence the entire three-input pentagon-trigger route is
killed, not merely the three relay maps tested.

The correct pivot is the five-block cluster

\[
\mathcal C_*=\{a_1,a_3,a_5,a_7,a_9\},
\]

whose elements are pairwise incompatible and whose unique state is
$s_*$. This is beyond the minimal three-block locus but still a valid
T4/B′(i) falsification target; crucially, deleting its local state leaves
the other ten states order-determining, exactly as in the certified
reduced pentagon representation of §11.

The first targeted relay census produced a crucial correction rather
than a candidate. Among 1,000 oriented bijective two-atom
identifications with two-cell girth at least five, 275 make $s_*$ a
fixed point. A preliminary filter found 170 maps whose σ-live set is all
eleven states. This is **failure**, not maximal success: if $s_*$ itself
is σ-live, then the full cluster already has a principal-master
σ-extension and T4 holds.

A clean representative is

\[
a_1^n=a_5^{n+1},qquad a_7^n=a_3^{n+1}. \tag{M*}
\]

Both ports are odd, so $s_*$ propagates and kills $D_n=a_0^n$ in every
cell. Target block-distances for gaps $g=1,2,\ldots$ begin

\[
4,5,8,9,12,13,16,17,\ldots,
\]

with $d_g=2g+2$ for odd $g$ and $d_g=2g+1$ for even $g$. Therefore all
targets may lie in one complete master block: the shortest master cycle
has length $d_1+1=5$.

The displayed $M^*$ map is one of these: it has a free $s_*$ self-loop
but also a principal-master path beginning at $s_*$. It is not an
all-remainder configuration. Even ignoring that, product-automaton
testing finds the adjacent false order
$a_4^0\le(a_4^1)^\perp$. Thus the positive interpretation above is
withdrawn; the geometry data remain valid diagnostics.

## 26. Corrected removable-state census kills all two-port pentagon relays (2026-07-11, session 32)

The correct local requirements are simultaneous:

1. $s_*$ has an all-zero-target infinite path;
2. $s_*$ is **not** σ-live for an exactly-one-target path; and
3. the σ-live states order-determine the full pentagon.

The exhaustive two-port census is decisive. Start with all 4,050
oriented bijections between an old atom pair and a new atom pair. After
quotienting the two pentagons, reject collapsed blocks, pairs of blocks
sharing more than one atom, and Berge three/four-cycles. Exactly 1,000
maps remain. Of these, 275 give $s_*$ a free zero self-loop, and 45 also
make $s_*$ non-σ-live. **None of the 45 has σ-live states that
order-determine the pentagon.** Their live-set sizes are

\[
0:5,\quad4:2,\quad5:4,\quad6:30,\quad9:4,
\]

and their false-nonorder counts are respectively distributed as
$4:4$, $55:30$, $65:2$, $71:2$, $102:2$, $350:5$. No map has the ideal
ten-state live set. Seven of the 45 independently satisfy the complete
master-cycle girth requirement, but all already fail locally. The same
zero-survivor verdict holds under the boundary-root-only liveness
convention.

Therefore the entire two-atom-identification pentagon relay class is
killed before cross-cell or completion checks. The failure is a genuine
tradeoff: maps with enough σ-live states to separate locally also make
the forbidden cluster state σ-live; maps excluding it lose other
indispensable witnesses.

The next uncovered finite classes are (i) three-or-more atom
identifications between two cells, subject to girth five, and (ii)
three-cell relays. Both must apply the corrected three-condition screen
before any master or infinite construction work. A larger finite OML
with a removable face richer than the pentagon's single state is the
co-equal alternative.

## 27. Next finite classes: k≥3 two-cell EXIT B, one-port three-cell unconditional no-go, and a richer removable face found (2026-07-11, session 33)

> **s34 resolution of the late s33 alarm.** The alleged σ-liveness bug
> was a convention mismatch.  The relay is a one-sided chain rooted at
> cell 0 and asks whether a state occurs at any position of a rooted
> path.  Period-collapse across phases and cyclic-rotation invariance
> instead assume a two-sided/translation-invariant chain, so they are not
> valid tests here.  An independent product-graph oracle agrees with
> `relay_core.analyze.live` on all 4,150 period-1 one/two-port maps and
> 600 sampled period-1/2/3 relays.  Hence the liveness-dependent s32/s33
> census results below stand.  The alternative 47-map computation uses
> the different two-sided convention.

The corrected screen of §26 was first reproduced exactly (4,050 → 1,000 →
275 → 45 → 0, both distributions, root-only 0; the M* gap sequence
4,5,8,9,12,13). One correction: the §26 "seven of 45 meet the master
girth requirement" line has no clean definition giving seven. Gap
distances are non-monotonic, so the shortest master Berge cycle is
$\min_g d_g + 1$, and **zero** of the 45 meet $\min_g d_g \ge 4$; the
"seven" was a loose diagnostic and was never load-bearing (all 45 fail
condition 3 locally regardless).

**Two-cell route (a): complete, EXIT B.** Coverage is total. For $k\ge6$
identifications there is no girth-valid map at all (six pentagon atoms
force a co-block pair whose two images would need block distance $\ge4$,
above the pentagon diameter; verified vacuous for $k=6,\dots,10$). For
$k=4,5$ every girth-valid $s_*$-preserving map has empty σ-live set
(condition 3 fails maximally, 350 false non-orders), so they die AT the
screen. For $k=3$ the screen is, for the first time, **not** the killer:
of 500 girth-valid maps, four pass all three local conditions with the
ideal ten-state σ-live set (all states but $s_*$), 0 false non-orders.
Their liveness was independently confirmed by explicit lasso construction
(automaton and lasso live-sets agree on all four). But all four die
downstream: two grow a Berge 3/4-cycle in the periodic chain by the third
cell (the 2-cell window girth is too local — the §24 global-girth
lesson), and two have $\min_g d_g = 2$, so the target-collecting master
block closes a Berge triangle; escaping that needs a spaced/multi-master,
the §20 route killed in §21/§27-prior. So $k=3$ is an honest **Exit B**:
screen-survivors exist but none reaches a witness.

**Three-cell route (b): one-port unconditional no-go, two-port design-
scoped.** Period-3 relays $(m_0,m_1,m_2)$. The full product of all 100
girth-valid one-port interfaces — $10^6$ triples, **no** $s_*$-preserving
pre-cut — yields zero screen-survivors at every phase: an unconditional
one-port no-go. The two-port product ($1000^3=10^9$) is infeasible whole;
within the s32 removable-state design class ($s_*$-preserving interfaces,
$275^3=2.08\times10^7$ triples) the result is **zero survivors at every
phase** — a no-go within the design class. Two-port outside the design
class is not covered and is not claimed closed.

**Co-equal route, Exit C: a richer removable face EXISTS.** The pentagon
is the degenerate zero-slack case — its only removable object is the
single state $s_*$; it has **no** face $F(C)$ with $|F|\ge2$ and
order-determining complement. Larger girth-≥5 Greechie OMLs have such
faces abundantly: the 6-loop has 18, the 7-loop 154, and two pentagons
sharing one atom have 4,825 (faces up to $|F|=10$), all with
full-state order-determination intact. A clean exemplar (7-loop, cluster
$\{a_0,a_3,a_{11}\}$, $|F|=3$) is *jointly* removable and each face state
is *individually* dispensable — the slack the pentagon lacks. **This
establishes only the local precondition.** The operative question the
co-equal route exists for — does the richer face avoid the pentagon's
dynamic liveness/separation tradeoff? — is untouched, because the tradeoff
lives in the σ-liveness of an infinite relay that is unbuilt for these
OMLs. Individual dispensability is a static property, suggestive not
probative. Next: generalize the relay automaton to the chosen OML, put
the whole face $F$ in $s_*$'s role, and run the three-condition screen;
the tradeoff is avoided iff some port makes *every* face state non-σ-live
while the complement stays σ-live and order-determining.

Machinery and full tables: `../verification/census_2026-07-11_s33/`
(`relay_core.py`, `s33_reproduce_s32.py`, `s33_census_k3plus.py`,
`s33_verify_survivors.py`, `s33_census_3cell.py`, `s33_face_census.py`,
`RESULTS.md`).

## 28. Operative richer-face screen: 7-loop period-one widths 1–3 are a bounded no-go (2026-07-12, session 35)

The §27 local precondition has now been tested dynamically on its clean
7-loop exemplar.  The cell has blocks
$B_i=\{a_{2i},a_{2i+1},a_{2i+2\bmod14}\}$, 29 two-valued states, and the
cluster $C=\{a_0,a_3,a_{11}\}$ selects a three-state removable face
$F$.  Its 26-state complement order-determines all 714 canonical
nonorders.  A necessary target correction is that every state in $F$
charges $a_0$; the common-zero target atoms are instead
$a_1,a_2,a_4,a_{10},a_{12},a_{13}$.  The cluster stabilizer pairs these
into three orbits $(1,13),(2,12),(4,10)$.

Exhaust every period-one oriented injective atom port of widths one through
three.  Per target, width one has 196 maps (all two-cell-girth-valid) and
width two has 16,562 maps (9,408 valid); neither has an operative
survivor.  Width three has 794,976 maps, 122,500 valid.  The operative
counts for targets $1,2,4,10,12,13$ are respectively
$2,9,0,0,9,2$.  Here operative means simultaneously: every face state
has a free all-zero path, no face state is σ-live, and the live complement
order-determines the cell.  Sixteen of the 22 pairs have live set exactly
$\Omega\setminus F$; the other six retain an order-determining 25-state
subset.

All 22 die downstream.  The four target-$1/13$ pairs fail relay girth in
the three-cell window.  The remaining 18 (nine reflection orbits) pass
quotient girth through six cells, but every one fails the complete-master
geometry already at adjacent targets: $d_1=2$ or $3<4$, producing a
master Berge cycle of length at most four.  None reaches cross-cell
separation.

Thus the richer face does avoid the pentagon's local liveness tradeoff—
genuine screen-survivors exist—but not the downstream geometry in this
class.  This is a rigorous bounded Exit B for the named face, period one,
and widths $k\le3$ only.  Widths $k\ge4$, periods $p\ge2$, other 7-loop
faces, and the higher-slack two-pentagon cell remain open.

Machinery and tables: `../verification/census_2026-07-12_s35/`,
`../verification/audit_s35_7loop_census.py`, and
`../verification/verify_s35_survivor_girth.py`.

## 29. Width four reaches geometry but fails rooted σ-separation; period-two width one empty (2026-07-12, session 36)

Continue with the same 7-loop face and exhaust all period-one width-four
ports.  Of $\binom{14}{4}^2 4!=24{,}048{,}024$ labeled maps, 477,848 pass
the pair-distance prefilter and **477,652** pass the exact two-cell
quotient girth test.  The 196-map difference matters: a short Berge cycle
may alternate across three or four identifications, so the pair rule is
necessary but not sufficient.  The operative survivor counts for target
representatives $a_1,a_2,a_4$ are $8,40,1$ (98 pairs after the cluster-
stabilizing reflection).

Only two representatives survive relay girth and the complete-master
distance gate, both at target $a_1$:

\[
((0,11),(3,5),(6,9),(13,3)),\qquad
((1,7),(5,9),(11,11),(12,3)).
\]

Both have $d_1=4$, pass target gaps through 60, and retain relay girth five
through 120 cells.  Both fail σ-state order separation.  The exact rooted
path oracle kills them already in cell zero: the first misses the genuine
nonorder $a_0\not\le a_4$, the second $a_0\not\le a_{10}$.  An independent
adjacent-cell computation also finds unwitnessed cross-cell nonorders.

The lesson is semantic but not a liveness correction: the phase `live`
mask is the union of restrictions occurring at *any* position, whereas
the boundary cell has only the root-live restrictions $E_1[0]$.  A phase
mask may order-determine the repeated local type while the actual root
cell does not.  Root-cell order determination and fixed-offset separation
are therefore mandatory downstream gates.

Combining §§28–29 gives a rigorous bounded Exit B for the named face,
period one, every injective width $k\le4$.  Separately, the complete
period-two width-one census has zero operative pairs among all
$196^2=38{,}416$ ordered pairs.  Period-two width two remains open:
274,299,844 raw pairs, 88,510,464 after individual interface validity,
with three-cell girth providing little further pruning.  A signature/
bitset census is the next bounded computation.

Artifacts: `../verification/census_2026-07-12_s36/`,
`../verification/audit_s36_k4_reduction.py`,
`../verification/audit_s36_candidate_*`, and
`../verification/audit_s36_p2_*`.

## 30. Period-two width-two exhaustive no-go (2026-07-12, session 37)

The complete period-two width-two census is empty.  There are 9,408
individually valid labeled interfaces and therefore
$9{,}408^2=88{,}510{,}464$ ordered interface pairs.  Exact rooted
two-phase fixpoints were evaluated for target representatives
$a_1,a_2,a_4$; the operative counts are $0,0,0$.  Reflection gives zero
for $a_{13},a_{12},a_{10}$.  Since no pair passes the local face-free,
face-nonlive, live-complement order screen, no downstream gate can restore
a candidate.

The optimized engine was triangulated against an independent Python
implementation on all 230,496 period-two width-one map/target cases and
6,000 deterministic width-two cases, with exact agreement for every
fixed-point and screen mask.  The audit again finds examples with
$E_1[0]\ne\operatorname{live}[0]$, preserving §29's mandatory root-cell
gate.  All 9,408 complete successor signatures are distinct, so exact
signature bucketing offers no hidden quotient.

Thus the named 7-loop face is closed for period two and widths $k\le2$.
The next inexpensive exhaustive class is period three, width one
($196^3=7{,}529{,}536$ triples).  Larger brute-force jumps should wait for
a structural rooted-separation or master-distance reduction.

Artifacts: `../verification/census_2026-07-12_s37/`,
`../verification/audit_s37_p2_optimizer*`, and
`../verification/audit_s37_downstream_*`.

## 31. Period-three width-one exhaustive no-go and failure concentration (2026-07-12, session 38)

The complete period-three width-one census is also empty.  All
$196^3=7{,}529{,}536$ ordered labeled interface triples were evaluated with
the exact rooted three-phase fixed points and the mandatory boundary-cell
$E_1[0]$ order gate.  For target representatives $a_1,a_2,a_4$, the operative
counts are $0,0,0$; reflection supplies the other three common-zero targets.

The sequential failures sharpen the earlier no-go.  For $a_1,a_2,a_4$,
respectively, face freedom first removes $1{,}488{,}811$,
$1{,}496{,}688$, and $1{,}476{,}353$ triples.  Face nonliveness then removes
$6{,}040{,}350$, $6{,}032{,}443$, and $6{,}052{,}798$.  Only $375,405,385$
cases satisfy both local face conditions, and every one fails live-complement
order determination.  Thus the local free/nonlive tension is overwhelmingly
dominant, while its rare exceptions lose indispensable order witnesses; no
triple reaches the root-cell gate.

An independent Python monotone-bitset implementation agrees on every fixed
point and screen mask for 1,000 deterministic triples across all six targets
(6,000 comparisons).  The named face is now closed at width one for periods
one through three, alongside the previous period-one $k\le4$ and period-two
$k\le2$ bounds.

Artifacts: `../verification/census_2026-07-12_s38/` and
`../verification/audit_s38_p3_optimizer*`.

---

*Feeds: shovel plan §2; frontier item 1 (this is its load-bearing case);
spine §4 scoping caveat (sufficiency side). Companions:
`HANDOFF_2026-07-12_boundary_descent.md` (current theorem-status and
execution handoff),
`relational_boundary_descent.md` (exact GSD/gluing formulation,
finite-interface quarantine, finite-atlas full-block localization, conditional
boundary-defect localization under face-image openness, a counterexample with
compact boundary Stone space to
automatic shadow openness, and the distributed-selection/rooting audit),
`oml_boundary_regularity.md` (genuine coarse reducible OML realization of a
dense nonopen shadow and σ-liftable locus; mixed-hierarchy decision),
`HANDOFF_2026-07-12_s38.md` (current execution order),
`HANDOFF_2026-07-12_s37.md` (prior),
`HANDOFF_2026-07-12_s36.md` (prior),
`HANDOFF_2026-07-12_s35.md` (prior),
`HANDOFF_2026-07-12_s34.md` (prior),
`HANDOFF_2026-07-11_s33.md` (prior; late alarm resolved in s34),
`HANDOFF_2026-07-11_s32.md` (prior),
`../sigma_essential_taxonomy.json` (walls, gluing map),
`../sigma_essential/czech_school_prior_art_sigma_essential.md`,
`../sigma_essential/sharp_skeleton_RDP_subroute_verdict.md`.*
