# Theorem 2 attack — the OML-lattice case at the regularity transition

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
✎s17 (2026-07-11): the foundation layer is now LEAN-VERIFIED —
`formalization/QuerySystem/QuerySystem/ConcreteOMLBlocks.lean`:
A1(a)–(c), L0 (both directions), C1′, and T3 (in full, on abstract
countably generated σ-fields) are axiom-free; A2 and the composite
"σ-states are Dirac on countably generated blocks" are machine-checked
modulo the ONE flagged cited axiom `foulis_holland_commute`
(= Foulis–Holland/commutant closure, Kalmbach Thm 5 / Bruns–Harding
2.2–2.8; the concrete upgrade through L0 is proved). `#print axioms`
receipts at file end. T1/P1 and the block-OVERLAP clause of A2 remain
hand-only. Awaits user ratification (now = read the one axiom against
its citation + accept the build).
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
NEXT, in order of leverage: (1) attempt B′(i) directly; (2) Skeleton A
read (`derr_williamson_2023.pdf` Thm D.6 + `maharam_1972.pdf` §8) with
the T3-specific question; (3) hunt a coarse-block toy: a concrete
σ-class OM lattice with one countable/co-countable-type block and one
incompatibility — even a failed construction will name the next wall.

## 10. Skeleton A read (2026-07-10, session 13): DW Thm D.6 + Maharam §8 — the T3 question answered

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
(10d(ii)–(iii)). Menu now, in order of leverage: (1) B′(i) with the
kernel-FIP shape + Marczewski pulls; (2) coarse-block toy hunt
(promoted — decides Theorem 2's second factor); (3) Skeleton C surviving
branch (PP1994). Owed: ~~s12-standard proof-read of §10~~ CLEARED
2026-07-10 s14 (receipt `PROOF_READ_2026-07-10_attack_s10.md`).

## 11. B′(i) direct attempt (2026-07-11, session 15): the cluster reduction, the Stone-density reframe, and the Marczewski read

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
general 𝒮, or a compactness argument replacing it) proves B′(i). **Next
concrete step:** run the crux through Maharam's topology-free f.a. glue
(Thm 6.1 / condition (8.2), anatomized §10a layer 1): "point Bl₀ at D
keeping the cluster" is a blockwise family whose (8.2)-consistency is a
computation in the cluster's finite geometry. Either it always passes —
crux resolved, B′(i) follows — or the failing inequality names the wall
intrinsically.

### 11g. Exit status

No proof, no refutation. Banked: 2BR (open locus = ≥ 3 blocks; witness's
|V| = 3 optimal), cluster normal form, P⁼ (pointed ⟺ σ; B′(i) = pure
selection problem; compact classes reassigned to the coarse factor),
kernel-FIP correction to §10e, representation-dependence of K(s) = ∅,
Φ-as-density, Marczewski read + intrinsic wall statement for the coarse
factor, T4 + crux ladder. Menu next (any order): (1) **T4 via Maharam
(8.2)** — now the sharpest B′(i) step; (2) coarse-block toy hunt
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

---

*Feeds: shovel plan §2; frontier item 1 (this is its load-bearing case);
spine §4 scoping caveat (sufficiency side). Companions:
`../sigma_essential_taxonomy.json` (walls, gluing map),
`../sigma_essential/czech_school_prior_art_sigma_essential.md`,
`../sigma_essential/sharp_skeleton_RDP_subroute_verdict.md`.*
