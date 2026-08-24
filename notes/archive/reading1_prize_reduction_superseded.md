> ⚑ ARCHIVED 2026-06-25 (σ-essential thread cleanup). Superseded by `sigma_essential_reduction_writeup.md` §0 (the question, now answered). Kept for the reasoning trail; not current.

# The Reading-1 prize reduces to a contextual-state question (and σ is load-bearing)

*Finding note, 2026-06-11. Continues `direction2_gate_finding.md`. After the
gate finding (the (a)/(b) fork), the user committed to **Reading 1** (relational =
no hidden (A)-realisation; the canonical dual P(A) is permitted) and asked the
follow-up: is "non-segregation" **detectable** by the programme's empiricist
observer? Working that question reduced the whole point-free swamp to a crisp,
classical quantum-logic question via contextuality.*

> **VERDICT (2026-06-11, after literature scout + OMP/OML hinge check): a
> well-posed, principled, programme-continuous OPEN QUESTION with NO known
> inhabitant — not a live lead, not a death.** Everything the reduction asks for
> EXCEPT one qualifier is *already inhabited by a 1978 example* (Wright's
> pentagon: finite, concrete, an OML, with a σ-additive contextual state outside
> the dispersion-free hull). The sole missing qualifier is **σ-essential**:
> contextuality that **no finite sub-OML witnesses**. That refinement is
> principled — it is exactly the CE / Paper-I compactness-failure phenomenon — but
> it has **no witness** (∏ₙMO₂ provably lacks one; Wright is finite; the scout
> found none) and **no impossibility proof**. By the repo's sharpen guardrail
> (principled refinement AND live witness, else kill) this is neither: it is a
> dormant, sharply-stated open problem. The two exits are Phase-4 math (below).

## The detectability question, and what the observer's data is

"Detectable" (for a Reading-1 empiricist) = a function of the observable data.
The user fixed the data model: **the full no-signalling empirical model** — for
each compatible context (block), the joint probability distribution of the
propositions' values, with marginals agreeing on context overlaps (the
sheaf/no-disturbance condition, Abramsky–Brandenburger). Two-valued evaluations
are the *degenerate slice* of this, not the whole ("1 is a subcase of 2").

This choice is decisive. Had the data been 2-valued-only, the detector space would
be exactly KS-colorability, and the chain would collapse totally:
*concrete ⟹ global 2-valued assignment ⟹ non-contextual ⟹ "segregated"*, making
non-segregation operationally invisible within the concrete class (the
empiricist-underdetermination meta-theorem). With real-valued + joint data, that
collapse does **not** go through — the detector space is the full correlation
polytope, strictly richer than KS-colorability.

## The reduction (advisor-confirmed sound)

With the real-valued data model, the detector for non-segregation is
**probabilistic contextuality**: does a *global joint distribution* reproduce all
the context-wise distributions? For a state `w` on a concrete OML this is
equivalent (a 2-valued state on a concrete OMP *is* a deterministic global section
/ KS assignment, so "global joint" and "hull-decomposition" are the same object):

> **`w` is non-contextual ⟺ `w` lies in the closed convex hull of the
> dispersion-free (2-valued) states ⟺ `w` has a global hidden-variable joint.**

A *contextual* state (no global joint) is exactly one with "no hidden realisation"
— which is the (a)-content. So the Reading-1 prize formalizes cleanly as:

> **Does a concrete OML carry a contextual state — a state NOT spanned by its
> dispersion-free states?**

Two corrections folded in (advisor): the handle is **spanning** (do the
dispersion-free states span the state space?), NOT *simplex* — non-uniqueness of
decomposition is irrelevant, only existence of *some* decomposition matters. And
the question must carry the **σ-additivity** qualifier the programme always
required (see next).

## σ is load-bearing — the ∏ₙMO₂ check (decisive, done by hand)

`W = ∏ₙ MO₂` has the powerset `P(ℕ)` sitting in its center (`∏ₙ{0,1}`). A state
restricts there to a finitely-additive probability on `P(ℕ)`:

- **Finitely additive:** a diffuse / free-ultrafilter / Banach-limit state
  (`w({n})=0` ∀n, `w(ℕ)=1`) is **not** in the closed hull of the point-states
  (the dispersion-free states of W). So `∏ₙ MO₂` **carries contextual states — in
  the finitely-additive layer.**
- **σ-additive:** a σ-additive state on `P(ℕ)` is determined by its singletons
  (`w(ℕ)=Σw({n})`); a diffuse one is impossible. Every σ-additive state is atomic
  = a countable mixture of point-states = **in the hull = non-contextual.**

**So for `∏ₙ MO₂`, contextuality lives only in the finitely-additive layer;
σ-additivity destroys it by forcing concentration on points.** This is the *exact*
CE / Paper-I mechanism (finite additivity has the diffuse/contextual states and
compactness; σ-additivity lacks it). σ is **load-bearing, not decorative** here —
which is why this is not an automatic decorative-σ death.

## What the literature already settles — Wright's pentagon (the constraint)

The scout (2026-06-11) found the finite cell **answered**:

- **Wright (1978), "The state of the pentagon."** The pentagon (pentagram) logic
  is a finite, **concrete** (partition/set-representable) orthomodular structure
  with a *separating* family of 11 dispersion-free states, yet it carries a state
  (μ(eₖ)=½, μ(fₖ)=0) that is **not** in the closed convex hull of its
  dispersion-free states — a contextual state. (Pták 1983, 1987; Svozil; Wilce SEP
  §6.1 corroborate and generalize.)
- **OMP-vs-OML hinge — CHECKED, escape closed.** The pentagon is a Greechie loop
  of length 5; by Greechie's theorem (lattice iff no loop of order <5) it **is an
  OML**, not merely an OMP. So the contextual state lives on a genuine OML.
- **Finite ⟹ σ-complete ⟹ σ-additive (vacuously).** No infinite joins, so the
  state is σ-additive trivially.

**Therefore Wright already inhabits: finite + concrete + OML + σ-additive +
contextual-state-outside-the-hull.** Every qualifier of the reduction except one
is met by a 1978 example. **General spanning (cell 3) is correspondingly
false** — no theorem says every state on a concrete OML is a dispersion-free
mixture; the pentagon refutes it.

## The one surviving qualifier — σ-essential — is the whole question

What Wright does **not** supply: the contextuality is witnessed by a **finite**
sub-OML (the pentagon itself). The reduction's prize needs the contextuality to be
**σ-essential** — present in the σ-complete whole but in **no finite sub-OML**:

> **Is there a σ-complete concrete OML carrying a σ-additive contextual state
> whose contextuality is witnessed by NO finite sub-OML?**

This is **not** a gerrymander to dodge Wright. "Every finite sub-OML has a global
section, but the σ-complete whole has none" is a **compactness failure** — exactly
the *finite-coherence-has-compactness / σ-additivity-does-not* structure that is
Paper I's CE core. That is why the `∏ₙ MO₂` check landed on the CE theme: same gap.
So the refinement is principled and programme-continuous (it clears the *(a)* half
of the sharpen guardrail). But there is **no witness** — `∏ₙ MO₂` provably lacks
one (σ kills its contextuality through the center), Wright is finite, the scout
found none — and **no impossibility proof**. Both halves of the guardrail are
needed; only one holds. Hence: dormant, well-posed, uninhabited.

## The two exits (Phase-4 — the mathematician's, not the LLM's)

> **Both exits SHARPENED by the CE-routing subsession (2026-06-12, verdict GAP —
> `sigma_essential_nonemptiness_finding.md`).** CE does not settle non-emptiness,
> but it localized why: the Boolean CE/Stone kill of ∏ₙMO₂ rests on the
> Boolean-only triple identity *principal ultrafilter = atom = dispersion-free
> state*; on an OML, σ-additivity forces concentration on **central** atoms, but a
> central atom subtends a (non-Boolean) block where a state can stay contextual.
> Irreducible (trivial-center) ⟹ the argument is vacuous. Consequences below.

1. **Exhibit a σ-essential witness** — an infinite concrete OML carrying a
   σ-additive contextual state that no finite sub-OML witnesses. This is the
   relational prize, and it would be genuinely new: a non-Boolean σ-additive
   probability with no global hidden joint, concrete (point-rich on canonical
   P(A)) yet irreducibly contextual *because of* its countable structure.
   **Target sharpened (GAP finding):** the witness must put its infinitary
   structure **off-center** (irreducible / non-central-infinite) — a *product of
   finite blocks like ∏ₙMO₂ is excluded a priori*, because it forces all
   infinitary content into the Boolean center, into Stone's reach. **Pasting /
   countable colimit of Wright-type blocks** is the CE-sanctioned place to look
   (finite sublogics non-contextual, σ-join forces the obstruction, center kept
   trivial); CE raises no objection.
2. **Prove none exists** — a compactness theorem: *every σ-additive state on a
   σ-complete concrete OML is spanned by its dispersion-free states except where a
   finite sub-OML is already contextual.* This is a Type-5 impossibility, equally a
   real result, and it **reinstates the empiricist-underdetermination
   meta-theorem** (`direction2_gate_finding.md`) as a theorem rather than a
   conditional. **Caveat sharpened (GAP finding):** this **cannot reuse the ∏ₙMO₂
   / Stone-over-center mechanism** — that is vacuous off-center. A genuinely
   different finite-witnessing argument is required.

Either exit is a genuine terminus. Neither is solo-LLM work; both are the
user's Phase-4 mathematics. The durable result of this arc is the **reduction
itself** — a two-year-old "point-free probability" intuition converted into a
sharp, classically-grounded open problem with a clean win/kill dichotomy.

## Pointers
- Predecessor: `direction2_gate_finding.md` (the (a)/(b) fork, why "point-free"
  has no stable referent).
- Survey: `oml_onboarding.tex` §5–§6 (the open problem + the fork).
- Origin theme this reconnects to: CE / Paper I (finite-additivity vs σ-additivity,
  the compactness gap) — `programme/program_overview.md`,
  `papers/paper_i/`. The reduction makes the descent axis continuous with the
  Boolean-era origin, as the (a)-alignment predicts.
- Related: [[oml_descent_inhabitation]], [[oml_two_point_spaces]],
  [[distributed_sensor_contextuality_seed]] (the prior contextuality contact —
  note its kill was about *dynamics-intrinsic* contextuality, a different claim).

---

## Update 2026-06-17 — structural dichotomy landed (the prize now has proved structure)

A multi-day hand+compute+lit+advisor push gave the prize a sharp internal
characterization (full record: `[[sigma_essential_construction_attempt]]` memory;
summary in `programme/program_overview.md` §"OML descent / AFTERLIFE"):

- **Sharp theorem.** With `S_df` the compact space of dispersion-free states and
  `O_B = {s : s principal on block B}` (open), `S_df^σ(L) = S_df ∩ ⋂_{block B} O_B`.
  So **≤ℵ₀ atomic blocks ⟹ μ(fakes)=0 ⟹ no leak ⟹ Exit B** (any ground set) —
  conullity via per-block-nullity + countability, **not** via G_δ-ness (`G_δ ⟹ conull`
  is false in general; `S_df^σ` G_δ is a parallel topological sibling, not the cause).
  Rests on F1 (block σ-closure) + the proved tail-chain null lemma; no cross-block ∩.
- **Necessary for any witness:** uncountably many infinite atomic blocks (`S_df^σ`
  non-`G_δ`).
- **The only live construction target is (B):** uncountably many *atomic* blocks on a
  *countable* ground set ℕ (|L| = 𝔠) — the partition-logic non-`G_δ` question. The
  alternative "one non-atomic block" is **struck** (Boolean ⟹ reducible + distributive,
  fails the irreducible + non-Boolean prize constraints).
- **Caveat:** `S_df^σ` ⊋ point-evaluations — consistent atom-threads are σ-additive by
  F1 even when no point of ℕ; the witness `w` must dodge `closed-conv` of all threads.

The two-exit framing of this note still holds (build the witness / prove
impossibility), but the witness exit is now pinned to route (B) and the impossibility
exit is bounded below by the sharp `G_δ` theorem (it must defeat the non-`G_δ`
necessary condition, not merely the finite ∏ₙMO₂ mechanism).
