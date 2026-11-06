#!/usr/bin/env python3
"""Minimum source reach: V_m(R) = min{t : R + tI in FW_m} (factor-width-m cone). Primal + dual SDP checks.
See notes/open_questions/views_across_records/SOURCE_REACH_SCOUT.md."""
import itertools, time
import numpy as np
import cvxpy as cp


def Vm_primal(R, m, solver="CLARABEL"):
    k = len(R); t = cp.Variable(); terms = []; cons = []
    for S in itertools.combinations(range(k), m):
        C = cp.Variable((m, m), PSD=True); P = np.zeros((k, m)); P[list(S), range(m)] = 1
        terms.append(P @ C @ P.T)
    cons.append(R + t * np.eye(k) == sum(terms))
    cp.Problem(cp.Minimize(t), cons).solve(solver=solver)
    return float(t.value)


def Vm_dual(R, m, solver="CLARABEL"):
    k = len(R); X = cp.Variable((k, k), symmetric=True)
    cons = [cp.trace(X) == 1] + [X[np.ix_(S, S)] >> 0 for S in map(list, itertools.combinations(range(k), m))]
    cp.Problem(cp.Maximize(-cp.trace(X @ R)), cons).solve(solver=solver)
    return float(-np.trace(X.value @ R))


def perron(R): return float(np.max(np.abs(np.linalg.eigvalsh(np.abs(R - np.eye(len(R)))))))


if __name__ == "__main__":
    rng = np.random.default_rng(0); worst = {"p-d": 0, "m2": 0, "mk": 0, "mono": 0}
    for trial in range(15):
        k = int(rng.integers(4, 7)); A = rng.normal(size=(k, k + 2)); C = A @ A.T + 0.3 * np.diag(rng.random(k))
        d = np.sqrt(np.diag(C)); R = C / np.outer(d, d)
        vals = []
        for m in range(2, k + 1):
            p, q = Vm_primal(R, m), Vm_dual(R, m); worst["p-d"] = max(worst["p-d"], abs(p - q)); vals.append(p)
        worst["m2"] = max(worst["m2"], abs(vals[0] - (perron(R) - 1)))
        worst["mk"] = max(worst["mk"], abs(vals[-1] + np.linalg.eigvalsh(R)[0]))
        worst["mono"] = max(worst["mono"], max(0, max(np.diff(vals))))
    print("max |primal-dual| =", f"{worst['p-d']:.1e}", "| max |V_2 - (Perron-1)| =", f"{worst['m2']:.1e}",
          "| max |V_k + lambda_min| =", f"{worst['mk']:.1e}", "| max increase in m (should be 0) =", f"{worst['mono']:.1e}")
    R = np.full((3, 3), 0.6); np.fill_diagonal(R, 1); print("equal triangle r=0.6: V_2 =", round(Vm_primal(R, 2), 4), " V_3 =", round(Vm_primal(R, 3), 4))
    for m in (3, 5):
        A = rng.normal(size=(10, 12)); C = A @ A.T; d = np.sqrt(np.diag(C)); R = C / np.outer(d, d)
        t0 = time.time(); Vm_dual(R, m); print(f"k=10, m={m}: dual solve {time.time()-t0:.2f}s")
