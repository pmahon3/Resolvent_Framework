# Commensurability of Empirical Adequacy and Realism

## The two theory types

Both sit on the same Stone-type construction:

**Type E (empirically adequate):** Work with the measure on the
dual space (μ̂ on St(C) or S₀(A)).  No descent to a realization
space.  Answers every finitary question.  No ontological claim.

**Type R (realist):** Descend to a measure P on (Ω, σ(C)).
Requires σ-additivity + choice of Ω.  Claims which observation-
patterns correspond to real states.

## The Boolean case (Paper I)

E and R agree on all finitary predictions: μ̂([E]) = ℓᵢ(E).
They disagree only at the infinitary level (tail events, limits).

The algebra imposes no constraint on descent (realization is
freely chosen structure).  So:

- Every Type E theory admits a Type R completion (choose any
  surjective-projecting S ⊆ St(C) as Ω)
- Every Type R theory has a Type E shadow (forget Ω, keep μ̂)
- The choice between E and R is philosophical, not mathematical
- Distributivity guarantees full commensurability

## The OML case (non-Boolean)

Kochen-Specker: no global 2-valued homomorphism on L(H) for
dim ≥ 3.  You CANNOT descend to a full realization — no
assignment of definite values to all observables simultaneously.

Bub-Clifton: given a state and a preferred observable, there IS
a unique maximal Boolean subalgebra admitting definite values.
So descent is possible, but only partially — to a context-
dependent Boolean subalgebra.

This means:

- Type E still works: states on the OML give well-defined
  probabilities for all (compatible) observations
- Type R is constrained: descent is partial, context-dependent,
  and not unique (depends on preferred observable)
- There exist Type E theories with no Type R completion
- The gap is mathematical, not philosophical

## The structural theorem

**Distributivity is the condition under which empirical adequacy
and realism are commensurable.**

| Algebra | E-theories | R-theories | Relation |
|---------|-----------|-----------|----------|
| Boolean | μ̂ on St(C) | P on (Ω, σ(C)) | E ≅ R (modulo Ω choice) |
| OML | state on S₀(A) | Partial descent | E ⊋ R (strict containment) |

When observations are compatible (Boolean / distributive):
- E and R are two descriptions of the same mathematics
- The realism/empiricism debate is a philosophical preference
- σ-additivity is the only bridge condition (Paper I)

When observations are incompatible (OML / non-distributive):
- E is strictly more general than R
- Full realism is blocked (Kochen-Specker)
- Partial realism is possible but context-dependent (Bub-Clifton)
- The algebra settles — at least partially — in favour of
  empirical adequacy

## What this means

The realism/empiricism debate in philosophy of science is not a
single debate.  It has different mathematical answers depending on
the observation algebra:

1. **Classical physics** (Boolean observations): genuine
   philosophical choice.  The mathematics is neutral.  Paper I's
   "geometric commitment" is freely available.

2. **Quantum physics** (OML observations): the mathematics is not
   neutral.  Full realism requires structure the algebra cannot
   provide.  Empirical adequacy is the natural resting place.

3. **The boundary** is distributivity.  The exact point where
   realism becomes mathematically optional (Boolean) or
   mathematically constrained (non-Boolean) is the point where
   the observation algebra loses distributivity.

## Connection to Paper I

Paper I's closing — "the passage to P on (Ω, σ(C)) is the
additional commitment" — is the Boolean case.  The commitment is
available but not forced.

In the OML case, the commitment is partially blocked.  The Stone
construction (or its OML analogue) remains unconditional — the
empirically adequate object always exists.  But the descent to
"what is really happening" is constrained by the algebra itself.

Paper I is the theorem that says: in the classical case, the
bridge between E and R is σ-additivity, it's all-or-nothing, and
the choice is free.  The OML programme asks: what happens to that
bridge when the algebra is non-distributive?

## Connection to coherence/consistency

The three-level structure:

1. Consistency — no contradiction within a single context
2. Contextual coherence — compatible across incompatible contexts
3. Probabilistic coherence — extension to measure on dual space

maps as:

| Transition | Boolean | OML |
|-----------|---------|-----|
| 1 → 2 | Trivial (distributivity) | Non-trivial (Kochen-Specker) |
| 2 → 3 | σ-additivity (Paper I) | Gleason-type extension |
| 3 → descent | Free choice of Ω | Constrained by algebra + state |

The commensurability result lives at the 3 → descent transition:
in the Boolean case it's free; in the OML case it's constrained.
But the OML also adds a new obstruction at 1 → 2 that doesn't
exist classically.
