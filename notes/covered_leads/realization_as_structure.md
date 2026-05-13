# Realization as Additional Structure

## The question

Can the role of Ω in selecting "principal" ultrafilters be characterized
purely in terms of properties of the ultrafilter collection on C,
without presupposing an external realization space?

## Answer: No — and the algebra imposes no constraint

Given any S ⊆ St(C) that projects surjectively onto each St(Bᵢ),
we can take Ω = S with eval maps given by the restriction maps
St(C) → St(Bᵢ).  Discriminability is automatic (distinct ultrafilters
separate).  So S = pure(Ω) for this instantiation.

**The algebra C places essentially no constraint on which ultrafilters
are realized.**  Any sufficiently surjective sub-collection works.
"Realization" is not additional in the sense of "one more datum to
pin down" — it is additional in the sense of "unconstrained by the
algebra."  This is the precise content of the claim that realization
is freely chosen structure over coherence.

## The three-layer nesting

```
pure(Ω)  ⊆  {countably complete ultrafilters on C}  ⊆  St(C)
   |                      |                               |
NOT intrinsic         intrinsic                       intrinsic
(depends on Ω)       (algebraic)                     (algebraic)
```

### Layer 1: St(C) — all ultrafilters

Determined by C alone.  Compact, Hausdorff, totally disconnected.
Every compatible family of charges lifts to a Baire probability
measure μ̂ on St(C) — unconditionally.

### Layer 2: countably complete ultrafilters

An ultrafilter u on C is **countably complete** (relative to C) if
whenever E₁, E₂, ... ∈ u and ⋂ₙ Eₙ ∈ C, then ⋂ₙ Eₙ ∈ u.

This is a purely algebraic property of u — no Ω involved.

Rao-Rao (Theorem 10.5.3): σ-additivity of a charge is equivalent to
its Stone extension vanishing on meagre Baire sets.  The algebraic
counterpart: μ̂ assigns full mass to the countably complete
ultrafilters.  This is the best intrinsic approximation to "mass
lives on realized states."

### Layer 3: pure(Ω) — principal ultrafilters

For a given instantiation (Ω, {evalᵢ}), each ω ∈ Ω determines
pure(ω) = {E ∈ C : ω ∈ E}.  Every principal ultrafilter is
countably complete (closed under all intersections that land in C).
So pure(Ω) ⊆ {countably complete ultrafilters}.

But which countably complete ultrafilters are principal depends on Ω.
The same Boolean algebra C can be instantiated as an algebra of sets
on different Ω's, giving different pure(Ω) inside the same St(C).

## The gap between Layers 2 and 3

σ-additivity guarantees mass concentrates on Layer 2.  Descent to Ω
requires mass on Layer 3.  The gap between them is where Ω plays an
irreducible role.

**How large can this gap be?**

This depends on C and, for σ-complete algebras, on set theory:

- For σ-complete algebras like P(κ), Ulam's theorem says every
  countably complete ultrafilter on P(κ) is principal when κ < the
  first measurable cardinal.  Under these conditions, Layers 2 and 3
  coincide and the gap vanishes: σ-additivity is sufficient for
  descent.

- For cylinder algebras C that are not σ-complete (the typical case),
  "countably complete relative to C" is a weaker condition than
  σ-completeness of an ultrafilter on a power set.  Non-principal
  ultrafilters satisfying this weaker condition can exist without
  measurable cardinals — the algebra simply doesn't contain enough
  countable intersections to rule them out.  The gap between Layers 2
  and 3 can be non-empty in ZFC.

This connects to the companion note: the non-derivability of
σ-additivity reflects the same boundary between algebraic and
set-theoretic structure, viewed from the charge side rather than the
ultrafilter side.

## What this means for Paper I

The paper states this correctly at the level of the construction:

- μ̂ on St(C) is free (any charges → Layer 1)
- σ-additivity gets μ̂ to Layer 2 (intrinsic)
- Descent to P on (Ω, σ(C)) requires Ω (Layer 2 → Layer 3)
- "The passage from coherent charges to probability is a geometric
   commitment, not a derivation"

The analysis above makes "geometric commitment" precise: it is the
choice of which countably complete ultrafilters count as "realized" —
a choice the algebra cannot make for you.

## Directions

The interesting follow-up is not "what conditions must S satisfy?"
(answer: essentially just surjective projection — too weak to be
useful), but rather:

1. **Minimality:** What is the *smallest* S ⊆ St(C) that supports a
   given μ̂?  Is the support of μ̂ restricted to countably complete
   ultrafilters already the minimal realization?

2. **Canonicity:** Is there a *canonical* choice of realization that
   doesn't smuggle in external structure?  The obvious candidate is
   S = {countably complete ultrafilters}, but this only works when
   Layers 2 and 3 coincide (σ-complete algebras, small cardinals).

3. **Dynamical structure:** If Ω carries additional structure (a
   group action, a topology, a shift), does this constrain which
   S ⊆ St(C) are admissible?  This connects to the broader open
   question: can dynamics emerge from observation without positing T?
   The answer here suggests not — the algebra doesn't constrain S,
   so it certainly doesn't constrain dynamical structure on S.
