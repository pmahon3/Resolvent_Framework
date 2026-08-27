/-
# The Product Ulam Carrier — Theorem 7.1 in ZFC

The assembly: instantiation at `ω₁` (`UlamWitnessOmega1`) + the coherence state
(`UlamWitnessState`) discharge the full main theorem with no hypotheses.

`#print axioms psi_ZFC` is the receipt: only `Classical.choice`,
`propext`, `Quot.sound` — ZFC, no cited axioms, no large cardinals.
-/
import QuerySystem.UlamWitnessOmega1
import QuerySystem.UlamWitnessState
import QuerySystem.SigmaEssentialOpenCore

namespace SigmaEssential.Ulam

open SigmaEssential

/-- **Theorem 7.1, ZFC.** The Specker pattern `s₀` on the product Ulam carrier
over `ω₁` is a σ-essential contextual state: finitely coherent (the vote state
`m`), with no σ-additive two-valued extension (Ulam rigidity + empty kernel). -/
theorem product_ulam_witness_ZFC : IsSigmaEssential s₀ :=
  corePattern_witness U₁ M₁_uncountable M₁_seg m₀

/-- **Ψ, in ZFC.** A σ-essential contextual state exists. -/
theorem psi_ZFC : Psi :=
  ⟨M₁ × Fin 4, L₁, coreBlock U₁, s₀, product_ulam_witness_ZFC⟩

/-- **Non-distributivity, machine-checked as a corollary.** The carrier cannot
be intersection-closed (Boolean): the Boolean baseline
(`boolean_no_witness` = Prop 1.6/2.1) forbids witnesses on Boolean
carriers, and the pattern IS a witness. So the witness itself certifies the
carrier's non-Booleanness — no separate structural proof needed. -/
theorem carrier_not_interClosed : ¬ InterClosed L₁ :=
  fun h => boolean_no_witness h s₀ product_ulam_witness_ZFC

#print axioms psi_ZFC
#print axioms carrier_not_interClosed

/-- **The carrier lies outside the Derr–Williamson boundary.** A witness carrier
cannot be Polish-representable (`witness_not_polish`, from DW Thm D.6), and `L₁`
carries one. Derived from the witness rather than exhibited, exactly as
`carrier_not_interClosed` is: the construction certifies its own position
relative to the boundary. -/
theorem carrier_not_polish :
    ¬ SigmaEssential.OpenCore.PolishRepresentable L₁ :=
  SigmaEssential.OpenCore.witness_not_polish s₀ product_ulam_witness_ZFC

#print axioms carrier_not_polish


end SigmaEssential.Ulam
