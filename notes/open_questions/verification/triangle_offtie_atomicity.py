"""Triangle: off-tie atomicity of the strict cyclic / anticyclic sets (2026-10-17).

Lemma checked (finite boxes): let S be the strict-cyclic set {x0<x1<x2, x1<x2<x0, x2<x0<x1} or the
strict-anticyclic set, and Delta the tie set (two coordinates equal). If f on [0,N)^3 is supported on
S u Delta and has zero triple interaction on every 2x2x2 box inside [0,N)^3, then f is constant on the
points of S inside the inner box [0,M)^3 (ties unconstrained).
Any f on N^3 with zero triple interaction restricts to such an f, so a pass for every M gives the lemma
on N^3. Rank is computed exactly over GF(P): the GF(P) kernel contains the reduction of the rational
kernel, so 'restricted rank 1 over GF(P)' implies rank <= 1 over Q (and 1 is attained by f = 1_S + ties).

Memory-safe (see CLAUDE.md, compute constraints): rows are streamed in chunks and folded into a
running row-echelon basis of at most #columns rows; no dense m x m object is ever built.
Usage: python3 triangle_offtie_atomicity.py A 4 3 [prime]   (check A|B|offtie, inner M, margin k)
The off-tie lemma above FAILS at finite boxes (superseded); checks A, B are gate.triangle_thin_atomicity.
"""
import itertools, sys
import numpy as np

P = 32749

def strict_cyc(x):
    a, b, c = x
    return (a < b < c) or (b < c < a) or (c < a < b)

def tie(x):
    return len(set(x)) < 3

def reduce_into(basis, piv, rows):
    """Fold rows (int64 array) into echelon basis (list of rows with pivot cols piv) mod P."""
    for r in rows:
        r = r % P
        for b, j in zip(basis, piv):
            if r[j]:
                r = (r - r[j] * b) % P
        nz = np.nonzero(r)[0]
        if len(nz):
            j = nz[0]
            r = (r * pow(int(r[j]), P - 2, P)) % P
            # keep basis fully reduced on pivot columns
            for i, b in enumerate(basis):
                if b[j]:
                    basis[i] = (b - b[j] * r) % P
            basis.append(r); piv.append(j)

def kernel(basis, piv, n):
    free = [j for j in range(n) if j not in set(piv)]
    K = np.zeros((len(free), n), dtype=np.int64)
    for k, fj in enumerate(free):
        K[k, fj] = 1
        for b, j in zip(basis, piv):
            K[k, j] = (-b[fj]) % P
    return K

def rank_mod(A):
    basis, piv = [], []
    reduce_into(basis, piv, A.astype(np.int64))
    return len(basis)

def Estar(x):
    x0, x1, x2 = x
    return int(x1 >= x0) + int(x2 >= x1 + 1) + int(x0 >= x2 + 1) == 2

def thin(x):
    """L: exactly the window cells inside Y = complement of E* (hand-checked)."""
    x0, x1, x2 = x
    return x1 == x2 or x0 == x2 or x0 == x1 + 1

def run(N, M, support, target):
    """Rank (mod P) of the zero-interaction kernel on support, restricted to inner points of target."""
    global P
    pts = [p for p in itertools.product(range(N), repeat=3) if support(p)]
    ix = {p: i for i, p in enumerate(pts)}
    n = len(pts)
    pr = list(itertools.combinations(range(N), 2))
    basis, piv, chunk = [], [], []
    for (a, A), (b, B), (c, C) in itertools.product(pr, repeat=3):
        r = np.zeros(n, dtype=np.int64)
        for s0, x0 in ((1, a), (-1, A)):
            for s1, x1 in ((1, b), (-1, B)):
                for s2, x2 in ((1, c), (-1, C)):
                    k = ix.get((x0, x1, x2))
                    if k is not None:
                        r[k] += s0 * s1 * s2
        if r.any():
            chunk.append(r)
        if len(chunk) >= 2000:
            reduce_into(basis, piv, np.array(chunk)); chunk = []
    if chunk:
        reduce_into(basis, piv, np.array(chunk))
    K = kernel(basis, piv, n)
    inner = [i for i, p in enumerate(pts) if max(p) < M and target(p)]
    return n, K.shape[0], rank_mod(K[:, inner]) if len(K) else 0

CHECKS = {
    # gate.triangle_thin_atomicity (pre-registered 2026-10-17)
    "A": (lambda x: not Estar(x), lambda x: not Estar(x) and not thin(x)),
    "B": (lambda x: Estar(x) or thin(x), Estar),
    # superseded off-tie lemma (kept for the record; fails)
    "offtie": (lambda x: tie(x) or strict_cyc(x), lambda x: strict_cyc(x) and not tie(x)),
}

if __name__ == '__main__':
    # usage: python3 triangle_offtie_atomicity.py CHECK M margin [prime]
    name, M, k = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
    if len(sys.argv) > 4:
        P = int(sys.argv[4])
    support, target = CHECKS[name]
    n, kd, rr = run(M + k, M, support, target)
    print(f"{name} M={M} N={M+k} P={P}: support points={n} kernel={kd} restricted rank={rr}"
          f" -> {'CONSTANT (pass)' if rr == 1 else 'NOT constant (fail)'}", flush=True)
