/-
# Axiom receipts — the Product Ulam Carrier formalization (2026-07-06)

`#print axioms` triangulation receipts for the full development. Everything
below must show ONLY `[propext, Classical.choice, Quot.sound]` — the standard
axioms (= ZFC). No `sorry`, no cited axioms, no large cardinals.

The chain: encoding fix (`SigmaEssentialAmended`) → σ-side (`UlamWitnessCore`,
`UlamWitnessOmega1`) → §3 invariant (`UlamWitnessInvariant`) → §6 vote state
(`UlamWitnessState`) → Theorem 7.1 (`UlamWitnessMain`), plus the Ω₇
amendment-forcing counterexample (`Omega7Counterexample`).
-/
import QuerySystem.UlamWitnessMain
import QuerySystem.Omega7Counterexample
import QuerySystem.EncodingDefectCheck
import QuerySystem.UlamWitnessFidelity

namespace SigmaEssential

-- The main theorem: Ψ (amended) holds in ZFC.
#print axioms Ulam.psiAmended_ZFC
-- The localized witness: the pattern is σ-essential on the ω₁ carrier.
#print axioms Ulam.product_ulam_witness_ZFC
-- The σ-side alone (rigidity + empty kernel).
#print axioms Ulam.s₀_no_sigma_extension
-- Clause (0): coherence via the vote state.
#print axioms Ulam.corePattern_coherent
-- The amended Boolean baseline (Prop 1.6).
#print axioms Amended.boolean_no_witness_amended
-- Ω₇: the literal definition breaks on a Boolean carrier; the amendment excludes it.
#print axioms Omega7.omega7_no_sigma_extension
#print axioms Omega7.omega7_not_coherent
-- The encoding defect in the OLD spine (psi_false is about the old encoding).
#print axioms EncodingDefect.psi_false
-- Fidelity closures: coherence upgrades LocalState to a full Def-1.2 state on B;
-- the witness block's only disjoint pairs are complement pairs.
#print axioms Amended.coherent_pattern_fully_additive
#print axioms Ulam.coreBlock_disjoint_eq_compl

end SigmaEssential
