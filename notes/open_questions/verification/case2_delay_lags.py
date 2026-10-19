"""Case study 2 (2026-10-19): delay windows of ONE scalar observable y = dominant species, on the rock-paper-
scissors heteroclinic cycle (a/b = 2). Running lag-tau tables T_tau(t)(i,j) = fraction of s <= t with
(y_s, y_{s+tau}) = (i,j). Hand prediction: off-diagonal mass -> 0 as t grows (switches are rare), so every
lag table is about diag(w(t)), and observers who agree on overlaps share w: no pointlessness.
"""
import numpy as np
a, b = 2.0, 1.0
A = np.array([[0, -a, b], [b, 0, -a], [-a, b, 0]], float)
y = np.log(np.array([0.5, 0.3, 0.2])); dt = 0.01; n = int(8000 / dt); ys = np.empty(n, dtype=np.int8)
for k in range(n):
    x = np.exp(y - y.max()); x /= x.sum()
    f = A @ x; y = y + dt * (f - x @ f); ys[k] = int(np.argmax(x))
for tau_time in (1.0, 10.0, 50.0):
    tau = int(tau_time / dt)
    for frac in (0.1, 0.3, 1.0):
        m = int(frac * (n - tau))
        off = np.mean(ys[:m] != ys[tau:tau + m])
        print(f"lag {tau_time:>5}: off-diagonal mass up to t = {m*dt:7.0f}: {off:.4f}")
