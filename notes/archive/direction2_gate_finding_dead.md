> ⚑ ARCHIVED 2026-06-25 (σ-essential thread cleanup). Superseded by `sigma_essential_reduction_writeup.md` (the point-free fork resolved via Reading 1). Kept for the reasoning trail; not current.

# Direction 2 gate finding — "point-free" has no stable referent, and it bottoms out at the (a)/(b) fork

*Finding note, 2026-06-11. Records what came out of pursuing §6 Direction 2 of
`oml_onboarding` ("settle the (A)/(B) status of L(H)+Gleason"). It is NOT a
resolution: the gate did not produce a verdict on Gleason. It produced a sharper
finding about the open problem itself, and then deposited the programme back at
the unresolved (a)/(b) fork (`programme/genealogy.md` §"THE OPEN QUESTION"). The
philosophy is left open, deliberately — no rush, per the genealogy.*

## What Direction 2 was supposed to do

Direction 2 is the *gate* among the three §6 directions: decide whether
L(H)+Gleason counts as a genuine point-free non-distributive σ-additive witness,
or is disqualified by the (A)/(B) point-space equivocation (Rmk 5.2). It looked
cheap and conceptual, and it gates the other two (if Gleason counts, Direction 1
is half-done; if it's disqualified, the prize is vacant and Direction 3 gets a
target).

Two sub-questions were on the table:
1. **Does Gleason count?** — already settled NO by the committed predicate
   (commit `dd561c3`): "point-free" was made to negate both point-spaces, and the
   (A)-prong forbids "recovered as s=tr(ρ·) from a ray/density datum," which *is*
   Gleason. So Gleason fails by construction.
2. **Is that (A)-prong principled or gerrymandered?** — i.e. can "relational /
   point-free" be characterized *without* naming Gleason, such that Gleason then
   fails for a structural reason? This was the live question.

## What we actually found — the vise

Testing candidate Gleason-free predicates for "point-free / relational":

| candidate predicate | Gleason on L(H) | ∏ₙMO₂ (segregated junk) | discriminates? |
|---|---|---|---|
| **P₁** — measure built from the lattice alone | passes | passes | ❌ vacuous — ρ is *derived* by Gleason's theorem, not an input |
| **P₂** — no Boolean / measurable pullback (μ = ν∘φ) | passes | passes | ❌ vacuous — failing it is just `∨≠∪`, i.e. non-classicality, which both have |
| **P_int** — not a barycentric integral / fractional average over any auxiliary point space | **fails** (averages over rays) | **fails** (averages over P(A)) | ⚠️ excludes *both* |

(Computations: Gleason's `μ(P)=Σλₙ⟨eₙ|P|eₙ⟩` is an integral of a *fractional*
function, not a set-pullback; and as ray-sets `range(P∨Q) ⊋ range(P)∪range(Q)`,
so no classical measure pulls back — but that `∨≠∪` failure is generic
non-classicality, not the relational property. ∏ₙMO₂ fails P_int identically: its
states are convex averages over its coordinate points P(A).)

**The vise.** Every formalization of "point-free / relational" is either:
- **too weak** (P₁, P₂): passes everything non-classical, so it only restates
  "non-distributive," which we already had — it does *not* isolate "relational"; or
- **fork-dependent and possibly too strong** (P_int): the one predicate that
  excludes Gleason for a stated, Gleason-free reason *also* excludes ∏ₙMO₂. It is
  tempting to read this as "P_int excludes every concrete OML" (concreteness =
  order-determining points, and a measure on a point-ful lattice averages over
  them) — **but that universal is UNPROVEN, and likely false.** It holds for MO₂
  and its products, where the extreme states are 2-valued; in general the extreme
  states of a concrete OML need not be 2-valued (on L(H) there are none at all, yet
  Gleason's states span via the rays). So P_int ∧ concrete is *not* known to be
  contradictory — and the gap is exactly where a witness could live.

The tension, stated without the false universal: "point-free" pushes toward
**point-poor** (no points to average over); "concrete" gives **point-rich**. The
open problem asks for an object that is
both.

## The deeper diagnosis — the recurring (A)/(B) equivocation

This is the **fourth** time a "point-free" formalization over- or under-shot this
session (the well-posedness referee's Test-1 artifact; the false "no non-Boolean
OML has homomorphisms" universal; the P₂-vs-integral-representation slip that
briefly looked like it contradicted Rmk 5.2; and now P_int). The recurrence is
not carelessness — it is the well-posedness referee's *deep* finding being
correct: **"point-free / relational" is not yet a defined predicate.** It slides
because it is doing two incompatible jobs:

- **(B)-job:** "the measure does not concentrate on the dual points P(A)." But
  concreteness *guarantees* enough points to determine the order, so a concrete
  lattice cannot satisfy this.
- **(A)-job:** "the measure is not an average over some auxiliary point space."
  But any measure with an integral representation (Gleason on rays; every state on
  a concrete OML on P(A)) fails this.

So the actual content of Direction 2 may be **not "does the witness exist" but
"is the witness-concept coherent."**

## Where it bottoms out — the (a)/(b) fork, technical form

"Point-free" was the technical proxy for "relational," and the vise is what
happens when the proxy is pinned down: *relational* and *point-free* come apart,
and which one the programme wants is exactly the (a)/(b) fork
(`programme/genealogy.md`), now in technical clothes:

- **Reading 1 — relational = no hidden *realization* space (anti-smuggling, (a)).**
  The enemy is the **(A)-points** (Gleason's hidden ray-space). The canonical MB
  dual **(B) = P(A)** is *fine* — it is built from the lattice, not presupposed.
  Correct predicate: "no (A)-realization" (measure not recovered from an
  auxiliary, non-canonical point space). This **excludes Gleason** (needs rays)
  and **keeps ∏ₙMO₂** (its P(A) is canonical). The vise *dissolves* — we stop
  demanding point-poverty, only no-smuggled-points. **Cost:** ∏ₙMO₂ is back in,
  so "relational" alone does not capture the prize; you still need
  *non-segregation* to exclude the junk, and that is still undefined. Problem stays
  alive, re-centered on defining non-segregation.

- **Reading 2 — relational = genuinely point-free (strict localic, (b)).**
  No points at all; the measure lives on the frame. Concreteness is the enemy and
  the prize is near-empty → **impossibility branch (Direction 3).**

These are the (a)-curiosity and the (b)-curiosity wearing different clothes.
Direction 2 turned the genealogy's open fork into a *technical* fork with
concrete consequences: **Reading 1 keeps the problem alive (re-centered on
non-segregation); Reading 2 pushes toward impossibility.**

## Status / what is and isn't decided

- **Established (fork-independent):** "point-free" has no stable referent; every
  formalization is vacuous or eats concreteness; the prize-concept is internally
  strained. This is a real result about the *shape* of the question.
- **NOT decided:** which reading the programme wants. This is the (a)/(b) fork,
  left open by the genealogy as "genuinely yours to settle," and forcing it now —
  under the momentum of a long session — is exactly what the genealogy warned
  against. It has been open a month; it stays open.
- **Routing, conditional on the fork (for when it is taken up):**
  - Reading 1 → next task is **define "non-segregation"** as a predicate (the junk
    ∏ₙMO₂ must fail it, a real witness must pass); then Direction 1.
  - Reading 2 → next task is **Direction 3** (impossibility via the concreteness/
    point-fullness tension; subadditivity boundary, Pták–Pulmannová).
- **Gleason:** correctly *out* under both readings (it needs the (A)-rays). So the
  uniqueness sub-question (2b) is moot — nothing for it to be unique among on L(H),
  since every L(H) measure has the ρ-form. The committed Rmk 5.2 stands; the
  P₂-slip that briefly seemed to contradict it was an equivocation, now resolved.

## Pointers

- Survey + the three directions: `oml_onboarding.tex` §5–§6.
- The fork this bottoms out at: `programme/genealogy.md` §"THE OPEN QUESTION".
- Live OML branch (Direction 2 was its "move 1"): the (b)-descent scout
  (`fork_scout_b_descent_impossibility.md`, since SUPERSEDED by the Reading-1
  contextuality reduction, commit 18ce527 — file removed) — this finding sharpened
  that scout's framing (the scout said "fix the question"; this is *why* the question
  resists fixing). The live successor is the σ-essential descent thread
  (`MAP_sigma_essential.md`, `CHARTED_sigma_essential.md`).
- Related memories: [[oml_descent_inhabitation]], [[oml_two_point_spaces]]
  (the (A)/(B) point-space distinction, which this finding shows is the crux).
