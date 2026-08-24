#!/usr/bin/env python3
"""Oracle for the B'(i) direct attempt (oml_lattice_regularity_attack.md §11, s15).

Rebuilds the Greechie 5-cycle (pentagon) abstract logic exactly as in
loop5_greechie_oracle.py (§9 oracle), represents it concretely TWICE --
on the full canonical point set Omega = St(L), and on a minimal proper
order-determining subset Omega' < St(L) -- and verifies / refutes the
finite-scale instances of the s15 claims:

  D1  two-block rescue: for every two-valued state mu and every pair of
      blocks (B1, B2), the block-meets E = /\{A in B1 : mu(A)=1} and
      F = /\{A in B2 : mu(A)=1} are elements of L with mu-value 1,
      E cap F is nonempty, and some point of E cap F induces a Dirac
      agreeing with mu on (B1 u B2)'s value-1 part (checked on BOTH reps);
  D2  cluster-reduction bookkeeping: orthomodular monotonicity (A <= B in
      L implies mu(A) <= mu(B) for every state) and in-block
      multiplicativity (mu(A)=mu(B)=1, A,B in a common block implies
      mu(A cap B)=1) (both reps);
  D3  kernel non-FIP witness ON THE REDUCED REP: some sigma-additive state
      nu has three block-kernels (kernel = intersection of nu's value-1
      elements of a block = the charged field atom) with pairwise nonempty
      but empty triple intersection -- so cross-block kernel FIP is NOT
      necessary for sigma-additivity / coherence.  On the canonical rep
      every state is Dirac-at-itself, so this is impossible there BY
      CONSTRUCTION (checked): kernel-emptiness and kernel-FIP-failure are
      properties of the representation, measuring the gap Omega < St_sigma;
  D4  empty-kernel coherent pattern ON THE REDUCED REP: some state mu has
      three value-1 elements A1,A2,A3 with A1 cap A2 cap A3 = 0 (pairwise
      nonempty forced by disjoint-additivity), no Dirac extends the
      pattern, and mu itself -- sigma-additive, the carrier being finite --
      does: a non-Dirac rescue at the >=3-block frontier.  Impossible on
      the canonical rep (checked);
  D5  pointedness: every state charges a field atom of every block --
      finite shadow of "sigma-additive iff blockwise pointed" for countably
      generated blocks (T3 + converse + A1c) (both reps).

Pure stdlib. Exit code 0 iff all checks land as asserted in §11.
"""

from itertools import combinations, product
import sys

N = 5  # pentagon


def build_abstract():
    blocks_a = [frozenset({2 * i, 2 * i + 1, (2 * i + 2) % (2 * N)})
                for i in range(N)]
    n_atoms = 2 * N

    def share_block(i, j):
        return i != j and any(i in b and j in b for b in blocks_a)

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
            return share_block(x[1], y[1])
        return False

    states = []
    for bits in product((0, 1), repeat=n_atoms):
        if all(sum(bits[a] for a in b) == 1 for b in blocks_a):
            states.append(bits)

    def val(s, x):
        if x == ZERO:
            return 0
        if x == ONE:
            return 1
        return s[x[1]] if x[0] == 'a' else 1 - s[x[1]]

    return elements, le, states, val


def represent(elements, le, states, val, points):
    """Concrete rep on the state-index subset `points`; None if not an
    order-determining injective order-iso."""
    for x in elements:
        for y in elements:
            if not le(x, y) and not any(
                    val(states[i], x) == 1 and val(states[i], y) == 0
                    for i in points):
                return None
    X = frozenset(points)
    Im = {x: frozenset(i for i in points if val(states[i], x) == 1)
          for x in elements}
    fam = set(Im.values())
    if len(fam) != len(elements):
        return None
    if not all((Im[x] <= Im[y]) == le(x, y)
               for x in elements for y in elements):
        return None

    def compat(A, B):
        return (A & B) in fam

    compat_pairs = {(A, B) for A in fam for B in fam if compat(A, B)}
    cliques = set()

    def extend(S, cand):
        ext = [A for A in cand if all((A, B) in compat_pairs for B in S)]
        if not ext:
            cliques.add(frozenset(S))
            return
        for A in ext:
            extend(S | {A}, [B for B in ext if B != A])

    extend(set(), sorted(fam, key=lambda A: (len(A), sorted(A))))
    blocks = [c for c in cliques if not any(c < d for d in cliques)]

    # all two-valued (finitely additive = sigma-additive, finite) states of
    # the abstract logic, transported to the representation
    mus = [{Im[x]: val(s, x) for x in elements} for s in states]
    return X, fam, blocks, mus


def inter(X, sets):
    out = X
    for A in sets:
        out = out & A
    return out


def check_rep(tag, X, fam, blocks, mus, results, details):
    # D1
    d1, n_cases = True, 0
    for mu in mus:
        for B1, B2 in combinations(blocks, 2):
            V1 = [A for A in B1 if mu[A] == 1]
            V2 = [A for A in B2 if mu[A] == 1]
            E, F = inter(X, V1), inter(X, V2)
            n_cases += 1
            if E not in fam or F not in fam:
                d1 = False; details.append(f"{tag} D1: block-meet not in L")
            elif mu[E] != 1 or mu[F] != 1:
                d1 = False; details.append(f"{tag} D1: block-meet not value 1")
            elif not (E & F):
                d1 = False; details.append(f"{tag} D1: E cap F empty")
            else:
                V = set(V1) | set(V2)
                if not any(all(w in A for A in V) for w in E & F):
                    d1 = False
                    details.append(f"{tag} D1: no Dirac point in E cap F")
    results[f'D1 {tag} two-block rescue ({n_cases} cases)'] = d1

    # D2
    d2 = True
    for mu in mus:
        for A in fam:
            for B in fam:
                if A <= B and mu[A] > mu[B]:
                    d2 = False
        for blk in blocks:
            for A, B in combinations(blk, 2):
                if mu[A] == 1 and mu[B] == 1 and mu[A & B] != 1:
                    d2 = False
    results[f'D2 {tag} monotonicity + multiplicativity'] = d2

    # D5 (+ kernels for D3/D4)
    def kernel(mu, blk):
        return inter(X, [A for A in blk if mu[A] == 1])

    d5 = True
    for mu in mus:
        for blk in blocks:
            if not kernel(mu, blk):
                d5 = False
    results[f'D5 {tag} every state blockwise pointed'] = d5

    # D3
    d3_witness = None
    for mu in mus:
        kers = [kernel(mu, blk) for blk in blocks]
        for K1, K2, K3 in combinations(kers, 3):
            if (K1 & K2) and (K1 & K3) and (K2 & K3) and not (K1 & K2 & K3):
                d3_witness = (K1, K2, K3)
                break
        if d3_witness:
            break

    # D4
    d4_witness = None
    for mu in mus:
        ones = [A for A in fam if mu[A] == 1 and A != X]
        for A1, A2, A3 in combinations(ones, 3):
            if not (A1 & A2 & A3) and (A1 & A2) and (A1 & A3) and (A2 & A3):
                if not any(all(w in A for A in (A1, A2, A3)) for w in X):
                    d4_witness = (mu, (A1, A2, A3))
                    break
        if d4_witness:
            break
    return d3_witness, d4_witness


def main():
    elements, le, states, val = build_abstract()
    all_idx = list(range(len(states)))

    results, details = {}, []

    # canonical rep: Omega = all states
    rep = represent(elements, le, states, val, all_idx)
    assert rep is not None, "canonical rep must exist"
    X, fam, blocks, mus = rep
    print(f"canonical: |Omega|={len(X)} |L|={len(fam)} blocks={len(blocks)} "
          f"states={len(mus)}")
    d3c, d4c = check_rep('canon', X, fam, blocks, mus, results, details)
    results['D3 canon: kernel non-FIP impossible (all Dirac)'] = d3c is None
    results['D4 canon: empty-kernel pattern impossible (all Dirac)'] = d4c is None

    # reduced rep: greedily drop states while order-determining
    points = list(all_idx)
    for i in all_idx:
        trial = [p for p in points if p != i]
        if represent(elements, le, states, val, trial) is not None:
            points = trial
    rep2 = represent(elements, le, states, val, points)
    assert rep2 is not None
    X2, fam2, blocks2, mus2 = rep2
    dropped = sorted(set(all_idx) - set(points))
    print(f"reduced:   |Omega'|={len(X2)} (dropped states {dropped}) "
          f"|L|={len(fam2)} blocks={len(blocks2)} states={len(mus2)}")
    d3r, d4r = check_rep('reduced', X2, fam2, blocks2, mus2, results, details)
    results['D3 reduced: kernel non-FIP witness exists'] = d3r is not None
    results['D4 reduced: empty-kernel coherent pattern exists'] = d4r is not None
    if d3r:
        details.append(f"D3 witness kernel sizes {[len(k) for k in d3r]}")
    if d4r:
        mu, tri = d4r
        details.append(f"D4 pattern sets sizes {[len(a) for a in tri]}; "
                       f"rescuing state is non-Dirac on Omega'")

    ok = all(results.values())
    for k, v in results.items():
        print(f"  {'PASS' if v else 'FAIL'}  {k}")
    for d in details[:12]:
        print(f"  note: {d}")
    print('ALL CHECKS AS ASSERTED IN §11' if ok else 'DISCREPANCY -- fix the note')
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
