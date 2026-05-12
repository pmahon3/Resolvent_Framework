"""
Experiment 2: Bandwidth stability of div vs σ.

Fix d=3 (correct for Lorenz), sweep h from 2 to 12.
Show: ⟨div⟩ is approximately h-independent while ⟨σ⟩ varies strongly.
This demonstrates that divergence is an intrinsic diagnostic.
"""

import numpy as np
import matplotlib.pyplot as plt
import time
from reconstruction import lorenz63, delay_embed, map_attractor

# --- Parameters ---
N = 50000
dt = 0.01
d = 3          # correct embedding dimension for Lorenz
L = 10         # lag
n_query = 300
seed = 42

# --- Generate data ---
print("Generating Lorenz-63 trajectory...")
traj = lorenz63(N, dt=dt, seed=seed)
y = traj[:, 0]
Z = delay_embed(y, d=d, L=L)
Z_t, Z_next = Z[:-1], Z[1:]
print(f"Embedded: {Z_t.shape[0]} points in R^{d}")

# --- Bandwidth sweep ---
h_values = np.array([2.0, 3.0, 4.0, 5.0, 6.0, 8.0, 10.0, 12.0])

results = {'h': [], 'mean_div': [], 'std_div': [],
           'mean_sigma': [], 'std_sigma': [], 'mean_neff': []}

print("\nBandwidth sweep:")
print("  h   | mean div  | std div  | mean σ   | std σ    | mean n_eff")
print("------+-----------+----------+----------+----------+-----------")

for h in h_values:
    t0 = time.time()
    res = map_attractor(Z_t, Z_next, h=h, n_query=n_query, seed=seed)
    elapsed = time.time() - t0

    if len(res) < 10:
        print(f"  {h:4.1f} | INSUFFICIENT DATA")
        continue

    divs = np.array([r.div for r in res])
    sigmas = np.array([r.sigma for r in res])
    neffs = np.array([r.n_eff for r in res])

    results['h'].append(h)
    results['mean_div'].append(np.mean(divs))
    results['std_div'].append(np.std(divs))
    results['mean_sigma'].append(np.mean(sigmas))
    results['std_sigma'].append(np.std(sigmas))
    results['mean_neff'].append(np.mean(neffs))

    print(f"  {h:4.1f} | {np.mean(divs):9.4f} | {np.std(divs):8.4f} | "
          f"{np.mean(sigmas):8.4f} | {np.std(sigmas):8.4f} | "
          f"{np.mean(neffs):8.0f}  ({elapsed:.1f}s)")

# --- Reference: Lorenz continuous-time Lyapunov sum ---
# λ₁ ≈ 0.91, λ₂ ≈ 0, λ₃ ≈ -14.57 → sum ≈ -13.66
# Discrete-time (dt=0.01): per-step divergence ≈ dt * (-σ - 1 - β)
# where σ=10, β=8/3: -10 - 1 - 8/3 ≈ -13.67
# So ⟨tr(A)⟩ should be ≈ d + dt * Lyapunov_sum ≈ 3 + 0.01*(-13.67) ≈ 2.86
# Actually for delay coordinates it's different — need to think more carefully
lyap_sum_ct = -10 - 1 - 8/3  # = -(σ + 1 + β) for Lorenz
print(f"\nContinuous-time Lyapunov sum: {lyap_sum_ct:.2f}")
print(f"Expected discrete-time div (d={d}, dt={dt}): ~{d + dt*lyap_sum_ct:.4f}")

# --- Plot ---
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

h_arr = np.array(results['h'])

ax1.errorbar(h_arr, results['mean_div'], yerr=results['std_div'],
             fmt='o-', capsize=4, color='tab:blue')
ax1.axhline(d + dt * lyap_sum_ct, color='red', linestyle='--',
            alpha=0.7, label=f'Expected: {d + dt*lyap_sum_ct:.3f}')
ax1.set_xlabel('Bandwidth h')
ax1.set_ylabel('Mean divergence tr(A)')
ax1.set_title('Divergence vs bandwidth (d=3, Lorenz)')
ax1.legend()

ax2.errorbar(h_arr, results['mean_sigma'], yerr=results['std_sigma'],
             fmt='s-', capsize=4, color='tab:orange')
ax2.set_xlabel('Bandwidth h')
ax2.set_ylabel('Mean noise amplitude σ')
ax2.set_title('Noise amplitude vs bandwidth (d=3, Lorenz)')

plt.tight_layout()
plt.savefig('bandwidth_stability.png', dpi=150)
print("\nFigure saved: bandwidth_stability.png")
plt.close()
