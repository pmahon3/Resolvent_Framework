# SIGMA_LAYER_TARGET — the Stage-0 pull-document

**Created:** 2026-07-20 (E-thread unit E5, bookkeeping session). **Authorized
by:** the user-ratified steering checkpoint (§A3), executing the banked E4
pivot instruction (`CAMPAIGN_CHAIN.md`, E-thread pivot note, clauses (a)/(b)/(c))
as amended by A2 (same file, AMENDMENT A2). **Status of this document:** it is
a TARGET and GATE document, not a results document. It adds NO new mathematical
claims. Every claim below is quoted or pointed-to with the verdict grade it
already carries in its home ledger; where a grade is conditional or
unverified, that is stated inline.

**What this document is for.** Two jobs, both gating:

1. **The pull.** It names the Stage-0 clauses that σ-layer work must serve.
   Under A2, grammar-engine iterations (`MEM/N/O/PENV` batches, forced-top
   descent, `ARR-CYL`) run ONLY when the session names the clause below it
   serves AND declares a per-session iteration budget up front.
2. **The spine.** It records the organizing goal (the Isolation Program, §2),
   the three workstreams (§3), the two Φ-primary campaigns (§4), and the
   external wall (§5), so that a later session inherits the frame and not just
   the backlog.

Standing gates that govern every session reading this file are in §6. Read §6
before running anything.

---

## 1. The three Stage-0 clauses

These are clauses (a)/(b)/(c) of the banked pivot, absorbed here as instructed.

### Clause (a) — the non-extendability necessary condition

**Statement (as banked, E1/E2, corpus-level necessary condition).** A
σ-essential witness is **non-extendable**: value-1 FIP fails at a finite stage
≥ 3. Fired on the Ψ-witness at **stage exactly 3** (E2b locator: A={1,2},
B={1,3}, C={2,3} → pairwise intersections singletons, triple intersection
empty).

**Grade.** Proved; survives the chain-level hostile audit (finding 6(1),
`CHAIN_HOSTILE_AUDIT_2026-07-20.md`). Lean-pinned on the witness: the
FIP-fails-at-stage-exactly-3 row is certified choice-free
(`UlamWitnessCore §7`). E1's proof-read was genuinely hostile — it CAUGHT and
downgraded the "exactly C11 Lemma C2" claim to "set-intersection shadow"
(partial match), and that downgrade stands.

**Reverse-math baseline — the BPI-exact calibration (state this whenever the
clause is used).** The underlying lemma is **BPI-exact**: the (3⟹2) direction
uses exactly the ultrafilter lemma, and the choice principle is flagged
honestly everywhere it appears (E1: "BPI-only exact"). This calibration is
part of the clause, not a footnote to it — a session invoking clause (a) must
carry the BPI-exactness with it, because it is what makes the condition a
*sharp* necessary condition rather than a ZFC-strength convenience.

**What serving this clause looks like.** Work that sharpens, generalizes, or
tests the stage-≥3 FIP failure — e.g. whether the finite stage can be bounded
above on a given carrier class, or whether non-extendability at stage 3
interacts with latticehood. Grammar-engine batches qualify only if the session
states which of these they test.

### Clause (b) — the second-inclusion localization

**Statement (as banked, E4 seed verdict = ABSORB-with-localization).** No
confirmed σ-complete **lattice** non-extendable carrier exists in the located
literature ⇒ **the third engine must act at the SECOND inclusion** (σ-states
catching non-extendable finitely additive states) — exactly the coarse factor
Campaigns 11/13 already flagged as the hard one.

**Grade — read this carefully before building on it.** The localization is
honestly labelled a **frontier-narrowing, NOT progress toward proving Φ**
(hostile audit finding 6(3)), and it is **CONTINGENT on an unverified,
paywalled lead**: it holds exactly when the screen turns up no lattice
σ-complete non-extendable carrier. The screen's one live lead, **DNP 2015**
(Math. Nachr. 288, 1995–2000), is **UNVERIFIED** — primary text paywalled
(Wiley HTTP 402), no preprint; its construction is claimed σ-complete, but
**whether it is a LATTICE is exactly the unknown**. Per the repo's
hostile-prior-art discipline, UNVERIFIED ≠ confirmed lattice candidate, and
the paywall must not become a guess in either direction. Promote-on-
confirmation: if DNP 2015's σ-complete construction IS a lattice with a
non-extendable state, re-audit → promote-to-seed. (The ILL request is
user-bound, low-priority, expected-negative.)

Supporting circumstantial pattern from the ACCESSIBLE neighbours (NOT a proof
about DNP 2015's object): difference-closed set systems are generically
orthomodular POSETS, not lattices — latticehood is an *extra* hypothesis; and
every *lattice* non-extendable example located in print is **FINITE** (MO₄;
the 32-element Ex 2.6 of arXiv:2401.13651), hence σ-tame, hence never a
σ-essential witness. This matches the Ψ-witness's own status (σ-complete OM
poset, not a lattice) and the DW wall.

**What serves this clause.** `ARR-CYL` is retained specifically here: it is the
live second-inclusion frontier question (A2 re-scoping). Any session running
`ARR-CYL` cites this clause and declares its budget.

### Clause (c) — W-P: HEURISTIC ONLY

**W-P (the perspectivity direction) is recorded here as a HEURISTIC and
NOTHING ELSE.** It is **never** a constraint and **never** a rejection
criterion. Explicitly: **a later session must never reject a witness candidate
for "perspectivity poverty."** If you find yourself using W-P to rule a
candidate out, you have misused this clause — stop and re-read this paragraph.

Status: parked on **rung 1, NOT cleared**; everything downstream in the W-P
note is conditional on rung 1. The perspectivity/twist route itself is CLOSED
— rung 1 killed the mechanism (ledger row; and see §6). The heuristic content
worth keeping is the shape it suggested: a witness would be a never-closing
infinitely-continued thread — coherent at every countable stage, closed at no
stage — the Hausdorff-gap shape. That is an intuition to think with, not a
test to apply.

Sources: `PERSPECTIVITY_WALL_CANDIDATE_2026-07-19.md`,
`W_P_FEASIBILITY_LADDER_2026-07-19.md`.

---

## 2. The organizing goal — the Isolation Program

The programme's summit is the **ISOLATION THEOREM**: compress the central
question to a named set-theoretic statement **S** with a proved equivalence
**Φ ⟺ S** (or the honest one-sided versions), in the genre of Shelah/Whitehead
and Mardešić–Prasolov/derived-limits.

Three governing facts:

- **The isolation is the THEOREM TO PROVE, not a preliminary.** Absorbing the
  lattice/measure content into the equivalence IS the work. A reduction that
  leaves the measure content outside S has not isolated anything.
- **The lim¹ / derived-limit identification (from the σ-nerve seed) is the
  TARGET, not an established premise.** Never cite it as settled. (The σ-nerve
  seed itself was PARKED/ABSORBED 2026-07-18 at Phase-2 audit REVISE; its
  keeper is the index-category fence on closure-based CODBC, in
  `oml_odbc_sigma_nerve_absorption.md` — ⚠ that file lives on the **unmerged**
  `explore/c-sigma-nerve` branch, NOT on this one; the worktree merge is
  pending the user. A W1/W2 session needing it must check out that branch.)
- **The known obstacles are three, and they are exactly the workstreams of §3.**

---

## 3. The three workstreams

### W1 — Index category determination (FIRST, sharpest)

**Task.** Determine the cofinal structure of the section-system index poset
for the two escape architectures (§4): is it **[ω₁]^≤ω-like**, **ω₁-tower-like**,
or **ω^ω-like**?

**Why first.** This decides WHICH set theory the residue belongs to:
ZFC-robust tower phenomena vs axiom-sensitive ω^ω phenomena. These are
different worlds and conflating them is a recorded error — an earlier
chat-level conflation of the two is on record and **corrected**; do not repeat
it.

**Deliverable.** Precise statement + proof of the index structure, banked with
a verdict grade, hostile-passed before banking.

### W2 — Coefficient normalization (SECOND, executable-adjacent)

**Task.** Run the σ-nerve seed's Theorem-A typing on (i) the counterexample
ledger and (ii) the two escape architectures. Do the convex σ-state fibres
normalize to torsor/group-valued form, where derived-limit machinery applies,
or does the expected third type appear?

**Discipline.** Report the ACTUAL coefficient structure. **Do not assume ℤ/2.**
A large "neither" mass is a **finding, not a failure** — bank it as such.

### W3 — Measure knot (PARKED, trigger unchanged)

**The obstacle.** S must eventually carry the **state**, not just the twist. A
twist-only reduction is not the isolation.

**Status.** PARKED behind its existing trigger: *a lattice-closed survivor at
finite scale*. Recorded here as the third obstacle precisely so that no future
session mistakes a twist-only reduction for the full isolation.

---

## 4. The Φ-primary campaigns

**Framing (A1, ratified).** Proving Φ is PRIMARY. The two targets are the two
escapes left open by the Campaign-11 puncture-meet theorem, which is correctly
scoped to kill only the countably-generated SEPARATING shared boundary:

- **escape (a):** the uncountably-generated separating boundary;
- **escape (b):** the distributed nonseparating quotients.

These are simultaneously the last witness-hunt targets and exactly what a
Φ-proof must close — same frontier, inverted priority.

**⚠ Do not oversell.** The hostile audit flags this pivot explicitly: "generalize
C11 to prove Φ" has a large **self-flagged gap** — the uncountable case is
exactly C12's central ω₁ cylinder, which C11 does **NOT** exclude.

### C-a (main push) — countable-meet generalization → escape (a)

Does the C11 obstruction extend to every faithful, order-separating,
countably-generated hub shared between two blocks of any concrete σ-complete
OML? (This is route (a) of `PSIOML_ROUTES_HANDOFF_2026-07-20.md` and
`conj:route-a` of the exposition — the campaign and the PsiOML route are the
same target.)

**Pre-registered exits.**
- Proof ⇒ escape (a) closed; major Φ progress.
- Failure ⇒ the failing hub class is a **named witness design constraint**,
  feeding W1/W2. (This is the conversion discipline, not a consolation prize.)

Slot on the chain per convention (next campaign number or E-unit — the opening
session verifies and slots it).

### C-b — distributed nonseparating quotients → escape (b)

Queued behind C-a **unless** W1's answer makes it the cheaper target; a session
may reorder with **one line of justification** recorded on the chain. (= route
(b) of the PsiOML handoff / `conj:route-b`.)

### The witness-side falsifier: `PsiOML`

The standing falsification channel is the Lean-pinned statement **`PsiOML`**
(`UlamWitnessLatticeGap.lean:144`):

```lean
def PsiOML : Prop :=
  ∃ (Ω : Type) (d : DynkinSystem Ω) (B : Block d) (s₀ : LocalState d B),
    MeetsExist d ∧ IsSigmaEssentialL s₀
```

`PsiOML → Ψ` is proved; **`Ψ → PsiOML` is open**. The proved ZFC witness `L₁`
is an OMP, machine-proved NOT a lattice (`witness_carrier_not_lattice`,
choice-free reduction + one cited axiom `slab0_not_mem`). **ALL witness
attempts route through `PsiOML`** — it is now the cleanest formal statement of
what a witness must supply. Cite the **FIP-fails-at-stage-exactly-3** Lean row
(`UlamWitnessCore §7`) as the certified calibration.

The ω₁ witness brief is RETAINED as the standing falsifier under A1.

---

## 5. External wall — the EPV locus constraint

**Escolano–Peralta–Villena**, *A Mackey–Gleason–Bunce–Wright theorem for
JBW\*-algebras*, **arXiv:2509.03213** (3 Sep 2025; full 65pp PDF read, receipt
`EPV_2025_PRIMARY_SOURCE_RECEIPT_2026-07-19.md`).

**Thm 6.1/6.2:** for a JBW\*-algebra J with **no type I₂ direct summand**,
every bounded finitely additive measure on P(J) extends to a bounded linear
functional. **The dual is in the primary text (pp. 62–63, not the abstract):**
for **every** type I₂ JBW\*-algebra there exists a positive finitely additive
measure on P(J) admitting **no** such extension. So the no-I₂ hypothesis is
**SHARP** — extension holds off I₂, fails on every I₂ summand. Both
load-bearing claims CONFIRMED against the body.

**The constraint this imposes on the witness locus.** The bounded-finitely-
additive route is closed off I₂: a witness must live where the EPV theorem
does not apply — **I₂-rich and symmetry-poor**. Record the mechanism caveat
from the receipt §4: EPV's Prop 3.5 gets uniform continuity from **projection
halving + isoclinic decomposition**, i.e. an abundance-of-symmetry mechanism.
That mechanism is **distinct from the σ-stage** at which this programme's
question lives. So EPV is a genuine external wall on the finitely-additive
layer, and it constrains WHERE to look — it is **not** a σ-layer theorem and
must not be cited as one.

---

## 6. Standing gates (read before running anything)

- **Do NOT re-open the perspectivity/twist route.** Rung-1 refutation; ledger
  row. Closed.
- **W-P is heuristic-only; NEVER a rejection criterion** (clause (c)).
- **The lim¹ identification is a TARGET, never a premise** (§2).
- **Grammar-engine hard gate (A2):** name the Stage-0 clause served + declare
  the per-session iteration budget up front, or the engine does not run.
  `ARR-CYL` is retained under clause (b) only.
- **Conversion discipline (A1), both directions:** every failed proof-step
  converts to a named witness design constraint; every failed construction
  converts to a named tameness mechanism. Bank the conversion, not just the
  failure.
- **Ledger edits are additive-plus-supersede** (strike-and-note; delete
  nothing). Verdict grades on everything. **Hostile pass before banking any
  W1/W2 verdict.**
- **Never push.** The user pushes.
- **Not Claude Code's tasks** (human-side, tracked elsewhere): the two reading
  programmes (σ-pasting/realization; ω₁/Maharam), the outreach letter, the DNP
  2015 ILL (low-priority, expected-negative).

---

## 7. Pointers

| What | Where |
|---|---|
| Authoritative ledger + A2 amendment | `CAMPAIGN_CHAIN.md` |
| Chain-level hostile audit (source of the inversion) | `CHAIN_HOSTILE_AUDIT_2026-07-20.md` |
| Compact mathematical state index | `CURRENT_STATE.md` |
| E4 verdict (clauses (a)/(b) origin) | `linearization_E4_verdict.md` |
| PsiOML routes (a)/(b) — the C-a/C-b hand-work handoff | `PSIOML_ROUTES_HANDOFF_2026-07-20.md` |
| Route (a) scope | `ROUTE_A_SCOPE_CLARIFICATION_2026-07-20.md` |
| EPV primary-source receipt | `EPV_2025_PRIMARY_SOURCE_RECEIPT_2026-07-19.md` |
| W-P (heuristic only) | `PERSPECTIVITY_WALL_CANDIDATE_2026-07-19.md`, `W_P_FEASIBILITY_LADDER_2026-07-19.md` |
| Lean pins (`PsiOML`, lattice gap) | `formalization/QuerySystem/.../UlamWitnessLatticeGap.lean`, `UlamWitnessCore` §7 |
| Jargon-free exposition (read-mostly) | `notes/exposition/problem_state.tex` |
