"""Oracle (exact, Fraction arithmetic): which flagship-contextual binary ring data
define a state on the glued Dynkin carrier D?

For each ring length L and each edge-sign pattern s in {=,!=}^L, take the parity
vertex of the coherence polytope C: every window uniform on its two legal pairs
(x_k = x_{k+1} if s_k is '=', x_k != x_{k+1} otherwise).  It is in R (realisable)
iff the number of '!=' edges is even; an odd count is the flagship's PR-box-type
contextual vertex (the golden-mean odd-ring gap is the all-'!=' case at odd L).
Test: does its unique linear extension define a state on D (well-defined, range
in [0,1])?  Same method as window_gluing_states.py.
See notes/open_questions/delay_embedding/collision_vs_generation.md (flagship match)."""
import itertools, sys
from fractions import Fraction as Fr
sys.path.insert(0, '.')
from window_gluing_dynkin import run
from window_gluing_states import rref

def state_range(n, W, marg):
    pts, D, _, _ = run(n, W)
    cols, m = [], []
    for w in W:
        for v in itertools.product(range(2), repeat=len(w)):
            cols.append([Fr(int(tuple(p[i] for i in w) == v)) for p in pts]); m.append(Fr(marg(w, v)))
    k, P = len(cols), len(pts)
    aug = [cols[j] + [Fr(int(t == j)) for t in range(k)] for j in range(k)]
    R, _ = rref(aug)
    wd = all(sum(r[P + t] * m[t] for t in range(k)) == 0 for r in R if all(v == 0 for v in r[:P]))
    basis = [(r[:P], sum(r[P + t] * m[t] for t in range(k))) for r in R if any(v != 0 for v in r[:P])]
    vals = []
    for E in D:
        y = [Fr(E >> i & 1) for i in range(P)]; L = Fr(0)
        for vec, lv in basis:
            c = next(i for i, v in enumerate(vec) if v != 0)
            coef = y[c] / vec[c]; y = [a - coef * b for a, b in zip(y, vec)]; L += coef * lv
        assert all(v == 0 for v in y)
        vals.append(L)
    return len(D), wd, min(vals), max(vals)

for n in (3, 4, 5, 6):
    W = [(i, (i + 1) % n) for i in range(n)]
    seen = {}
    for s in itertools.product((0, 1), repeat=n):          # 1 = '!=' edge
        marg = lambda w, v, s=s: Fr(1, 2) if (v[0] != v[1]) == bool(s[W.index(w)]) else 0
        dsz, wd, lo, hi = state_range(n, W, marg)
        odd = sum(s) % 2 == 1
        key = (odd, wd, lo >= 0 and hi <= 1)
        seen.setdefault(key, []).append(''.join('x' if b else '=' for b in s))
    print(f"L={n} |D|={dsz}")
    for (odd, wd, ok), pats in sorted(seen.items()):
        print(f"   {'CONTEXTUAL' if odd else 'realisable'}  well-defined={wd}  state on D={ok}  "
              f"({len(pats)} patterns, e.g. {pats[0]})")

# --- Whole-polytope check (float LP, scipy): is every point of C a state on D? ---
# For each E in D, write 1_E = sum_t c_E[t] * 1_{window cell t} (exactly, over Q) and
# minimise c_E . m over the coherence polytope C (window tables: nonnegative, each sums
# to 1, single-coordinate marginals agree on shared coordinates).
from scipy.optimize import linprog

def coeffs(n, W):
    pts, D, _, _ = run(n, W)
    cols = []
    for w in W:
        for v in itertools.product(range(2), repeat=len(w)):
            cols.append([Fr(int(tuple(p[i] for i in w) == v)) for p in pts])
    k, P = len(cols), len(pts)
    aug = [cols[j] + [Fr(int(t == j)) for t in range(k)] for j in range(k)]
    R, _ = rref(aug)
    basis = [(r[:P], r[P:]) for r in R if any(v != 0 for v in r[:P])]
    out = []
    for E in D:
        y = [Fr(E >> i & 1) for i in range(P)]; c = [Fr(0)] * k
        for vec, comb in basis:
            i0 = next(i for i, v in enumerate(vec) if v != 0)
            coef = y[i0] / vec[i0]; y = [a - coef * b for a, b in zip(y, vec)]
            c = [a + coef * b for a, b in zip(c, comb)]
        assert all(v == 0 for v in y)
        out.append((E, c))
    return pts, out, k

def polytope_C(n, W, k):
    A, b = [], []
    for j, w in enumerate(W):
        row = [0] * k; row[4 * j:4 * j + 4] = [1] * 4; A.append(row); b.append(1)
    # window j = (j, j+1) and window j+1 = (j+1, j+2) share coordinate j+1
    for j in range(n):
        j2 = (j + 1) % n
        for a in range(2):
            row = [0] * k
            for v in itertools.product(range(2), repeat=2):
                if v[1] == a: row[4 * j + 2 * v[0] + v[1]] += 1
                if v[0] == a: row[4 * j2 + 2 * v[0] + v[1]] -= 1
            A.append(row); b.append(0)
    return A, b

print("\nWhole coherence polytope C (LP, float): min over C of the extension on each E in D")
for n in (3, 4, 5, 6):
    W = [(i, (i + 1) % n) for i in range(n)]
    pts, out, k = coeffs(n, W)
    A, b = polytope_C(n, W, k)
    worst = min(linprog([float(x) for x in c], A_eq=A, b_eq=b, bounds=[(0, None)] * k,
                        method="highs").fun for _, c in out)
    print(f"L={n}: min_E min_C L(E) = {worst:+.6f}  -> C inside states-on-D: {worst > -1e-9}")

# --- Triangle: does "state on D" cut C down to R? ---
# Maximise each odd-parity cycle functional  sum_k P(window k matches s_k)  over
# C ∩ {L(E) >= 0 for all E in D}.  Over R the maximum is L-1 = 2; over C it is 3.
print("\nTriangle: odd-parity cycle functionals over C ∩ states-on-D (R value 2, C value 3)")
n = 3; W = [(i, (i + 1) % n) for i in range(n)]
pts, out, k = coeffs(n, W); A, b = polytope_C(n, W, k)
A_ub = [[-float(x) for x in c] for _, c in out]; b_ub = [0.0] * len(out)
for s in itertools.product((0, 1), repeat=n):
    if sum(s) % 2 == 0: continue
    obj = [0.0] * k
    for j in range(n):
        for v in itertools.product(range(2), repeat=2):
            if (v[0] != v[1]) == bool(s[j]): obj[4 * j + 2 * v[0] + v[1]] = -1.0
    res = linprog(obj, A_ub=A_ub, b_ub=b_ub, A_eq=A, b_eq=b, bounds=[(0, None)] * k, method="highs")
    print("  s =", ''.join('x' if t else '=' for t in s), " max =", round(-res.fun, 6))
