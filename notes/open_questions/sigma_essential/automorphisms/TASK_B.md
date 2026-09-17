# Task B: computing Stab(L)

By Theorem A the question is: which pi in Sym(Omega) satisfy pi(L)=L?
Answers below are graded; several sub-claims of Conjecture B are refuted.

## B0. Two subgroups exhibited (lower bounds on Stab(L))

**(a) The full fibre group S_4.** For every tau in Sym(F), pi = id_M x tau is
in Stab(L). Proof: pi fixes each cell D_{a,n} = C_{a,n} x F SETWISE (tau
permutes F onto F); pi permutes singletons; and pi(A_i) = M x tau(supp A_i).
The six weight-2 fibre sets M x S (|S|=2) are ALL in L -- the three cores and
their three complements -- and tau permutes the six among themselves (verified
by exhaustive computation: the stabiliser of the six-element family in Sym(4)
is all of Sym(4)). Since pi is a bijection it preserves complements and
disjoint unions, so pi(L) is a sigma-class containing every generator, whence
L subseteq pi(L); applying the same to pi^{-1} gives equality.

**>>> This REFUTES Conjecture B's "S_3 permuting the three cores while fixing
fibre 4".** The group is S_4, order 24, not S_3, order 6. The error in the
conjecture: it computed the stabiliser of the core family {A_1,A_2,A_3}
(which IS S_3 fixing 4 -- exhaustively confirmed, order 6), but L is
complement-closed, so the invariant family is the six weight-2 fibre sets, not
the three cores. The stabiliser of the six is all of S_4. Equivalently: the
normalised set N of Definition 5.4 is an artefact of choosing one representative
per complement pair; it is NOT canonical, and Sym(F) acts on E_4 preserving
weight, hence preserving E_4 itself (all 24 preserve E_4 -- confirmed).

Fibre-4 is therefore NOT distinguished by L. It looks distinguished only
because (A_1 u A_2 u A_3)^perp = M x {4}; but M x {4} is an ODD-weight fibre
set and by Corollary 5.9's argument it is NOT in L. So L cannot see it.

**(b) Countably-supported permutations.** If pi in Sym(Omega) satisfies
pi = id off a countable set N, then for every E in L, pi(E) Delta E subseteq N
is countable, so pi(E) in L by Lemma 5.3(3). Hence the group
  Sym_ctble(Omega) := { pi : |{x : pi(x) =/= x}| <= aleph_0 }
is contained in Stab(L), and it is NORMAL in Stab(L) (conjugation maps support
to the image of the support, preserving countability).

**>>> This REFUTES sub-question B4's product form.** pi = the transposition of
(alpha_0, 1) and (alpha_0, 2) has support of size 2, lies in Stab(L), and
mixes the two coordinates: it is not sigma x tau for any (sigma,tau). Product
form can hold at most MODULO the countable ideal.

## B1. Must pi preserve the fibre partition? -- NO exactly; UNDETERMINED mod ctble

Exactly: NO, by B0(b) (the 2-cycle above destroys the partition at one point).

The task's worry is well-placed but the diagnosis is off: it is not that the
pairwise intersections fail to be in L (they do fail, Cor 5.9), it is that the
fibre partition is not an invariant at all, because L is blind to countable
perturbation. The right question is the mod-countable one, and there the
trace invariant DOES supply a substitute, partially:

**Supported.** Stab(L) acts on the quotient L/ctble, and preserves the
partition of L/ctble into "diagonal" (kappa=0000) and "weight-2" classes,
because that partition is order-theoretically definable mod countable. An
intrinsic separator, from Lemma 5.7 (trichotomy) + Lemma 5.6(IV):

  [E] uncountable is WEIGHT-2 iff every G in L with E n G = empty is countable
  or satisfies E u G co-countable
  (i.e. [E] has at most one nonzero complement-class below [E]^perp),

whereas a DIAGONAL E of uncountable class admits uncountable disjoint G with
E u G not co-countable -- e.g. two distinct cells C_{a,n} x F, C_{a,m} x F in
one row are disjoint, both diagonal-uncountable, union not co-countable.
Hand-check of the "only if": if E is weight-2 with rep (xi,kappa) and G in L is
disjoint from E, Lemma 5.6 leaves only cases (II) [G weight-2 same coset,
eta ~ xi^perp, union co-countable] and (III) [G countable]. Case (IV) is
impossible and case (I) needs both diagonal. So the characterisation holds.
GRADE: **UNDETERMINED** -- the "iff" is FALSE as stated. E = Omega is diagonal
and uncountable, yet its only disjoint partner in L is the empty set, so it
satisfies the right-hand side vacuously. The forward direction (weight-2 => RHS)
is PROVED by the case walk above; the backward direction was established only by
ONE witness (two cells in a row), which gives "some diagonal E fail the RHS",
not "all". In general the backward direction reduces to the matrix-dependent
Afrak question of B2. See SEPARATOR_CHECK.md.

Consequently -- IF a separator existed -- Stab(L) would permute the three
weight-2 cosets of L/ctble, giving a homomorphism Stab(L) -> Sym(3). Since the
separator is UNDETERMINED, this homomorphism is NOT established. What follows
unconditionally concerns only the fibre subgroup id_M x Sym(F): The S_4 of B0(a) surjects onto this Sym(3) with
kernel the Klein four-group V_4 = {id,(12)(34),(13)(24),(14)(23)}: each
double-transposition fixes every weight-2 SUBSET of F setwise-or-to-its-
complement... let me be exact: V_4 acts trivially on the three COMPLEMENT PAIRS
{12,34},{13,24},{23,14}, which are exactly the three weight-2 cosets. So the
fibre action on cosets is S_4/V_4 ~= S_3, matching the "S_3" of Conjecture B --
but only as a QUOTIENT of the fibre group, not as the fibre group itself, and
with fibre 4 not fixed.

## B2. Must pi preserve the cell family? -- MALFORMED as posed

Cells are GENERATORS, not invariants; a set can be generated many ways and
generators are not preserved by automorphisms in general. Restated answerably:

  Does pi induce an automorphism of the diagonal sigma-algebra
  Afrak = sigma(singletons, {C_{a,n}}) on M, mod countable?

GRADE: UNDETERMINED. I did not resolve this. What makes it hard: L depends on
the arbitrary choice of injections g_beta in Lemma 5.1; different Ulam matrices
give literally different carriers L. So "compute Stab(L)" has no choice-free
answer on the diagonal side. A determinate question would fix the matrix and
ask about Aut of the resulting Boolean sigma-algebra mod countable, which is a
question about Sym(omega_1) acting on omega_1/ctble and is not answered here.

## B3. Does the parity code E_4 constrain the fibre action? -- REFUTED (it does not)

Computed: all 24 elements of Sym(F) preserve E_4 (obvious in hindsight --
permutations preserve Hamming weight, and E_4 is the even-weight code, defined
by weight alone). The subgroup preserving the NORMALISED set N has order 6, but
N is not an invariant of L (see B0(a)): normalisation is a bookkeeping choice
of one representative per complement pair, made in Definition 5.4 for
convenience. So the expected "S_3 x {fixing 4}" is not what the code gives.
GRADE: REFUTED (the code imposes no constraint; the constraint claimed came
from a non-invariant normalisation).

## B4. Is product form forced? -- REFUTED

See B0(b). Mixing example exhibited. Mod countable, whether the induced action
on L/ctble is a product is UNDETERMINED, and depends on B2.

## Summary: as much of Stab(L) as the fences support

  Sym_ctble(Omega)  <|  Stab(L),   and   S_4 <= Stab(L) via id_M x tau.
  Stab(L) -> Sym(3) (action on the three weight-2 cosets of L/ctble), the
  composite S_4 -> Sym(3) being S_4/V_4, surjective.
  The kernel of Stab(L) -> Sym(3), modulo Sym_ctble, is UNDETERMINED and is
  essentially the automorphism group of the diagonal sigma-algebra mod
  countable -- matrix-dependent, hence not choice-free.

Conjecture B is REFUTED in both of its stated clauses (S_3-fixing-4; and the
implicit product form). What survives is the weaker, true statement: the fibre
group is S_4 and acts on the three weight-2 cosets through S_4/V_4 ~= S_3.
