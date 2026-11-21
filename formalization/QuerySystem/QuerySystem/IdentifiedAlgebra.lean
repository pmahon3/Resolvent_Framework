/-
Identification through a reduction: the set-theoretic cores of Propositions 2 and 3 of
`~/Work/INN-Science/identification-through-reduction/paper/core.tex` (2026-11-19).

Setting. Θ = full parameters, C = reduced coefficients, P = laws of the record, G = values of a
target functional. A reduction ρ : Θ → C and a reduced-law map Λ : C → P give the model
Ψ = Λ ∘ ρ (the ε = 0 case: no leak). Two parameters are *observationally equivalent* when
Ψ θ = Ψ θ' (equal record laws; at ε = 0 every statistic is a flow observable, so this is
equivalence with respect to every flow observable). A target g : Θ → G is *identified* when
observationally equivalent parameters have equal g.

Proposition 2 (global part): if Λ is injective, g is identified iff g factors through ρ.
Proposition 3 (global part): with conditions k ∈ K, each with its own ρ k and Λ k, and an
admissible set A, g is identified on A across the conditions iff g factors on A through the
joint reduction θ ↦ (ρ k θ)_k.

The local (constant-rank) forms of both propositions are NOT formalised here; they rest on the
constant rank theorem, cited in the paper, and were checked by hand and by an independent
referee pass on 2026-11-19.
-/
import Mathlib.Logic.Function.Basic
import Mathlib.Data.Set.Defs

namespace IdentifiedAlgebra

variable {Θ C P G : Type*}

/-- Observational equivalence under the model `Λ ∘ ρ`. -/
def ObsEquiv (ρ : Θ → C) (Λ : C → P) (θ θ' : Θ) : Prop := Λ (ρ θ) = Λ (ρ θ')

/-- `g` is identified by the model: equivalent parameters have equal target values. -/
def Identified (ρ : Θ → C) (Λ : C → P) (g : Θ → G) : Prop :=
  ∀ θ θ', ObsEquiv ρ Λ θ θ' → g θ = g θ'

/-- `g` lies in the identified algebra of `ρ`: it factors through the reduction. -/
def InIdentifiedAlgebra (ρ : Θ → C) (g : Θ → G) : Prop := ∃ g' : C → G, g = g' ∘ ρ

/-- **Proposition 2, global part.** With `Λ` injective, `g` is identified iff `g ∈ 𝒜_ρ`. -/
theorem identified_iff_inIdentifiedAlgebra [Nonempty G] (ρ : Θ → C) (Λ : C → P)
    (hΛ : Function.Injective Λ) (g : Θ → G) :
    Identified ρ Λ g ↔ InIdentifiedAlgebra ρ g := by
  constructor
  · intro h
    have hft : Function.FactorsThrough g ρ := fun θ θ' hρ => h θ θ' (by
      show Λ (ρ θ) = Λ (ρ θ'); rw [hρ])
    refine ⟨Function.extend ρ g (fun _ => Classical.arbitrary G), ?_⟩
    funext θ
    exact (hft.extend_apply _ θ).symm
  · rintro ⟨g', rfl⟩ θ θ' h
    have : ρ θ = ρ θ' := hΛ h
    simp [Function.comp, this]

/-- The easy direction, with no `Nonempty` hypothesis: anything that factors through `ρ`
is identified as soon as `Λ` is injective. -/
theorem identified_of_inIdentifiedAlgebra (ρ : Θ → C) (Λ : C → P) (hΛ : Function.Injective Λ)
    (g : Θ → G) (hg : InIdentifiedAlgebra ρ g) : Identified ρ Λ g := by
  rcases hg with ⟨g', rfl⟩
  intro θ θ' h
  have : ρ θ = ρ θ' := hΛ h
  simp [Function.comp, this]

section Family

variable {K : Type*} {Cf : K → Type*} {Pf : K → Type*}

/-- Joint observational equivalence on an admissible set `A`, across conditions `k`. -/
def ObsEquivFamily (ρ : ∀ k, Θ → Cf k) (Λ : ∀ k, Cf k → Pf k) (θ θ' : Θ) : Prop :=
  ∀ k, Λ k (ρ k θ) = Λ k (ρ k θ')

/-- `g` is identified on `A` across the conditions. -/
def IdentifiedOn (A : Set Θ) (ρ : ∀ k, Θ → Cf k) (Λ : ∀ k, Cf k → Pf k) (g : Θ → G) : Prop :=
  ∀ θ ∈ A, ∀ θ' ∈ A, ObsEquivFamily ρ Λ θ θ' → g θ = g θ'

/-- `g` factors on `A` through the joint reduction `θ ↦ (ρ k θ)_k`. -/
def FactorsOn (A : Set Θ) (ρ : ∀ k, Θ → Cf k) (g : Θ → G) : Prop :=
  ∃ g' : (∀ k, Cf k) → G, ∀ θ ∈ A, g θ = g' (fun k => ρ k θ)

/-- **Proposition 3, global part.** With every `Λ k` injective, `g` is identified on `A`
across the conditions iff it factors on `A` through the joint reduction. -/
theorem identifiedOn_iff_factorsOn [Nonempty G] (A : Set Θ) (ρ : ∀ k, Θ → Cf k)
    (Λ : ∀ k, Cf k → Pf k) (hΛ : ∀ k, Function.Injective (Λ k)) (g : Θ → G) :
    IdentifiedOn A ρ Λ g ↔ FactorsOn A ρ g := by
  constructor
  · intro h
    -- restrict to the subtype `A` and factor through the joint reduction there
    let ρA : {a : Θ // a ∈ A} → (∀ k, Cf k) := fun a k => ρ k a.1
    let gA : {a : Θ // a ∈ A} → G := fun a => g a.1
    have hft : Function.FactorsThrough gA ρA := by
      intro a b hab
      apply h a.1 a.2 b.1 b.2
      intro k
      have : ρ k a.1 = ρ k b.1 := congrFun hab k
      show Λ k (ρ k a.1) = Λ k (ρ k b.1); rw [this]
    refine ⟨Function.extend ρA gA (fun _ => Classical.arbitrary G), ?_⟩
    intro θ hθ
    exact (hft.extend_apply _ ⟨θ, hθ⟩).symm
  · rintro ⟨g', hg'⟩ θ hθ θ' hθ' h
    rw [hg' θ hθ, hg' θ' hθ']
    congr 1
    funext k
    exact hΛ k (h k)

end Family

end IdentifiedAlgebra
