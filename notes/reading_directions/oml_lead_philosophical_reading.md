# Reading directions — the OML lead's philosophical scaffold

*Written 2026-06-18. A focused, durable reading path for the ONE remaining open
problem (OML σ-essential descent), oriented around the big-picture question it
sits inside — not the whole programme scaffold (for that, see
`notes/unsorted/foundations/coherence_completion/philosophy_lit_review.md`, which is
explicitly "scaffolding to be cast away"). This note is orientation, not
load-bearing argument: the mathematics carries the work; the philosophy phrases the
question.*

---

## The question this lead is about (machinery stripped out)

> **Can you form a coherent *world* — an open horizon — when the logic is
> non-distributive?**

An *open horizon* (Merleau-Ponty): a world that is locally coherent everywhere but
never finitely completed — coherent in the small, open in the whole. Its openness
is **structural, not a defect.**

*Distributivity* is the algebraic name for "the parts assemble into one hidden
whole" (`a ∧ (b∨c) = (a∧b) ∨ (a∧c)`: asking-then-combining = combining-then-asking,
same world either way). *Non-distributivity* is the failure of that guarantee — the
order of asking changes what is there; there is **no hidden whole beneath the
relations.** Operationally this is incompatibility (observations that can't be
jointly made); logically it is non-distributivity; they are the same fact seen from
two sides.

So the lead's question is the collision of two commitments the programme already
holds:

- **Phenomenology (Merleau-Ponty / Cassirer):** objecthood *is* relational openness;
  there is no substance behind the relations.
- **Quantum logic (Putnam / Stairs / Bub–Pitowsky):** non-distributivity is exactly
  the regime where the hidden value-definite realization provably cannot exist.

Both traditions agree the non-distributive world has **no hidden whole**. The open
question is whether what remains — relational, open — can still be a *coherent
probabilistic world*, or whether removing the hidden whole also removes the
coherence. **The lead lives precisely where phenomenology's "open horizon" meets
quantum logic's "no value-definiteness."**

### Openness, made precise (the f.a.-vs-σ framing) ⟦2026-06-19⟧

Trying to formalize "openness" and "coherence" abstractly (as properties of a
closure operator on an OML) and assume them jointly with non-distributivity yields a
sharp diagnostic, *not* a new theorem: **openness is not an order-theoretic or
convex-geometric property — it is a σ-additivity property.** Concretely:

> **Openness = the gap between the *finitely-additive completion* of the classical
> core (which always exists — Stone duality, "the first arrow is free") and the
> *σ-completion* (which may not carry a coherent world). Non-distributivity is what
> forbids collapsing the two via a faithful representation** (faithful set-rep ⟹
> distributive image ⟹ Boolean — the universal floor).

Why this matters for reading: the coarse abstraction (convexity/order only) is
*provably too coarse* — at that level local coherence + compactness always yields a
global classical mixture (`closed-conv(D)` is compact, inverse limit nonempty), so
openness can be neither forced nor forbidden. Openness only becomes *stateable* at
the σ-level, where `S_df^σ` is non-compact. And at the σ-level, "are openness +
coherence + non-distributivity jointly consistent?" *is* the open problem verbatim
(consistent = a witness exists = Exit A; inconsistent = Exit B) — there is no
altitude where the difficulty evaporates. **The convergence is the signal:** four
independent framings now land on the same wall — (1) the σ-additivity *tetralemma*
(assume/negate/both/neither each self-destruct), (2) *Loomis–Sikorski* (faithful ⟹
Boolean, so the measure-carrying σ-duality is the open piece), (3) *openness/
coherence* (the f.a.-vs-σ gap), and (4) the *topos/Bohrification* read (2026-06-19):
the one machinery giving a point-free σ-additive valuation on a quantum logic
confines its σ-additivity to a *distributive* object / per-context Boolean blocks
(HLS Def 6.17(a); Döring via daseinisation, which Wolters proves can't be a
homomorphism) — the topos analogue of faithful ⟹ Boolean. All land on **one wall:
the absence of a σ-measure that crosses a genuine non-distributive join — a
σ-Loomis–Sikorski for non-distributive lattices.** That is strong grip on *why* the
problem is hard and *where* the single hard thing lives; it is not a way through (the
topos route *sidesteps* the wall by design — internally distributive spectrum — it
does not prove impossibility). The one thing that would be progress is a tool for the
f.a.-vs-σ gap on non-distributive lattices (route-(iii)); known machinery is now
exhausted as a *crack*.

## Where it sits relative to what's done

CE / Paper I answered the *same* question in the **Boolean (classical)** world:
finite coherence does not force σ-additivity; the open horizon there is *real and
irreducible* (the ultrafilter charge inhabits it; proved, Lean-verified). The OML
lead is **CE's reflection across the distributivity line** — the identical question
(what does coherent observation force / where must you commit / does the open
horizon survive) asked in the **non-Boolean** world. Paper II already identified
distributivity as *the* dividing line between the two worlds. So the lead is the one
place the programme's central claim (objecthood = open horizon) is still genuinely
undecided, sitting on the far side of the exact line Paper II drew.

Current lean (evidence-direction, NOT a verdict): every construction collapses
because non-distributive σ-closure over-fires back to Boolean — so the open horizon
may be a *Boolean privilege*, fragile under non-distributivity. Either answer is a
real result: a witness → the thesis recurs in a new world; a clean impossibility →
the open-horizon mode of being has a sharp boundary, and the boundary is
distributivity. Hold it as an *open question about a passage*, not an object that
exists/doesn't (see Discipline below).

---

## The reading path (by role in the argument, not by author)

### Tier 0 — the two anchors (re-read first)
- **van Fraassen, *The Scientific Image* (1980)** [`vanFraassen1980`]. Constructive
  empiricism = the EA/PR/VDR stance operationalized in Paper II. Re-read for: why
  "mark the distinctions, serve all three" is the faithful posture; the descent
  question is "is there a realist completion?", not "what's true behind the data."
- **Merleau-Ponty, *Phenomenology of Perception*** — selected passages on **horizon**
  and object-perception (on-ramp: https://philopedia.org/works/phenomenology-of-perception/).
  Re-read for: object as "the horizon's stable way of opening"; coherence of
  perspectives with no pre-given whole beneath. Source of the "coherent world in an
  open horizon" framing.

### Tier 1 — object as relation, not hidden substance (the non-distributivity payload)
- **Cassirer, *Substance and Function*** — the strongest scaffold (lit-review §2).
  Substance-concept vs function-concept = the distributive (whole-behind-the-parts)
  vs non-distributive (relational, no hidden whole) distinction. The cleanest
  articulation of *what fails* when distributivity fails.
- **Friedman, *Dynamics of Reason*** — the relativized a priori. Admissibility
  conditions (CE, σ-additivity, faithfulness) as framework-relative constitutive
  principles = the Passage-Conditions grammar's philosophical home.

### Tier 2 — problem before solution; local→global passage (the failure-mode lens)
- **Lautman** (Duffy, "Lautman on problems as conditions of existence of solutions,"
  PhilPapers `DUFLOP`). Problem-horizon more fundamental than any solution → "local
  horizon / global completion / failure mode." The "Exit-A / Exit-B are two outcomes
  of one question" insight is pure Lautman.
- **Zalamea, *Synthetic Philosophy of Contemporary Mathematics*** — local/global,
  sheafification, transit (Urbanomic excerpt). Closest existing vocabulary to "does
  the horizon close into a world."
- *(Lighter: SEP "Structuralism in the Philosophy of Mathematics" — but flagged "too
  static"; want the dynamic/horizon version, which is why Lautman/Zalamea sit above.)*

### Tier 3 — the quantum-foundations realism axis (where the lead literally lives)
*The Paper II cluster — the most direct prior art for the remaining lead.*
- **Putnam, "Is Logic Empirical?" (1968)** [`Putnam1968`]. Origin of "the realism
  question turns on distributivity"; the boldest version of the thesis (quantum
  logic's non-distributivity as a factual discovery).
- **Stairs, "Quantum Logic, Realism, and Value Definiteness," *Phil. Sci.* 50 (1983)
  578–602** [`Stairs1983`]. The conclusion Paper II says Stairs reached directly:
  value-definiteness fails under non-distributivity. **Closest published statement to
  the lead's negative horn** — read knowing it is near-neighbor prior art. (Also: a
  Paper-II citation gap flagged 2026-06-13; see `two_species_underdetermination_kill`.)
- **Bub & Pitowsky, "Two Dogmas about Quantum Mechanics" (2010)** [`BubPitowsky2010`].
  Treat the non-Boolean event structure as primitive; don't seek a hidden
  state-space. The contemporary form of "relational, no smuggled realization" =
  Reading 1.
- **Pitowsky, *Quantum Probability — Quantum Logic* (LNP 321, 1989)** [`Pitowsky1989`].
  Probability *on* a non-Boolean logic, done rigorously — most directly about the
  lead's actual object.
- *(Background, for the philosophical gloss only — you know these technically:
  Kochen–Specker 1967 `KochenSpecker1967`; Bub–Clifton 1996 `BubClifton1996`.)*

### Tier 4 — the discipline guardrail (read last, keep in view)
- **Maddy, *Second Philosophy*** — philosophy *serves* the mathematics and is cast
  away when the theorem path is clear. The antidote to over-philosophizing the lead
  into a verdict it hasn't earned.

---

## Discipline (the two scaffold sections most relevant right now)

From `philosophy_lit_review.md`:
- **§10 the tetralemma scaffold** — the lead resists the inside/outside binary
  (assume-σ / negate-σ / both / neither each self-destruct on the Boolean side; the
  σ-essential state is the OML image of the finite-cofinite charge). The useful
  residue: *the question is which admissibility condition licenses the passage from
  non-distributive coherence to relational probability* — not whether probability is
  "inside or outside."
- **§11 do not objectify the middle** — state obstructions, state the passage, do NOT
  ontologize the passage into "the σ-essential object exists/doesn't." Hold it as an
  open question about a crossing. (This is the exact failure mode — tidying an
  inclination into a verdict — that recurs and must be braked.)

## Pointers
- Whole-programme scaffold: `notes/unsorted/foundations/coherence_completion/philosophy_lit_review.md`.
- The lead's technical state + orientation pole: `oml_onboarding.tex` (§4.3
  route-(iii), §5 the open problem); the `sigma_essential_construction_attempt` memory
  (THE POLE block).
- Paper II (the realism vocabulary this reading supports): `papers/paper_ii/`.
- Bib entries: `papers/paper_ii/references.bib` (the Tier-3 keys above).
