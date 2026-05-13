"""
Experiment: Rössler system — validate generality on different topology.

Rössler has a simpler folding structure than Lorenz.
Lyapunov exponents: λ₁ ≈ 0.07, λ₂ ≈ 0, λ₃ ≈ -5.4.
Run both diagnostics on clean and noisy Rössler.
"""

import numpy as np
import matplotlib.pyplot as plt
import time
from reconstruction import rossler, delay_embed, map_attractor
from scipy.spatial import KDTree

# --- Parameters ---
N = 80000   # Rössler is slower, need more points
dt = 0.05   # Larger dt for Rössler (orbital period ~6)
L = 5       # Lag: 5 steps = 0.25 time units
h = 3.0     # Rössler attractor is smaller than Lorenz
n_query = 200
seed = 42

# --- Generate data ---
print("Generating Rössler trajectory...")
traj = rossler(N, dt=dt, seed=seed)
y_clean = traj[:, 0]
y_std = y_clean.std()
print(f"Signal std: {y_std:.2f}, range: [{y_clean.min():.1f}, {y_clean.max():.1f}]")

rng = np.random.default_rng(seed + 1)
y_noisy = y_clean + 0.05 * y_std * rng.standard_normal(len(y_clean))


def run_diagnostic_sweep(y, label, d_range, L, h, n_query, seed):
    """Run both diagnostics across embedding dimensions."""
    print(f"\n{label}:")
    print("  d | |div|   | acf1   | CV(σ)  | σ")
    print("----+---------+--------+--------+--------")

    for d in d_range:
        Z = delay_embed(y, d=d, L=L)
        Z_t, Z_next = Z[:-1], Z[1:]

        t0 = time.time()
        results = map_attractor(Z_t, Z_next, h=h, n_query=n_query, seed=seed)
        elapsed = time.time() - t0

        if len(results) < 20:
            print(f"  {d} | FAIL ({len(results)} pts)")
            continue

        divs = np.array([r.div for r in results])
        sigmas = np.array([r.sigma for r in results])

        # acf1
        n = len(Z_t)
        dim = Z_t.shape[1]
        rng_local = np.random.default_rng(seed)
        sample_idx = rng_local.choice(n, min(2000, n), replace=False)
        sample_idx.sort()

        query_points = np.array([r.z for r in results])
        tree = KDTree(query_points)
        _, nn_idx = tree.query(Z_t[sample_idx])

        residuals = np.zeros((len(sample_idx), dim))
        for j, (t, qi) in enumerate(zip(sample_idx, nn_idx)):
            r = results[qi]
            delta = Z_t[t] - r.z
            predicted = delta @ r.A.T + r.b
            residuals[j] = Z_next[t] - predicted

        acf1_vals = []
        for dm in range(dim):
            res = residuals[:, dm]
            res_c = res - res.mean()
            var = np.sum(res_c ** 2)
            if var < 1e-12:
                continue
            acf1_vals.append(abs(np.sum(res_c[:-1] * res_c[1:]) / var))

        acf1 = np.mean(acf1_vals) if acf1_vals else np.nan
        cv = np.std(sigmas) / np.mean(sigmas)

        print(f"  {d} | {abs(np.mean(divs)):7.2f} | {acf1:.4f} | "
              f"{cv:.4f} | {np.mean(sigmas):.3f}  ({elapsed:.1f}s)")


# --- Check data scale for bandwidth ---
Z_test = delay_embed(y_clean, d=3, L=L)
dists = np.linalg.norm(Z_test[1:] - Z_test[:-1], axis=1)
print(f"\nDelay-embedded (d=3): shape={Z_test.shape}, "
      f"consec dist mean={dists.mean():.3f}, std per dim={Z_test.std(axis=0)}")

# Adjust h if needed
ref = Z_test[1000]
all_dists = np.linalg.norm(Z_test - ref, axis=1)
print(f"Distances from ref: p10={np.percentile(all_dists,10):.2f}, "
      f"p50={np.percentile(all_dists,50):.2f}")

# --- Dimension sweeps ---
run_diagnostic_sweep(y_clean, "CLEAN Rössler", range(2, 7), L, h, n_query, seed)
run_diagnostic_sweep(y_noisy, "NOISY Rössler (5%)", range(2, 7), L, h, n_query, seed)

print("\n" + "=" * 50)
print("Expected: same pattern as Lorenz — stochastic diagnostic")
print("(acf1) works for both clean and noisy; deterministic (div)")
print("works only for clean.")
