#!/usr/bin/env python3
"""
Diagnose why oracle locality curve is flat.
Check if model bias is actually changing with h_fit.
"""

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

import common_utils as cu
from tier1_scalar import simulate_scalar_system

def diagnose_model_bias():
    """Check if local linear model predictions change with h_fit."""

    # Setup
    q = 1.5
    sigma = 0.01
    n = 15000
    seed = 60
    rng = np.random.default_rng(seed)

    # Generate data
    y = simulate_scalar_system(n, q=q, sigma=sigma, rng=rng)

    # Prepare data
    n_train = int(0.6 * n)
    y_train = y[:n_train]
    y_test = y[n_train:]

    X_train = y_train[:-1].reshape(-1, 1)
    Y_train = y_train[1:].reshape(-1, 1)
    X_test = y_test[:-1].reshape(-1, 1)
    Y_test = y_test[1:].reshape(-1, 1)

    # Z-score
    X_train_z, x_mean, x_std = cu.zscore(X_train, axis=0)
    Y_train_z, y_mean, y_std = cu.zscore(Y_train, axis=0)
    X_test_z = (X_test - x_mean) / x_std
    Y_test_z = (Y_test - y_mean) / y_std

    # Select a single test point (near mean)
    test_idx = np.argmin(np.abs(X_test_z))
    x0 = X_test_z[test_idx]
    x0_orig = X_test[test_idx]

    print(f"Test point: x0 = {x0_orig[0]:.4f} (z-scored: {x0[0]:.4f})")

    # True oracle prediction
    mu_true = np.sign(x0_orig[0]) * np.abs(x0_orig[0])**q
    print(f"Oracle: μ_true = {mu_true:.6f}, σ = {sigma:.6f}")

    # Try different h_fit values
    iact_val = cu.iact(y_train)
    n_eff = len(y_train) / max(iact_val, 1.0)
    h_star = n_eff**(-1/(2*q + 1))

    h_mult = np.array([0.25, 0.5, 1.0, 2.0, 4.0, 8.0])
    h_fit_grid = h_mult * h_star

    print(f"\nh_star = {h_star:.4f}, n_eff = {n_eff:.1f}")
    print(f"\nModel predictions at x0 = {x0_orig[0]:.4f}:")
    print("-" * 80)
    print(f"{'h_fit':>10} {'h/h*':>8} {'μ_model':>12} {'σ_model':>12} {'Bias':>12} {'Bias %':>10}")
    print("-" * 80)

    mu_models = []
    sigma_models = []
    biases = []

    for h_fit in h_fit_grid:
        # Gaussian weights
        result = cu.local_linear_mean(
            X_train_z, Y_train_z, x0, h=h_fit, ridge=1e-6, weight="gaussian"
        )

        mu_model_z = result.mu
        sigma_model_z = np.sqrt(result.Sigma) if result.Sigma > 0 else 0.01

        # Convert back to original coordinates
        mu_model = mu_model_z * y_std + y_mean
        sigma_model = sigma_model_z * y_std

        # Bias
        bias = mu_model - mu_true
        bias_pct = 100 * bias / (abs(mu_true) + 1e-10)

        mu_models.append(float(mu_model))
        sigma_models.append(float(sigma_model))
        biases.append(float(bias))

        print(f"{float(h_fit):>10.4f} {float(h_fit)/h_star:>8.2f} {float(mu_model):>12.6f} "
              f"{float(sigma_model):>12.6f} {float(bias):>12.6f} {float(bias_pct):>10.2f}")

    print("-" * 80)
    print(f"Oracle:    {'':>8} {float(mu_true):>12.6f} {sigma:>12.6f} {'0.000000':>12} {'0.00':>10}")
    print("-" * 80)

    # Compute JS divergence between oracle N(μ_true, σ²) and model N(μ_model, σ_model²)
    print(f"\nJS divergence between oracle and model conditionals:")
    print("-" * 60)
    print(f"{'h_fit':>10} {'μ_model':>12} {'σ_model':>12} {'JS (analytical)':>18}")
    print("-" * 60)

    for i, h_fit in enumerate(h_fit_grid):
        mu_m = mu_models[i]
        sigma_m = sigma_models[i]

        # Analytical JS divergence between two Gaussians
        # JS(N(μ1,σ1²) || N(μ2,σ2²))
        # For two 1D Gaussians, we can compute this exactly
        # But let's use sampling for consistency
        n_samples = 10000
        samples_oracle = rng.normal(float(mu_true), sigma, n_samples)
        samples_model = rng.normal(mu_m, sigma_m, n_samples)

        js_div = cu.js_divergence(samples_oracle, samples_model, method="hist", bins=50)

        print(f"{float(h_fit):>10.4f} {mu_m:>12.6f} {sigma_m:>12.6f} {js_div:>18.6f}")

    print("-" * 60)

    # Plot
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))

    # Plot 1: Model mean vs h_fit
    ax = axes[0, 0]
    ax.semilogx(h_fit_grid, mu_models, 'o-', markersize=8, linewidth=2, label='Model')
    ax.axhline(float(mu_true), color='r', linestyle='--', linewidth=2, label='Oracle')
    ax.axvline(h_star, color='gray', linestyle=':', alpha=0.5)
    ax.set_xlabel('h_fit', fontsize=11)
    ax.set_ylabel('Mean prediction μ', fontsize=11)
    ax.set_title('Model Mean vs h_fit', fontsize=12)
    ax.legend()
    ax.grid(True, alpha=0.3)

    # Plot 2: Model std vs h_fit
    ax = axes[0, 1]
    ax.semilogx(h_fit_grid, sigma_models, 'o-', markersize=8, linewidth=2, label='Model')
    ax.axhline(sigma, color='r', linestyle='--', linewidth=2, label='Oracle')
    ax.axvline(h_star, color='gray', linestyle=':', alpha=0.5)
    ax.set_xlabel('h_fit', fontsize=11)
    ax.set_ylabel('Std prediction σ', fontsize=11)
    ax.set_title('Model Std vs h_fit', fontsize=12)
    ax.legend()
    ax.grid(True, alpha=0.3)

    # Plot 3: Bias vs h_fit
    ax = axes[1, 0]
    ax.semilogx(h_fit_grid, np.abs(biases), 'o-', markersize=8, linewidth=2)
    ax.axvline(h_star, color='gray', linestyle=':', alpha=0.5)
    ax.set_xlabel('h_fit', fontsize=11)
    ax.set_ylabel('|Bias| = |μ_model - μ_true|', fontsize=11)
    ax.set_title('Model Bias vs h_fit (should increase)', fontsize=12)
    ax.grid(True, alpha=0.3)

    # Plot 4: Relative bias percentage
    ax = axes[1, 1]
    bias_pct = 100 * np.abs(biases) / (abs(float(mu_true)) + 1e-10)
    ax.semilogx(h_fit_grid, bias_pct, 'o-', markersize=8, linewidth=2)
    ax.axvline(h_star, color='gray', linestyle=':', alpha=0.5)
    ax.set_xlabel('h_fit', fontsize=11)
    ax.set_ylabel('Relative bias (%)', fontsize=11)
    ax.set_title('Relative Bias vs h_fit', fontsize=12)
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    fig_path = Path("figures") / "model_bias_diagnostic.png"
    fig.savefig(fig_path, dpi=150, bbox_inches='tight')
    print(f"\nSaved diagnostic plot: {fig_path}")

    return {
        "h_fit_grid": h_fit_grid,
        "mu_models": np.array(mu_models),
        "sigma_models": np.array(sigma_models),
        "biases": np.array(biases),
        "mu_true": float(mu_true),
        "sigma_true": sigma,
    }


if __name__ == "__main__":
    results = diagnose_model_bias()
