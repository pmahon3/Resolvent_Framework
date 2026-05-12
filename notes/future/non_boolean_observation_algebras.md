# Non-Boolean Observation Algebras

## The structural question

Paper I works with Boolean algebras (cylinder algebras).  The
main finding: realization (which ultrafilters are principal) is
unconstrained by the algebra.  What happens for non-Boolean
observation algebras — orthomodular lattices (OMLs)?

## Three programmes, one table

| Programme | Dual space | "Which points are real?" | Constrained? |
|---|---|---|---|
| Paper I (Boolean) | St(C) = ultrafilters | pure(Ω) = principal ultrafilters | No |
| McDonald-Bimbó 2023 (OML) | F(A) = all filters | P(A) = principal filters | Yes — part of structure |
| Döring-Isham (topos) | Spectral presheaf Σ | Global sections of Σ | Maximally — none exist |

## Why OMLs change everything

In the Boolean case, Stone duality uses ultrafilters (2-valued
homomorphisms).  Every Boolean algebra has plenty of them.
Principality is invisible to the duality — additional structure
that the algebra cannot see.

In the orthomodular case (McDonald-Bimbó, MLQ 2023):
- The dual space is F(A) = all filters, not just ultrafilters
- **Principal filters P(A) ⊆ F(A) are part of the dual structure**
- The Kochen-Specker obstruction means there may be no 2-valued
  homomorphisms at all
- The duality reduces to classical Stone duality when the OML is
  Boolean (distributive)

This formalizes Paper I's philosophical observation: "realization
is additional structure over coherence."  In the Boolean case,
this is a philosophical claim.  In the OML case, it is a theorem:
the duality itself requires P(A) as structural data.

## The programme: Paper I for OMLs

### Setup
A directed system (ι, ≤) of orthomodular lattices {L_i} with
compatible "charges" (states, in OML terminology).

### Questions
1. Does a "Stone measure" on F(C) exist unconditionally?
   (Analogue of Paper I's unconditional μ̂ on St(C))

2. What does σ-additivity mean for OML states?
   (Analogue of CE / continuity at ∅)

3. When does mass concentrate on P(C)?
   (Analogue of μ̂(pure(Ω)) = 1)

4. Is the descent constrained — does the OML structure limit
   which sub-collections of filters can serve as "realized"?
   (Analogue of the realization_as_structure.md question)

### Why question 4 might have a different answer

In the Boolean case: any surjective-projecting S ⊆ St(C) works
as a realization.  The algebra imposes no constraint.

In the OML case: the orthogonality relation ⊥ on F(A) encodes
non-commutativity.  Two filters x, y are orthogonal iff ∃a: a ∈ x
and ¬a ∈ y.  This relation constrains which sub-collections can
be "consistent" — you can't simultaneously realize filters that
are orthogonal in the wrong way.

The Kochen-Specker obstruction (no global 2-valued homomorphism)
means there is no "maximal consistent" realization.  But the
Bub-Clifton theorem shows there IS a unique maximal Boolean
subalgebra on which definite values are consistent, given a state
and a preferred observable.

This suggests: **in the OML setting, the algebra DOES constrain
realization, and the state plays a role in determining the
constraint.**  This is the opposite of the Boolean case.

## Prerequisites and hard parts

1. **Existence of states on OMLs**: Not every OML admits a state
   (unlike Boolean algebras, which always have ultrafilters).
   Gleason's theorem gives states on L(H) for dim(H) ≥ 3, but
   the general existence problem is hard.

2. **Directed systems of OMLs**: The morphisms between OMLs are
   ortholattice homomorphisms.  Compatibility of states across a
   directed system needs careful formulation.

3. **Measure theory on F(A)**: McDonald-Bimbó give the topology
   on F(A); defining measures and proving extension theorems
   requires new work.

4. **Kochen-Specker in directed systems**: The obstruction is for
   a single OML.  Does it persist/strengthen/weaken in a directed
   system?

## Key references

- McDonald & Bimbó, "Topological duality for orthomodular
  lattices," MLQ 2023 (arXiv:2208.07430)
- Cannon & Döring, "A generalisation of Stone duality to
  orthomodular lattices," Springer 2018
- Döring & Isham, "A topos foundation for theories of physics,"
  JMP 2008
- Bub & Clifton, "A uniqueness theorem for 'no collapse'
  interpretations," SHPMP 1996
- Halvorson & Clifton, "Maximal beable subalgebras," IJTP 1999
- Clifton, Bub & Halvorson, "Characterizing quantum theory in
  terms of information-theoretic constraints," FoP 2003

## Assessment

This is a genuine programme — not a remark, not a repackaging.
The structural parallel between Paper I (Boolean, unconstrained
realization) and the OML case (non-Boolean, constrained
realization) is precise and the existing duality theorems provide
the right framework.

But it requires expertise in orthomodular lattice theory and
quantum logic that is beyond the current project's scope.  It
would likely need a collaborator with background in algebraic
quantum theory.

**Status:** Scoped.  Not for immediate pursuit.  Seed for
post-submission collaboration or future programme.
