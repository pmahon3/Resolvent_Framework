"""Case study 1, check 3 (2026-10-19). a/b = 2. Each station records long-run frequencies of 'which species is
dominant' (argmax), so its reports are exact frequencies with no abundance approximation. Construct the bad
inscribed configuration P, Q = P + d(-1,0,1), R = P + d(0,-1,1) on the limit triangle, then find times in a
simulated trajectory whose running dominance frequencies are close to P, Q and R. Report the stations'
pairwise-consistent reports and the implied probability of 'no species dominant'.
"""
import numpy as np
a, b = 2.0, 1.0
A = np.array([[0, -a, b], [b, 0, -a], [-a, b, 0]], float)
y = np.log(np.array([0.5, 0.3, 0.2])); t = 0.0; dt = 0.002; C = np.zeros(3); traj = []
while t < 13000:
    x = np.exp(y - y.max()); x /= x.sum()
    f = A @ x; y = y + dt * (f - x @ f); t += dt
    C[int(np.argmax(x))] += dt
    if int(t / dt) % 50 == 0: traj.append(C / t)
traj = np.array(traj)
# limit triangle from the hand formula (visits run 0 -> 1 -> 2 cyclically: direction +1), r = b/a
r = b / a; e = np.eye(3)
V = [(e[i] + r * e[(i - 1) % 3] + r * r * e[(i - 2) % 3]) / (1 + r + r * r) for i in range(3)]
u = np.array([-1.0, 0, 1]); v = np.array([0, -1.0, 1])
best = None
E = [(V[i], V[(i + 1) % 3] - V[i]) for i in range(3)]
for i in range(3):
    for j in range(3):
        for k in range(3):
            (Pi, Di), (Pj, Dj), (Pk, Dk) = E[i], E[j], E[k]
            M = np.zeros((4, 4)); rhs = np.zeros(4)
            for c in range(2):
                M[c] = [-Di[c], Dj[c], 0, -u[c]]; rhs[c] = Pi[c] - Pj[c]
                M[2 + c] = [-Di[c], 0, Dk[c], -v[c]]; rhs[2 + c] = Pi[c] - Pk[c]
            if abs(np.linalg.det(M)) < 1e-12: continue
            tP, tQ, tR, d = np.linalg.solve(M, rhs)
            if all(-1e-9 <= s <= 1 + 1e-9 for s in (tP, tQ, tR)) and d > 1e-6:
                best = (Pi + tP * Di, d)
P, d = best; Q = P + d * u; R = P + d * v
print("P, Q, R:", np.round(P, 3), np.round(Q, 3), np.round(R, 3), " delta =", round(d, 3))
late = traj[len(traj) // 10:]
def nearest(p):
    dist = np.linalg.norm(late - p, axis=1); i = int(np.argmin(dist)); return late[i], dist[i]
(Pp, eP), (Qq, eQ), (Rr, eR) = nearest(P), nearest(Q), nearest(R)
print("closest simulated running frequencies:", np.round(Pp, 3), np.round(Qq, 3), np.round(Rr, 3),
      " distances:", round(eP, 4), round(eQ, 4), round(eR, 4))
# station reports from the simulated epochs: (1,2) from P-epoch, (2,3) from Q-epoch, (3,1) from R-epoch
print("overlap checks (species 2: P vs Q; species 3: Q vs R; species 1: R vs P):",
      round(Pp[1] - Qq[1], 3), round(Qq[2] - Rr[2], 3), round(Rr[0] - Pp[0], 3))
print("implied P(no species dominant) = w3(P) - w3(Q) =", round(Pp[2] - Qq[2], 3))
