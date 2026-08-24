#!/usr/bin/env python3
"""Pentagon (Greechie 5-cycle) core machinery for the s15 adversarial
proof-read.  Written FROM SCRATCH from the statements file alone; no
repository code consulted or reused.

Abstract logic: 0, 1, atoms a0..a9, coatoms a0'..a9'.
Blocks Bl_i = <a_{2i}, a_{2i+1}, a_{(2i+2) mod 10}>, i = 0..4, each = 2^3,
adjacent blocks sharing one (even-indexed) atom.
Two-valued states = one atom per block, consistently.
Concrete rep on a set Omega of two-valued states: A |-> {s in Omega : s(A)=1}.
"""
from itertools import combinations, product

BLOCK_ATOMS = [frozenset({2 * i, 2 * i + 1, (2 * i + 2) % 10}) for i in range(5)]


def all_states():
    """All two-valued states, as frozensets of value-1 atoms.

    A state's even-atom part is an independent set in the 5-cycle
    (a_{2i} and a_{2i+2} share block i); each uncovered block takes its
    private odd atom a_{2i+1}."""
    out = []
    for r in range(3):
        for pos in combinations(range(5), r):  # chosen even atoms a_{2i}, i in pos
            if any(((b - a) % 5) in (1, 4) for a in pos for b in pos if a != b):
                continue  # adjacent evens share a block: not a state
            T = {2 * i for i in pos}
            for i in range(5):
                if not (T & BLOCK_ATOMS[i]):
                    T.add(2 * i + 1)
            for i in range(5):
                assert len(T & BLOCK_ATOMS[i]) == 1, 'exactly one atom per block'
            out.append(frozenset(T))
    assert len(out) == len(set(out)) == 11, 'pentagon has 11 two-valued states'
    return sorted(out, key=sorted)


STATES = all_states()
S_EMPTY = frozenset({1, 3, 5, 7, 9})  # the all-odd state (no even atom chosen)
assert S_EMPTY in STATES

SYMBOLS = ([('zero',), ('one',)]
           + [('atom', i) for i in range(10)]
           + [('coatom', i) for i in range(10)])


def sval(sym, T):
    """Value of the abstract two-valued state T on the symbol sym."""
    if sym[0] == 'zero':
        return 0
    if sym[0] == 'one':
        return 1
    if sym[0] == 'atom':
        return 1 if sym[1] in T else 0
    return 0 if sym[1] in T else 1  # coatom


def img(sym, Omega):
    return frozenset(T for T in Omega if sval(sym, T))


# Abstract order := the order determined by ALL 11 states.  check_canonical
# verifies independently that under this order the canonical rep is a
# concrete sigma-class OML with the advertised block structure; that check
# grounds the use of CANON as "the" pentagon order.
CANON = {sym: img(sym, STATES) for sym in SYMBOLS}


def leq_abs(x, y):
    return CANON[x] <= CANON[y]


def inter(sets, U):
    """Intersection of a finite family of subsets of U (= U if empty)."""
    out = set(U)
    for X in sets:
        out &= X
    return frozenset(out)


class Rep:
    """A candidate concrete representation on Omega (a subset of STATES)."""

    def __init__(self, Omega):
        self.U = frozenset(Omega)
        self.imgs = {sym: img(sym, self.U) for sym in SYMBOLS}
        self.F = sorted(set(self.imgs.values()),
                        key=lambda X: (len(X), sorted(sorted(t) for t in X)))

    # -- validity: order-isomorphism onto image + image family is a
    #    concrete sigma-class OML (checked directly from the definitions) --
    def valid(self):
        m = self.imgs
        if len(set(m.values())) != len(SYMBOLS):
            return False, 'not injective'
        for x in SYMBOLS:
            mx = m[x]
            for y in SYMBOLS:
                if (mx <= m[y]) != leq_abs(x, y):
                    return False, 'order not preserved and reflected'
        F, U = set(self.F), self.U
        if frozenset() not in F or U not in F:
            return False, 'missing 0 or 1'
        for X in F:
            if (U - X) not in F:
                return False, 'not complement-closed'
        for X in F:
            for Y in F:
                if not (X & Y) and (X | Y) not in F:
                    return False, 'not disjoint-union closed'
        # lattice + orthomodular law, checked concretely
        for X in self.F:
            for Y in self.F:
                if self.meet(X, Y) is None or self.join(X, Y) is None:
                    return False, 'not a lattice'
        for X in self.F:
            for Y in self.F:
                if X <= Y:
                    Z = self.meet(Y, U - X)
                    if Z is None or self.join(X, Z) != Y:
                        return False, 'orthomodular law fails'
        return True, 'ok'

    def meet(self, X, Y):
        lbs = [Z for Z in self.F if Z <= X and Z <= Y]
        g = max(lbs, key=len)
        return g if all(Z <= g for Z in lbs) else None

    def join(self, X, Y):
        ubs = [Z for Z in self.F if X <= Z and Y <= Z]
        l = min(ubs, key=len)
        return l if all(l <= Z for Z in ubs) else None

    def compat(self, X, Y):
        """A <-> B iff A = (A ^ B) v (A ^ Bc)  (definition in the task file)."""
        U = self.U
        mXY, mXYc = self.meet(X, Y), self.meet(X, U - Y)
        if mXY is None or mXYc is None:
            return False
        j = self.join(mXY, mXYc)
        return j == X

    def compat_table(self):
        F = self.F
        return {(X, Y): self.compat(X, Y) for X in F for Y in F}

    def blocks(self):
        """Maximal pairwise-compatible subsets of F (maximal cliques),
        via Bron--Kerbosch with pivoting."""
        F = self.F
        ct = self.compat_table()
        adj = {X: frozenset(Y for Y in F if Y != X and ct[(X, Y)] and ct[(Y, X)])
               for X in F}
        cliques = []

        def bk(R, P, Xx):
            if not P and not Xx:
                cliques.append(frozenset(R))
                return
            piv = max(P | Xx, key=lambda v: len(adj[v] & P))
            for v in list(P - adj[piv]):
                bk(R | {v}, P & adj[v], Xx & adj[v])
                P = P - {v}
                Xx = Xx | {v}

        bk(set(), set(F), set())
        return sorted(cliques, key=lambda B: sorted(len(X) for X in B))

    @staticmethod
    def block_atoms(B):
        """Minimal nonempty elements of a block (as a family of sets)."""
        return [X for X in B if X and not any(Y and Y < X for Y in B)]

    def fa_states(self):
        """ALL two-valued f.a. states on the family F, enumerated
        exhaustively: mu(U)=1 and, for EVERY pairwise-disjoint subfamily
        with union in F, additivity holds.  (Omega finite, so sigma- and
        finite additivity coincide: any countable disjoint family has only
        finitely many distinct nonempty members and mu(empty)=0.)

        Exhaustiveness of the parametrization: any f.a. state must satisfy
        mu(X) + mu(U-X) = mu(U) = 1 (X and U-X are disjoint with union U in
        F), which forces coatom values from atom values, mu(empty)=0 and
        mu(U)=1; so ranging over the 2^10 atom-value vectors covers every
        candidate."""
        F, U = self.F, self.U
        Fset = set(F)
        nz = [X for X in F if X]
        cons = []

        def rec(start, chosen, un):
            if len(chosen) >= 2 and un in Fset:
                cons.append((tuple(chosen), un))
            for i in range(start, len(nz)):
                Xi = nz[i]
                if un & Xi:
                    continue
                rec(i + 1, chosen + [Xi], un | Xi)

        rec(0, [], frozenset())
        ai = [self.imgs[('atom', i)] for i in range(10)]
        ci = [self.imgs[('coatom', i)] for i in range(10)]
        out = []
        for bits in product((0, 1), repeat=10):
            mu = {frozenset(): 0, U: 1}
            ok = True
            for i in range(10):
                mu[ai[i]] = bits[i]
                mu[ci[i]] = 1 - bits[i]
            for G, u in cons:
                if sum(mu[X] for X in G) != mu[u]:
                    ok = False
                    break
            if ok:
                out.append(mu)
        return out


def dirac(rep, w):
    """delta_w as a map on the family."""
    return {X: (1 if w in X else 0) for X in rep.F}


def induced_state(rep, T):
    """The map on the family induced by the ABSTRACT state T (which need
    not lie in rep.U).  Well-defined because rep is injective on symbols."""
    return {rep.imgs[sym]: sval(sym, T) for sym in SYMBOLS}
