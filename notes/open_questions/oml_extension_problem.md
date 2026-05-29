# The Extension Problem for Orthomodular Observation Algebras

## Problem statement

Let A be an orthomodular lattice with a state s : A → [0,1]
(s(1) = 1, s(a + b) = s(a) + s(b) when a ⊥ b).  The McDonald-
Bimbó dual S₀(A) = (F(A), ⊆, ⊥_A, P(A), T(S)) is a compact
topological space.

Define μ on the clopen ⊥-stable sets CO(S₀(A))† by:

  μ(h(a)) = s(a),     where h(a) = {x ∈ F(A) : a ∈ x}.

**Question:** Does μ extend to a σ-additive measure on the
Baire (or Borel) σ-algebra of S₀(A)?

This is the direct OML analogue of Paper I's stone_measure_exists.

## Why it's hard: the structural obstacle

In the Boolean case (Paper I):
- h : A → Clop(St(A)) is a Boolean algebra isomorphism
- The clopens form a Boolean algebra
- s is finitely additive on this Boolean algebra
- Standard extension (Carathéodory / Choksi) applies
- Compactness gives σ-subadditivity for free

In the OML case:
- h : A → CO(S₀(A))† is an OML isomorphism
- CO(S₀(A))† is an OML, NOT a Boolean algebra
- s is additive on orthogonal pairs only, not arbitrary unions
- **Carathéodory does not apply** — no Boolean algebra of sets
- Compactness holds (Lemma 3.5 of McDonald-Bimbó), but the
  σ-subadditivity argument needs orthogonality structure

The gap: in the Boolean case, "finitely additive on a compact
Boolean algebra of clopens" automatically extends.  In the OML
case, "orthogonally additive on a compact OML of clopen ⊥-stable
sets" does NOT automatically extend — the extension requires
additional input.

## Where Gleason's theorem enters

For the prototypical case A = L(H) (closed subspaces of Hilbert
space, dim(H) ≥ 3):

- Gleason's theorem: every state on L(H) is of the form
  s(P) = tr(ρP) for a density operator ρ
- This gives a σ-additive measure on L(H)
- The extension to S₀(L(H)) follows

For general OMLs, Gleason-type results are not available.  The
extension problem is the theorem:

**Theorem (to prove or disprove):** Under what conditions on the
OML A does every state s extend to a σ-additive measure on
S₀(A)?

## What's different from the Boolean case

| Feature | Boolean (Paper I) | OML (this problem) |
|---------|------------------|-------------------|
| Dual space | St(A) = ultrafilters | S₀(A) = all filters |
| Distinguished subset | pure(Ω), not canonical | P(A), canonical |
| Clopens | Boolean algebra | OML (non-distributive) |
| Additivity | full (finite) | orthogonal pairs only |
| Extension | automatic (Carathéodory) | requires Gleason-type result |
| Realization constrained? | No | Yes (Kochen-Specker) |

## The descent question

Even if μ extends to a measure on S₀(A), the descent question
changes character:

- Boolean: does μ̂ concentrate on pure(Ω)? Answer: iff
  σ-additive. Unconstrained choice of Ω.
- OML: does μ̂ concentrate on P(A)? Answer: ???
  P(A) is part of the structure.  The Kochen-Specker obstruction
  means not all filters can be simultaneously realized.  The
  Bub-Clifton theorem says the state determines a maximal
  Boolean subalgebra of definite values.

So the descent is not a free choice — the algebra + state
together constrain which filters are "realized."

## Connections

- **Paper I:** the Boolean special case; Stone construction;
  unconditional measure on St(C); descent requires Ω
- **McDonald-Bimbó 2023:** the OML duality providing S₀(A)
- **Gleason 1957:** extension for L(H), dim ≥ 3
- **Bub-Clifton 1996:** uniqueness of definite-value subalgebra
- **Döring-Isham 2008:** topos approach; spectral presheaf; 
  states ↔ measures on presheaf
- **Derr-Williamson 2023:** pre-Dynkin systems; coherent partial
  probabilities; related but different generalization (partial
  precision on Boolean algebra vs full precision on non-Boolean)

## The structural diagnosis (literature audit 2026-05-17)

**Key finding:** Pták-Pulmannová (1994) proves that conditions
strong enough to force σ-additivity on OML states collapse
the OML back to a Boolean algebra.  This is the structural
reason no KVP analogue exists for OMLs.

Specifically: if every unital subadditive measure on an OMP is
a state (the condition needed for Carathéodory-style extension),
the lattice must be Boolean.  The non-distributivity of OMLs is
load-bearing — it blocks the Boolean extension machinery at the
algebraic level, not just by lacking the right theorem.

### Why this is harder than "find the right condition"

In the Boolean case, KVP (Fremlin Theorem 391D) gives:
  measurable ⟺ Dedekind σ-complete + weakly (σ,∞)-distributive + chargeable

Each condition is algebraic and non-trivially constraining.  For OMLs:
- Dedekind σ-completeness makes sense but is very strong
- Weak (σ,∞)-distributivity has no clean OML analogue
- Chargeability (existence of a strictly positive finitely additive
  measure) has no known structural characterization on OMLs

The OML extension problem requires genuinely new ideas, not
adaptation of Boolean techniques.

### What the recent literature shows

**Positive results (special cases):**
- Gleason (1957): L(H), dim ≥ 3 — the prototype
- Bunce-Wright (1992): JBW-algebras; σ-additivity via
  operator-algebraic structure
- Chetcuti-Dvurečenskij (2003, 2005): lattice effects algebras;
  positive results when the algebra has "enough structure"
  (completeness conditions close to von Neumann)

**Negative/obstructive results:**
- Pták-Pulmannová (1994): unital subadditive → Boolean (the killer)
- Navara (1992): regularity does NOT force σ-additivity on
  general OMPs; Béaver-Cook is special to von Neumann algebras
- Pták (1987): exotic OML state spaces; obstruction is
  combinatorial (Greechie pasting), not from center

**Recent incremental work (2020s):**
- Voráček-Pták (2023): signed measures on OMPs
- Burešová-Pták (2023): variations on regularity conditions
- De Simone-Navara (ongoing): YH-type decompositions for OMPs

**Assessment:** The field is active but no one has found the
right condition.  The gap between "too weak" (allows non-σ-additive
states) and "too strong" (collapses to Boolean) appears
structurally robust.  This is not a problem where more reading
will unstick it — it needs a new idea.

### Construction tools

All known exotic OML state spaces are built by **Greechie pasting**
(confirmed by Wilce 2009, Handbook of Quantum Logic ch. 24;
Shultz 1974; Pták 1987).  Any progress on the extension problem
likely requires either:
- A new pasting technique that controls σ-additivity, or
- An approach that bypasses the state space entirely (e.g.,
  categorical/topos-theoretic)

## Assessment

This is a precise, well-formulated problem.  The main theorem
(extension from OML state to measure on S₀(A)) would unify:
- Paper I (Boolean case)
- Gleason's theorem (L(H) case)
- Bub-Clifton (descent/realization)

under a single framework: states on directed OMLs → measures
on dual spaces → constrained descent.

**Difficulty:** High.  The Pták-Pulmannová obstruction shows this
is not merely "find the right condition" — conditions strong enough
to force extension destroy the non-Boolean structure.  Requires a
genuinely new approach.

**Novelty:** The formulation via McDonald-Bimbó duality appears
to be new.  The Döring-Isham topos approach addresses related
questions but via presheaves, not the filter-space duality.

**Status:** OPEN but structurally resistant (2026-05-17).  Not a
current active lead — needs collaboration or a new idea.
