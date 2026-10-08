# Open question: when does geometric refinement give σ-algebraic generation?

**Opened 2026-10-08.** Dormant until new input (open-question lifecycle).
This is the "well-conditioned" half of the programme's root question. The
flagship kept the injectivity half and recast it as commensurability.
`notes/programme/genealogy.md` (update 2026-10-08) records the root.

## Statement

Delay factor O_L = σ(Φ_L), fibre weights p_z, conditional laws μ_z.

- Collision mass C_L = Σ_z p_z² (geometric refinement).
- Algebraic defect δ_L(S) = E[Var(1_S | O_L)] = Σ_z p_z μ_z(S)μ_z(Sᶜ).

What condition on Φ_L, not equivalent to the conclusion O_∞ = ℬ mod μ, makes
C_L → 0 imply sup_S δ_L(S) → 0?

## What is already settled (`notes/covered_leads/fibre_mixing.md`)

- δ → 0 ⟹ C → 0. The converse is false.
- Witness: the skew product X = A^ℤ × B^ℤ with h(a,b) = a₀ and independent iid
  coordinates gives C_L = 2^{-(L+1)} → 0 while δ_L = 1/4 for all L.
- Fibre mixing (a lower bound per fibre) is useless. The candidate direction
  is an *upper* rate bound, uniform decay of μ_z(S)μ_z(Sᶜ) as C_L → 0.

## Exit criteria

- **Promote:** a non-circular sufficient condition with a proof sketch.
- **Kill:** the condition turns out to be classical in Rokhlin or
  Kolmogorov–Sinai generator theory. The 2026-05 investigation did not run a
  generator-theory prior-art check.
- **New input that would wake it:** any flagship result quantitative in the
  window length; any metric or conditioning statement on windows.

## Bridge hypothesis (flagged 2026-10-08) and its first falsifier

**Hypothesis ⟦HAND — direction, not result⟧.** The conditioning step is the only
point where the two DAG components could constrain each other. Real-valued
windows remove the finite-alphabet compactness (seed C1′) that keeps them apart.
Contextual window families, glued along shared coordinates, give Polish-built,
non-Boolean carriers, and those fall under the paper's open Q6.6 (`DWPolishCut`).
If Q6.6 is negative, continuous-observation protocols carry no σ-essential
obstruction. If it is positive, delay-window gluings are a place to search for a
witness. Bar: amendment 4(b) of `notes/programme/blueprint_dag_connectivity.md`.
Each lane must constrain the other; an instantiation does not count.

**Falsifier.** Does the gluing collapse to a Boolean carrier, or to a class already
settled (Boolean, or horizontal σ-sum, `lem:horizontal`)? **It did not fire.**

| leg | result | grade |
|---|---|---|
| non-Boolean | Two coordinates that each lie in some window but share none make the glued Dynkin carrier fail intersection-closure. Covers chains of length ≥ 2 and rings of length ≥ 4. The real 4-ring is an instance. `formalization/staging/WindowGluing.lean`: `glued_not_interClosed`, `ring4_real_not_interClosed` | **Lean**, axioms `[propext, Classical.choice, Quot.sound]` |
| concrete, σ-complete | automatic for any `DynkinSystem` (`isConcreteCarrier`, `isSigmaCompleteCarrier`) | Lean (existing) |
| Borel on a Polish space | `glued_le_borel`: the carrier lies inside the product σ-algebra. This is the Derr–Williamson D.6 setting; whether σ(D) is the full σ-algebra is not proved here | **Lean** (containment only) |
| `PolishRepresentable` | cannot be certified: it is an opaque `axiom` in `SigmaEssentialOpenCore` | **not decidable in the current formalization** |
| not a horizontal σ-sum | `{x₀∈U}` and `{x₁∈U}` share the Boolean window σ(x₀,x₁), and `{x₁∈U}` and `{x₂∈U}` share σ(x₁,x₂). In a horizontal sum each nontrivial element lies in exactly one block, and every Boolean sub-σ-algebra lies in a block (Zorn). So all three would share one Boolean block, and `{x₀∈U}∩{x₂∈U}` would be in D. Lean refutes that | ⟦HAND⟧ on top of the Lean refutation |
| triangle (all pairs share a window) | non-Boolean in the finite binary oracle only. The Lean invariant does not reach it; a triple-difference version would | machine, finite |

**Contextual statistics live on the carrier, but that does not make a witness.**
In the finite binary oracle (`notes/open_questions/verification/window_gluing_states.py`):
- The odd-parity 4-ring statistics (PR-box-like, not realisable) define a genuine
  state on the glued carrier, with range [0,1].
- The contextual triangle statistics do **not**: the carrier contains
  `{000,111}`, which gets −1/2.
- Restriction to `{0,1}^4 ⊂ ℝ^4` is a Dynkin homomorphism ⟦HAND⟧. So the
  4-ring state pulls back to a **σ-additive** state on the real carrier that no
  Borel measure extends.

That is contextuality, but not σ-essentiality: Φ concerns *two-valued* states.
On the finite glued ring every two-valued state is a Dirac (window restrictions
are Diracs; shared coordinates force a global point) ⟦HAND⟧. This agrees with
standing check 3.

**What is left: the real question, sharpened.** A σ-essential witness on a
window gluing needs finitely additive two-valued window states (Borel
ultrafilters, not points) that agree on shared coordinates but do not glue
around a cycle. Chains (trees) plausibly always amalgamate; rings are the
candidate ⟦HAND — speculative⟧. Next check: can Borel-ultrafilter patterns on
ring windows fail to amalgamate, and does that cycle condition match the
flagship's winding/parity obstruction? A match would be the two-way constraint
the bar asks for. A mismatch, or always-amalgamating rings, would kill the bridge.
