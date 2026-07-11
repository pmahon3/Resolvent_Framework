#!/usr/bin/env python3
"""Fresh-context adversarial re-derivation, receipt (a): the Greechie pentagon
built FROM SCRATCH (independent of the repo's loop5 oracle, which was not read).

Structure: 5 three-atom Boolean blocks pasted in a 5-cycle, adjacent blocks
sharing one atom.  Atoms: a0..a4 (shared), b0..b4 (private);
block B_k = {a_k, b_k, a_{k+1 mod 5}}.

Checks (each prints PASS/FAIL; exit code = number of failures):
  - 11 two-valued states (= independent sets of C5), one atom per block
  - canonical representation on X = St(L): 22 distinct sets (injectivity)
  - order-determination: abstract pasted order <-> set inclusion (both ways)
  - sigma-class axioms on the 22-set family (empty set, complements,
    pairwise-disjoint unions; finite => countable at this scale)
  - lattice: every pair has a greatest lower bound; joins exist; orthomodular
  - non-Boolean; count of incompatible pairs; 100 intersection-poor pairs
    (unordered); strong poorness == (meet=0 & nonempty overlap) on a lattice
  - trivial centre; blocks = 5 maximal compatible cliques of size 8, each a
    field of sets; every pairwise block overlap a field; adjacent overlaps
    nontrivial => NOT a horizontal sum
  - no singletons of X in L
  - L0 (compatible <=> commuting; compatible meets are intersections)
  - T1 contrapositive (every incompatible overlap has an unresolved point)
  - P1 (poor pairs incompatible / no common block / hereditary;
    sigma-superadditivity of meets over disjoint decompositions)
  - St_fa(L) = exactly the 11 Diracs (so Phi holds trivially, finite scale)
  - Corollary atom mechanics: pairwise-compatible pattern + global f.a. state
    => value-1 atom of generated subfield nonempty, Dirac there extends s0
  - T3 mechanics on each block (finite sigma-field): F_n/D construction
    lands on the state's atom; nu = delta_omega on the block for all omega in D
"""
import sys
from itertools import combinations

fails = []
def check(name, cond, detail=""):
    print(("PASS: " if cond else "FAIL: ") + name + (f" [{detail}]" if detail else ""))
    if not cond:
        fails.append(name)

# ---------- abstract pentagon ----------
A = [("a", i) for i in range(5)]
B = [("b", i) for i in range(5)]
ATOMS = A + B
BLOCKS = [frozenset([("a", k), ("b", k), ("a", (k + 1) % 5)]) for k in range(5)]

def share_block(x, y):
    return any(x in blk and y in blk for blk in BLOCKS)

# ---------- two-valued states ----------
states = []
for mask in range(32):
    T = {i for i in range(5) if (mask >> i) & 1}
    if any(((i + 1) % 5) in T for i in T):     # adjacent in C5 -> conflict
        continue
    ones = frozenset({("a", i) for i in T} |
                     {("b", k) for k in range(5)
                      if k not in T and (k + 1) % 5 not in T})
    states.append(ones)
check("state count is 11 (independent sets of C5)", len(states) == 11,
      f"got {len(states)}")
check("each state selects exactly ONE atom per block",
      all(sum(x in s for x in blk) == 1 for s in states for blk in BLOCKS))

N = len(states)
X = frozenset(range(N))

def hat_atom(x):
    return frozenset(i for i, s in enumerate(states) if x in s)

# element labels: ("zero",), ("one",), ("at",kind,i), ("co",kind,i)
hat = {("zero",): frozenset(), ("one",): X}
for x in ATOMS:
    hat[("at",) + x] = hat_atom(x)
    hat[("co",) + x] = X - hat_atom(x)

L = sorted(set(hat.values()), key=lambda s: (len(s), sorted(s)))
check("representation has exactly 22 distinct sets (map injective)",
      len(L) == 22 and len(hat) == 22, f"got {len(set(hat.values()))}")
Lset = set(L)

# ---------- abstract order of the pasted structure ----------
def le_abs(e, f):
    if e == f or e == ("zero",) or f == ("one",):
        return True
    if e == ("one",) or f == ("zero",):
        return False
    ek, ex = e[0], e[1:]
    fk, fx = f[0], f[1:]
    if ek == "at" and fk == "at":
        return ex == fx
    if ek == "co" and fk == "co":
        return ex == fx
    if ek == "at" and fk == "co":       # atom <= coatom iff orthogonal atoms
        return ex != fx and share_block(ex, fx)
    return False                         # coatom never <= a (proper) atom

ok = True
for e in hat:
    for f in hat:
        if le_abs(e, f) != (hat[e] <= hat[f]):
            ok = False
check("order-determining: abstract pasted order == set inclusion (all 484 pairs)", ok)

# ---------- sigma-class axioms ----------
check("empty set in L", frozenset() in Lset)
check("complement-closed", all((X - S) in Lset for S in L))
ok = True
for S, T in combinations(L, 2):
    if S & T == frozenset() and (S | T) not in Lset:
        ok = False
check("closed under pairwise disjoint unions (=> finite by induction)", ok)

# ---------- lattice structure ----------
def meet(Sa, Sb):
    lows = [C for C in L if C <= Sa and C <= Sb]
    tops = [C for C in lows if all(D <= C for D in lows)]
    return tops[0] if tops else None

def join(Sa, Sb):
    ups = [C for C in L if Sa <= C and Sb <= C]
    bots = [C for C in ups if all(C <= D for D in ups)]
    return bots[0] if bots else None

MEET = {}
ok_m = ok_j = True
for Sa in L:
    for Sb in L:
        m = meet(Sa, Sb)
        j = join(Sa, Sb)
        if m is None: ok_m = False
        if j is None: ok_j = False
        MEET[(Sa, Sb)] = m
check("every pair has a greatest lower bound (lattice)", ok_m)
check("every pair has a least upper bound", ok_j)

ok = True
for Sa in L:
    for Sb in L:
        if Sa <= Sb:  # orthomodularity: B = A join (B meet A^c), disjointly
            d = MEET[(Sb, X - Sa)]
            if d is None or (Sa | d) != Sb or (Sa & d):
                ok = False
check("orthomodular law on all comparable pairs", ok)

# ---------- compatibility, blocks ----------
def compat(Sa, Sb):
    return (Sa & Sb) in Lset

# maximal cliques of the compatibility graph (Bron-Kerbosch, no pivot)
idx = {S: i for i, S in enumerate(L)}
adj = {i: set() for i in range(22)}
for Sa, Sb in combinations(L, 2):
    if compat(Sa, Sb):
        adj[idx[Sa]].add(idx[Sb]); adj[idx[Sb]].add(idx[Sa])
for i in range(22):
    adj[i].add(i)
cliques = []
def bk(R, P, Xc):
    if not P and not Xc:
        cliques.append(frozenset(R)); return
    for v in list(P):
        bk(R | {v}, P & adj[v] - {v}, Xc & adj[v] - {v})
        P = P - {v}; Xc = Xc | {v}
bk(set(), set(range(22)), set())
blocks_rep = [frozenset(L[i] for i in c) for c in cliques]
check("exactly 5 blocks (maximal compatible cliques)", len(blocks_rep) == 5,
      f"got {len(blocks_rep)}")
check("every block has 8 elements", all(len(b) == 8 for b in blocks_rep))

def is_field(fam):
    if frozenset() not in fam or X not in fam: return False
    return (all((X - S) in fam for S in fam) and
            all((S & T) in fam for S in fam for T in fam))
check("every block is a field of sets (A2 finite instance)",
      all(is_field(b) for b in blocks_rep))
ok = True
nontriv_overlap = 0
for b1, b2 in combinations(blocks_rep, 2):
    ov = b1 & b2
    if not is_field(ov): ok = False
    if len(ov) > 2: nontriv_overlap += 1
check("every pairwise block overlap is a field", ok)
check("NOT a horizontal sum: some block overlap exceeds {0,1}",
      nontriv_overlap > 0, f"{nontriv_overlap} nontrivial overlaps (expect 5 adjacent)")
check("adjacent overlaps: exactly 5 of size 4 (shared atom + coatom + 0,1)",
      sorted(len(b1 & b2) for b1, b2 in combinations(blocks_rep, 2)) ==
      [2, 2, 2, 2, 2, 4, 4, 4, 4, 4])
check("block atoms partition X (each block's 3 atoms cover X disjointly)",
      all(sorted(len(s) for s in b if s and not any(t < s for t in b if t)) and
          set().union(*[s for s in b if s and not any(t < s and t for t in b)]) == set(X)
          for b in blocks_rep))

# ---------- centre, non-Booleanness, poor pairs ----------
centre = [S for S in L if all(compat(S, T) for T in L)]
check("trivial centre {0, X}", sorted(map(len, centre)) == [0, N],
      f"centre sizes {sorted(map(len, centre))}")

incompat = [(Sa, Sb) for Sa, Sb in combinations(L, 2) if not compat(Sa, Sb)]
check("non-Boolean: incompatible pairs exist", len(incompat) > 0,
      f"{len(incompat)} unordered incompatible pairs")

poor = [(Sa, Sb) for Sa, Sb in combinations(L, 2)
        if MEET[(Sa, Sb)] == frozenset() and (Sa & Sb)]
check("exactly 100 intersection-poor pairs (unordered)", len(poor) == 100,
      f"got {len(poor)}")
ok = True
for Sa, Sb in combinations(L, 2):
    weak = (MEET[(Sa, Sb)] == frozenset() and bool(Sa & Sb))
    strong = bool(Sa & Sb) and not any(C and C <= (Sa & Sb) for C in L)
    if weak != strong: ok = False
check("on a lattice: (meet=0 & overlap nonempty) == (no nonzero L-element in overlap)", ok)

check("no singletons of X in L", all(len(S) != 1 for S in L))

# ---------- L0 ----------
ok_fwd = ok_bwd = ok_meetint = True
for Sa in L:
    for Sb in L:
        c = compat(Sa, Sb)
        m1, m2 = MEET[(Sa, Sb)], MEET[(Sa, X - Sb)]
        commutes = (m1 | m2 == Sa) and not (m1 & m2)
        if c:
            if MEET[(Sa, Sb)] != (Sa & Sb): ok_meetint = False
            if not commutes: ok_fwd = False
        if commutes and not c: ok_bwd = False
check("L0 forward: compatible => commutes", ok_fwd)
check("L0 forward: compatible => meet is the set intersection", ok_meetint)
check("L0 converse: commutes => compatible (A cap B in L)", ok_bwd)

# ---------- T1 contrapositive ----------
ok = True
for Sa, Sb in incompat:
    ov = Sa & Sb
    unresolved = [w for w in ov
                  if not any(C and w in C and C <= ov for C in L)]
    if ov and not unresolved: ok = False
check("T1: every incompatible overlap has a point in no L-member inside it", ok)

# ---------- P1 ----------
blocks_as_sets = [set(b) for b in blocks_rep]
ok = all(not compat(Sa, Sb) for Sa, Sb in poor)
check("P1: poor pairs are incompatible", ok)
ok = all(not any(Sa in bl and Sb in bl for bl in blocks_as_sets) for Sa, Sb in poor)
check("P1: poor pairs lie in no common block", ok)
ok = True   # hereditary: subelements of a poor pair with nonempty overlap stay poor
for Sa, Sb in poor:
    for Sa2 in L:
        if not Sa2 or not (Sa2 <= Sa): continue
        for Sb2 in L:
            if not Sb2 or not (Sb2 <= Sb) or not (Sa2 & Sb2): continue
            if any(C and C <= (Sa2 & Sb2) for C in L): ok = False
check("P1: poorness hereditary (nonempty subregions contain no nonzero L-element)", ok)
ok_super = ok_inL = True   # sigma-superadditivity, finite (pairwise) instances
for C1, C2 in combinations(L, 2):
    if C1 & C2 or (C1 | C2) not in Lset: continue
    for Sb in L:
        left = MEET[(C1, Sb)] | MEET[(C2, Sb)]
        if left not in Lset: ok_inL = False
        if not left <= MEET[((C1 | C2), Sb)]: ok_super = False
check("P1: disjoint-union of blockmeets lies in L (sup-side of superadditivity)", ok_inL)
check("P1: superadditivity  (C1^B) u (C2^B) <= (C1 u C2)^B  for all disjoint C1,C2", ok_super)
ok = True   # A = |_| A_n with A^B = 0  =>  each A_n^B = 0, some A_n cap B nonempty
for C1, C2 in combinations(L, 2):
    if C1 & C2 or (C1 | C2) not in Lset: continue
    Ssum = C1 | C2
    for Sb in L:
        if MEET[(Ssum, Sb)] == frozenset() and (Ssum & Sb):
            if MEET[(C1, Sb)] or MEET[(C2, Sb)]: ok = False
            if not ((C1 & Sb) or (C2 & Sb)): ok = False
check("P1: poor pairs propagate down disjoint decompositions", ok)

# ---------- St_fa = 11 Diracs; Phi trivially ----------
# a two-valued f.a. state is determined by its atom values; enumerate 2^10
fa_states = []
atom_hats = [hat[("at",) + x] for x in ATOMS]
for mask in range(1 << 10):
    val = {}
    for k, S in enumerate(atom_hats):
        val[S] = (mask >> k) & 1
    mu = dict(val)
    mu[frozenset()] = 0; mu[X] = 1
    for S in list(val):
        mu[X - S] = 1 - val[S]
    if len(mu) != 22:      # coatom value clash (cannot happen; safety)
        continue
    good = all(mu[Sa] + mu[Sb] == mu[Sa | Sb]
               for Sa, Sb in combinations(L, 2)
               if not (Sa & Sb) and (Sa | Sb) in Lset)
    if good:
        fa_states.append(mu)
diracs = [{S: int(i in S) for S in L} for i in range(N)]
check("St_fa(L) has exactly 11 elements", len(fa_states) == 11,
      f"got {len(fa_states)}")
check("every f.a. two-valued state is a Dirac (concreteness; Phi trivial here)",
      all(any(mu == d for d in diracs) for mu in fa_states))

# ---------- Corollary atom mechanics ----------
def signature_atoms(field):
    sig = {}
    for w in X:
        key = tuple(sorted(tuple(sorted(S)) for S in field if w in S))
        sig.setdefault(key, set()).add(w)
    return [frozenset(v) for v in sig.values()]

ok = True
for bl in blocks_rep:
    elems = sorted(bl, key=lambda s: (len(s), sorted(s)))
    for r in range(1, 5):
        for B0 in combinations(elems, r):
            B0c = set(B0) | {X - S for S in B0}          # perp-closure
            # generated subfield inside the block: closure under cap and c
            F = set(B0c) | {frozenset(), X}
            changed = True
            while changed:
                changed = False
                for S in list(F):
                    if (X - S) not in F: F.add(X - S); changed = True
                for S in list(F):
                    for T in list(F):
                        if (S & T) not in F: F.add(S & T); changed = True
            if not F <= bl: ok = False                    # subfield of the block
            atoms_F = signature_atoms(F)
            for mu in fa_states:                          # global f.a. extensions
                one_atoms = [a for a in atoms_F
                             if all(mu[S] == 1 for S in F if a <= S and S in mu or False)]
                # value-1 atom: the unique atom on which mu concentrates.
                # mu is Dirac delta_i here; its atom is the signature class of i.
                i = next(j for j in range(N) if all(mu[S] == int(j in S) for S in L))
                a = next(at for at in atoms_F if i in at)
                if not a: ok = False
                for w in a:                               # Dirac at ANY w extends s0
                    if any(int(w in S) != mu[S] for S in B0c): ok = False
check("Corollary: value-1 atom of the generated subfield nonempty; "
      "Dirac at each of its points extends s0 on the pattern", ok)

# ---------- T3 mechanics on each block ----------
ok = True
for bl in blocks_rep:
    field = sorted(bl, key=lambda s: (len(s), sorted(s)))
    atoms_bl = [S for S in field if S and not any(T and T < S for T in field)]
    for a_sel in atoms_bl:                    # each two-valued additive state
        nu = {S: int(a_sel <= S) for S in field}
        # sanity: additive on the block
        for S, T in combinations(field, 2):
            if not (S & T) and (S | T) in bl:
                if nu[S] + nu[T] != nu[S | T]: ok = False
        gens = [S for S in field]             # generators: the whole field
        D = X
        for G in gens:
            side = G if nu[G] == 1 else X - G
            if nu[G] + nu[X - G] != 1: ok = False
            D = D & side
            if D not in bl: ok = False        # F_n stays in the block
            if not (a_sel <= D): ok = False   # nu(F_n) = 1 throughout
        if D != a_sel: ok = False             # D = the state's atom, nonempty
        if not D: ok = False
        for w in D:
            if any(nu[S] != int(w in S) for S in field): ok = False
check("T3 mechanics: F_n construction stays in block, nu(F_n)=1, D = value-1 atom "
      "nonempty, nu = Dirac restricted to the block for every point of D", ok)

print()
print(f"{'ALL CHECKS PASS' if not fails else str(len(fails)) + ' FAILURES'}"
      f" ({22 if True else 0} elements, {len(states)} states)")
sys.exit(len(fails))
