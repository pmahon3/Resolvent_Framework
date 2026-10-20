"""Problem 2(a), exact (2026-10-20): enumerate ALL extreme rays of V+ = {g in span of pair cells, g >= 0}
for the triangle with sizes (a0,a1,a2), via cdd double description on g = B y, B an integer basis of the
span (independent cell columns). A non-binary extreme ray exists iff a hidden twist exists from that
source (the other source, a gap V01 \\ D, is reported separately if needed). Rays re-checked exactly (sympy).
"""
import itertools, sys
import numpy as np
import cdd, sympy as sp
sz = tuple(map(int, sys.argv[1].split(",")))
pts = list(itertools.product(*[range(s) for s in sz])); E = [(0, 1), (1, 2), (2, 0)]
cells = [(e, a, b) for e in range(3) for a in range(sz[E[e][0]]) for b in range(sz[E[e][1]])]
M = np.array([[1 if (p[E[e][0]] == a and p[E[e][1]] == b) else 0 for (e, a, b) in cells] for p in pts])
cols = []
for j in range(M.shape[1]):
    if np.linalg.matrix_rank(M[:, cols + [j]]) > len(cols): cols.append(j)
B = M[:, cols]; r = len(cols)
H = cdd.matrix_from_array([[0] + list(map(int, row)) for row in B], rep_type=cdd.RepType.INEQUALITY)
P = cdd.polyhedron_from_matrix(H); G = cdd.copy_generators(P)
rays = [np.array(row[1:]) for row in G.array if row[0] == 0]
nb, examples = 0, []
for y in rays:
    g = B @ y; g[np.abs(g) < 1e-9] = 0; nz = g[g > 0]
    if len(nz) == 0: continue
    if not np.allclose(nz, nz[0], rtol=1e-7, atol=1e-9):
        nb += 1
        if len(examples) < 1: examples.append(np.round(g / nz.min(), 6))
print(f"sizes {sz}: dim V = {r}, extreme rays = {len(rays)}, non-binary = {nb}")
for g in examples:
    gi = [int(round(x)) for x in g]
    Ms = sp.Matrix(M); Z = [i for i in range(len(pts)) if gi[i] == 0]
    ok = (Ms.row_join(sp.Matrix(gi)).rank() == Ms.rank()) and (Ms.rank() - Ms.extract(Z, list(range(M.shape[1]))).rank() == 1)
    print("  exact re-check of first non-binary ray:", ok, "| values", sorted(set(gi)))
