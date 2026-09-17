# Task A: the automorphism group is the setwise stabiliser

## Category correction (the claim as posed is MALFORMED)

Claim A says "the group of ORTHOLATTICE automorphisms of L". Corollary 5.11
proves L is **not a lattice**: A_1 ^ A_2 does not exist. So "ortholattice
automorphism of L" has no referent. The operative notion:

**Definition.** An *orthoposet automorphism* of L is a bijection
phi : L -> L with (i) E subseteq G  <=>  phi(E) subseteq phi(G), and
(ii) phi(E^perp) = phi(E)^perp.

All of Theorem A below is stated for that group, written Aut(L).
(Remark: (ii) turns out to be redundant -- see Step 5.)

## Theorem A
Let Omega be any set and L subseteq P(Omega) a concrete orthoposet containing
every singleton. Then
    Aut(L)  ~=  Stab(L) := { pi in Sym(Omega) : pi(L) = L },
via pi |-> (E |-> pi(E)), and the inverse sends phi to its action on atoms.

Note the hypotheses: ONLY "contains all singletons". Nothing about the Ulam
matrix, the cores, the invariant, or rigidity. The product Ulam carrier L of
Definition 5.2 satisfies this by construction.

## Proof

**Step 1 (suprema in L are unions).** Let {E_i} subseteq L and suppose
U := union_i E_i lies in L. Then U = sup_L {E_i}: it is an upper bound, and if
G in L is any upper bound then E_i subseteq G for all i, so U subseteq G.
(No sigma-class closure is used -- only that the union happens to be in L.)

**Step 2 (atoms = singletons).** 0_L = empty set. Singletons are in L by
hypothesis and are minimal nonzero in P(Omega), a fortiori in L: atoms.
Conversely let E in L with E =/= empty and E not a singleton. Pick omega in E.
Then empty !=  {omega} subsetneq E and {omega} in L, so E is not an atom.
Hence Atoms(L) = { {omega} : omega in Omega }.

**Step 3 (L is atomistic).** For every E in L,
    E = sup_L { {omega} : omega in E },
because union_{omega in E} {omega} = E in L, and Step 1 applies.
*** This is the load-bearing step. *** It holds for arbitrary E, including
uncountable E where the union is NOT a countable orthogonal join -- Step 1
does not care, since the union is in L by assumption (it equals E).

**Step 4 (phi is induced by a permutation).** Let phi in Aut(L). Being an
order-isomorphism, phi maps atoms bijectively to atoms, so by Step 2 there is
a unique pi in Sym(Omega) with phi({omega}) = {pi(omega)}.
An order-isomorphism preserves all existing suprema. So for E in L, using
Step 3 twice,
    phi(E) = phi( sup {{omega}: omega in E} ) = sup { {pi(omega)} : omega in E }
           = sup { {omega'} : omega' in pi(E) } = pi(E),
the last equality being Step 3 applied to phi(E) in L (which has atom set
exactly {{pi(omega)} : omega in E}). Hence phi(E) = pi(E) as SETS, and since
phi is onto L, pi(L) = L: pi in Stab(L).

**Step 5 (converse; perp is automatic).** Let pi in Stab(L). Then E |-> pi(E)
is a bijection L -> L (inverse given by pi^{-1}, also in Stab(L)), clearly an
order-isomorphism for subseteq. And
    pi(E^perp) = pi(Omega \ E) = Omega \ pi(E) = pi(E)^perp,
because pi is a BIJECTION of Omega (injectivity gives subseteq-one-way,
surjectivity the other). So perp-preservation is automatic, and clause (ii) of
the definition of Aut(L) is redundant given (i): by Steps 3-4 every
order-automorphism is already of the form pi(-), hence already perp-preserving.

**Step 6 (the maps are mutually inverse group homomorphisms).**
Steps 4 and 5 give maps Aut(L) -> Stab(L) and Stab(L) -> Aut(L). Step 4 shows
the composite Aut -> Stab -> Aut is the identity (phi(E)=pi(E) for all E); and
Stab -> Aut -> Stab is the identity because pi is recovered from E|->pi(E) by
its action on singletons. Both respect composition. QED.

## Route 2 (states) -- checked, and strictly weaker

Route 2 as proposed: phi pulls back sigma-additive two-valued states; by
Theorem 5.13 all are Dirac; so delta_omega o phi = delta_{pi(omega)}; unwind.

It DOES work, and the worry raised in the task ("does phi preserve *countable*
orthogonal joins?") dissolves: by Step 1, a countable orthogonal join in a
sigma-class IS the supremum in (L, subseteq), and an order-isomorphism
preserves existing suprema. So the pullback is well-defined. No separate
verification needed. Unwinding: delta_omega o phi is a sigma-additive
two-valued state (phi preserves the relevant joins and perp), hence = delta_p(omega)
for a unique p(omega); then phi(E) = {omega : delta_omega(phi(E))=1}
= {omega : delta_{p(omega)}(E)=1} = p^{-1}(E). Setting pi = p^{-1} recovers
Step 4.

**The informative asymmetry.** Route 2 CONSUMES Theorem 5.13 (rigidity), the
paper's hardest ingredient in this section, and additionally needs to know that
delta_omega o phi is sigma-additive. Route 1 consumes NOTHING but "all
singletons are in L". The routes agree, and the agreement is not the finding --
the finding is that Route 1 proves strictly more (Theorem A above holds for any
concrete orthoposet with singletons, rigid or not), so rigidity is irrelevant
to Claim A. Route 2 is therefore a correct but circuitous proof of a weaker
statement.

## Why MO_2 does not contradict this (and what it shows)

See TASK_C.md, C3: for MO_2, Aut(MO_2, subseteq) has order 24 but the
ORTHOposet automorphism group has order 8.

No contradiction -- but the reason is NOT that MO_2 fails to be atomistic.
MO_2 IS atomistic (four atoms; every element is a sup of atoms). The actual
difference is about what perp does to atoms:

  in MO_2,  perp maps ATOMS to ATOMS   (a |-> a^perp is again an atom);
  in L,     perp maps ATOMS to CO-ATOMS ({omega}^perp = Omega \ {omega}).

That is exactly why the order cannot see the orthocomplementation in MO_2 --
the four atoms are order-theoretically interchangeable, so one is free to
choose which pair up, and 24/8 = 3 counts the three perfect matchings of four
atoms. In L the order pins perp completely.

Equivalently, and this is the cleanest statement of why MO_2 fails Theorem A's
hypothesis: **MO_2 admits no representation as a concrete orthoposet containing
all singletons of its carrier.** If its atoms were {1},{2},{3},{4} on
Omega={1,2,3,4} with perp = set complement, then {1}^perp = {2,3,4} would have
three atoms below it, not one -- contradicting MO_2's height 2.

MO_2 is thus the witness that Step 3 (atomisticity WITH perp = set complement)
is load-bearing rather than decorative.

## Genericity (sharper than first stated)

Step 3 uses only that union_{omega in E} {omega} = E lies in L. It uses no
sigma-closure, no orthomodularity, and -- for the order half -- no perp at all.
So Theorem A holds for **any family L subseteq P(Omega) containing every
singleton and closed under complement**. This strengthens the Task D negative:
the result is not even about sigma-orthoposets, let alone about this carrier.
