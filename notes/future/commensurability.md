# Commensurability of Realism and Empirical Adequacy

## Three kinds of realism (critical distinction)

"Realism" is not monolithic.  Three nested positions:

**Value-definite realism (VDR):** Every observable simultaneously
has a definite value.  Mathematically: a global 2-valued
homomorphism (dispersion-free state) exists.

**Probabilistic realism (PR):** There exists an underlying
probability space (Ω, σ(C), P) generating the observations.
Mathematically: descent from the dual-space measure to a
measure on a realization space.

**Empirical adequacy (EA):** The measure on the dual space
agrees with all observations.  No claim about an underlying Ω.

Nested: VDR ⟹ PR ⟹ EA.

## The algebra determines which positions are available

| Type | Boolean | OML (dim ≥ 3) |
|------|---------|---------------|
| EA | Available (Stone) | Available (OML dual) |
| PR | Available (Paper I descent) | Available (Gleason/Born) |
| VDR | Available (ultrafilters) | **Blocked** (Kochen-Specker) |

## The Boolean case (Paper I)

All three positions commensurable.  Distributivity guarantees
2-valued homomorphisms exist, so VDR is available.  The choice
among EA, PR, VDR is philosophical, not mathematical.

Paper I's content: PR requires σ-additivity (the bridge from
EA to PR).  But once σ-additivity holds, realization is
unconstrained — the algebra imposes no constraint on Ω.

## The OML case

EA and PR remain commensurable (Gleason gives the bridge for
L(H), dim ≥ 3).  But VDR is **blocked**: Kochen-Specker says
no global dispersion-free state exists.

Bub-Clifton: given a state and a preferred observable, there IS
a unique maximal Boolean subalgebra admitting value-definite
descent.  But this is partial, context-dependent, and not global.

## The structural theorem

**Distributivity is the exact algebraic condition under which
value-definite realism and empirical adequacy are commensurable.**

- Boolean (distributive): EA ↔ PR ↔ VDR (all commensurable)
- OML (non-distributive, dim ≥ 3): EA ↔ PR but VDR blocked

This is the precise mathematical content of the realism/
empiricism debate as it pertains to the observation algebra.

## What this means

1. **Classical physics** (Boolean): VDR, PR, EA all available.
   Genuine philosophical choice.  Paper I's "geometric commitment"
   is freely available at every level.

2. **Quantum/contextual** (OML): PR and EA available, VDR blocked.
   The demand for value-definiteness is algebraically refuted.
   The "God does not play dice" position (Einstein) is not just
   philosophically resisted but algebraically impossible.

3. **Van Fraassen's EA** is always available — it's the generic
   position.  The question is which *stronger* positions the
   algebra permits.

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
