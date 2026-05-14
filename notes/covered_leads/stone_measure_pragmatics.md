# Pragmatic Utility of μ̂ on St(C)

## The question

μ̂ on St(C) exists unconditionally — no σ-additivity, no Ω.  Is this
pragmatically useful, or merely a proof device?

## The finitary level: no gain

For any cylinder event E ∈ C, the clopen [E] ⊆ St(C) satisfies
μ̂([E]) = ℓᵢ(E).  So for any question about finitely many
observations, μ̂ gives exactly the same answer as the charges.  The
Stone construction adds nothing at the finitary level.

## The infinitary level: genuine content

μ̂ can integrate Baire-measurable functions on St(C), including those
depending on infinitely many coordinates.  Tail events — "the
limiting frequency exists," "the observations converge" — have
well-defined μ̂-probabilities.  These are statements about
observation-patterns (ultrafilters), not about states.

Without descending to Ω, μ̂ answers questions about the asymptotic
behaviour of observations.  This is genuine content beyond the
finitary charges.

## The tractability problem

St(C) is compact, Hausdorff, totally disconnected — but typically
enormous and non-metrizable.  Computing ∫ f dμ̂ for a general
Baire-measurable f on St(C) is not practically feasible without
additional structure.

**The pragmatic utility of μ̂ depends on whether St(C) can be
collapsed to a tractable quotient.**  Symmetry is the classical
mechanism for such collapse.

## De Finetti as proof-of-concept

De Finetti's representation theorem for exchangeable {0,1} sequences
is a case where symmetry makes μ̂ tractable:

- C = cylinder algebra on {0,1}^ℕ
- Charges ℓᵢ are invariant under finite permutations
- St(C) = all ultrafilters on C (enormous)
- Exchangeability symmetry collapses St(C) → [0,1]
- μ̂ pushes forward to the mixing measure on [0,1]

The factoring: the Stone construction gives μ̂ on St(C).
Exchangeability imposes invariance.  The ergodic decomposition
(extreme points of the invariant simplex = Bernoulli measures Ber(p))
collapses the enormous Stone space to the interval [0,1].  De
Finetti's mixing measure is the pushforward of μ̂ through this
collapse.

**De Finetti's theorem factors through Stone.**  The Stone
construction provides the unconditional measure; exchangeability
provides the collapse that makes it computable.

## The general picture

Stone generalizes de Finetti's philosophical move — probability
without ontological commitment to states — to arbitrary directed
systems, without requiring exchangeability.  But without symmetry
(or another structural constraint), the resulting object may be too
wild for computation.

```
directed system + charges
        │
        ▼
   μ̂ on St(C)           ← unconditional, always exists
        │
        ├──[symmetry]──▶  μ on parameter space  (de Finetti)
        │
        ├──[σ-additivity + Ω]──▶  P on (Ω, σ(C))  (Paper I descent)
        │
        └──[nothing]──▶  ??? (St(C) too wild)
```

The three exits from the Stone construction:

1. **Symmetry collapse:** exchangeability, stationarity, or other
   symmetry reduces St(C) to a tractable parameter space.  The mixing
   measure is computable.  This is de Finetti's route.

2. **Realization descent:** σ-additivity + choice of Ω collapses μ̂
   to P on (Ω, σ(C)).  This is Paper I's route.

3. **Neither:** μ̂ exists but may not be practically useful.  The
   charges ℓᵢ already answer every finitary question; μ̂ adds
   infinitary content that cannot be extracted without structural
   commitments.

## What this means

The pragmatic answer: **μ̂ on St(C) is useful when the directed
system has enough structure to make St(C) tractable.**  Without such
structure, the Stone construction is a proof device — powerful for
establishing theoretical results (Paper I's Stone route), but not a
computational tool.

The philosophical answer: μ̂ on St(C) is the mathematically precise
version of "probability as coherent assignment of betting rates on
observables, without ontological commitment to states."  Whether this
is pragmatically useful or merely philosophically satisfying depends
on whether you can compute with it — which depends on symmetry or
other structural constraints that the algebra alone does not provide.

## Connection to realization_as_structure.md

This reinforces the central conclusion: the algebra C does not
constrain the choice of Ω, and it also does not (generically)
provide a tractable replacement for Ω.  Realization is additional
structure in both senses:

- **Ontological:** which ultrafilters are "real"
- **Computational:** which quotient of St(C) is tractable

Both require input beyond C.  The Stone construction makes this
transparent by showing exactly where the unconditional part ends
and the commitments begin.
