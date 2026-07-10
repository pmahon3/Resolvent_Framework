# Theorem 2 attack — the OML-lattice case at the regularity transition

*Opened 2026-07-10 (session 8), per `shovel_plan.md` §2 + §Execution-order.
This is the attack-opening note the frontier map prescribes: collect the three
meet-destruction mechanisms into one frame; say what a unified
liftability-from-latticehood argument needs; find where it first breaks.
Yield = sharpened conjectures + named obstruction, not a proof.*

*Status of everything below: ⟦HAND⟧ framing over verified corpus pointers;
no new theorem claimed.*

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
  Derr–Williamson (Polish ⟹ Φ). Call this the **representability form**:

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
corpus already mapped (`czech_school_prior_art_sigma_essential.md`).

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
   non-lattice OMP — `sharp_skeleton_RDP_subroute_verdict.md`). Where
   pasting does give concrete lattices the results are confined to
   finitary Kalmbach-type K(L) (Mayet–Navara 1995) — no σ. The located
   literature gap: *no paper realizes a non-simplex state space on an OML
   simultaneously concrete AND σ-complete*
   (`czech_school_prior_art_sigma_essential.md` §POSITIVE).

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
  when overlaps are meet-closed.

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
  the σ-form; `czech_school_prior_art_sigma_essential.md` §4).
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
representability, which is exactly 2a). No theorem occupies the gap, and
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
  DW's inner-regularity is near-automatic (`sigma_essential_prior_art_verdict.md`).
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

**(i) BNPW is provably NOT a lattice ⟦HAND — derivation over verified
text, elementary⟧.** Dirac states on any concrete logic are 2-valued,
σ-additive (automatic: point-evaluation respects any disjoint countable
union that exists in L), and full. On BNPW's object every σ-additive state
is JP (Q5.4 note), so all Dirac states are JP; a JP Dirac state at
x ∈ A∩B produces nonempty C ∈ L, C ⊂ A∩B, i.e. the logic is
downward-directed; Prop 4.4 then forces any lattice to be Boolean; BNPW's
object is non-Boolean, hence **not a lattice**. Skeleton C's second half is
untouched; BNPW joins the every-wild-object-is-a-non-lattice pattern (now
forced, not inferred). *Residual risk: the derivation trusts MPT 1992's
one-line report of BNPW's content; the ILL pull remains worthwhile as
confirmation, no longer as a gate.*

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

**(iv) Closed leads.** arXiv:2308.08508 = Harding–Kornell, "Completely
hereditarily atomic OMLs" (algebraicity/covering property/Kalmbach+Keller
constructions) — no JP or σ-additivity content; irrelevant to this attack
(background only for 2a construction techniques). Bunce–Hamhalter 2000:
scout could not access full text or any substantive secondary description
(Springer/WorldSci/zbMATH/ResearchGate all blocked); scope unknown —
**cite nothing from it; ILL pull stands**, now first in the queue.

## 8. Exit criteria for the attack

- **Sharpened-conjecture exit (expected):** 2a and/or the σ-JP question
  stated precisely with the literature swept — an open problem with stakes.
- **Kill exit:** a located theorem or construction settling Ψ_OML either
  way (scout the JP line before investing hand-work).
- **Proof exit (unexpected this session per frontier map):** one of
  Skeletons A–C closes.

*Feeds: shovel plan §2; frontier item 1 (this is its load-bearing case);
spine §4 scoping caveat (sufficiency side). Companions:
`sigma_essential_taxonomy.json` (walls, gluing map),
`czech_school_prior_art_sigma_essential.md`,
`sharp_skeleton_RDP_subroute_verdict.md`.*
