"""
Experiment 1: Lorenz-63 dimension sweep.

Demonstrates the divergence-based embedding diagnostic:
- Generate Lorenz-63 trajectory
- Observe scalar (x-component)
- Embed at dimensions d = 1, 2, ..., 7
- At each d: compute mean σ(z) and mean div(z)
- Show: σ decreases and div stabilizes at d = 3 (correct dimension)

Expected results:
- Lorenz Lyapunov sum ≈ -(σ + β + 1) + 2*σ ≈ -13.66 (continuous time)
- In discrete time with dt=0.01: sum ≈ exp(Λ_sum * dt) - 1 per step
- div(A) should approach this as d → 3+
"""

import numpy as np
import matplotlib.pyplot as plt
from reconstruction import lorenz63, delay_embed, dimension_sweep, map_attractor

# --- Parameters ---
N = 50000          # time series length
dt = 0.01          # integration step
L = 10             # lag (10 steps = 0.1 time units, ~1/10 of orbital period)
h = 2.0            # bandwidth (will need tuning)
n_query = 500      # query points per dimension
seed = 42

# --- Generate Lorenz data ---
print("Generating Lorenz-63 trajectory...")
traj = lorenz63(N, dt=dt, seed=seed)
y = traj[:, 0]  # observe x-component

print(f"Time series: N={len(y)}, range=[{y.min():.2f}, {y.max():.2f}]")

# --- Dimension sweep ---
print("\nDimension sweep (d = 1 to 7)...")
results = dimension_sweep(y, L=L, d_range=range(1, 8), h=h,
                          n_query=n_query, seed=seed)

# --- Print results ---
print("\n  d | mean σ(z) | std σ(z) | mean div(z) | std div(z) | n_success")
print("----+-----------+----------+-------------+------------+----------")
for i, d in enumerate(results['d']):
    print(f"  {d} | {results['mean_sigma'][i]:9.4f} | {results['std_sigma'][i]:8.4f} | "
          f"{results['mean_div'][i]:11.4f} | {results['std_div'][i]:10.4f} | "
          f"{results['n_success'][i]:>5}")

# --- Expected Lyapunov sum ---
# Lorenz continuous-time: λ₁ ≈ 0.91, λ₂ ≈ 0, λ₃ ≈ -14.57
# Sum ≈ -13.66
# Discrete-time Jacobian trace: approximately σ + ρ + β in some scaling
# For dt=0.01: det(I + dt*DF) ≈ 1 + dt*tr(DF) = 1 + dt*(-σ - 1 - β) ≈ 0.8634
# So tr(A) ≈ d + dt*(sum of Lyapunov exponents) for d-dimensional embedding
# Actually for delay embedding it's more complex — the Jacobian is in delay coords
print(f"\nExpected: σ(z) → 0 and div(z) stabilizes as d → 3+")

# --- Plot ---
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

ax1.errorbar(results['d'], results['mean_sigma'],
             yerr=results['std_sigma'], fmt='o-', capsize=4)
ax1.set_xlabel('Embedding dimension d')
ax1.set_ylabel('Mean noise amplitude σ(z)')
ax1.set_title('Lorenz-63: Noise vs embedding dimension')
ax1.axhline(0, color='gray', linestyle='--', alpha=0.5)

ax2.errorbar(results['d'], results['mean_div'],
             yerr=results['std_div'], fmt='s-', capsize=4, color='tab:orange')
ax2.set_xlabel('Embedding dimension d')
ax2.set_ylabel('Mean divergence tr(A(z))')
ax2.set_title('Lorenz-63: Divergence vs embedding dimension')

plt.tight_layout()
plt.savefig('lorenz_dimension_sweep.png', dpi=150)
plt.show()

print("\nFigure saved: lorenz_dimension_sweep.png")
