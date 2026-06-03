"""
Entry point #3 (concrete/non-concrete boundary) — REFUTATION.

The note `oml_extension_problem.{md,tex}` claims:

  "For concrete (set-representable) OMLs the lattice meet is set
   intersection, so meet-zero coincides with orthogonality, and the
   extension axis reduces to the classical Pitowsky non-contextuality
   problem."

This is FALSE. This script exhibits an explicit, valid concrete logic
(MO_2) containing a pair a,b with:
    a ∧ b = 0  (meet-zero)   but   a ∩ b ≠ ∅  (NOT orthogonal/disjoint).

WHY the claim fails (Burešová–Pták arXiv:2401.13798, Def 1.1):
A set-representable OMP (P, L) requires only:
    (i)   P ∈ L
    (ii)  A ∈ L  ⟹  A' = P∖A ∈ L          (complement closure)
    (iii) A,B ∈ L, A∩B = ∅  ⟹  A∪B ∈ L    (DISJOINT-union closure)
Closure under arbitrary INTERSECTION is NOT required — and demanding it
would force L to be a field of sets, i.e. Boolean. So in a genuinely
non-distributive concrete logic, A∩B need not lie in L.

The lattice meet a∧b is the GREATEST L-member contained in A∩B, hence
    a∧b ⊆ A∩B   always,   with equality  iff  A∩B ∈ L.
Therefore:
    orthogonal (A∩B=∅)  ⟹  meet-zero          [always]
    meet-zero           ⟹̸ orthogonal          [fails for incompatible pairs]

CONSEQUENCE: MO_3 — the note's own flagship counterexample for "meet-zero
≠ orthogonal" — is itself CONCRETE (set-representable; it has 2^3 ordering
two-valued states, Gudder's representation theorem). So the note's two
claims ("meet-zero ≠ orthogonal on MO_3" and "meet-zero = orthogonal on
concretes") are mutually contradictory. The second is the wrong one.

The correct dividing line is NOT concrete vs non-concrete. It is a
RICHNESS / atomicity condition: meet-zero = orthogonal holds iff every
nonempty A∩B (A,B ∈ L) contains a nonzero member of L (sufficient:
all singletons of P lie in L). This property has no established standard
name in the primary literature (cousins: Jauch–Piron, Tkadlec "regional",
"point-distinguishing" — all distinct). MO_2/MO_3 fail it.

Terminology trap: MO_3's famous NON-representability is von Neumann
COORDINATIZATION (not a subspace lattice of a projective geometry) — a
different notion entirely from set-representability. Do not conflate.

Primary source: Burešová–Pták, arXiv:2401.13798, Def 1.1.
Verified independently here by elementary set arithmetic.
"""

# ---- MO_2 as an explicit concrete logic ----
# P = {1,2,3,4};  two independent bipartitions give the two complementary
# atom pairs.  L is the 6-element set-representable OML isomorphic to MO_2.
P = frozenset({1, 2, 3, 4})
L = [
    frozenset(),
    frozenset({1, 2}), frozenset({3, 4}),   # pair 1
    frozenset({1, 3}), frozenset({2, 4}),   # pair 2
    P,
]
Lset = set(L)


def comp(A):
    return P - A


def check_concrete_axioms():
    """Verify (P, L) satisfies the SOMP axioms (Burešová–Pták Def 1.1)."""
    assert P in Lset, "(i) P ∈ L fails"
    assert all(comp(A) in Lset for A in L), "(ii) complement closure fails"
    for A in L:
        for B in L:
            if not (A & B):                       # disjoint
                assert (A | B) in Lset, \
                    f"(iii) disjoint-union closure fails on {set(A)},{set(B)}"
    return True


def meet(A, B):
    """Lattice meet in L = greatest L-member contained in A∩B."""
    below = [C for C in L if C <= A and C <= B]
    return max(below, key=len)            # greatest by inclusion


def main():
    assert check_concrete_axioms()
    print("MO_2 model satisfies the SOMP axioms (i),(ii),(iii). ✓ concrete logic.")

    # The witnessing pair: two atoms from different complementary pairs.
    a, b = frozenset({1, 2}), frozenset({1, 3})
    inter = a & b
    m = meet(a, b)

    orthogonal = (len(inter) == 0)
    meet_zero = (m == frozenset())

    print(f"\na = {tuple(sorted(a))}, b = {tuple(sorted(b))}")
    print(f"  set intersection a∩b = {tuple(sorted(inter))}  (empty: {not inter})")
    print(f"  lattice meet a∧b     = {tuple(sorted(m))}  (= bottom 0: {meet_zero})")
    print(f"  orthogonal (disjoint): {orthogonal}")
    print(f"  meet-zero:             {meet_zero}")

    assert meet_zero and not orthogonal, "expected meet-zero ∧ not-orthogonal"
    print("\nVERDICT: meet-zero holds, orthogonality FAILS in a concrete logic.")
    print("=> 'concrete ⟹ meet-zero = orthogonal' is REFUTED.")

    # The richness condition that actually controls it:
    singletons = [A for A in L if len(A) == 1]
    print(f"\nSingletons in L: {singletons or 'none'} "
          f"-> richness/atomicity condition FAILS (as predicted).")
    print("Under richness (a∩b≠∅ ⟹ some nonzero L-member below both), the")
    print("converse would hold. Plain concreteness does not supply it.")


if __name__ == "__main__":
    main()
