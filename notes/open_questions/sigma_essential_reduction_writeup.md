# The σ-essential contextual witness localizes to a non-Dirac σ-state core

*(Title was "…reduces to σ-point-selection"; corrected 2026-06-25 — it is a
LOCALIZATION to clause (ii), not a reduction to a separate harder named problem. See
§1 and the airtight verification.)*

*Standalone writeup, 2026-06-25. For understanding and record (not submission). This
consolidates the scattered ledger material into one coherent statement. The terse
working record is `CHARTED_sigma_essential.md`; the result-with-corrections is
[[sigma_essential_reduction_result]]; the forcing-context post-mortem is
[[forcing_programme_status]]. ⟦HAND throughout — verified at sketch level + advisor-
checked; not Lean-formalized, not refereed.⟧*

---

## 0. The question

Is there a **concrete σ-essential contextual witness**: a concrete σ-complete
non-Boolean off-center orthomodular lattice `L ⊆ P(Ω)` (orthocomplement =
set-complement, joins of orthogonal elements = disjoint unions) carrying a finite
sub-orthoposet `B ⊆ L` and a 2-valued state `s₀` on `B` that extends to **no** global
σ-additive 2-valued state on `L`?

Motivation: this is the lattice-theoretic form of "a contextual probability assignment
witnessed by no finite sub-system but blocked at the σ-level" — the residue of the
OML-descent programme, and (independently) the same realization gap that parks Paper I.

## 1. The result — a verified LOCALIZATION (the problem's spine, not its headline)

**What this is, stated honestly (⚠ reframed 2026-06-25).** This is NOT a "theorem"
in the banked sense that headlines a paper — the *headline question* (does the
σ-essential witness exist / is its existence ZFC-independent) is **open**. What we
have is a **precise problem statement with a verified decomposition**: a clean iff
that isolates the irreducible hard core. That decomposition is the rigorous spine that
makes the open question sharp.

> **Localization (the verified decomposition).** A concrete σ-essential witness exists
> **iff** (i) no point-evaluation `δ_ω` extends the local pattern `s₀` **and** (ii) no
> **non-Dirac** σ-additive 2-valued state extends it. Clause (i) is **concrete and
> freely arrangeable** (the Navara–Pták device makes it hold for free); therefore all
> the difficulty — and any set-theoretic sensitivity — **localizes to clause (ii): the
> existence of a non-Dirac σ-additive 2-valued state realizing `s₀`.** Call clause
> (ii) the **σ-point-selection** core. ⟦HAND-verified 7/7,
> `reduction_airtight_verification.md`.⟧

**On Lean (programme standard = zero-sorry Lean for *novel* results): the localization
is EXEMPT, not pending.** The iff (claims 4–5) is a *partition tautology* (a state is
Dirac or non-Dirac; "no state extends `s₀`" iff "no Dirac" ∧ "no non-Dirac"); its
content — clause (i) freely arrangeable — rests on the **Navara–Pták example (their
published theorem, cited)**, not a novel result of ours. So there is no novel
non-tautological kernel here for Lean to certify; formalizing it would add rigor where
it is least needed. The Lean step belongs **later, on a real partial result about
clause (ii)** (the open part) — rescheduled by the honest reframe, not skipped.

**Honest scope (⚠ corrected — this is a localization, NOT a reduction to a harder
named problem).** σ-point-selection is *our name for clause (ii)*; it is written down
in no prior literature (validation scouts). So the value is **localizing** the witness
question to its non-Dirac core — *not* an equivalence with a separate, recognized,
harder problem. ("Witness ⟺ no σ-state-of-any-kind extends `s₀`" is a tautology — it
just unfolds the definition of witness; the content is that the *Dirac* half is
arrangeable, so the weight falls entirely on the *non-Dirac* half.) Whether (ii)
carries *measurable-cardinal strength* is CONJECTURED, not established (§5/§6: the
strength claim rode the struck Blecher–Weaver weld; only the refutation side has
independent evidence touching "no measurable cardinal").

The witness is neither built nor refuted; it is *located* — its difficulty pinned to
the non-Dirac realization core (ii).

## 2. Why (the mechanism) — ⟦verified 2026-06-25, `reduction_airtight_verification.md`⟧

Let `B ⊆ L` be a **⊥-closed finite sub-orthoposet** (the quantifier is sub-orthoposets,
not generating sets — load-bearing below) and `s₀` a 2-valued state on `B`. Every
global σ-additive 2-valued state on `L ⊆ P(Ω)` is either a point-evaluation `δ_ω`
(always a σ-state) or **non-Dirac**, and these exhaust all σ-states. So `s₀` **extends
to no** global σ-state iff:

(i) **no `δ_ω` extends it** — i.e. `⋂{A ∈ B : s₀(A)=1} = ∅`. (The `s₀`-false
    constraints are *subsumed*: `B` ⊥-closed ⟹ a false `A` has `A^⊥ ∈ B` true, already
    in the intersection — so only the `s₀`-true elements matter.) This is freely
    arrangeable: the Navara–Pták 1983 intersection device (`B∩C∩D=∅` on a concrete
    σ-class over ℚ²) makes the intersection empty for free; **and**

(ii) **no non-Dirac σ-state extends it** — the **σ-point-selection** core.

Hence **witness ⟺ (i) ∧ (ii)** (both negative clauses; the partition Dirac/non-Dirac
is exhaustive of all σ-states). Since (i) is arrangeable, the witness question is
*essentially* (ii), modulo the freely-arranged (i): a **localization** of the
difficulty to the non-Dirac realization core — not an equivalence with a separate
harder problem (§1).

**Navara–Pták supplies two things** (verified against the paper): the
*concentration = Dirac* identification (their "concentrated measure" := `∃x, m(A)=1
⟺ x∈A`, i.e. `δ_x`), which is what clause (i) uses; and their **explicit example** — a
2-valued σ-state that is *not* concentrated (`B∩C∩D=∅`) — which is a genuine non-Dirac
state extending the local pattern. So their example *satisfies (i) but fails (ii)*:
the device alone is **not** a witness because N–P *build the rescuer*. That is exactly
why the whole weight falls on (ii). (We use their concentration concept + example, not
their integration-additivity theorem, which concerns a different question.)

## 3. Three walls, kept distinct

The reduction's "bottom" is one of three distinct objects; conflating them was the
recurring error, so they are named separately:

| | wall | character | cardinal? |
|---|---|---|---|
| **A** | **σ-point-selection** | does a coherent local 2-valued pattern extend to a global σ-additive **state**? | CONJECTURED (the Ulam link via Blecher–Weaver is the Hilbert analogue, STRUCK as a transfer — §5; only the ¬-side has independent cardinal evidence) |
| **B** | **faithful-tribe-representability** | does `L` embed faithfully into a σ-tribe of *honest sets*? | — |
| **C** | **HW Problem 2** | does `L` embed into *some* σ-complete **OMP** `L̄` (not a tribe of sets, not concrete, not state-separating)? | no (plain ZFC) |

Established relations:

- **A is strictly above B.** ⟦charted, cited⟧ The Floor (`thm:floor`): a faithful
  tribe-of-sets representation forces distributivity ⟹ Boolean. Dvurečenskij σ-LS
  (J. Austral. Math. Soc. 68, 2000): every `L` admits only a σ-*epimorphic* (lossy,
  non-faithful) tribe image, which does **not** separate the 2-valued points — the
  "tribe-vs-points gap." RDP is needed and OMLs lack it (MO₂ is the standard witness).
- **C does not entail B.** ⟦HAND, 2026-06-25⟧ HW2's `L̄` may be a non-distributive
  *abstract* σ-OMP with no tribe-of-sets structure, so it sidesteps the Floor entirely.
  (One non-implication only — **not** mutual independence.)
- **A and C are ORTHOGONAL — a TYPE MISMATCH** ⟦HAND, self-checked, advisor-pass
  pending (advisor was down at recording)⟧. **The weld run (2026-06-25) resolves the
  A↔C relation: neither cross-implication holds, for a structural reason.**
  - *C-fails ⟹ A-fails: VACUOUS.* A's carrier is **already σ-complete** (C2 is a
    standing hypothesis; the witness is "concrete σ-**complete**"). C (does an OMP
    embed into *some* σ-complete OMP?) is **trivially YES** on A's carriers — they
    are their own σ-completion. So C-failure can only occur for *non*-σ-complete
    OMPs, which A's carrier class **excludes**. The two walls do not range over the
    same lattices.
  - *A-fails ⟹ C-fails: also fails.* A-failure is a **state** defect on an
    already-σ-complete `L`; it exhibits no OMP *lacking* a σ-completion. (`L` has one
    — itself.)
  - *Adversarial self-check (advisor down):* could A-failure secretly encode a
    completion failure of the **finite** sub-OMP `⟨B⟩`? No — `⟨B⟩` is finite, hence
    trivially σ-complete and σ-embeds into `L`; the defect is in the **state**, not
    the lattice. No hidden completion question inside A.
- **∴ HW Problem 2 (C) DROPS OUT of the picture.** It is not "the bottom," not
  "above," not "below" A — it is about a *different* phenomenon (lattice completion
  of non-σ-complete OMPs) than A (state realization on σ-complete OMLs). The earlier
  "the witness reduces to HW2 / σ-LS" framing welded two genuinely orthogonal walls.

So the bottom is **A (σ-point-selection) — full stop**, strictly above B, with C
removed as a red herring. A is a **state-realization** question on a fixed
σ-complete lattice; the reduction does NOT route through any lattice-completion
problem.

## 4. What it is and is not

- **Is:** a **localization** of the σ-essential witness question to the non-Dirac
  σ-state core (clause (ii), "wall A"), with A's location relative to B and C pinned.
  The honest, recorded form of "the difficulty is load-bearing and lives in (ii)" —
  NOT an equivalence with a separate harder named problem (§1).
- **Is not a proof the cell is empty (¬Ψ).** Blecher–Weaver: the *Hilbert* analogue —
  a singular σ-additive pure state on B(ℓ²(κ))'s projection lattice — **exists ⟺ κ is
  Ulam-measurable.** So ¬Ψ is not a ZFC theorem; the analogous object exists under a
  large cardinal in the Hilbert sector. The concrete sector is the open transfer.
- **Is not an independence proof.** That would need clause (ii) turned into a clean
  independence-ready sentence (see [[forcing_programme_status]]); it is currently an
  open math problem, not an undecided sentence.

**Scoping remark (why the solved Hilbert case does not close (ii)).** ⟦remark-strength,
cited facts — NOT a theorem; the openness of (ii) is established by the literature
sweep, not by this remark.⟧ The Hilbert result lives in a genuinely different sector,
and the obvious transfer tool fails:
- **Sectors differ (Kochen–Specker).** A *concrete* σ-OML has, by definition (Gudder),
  an order-determining family of 2-valued states; `L(H)` (dim ≥ 3) has **none**
  (Kochen–Specker). So concrete σ-OMLs are not projection lattices — B–W's object and
  ours are not the same kind of structure.
- **The obvious bridge fails (Akemann–Weaver).** The natural transfer between a
  non-commutative algebra and an abelian subalgebra — masa-factoring — **fails for the
  pure 2-valued case** (Akemann–Weaver 2008: a pure state on B(H) multiplicative on no
  masa; B–W themselves use MSS paving for exactly this reason).

⟹ B–W's Hilbert dichotomy does not transfer to the concrete sector by the obvious
routes, and clause (ii) for concrete σ-OMLs is **open** (no prior art; validation
literature sweep, 2026-06-25). This is the honest scope of the "no routing port"
observation — a remark assembling two cited facts, **not** a categorical
non-reducibility theorem (which would need a fixed reduction notion à la
Borel-reducibility, out of scope and not needed: the deliverable rests on the §2
localization + the literature-established openness of (ii) + this boundary map).

## 5. A bottleneck, not a convergence — ⚠ CORRECTED 2026-06-25 (hostile audit)

**An earlier draft of this section claimed "seven independent routes converge on
wall A" and treated that as a unification. A hostile audit BROKE that claim. The
honest finding is a BOTTLENECK, not a convergence — and a bottleneck is nearly
tautological once the core is named.** The corrected count:

- **Genuine independent reductions to wall A: ≈ 1.** The §2 equivalence (witness ⟺
  σ-point-selection) is the one real reduction.
- **Routes 4 (¬Ψ-lever), 5 (Con(Ψ) construction), 6 (template no-go) are ONE
  argument, three angles** — refute / build / bound the *same* clause-(ii) object.
  The ledger says so verbatim: "#28 and #29 are ONE theorem"; "one task, three
  exits." Not three confirmations; one fact viewed three ways.
- **Route 3 (Blecher–Weaver) does NOT reduce to wall A.** It is the *Hilbert* sector
  (pure states on `B(ℓ²(κ))`, non-concrete by KS); Akemann–Weaver's "no routing
  port" means the concrete 2-valued question does not factor through it. Listing it
  as a route to A is a THIRD HW2-style weld (cf. §3) — caught here, struck.
- **Routes 1 (catuṣkoṭi) and 2 (structural-reduction) are failed dissolutions**, not
  reductions ("4 obstacles dissolved on inspection"); route 2 has no ledger record.
- **Route 7 (weld run) is a map *subtraction*** (HW2 removed as orthogonal), not a
  reduction TO A.

**So the structural finding is:** σ-point-selection (wall A) is a **load-bearing
bottleneck** — every *complete* attack on the σ-essential witness question must
engage clause (ii) of §2 — NOT a Type-3 unification of separate areas (the
"convergence" buys no method-transfer; it says distinct directions stall on the same
missing fact). The §2 reduction stands; the seven-route gloss was inflation.

**What remains true and load-bearing:** the §2 equivalence (witness ⟺
σ-point-selection); wall A strictly above B (§3, cited); HW2 (C) orthogonal (§3, the
weld run). σ-point-selection for non-distributive concrete σ-OMLs is the genuine,
located, open object — reached by one reduction, not seven.

## 6. Primary sources

- Navara & Pták, *Two-valued measures on σ-classes*, Čas. Pěst. Mat. 108 (1983)
  225–229. (Template + concentration criterion; in the library.)
- Blecher & Weaver, *Quantum measurable cardinals*, arXiv:1607.08505 (JFA 272, 2017).
  (Hilbert-side Ulam-measurable dichotomy.)
- Dvurečenskij, σ-Loomis–Sikorski for RDP structures, J. Austral. Math. Soc. 68 (2000).
- Harding & Wang, *On some problems concerning… completions*, arXiv:2108.09819,
  Problem 2 (the embedding wall C; in the library).
- Derr & Williamson, arXiv:2302.03522, Thm D.6 (Polish-representable ⟹ no gap; the
  upper bound — any witness must be non-Polish).
- Akemann & Weaver, PNAS 105(14) (2008) (pure state on no masa — no routing port).

## 6. THE SWING — the boldest *true* target (2026-06-25)

After correcting §5, the honest fence:

> **CONJECTURE.** The existence of a concrete σ-essential witness is **independent of
> ZFC** — a new ZFC-independence phenomenon in quantum logic (concrete σ-OMLs).

**Strength is CONJECTURED, not assumed.** Discipline check (so the just-struck
Blecher–Weaver weld does not walk back in through the framing):
- **¬-side has independent evidence.** "No measurable cardinal ⟹ every σ-additive
  2-valued state on a concrete σ-OML is Dirac" is a direct structural fact about the
  *concrete* object — it does NOT route through B(H). So the *refutation* direction
  genuinely touches "no measurable cardinal." This is real, in-field evidence the
  object is independence-flavored.
- **Con-side strength is NOT independently established.** "Measurable cardinal
  *suffices* to build the witness" was entirely inherited from the B–W Hilbert
  analogy — which §5 STRUCK (no routing port). So the consistency direction, and its
  exact strength, is the open construction to be EARNED, not imported. Do not state
  "measurable-cardinal strength" as a premise.

**Two halves of the swing:** (Con) build a concrete σ-essential witness under *some*
large-cardinal hypothesis — genuinely new, in-field construction; (¬) prove no
witness in L — the ¬Ψ lever exists but stalled at the σ-class-vs-σ-algebra gap.

**STOP-CONDITION (pre-committed, before swinging):** if the construction's first
concrete step does NOT survive the σ-class-vs-σ-algebra gap that already stalled the
¬Ψ run, that is the signal the move is genuinely out-of-field — the honest output is
then **"independence-conjecture-with-evidence, recorded for a set-theorist,"** NOT an
nth run. This is where hubris and discipline coexist concretely: swing hard, with a
defined miss.

## 7. THE SWING — taken, and the stop-condition FIRED (2026-06-25)

The ¬-side first step was attempted (its first step IS the pre-committed miss-test).
**Redirect logged:** mid-swing the ¬-target mutated from "¬Ψ via no-measurable-cardinal"
to "ZFC no-witness via countable-carrier collapse" (a legitimate redirect — more
decidable, not less). The sharp question reached: *does a finitely-coherent
Dirac-unrealizable s₀ exist on a COUNTABLE concrete σ-OML with no non-Dirac rescuer?*

**Attempted argument:** on a countable carrier, the tower `A_k ↓ ∅` gives orthogonal
increments in L, so σ-additivity forces `s(A_k) → 0`, killing any rescuer ⟹ ¬Ψ
provable for countably-generated L ⟹ (tempting) Paper-I gap closable in ZFC.

**WHIFF — verified against own ledger (CHARTED line 64).** The load-bearing step
"`A_k↓∅` gives orthogonal increments IN L" REQUIRES the disjointification identity
`(a∨b)∧a⊥=b∧a⊥`, which CHARTED records as a WALL: **distributive, FALSE on OMLs.** On a
non-Boolean L the tower lives across incompatible blocks; its increments need not be in
L *even when Ω is countable*. So "countable ⟹ no rescuer" is FALSE — what was actually
shown is "orthogonally-refinable ⟹ no rescuer," and refinability is the
**distributivity (Floor/RDP) axis, NOT the cardinality axis.** The fork is
refinable-vs-not, which is the σ-class-vs-σ-algebra gap — **this "new result" is the
4th costume of the same weld**, not a theorem. (Unit test confirms: ∏ₙMO₂'s gap can't
bite because it's *segregated*, not because it's countable — CHARTED 111.)

**∴ STOP-CONDITION FIRED, honestly.** The construction's first concrete step did NOT
survive the σ-class/σ-algebra gap — exactly the pre-committed miss (§6). Per the
pre-commitment, the honest output is now: **independence-conjecture-with-evidence,
recorded for a set-theorist** — NOT a 5th angle. The witness, if it exists, requires a
NON-refinable (distributivity-failing, plausibly uncountable) carrier; whether such a
carrier hosts the obstruction without a large cardinal is the genuinely open
set-theory question, out-of-field by the stated driver. **Paper-I gap NOT closable by
this route** (its carrier isn't forced refinable). The swing was real, the miss is
real, and it's called — discipline and hubris, both honored.

## 8. SWING VALIDATION — deep research (2026-06-25): redirect to the reduction-map

Two validation scouts (is-the-prize-real + framing/payoff). Verdict:

- **Q1 PRIZE REAL — genuinely open, no settling result either direction.** Concrete-vs-Hilbert gap intact; Ulam transfer conjectured not proven (no-routing-port confirmed). Not a kill.
- **Q2 RECOGNIZED — PARTIAL.** The GENRE (set-theoretic strength of state existence: Naimark/Akemann–Weaver, Blecher–Weaver, live 2026 Dzhenzher line) is flagship-valued. But THIS exact concrete-σ-OML question is stated NOWHERE — an unclaimed gap BETWEEN set-theory-of-operator-algebras (has the forcing tools, works on B(H)) and OML/quantum-logic (owns the structures, doesn't force). Opportunity (no competitor) + risk (no external pull; you motivate it).
- **⚠ OVERCLAIM CAUGHT + CORRECTED:** "independence phenomenon" is PART OF THE CONJECTURE, not established. Routing port closed ⟹ no basis to assume independent vs. plain-ZFC-decidable. Honest object = "an open, located, reduced problem whose set-theoretic CHARACTER is unknown." NEVER frame as "new independence phenomenon"; always pair Blecher–Weaver with the no-routing-port caveat.
- **Blecher–Weaver is the PURE-state analogue, not the two-valued one** (two-valued ≠ pure on B(H); 2-valued generically nonexistent by Gleason). Makes the analogy LOOSER — reinforces nothing transfers automatically. State as "pure-state precedent shows the phenomenon CAN be large-cardinal-sensitive at all," not "the OML image of B–W."

**THE REDIRECT (both scouts converge):** the reachable, in-field, publishable deliverable is the **REDUCTION-AND-BOUNDARY-MAP**, NOT the independence theorem (which bottoms out in forcing = expertise mismatch, needs a set-theorist collaborator). Package: the §2 reduction (witness ⟺ σ-point-selection) + boundary results (Polish→no-gap; no-routing-port; disjointification ⟹ non-distributive mechanism) as one clean map, written for the set-theory-of-op-algebras register (JFA/IJM/Fund.Math.), OML setup made legible. Then hand a set-theorist a sharply-posed, already-reduced problem — the no-competition gap becomes an ASSET.

**THE LOAD-BEARING TASKS — UPDATED 2026-06-25 (both resolved):**
- **(1) Make the §2 reduction AIRTIGHT — DONE.** 7/7 claims verified
  (`reduction_airtight_verification.md`); the airtight pass downgraded the headline
  from "reduces to" to **localization** (§1/§2 corrected). The core is now verified +
  honestly framed.
- **(2) "Turn no-routing-port into a theorem" — DEMOTED TO A REMARK (the 4th overclaim
  caught).** The paper does NOT need a non-reducibility theorem: "no reduction exists"
  has no theorem-shaped meaning without a fixed reduction notion (Borel-reducibility
  style), which is out of scope and unneeded. What the deliverable needs is "**clause
  (ii) is open**" — already established by the literature sweep, not by any
  no-routing-port claim. Written as the §4 **scoping remark** (KS sectors-differ +
  A–W masa-factoring-fails, both cited, remark-strength).

**∴ The in-field deliverable is essentially COMPLETE:** the §2 localization (airtight)
+ the literature-established openness of (ii) + the boundary map (§3–4: Polish→no-gap,
HW2 orthogonal, faithful-tribe below, the scoping remark). Realistic outcome = "located
+ localized an open problem," publishable as such, pending the eventual set-theorist
hand-off for the independence question itself. NOT a named independence theorem solo.
