"""Definitions test (2026-10-19): 'linearly local' (0/1 elements of the span V of view functions) versus
'constructively local' (the carrier D, built by 'not' and 'either one'). Prediction: hidden twists live in
the gap V_01 \\ D. Small graphs, alphabet A, D by direct closure, V_01 by brute force over all 0/1 vectors.
"""
import itertools, sys
import numpy as np
def run(name, V, E, A):
    pts = list(itertools.product(range(A), repeat=V)); n = len(pts); full = (1 << n) - 1
    gens = set()
    for (i, j) in E:
        for S in range(1 << (A * A)):
            m = 0
            for t, p in enumerate(pts):
                if S >> (p[i] * A + p[j]) & 1: m |= 1 << t
            gens.add(m)
    D = set(gens) | {0, full}; fr = list(D)
    while fr:
        new = set(); L = list(D)
        for a in fr:
            if full ^ a not in D: new.add(full ^ a)
            for b in L:
                if a & b == 0 and (a | b) not in D: new.add(a | b)
        D |= new; fr = list(new)
    # span basis: indicator vectors of window cells
    B = np.array([[1.0 if (p[i] == a and p[j] == b) else 0.0 for p in pts] for (i, j) in E for a in range(A) for b in range(A)]).T
    Q, R = np.linalg.qr(B); r = np.linalg.matrix_rank(B); Qr = np.linalg.svd(B, full_matrices=False)[0][:, :r]
    V01 = 0
    for m in range(1 << n):
        f = np.array([(m >> t) & 1 for t in range(n)], float)
        if np.linalg.norm(f - Qr @ (Qr.T @ f)) < 1e-9: V01 += 1
    print(f"{name} (A={A}): |D| = {len(D)}, |0/1 elements of span| = {V01}, gap = {V01 - len(D)}", flush=True)
run("triangle", 3, [(0, 1), (1, 2), (2, 0)], 2)
run("path P4", 4, [(0, 1), (1, 2), (2, 3)], 2)
run("C4", 4, [(0, 1), (1, 2), (2, 3), (3, 0)], 2)
run("diamond", 4, [(0, 1), (1, 2), (0, 2), (2, 3), (3, 0)], 2)
run("K4", 4, [(0, 1), (1, 2), (2, 3), (3, 0), (0, 2), (1, 3)], 2)
