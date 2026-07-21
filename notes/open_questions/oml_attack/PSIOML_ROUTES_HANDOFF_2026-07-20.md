# PsiOML routes (a) then (b) — handoff, 2026-07-20

**Order: attack route (a) first, then route (b).** This file is the
self-contained starting point for that work; it does not assume the
reader has the conversation that produced it.

## What PsiOML is

`PsiOML : Prop` (`UlamWitnessLatticeGap.lean:144`) — named, never assumed:

```lean
def PsiOML : Prop :=
  ∃ (Ω : Type) (d : DynkinSystem Ω) (B : Block d) (s₀ : LocalState d B),
    MeetsExist d ∧ IsSigmaEssentialL s₀
```

Does a σ-essential witness exist on a carrier that IS a lattice (not just
an orthomodular poset)? The proved ZFC witness `L₁` (`psiAmended_ZFC`) is
an OMP, machine-proved NOT a lattice (`witness_carrier_not_lattice`,
`UlamWitnessLatticeGap.lean:132`). PsiOML is the surviving open question.
Working conjecture: **PsiOML is FALSE** — every concrete σ-complete OML
satisfies Φ (σ-additive lifting), so latticehood forces liftability. This
is `Conjecture~\ref{conj:main}` in `notes/exposition/problem_state.tex`
§7 (exposition, read-only file — do not edit it from this thread).

## The two routes, precisely

**Route (a) — generalized countable-meet obstruction**
(`Conjecture~\ref{conj:route-a}`, exposition §8):
Does the two-cell countable-meet mechanism that kills `L₁`'s latticehood
(a specific meet forced not to exist at a *countably-generated* shared
boundary between two blocks) generalize to forbid **every** faithful,
order-separating, countably-generated hub shared between two blocks of
*any* concrete σ-complete OML? If proved: eliminates every
countably-generated-boundary witness construction at once. If it fails:
the surviving counterexample is a concrete design template for a witness
attempt.

**Route (b) — distributed nonseparating quotient**
(`Conjecture~\ref{conj:route-b}`, exposition §8):
Route (a) only reaches countably-generated hubs. Is there a concrete
σ-complete OML built from **uncountably**-generated boundary data whose
σ-states do NOT order-separate points globally — by distributing
nonseparating quotient copies — so that no global σ-state assembles,
while every finite/countable sub-piece stays locally consistent? If
constructible as a genuine lattice: refutes the conjecture outright
(PsiOML becomes true). If provably impossible: the complementary half of
a full impossibility proof, alongside (a).

Together (a) + (b) are meant to be exhaustive: (a) kills the
countably-generated case, (b) kills-or-realizes the uncountably-generated
nonseparating case that (a) cannot reach.

## Literature groundwork already done (2026-07-20) — do not re-scout

A literature-scout pass plus independent primary-source reading (not just
abstracts — this matters, see lesson below) covered five key papers.
**No direct hit on either route.** Findings, each verified by reading the
actual proof:

1. **De Simone–Navara–Ptak 2007** (arXiv:math-ph/0311012) — purely finite
   concrete logics, no σ-additivity. No bearing on either route.

2. **Tkadlec 2007, "Effect algebras with the maximality property"**
   (arXiv:0712.3717) — Theorem 3.7: Jauch–Piron + **countable** unital
   state set ⟹ orthomodular LATTICE. Example 3.8: a countable,
   *separating* non-lattice OMP exists (opposite of what route (b)
   wants — route (b) needs uncountable + non-separating).

3. **Navara–Ptak–Rogalewicz 1988, "Enlargements of Quantum Logics"**
   (Pacific J. Math. 135, free at
   `https://msp.org/pjm/1988/135-2/pjm-v135-n2-p10-p.pdf`) — Theorem 2.3:
   total freedom to realize ANY compact convex set as the state space of
   an OML with prescribed centre, via pasting. **CAUTION (this was a
   live error mid-session, corrected by advisor):** their "state" is only
   *finitely* additive and the construction is not σ-complete (finite
   range functions). This result does NOT cut against route (a) — it
   lives entirely outside the σ-additive/σ-complete regime route (a) is
   about. It sharpens the real question instead: does this
   finite-additivity realization freedom survive passage to σ-complete
   OMLs with σ-additive states? If it collapses under σ-completion, that
   collapse mechanism IS route (a)'s obstruction.

4. **Tkadlec–Svozil 1996, "Greechie diagrams, nonexistence of measures..."**
   (J. Math. Phys. 37, free at
   `https://math.fel.cvut.cz/en/people/tkadlec/papers/svtk.pdf`) —
   Greechie-diagram machinery, finite realizability in H₃. No
   σ-additivity, no infinite/uncountable regime. Confirms this whole
   corpus is finite-focused.

5. **Navara–Rogalewicz 1991, "The Pasting Constructions for Orthomodular
   Posets"** (Math. Nachr. 154 — the hardest to get; ResearchGate
   bot-blocks automated fetch, obtained via user's own browser/library
   access, now in `notes/literature_review/literature/` — check there
   first before re-fetching). **Most relevant of the five, but still not
   a hit.** Whole paper is algebraic/structural (completeness,
   latticehood, automorphisms) — contains NO σ-additive-state theorems.
   Two results matter:
   - **Theorem 4.11**: a σ-orthocomplete limit of a sequence of OMLs is
     itself an OML.
   - **Proposition 4.2(iii)**: m-orthocompleteness is preserved by
     pasting under mild conditions (common bound on pairwise
     intersections).
   - **Example 4.8**: two Boolean algebras pasted along a shared
     finite/cofinite intersection produce a non-lattice OMP (no join
     for `X₁∪X₂`, `X₁∪X₃`) — a concrete template for a no-join hub,
     though only two pieces, finite boundary, no states discussed.
   - **Upshot for route (b):** the algebraic scaffolding to build an
     uncountably-generated, σ-complete concrete OML by pasting/limits is
     already available from 1991-vintage tools. Route (b)'s entire
     remaining difficulty is on the STATE side — arranging that no
     global σ-additive state assembles — not the structural side.

6. **Müller 1993, "Jauch–Piron States on Concrete Quantum Logics"**
   (IJTP 32, in `notes/literature_review/literature/muller_1993_jauch_piron.pdf`)
   — closest cousin found, NOT a hit. Builds a non-Boolean concrete
   logic (`|X|=ℵ₁`) where every *finitely additive* state is Jauch–Piron.
   But his own Theorem 2 proves: for COMPLETE concrete logics (closed
   under arbitrary disjoint unions, a stronger hypothesis than
   σ-completeness), all-states-Jauch–Piron ⟺ complete Boolean algebra —
   and his own witness, once σ-completed, is Boolean by a cited result
   (Müller–Ptak–Tkadlec 1993, on logics with the same "intersection
   property" his construction uses). The GENERAL claim (any σ-logic with
   all-finitely-additive-states-JP is Boolean) he states only as HIS OWN
   CONJECTURE, not a theorem — and he explicitly calls the
   σ-logic/finitely-additive regime "unnatural." Jauch–Piron is a
   different property from PsiOML's σ-additive-extension question, and
   his positive results need a stronger completeness hypothesis than
   PsiOML needs. Not a resolution — but positioning-relevant: the
   nearest author in this literature named exactly this neighborhood
   (σ-complete carrier, finitely-additive states failing to lift
   σ-additively) "unnatural" and moved on. Nobody has gone there; the
   silence isn't a settled negative.

**Overall verdict:** conjecture (PsiOML false) is unrefuted and mildly
supported by everything found. Neither route is closed or opened by
prior art. Proceed to hand-work.

## Session lesson (apply going forward)

Mid-session, reading only an abstract/theorem-statement summary of the
1988 paper led to a wrong claim ("cuts against route (a)") that got
corrected only because of a second, closer read against the primary
source. **Read the actual proof/definitions, not just the theorem
statement, before drawing a conclusion that a paper settles or bears on
either route** — this is the same standing lesson as
`feedback_verify_by_building` / the σ-essential prior-art 4×-oscillation
history. Don't re-derive the literature pass above; do apply this
standard to anything NEW cited while working the routes.

## Where things stand / what's next

- Both routes are genuinely open, hand-work required (Phase 4 —
  mathematical architecture is the user's, not the LLM's, per
  `CLAUDE.md`).
- Start with **route (a)**. The sharpened form to attack, per finding 3
  above: characterize what σ-completeness costs the 1988 realization
  freedom — if finite-additivity-realization collapses under
  σ-completion, that collapse mechanism is the obstruction route (a)
  wants.
- Then **route (b)**, using Navara–Rogalewicz 1991 Thm 4.11 + Prop
  4.2(iii) as the algebraic scaffold (build via σ-orthocomplete
  limit/pasting) and Example 4.8 as the no-join hub template — the open
  content is entirely on the state-non-assembly side.
- Formalize in Lean only once a route yields a genuinely novel result
  (per `CLAUDE.md`: "Don't formalize known results; use axiom with
  citation").
