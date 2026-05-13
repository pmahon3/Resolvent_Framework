"""
Experiment: Phase diagram — noise level vs embedding dimension.

Sweep noise amplitude (0% to 20%) and embedding dimension (d=2..7).
At each (noise, d) pair, compute both diagnostics:
  - Deterministic: |mean div| (large = informative)
  - Stochastic: 1 - acf(1) (large = white residuals = good)

Produce a 2D heatmap showing which diagnostic is informative where.
This is the paper's central figure.
"""

import numpy as np
import matplotlib.pyplot as plt
import time
from reconstruction import lorenz63, delay_embed, map_attractor
from scipy.spatial import KDTree

# --- Parameters ---
N = 50000
dt = 0.01
L = 10
h = 5.0
n_query = 200
seed = 42

noise_fracs = np.array([0.0, 0.005, 0.01, 0.02, 0.05, 0.10, 0.15, 0.20])
d_range = range(2, 8)

# --- Generate clean data ---
print("Generating Lorenz-63...")
traj = lorenz63(N, dt=dt, seed=seed)
y_clean = traj[:, 0]
y_std = y_clean.std()

# --- Compute diagnostics at each (noise, d) ---
div_grid = np.full((len(noise_fracs), len(list(d_range))), np.nan)
acf_grid = np.full_like(div_grid, np.nan)
cv_grid = np.full_like(div_grid, np.nan)


def compute_acf1_global(Z_t, Z_next, results, seed):
    """Compute lag-1 autocorrelation of residuals using nearest query point."""
    n = len(Z_t)
    d = Z_t.shape[1]
    rng = np.random.default_rng(seed)
    sample_idx = rng.choice(n, min(2000, n), replace=False)
    sample_idx.sort()

    query_points = np.array([r.z for r in results])
    tree = KDTree(query_points)
    _, nn_idx = tree.query(Z_t[sample_idx])

    residuals = np.zeros((len(sample_idx), d))
    for j, (t, qi) in enumerate(zip(sample_idx, nn_idx)):
        r = results[qi]
        delta = Z_t[t] - r.z
        predicted = delta @ r.A.T + r.b
        residuals[j] = Z_next[t] - predicted

    acf1_vals = []
    for dim in range(d):
        res = residuals[:, dim]
        res_c = res - res.mean()
        var = np.sum(res_c ** 2)
        if var < 1e-12:
            continue
        acf1_vals.append(abs(np.sum(res_c[:-1] * res_c[1:]) / var))

    return np.mean(acf1_vals) if acf1_vals else np.nan


rng_noise = np.random.default_rng(seed + 1)

print("\nPhase diagram computation:")
total = len(noise_fracs) * len(list(d_range))
count = 0

for i, nf in enumerate(noise_fracs):
    noise_amp = nf * y_std
    y = y_clean + noise_amp * rng_noise.standard_normal(len(y_clean))

    for j, d in enumerate(d_range):
        count += 1
        t0 = time.time()

        Z = delay_embed(y, d=d, L=L)
        Z_t, Z_next = Z[:-1], Z[1:]

        results = map_attractor(Z_t, Z_next, h=h, n_query=n_query, seed=seed)

        if len(results) < 20:
            print(f"  [{count}/{total}] noise={nf:.1%} d={d}: insufficient data")
            continue

        # Deterministic diagnostic: |mean div|
        divs = np.array([r.div for r in results])
        div_grid[i, j] = abs(np.mean(divs))

        # Stochastic diagnostic: acf(1)
        acf1 = compute_acf1_global(Z_t, Z_next, results, seed)
        acf_grid[i, j] = acf1

        # σ uniformity: CV
        sigmas = np.array([r.sigma for r in results])
        cv_grid[i, j] = np.std(sigmas) / np.mean(sigmas)

        elapsed = time.time() - t0
        print(f"  [{count}/{total}] noise={nf:.1%} d={d}: |div|={div_grid[i,j]:.2f}, "
              f"acf1={acf1:.3f}, CV={cv_grid[i,j]:.3f} ({elapsed:.1f}s)")

# --- Plot phase diagram ---
d_vals = np.array(list(d_range))

fig, axes = plt.subplots(1, 3, figsize=(16, 5))

# Panel 1: Deterministic diagnostic (|div|)
im1 = axes[0].imshow(div_grid, aspect='auto', origin='lower',
                      extent=[d_vals[0]-0.5, d_vals[-1]+0.5,
                              noise_fracs[0]*100-0.5, noise_fracs[-1]*100+0.5],
                      cmap='viridis', interpolation='nearest')
axes[0].set_xlabel('Embedding dimension d')
axes[0].set_ylabel('Noise (%)')
axes[0].set_title('|mean div| (deterministic)')
axes[0].set_yticks(noise_fracs * 100)
plt.colorbar(im1, ax=axes[0], label='|⟨tr(A)⟩|')

# Panel 2: Stochastic diagnostic (1 - acf1)
whiteness = 1.0 - acf_grid
im2 = axes[1].imshow(whiteness, aspect='auto', origin='lower',
                      extent=[d_vals[0]-0.5, d_vals[-1]+0.5,
                              noise_fracs[0]*100-0.5, noise_fracs[-1]*100+0.5],
                      cmap='viridis', interpolation='nearest')
axes[1].set_xlabel('Embedding dimension d')
axes[1].set_ylabel('Noise (%)')
axes[1].set_title('Residual whiteness (stochastic)')
axes[1].set_yticks(noise_fracs * 100)
plt.colorbar(im2, ax=axes[1], label='1 - acf(1)')

# Panel 3: Which diagnostic is more informative?
# Normalize each to [0,1] range, then show the difference
div_norm = div_grid / np.nanmax(div_grid)
white_norm = whiteness / np.nanmax(whiteness)
advantage = white_norm - div_norm  # positive = stochastic better

im3 = axes[2].imshow(advantage, aspect='auto', origin='lower',
                      extent=[d_vals[0]-0.5, d_vals[-1]+0.5,
                              noise_fracs[0]*100-0.5, noise_fracs[-1]*100+0.5],
                      cmap='RdBu', interpolation='nearest',
                      vmin=-1, vmax=1)
axes[2].set_xlabel('Embedding dimension d')
axes[2].set_ylabel('Noise (%)')
axes[2].set_title('Stochastic advantage')
axes[2].set_yticks(noise_fracs * 100)
plt.colorbar(im3, ax=axes[2], label='stoch − determ')

plt.tight_layout()
plt.savefig('phase_diagram.png', dpi=150)
print("\nFigure saved: phase_diagram.png")
plt.close()

# --- Print summary ---
print("\n" + "=" * 50)
print("PHASE DIAGRAM SUMMARY")
print("=" * 50)
print("\nDeterministic diagnostic (|div|) is informative when:")
print("  Large values → strong trend with d")
for i, nf in enumerate(noise_fracs):
    vals = div_grid[i, :]
    trend = vals[-1] - vals[0] if not np.any(np.isnan(vals)) else np.nan
    print(f"  noise={nf:5.1%}: range {np.nanmin(vals):.2f}–{np.nanmax(vals):.2f}, "
          f"trend={trend:+.2f}")

print("\nStochastic diagnostic (acf1) is informative when:")
print("  Values decrease with d → residuals whiten")
for i, nf in enumerate(noise_fracs):
    vals = acf_grid[i, :]
    trend = vals[-1] - vals[0] if not np.any(np.isnan(vals)) else np.nan
    print(f"  noise={nf:5.1%}: range {np.nanmin(vals):.3f}–{np.nanmax(vals):.3f}, "
          f"trend={trend:+.3f}")
