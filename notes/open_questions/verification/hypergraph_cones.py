#!/usr/bin/env python3
"""Step 1 checks for HYPERGRAPH_CENTRES.md: membership R in FW_H by SDP; facts F1 (chordal cliques suffice) and F2 (balanced support => FW_2 = PSD)."""
import itertools
import numpy as np
import cvxpy as cp


def V_H(R, H):
    """min t s.t. R + tI = D + sum_{S in H} C_S, C_S PSD on S, D >= 0 diagonal."""
    k = len(R); t = cp.Variable(); d = cp.Variable(k, nonneg=True); terms = []
    for S in H:
        S = list(S); C = cp.Variable((len(S), len(S)), PSD=True); P = np.zeros((k, len(S))); P[S, range(len(S))] = 1; terms.append(P @ C @ P.T)
    cp.Problem(cp.Minimize(t), [R + t * np.eye(k) == cp.diag(d) + sum(terms)]).solve(solver="CLARABEL")
    return float(t.value)


def random_R_with_support(edges, k, rng, sign=+1, signs=None):
    """Random valid correlation matrix with exactly this support (and given sign of entries), scaled to near the PSD boundary."""
    A = np.zeros((k, k))
    for e, (i, j) in enumerate(edges): A[i, j] = A[j, i] = (signs[e] if signs is not None else sign) * rng.uniform(0.2, 1.0)
    lam = np.linalg.eigvalsh(A)[0]; s = 0.999 / max(1e-9, -lam) if lam < 0 else 0.999 / np.max(np.abs(np.linalg.eigvalsh(A)))
    M = np.eye(k) + s * A
    if np.linalg.eigvalsh(M)[0] < 0: M = np.eye(k) + 0.5 * s * A
    d = np.sqrt(np.diag(M)); return M / np.outer(d, d)


def cycle(L): return [(i, (i + 1) % L) for i in range(L)]


def main():
    rng = np.random.default_rng(19)
    pairs = lambda k: list(itertools.combinations(range(k), 2))
    print("F2: max V_2 over 40 random PSD matrices with positive entries on the support (V_2 <= 0 means pairwise centres suffice)")
    for L in (3, 4, 5, 6, 7):
        vs = [V_H(random_R_with_support(cycle(L), L, rng), pairs(L)) for _ in range(40)]
        print(f"   {L}-cycle ({'odd' if L % 2 else 'even'}): max V_2 = {max(vs):+.4f}")
    # mixed signs: a 3-cycle with one negative edge is balanced in the F2 sense (product of signs = -1 = (-1)^3)
    vs = []
    for _ in range(40):
        R = random_R_with_support(cycle(3), 3, rng, signs=[-1, 1, 1]); vs.append(V_H(R, pairs(3)))
    print(f"   3-cycle with one negative edge (F2-balanced): max V_2 = {max(vs):+.4f} over {len(vs)}")
    print("F1: chordal support (two triangles sharing an edge, 4 sites); cliques {0,1,2},{0,2,3} should suffice")
    vs = []
    for _ in range(40):
        R = random_R_with_support([(0, 1), (1, 2), (0, 2), (2, 3), (0, 3)], 4, rng); vs.append(V_H(R, [(0, 1, 2), (0, 2, 3)]))
    print(f"   max V over maximal-clique hypergraph = {max(vs):+.4f}")
    vs = [V_H(random_R_with_support(cycle(4), 4, rng, signs=[-1, 1, 1, 1]), pairs(4)) for _ in range(40)]
    print(f"   4-cycle with one negative edge (F2-UNbalanced: product -1 != (-1)^4): max V_2 = {max(vs):+.4f}")
    print("Non-chordal positive 4-cycle vs its cliques (= edges): see the F2 line for L = 4")


if __name__ == "__main__":
    main()
