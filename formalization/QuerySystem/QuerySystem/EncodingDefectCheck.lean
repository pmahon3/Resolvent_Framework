/-
# Encoding-defect certificate (2026-07-06, verification session)

The scaffold's witness predicate is UNSATISFIABLE as encoded: `Extends` takes the
local pattern `s₀` as a *global* `TwoValuedState d` (σ-additive by definition), so
`s₀` extends itself and `IsSigmaEssential`/`Psi` are provably false — about the
ENCODING, not about the mathematics. Consequences certified below:

* `extends_refl` — the pattern always extends itself.
* `isSigmaEssential_unsatisfiable` — no `(s₀, B)` is ever a witness *as encoded*.
* `psi_false` — the formalized `Psi` is provably false (NOT the paper's Ψ!).
* `diracOnly_certificate_vacuous` — the hypotheses of
  `diracOnly_with_clause_i_gives_witness` are jointly contradictory, so that
  theorem certifies nothing.

Fix required: re-encode the pattern as a LOCAL state on `B` only (values on
`B.sets`, complement-additivity inside `B`), not as a `TwoValuedState d`.
-/
import QuerySystem.SigmaEssentialOpenCore

open Set MeasurableSpace

namespace SigmaEssential.EncodingDefect

open SigmaEssential OpenCore

/-- The pattern trivially extends itself: `Extends` is reflexive. -/
theorem extends_refl {Ω : Type*} {d : DynkinSystem Ω}
    (s₀ : TwoValuedState d) (B : Block d) :
    Extends s₀ s₀ B :=
  fun _ _ => Iff.rfl

/-- **The defect.** `IsSigmaEssential` is unsatisfiable as encoded. -/
theorem isSigmaEssential_unsatisfiable {Ω : Type*} {d : DynkinSystem Ω}
    (s₀ : TwoValuedState d) (B : Block d) :
    ¬ IsSigmaEssential s₀ B :=
  fun h => h ⟨s₀, extends_refl s₀ B⟩

/-- The formalized `Psi` is provably FALSE — a fact about the encoding (the pattern
typed as a global σ-additive state), not about the open problem. -/
theorem psi_false : ¬ Psi := by
  rintro ⟨Ω, d, s₀, B, h⟩
  exact isSigmaEssential_unsatisfiable s₀ B h

/-- The hypotheses of `diracOnly_with_clause_i_gives_witness` are jointly
contradictory: on a Dirac-only carrier the (globally typed) pattern `s₀` is some
`δ_ω`, and then `ω ∈ K(s₀)`, so the kernel cannot be empty. The "certificate" that
Dirac-only + clause (i) yields a witness is therefore vacuous. -/
theorem diracOnly_certificate_vacuous {Ω : Type*} {d : DynkinSystem Ω}
    (hDO : DiracOnly d) (s₀ : TwoValuedState d) (B : Block d)
    (hi : kernel s₀ B = ∅) : False := by
  obtain ⟨ω, rfl⟩ := hDO s₀
  have : ω ∈ kernel (dirac ω) B :=
    (dirac_iff (dirac ω) B ω).mp (extends_refl (dirac ω) B)
  rw [hi] at this
  exact notMem_empty ω this

end SigmaEssential.EncodingDefect
