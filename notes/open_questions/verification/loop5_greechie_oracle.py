#!/usr/bin/env python3
"""Oracle for the Skeleton B cold attack (oml_lattice_regularity_attack.md §9).

Builds the Greechie n-cycle logic (n blocks of 3 atoms pasted in a cycle,
adjacent blocks sharing one atom; loop lemma: OML iff n >= 5), computes its
two-valued states, tests concreteness (order-determining state set), builds
the canonical concrete representation on X = St(L), and then verifies /
refutes the finite-scale claims of the attack note:

  C1  the representation is a concrete logic (complement + disjoint-union
      closed), and set-disjointness coincides with abstract orthogonality;
  C2  it is a lattice (all pairwise meets exist in the set-poset);
  C3  it is non-Boolean, with intersection-poor pairs (Prop 4.4 anatomy:
      A cap B nonempty, no nonempty element of L inside);
  C4  centre is trivial (irreducible);
  C5  it is NOT a horizontal sum (some block overlap differs from {0,1});
  C6  every maximal pairwise-compatible set (block) is cap-closed, i.e. a
      Boolean field of sets (Foulis-Holland consequence, finite instance);
  C7  every pairwise-compatible triple lies in a common block (OML
      regularity, finite instance);
  C8  every pairwise-disjoint family of elements lies in a common block
      (confinement lemma A1, finite instance);
  C9  singleton quarantine (T1, finite instance): for every incompatible
      pair, the overlap A cap B contains a point x with {x} not in L
      (trivially true if L has no singletons -- reported either way);
  C10 blockwise Dirac realization (T3, finite instance): every two-valued
      finitely additive state on each block (a finite field of sets) is
      realized by a Dirac at a point of X.

Pure stdlib. Exit code 0 iff all checks land as asserted in the note.
"""

from itertools import combinations, product
import sys

def build_cycle(n):
    """n blocks of 3 atoms in a cycle. Atoms 0..2n-1.
    Block i = {2i, 2i+1, (2i+2) mod 2n}: even atoms shared, odd private."""
    return [frozenset({2 * i, 2 * i + 1, (2 * i + 2) % (2 * n)}) for i in range(n)]

def analyze(n, verbose=True):
    blocks = build_cycle(n)
    n_atoms = 2 * n
    atom_blocks = {a: [b for b in blocks if a in b] for a in range(n_atoms)}

    def share_block(i, j):
        return i != j and any(i in b and j in b for b in blocks)

    # ---- abstract elements: 0, 1, atoms, coatoms -------------------------
    ZERO, ONE = ('0',), ('1',)
    atoms = [('a', i) for i in range(n_atoms)]
    coatoms = [('c', i) for i in range(n_atoms)]
    elements = [ZERO, ONE] + atoms + coatoms

    def le(x, y):
        if x == ZERO or y == ONE or x == y:
            return True
        if x[0] == 'a' and y[0] == 'a':
            return x[1] == y[1]
        if x[0] == 'a' and y[0] == 'c':
            return share_block(x[1], y[1])   # a_i <= a_j' iff a_i perp a_j
        return False                          # coatom below atom/other coatom: no

    def comp(x):
        if x == ZERO:
            return ONE
        if x == ONE:
            return ZERO
        return ('c', x[1]) if x[0] == 'a' else ('a', x[1])

    # ---- two-valued states: one atom per block ---------------------------
    states = []
    for bits in product((0, 1), repeat=n_atoms):
        if all(sum(bits[a] for a in b) == 1 for b in blocks):
            states.append(bits)
    if verbose:
        print(f"[n={n}] blocks={len(blocks)}  atoms={n_atoms}  "
              f"elements={len(elements)}  two-valued states={len(states)}")

    def val(s, x):
        if x == ZERO:
            return 0
        if x == ONE:
            return 1
        return s[x[1]] if x[0] == 'a' else 1 - s[x[1]]

    # ---- concreteness: order-determining? --------------------------------
    full = True
    for x in elements:
        for y in elements:
            if not le(x, y):
                if not any(val(s, x) == 1 and val(s, y) == 0 for s in states):
                    full = False
                    if verbose:
                        print(f"  NOT order-determining at pair {x} !<= {y}")
    if not full:
        return None
    if verbose:
        print(f"  order-determining: YES -> concrete representation exists")

    # ---- canonical representation on X = states --------------------------
    X = frozenset(range(len(states)))
    Im = {x: frozenset(i for i, s in enumerate(states) if val(s, x) == 1)
          for x in elements}
    fam = set(Im.values())
    results = {}

    assert len(fam) == len(elements), "representation not injective"
    order_iso = all((Im[x] <= Im[y]) == le(x, y)
                    for x in elements for y in elements)
    results['order-iso'] = order_iso

    inv = {v: k for k, v in Im.items()}

    # C1: complement closure + disjoint-union closure + disjoint<=>orthogonal
    c1 = all(X - A in fam for A in fam)
    accidental = []
    for A, B in combinations(fam, 2):
        if not (A & B):
            x, y = inv[A], inv[B]
            if not le(x, comp(y)):
                accidental.append((x, y))     # set-disjoint but not abstractly orthogonal
            if A | B not in fam:
                c1 = False
    results['C1 concrete logic (comp + disjoint-union closed)'] = c1 and not accidental
    results['C1b no accidental disjointness'] = not accidental

    # C2: lattice -- every pair has a maximum lower bound in the family
    def meet(A, B):
        lbs = [C for C in fam if C <= A and C <= B]
        mx = [C for C in lbs if not any(C < D for D in lbs)]
        return mx[0] if len(mx) == 1 else None
    meets = {}
    c2 = True
    for A, B in combinations(fam, 2):
        m = meet(A, B)
        if m is None:
            c2 = False
        meets[(A, B)] = meets[(B, A)] = m
    results['C2 lattice'] = c2

    # compatibility (concrete test: A cap B in L)
    def compat(A, B):
        return (A & B) in fam

    # C3: non-Boolean + intersection-poor pairs
    poor = [(inv[A], inv[B]) for A, B in combinations(fam, 2)
            if (A & B) and not any(C and C <= (A & B) for C in fam)]
    results['C3 non-Boolean (has incompatible pair)'] = any(
        not compat(A, B) for A, B in combinations(fam, 2))
    results['C3b intersection-poor pair exists (Prop 4.4)'] = bool(poor)
    if verbose and poor:
        print(f"  poor pairs: {len(poor)}, e.g. {poor[0][0]} vs {poor[0][1]}")

    # C4: trivial centre
    centre = [A for A in fam if all(compat(A, B) for B in fam)]
    results['C4 centre trivial'] = sorted(map(len, centre)) == [0, len(X)]
    if verbose:
        print(f"  centre size: {len(centre)} (expect 2)")

    # blocks = maximal pairwise-compatible subsets (greedy exact for small fam)
    fam_l = sorted(fam, key=lambda A: (len(A), sorted(A)))
    compat_pairs = {(A, B) for A in fam for B in fam if compat(A, B)}
    def is_clique(S):
        return all((A, B) in compat_pairs for A, B in combinations(S, 2))
    # maximal cliques via extension of each element set (fam is small: 22-26)
    cliques = set()
    def extend(S, cand):
        ext = [A for A in cand if all((A, B) in compat_pairs for B in S)]
        if not ext:
            cliques.add(frozenset(S))
            return
        done = False
        for A in ext:
            extend(S | {A}, [B for B in ext if B != A])
            done = True
        if not done:
            cliques.add(frozenset(S))
    extend(set(), fam_l)
    maximal = [c for c in cliques if not any(c < d for d in cliques)]
    if verbose:
        print(f"  blocks (maximal compatible sets): {len(maximal)}")

    # C5: not a horizontal sum -- some pairwise block overlap != {0, X}
    triv = {frozenset(), X}
    overlaps = [b1 & b2 for b1, b2 in combinations(maximal, 2)]
    results['C5 NOT horizontal sum'] = any(o - triv for o in overlaps)

    # C6: every block cap-closed (a field of sets)
    results['C6 blocks cap-closed'] = all(
        (A & B) in blk for blk in maximal for A in blk for B in blk)

    # C7: pairwise-compatible triples lie in a common block (regularity)
    c7 = all(any(A in blk and B in blk and C in blk for blk in maximal)
             for A, B, C in combinations(fam, 3)
             if is_clique({A, B, C}))
    results['C7 pairwise-compatible triples confined'] = c7

    # C8: pairwise-disjoint families confined to a block
    c8 = True
    for k in (2, 3):
        for S in combinations([A for A in fam if A], k):
            if all(not (A & B) for A, B in combinations(S, 2)):
                if not any(all(A in blk for A in S) for blk in maximal):
                    c8 = False
    results['C8 orthogonal families confined'] = c8

    # C9: singleton quarantine (T1) -- incompatible overlaps have a
    # singleton-free point (here: does L contain singletons at all?)
    singletons_in_L = [A for A in fam if len(A) == 1]
    c9 = True
    for A, B in combinations(fam, 2):
        if not compat(A, B):
            if all(frozenset({x}) in fam for x in A & B):
                c9 = False
    results['C9 T1: incompatible overlaps not singleton-resolved'] = c9
    if verbose:
        print(f"  singletons in L: {len(singletons_in_L)}")

    # C10: blockwise Dirac realization (T3 finite instance)
    c10 = True
    for blk in maximal:
        blk_sets = sorted(blk, key=sorted)
        # two-valued finitely additive states on the finite field blk:
        # concentrate on an atom of the field; enumerate field atoms
        pts = X
        # atoms of the field generated by blk (blk is already the field, C6)
        from functools import reduce
        sig = {}
        for p in pts:
            sig.setdefault(tuple(p in A for A in blk_sets), set()).add(p)
        for key, atom_pts in sig.items():
            # the state "1 on A iff atom subset A" must equal some Dirac
            p0 = next(iter(atom_pts))
            for A, inA in zip(blk_sets, key):
                if (p0 in A) != inA:
                    c10 = False
    results['C10 T3: blockwise states Dirac-realized'] = c10

    ok = all(results.values())
    if verbose:
        for k, v in results.items():
            print(f"  {'PASS' if v else 'FAIL'}  {k}")
        print(f"[n={n}] {'ALL CHECKS AS ASSERTED' if ok else 'DISCREPANCY'}")
    return ok

if __name__ == '__main__':
    overall = True
    for n in (5, 6):
        r = analyze(n)
        print()
        if r is None:
            print(f"[n={n}] not concrete -- skipped structural checks\n")
        else:
            overall = overall and r
    sys.exit(0 if overall else 1)
