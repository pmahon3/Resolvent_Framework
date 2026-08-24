/-
# The Product Ulam Carrier at ω₁ — the σ-side, ZFC-unconditional

Instantiates `UlamWitnessCore` at `M₁ := (ω₁).toType`: uncountable, with
countable initial segments (the two facts Lemma 2.1 needs, discharged from
Mathlib's ordinal/cardinal API). Everything from the core then holds with **no
hypotheses**: the carrier exists, every σ-additive two-valued state on it is
Dirac-on-carrier, the Specker pattern has empty kernel and no σ-additive
extension, and the witness question for this carrier IS the coherence question.
-/
import QuerySystem.UlamWitnessCore
import Mathlib.SetTheory.Cardinal.Aleph

namespace SigmaEssential.Ulam

open Set Ordinal Cardinal SigmaEssential SigmaEssential.Amended

/-- The concrete index set: the type of the first uncountable ordinal. -/
def M₁ : Type := (ω₁ : Ordinal).ToType

noncomputable instance : LinearOrder M₁ :=
  inferInstanceAs (LinearOrder (ω₁ : Ordinal).ToType)

instance : WellFoundedLT M₁ :=
  inferInstanceAs (WellFoundedLT (ω₁ : Ordinal).ToType)

/-- `M₁` is uncountable. -/
theorem M₁_uncountable : ¬ (Set.univ : Set M₁).Countable := by
  intro h
  have hcard : #M₁ = ℵ₁ := by
    have : #M₁ = (ω₁ : Ordinal).card := Cardinal.mk_toType _
    rw [this]
    exact Ordinal.card_omega 1
  have hle : #M₁ ≤ ℵ₀ := by
    have : Countable M₁ := Set.countable_univ_iff.mp h
    exact Cardinal.mk_le_aleph0
  rw [hcard] at hle
  exact absurd hle (not_le.mpr Cardinal.aleph0_lt_aleph_one)

/-- Initial segments of `M₁` are countable. -/
theorem M₁_seg (β : M₁) : (Set.Iio β).Countable := by
  rw [Cardinal.countable_iff_lt_aleph_one _]
  have htype : type (α := M₁) (· < ·) = ω₁ := type_toType _
  have hmk : #(Set.Iio β) = (typein (α := M₁) (· < ·) β).card := by
    rw [← Ordinal.card_type (α := Set.Iio β) (· < ·), Ordinal.type_Iio_lt]
  rw [hmk, ← Cardinal.ord_aleph, ← Cardinal.lt_ord] at *
  rw [← htype]
  exact typein_lt_type _ β

instance : Nonempty M₁ := by
  by_contra h
  rw [not_nonempty_iff] at h
  exact M₁_uncountable (Set.countable_univ)

/-- A fixed Ulam matrix on `M₁` (Lemma 2.1 discharged). -/
noncomputable def U₁ : UlamMatrix M₁ :=
  (ulamMatrix_exists M₁_seg).some

/-- **The carrier**, concretely: the σ-class on `ω₁ × {0,1,2,3}`. -/
noncomputable def L₁ : MeasurableSpace.DynkinSystem (M₁ × Fin 4) := carrier U₁

/-- A base point (any one will do; the pattern's marked points sit over it). -/
noncomputable def m₀ : M₁ := Classical.arbitrary M₁

/-- **The pattern** `s₀` on the Specker-triple block. -/
noncomputable def s₀ : LocalState L₁ (coreBlock U₁) := corePattern U₁ m₀

/-- **Clause (i), ZFC:** the kernel is empty — no point realizes the pattern. -/
theorem s₀_kernel_empty : kernelL s₀ = ∅ := kernel_empty U₁ m₀

/-- **The σ-side of the main theorem, ZFC-unconditional:** no σ-additive
two-valued state on the carrier extends the pattern (Thm 7.1(2)). -/
theorem s₀_no_sigma_extension (s : TwoValuedState L₁) : ¬ ExtendsS s s₀ :=
  no_sigma_state_extends M₁_uncountable M₁_seg m₀ s

/-- **The reduction, ZFC-unconditional:** the pattern is a σ-essential
contextual state (amended encoding) **iff** it is finitely coherent. Clause (0)
— the §3 invariant + §6 vote state — is the sole remaining obligation; once
`FinitelyCoherent s₀` is proved, `PsiAmended` follows. -/
theorem s₀_witness_iff_coherent : IsSigmaEssentialL s₀ ↔ FinitelyCoherent s₀ :=
  witness_iff_coherent M₁_uncountable M₁_seg m₀

/-- Coherence would close the whole problem: `FinitelyCoherent s₀ → PsiAmended`. -/
theorem psiAmended_of_coherent (h : FinitelyCoherent s₀) : PsiAmended :=
  ⟨M₁ × Fin 4, L₁, coreBlock U₁, s₀, s₀_witness_iff_coherent.mpr h⟩

end SigmaEssential.Ulam
