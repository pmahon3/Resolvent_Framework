"""Test (b), 2026-10-19: is 'state on D' (non-negative on every buildable set) the same as the single-copy
exclusivity principle (E1: pairwise exclusive window cells have total probability <= 1)? A = 2.
Both are cut out of the no-signalling polytope NS (consistent edge marginals). Compare by LP:
  - max over P_E of the most negative D-value  (P_E subset of P_D?)
  - max over P_D of the largest exclusive-clique sum  (P_D subset of P_E?)
"""
import itertools
import numpy as np
from scipy.optimize import linprog
import networkx as nx
from gap_five_vertex import run

def test(name, V, E):
    D, V01, pts = run(name, V, E)
    n = len(pts); A = 2
    cells = [(e, a, b) for e in range(len(E)) for a in range(A) for b in range(A)]
    M = np.array([[1.0 if (p[E[e][0]] == a and p[E[e][1]] == b) else 0.0 for p in pts] for (e, a, b) in cells]).T
    k = len(cells)
    # NS: each edge sums to 1; vertex marginals agree across edges
    Aeq, beq = [], []
    for e in range(len(E)):
        Aeq.append([1.0 if c[0] == e else 0.0 for c in cells]); beq.append(1.0)
    for v in range(V):
        es = [(e, E[e].index(v)) for e in range(len(E)) if v in E[e]]
        for (e1, s1), (e2, s2) in zip(es, es[1:]):
            row = [0.0] * k
            for j, (e, a, b) in enumerate(cells):
                if e == e1 and (a, b)[s1] == 0: row[j] += 1
                if e == e2 and (a, b)[s2] == 0: row[j] -= 1
            Aeq.append(row); beq.append(0.0)
    # well-definedness: NS functionals must kill the null space of M (dependencies among cell indicators)
    _, s, Vt = np.linalg.svd(M); null = Vt[np.sum(s > 1e-9):]
    sol = np.linalg.lstsq(np.array(Aeq), np.array(beq), rcond=None)[0]
    ns_basis = np.linalg.svd(np.array(Aeq))[2][np.linalg.matrix_rank(np.array(Aeq)):]
    ok = np.allclose(null @ sol, 0) and np.allclose(null @ ns_basis.T, 0)
    # D rows: coefficient vector c_S with M c_S = 1_S; value = c_S . mu
    Drows = []
    for m in D:
        f = np.array([(m >> t) & 1 for t in range(n)], float)
        c = np.linalg.lstsq(M, f, rcond=None)[0]; assert np.allclose(M @ c, f); Drows.append(c)
    Drows = np.array(Drows)
    # exclusivity graph on cells: exclusive iff they give different values to a shared variable
    def val(c):
        e, a, b = cells[c]; return {E[e][0]: a, E[e][1]: b}
    G = nx.Graph(); G.add_nodes_from(range(k))
    for i, j in itertools.combinations(range(k), 2):
        vi, vj = val(i), val(j)
        if any(vi[x] != vj[x] for x in vi if x in vj): G.add_edge(i, j)
    cliques = [c for c in nx.find_cliques(G) if len(c) > 1]
    Erows = np.array([[1.0 if j in c else 0.0 for j in range(k)] for c in cliques])
    bnd = [(0, None)] * k
    # P_E subset of P_D ?  minimise each D-value over P_E
    worstD = min(linprog(r, A_ub=Erows, b_ub=np.ones(len(Erows)), A_eq=Aeq, b_eq=beq, bounds=bnd).fun for r in Drows)
    # P_D subset of P_E ?  maximise each clique sum over P_D
    worstE = max(-linprog(-r, A_ub=-Drows, b_ub=np.zeros(len(Drows)), A_eq=Aeq, b_eq=beq, bounds=bnd).fun for r in Erows)
    print(f"  well-defined on span: {ok}; |cliques| = {len(cliques)}; min D-value over P_E = {worstD:.4f}; "
          f"max clique sum over P_D = {worstE:.4f}", flush=True)

test("triangle", 3, [(0, 1), (1, 2), (2, 0)])
test("C4", 4, [(0, 1), (1, 2), (2, 3), (3, 0)])
test("C5", 5, [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0)])
test("house", 5, [(0, 1), (1, 2), (2, 3), (3, 0), (2, 4), (3, 4)])
