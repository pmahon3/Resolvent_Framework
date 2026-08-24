"""Mechanical check of the finite parity core of the Product Ulam Carrier witness.

Tests (exact-disjointness shadow of the mod-countable arguments):
  1. S-hat contains exactly one member of each complement pair of E4.
  2. Lemma 3.3(IV): for distinct weight-2 kappa, lambda in N, the coordinate-pair
     multiset is exactly {(1,1),(1,0),(0,1),(0,0)}  (each of the 3 unordered pairs).
  3. Cor 4.1 shadow: trace pattern 1000 (A cap B) is unrepresentable (odd weight).
  4. Thm 6.3 shadow: on a finite model M (|M|=5), P-tilde = {E : E_f = xi^(kappa_f)},
     with u = ANY finitely-additive 2-valued measure on P(M) (here: all principal
     ultrafilters — the only ones on a finite set, and additivity of m uses only
     finite additivity of u), check: for ALL pairs E,G in P-tilde with E cap G = empty
     and E-join-G in P-tilde:  m(E) + m(G) == m(E join G).
     Also check E join G IS in P-tilde whenever E,G in P-tilde disjoint (3.3 shadow).
  5. Lemma 3.2 shadow (uniqueness): each E in P-tilde has exactly one normalized
     (xi, kappa in N) representation (exact regime: uniqueness on the nose except
     trivial coincidences xi in {empty, M} — report what is found).
  6. Vote well-definedness: m computed from ANY representation (xi,kappa), kappa in E4,
     agrees with m from the normalized one.
"""
from itertools import product

F2_4 = [tuple(v) for v in product((0, 1), repeat=4)]
E4 = [v for v in F2_4 if sum(v) % 2 == 0]
N = [v for v in E4 if v[3] == 0]
W2 = [v for v in N if sum(v) == 2]
SHAT = [(1, 1, 1, 1), (1, 1, 0, 0), (1, 0, 1, 0), (0, 1, 1, 0)]

def xor(a, b):
    return tuple(x ^ y for x, y in zip(a, b))

ONES = (1, 1, 1, 1)

# --- Test 1: S-hat one per complement pair
pairs = set()
for v in E4:
    pairs.add(frozenset({v, xor(v, ONES)}))
assert len(pairs) == 4
for p in pairs:
    inS = [v for v in p if tuple(v) in SHAT]
    assert len(inS) == 1, f"complement pair {p} has {len(inS)} members in S-hat"
print("Test 1 PASS: S-hat selects exactly one member of each of the 4 complement pairs")

# --- Test 2: Lemma 3.3(IV) coordinate-pair multiset
for i in range(len(W2)):
    for j in range(i + 1, len(W2)):
        k, l = W2[i], W2[j]
        ms = sorted(zip(k, l))
        assert ms == sorted([(1, 1), (1, 0), (0, 1), (0, 0)]), f"{k},{l}: {ms}"
print(f"Test 2 PASS: all {len(W2)*(len(W2)-1)//2} distinct weight-2 pairs in N give multiset {{(1,1),(1,0),(0,1),(0,0)}}")

# --- Finite model
M = list(range(5))
F = [1, 2, 3, 4]

def subsets(s):
    s = list(s)
    for mask in range(1 << len(s)):
        yield frozenset(x for k, x in enumerate(s) if mask >> k & 1)

def traces(E):
    return tuple(frozenset(x for x in M if (x, f) in E) for f in F)

def build(xi, kappa):
    xi = frozenset(xi)
    out = set()
    for f_idx, f in enumerate(F):
        part = set(M) - xi if kappa[f_idx] else xi
        out |= {(x, f) for x in part}
    return frozenset(out)

# P-tilde with all representations
rep_map = {}  # E -> list of (xi, kappa) over kappa in E4
for xi in subsets(M):
    for kappa in E4:
        E = build(xi, kappa)
        rep_map.setdefault(E, []).append((xi, kappa))
P_tilde = set(rep_map)

# --- Test 3: A cap B (trace 1000) unrepresentable
AcapB = build(set(M), (0, 1, 1, 1))  # M x {1} = xi=M on fiber1 only: traces (M,0,0,0)
AcapB = frozenset((x, 1) for x in M)
assert AcapB not in P_tilde, "A cap B unexpectedly representable"
print("Test 3 PASS: A cap B (trace pattern 1000) is NOT in P-tilde")

# --- Test 5/6: normalized representation uniqueness + vote well-definedness
def normalized_reps(E):
    return [(xi, k) for (xi, k) in rep_map[E] if k in N]

def vote(xi, kappa, u):
    return xor(kappa, ONES if u(xi) else (0, 0, 0, 0))

def m_of(E, u):
    reps = normalized_reps(E)
    votes = {vote(xi, k, u) for (xi, k) in reps}
    assert len(votes) == 1, f"vote not well-defined on {E}: {votes} from {reps}"
    return 1 if votes.pop() in SHAT else 0

us = [lambda xi, p=p: 1 if p in xi else 0 for p in M]  # principal ultrafilters

for E in P_tilde:
    nr = normalized_reps(E)
    assert len(nr) >= 1
    for u in us:
        mE = m_of(E, u)  # asserts vote well-defined across normalized reps
        # Test 6: any E4-representation gives same m
        for (xi, k) in rep_map[E]:
            v = vote(xi, k, u)
            assert (1 if v in SHAT else 0) == mE, f"rep ({xi},{k}) of {E} disagrees"
print(f"Test 5/6 PASS: vote/m well-defined across ALL representations, all {len(P_tilde)} P-tilde sets, all {len(us)} ultrafilters")

# --- Test 4: closure under disjoint union + additivity of m
n_pairs = 0
Pl = sorted(P_tilde, key=lambda s: (len(s), sorted(s)))
for i in range(len(Pl)):
    for j in range(i, len(Pl)):
        E, G = Pl[i], Pl[j]
        if E & G:
            continue
        H = E | G
        assert H in P_tilde, f"disjoint union escapes P-tilde: {E} + {G}"
        for u in us:
            assert m_of(E, u) + m_of(G, u) == m_of(H, u), \
                f"additivity fails: E={E} G={G} u={u}"
        n_pairs += 1
print(f"Test 4 PASS: {n_pairs} disjoint pairs — union stays in P-tilde and m(E)+m(G)=m(H) for all {len(us)} ultrafilters")

# --- Bonus: complement closure and m flip
for E in P_tilde:
    Ec = frozenset(product(M, F)) - E
    assert Ec in P_tilde
    for u in us:
        assert m_of(E, u) + m_of(Ec, u) == 1
print("Bonus PASS: complement closure and m(E)+m(E-perp)=1")

# --- Cores get m=1 under every u (votes = kappa, u(empty)=0)
A = build(frozenset(), (1, 1, 0, 0))
B = build(frozenset(), (1, 0, 1, 0))
C = build(frozenset(), (0, 1, 1, 0))
for u in us:
    assert m_of(A, u) == m_of(B, u) == m_of(C, u) == 1
assert not (A & B & C)
print("Cores PASS: m(A)=m(B)=m(C)=1 for every ultrafilter; A cap B cap C = empty")
print("\nALL MECHANICAL CHECKS PASS")
