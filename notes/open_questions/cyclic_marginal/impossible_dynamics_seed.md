# Dynamics on impossible figures (seed, 2026-10-17)

reviewed: false. This is the user's idea (2026-10-16), seeded as `conj.impossible_dynamics` in
`glued_carriers_taxonomy.json`. It was taken up after the triangle settled.

## The puzzle: Escher's staircase as a frieze

Escher's *Ascending and Descending* repeats. Unroll it and you get an endless
frieze of landings …, x₋₁, x₀, x₁, x₂, …:
- every flight goes up: x_n < x_{n+1};
- the picture repeats every 4 landings.

Walking the stairs is the dynamics: one step is the shift x_n ↦ x_{n+1}.

**What it means for walking to change nothing:**
- **A real building.** Repeating every 4 landings would force x₀ < x₁ < x₂ < x₃ < x₄ = x₀, so there
  is none. That is the ring of length 4.
- **On the unrolled frieze.** There are real buildings, for example x_n = n. But walking changes them,
  since x_n = n becomes x_n = n+1.
- **The question.** Is there a consistent answer pattern about the frieze that walking leaves
  unchanged, but that no building, not even an ideal one, fits in a way walking leaves unchanged?

## Dictionary

| figure | dynamics |
|---|---|
| a loop in the window graph | a group acting freely on the window graph (the quotient has the loop) |
| a window (one flight) | one time step {x, Tx} |
| the twist (all flights up) | a cocycle with nonzero "winding": steps that never sum back to 0 |
| real building | a height function h with h(Tx) = h(x) + step (a coboundary) |
| pointless state | an *invariant* state with no *invariant* ideal point |

## Hand observations ⟦HAND — unverified⟧

**H1. An invariant state on the frieze exists (L ≥ 4).**
- Let ι: ℕ^L → ℕ^ℤ copy a ring configuration periodically.
- The preimage of a frieze window event is a ring window event. Preimages also respect complements
  and countable disjoint unions. So ι⁻¹(D_line) ⊆ D_ring.
- Hence s = μ ∘ ι⁻¹ is a state on the frieze carrier, with μ the ring staircase state
  (Lean, `WindowGluing`). Every window of s is p⊗p, with every flight going up.
- s is shift-invariant provided μ is invariant under rotating the ring. By locality
  (`thm:star`), a state on a triangle-free graph is determined by its window values, and the window
  family is rotation-symmetric, so μ is.
- **Check needed:** that `thm:star` applies to the ring (L ≥ 4, triangle-free: yes, hand).

**H2. No invariant ultrafilter fits it.**
- Suppose U is a shift-invariant ultrafilter on ℕ^ℤ containing {x₀ < x₁}.
- Then U contains the non-constant sequences, an invariant set on which the shift has no fixed
  point.
- Katětov's three-set lemma (cited, not proved here): a map with no fixed point splits its domain
  into A₁, A₂, A₃ with f(Aᵢ) ∩ Aᵢ = ∅.
- So some Aᵢ ∈ U. By invariance σ(Aᵢ) ∈ U as well, which gives ∅ ∈ U, a contradiction.
- **Consequence (H1 + H2):** the frieze carries an invariant state that no invariant ideal point
  fits. The twist has moved out of the window graph, which is a line (a forest), and into the
  group action.

**H3. σ-additively, even a stationary version is impossible.**
- If X₀ < X₁ almost surely with the same law, then for every K,
  E[min(X₁,K)] − E[min(X₀,K)] = 0, while min(X₁,K) ≥ min(X₀,K) with strict inequality when
  X₀ < K.
- So P(X₀ < K) = 0 for every K, which is impossible.
- This is the dynamical form of `prop:sigma`.

**H4. The circle version.**
- Rotate a circle by an irrational angle α, and let each step go up by 1.
- A *measurable* height h with h(x+α) = h(x) + 1 is impossible. For every t, e^{2πi t h} would be an
  eigenfunction of the rotation with eigenvalue e^{2πit}, but the rotation's eigenvalues are only
  the countable set {e^{2πikα}}.
- Heights that are not measurable exist (choose one per orbit).
- So here the role of "ideal" is played by regularity (measurability or invariance), not by
  compactness.

## Seam guess

These theories each own a piece of the region:
- **Penrose:** an impossible figure is a nonzero class in Čech H¹ (Penrose 1991/1992). That part is
  owned.
- **Cocycles and coboundaries in ergodic theory:** Gottschalk–Hedlund 1955; Anosov 1973;
  K. Schmidt 1977. Owned.
- **Amenability and invariant means:** Tarski, and finitely additive *probability* invariant states.
  Owned.
- **No invariant ultrafilters for free actions:** Katětov 1967, essentially folklore. Owned.

The candidate seam is **two-valued invariant states on glued (non-Boolean) carriers**: the
equivariant version of pointless coherence. It lies between the covering-space or cohomology view
and invariant means. Means are probability-valued, and our states are two-valued.

## Theory sketch: candidate conjectures

**CE1 (covering).** Let a group G act freely on a window graph Γ. Then G-invariant states on Γ
correspond to states on the quotient Γ/G. In particular, equivariant pointlessness on a free
cover happens exactly when the quotient has a pointless state.
- If true, the dynamics adds nothing beyond loops. It would be a statement about quotients, and an
  owner should be looked for.

**CE2 (aperiodic).** Probe P1 decides between CE1 and CE2. Some shift-invariant states on the
ℤ-line staircase carrier do **not** come from any periodic (ring) state. If so, the dynamics is
genuinely new: twist without a finite loop, for example along a Sturmian or irrational-rotation
pattern.

## Pre-registered probes (2026-10-17, before any work)

**P1. Does every invariant state on the frieze come from a ring?**
- The setting is the ℤ-line, windows {n, n+1}, window states p⊗p going up.
- Does every shift-invariant state on the carrier factor through some ring of length L via ι?
  - (a) Yes → CE1 gains support, and the dynamics reduces to loops in quotients.
  - (b) No → CE2. Then classify the aperiodic invariant states.

**P2. Circle.**
- The setting: slots are the points of the circle, windows are {x, x+α}, and steps go up.
- Does a rotation-invariant state exist on the carrier? If one exists, is it pointless in the
  equivariant sense?
  - (a) Yes → a genuinely ergodic impossible figure.
  - (b) No → the obstruction is σ-like even for finite additivity, and the reason is the next
    object of study.
- **Scope:** the possibility space is uncountable (ℕ^X), while our theorems assume finitely many
  slots. First check which results survive infinitely many slots: locality, and the forests
  theorem by compactness.

**First step.** Run a hostile owned-region scout on the four seam pieces above and on "invariant
two-valued states / equivariant contextuality / periodic contextuality". Do this before any hand
work on P1 or P2.
