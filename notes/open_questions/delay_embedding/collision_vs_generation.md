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
