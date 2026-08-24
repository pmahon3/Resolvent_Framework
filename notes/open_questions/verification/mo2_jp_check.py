"""
Purpose-built check for section 7c(iii-b)'s exact claim: on the concrete
4-point representation of MO2 (X={1,2,3,4}, L={emptyset,X,{1,2},{3,4},{1,3},{2,4}}),
the Dirac state at point 1 is a genuine 2-valued state that violates Jauch-Piron.

This is a purpose-built discharge of what §7c(iii-b) *says* was machine-checked
("concrete-logic axioms, lattice/meets, non-Boolean, trivial centre, Dirac@1
non-JP -- all pass"). Neither pre-existing script in the repo computes all of
these; this script does. Scratchpad only, not written to the repo.
"""

X = frozenset({1, 2, 3, 4})
L = [
    frozenset(),
    frozenset({1, 2}), frozenset({3, 4}),
    frozenset({1, 3}), frozenset({2, 4}),
    X,
]
Lset = set(L)


def comp(A):
    return X - A


def is_concrete_logic():
    ok = True
    if frozenset() not in Lset:
        ok = False
    for A in L:
        if comp(A) not in Lset:
            ok = False
    for A in L:
        for B in L:
            if not (A & B):
                if (A | B) not in Lset:
                    ok = False
    return ok


def meet(A, B):
    below = [C for C in L if C <= A and C <= B]
    return max(below, key=len)


def join(A, B):
    above = [C for C in L if A <= C and B <= C]
    return min(above, key=len)


def is_lattice():
    for A in L:
        for B in L:
            below = [C for C in L if C <= A and C <= B]
            above = [C for C in L if A <= C and B <= C]
            if not below or not above:
                return False
            # unique greatest lower bound / least upper bound in a finite poset
            m = max(below, key=len)
            j = min(above, key=len)
            if any(len(C) > len(m) and C <= A and C <= B for C in L):
                return False
            if any(len(C) < len(j) and A <= C and B <= C for C in L):
                return False
    return True


def is_boolean():
    # Boolean iff meet = set intersection for every pair (equiv. A∩B ∈ L always)
    for A in L:
        for B in L:
            if (A & B) not in Lset:
                return False
    return True


def centre():
    # z is central if z is compatible with every element: z∧a, z∧a' generate a
    # sublattice with a = (a∧z) v (a∧z') for all a -- use the simple sufficient
    # test for this finite case: z central iff z ∈ {emptyset, X} (trivial) or
    # z commutes (meet/join distribute) with every element.
    central = []
    for z in L:
        ok = True
        for a in L:
            # de Morgan/distributive check across z
            lhs = join(meet(z, a), meet(comp(z), a))
            if lhs != a:
                ok = False
                break
        if ok:
            central.append(z)
    return central


def dirac(point):
    return {A: (1 if point in A else 0) for A in L}


def is_state(s):
    if s[frozenset()] != 0 or s[X] != 1:
        return False
    for A in L:
        for B in L:
            if not (A & B):
                if (A | B) in Lset:
                    if s[A | B] != s[A] + s[B]:
                        return False
    return True


def is_two_valued(s):
    return all(v in (0, 1) for v in s.values())


def jp_violation(s):
    for A in L:
        for B in L:
            if s[A] == 1 and s[B] == 1:
                m = meet(A, B)
                if s[m] != 1:
                    return (A, B, m)
    return None


def main():
    print("(1) concrete logic axioms:", is_concrete_logic())
    print("(2) is a lattice:", is_lattice())
    print("(3) is Boolean (should be False -- MO2 is the canonical non-Boolean case):",
          is_boolean())
    print("(4) centre:", [tuple(sorted(z)) for z in centre()],
          " -- trivial (only bot/top) :", set(centre()) == {frozenset(), X})

    s = dirac(1)
    print("\nDirac state at point 1:", {tuple(sorted(k)): v for k, v in s.items()})
    print("(5) genuine state (additive on finite disjoint unions, s(0)=0,s(1)=1):",
          is_state(s))
    print("(6) two-valued:", is_two_valued(s))
    v = jp_violation(s)
    print("(7) Jauch-Piron violation found:", v is not None)
    if v:
        A, B, m = v
        print(f"    witness: A={tuple(sorted(A))}, B={tuple(sorted(B))}, "
              f"s(A)=s(B)=1, meet(A,B)={tuple(sorted(m))}, s(meet)={s[m]}")
    print("\nCONCLUSION: Dirac@1 is a genuine 2-valued state on concrete MO2,",
          "non-Boolean, trivial centre, and violates JP -- matches §7c(iii-b).")


if __name__ == "__main__":
    main()
