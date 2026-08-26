/-
# Axiom receipts — the Product Ulam Carrier formalization (2026-07-06)

`#print axioms` triangulation receipts for the full development. Everything
below must show ONLY `[propext, Classical.choice, Quot.sound]` — the standard
axioms (= ZFC). No `sorry`, no cited axioms, no large cardinals.

The chain: the pattern encoding (`SigmaEssentialWitness`) → σ-side (`UlamWitnessCore`,
`UlamWitnessOmega1`) → §3 invariant (`UlamWitnessInvariant`) → §6 vote state
(`UlamWitnessState`) → Theorem 7.1 (`UlamWitnessMain`), plus the Ω₇
the counterexample that forces the coherence clause (`Omega7Counterexample`).
-/
import QuerySystem.UlamWitnessMain
import QuerySystem.Omega7Counterexample
import QuerySystem.UlamWitnessFidelity

namespace SigmaEssential

-- The main theorem: Ψ holds in ZFC.
#print axioms Ulam.psi_ZFC
-- The localized witness: the pattern is σ-essential on the ω₁ carrier.
#print axioms Ulam.product_ulam_witness_ZFC
-- The σ-side alone (rigidity + empty kernel).
#print axioms Ulam.s₀_no_sigma_extension
-- Clause (0): coherence via the vote state.
#print axioms Ulam.corePattern_coherent
-- The Boolean baseline (Prop 1.6).
#print axioms boolean_no_witness
-- Ω₇: without the coherence clause a Boolean carrier would qualify; it does not.
#print axioms Omega7.omega7_no_sigma_extension
#print axioms Omega7.omega7_not_coherent
-- Fidelity closures: coherence upgrades LocalState to a full Def-1.2 state on B;
-- the witness block's only disjoint pairs are complement pairs.
#print axioms coherent_pattern_fully_additive
#print axioms Ulam.coreBlock_disjoint_eq_compl
-- E-thread (E4): the witness's value-1 core family fails FIP at stage exactly 3.
-- This direction is choice-free at its own content (finite Fin-4 fiber arithmetic);
-- Classical.choice appears only via the ambient corePattern/kernel machinery, never
-- from an ultrafilter extension (the BPI leg of the E1 lemma is NOT formalized here).
#print axioms Ulam.fip_fails_at_stage_three

end SigmaEssential
