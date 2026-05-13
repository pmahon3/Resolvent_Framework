"""
Experiment: Lag selection via commitment-indexed diagnostics.

Fix d=3 (correct for Lorenz). Sweep L=1..30.
At each L, compute both diagnostics for clean and noisy data.

Good lag: dynamics are well-sampled; diagnostics should be optimal.
Bad lag (too small): oversampled, delay vectors nearly collinear.
Bad lag (too large): undersampled, dynamics look discontinuous.

Question: do both diagnostics detect bad lags? Does the stochastic
diagnostic work for lag selection under noise?
"""

import numpy as np
import matplotlib.pyplot as plt
import time
from reconstruction import lorenz63, delay_embed, map_attractor
from scipy.spatial import KDTree

# --- Parameters ---
N = 50000
dt = 0.01
d = 3
h = 5.0
n_query = 200
seed = 42

L_values = np.arange(1, 31)

# --- Generate data ---
print("Generating Lorenz-63...")
traj = lorenz63(N, dt=dt, seed=seed)
y_clean = traj[:, 0]
y_std = y_clean.std()

rng = np.random.default_rng(seed + 1)
y_noisy = y_clean + 0.05 * y_std * rng.standard_normal(len(y_clean))


def compute_diagnostics(y, L, d, h, n_query, seed):
    """Compute div and acf1 for a given (y, L, d)."""
    Z = delay_embed(y, d=d, L=L)
    Z_t, Z_next = Z[:-1], Z[1:]

    results = map_attractor(Z_t, Z_next, h=h, n_query=n_query, seed=seed)

    if len(results) < 20:
        return None

    divs = np.array([r.div for r in results])
    sigmas = np.array([r.sigma for r in results])

    # acf1 of global residuals
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
    cv = np.std(sigmas) / np.mean(sigmas) if np.mean(sigmas) > 0 else np.nan

    return {
        'mean_div': np.mean(divs),
        'abs_div': abs(np.mean(divs)),
        'acf1': acf1,
        'cv_sigma': cv,
        'mean_sigma': np.mean(sigmas),
    }


# --- Lag sweep: clean data ---
print("\nLag sweep — CLEAN data (d=3):")
print("  L  | |div|   | acf1   | CV(σ)  | σ")
print("-----+---------+--------+--------+--------")

clean_results = []
for L in L_values:
    t0 = time.time()
    diag = compute_diagnostics(y_clean, L, d, h, n_query, seed)
    elapsed = time.time() - t0
    if diag is None:
        print(f"  {L:2d} | FAIL")
        clean_results.append(None)
        continue
    clean_results.append(diag)
    print(f"  {L:2d} | {diag['abs_div']:7.2f} | {diag['acf1']:.4f} | "
          f"{diag['cv_sigma']:.4f} | {diag['mean_sigma']:.3f}  ({elapsed:.1f}s)")

# --- Lag sweep: noisy data ---
print("\nLag sweep — NOISY data (5% noise, d=3):")
print("  L  | |div|   | acf1   | CV(σ)  | σ")
print("-----+---------+--------+--------+--------")

noisy_results = []
for L in L_values:
    diag = compute_diagnostics(y_noisy, L, d, h, n_query, seed)
    if diag is None:
        print(f"  {L:2d} | FAIL")
        noisy_results.append(None)
        continue
    noisy_results.append(diag)
    print(f"  {L:2d} | {diag['abs_div']:7.2f} | {diag['acf1']:.4f} | "
          f"{diag['cv_sigma']:.4f} | {diag['mean_sigma']:.3f}")

# --- Plot ---
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Extract arrays
L_clean = [L_values[i] for i, r in enumerate(clean_results) if r is not None]
div_clean = [r['abs_div'] for r in clean_results if r is not None]
acf_clean = [r['acf1'] for r in clean_results if r is not None]
cv_clean = [r['cv_sigma'] for r in clean_results if r is not None]

L_noisy = [L_values[i] for i, r in enumerate(noisy_results) if r is not None]
div_noisy = [r['abs_div'] for r in noisy_results if r is not None]
acf_noisy = [r['acf1'] for r in noisy_results if r is not None]
cv_noisy = [r['cv_sigma'] for r in noisy_results if r is not None]

axes[0, 0].plot(L_clean, div_clean, 'o-', label='Clean', markersize=3)
axes[0, 0].plot(L_noisy, div_noisy, 's-', label='Noisy (5%)', markersize=3)
axes[0, 0].set_xlabel('Lag L')
axes[0, 0].set_ylabel('|mean div|')
axes[0, 0].set_title('Deterministic diagnostic vs lag')
axes[0, 0].legend()

axes[0, 1].plot(L_clean, acf_clean, 'o-', label='Clean', markersize=3)
axes[0, 1].plot(L_noisy, acf_noisy, 's-', label='Noisy (5%)', markersize=3)
axes[0, 1].set_xlabel('Lag L')
axes[0, 1].set_ylabel('acf(1)')
axes[0, 1].set_title('Stochastic diagnostic vs lag')
axes[0, 1].legend()

axes[1, 0].plot(L_clean, cv_clean, 'o-', label='Clean', markersize=3)
axes[1, 0].plot(L_noisy, cv_noisy, 's-', label='Noisy (5%)', markersize=3)
axes[1, 0].set_xlabel('Lag L')
axes[1, 0].set_ylabel('CV(σ)')
axes[1, 0].set_title('σ uniformity vs lag')
axes[1, 0].legend()

# Panel 4: sigma vs lag
sig_clean = [r['mean_sigma'] for r in clean_results if r is not None]
sig_noisy = [r['mean_sigma'] for r in noisy_results if r is not None]
axes[1, 1].plot(L_clean, sig_clean, 'o-', label='Clean', markersize=3)
axes[1, 1].plot(L_noisy, sig_noisy, 's-', label='Noisy (5%)', markersize=3)
axes[1, 1].set_xlabel('Lag L')
axes[1, 1].set_ylabel('Mean σ')
axes[1, 1].set_title('Noise amplitude vs lag')
axes[1, 1].legend()

plt.tight_layout()
plt.savefig('lag_sweep.png', dpi=150)
print("\nFigure saved: lag_sweep.png")
plt.close()
