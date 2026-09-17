# Working notes: Aut of the product Ulam carrier
(scratch; verdicts consolidated in AUT_LEDGER.md)

## Step check: is id_M x tau in Aut(L) for all tau in Sym(F)?
pi = id x tau is a bijection of Omega. Need pi(L)=L.
Generators of L: singletons, cells D_{a,n}=C_{a,n} x F, cores A_i.
- pi(singleton) = singleton. OK.
- pi(D_{a,n}) = C_{a,n} x tau(F) = C_{a,n} x F = D_{a,n}. FIXED POINTWISE as a set. OK.
- pi(A_i) = M x tau(supp A_i), a weight-2 fibre set, which IS in L (six weight-2
  fibre sets all in L: three cores + three core complements).
Since pi is a bijection, pi preserves complements and disjoint unions, so
pi(L) is a sigma-class containing the generators => L subseteq pi(L); same for
pi^{-1} => equality.
=> Sym(F) = S_4 (order 24) embeds in Aut(L) via tau |-> id x tau.
This REFUTES the "S_3 fixing fibre 4" clause of Conjecture B.

## Step check: countably-supported permutations (refutes product form, B4)
Let pi in Sym(Omega) move only points inside a COUNTABLE set N subseteq Omega
(pi = id off N, pi(N)=N). For any E in L:
  pi(E) Delta E subseteq N, countable.
By Lemma 5.3(3) (countable perturbation) pi(E) = (E \ (E Delta pi(E))) u (pi(E)\E)
is in L. Same for pi^{-1}. So pi(L)=L: pi in Aut(L).
Concrete witness: pi = transposition of (alpha0,1) and (alpha0,2) for any
alpha0 in M. Support size 2. NOT of the form sigma x tau (it moves the fibre
coordinate at one M-point only).
=> "product form (sigma,tau)" is REFUTED as stated. Product form can hold at
most MODULO the countable ideal, and B4's "derive it or exhibit a mixing
example" is answered by the example.

Note this also shows Aut(L) is NOT countable and contains Sym(N) for every
countable N subseteq Omega -- a large "local" subgroup, in fact the group of
all permutations with countable support, which is a normal subgroup? Check:
conjugating a countable-support permutation by any pi in Aut(L) gives a
countable-support permutation (support maps to support). YES, normal.
