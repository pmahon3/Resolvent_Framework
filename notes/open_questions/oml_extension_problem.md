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

## Two axes: extension and descent (sharpened 2026-06-02)

The bridge from a state on A to a measure on S₀(A) splits into two
distinct axes that the Boolean case fuses but the OML case separates.
S₀(A) is a Stone space (McDonald-Bimbó Cor. 3.7). Its *full* clopen
algebra CO(S₀(A)) is Boolean; the state lives only on the ⊥-stable
clopens CO(S₀(A))† — the OML, = image of h (Thm. 3.9). These share
only meet (∩); join, complement, and bottom all differ (OML bottom
is {ω}, not ∅).

**(A) Extension axis.** Extend the orthogonally-additive set function
μ from the ⊥-stable clopens to a finitely additive charge on the
*full* Boolean algebra of clopens — the classical Boolean extension
problem (Horn-Tarski 1948). Because h preserves meets, a∧b = 0 forces
h(a)∩h(b) = h(0): meet-zero elements map to *disjoint* clopens. So a
charge must satisfy, for every pairwise-meet-zero family {aᵢ},
Σ s(aᵢ) ≤ 1 — a Pitowsky correlation-polytope / Bell-Boole inequality
system. σ-additivity does not help here.

**(B) Compactness.** Once (A) succeeds, the charge extends to a
σ-additive Borel measure automatically (Stone space, compactness gives
σ-subadditivity for free). This step is unconditional.

**The obstruction is meet-zero vs orthogonal (CORRECTED 2026-06-03).**
Earlier this note called axis (A) "the Pták-Pulmannová frontier needing
a new idea." That was wrong. Three strengthening conditions on s
(Pták-Pulmannová 1994, Def. 2):
1. *State* — additive on orthogonal pairs (a ≤ b⊥).
2. *Valuation* — additive on meet-zero pairs (a∧b=0); binary;
   strictly stronger, since meet-zero is coarser than orthogonality in
   a non-distributive OML.
3. *Extends to a Boolean charge* — the n-ary condition Σ s(aᵢ) ≤ 1 for
   every pairwise-meet-zero family; strictly stronger again.

Axis (A) is condition (3). **It can fail for every state.** On MO₃
(three 2×2 blocks pasted at 0,1) all six atoms are pairwise meet-zero,
so orthoadditivity forces the three complementary pairs to sum to 3
while a charge demands ≤ 1 — no state extends. Verified by independent
LP (`/tmp/mo3_extension.py`, 216-state grid + maximally-mixed: all
infeasible). The maximally-mixed s ≡ ½ *is* a valuation (satisfies (2))
yet fails (3) at {p,q,r} where ½+½+½ = 3/2 > 1. So the obstruction is
the meet-zero/orthogonal gap — **not** σ-additivity and **not**
non-contextuality.

Pták-Pulmannová 1994 Theorem 1 ("unital set of subadditive states ⟹
Boolean") is about the *supply* of valuations, NOT whether a given
state extends — a different statement. Citing it as the extension
obstruction was the error.

**Status of axis (A):**
- *Concrete (set-representable) OMLs:* meet = intersection, so
  meet-zero = orthogonal; (A) reduces to the classical marginal /
  Pitowsky non-contextuality problem.
- *Non-concrete OMLs* (MO₃, L(H)): (A) is strictly stronger, can fail
  universally.
- *Finite case:* a decidable LP — NOT a structurally resistant frontier.
- *Infinite case* (L(H), actual σ-additive measure on S₀(A)): the
  finite counterexample does not speak to it. OPEN.

## The descent question

σ-additivity of the state governs *descent*, not extension. Even
once μ extends to a measure μ̂ on S₀(A):

- Boolean: does μ̂ concentrate on pure(Ω)? Answer: iff
  σ-additive. Unconstrained choice of Ω.
- OML: does μ̂ concentrate on P(A)? Answer: ???
  P(A) is part of the structure.  The Kochen-Specker obstruction
  means not all filters can be simultaneously realized.  The
  Bub-Clifton theorem says the state determines a maximal
  Boolean subalgebra of definite values.

So the descent is not a free choice — the algebra + state
together constrain which filters are "realized."

**Caveat on the descent mechanism.** The McDonald-Bimbó duality is
*finitary*. The identity h(∨ₙ aₙ) = (∪ₙ h(aₙ))^⊥⊥ holds for *finite*
joins but is false in general for countable joins — finitary OML
homomorphisms do not preserve infinite suprema. So even the
σ-additivity ⟹ concentration story (the analogue of Paper I's
descent argument) requires additional σ-completeness + continuity
hypotheses that the 2023 duality does not supply. Making the descent
argument rigorous in the OML setting is itself open.

**The Yosida-Hewitt connection.** De Simone-Navara (2001) decompose
OMP states as s = s_σ + s_wpfa (σ-additive + weakly purely finitely
additive). By the axis split above, the wpfa component governs the
*descent* axis — the analogue of ℓ_p in Yosida-Hewitt — NOT the
extension axis. A natural-looking conjecture ("s extends iff
s_wpfa = 0") is therefore mis-targeted: wpfa = 0 concerns descent
(does the σ-additive state's measure concentrate on P(A)?), while
extension (axis A) is blocked by non-distributivity regardless of
the wpfa component. The decomposition theory and the extension
problem live on different axes.

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
