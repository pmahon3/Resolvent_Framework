# Paper II Outline

## Working title

"Distributivity and the Commensurability of Empirical Adequacy
and Realism"

## Thesis

The realism/empiricism debate has a mathematical answer that
depends on the observation algebra.  Distributivity is the exact
condition under which empirical adequacy and realism are
commensurable.

## Structure

### §1. Introduction

The philosophical problem: when does an empirically adequate
theory admit a realist completion?  Van Fraassen (1980): the
constructive empiricist holds that empirical adequacy suffices;
the realist demands descent to an underlying state space.

Our contribution: this is not a uniform question.  Its answer
depends on the algebraic structure of observations.  We identify
distributivity as the dividing line.

Preview the three-level coherence hierarchy:
1. Consistency (no local contradiction)
2. Contextual coherence (compatible across contexts)
3. Probabilistic coherence (extension to a measure on the dual)

And the descent question: does the measure concentrate on
"realized" points?

### §2. The Boolean case (recap of Paper I)

Directed system (ι, ≤) of Boolean algebras.  Compatible charges.
Cylinder algebra C.  Stone space St(C).

Two constructions:
- Carathéodory: assumes σ-additivity, builds P on (Ω, σ(C))
- Stone: unconditional, builds μ̂ on St(C)

Main result (Paper I): σ-additivity ↔ μ̂(pure(Ω)) = 1.

Key structural facts:
- pure(Ω) ⊆ {countably complete ultrafilters} ⊆ St(C)
- Principality is not intrinsic — depends on choice of Ω
- ANY surjective-projecting S ⊆ St(C) serves as a realization
- The algebra imposes no constraint on descent

**Conclusion:** In the Boolean case, E and R are commensurable.
Every E-theory admits an R-completion (freely chosen).  The
bridge is σ-additivity — all-or-nothing, and the choice is free.

### §3. Orthomodular observation algebras

Motivation: observations that cannot be performed simultaneously.
Not specific to quantum mechanics — arises in experimental
design, database queries, contextual behavioural science,
distributed systems.

Definition of orthomodular lattices (OMLs).  Key property: a, b
commute iff they generate a Boolean subalgebra.  Non-commuting
elements = incompatible observations.

States on OMLs: s : A → [0,1], s(1) = 1, s(a ∨ b) = s(a) + s(b)
when a ⊥ b.  Additive on orthogonal pairs only.

The Kochen-Specker obstruction: for L(H), dim ≥ 3, no 2-valued
homomorphism exists.  No global assignment of definite values.
No global "realization."

### §4. The OML dual space

McDonald-Bimbó duality (2023): the dual of an OML A is
S₀(A) = (F(A), ⊆, ⊥_A, P(A), T(S)).

Key difference from Stone duality:
- The dual uses ALL filters, not just ultrafilters
- Principal filters P(A) are PART OF THE STRUCTURE
- The orthogonality relation ⊥ encodes incompatibility
- When A is Boolean, reduces to classical Stone duality

The representation theorem: A ≅ CO(S₀(A))† (clopen ⊥-stable
sets).  S₀(A) is compact.

### §5. Three kinds of realism

Critical distinction — "realism" is not monolithic:

**Value-definite realism (VDR):** Every observable simultaneously
has a definite value.  Mathematically: a global 2-valued
homomorphism on the observation algebra exists.  In the dual
space: a point in S₀(A) that is dispersion-free for all
observables.

**Probabilistic realism (PR):** There exists an underlying
probability space (Ω, σ(C), P) generating the observations.
Mathematically: descent from the dual-space measure to a
measure on a realization space.

**Empirical adequacy (EA):** The measure on the dual space
agrees with all observations.  No claim about an underlying Ω.

These are nested: VDR ⟹ PR ⟹ EA.

| Type | Boolean | OML |
|------|---------|-----|
| VDR | Available (ultrafilters exist) | Blocked (Kochen-Specker) |
| PR | Available (Paper I descent) | Available (Gleason/Born) |
| EA | Available (Stone construction) | Available (OML dual) |

The key insight: **distributivity controls VDR, not PR.**
Probabilistic realism works in both settings (classically via
Paper I, quantum-mechanically via Gleason).  What fails in the
OML case is the stronger demand that every observable
simultaneously have a definite value.

### §6. The descent problem for OMLs

State s on A → defines μ on CO(S₀(A))† via μ(h(a)) = s(a).

**Question:** Does μ extend to a measure on S₀(A), and does it
concentrate on P(A)?

Structural obstacles (contrast with Boolean case):
- CO(S₀(A))† is an OML, not a Boolean algebra
- Carathéodory fails — additivity on orthogonal pairs only
- Extension requires Gleason-type result (available for L(H),
  not for general OMLs)

For L(H), dim ≥ 3: Gleason gives extension, Born gives descent.
PR is available.  But VDR is blocked (Kochen-Specker).

Bub-Clifton: given a state and a preferred observable, there IS
a unique maximal Boolean subalgebra admitting value-definite
descent.  But the VDR-descent is partial and context-dependent.

### §7. Distributivity as the commensurability condition

The main structural result:

**Theorem (structural):** Let A be a complemented lattice.

(a) If A is distributive (Boolean), then VDR, PR, and EA are
    mutually commensurable.  Every EA-theory admits a VDR-
    completion (via ultrafilters).  The realization is
    unconstrained by the algebra.

(b) If A is non-distributive (OML, dim ≥ 3), then:
    - EA and PR remain commensurable (Gleason)
    - VDR is blocked (Kochen-Specker)
    - Partial VDR is context-dependent (Bub-Clifton)

Part (a) is Paper I + Stone duality.  Part (b) follows from
Kochen-Specker + Gleason + Bub-Clifton + McDonald-Bimbó.

**Corollary:** Distributivity is the exact algebraic condition
under which value-definite realism and empirical adequacy are
commensurable.

This is the precise mathematical content of the realism/
empiricism debate as it pertains to the observation algebra.

### §8. The coherence hierarchy

Four levels, each a strengthening:

1. **Consistency** — no contradiction within a single Boolean
   context (a single maximal commuting subalgebra)
2. **Contextual coherence** — compatible assignments across
   all contexts (a state on the OML)
3. **Probabilistic coherence** — extension to a σ-additive
   measure on the dual space (Gleason-type)
4. **Value-definite coherence** — a global dispersion-free
   state (2-valued homomorphism on the full algebra)

| Transition | Boolean | OML |
|-----------|---------|-----|
| 1 → 2 | Trivial (distributivity) | Non-trivial but possible |
| 2 → 3 | σ-additivity (Paper I) | Gleason-type extension |
| 3 → 4 | Available (ultrafilters) | Blocked (Kochen-Specker) |

Paper I lives at transition 2→3.  The OML paper lives at 3→4
and shows it's exactly where distributivity matters.

The Boolean case collapses: 1→2 is trivial, 3→4 is free, so
the only interesting transition is 2→3.  The OML case has
non-trivial structure at every level, and the critical
obstruction is at 3→4 — the point where the algebra refuses
value-definiteness.

### §9. Discussion

Philosophical consequences:
- The realism debate is not one debate — it stratifies into
  VDR, PR, and EA, with different algebraic answers
- Classical physics (Boolean): VDR, PR, EA all commensurable.
  The realism/empiricism debate is a genuine philosophical
  choice.  Paper I's "geometric commitment" is freely available.
- Quantum/contextual (OML): PR and EA commensurable, but VDR
  blocked.  The demand for value-definiteness is algebraically
  refuted, not just philosophically resisted.
- Van Fraassen's EA is always available; the question is which
  stronger positions the algebra permits

Connection to:
- De Finetti's operationalism (Boolean EA)
- Bohr's complementarity (OML obstruction at 1→2 = VDR blocked)
- Bell's "beables" (Halvorson-Clifton: which observables CAN
  have definite values — the maximal Boolean subalgebra)
- Einstein's realism ("God does not play dice" = demand for VDR)

Open questions:
- The OML extension problem (does the measure on S₀(A) exist
  unconditionally, as in the Boolean case?)
- Ergodic theory of the purely finitely additive part (for
  stationary processes with weaker symmetry)
- Non-OML generalizations (effect algebras, pre-Dynkin systems)

## Estimated length

15-20 pages.  The mathematical content is mostly cited; the
contribution is the structural analysis and the commensurability
theorem.

## Target venues

- Foundations of Physics
- Studies in History and Philosophy of Modern Physics
- Journal of Philosophical Logic
- Synthese (philosophy of science section)

## Dependencies

- Paper I (cited, should be submitted first)
- McDonald-Bimbó 2023 (published)
- Kochen-Specker 1967, Gleason 1957, Bub-Clifton 1996 (classical)
- Van Fraassen 1980 (philosophical framing)
