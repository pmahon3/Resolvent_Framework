"""Definitions test 1, more data (2026-10-19): the gap V_01 \\ D on 5-vertex graphs (A = 2).
V_01 exactly: rational RREF of the window-cell indicators; a span element is fixed by its values on the
pivot coordinates, so enumerate 0/1 values there and keep the 0/1 results. D: closure of the window events
under complement and disjoint union, computed inside V_01 (D is a subset of V_01).
"""
import itertools
from fractions import Fraction
def rref(rows, n):
    M = [list(map(Fraction, r)) for r in rows]; piv = []; k = 0
    for c in range(n):
        p = next((i for i in range(k, len(M)) if M[i][c] != 0), None)
        if p is None: continue
        M[k], M[p] = M[p], M[k]; M[k] = [x / M[k][c] for x in M[k]]
        for i in range(len(M)):
            if i != k and M[i][c] != 0: M[i] = [a - M[i][c] * b for a, b in zip(M[i], M[k])]
        piv.append(c); k += 1
    return M[:k], piv
def run(name, V, E, A=2):
    pts = list(itertools.product(range(A), repeat=V)); n = len(pts); full = (1 << n) - 1
    cells = [[1 if (p[i] == a and p[j] == b) else 0 for p in pts] for (i, j) in E for a in range(A) for b in range(A)]
    R, piv = rref(cells, n); r = len(piv)
    V01 = set()
    for bits in range(1 << r):
        f = [sum(((bits >> k) & 1) * R[k][t] for k in range(r)) for t in range(n)]
        if all(x in (0, 1) for x in f): V01.add(sum(1 << t for t in range(n) if f[t] == 1))
    gens = {sum(1 << t for t, p in enumerate(pts) if S >> (p[i] * A + p[j]) & 1)
            for (i, j) in E for S in range(1 << (A * A))}
    D = gens | {0, full}; fr = list(D)
    while fr:
        new = set(); L = list(D)
        for a in fr:
            if full ^ a not in D: new.add(full ^ a)
            for b in L:
                if a & b == 0 and (a | b) not in D: new.add(a | b)
        D |= new; fr = list(new)
    assert D <= V01
    print(f"{name}: dim V = {r}, |D| = {len(D)}, |V01| = {len(V01)}, gap = {len(V01) - len(D)}", flush=True)
    return D, V01, pts
if __name__ == "__main__":
    run("C4 (check: 82/90)", 4, [(0, 1), (1, 2), (2, 3), (3, 0)])
    run("P5 (chordal)", 5, [(0, 1), (1, 2), (2, 3), (3, 4)])
    run("fan (chordal: triangles 012,023,034)", 5, [(0, 1), (1, 2), (0, 2), (2, 3), (0, 3), (3, 4), (0, 4)])
    run("C4 + pendant (non-chordal)", 5, [(0, 1), (1, 2), (2, 3), (3, 0), (3, 4)])
    run("house (non-chordal: C4 + roof)", 5, [(0, 1), (1, 2), (2, 3), (3, 0), (2, 4), (3, 4)])
    run("C5 (non-chordal)", 5, [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0)])
