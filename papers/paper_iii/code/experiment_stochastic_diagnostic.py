"""
Experiment C: Stochastic diagnostic (residual whiteness) on noisy Lorenz.

The deterministic diagnostic (tr(A) convergence) fails for noisy data
(Experiment 3). The stochastic commitment says: if the Langevin model
z_{t+1} = A(z)z + b(z) + σ(z)η is correct, residuals should be white.

Diagnostic: at each embedding dimension d, compute:
  1. Residual autocorrelation (Ljung-Box test on ε_t)
  2. Spatial uniformity of σ(z) (coefficient of variation)
  3. Normality of residuals (Shapiro-Wilk on ε components)

If the embedding is sufficient for the stochastic model, residuals
should be: uncorrelated, spatially uniform noise, approximately normal.
If insufficient, residuals carry deterministic structure.

Key question: does this diagnostic correctly identify sufficient d
for noisy Lorenz where tr(A) failed?
"""

import numpy as np
from scipy import stats
from reconstruction import lorenz63, delay_embed, map_attractor
import time

# --- Parameters ---
N = 50000
dt = 0.01
L = 10
h = 5.0
n_query = 300
seed = 42
noise_frac = 0.05  # 5% noise — where tr(A) diagnostic failed

# --- Generate noisy Lorenz ---
print("Generating Lorenz-63 + 5% observational noise...")
traj = lorenz63(N, dt=dt, seed=seed)
y_clean = traj[:, 0]
y_std = y_clean.std()
noise_amp = noise_frac * y_std

rng = np.random.default_rng(seed + 1)
y_noisy = y_clean + noise_amp * rng.standard_normal(len(y_clean))
print(f"Signal std: {y_std:.2f}, noise amplitude: {noise_amp:.3f}")


def residual_whiteness_diagnostic(Z_t, Z_next, h, n_query, seed):
    """Compute stochastic diagnostic: residual autocorrelation + uniformity.

    Returns dict with:
      - mean_acf1: mean absolute lag-1 autocorrelation of residuals
      - mean_acf5: mean absolute lag-5 autocorrelation
      - cv_sigma: coefficient of variation of σ(z) across query points
      - frac_normal: fraction of query points where residuals pass normality
      - mean_sigma: mean noise amplitude
      - mean_div: mean divergence (for comparison)
    """
    results = map_attractor(Z_t, Z_next, h=h, n_query=n_query, seed=seed)

    if len(results) < 20:
        return None

    sigmas = np.array([r.sigma for r in results])
    divs = np.array([r.div for r in results])

    # --- Residual autocorrelation ---
    # For each query point, the residuals at nearby points should be
    # temporally uncorrelated if the model is sufficient.
    # We compute lag-1 and lag-5 autocorrelation of the GLOBAL residual
    # sequence (predicted vs actual for consecutive time steps).

    # Compute global residuals: for each t, ε_t = z_{t+1} - (A(z_t)·Δ + b)
    # Use a random subset of the full time series
    n = len(Z_t)
    d = Z_t.shape[1]
    sample_idx = np.random.default_rng(seed).choice(n, min(2000, n), replace=False)
    sample_idx.sort()

    # Find the nearest query point for each sample and use its A, b
    from scipy.spatial import KDTree
    query_points = np.array([r.z for r in results])
    tree = KDTree(query_points)
    _, nn_idx = tree.query(Z_t[sample_idx])

    residuals = np.zeros((len(sample_idx), d))
    for j, (t, qi) in enumerate(zip(sample_idx, nn_idx)):
        r = results[qi]
        delta = Z_t[t] - r.z
        predicted = delta @ r.A.T + r.b
        residuals[j] = Z_next[t] - predicted

    # Lag-1 autocorrelation per dimension
    acf1_per_dim = []
    acf5_per_dim = []
    for dim in range(d):
        res_dim = residuals[:, dim]
        res_centered = res_dim - res_dim.mean()
        var = np.sum(res_centered ** 2)
        if var < 1e-12:
            continue
        # Lag 1
        acf1 = np.sum(res_centered[:-1] * res_centered[1:]) / var
        acf1_per_dim.append(abs(acf1))
        # Lag 5
        if len(res_centered) > 5:
            acf5 = np.sum(res_centered[:-5] * res_centered[5:]) / var
            acf5_per_dim.append(abs(acf5))

    mean_acf1 = np.mean(acf1_per_dim) if acf1_per_dim else np.nan
    mean_acf5 = np.mean(acf5_per_dim) if acf5_per_dim else np.nan

    # --- Spatial uniformity of σ ---
    cv_sigma = np.std(sigmas) / np.mean(sigmas) if np.mean(sigmas) > 0 else np.nan

    # --- Normality of residuals ---
    # Shapiro-Wilk on each dimension (subsample for speed)
    n_test = min(500, len(residuals))
    frac_normal = 0
    n_tests = 0
    for dim in range(d):
        _, p = stats.shapiro(residuals[:n_test, dim])
        n_tests += 1
        if p > 0.05:
            frac_normal += 1
    frac_normal = frac_normal / n_tests if n_tests > 0 else np.nan

    return {
        'mean_acf1': mean_acf1,
        'mean_acf5': mean_acf5,
        'cv_sigma': cv_sigma,
        'frac_normal': frac_normal,
        'mean_sigma': np.mean(sigmas),
        'std_sigma': np.std(sigmas),
        'mean_div': np.mean(divs),
        'n_results': len(results),
    }


# --- Dimension sweep with stochastic diagnostic ---
print("\n" + "=" * 70)
print("STOCHASTIC DIAGNOSTIC: dimension sweep on noisy Lorenz (5% noise)")
print("=" * 70)
print("\n  d | acf(1) | acf(5) | CV(σ)  | %normal | mean σ  | mean div")
print("----+--------+--------+--------+---------+---------+---------")

for d in range(2, 8):
    Z = delay_embed(y_noisy, d=d, L=L)
    Z_t, Z_next = Z[:-1], Z[1:]

    t0 = time.time()
    diag = residual_whiteness_diagnostic(Z_t, Z_next, h=h, n_query=n_query, seed=seed)
    elapsed = time.time() - t0

    if diag is None:
        print(f"  {d} | INSUFFICIENT DATA")
        continue

    print(f"  {d} | {diag['mean_acf1']:6.4f} | {diag['mean_acf5']:6.4f} | "
          f"{diag['cv_sigma']:6.3f} | {diag['frac_normal']*100:5.1f}%  | "
          f"{diag['mean_sigma']:7.3f} | {diag['mean_div']:7.3f}  ({elapsed:.1f}s)")

# --- Comparison: same sweep on CLEAN data ---
print("\n" + "=" * 70)
print("STOCHASTIC DIAGNOSTIC: dimension sweep on CLEAN Lorenz (for comparison)")
print("=" * 70)
print("\n  d | acf(1) | acf(5) | CV(σ)  | %normal | mean σ  | mean div")
print("----+--------+--------+--------+---------+---------+---------")

for d in range(2, 8):
    Z = delay_embed(y_clean, d=d, L=L)
    Z_t, Z_next = Z[:-1], Z[1:]

    diag = residual_whiteness_diagnostic(Z_t, Z_next, h=h, n_query=n_query, seed=seed)

    if diag is None:
        print(f"  {d} | INSUFFICIENT DATA")
        continue

    print(f"  {d} | {diag['mean_acf1']:6.4f} | {diag['mean_acf5']:6.4f} | "
          f"{diag['cv_sigma']:6.3f} | {diag['frac_normal']*100:5.1f}%  | "
          f"{diag['mean_sigma']:7.3f} | {diag['mean_div']:7.3f}")

print("\n" + "=" * 70)
print("INTERPRETATION")
print("=" * 70)
print("""
If the stochastic diagnostic works:
- acf(1) should DECREASE with d (residuals become more white)
- CV(σ) should DECREASE with d (σ becomes more uniform)
- %normal should INCREASE with d (residuals become more Gaussian)
- These should work even for noisy data (where div failed)

If it doesn't work:
- acf/CV/%normal don't trend with d → diagnostic is not sensitive
  to embedding dimension at this commitment level
""")
