# Task C: literature claims

## C1. Aut of the projection lattice -- SUPPORTED, with two corrections

**The claim as posed:** "for dim H >= 3, every ortholattice automorphism of the
projection lattice of B(H) is implemented by a unitary or antiunitary, giving
Aut ~= PU(H) x| Z_2, via Wigner / the fundamental theorem of projective
geometry."

**Verdict:** the mathematical content is right; the attribution and the group
formula both need correction.

(a) ATTRIBUTION. The result for ORTHOLATTICE automorphisms is **Uhlhorn's**
theorem (1962), not Wigner's. Wigner's theorem is about ray maps preserving
transition probabilities; Uhlhorn weakened the hypothesis to preserving
ORTHOGONALITY of rays, which is the lattice-theoretic form and is what the
claim actually needs. Uhlhorn's version is, as the literature puts it, "a
purely lattice-theoretical result, close to the First Fundamental Theorem of
projective geometry". Citing "Wigner" for the ortholattice statement is citing
the wrong (stronger-hypothesis) theorem.

(b) DIMENSION. dim >= 3 is correct and is NOT removable: there are explicit
counterexamples to the Uhlhorn form in dimension 2. The reason is standard --
in dim 2 the orthogonality relation on rays is a perfect matching (each ray has
exactly one orthogonal ray), so ANY bijection of the Bloch sphere commuting
with the antipodal map preserves orthogonality, and most are not induced by
unitaries/antiunitaries. Dimension 2 is exactly the MO_kappa-like degeneracy --
which is the same degeneracy as C3 below, and worth noting: MO_2 is the
2-dimensional pathology in miniature.

(c) THE GROUP. "PU(H) x| Z_2" is imprecise. What the theorem gives is that the
automorphism group is the group of unitaries-and-antiunitaries modulo phases,
i.e. PU(H).Z_2, an extension
    1 -> PU(H) -> Aut(P(H)) -> Z_2 -> 1
which is SPLIT for complex H (complex conjugation in an orthonormal basis is an
antiunitary involution), so PU(H) x| Z_2 is right FOR COMPLEX H, dim >= 3.
But for REAL H every automorphism is orthogonal-induced and there is no
antiunitary/unitary distinction: Aut = PO(H), with NO Z_2 factor. So the formula
is correct only with "complex" stated. The claim omitted that hypothesis.

(d) SEPARABILITY. Not required. Uhlhorn/FTPG arguments are dimension-theoretic,
not separability-theoretic; dim >= 3 (any cardinal) suffices.

**WHAT WOULD REFUTE C1:** a dim >= 3 complex Hilbert space and an
orthogonality-preserving bijection of its rays not induced by a unitary or
antiunitary. (None exists -- that is the theorem.)

**Sources.** Uhlhorn, U. (1963), "Representation of symmetry transformations in
quantum mechanics", Arkiv Fysik 23, 307-340. Standard textbook treatment:
Varadarajan, *Geometry of Quantum Theory*, 2nd ed., Springer 1985 (already in
the repo bib as `Varadarajan1985`, notes/open_questions/kits/references_oml.bib)
-- "the automorphisms of the standard logics are induced by the unitary and
antiunitary operators". SHELF STATUS: Varadarajan is in the repo's bib but the
PDF is NOT in notes/literature_review/literature/; Kalmbach 1983 IS on the shelf
but does not state the implementation theorem (checked by full-text extraction).
So this one genuinely needed the web, after the shelf came up empty.

## C2. OML automorphism universality -- CONFIRMED, NOT a confabulation

The claim was flagged "very low confidence, possibly a confabulation". It is
**real**, and the primary source was on the shelf.

**Theorem (Schrag 1976).** Every FINITE group is the automorphism group of some
finite orthomodular lattice.

  Schrag, G. (1976). "Every finite group is the automorphism group of some
  finite orthomodular lattice." Proc. Amer. Math. Soc. 55, 243-249.

Verified by full-text extraction of the shelf copy of Kalmbach (1983),
`notes/literature_review/literature/kalmbach_1983_orthomodular_lattices.pdf`,
Ch. I §4 discussion (p. 55) + bibliography entry. Kalmbach's text: "Schrag 76
used this result in order to prove that every finite group is the automorphism
group of some finite orthomodular lattice." The "this result" is
Sabidussi, G. (1957), "Graphs with given group and given graph-theoretical
properties", Canadian J. Math. 9, 515-525 -- the graph-theoretic Frucht-type
input. So the user's instinct "Frucht/Birkhoff-style" was exactly right in
lineage: it goes Frucht -> Sabidussi -> Schrag.

**CORRECTION to the claim as posed:** the claim said "every group". The theorem
is for **finite** groups and **finite** OMLs. Whether every group (infinite
included) is Aut of some OML I did NOT establish -- GRADE UNDETERMINED for the
infinite case. (Kalmbach Ch. I §4 Exercise 8 and the open-problem list on the
same pages show the area was actively open at that time; note also Kalmbach's
own open problem "compute the automorphism group of the orthomodular lattice
..." at line 2670 of the extract, indicating these computations are not routine.)

**WHAT WOULD REFUTE C2:** a finite group provably not arising as Aut(L) for any
finite OML. (Refuted by Schrag's construction.)
**WHAT WOULD SETTLE the infinite case:** a cardinality or definability
obstruction, or a transfinite extension of the Sabidussi/Schrag construction.

## C3. MO_2 sanity anchor -- PROVED (both numbers confirmed)

Computed exhaustively (and it is a genuine five-minute hand check):

  Aut(MO_2, <=)            = Sym(4),  order **24**.
  Aut(MO_2, <=, perp)      = order **8**.

MO_2 = {0,1} u {a, a^perp, b, b^perp}, four pairwise-incomparable atoms, height
2. Any permutation of the four atoms is an order-automorphism (0,1 forced), so
the order group is Sym(4), order 24. An ORTHO-automorphism must additionally
commute with the involution a<->a^perp, b<->b^perp, i.e. preserve the perfect
matching {{a,a^perp},{b,b^perp}}. That stabiliser is the wreath product
Z_2 wr Z_2 = (Z_2 x Z_2) x| Z_2 ~= D_4, order 8 = 2*2*2 (flip within each of the
two pairs, times swap the two pairs). Both numbers verified by brute force.

**Task A's framing survives.** Indeed C3 is the sharpest illustration of WHY
Theorem A needs atomisticity: in MO_2 the order does NOT determine perp
(24 =/= 8), so "order-automorphism" and "ortho-automorphism" genuinely differ.
In the product Ulam carrier L they COINCIDE, because L contains all singletons
and is atomistic with perp = set complement (Theorem A, Step 5). MO_2 is not a
counterexample to Theorem A -- it fails Theorem A's hypothesis, since MO_2 is
not presented as a concrete orthoposet containing all singletons of its carrier.
This is exactly the load-bearing role of Step 3.
