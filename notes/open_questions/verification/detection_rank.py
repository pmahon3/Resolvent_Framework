"""Detection rank (2026-10-20; predictions pre-registered in definitions_draft.md section 15).
D_k = Dynkin closure of all events depending on <= k variables; V01 = 0/1 elements of the pair span.
Rank = least k with min Lambda < 0 on D_k cap V01. A = 2 here (2^V points).
"""
import itertools, numpy as np
def rank(name, V, E, law):
    n = 2; pts = list(itertools.product(range(n), repeat=V)); N = len(pts); full = (1 << N) - 1
    cells = [(k, a, b) for k in range(len(E)) for a in range(n) for b in range(n)]
    M = np.array([[1.0 if (p[E[k][0]] == a and p[E[k][1]] == b) else 0.0 for (k, a, b) in cells] for p in pts])
    mu = np.array([law(k, a, b) for (k, a, b) in cells])
    _, s, Vt = np.linalg.svd(M); null = Vt[np.sum(s > 1e-9):]; assert np.allclose(null @ mu, 0)
    Q, _ = np.linalg.qr(M); r = np.linalg.matrix_rank(M); U = np.linalg.svd(M, full_matrices=False)[0][:, :r]
    def inspan(f): return np.linalg.norm(f - U @ (U.T @ f)) < 1e-9
    def val(f): c = np.linalg.lstsq(M, f, rcond=None)[0]; return float(c @ mu)
    out = []
    for k in range(2, V + 1):
        gens = set()
        for S in itertools.combinations(range(V), k):
            sub = list(itertools.product(range(n), repeat=k))
            for T in range(1 << len(sub)):
                gens.add(sum(1 << t for t, p in enumerate(pts) if T >> sub.index(tuple(p[i] for i in S)) & 1))
        if k == V: D = set(range(1 << N)) if N <= 16 else None
        else:
            D = gens | {0, full}; fr = list(D)
            while fr:
                new = set(); L = list(D)
                for a in fr:
                    if full ^ a not in D: new.add(full ^ a)
                    for b in L:
                        if a & b == 0 and (a | b) not in D: new.add(a | b)
                D |= new; fr = list(new)
        if D is None: out.append(f"k={k}: skipped"); continue
        vs = [val(f) for m in D for f in [np.array([(m >> t) & 1 for t in range(N)], float)] if inspan(f)]
        out.append(f"k={k}: |D_k|={len(D)} min={min(vs):+.3f}")
        if min(vs) < -1e-9: break
    print(f"{name:36s} " + " | ".join(out), flush=True)
spec = lambda k, a, b: 0.5 if a != b else 0.0
rank("triangle Specker (control: rank 2)", 3, [(0, 1), (1, 2), (2, 0)], spec)
par4 = lambda k, a, b: 0.5 if ((a != b) if k != 2 else (a == b)) else 0.0
rank("C4 parity (P1)", 4, [(0, 1), (1, 2), (2, 3), (3, 0)], par4)
rank("C5 all-differ (P1)", 5, [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0)], spec)
