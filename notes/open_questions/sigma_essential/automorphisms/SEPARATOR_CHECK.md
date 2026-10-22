# The B1-int separator: counterexample and the atom route

## Counterexample (advisor, verified)
E = Omega has normalised rep (M,0000): DIAGONAL, and uncountable.
The only G in L with Omega n G = empty is G = empty, which is countable.
So Omega satisfies the RHS ("every disjoint G is ctble or complements E mod
ctble") VACUOUSLY while being diagonal. The "iff" is FALSE as stated.

Diagnosis: I proved the forward direction (weight-2 => RHS) correctly by the
Lemma 5.6 case walk. The backward direction I established by ONE witness --
two cells in a row -- which shows SOME diagonal elements fail the RHS, not ALL.
Quantifier error on my part.

Restricting to "E and E^perp both of uncountable class" removes Omega and the
countable/co-countable degenerate cases, but supplies no backward direction.

## The backward direction, in general
Given diagonal E with rep (xi,0000), xi and xi^perp both uncountable, need:
an UNCOUNTABLE G in L, disjoint from E, with E u G not co-countable.
Such a G is diagonal with eta subseteq xi^perp mod ctble, eta uncountable,
and xi u eta not co-countable, i.e. xi^perp \ eta uncountable.
So the question is: does the diagonal sigma-algebra
  Afrak = sigma(singletons, {C_{a,n}}) on M
split xi^perp into two uncountable pieces, for every such xi?
That is EXACTLY the matrix-dependent question fenced in B2. So the backward
direction does not merely lack a proof -- it REDUCES to the UNDETERMINED item.

## The cheaper route (advisor's suggestion): atoms of L/ctble
Cor 5.10 (stripping bar): E in L with E subseteq A_1 mod ctble is countable or
E ~ A_1. So [A_1] is an ATOM of L/ctble. Same for A_2,A_3 and complements.
If some uncountable DIAGONAL element of L/ctble were NOT an atom, that would
separate weight-2 from diagonal order-theoretically, with no case walk.

Test on a cell: is [D_{a,n}] an atom of L/ctble?
Need G in L, G subseteq D_{a,n} mod ctble, G uncountable, G not ~ D_{a,n}.
- G = C_{a,n} x {1,2}? NOT in Ptilde: its trace quadruple is
  (C_{a,n}, C_{a,n}, empty, empty). A representation needs each coordinate
  ~ xi or ~ xi^perp; coords 3,4 give xi ~ empty, coords 1,2 then give
  xi ~ C_{a,n}, so C_{a,n} ~ empty -- false, C_{a,n} may be uncountable.
  (Advisor flagged this; confirmed by the Def 5.4 analysis.) NOT a candidate.
- G = Y x F for Y subseteq C_{a,n}, Y in Afrak, Y and C_{a,n}\Y both uncountable?
  This IS in Ptilde, rep (Y,0000), and is in L iff Y is built from the
  generators. Whether such a Y exists inside a single cell is again the
  matrix-dependent Afrak question.

=> The atom route bottoms at the SAME fence. If cells are atoms mod countable,
the separator is genuinely unavailable.

## VERDICT
B1-int: **UNDETERMINED** (was: SUPPORTED -- downgraded).
Forward direction (weight-2 => RHS) stands as PROVED.
Backward direction reduces to the matrix-dependent Afrak question (B2).
Consequently B4' (Stab(L) -> Sym(3) well-defined) is UNDETERMINED: without an
order-theoretic invariant separating the classes, a pi in Stab(L) carrying a
weight-2 class to a diagonal class is not excluded.
B-quot SURVIVES but only as a statement about the FIBRE SUBGROUP id_M x Sym(F),
which is proved directly by brute force and needs no separator.
