# Seed Note: CE as Gluing Obstruction in Boolean Localization

## Phase: 1 (seed) — needs Phase 2 audit

## The claim

The failure of σ-additive state extension (CE failure) on a Boolean
algebra — or more generally on an OML — might be expressible as a
cohomological/sheaf-theoretic gluing obstruction in the framework of
Boolean localization (Zafiris).

Specifically: represent an OML (or Boolean algebra with refinement
structure) as a sheaf of Boolean algebras over a site of contexts.
Local states (finitely additive charges on each Boolean context)
always exist. The question "does a global σ-additive state exist?"
becomes "do the local states GLUE to a global section?"

If CE failure = non-trivial cohomology class (obstruction to gluing),
then CE has a topological characterization after all — not as a
frame-internal property of one locale (which failed: Simpson dead),
but as a GLUING condition across a diagram of contexts.

## Why this might work where the locale approach failed

The locale approach (Simpson's sublocale) tried to characterize CE
as a property of one valuation on one frame. This failed because:
- Both CE and non-CE valuations are indistinguishable on general opens
- Spatiality of sublocales is trivial classically

The sheaf/gluing approach is structurally different:
- You have MANY Boolean algebras (local contexts), each with a state
- The question is whether these local states are COMPATIBLE in a way
  that forces a global σ-additive state
- The obstruction (if any) lives in the cohomology of the diagram,
  not in the behavior of one valuation on one frame

This is closer to Abramsky-Brandenburger (2011): they show quantum
contextuality = obstruction to global section of a presheaf of
distributions. CE failure might be the MEASURE-EXTENSION analogue
of their contextuality obstruction.

## What to look for in Zafiris

1. Does he define a site/topology on the category of Boolean
   subalgebras of an OML?
2. Does he study STATES as sheaf sections?
3. Does he identify when local states fail to glue?
4. Does σ-additivity appear as a condition on the sheaf/site?
5. Is there a cohomological obstruction to state extension?
6. Does his framework specialize to the Boolean case (where the
   OML IS a Boolean algebra and the "contexts" are sub-algebras)?

## The Boolean case specifically

For a Boolean algebra B with directed refinement:
- "Contexts" could be the finite sub-algebras B_i
- Local states: charges ℓ_i on each B_i (always exist)
- Compatibility: ℓ_j restricts to ℓ_i on B_i ⊆ B_j
- Gluing to global σ-additive state: ← THIS IS CE

So in the Boolean case: CE = the sheaf condition for states
on the directed system of finite Boolean sub-algebras?

But wait — compatibility of charges (ℓ_j restricts to ℓ_i) is
already part of the setup (Paper I's compatibility condition).
The EXTRA content of CE is: the compatible family extends to a
σ-ADDITIVE measure. Not just any extension — a σ-additive one.

So the gluing question isn't "do local states glue?" (they always
do, to a finitely additive charge — Kolmogorov consistency). It's
"do they glue to something σ-ADDITIVE?" That's the extra condition.

## The key question

Is there a TOPOLOGY on the site of contexts such that:
- The sheaf condition for that topology = σ-additivity of the glued state
- The failure of the sheaf condition = CE failure = purely finitely
  additive component persists

If the topology is the right one, then:
- Sheaf (= states glue σ-additively) ↔ CE holds
- Presheaf-but-not-sheaf (= states glue only finitely additively) ↔ CE fails

This would be a non-trivial sheaf-theoretic characterization of CE.
The topology on the site does the work that the frame-internal
approach couldn't do.

## Relationship to the stalled CE-as-sheaf seed

The earlier attempt (directedness_interpolation) tried to put a
Grothendieck topology on the INDEX CATEGORY of the query system
and make CE into a sheaf condition there. It stalled because:
- Witnessing-by-emptiness was too coarse
- Witnessing-by-charge-decay was circular

The Zafiris approach is different: the site is the category of
BOOLEAN SUBALGEBRAS (contexts), not the index category. The
topology comes from the LATTICE STRUCTURE of contexts, not from
the charges. This might avoid the circularity.

## Risk assessment

- Zafiris might already have this → then it's known (check the book)
- The topology required might not exist or might be trivial
- The Boolean case might collapse (all compatible families extend
  finitely additively; σ-additivity might not be a sheaf condition
  for ANY topology on finite sub-algebras)
- This might be the same dead end as before in different language

## Status: DEAD (2026-05-17)

Both prior-art candidates from the seed's decision criterion
resolve negative. The sheaf-theoretic characterization of CE
is a dictionary translation, not a theorem.

### What was read

- Epperson & Zafiris, *Foundations of Relational Realism* (2013),
  Chapters 6, 8, 9, 10 — the book's full sheaf-theoretic framework
- Zafiris (2006) "Sheaf-theoretic representation of quantum measure
  algebras" — J. Math. Phys. 47, 092103 — the paper that puts
  *measures* (not just events) on the Boolean localization site
- Biesel (2024) "Sheaves of Probability" — arXiv:2401.01968 —
  sheaves of measures/probability on measurable spaces

### Why dead: Zafiris (four discriminating constraints)

1. **σ-completeness is presupposed, not produced.** Zafiris (2006)
   p. 5: "The σ-completeness condition... is also required in order
   to have a well-defined theory of observables over L." It's an
   axiom on L, not something the sheaf condition forces.

2. **States are finitely additive throughout.** p. 2: p(x∨y) =
   p(x) + p(y) for x⊥y. σ-additivity never appears as a property
   states must satisfy or that gluing produces.

3. **The topology J = epimorphic families, no cardinality grading.**
   Section VII.B (p. 14): covering sieves are epimorphic families
   in Q — the index set I is unconstrained. Finite, countable, and
   uncountable covers satisfy J uniformly. The finite/countable
   boundary where CE lives is invisible to J.

4. **No cohomology is computed.** The salvage route (H¹ unification
   with Abramsky-Brandenburger contextuality) does not appear.
   Zafiris proves a *reconstruction* theorem (counit ε_L is iso),
   not an *obstruction* theorem.

### Why dead: Biesel (the dictionary translation confirmed)

Biesel proves measures form a sheaf for *finite* covers (Theorem 8)
and probability measures form a sheaf for finite covers (Theorem 11).
Countable covers are explicitly excluded (Remark 7: compatible
family of uniform measures on {1,...,n} fails to glue to ℕ).

The key sentence (§5, p. 6): "Theorems 8 and 11 and Corollary 9
remain valid when we consider measures that are merely *finitely
additive*... since our finite covers do not require us to break any
sets into countable disjoint unions."

This IS the devastating objection stated as a theorem:
- Finitely additive ↔ sheaf for finite covers
- σ-additive ↔ sheaf for countable covers
- The step from finite to countable is exactly CE
- No hidden cohomological structure; just the tautology

For countable covers: Theorem 8 (Meas) still holds, Corollary 9
needs "σ-finite" replacing "finite," Theorem 11 generalizes only
up to scaling (σ-finite equivalence classes). Standard measure
theory throughout.

### The devastating objection: final form

The seed asked: is there a topology on the site of contexts such
that the sheaf condition = σ-additivity? Answer: yes, trivially —
the countable-partition topology. But this is a restatement of the
definition of σ-additivity, not a characterization. The two
candidates that might have given non-trivial content (Zafiris's
epimorphic-family topology, Biesel's finite-cover lattice) both
fail: Zafiris can't see the finite/countable boundary, and Biesel
sees it exactly but confirms it's just the definition.

No cohomological unification with Abramsky-Brandenburger
contextuality was found in either source. The H¹ salvage route
has no positive evidence from the two closest candidates.

### Useful residue (not a lead, but citable)

- Biesel's Theorems 8 and 11 are clean citations for Paper I's CE
  discussion: "finitely additive charges form a sheaf for finite
  covers; σ-additivity reappears exactly at countable covers."
- Ross (2012) "All roads lead to violations of countable additivity"
  (*Phil. Studies* 161:381–390) — Biesel's ref [2] — potentially
  relevant for the Howson/de Finetti reading direction.
