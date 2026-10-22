"""Priority 1 (finite, probabilistic), 2026-10-18. Triangle over {0,1,2}: is every probability state on the
board a mixture of points?
- Board polytope: window cell probabilities mu (consistent marginals) whose forced value Lambda_mu(E) >= 0 for
  every buildable E. At A=3 the buildable sets are exactly the 0/1 elements of the span V (machine count
  15,914); we enumerate them.
- Joint polytope: mixtures of points = conv{cell indicator vector of each point}.
Method: compute the facets of the joint polytope (qhull, in its affine hull), then minimise each facet
functional over the board polytope by LP. A negative minimum means a board state that is not a mixture of
points: a finite, probabilistic pointless state.
"""
import itertools
import numpy as np
from scipy.optimize import linprog
from scipy.spatial import ConvexHull

A = 3
pts = list(itertools.product(range(A), repeat=3)); ix = {p: i for i, p in enumerate(pts)}; n = len(pts)
W = [(0, 1), (1, 2), (2, 0)]
cells = [(k, a, b) for k in range(3) for a in range(A) for b in range(A)]
G = np.array([[1.0 if (p[W[k][0]] == a and p[W[k][1]] == b) else 0.0 for (k, a, b) in cells] for p in pts])

# enumerate 0/1 elements of V (anchor-0 expansion, as in triangle_span_count.py)
face = [x for x in pts if 0 in x]; inner = [x for x in pts if 0 not in x]
D = []
for bits in itertools.product((0, 1), repeat=len(face)):
    f = dict(zip(face, bits)); ok = True
    for (a, b, c) in inner:
        v = f[(a, b, 0)] + f[(a, 0, c)] + f[(0, b, c)] - f[(a, 0, 0)] - f[(0, b, 0)] - f[(0, 0, c)] + f[(0, 0, 0)]
        if v not in (0, 1): ok = False; break
        f[(a, b, c)] = v
    if ok: D.append(np.array([f[p] for p in pts], dtype=float))
print("0/1 elements of V:", len(D))
Gp = np.linalg.pinv(G)
Y = np.array([Gp @ f for f in D])          # Lambda_mu(E) = Y_E . mu
assert max(np.abs(G @ Y[i] - D[i]).max() for i in range(0, len(D), 997)) < 1e-9

# board polytope constraints on mu (27 cell probabilities)
Aeq = []; beq = []
for k in range(3):                          # each window sums to 1
    Aeq.append([1.0 if c[0] == k else 0.0 for c in cells]); beq.append(1.0)
def marg(k, coord_pos, val):                # marginal of window k on its coord_pos-th coordinate
    return [1.0 if (c[0] == k and (c[1] if coord_pos == 0 else c[2]) == val) else 0.0 for c in cells]
for val in range(A):                        # shared coordinates agree: x1 (w0 pos1, w1 pos0), x2 (w1 pos1, w2 pos0), x0 (w2 pos1, w0 pos0)
    for (k1, q1, k2, q2) in ((0, 1, 1, 0), (1, 1, 2, 0), (2, 1, 0, 0)):
        Aeq.append(list(np.array(marg(k1, q1, val)) - np.array(marg(k2, q2, val)))); beq.append(0.0)
Aub = -Y; bub = np.zeros(len(D))            # -Lambda_mu(E) <= 0

# Instead of facets (qhull in 18 dimensions used >1 GB and was stopped), sample board vertices with random
# objectives and test each for membership in the joint polytope by LP. A non-member is a rigorous witness.
rng = np.random.default_rng(0)
Pm = G.T                                    # columns = cell vectors of points
def is_mixture(mu):
    r = linprog(np.zeros(n), A_eq=np.vstack([Pm, np.ones((1, n))]), b_eq=np.concatenate([mu, [1.0]]),
                bounds=(0, None), method='highs')
    return r.status == 0
found = None; tried = 0
for t in range(400):
    cvec = rng.normal(size=len(cells))
    res = linprog(-cvec, A_ub=Aub, b_ub=bub, A_eq=np.array(Aeq), b_eq=np.array(beq), bounds=(0, 1), method='highs')
    if res.status != 0: continue
    tried += 1
    joint_max = max(cvec @ G[i] for i in range(n))
    if -res.fun > joint_max + 1e-7 and not is_mixture(res.x):
        found = res.x; break
print(f"sampled {tried} board vertices; non-mixture found: {found is not None}", flush=True)
if found is not None:
    print("witness window marginals (nonzero cells):", {cells[i]: round(v, 4) for i, v in enumerate(found) if v > 1e-6})
    print("min Lambda over buildable sets at the witness:", round(float((Y @ found).min()), 6))
