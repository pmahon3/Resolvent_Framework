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

## Status: CONDITIONAL (audit 2026-05-17)

Not found in literature, but possibly tautological.

**The devastating objection:** σ-additivity IS the sheaf condition
for countable-partition topology by definition. μ(A) = Σμ(Aᵢ) for
countable partitions = "sheaf for countable covers." If that's all
this is, it's a dictionary translation, not a theorem.

**The salvage route:** Does the cohomological formulation UNIFY
CE failure with Abramsky-Brandenburger contextuality? If both are
H¹ classes of the same presheaf in different topologies on the same
site, that's a genuine structural insight connecting Paper I to
quantum foundations. This would NOT be a dictionary translation.

**Prior art to read before proceeding:**
- Zafiris (2006) "Sheaf-theoretic representation of quantum measure
  algebras" — J. Math. Phys. 47, 092103 (CHECKED OUT in book form)
- Biesel (2024) "Sheaves of Probability" — arXiv:2401.01968
- Abramsky et al. (2015) "Contextuality, Cohomology and Paradox"

**Decision after reading:** If route 2 (unification) has substance
→ promote to active lead. If only dictionary translation → dead.
