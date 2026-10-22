"""gate.finite_staircase_carrier (pre-registered 2026-10-18).

Triangle over the alphabet {0..A-1}. Window family F_A: x1 = x0+1, x2 = x1+1, x0 = x2+1 (mod A), each with a
uniform slot. It is locally consistent, and has no joint picture unless A | 3.
Lambda = the forced linear functional on the span V of window functions (well defined because the
marginals agree). Question: is Lambda >= 0 on every 0/1 element of V? (D = 0/1 elements of V is
machine-checked at A=3.) We compute min Lambda over 0/1 f in V by exact MILP. V is described by
the vanishing of every 2x2x2 box interaction.
Memory: at most A^3 = 216 binary variables, about 3.4k equality rows (A=6). Tiny.
"""
import itertools, sys
import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds
from scipy.sparse import lil_matrix

def run(A, family='plus1'):
    pts = list(itertools.product(range(A), repeat=3)); ix = {p: i for i, p in enumerate(pts)}; n = len(pts)
    W = [(0, 1), (1, 2), (2, 0)]
    def u(k, a, b):          # window k on (x_i, x_j) = (a, b)
        if family == 'plus1':
            return 1.0 / A if b == (a + 1) % A else 0.0
        raise ValueError
    # lambda in R^Omega with <lambda, window cell indicator> = u
    rows = []; rhs = []
    for k, (i, j) in enumerate(W):
        for a in range(A):
            for b in range(A):
                r = np.zeros(n)
                for p in pts:
                    if p[i] == a and p[j] == b: r[ix[p]] = 1
                rows.append(r); rhs.append(u(k, a, b))
    M = np.array(rows); lam, res, rk, _ = np.linalg.lstsq(M, np.array(rhs), rcond=None)
    resid = np.abs(M @ lam - np.array(rhs)).max()
    # box constraints
    pr = list(itertools.combinations(range(A), 2))
    B = lil_matrix((len(pr) ** 3, n)); r_ = 0
    for (a, a2), (b, b2), (c, c2) in itertools.product(pr, repeat=3):
        for (x0, s0), (x1, s1), (x2, s2) in itertools.product(((a, 1), (a2, -1)), ((b, 1), (b2, -1)), ((c, 1), (c2, -1))):
            B[r_, ix[(x0, x1, x2)]] += s0 * s1 * s2
        r_ += 1
    cons = LinearConstraint(B.tocsr(), 0, 0)
    res = milp(c=lam, constraints=[cons], integrality=np.ones(n), bounds=Bounds(0, 1))
    f = np.round(res.x).astype(int)
    S = [pts[i] for i in range(n) if f[i]]
    return resid, res.fun, S

if __name__ == '__main__':
    for A in range(3, int(sys.argv[1]) + 1 if len(sys.argv) > 1 else 6):
        resid, val, S = run(A)
        print(f"A={A}: consistency residual {resid:.1e}; min Lambda over 0/1 elements of V = {val:.4f}; "
              f"minimiser has {len(S)} points", flush=True)
        if val < -1e-9 and A <= 4:
            print("   set:", S)
