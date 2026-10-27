"""Hostile probe: is the clique (single-copy exclusivity / CE^1) relaxation already exact on the triangle?
For size sz: P = marginal polytope (conv of point marginal vectors). Facets via cdd. CE1 = consistent normalized
pair laws, >=0, with sum over every maximal clique of pairwise-disjoint cells <= 1. Report facets g with
min_{CE1} Lambda(g) < 0."""
import itertools, sys, numpy as np, cdd, networkx as nx
from fractions import Fraction
from scipy.optimize import linprog
sz = tuple(int(x) for x in sys.argv[1].split(','))
E = [(0, 1), (1, 2), (2, 0)]
pts = list(itertools.product(*[range(s) for s in sz]))
cells = [(e, a, b) for e in range(3) for a in range(sz[E[e][0]]) for b in range(sz[E[e][1]])]
def cellset(c):
    e, a, b = c; i, j = E[e]; return frozenset(t for t, p in enumerate(pts) if p[i] == a and p[j] == b)
CS = [cellset(c) for c in cells]
M = np.array([[1 if t in CS[k] else 0 for k in range(len(cells))] for t in range(len(pts))])
# facets of P
mat = cdd.matrix_from_array([[1] + list(r) for r in M], rep_type=cdd.RepType.GENERATOR)
poly = cdd.polyhedron_from_matrix(mat); H = cdd.copy_inequalities(poly)
lin = set(H.lin_set); facets = [np.array(H.array[i], float) for i in range(len(H.array)) if i not in lin]
# CE1 constraints
G = nx.Graph(); G.add_nodes_from(range(len(cells)))
for k in range(len(cells)):
    for l in range(k + 1, len(cells)):
        if not (CS[k] & CS[l]): G.add_edge(k, l)
cliques = [q for q in nx.find_cliques(G) if len(q) > 1]
A_ub = []; b_ub = []
for q in cliques:
    row = np.zeros(len(cells)); row[q] = 1; A_ub.append(row); b_ub.append(1)
# consistency: one-variable marginals agree; normalization per context
A_eq = []; b_eq = []
for e in range(3):
    row = np.zeros(len(cells)); row[[k for k, c in enumerate(cells) if c[0] == e]] = 1; A_eq.append(row); b_eq.append(1)
for v in range(3):
    ctxs = [(e, pos) for e in range(3) for pos in (0, 1) if E[e][pos] == v]
    (e1, p1), (e2, p2) = ctxs
    for val in range(sz[v]):
        row = np.zeros(len(cells))
        for k, c in enumerate(cells):
            if c[0] == e1 and c[1 + p1] == val: row[k] += 1
            if c[0] == e2 and c[1 + p2] == val: row[k] -= 1
        A_eq.append(row); b_eq.append(0)
bad = []; gw = {}
for f in facets:
    b0, a = f[0], f[1:]
    res = linprog(a, A_ub=np.array(A_ub), b_ub=b_ub, A_eq=np.array(A_eq), b_eq=b_eq, bounds=[(0, None)] * len(cells), method='highs')
    val = b0 + res.fun
    g = b0 + M @ a; gpos = g[g > 1e-9]; ratio = round(gpos.max() / gpos.min(), 6)
    gw[ratio] = gw.get(ratio, 0) + 1
    if val < -1e-8: bad.append((val, ratio))
print(f"size {sz}: |Omega|={len(pts)} cells={len(cells)} facets={len(facets)} maxcliques={len(cliques)} "
      f"facet max/min nonzero-value ratios={gw} | facets violated on CE1: {len(bad)}; worst={min(bad)[0] if bad else None}; "
      f"violated ratios={sorted(set(r for _, r in bad))}")
