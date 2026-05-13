"""
Experiment: FNN comparison — does FNN degrade at the same noise threshold?

Compute false nearest neighbour percentage as a function of d,
for clean and noisy Lorenz. Compare degradation with our Jacobian
diagnostic.

FNN algorithm (Kennel-Brown-Abarbanel 1992):
For each point x_t in d-dimensional embedding:
  1. Find nearest neighbour x_nn in d dimensions
  2. Check if they remain neighbours in d+1 dimensions
  3. If ||x_t^{d+1} - x_nn^{d+1}|| / ||x_t^d - x_nn^d|| > R_tol,
     the neighbour is "false"
  4. FNN% = fraction of false neighbours

Sufficient d: FNN% → 0.
"""

import numpy as np
import matplotlib.pyplot as plt
import time
from reconstruction import lorenz63, delay_embed
from scipy.spatial import KDTree

# --- Parameters ---
N = 50000
dt = 0.01
L = 10
R_tol = 15.0    # Standard FNN threshold (Kennel et al. use 10-15)
n_test = 2000   # Points to test
seed = 42


def fnn_percentage(y, d, L, R_tol=15.0, n_test=2000, seed=None):
    """Compute false nearest neighbour percentage.

    Parameters
    ----------
    y : array, shape (N,)
        Scalar time series.
    d : int
        Current embedding dimension.
    L : int
        Lag.
    R_tol : float
        Threshold for identifying false neighbours.
    n_test : int
        Number of points to test.
    seed : int
        Random seed for point selection.

    Returns
    -------
    fnn_frac : float
        Fraction of false nearest neighbours (0 to 1).
    """
    # Embed at d and d+1
    Z_d = delay_embed(y, d, L)
    Z_d1 = delay_embed(y, d + 1, L)

    # Z_d1 is shorter — align indices
    n_d = len(Z_d)
    n_d1 = len(Z_d1)
    # Z_d1[t] corresponds to Z_d[t] for t < n_d1
    n = min(n_d, n_d1)
    Z_d = Z_d[:n]
    Z_d1 = Z_d1[:n]

    # Select test points
    rng = np.random.default_rng(seed)
    test_idx = rng.choice(n, size=min(n_test, n), replace=False)

    # Build KDTree for d-dimensional embedding
    tree = KDTree(Z_d)

    false_count = 0
    total_count = 0

    for i in test_idx:
        # Find nearest neighbour in d dimensions (k=2 because first is self)
        dists, indices = tree.query(Z_d[i], k=2)
        nn_idx = indices[1]
        nn_dist_d = dists[1]

        if nn_dist_d < 1e-10:
            continue  # Skip if distance is essentially zero

        # Check distance in d+1 dimensions
        nn_dist_d1 = np.linalg.norm(Z_d1[i] - Z_d1[nn_idx])

        # Extra component distance
        extra_dist = abs(Z_d1[i, -1] - Z_d1[nn_idx, -1])

        # FNN criterion: ratio of extra distance to d-distance
        ratio = extra_dist / nn_dist_d

        if ratio > R_tol:
            false_count += 1
        total_count += 1

    return false_count / total_count if total_count > 0 else np.nan


# --- Generate data ---
print("Generating Lorenz-63...")
traj = lorenz63(N, dt=dt, seed=seed)
y_clean = traj[:, 0]
y_std = y_clean.std()

noise_fracs = [0.0, 0.01, 0.02, 0.05, 0.10, 0.20]
rng = np.random.default_rng(seed + 1)

# --- FNN sweep ---
print("\nFNN percentage vs embedding dimension:")
print("=" * 60)

fnn_results = {}

for nf in noise_fracs:
    noise_amp = nf * y_std
    y = y_clean + noise_amp * rng.standard_normal(len(y_clean))

    print(f"\nNoise: {nf:.0%}")
    print("  d | FNN%")
    print("----+------")

    fnn_vals = []
    for d in range(1, 8):
        t0 = time.time()
        fnn = fnn_percentage(y, d, L, R_tol=R_tol, n_test=n_test, seed=seed)
        elapsed = time.time() - t0
        fnn_vals.append(fnn)
        print(f"  {d} | {fnn*100:5.1f}%  ({elapsed:.1f}s)")

    fnn_results[nf] = fnn_vals

# --- Plot ---
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

colors = plt.cm.viridis(np.linspace(0, 0.8, len(noise_fracs)))
d_vals = list(range(1, 8))

for nf, color in zip(noise_fracs, colors):
    label = f'{nf:.0%}' if nf > 0 else 'Clean'
    axes[0].plot(d_vals, [f * 100 for f in fnn_results[nf]],
                 'o-', color=color, label=label, markersize=4)

axes[0].set_xlabel('Embedding dimension d')
axes[0].set_ylabel('FNN %')
axes[0].set_title('False Nearest Neighbours vs noise')
axes[0].legend(title='Noise level')
axes[0].set_ylim(-5, 105)
axes[0].axhline(5, color='gray', linestyle='--', alpha=0.5, label='5% threshold')

# Panel 2: FNN at d=3 vs noise level (the threshold)
fnn_at_d3 = [fnn_results[nf][2] for nf in noise_fracs]  # d=3 is index 2
axes[1].plot([nf * 100 for nf in noise_fracs], [f * 100 for f in fnn_at_d3],
             'o-', color='tab:red', markersize=6)
axes[1].set_xlabel('Noise level (%)')
axes[1].set_ylabel('FNN % at d=3')
axes[1].set_title('FNN degradation with noise (d=3)')
axes[1].axhline(5, color='gray', linestyle='--', alpha=0.5)

plt.tight_layout()
plt.savefig('fnn_comparison.png', dpi=150)
print("\nFigure saved: fnn_comparison.png")
plt.close()

# --- Summary ---
print("\n" + "=" * 60)
print("SUMMARY: FNN at d=3 (correct dimension) vs noise")
print("=" * 60)
for nf in noise_fracs:
    fnn = fnn_results[nf][2]  # d=3
    status = "✓ clean" if fnn < 0.05 else "✗ degraded"
    print(f"  Noise {nf:5.1%}: FNN = {fnn*100:5.1f}%  {status}")
