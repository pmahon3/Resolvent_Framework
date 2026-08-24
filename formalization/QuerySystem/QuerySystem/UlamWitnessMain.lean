/-
# The Product Ulam Carrier — Theorem 7.1 in ZFC

The assembly: instantiation at `ω₁` (`UlamWitnessOmega1`) + the coherence state
(`UlamWitnessState`) discharge the full amended main theorem with no hypotheses.

`#print axioms psiAmended_ZFC` is the receipt: only `Classical.choice`,
`propext`, `Quot.sound` — ZFC, no cited axioms, no large cardinals.
-/
import QuerySystem.UlamWitnessOmega1
import QuerySystem.UlamWitnessState

namespace SigmaEssential.Ulam

open SigmaEssential SigmaEssential.Amended

/-- **Theorem 7.1, ZFC.** The Specker pattern `s₀` on the product Ulam carrier
over `ω₁` is a σ-essential contextual state: finitely coherent (the vote state
`m`), with no σ-additive two-valued extension (Ulam rigidity + empty kernel). -/
theorem product_ulam_witness_ZFC : IsSigmaEssentialL s₀ :=
  corePattern_witness U₁ M₁_uncountable M₁_seg m₀

/-- **Ψ (amended), ZFC.** A σ-essential contextual state exists. -/
theorem psiAmended_ZFC : PsiAmended :=
  ⟨M₁ × Fin 4, L₁, coreBlock U₁, s₀, product_ulam_witness_ZFC⟩

/-- **Non-distributivity, machine-checked as a corollary.** The carrier cannot
be intersection-closed (Boolean): the amended Boolean baseline
(`boolean_no_witness_amended` = Prop 1.6/2.1) forbids witnesses on Boolean
carriers, and the pattern IS a witness. So the witness itself certifies the
carrier's non-Booleanness — no separate structural proof needed. -/
theorem carrier_not_interClosed : ¬ InterClosed L₁ :=
  fun h => boolean_no_witness_amended h s₀ product_ulam_witness_ZFC

#print axioms psiAmended_ZFC
#print axioms carrier_not_interClosed

end SigmaEssential.Ulam
