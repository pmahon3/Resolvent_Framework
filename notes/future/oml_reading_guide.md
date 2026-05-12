# Reading Guide: OML Extension Problem

Minimal path from Paper I background to a working grasp of the
OML extension problem.  Assumes: Boolean algebras, Stone duality,
Carathéodory/Choksi, finitely additive charges, Yosida-Hewitt.

## Level 1: What is an OML? (1-2 days)

An ortholattice with the orthomodular law: a ≤ b ⟹ b = a ∨ (a⊥ ∧ b).
Not necessarily distributive.  Failure of distributivity = the point.

**Read:**
- Kalmbach, *Orthomodular Lattices* (1983), Ch 1-2
- OR Beran, *Orthomodular Lattices: Algebraic Approach* (1985), Ch 1-3

**Focus on:**
- The orthomodular law vs distributivity
- Commutativity: a, b commute iff they generate a Boolean subalgebra
- Boolean subalgebras = "classical contexts"
- Filters vs ultrafilters — why ultrafilters may not exist / be 2-valued

## Level 2: States on OMLs (2-3 days)

s : A → [0,1], s(1) = 1, s(a ∨ b) = s(a) + s(b) when a ⊥ b.
OML analogue of a finitely additive charge.

**Read:**
- Pták & Pulmannová, *Orthomodular Structures as Quantum Logics*
  (1991), Ch 2
- Gleason, "Measures on the closed subspaces of a Hilbert space"
  (J Math Mech, 1957)
- OR Dvurečenskij, *Gleason's Theorem and Its Applications* (1993)

**Focus on:**
- Not every OML admits a state (unlike Boolean → ultrafilters)
- Dispersion-free states = 2-valued homomorphisms
- Kochen-Specker: L(H) has NO dispersion-free states (dim ≥ 3)
- Gleason: every state on L(H) is tr(ρP) for dim ≥ 3
- σ-additivity for OML states

## Level 3: Kochen-Specker theorem (1-2 days)

No 2-valued homomorphism on L(H) for dim ≥ 3.  No global
"realization."  The structural obstruction.

**Read:**
- Mermin, "Hidden variables and the two theorems of John Bell"
  (Rev Mod Phys, 1993) — clearest entry point
- Held, "The Kochen-Specker theorem" (SEP)

**Focus on:**
- Why dimensional (fails dim = 2, holds dim ≥ 3)
- Contextuality: outcomes depend on measurement context
- Bub-Clifton: state + preferred observable → unique maximal
  Boolean subalgebra with definite values

## Level 4: McDonald-Bimbó duality (2-3 days)

The OML analogue of Stone duality.

**Read:**
- McDonald & Bimbó, "Topological duality for orthomodular lattices"
  (MLQ 2023, arXiv:2208.07430)

**Focus on:**
- Def 3.4: S₀(A) = (F(A), ⊆, ⊥_A, P(A), T(S))
- Lemma 3.5: S₀(A) is compact
- A ≅ CO(S₀(A))† — representation theorem
- How P(A) enters as structure (vs invisible in Stone)
- Boolean reduction: verify A Boolean ⟹ classical Stone

## Level 5: Connect back to Paper I (1-2 days)

Re-read Paper I and ask:
- Which arguments use distributivity?
- Which use only compactness?
- Where does Carathéodory break?
- What does descent (μ̂ on S₀(A) concentrating on P(A)) look like?

## Optional

- Döring & Isham, "A topos foundation for theories of physics"
  (JMP 2008) — presheaf approach, same motivation
- Derr & Williamson, "Systems of Precision" (arXiv:2302.03522)
  — partial probabilities on pre-Dynkin systems
- Bub & Clifton, "A uniqueness theorem for 'no collapse'
  interpretations" (SHPMP 1996)
- Halvorson & Clifton, "Maximal beable subalgebras" (IJTP 1999)

## Estimated timeline

Levels 1-4: ~7-10 days focused reading.
Level 5: transition from reading to doing mathematics.
