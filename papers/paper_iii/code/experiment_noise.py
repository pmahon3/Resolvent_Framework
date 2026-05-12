"""
Experiment 3: Lorenz + observational noise.

Add Gaussian noise to the scalar time series at varying amplitudes.
Show:
- div still converges with d (robust to moderate noise)
- σ has an irreducible floor proportional to the true noise
- At high noise, div convergence degrades
"""

import numpy as np
import matplotlib.pyplot as plt
import time
from reconstruction import lorenz63, delay_embed, dimension_sweep

# --- Parameters ---
N = 50000
dt = 0.01
L = 10
h = 5.0        # moderate bandwidth
n_query = 200
seed = 42

# --- Generate clean Lorenz data ---
print("Generating Lorenz-63 trajectory...")
traj = lorenz63(N, dt=dt, seed=seed)
y_clean = traj[:, 0]
y_std = y_clean.std()
print(f"Clean signal std: {y_std:.2f}")

# --- Noise levels (as fraction of signal std) ---
noise_fracs = [0.0, 0.01, 0.05, 0.10, 0.20]
rng = np.random.default_rng(seed + 1)

print("\n" + "=" * 70)
print("DIMENSION SWEEP AT EACH NOISE LEVEL")
print("=" * 70)

all_results = {}

for nf in noise_fracs:
    noise_amp = nf * y_std
    y_noisy = y_clean + noise_amp * rng.standard_normal(len(y_clean))

    print(f"\n--- Noise fraction: {nf:.0%} (amplitude: {noise_amp:.3f}) ---")
    print("  d | mean_sigma | mean_div | n_success")

    t0 = time.time()
    results = dimension_sweep(y_noisy, L=L, d_range=range(2, 7),
                              h=h, n_query=n_query, seed=seed)
    elapsed = time.time() - t0

    for i, d in enumerate(results['d']):
        print(f"  {int(d)} | {results['mean_sigma'][i]:10.4f} | "
              f"{results['mean_div'][i]:8.4f} | {int(results['n_success'][i])}")

    all_results[nf] = results
    print(f"  ({elapsed:.1f}s)")

# --- Plot ---
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

colors = plt.cm.viridis(np.linspace(0, 0.8, len(noise_fracs)))

for nf, color in zip(noise_fracs, colors):
    r = all_results[nf]
    label = f'{nf:.0%} noise' if nf > 0 else 'Clean'
    axes[0].plot(r['d'], r['mean_div'], 'o-', color=color, label=label)
    axes[1].plot(r['d'], r['mean_sigma'], 's-', color=color, label=label)

axes[0].set_xlabel('Embedding dimension d')
axes[0].set_ylabel('Mean divergence tr(A)')
axes[0].set_title('Divergence convergence under noise')
axes[0].legend(fontsize=8)

axes[1].set_xlabel('Embedding dimension d')
axes[1].set_ylabel('Mean noise amplitude σ')
axes[1].set_title('Residual noise under observational noise')
axes[1].legend(fontsize=8)

plt.tight_layout()
plt.savefig('noise_robustness.png', dpi=150)
print("\nFigure saved: noise_robustness.png")
plt.close()

# --- Summary ---
print("\n" + "=" * 70)
print("SUMMARY: div at d=5 vs noise level")
print("=" * 70)
print("  noise% |  div(d=5)")
for nf in noise_fracs:
    r = all_results[nf]
    idx = list(r['d']).index(5)
    print(f"  {nf:5.1%}  | {r['mean_div'][idx]:8.4f}")
