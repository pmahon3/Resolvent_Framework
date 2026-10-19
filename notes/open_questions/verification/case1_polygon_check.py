"""Case study 1, check 2 (2026-10-19). Three-species rock-paper-scissors with an attracting heteroclinic cycle.
(i) Simulate the replicator dynamics x_i' = x_i((Ax)_i - x.Ax) in log coordinates (softmax), for
A = [[0,-a,b],[b,0,-a],[-a,b,0]] with a > b (attracting cycle), and record running time-averages; compare their
turning points with the hand formula V_i ~ e_i + r e_{i-1} + r^2 e_{i-2}.
(ii) Geometry: is there P on the boundary of the limit triangle and delta > 0 with P + delta(-1,0,1) and
P + delta(0,-1,1) also on the boundary? (the asynchronous-observer inconsistency of finding F3), for both
traversal directions and a range of r.
"""
import numpy as np
def sim(a, b, T_end=4000.0, dt=0.002):
    A = np.array([[0, -a, b], [b, 0, -a], [-a, b, 0]], float)
    y = np.log(np.array([0.5, 0.3, 0.2])); t = 0.0; S = np.zeros(3); dom = []; prev = -1
    while t < T_end:
        x = np.exp(y - y.max()); x /= x.sum()
        f = A @ x; y = y + dt * (f - x @ f); t += dt; S += dt * x
        k = int(np.argmax(x))
        if k != prev: dom.append((t, k, S / t)); prev = k
    return dom
def turning_points(dom):
    # running average at the moment dominance switches = end of a stay
    return [(k_prev, avg) for (_, k_prev, _), (_, _, avg) in zip(dom[:-1], dom[1:])]
for (a, b) in ((2.0, 1.0), (1.5, 1.0)):
    dom = sim(a, b)
    tp = turning_points(dom)[-6:]
    print(f"a={a}, b={b}: last turning points (species, running average):")
    for k, avg in tp: print("   ", k, np.round(avg, 3))
    # estimate r from successive stay durations
    times = [t for t, _, _ in dom]
    d = np.diff(times)[-6:]
    print("    stay durations:", np.round(d, 1), " ratio ~", np.round(d[1:] / d[:-1], 3))
def boundary(V, s):
    # point at parameter s in [0,3) along triangle V0->V1->V2->V0
    i = int(s) % 3; f = s - int(s)
    return (1 - f) * V[i] + f * V[(i + 1) % 3]
def on_boundary(V, p, tol):
    best = 1e9
    for i in range(3):
        A_, B_ = V[i], V[(i + 1) % 3]; AB = B_ - A_
        t = np.clip(np.dot(p - A_, AB) / np.dot(AB, AB), 0, 1)
        best = min(best, np.linalg.norm(A_ + t * AB - p))
    return best < tol
u = np.array([-1.0, 0, 1]); v = np.array([0, -1.0, 1])
# Exact: corners P on edge i, Q on edge j, R on edge k (edge e = V[e] + t (V[e+1]-V[e]), t in [0,1]);
# solve Q - P = d u and R - P = d v (first two coordinates; the third follows since all sum to 1).
def solve(V):
    sols = []
    E = [(V[i], V[(i + 1) % 3] - V[i]) for i in range(3)]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                (Pi, Di), (Pj, Dj), (Pk, Dk) = E[i], E[j], E[k]
                # unknowns: tP, tQ, tR, d
                M = np.zeros((4, 4)); rhs = np.zeros(4)
                for c in range(2):
                    M[c] = [-Di[c], Dj[c], 0, -u[c]]; rhs[c] = Pi[c] - Pj[c]
                    M[2 + c] = [-Di[c], 0, Dk[c], -v[c]]; rhs[2 + c] = Pi[c] - Pk[c]
                if abs(np.linalg.det(M)) < 1e-12: continue
                tP, tQ, tR, d = np.linalg.solve(M, rhs)
                if all(-1e-9 <= t <= 1 + 1e-9 for t in (tP, tQ, tR)) and abs(d) > 1e-6:
                    sols.append(d)
    return sols
for direction in (+1, -1):
    for r in (0.1, 0.3, 0.5, 2/3, 0.9):
        e = np.eye(3)
        V = [(e[i] + r * e[(i - direction) % 3] + r * r * e[(i - 2 * direction) % 3]) / (1 + r + r * r) for i in range(3)]
        ds = solve(V)
        pos = [round(d, 4) for d in ds if d > 0]; neg = [round(d, 4) for d in ds if d < 0]
        print(f"direction {direction:+d}, r = {r:.3f}: inscribed copies with delta > 0 (bad): {sorted(set(pos))}; delta < 0 (harmless): {sorted(set(neg))}")
