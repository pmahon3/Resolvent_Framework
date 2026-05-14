"""
Targeted diagnostics to pinpoint the remaining ~20% gap in η.

Current status: η = 2.405, theory = 3.0, gap = -19.8%

Hypotheses to test:
1. **Curvature contamination**: Linear fit captures f'(x₀) but also ~(h²/2)f'''(x₀)
   - For f(y) = sign(y)|y|^q, check if δ² has O(h⁴) component from curvature
   - Test: Fit δ² ~ c₁·h^η + c₂·h^4 to see if curvature term is significant

2. **Non-locality leakage**: r_eff/h ≈ 1.0 means we're averaging over ~1 bandwidth
   - Theory assumes LOCAL approximation (r_eff << h)
   - Test: Compare η at r_eff/h = 0.5 vs 1.0

3. **Query distribution bias**: Queries span |y| ∈ [0.008, 0.016]
   - Drift varies: f'(y) ~ q·|y|^(q-1), so f'(0.008) vs f'(0.016) differ by 2×
   - Test: Per-quartile η to see if heterogeneity flattens overall slope

4. **Finite sample bias in local fit**: WLS with n_eff ~ 2000-4000
   - Test: Compare η for different subsamples to estimate variance

5. **True drift approximation error**: Using f(y) = sign(y)|y|^q
   - Actual SDE might have small deviations from pure power law
   - Test: Compare empirical drift to analytic for query points
"""

import numpy as np
import matplotlib.pyplot as plt
import argparse
from pathlib import Path

import common_utils as cu
from tier1_scalar import simulate_scalar_system


def diagnose_gap(
    q: float = 1.5,
    sigma: float = 0.01,
    n: int = 15000,
    seed: int = 100,
):
    """
    Focused diagnostics for the η gap.
    """
    logger = cu.logger
    rng = cu.make_rng(seed)

    logger.info("=" * 70)
    logger.info("GAP ANALYSIS: Why is η = 2.4 instead of 3.0?")
    logger.info("=" * 70)

    # Simulate system
    y = simulate_scalar_system(n, q, sigma, rng=rng)

    # Prepare data
    X = y[:-1].reshape(-1, 1)
    Y = y[1:].reshape(-1, 1)

    # Z-score
    X_z, x_mean, x_std = cu.zscore(X, axis=0)
    Y_z, y_mean, y_std = cu.zscore(Y, axis=0)

    # True drift function
    def true_drift_fn(y_val):
        return np.sign(y_val) * np.abs(y_val)**q

    # Train/test split
    n_train = int(0.6 * len(X_z))
    X_train_z = X_z[:n_train]
    Y_train_z = Y_z[:n_train]
    X_test_z = X_z[n_train:]

    # Query selection (interior tail, 60-90 percentile)
    X_test_orig = X_test_z * x_std + x_mean
    abs_x_orig = np.abs(X_test_orig.flatten())

    p60 = np.percentile(abs_x_orig, 60)
    p90 = np.percentile(abs_x_orig, 90)
    interior_mask = (abs_x_orig >= p60) & (abs_x_orig <= p90)
    interior_indices = np.where(interior_mask)[0]

    n_queries = min(100, len(interior_indices))
    query_idx = rng.choice(interior_indices, size=n_queries, replace=False)
    query_points = X_test_z[query_idx]

    # Bandwidth grid
    n_eff = n_train / cu.iact(y[:n_train])
    h_star_z = n_eff**(-1 / (2*q + 1))

    # Extended grid with dense bias-regime coverage
    h_mult = np.array([0.5, 0.75, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0])
    h_fit_grid_z = h_mult * h_star_z

    logger.info(f"n_eff = {n_eff:.1f}, h*_z = {h_star_z:.4f}")
    logger.info(f"Query range: |y| ∈ [{p60:.4f}, {p90:.4f}]")
    logger.info("")

    # Compute δ² for all h
    results = {
        'h_fit': [],
        'mean_delta2': [],
        'std_delta2': [],
        'r_eff_over_h': [],
        'n_eff_mean': [],
        'cond_mean': [],
        'A_norm_mean': [],
    }

    for h_fit_z in h_fit_grid_z:
        delta2_list = []
        r_eff_list = []
        n_eff_list = []
        cond_list = []
        A_norm_list = []

        for x0 in query_points:
            result = cu.local_linear_mean(
                X_train_z, Y_train_z, x0, h=h_fit_z,
                ridge=1e-6, weight="gaussian"
            )

            # Bias δ²
            mu_model = result.mu
            x0_orig = x0 * x_std + x_mean
            mu_true = true_drift_fn(x0_orig)
            mu_model_orig = mu_model * y_std + y_mean
            delta2 = (mu_model_orig - mu_true)**2
            delta2_list.append(float(delta2.flatten()[0]))

            r_eff_list.append(result.r_eff)
            n_eff_list.append(result.n_eff)
            cond_list.append(result.cond)
            A_norm_list.append(np.linalg.norm(result.A))

        results['h_fit'].append(h_fit_z)
        results['mean_delta2'].append(np.mean(delta2_list))
        results['std_delta2'].append(np.std(delta2_list))
        results['r_eff_over_h'].append(np.mean(r_eff_list) / h_fit_z)
        results['n_eff_mean'].append(np.mean(n_eff_list))
        results['cond_mean'].append(np.nanmean(cond_list))
        results['A_norm_mean'].append(np.mean(A_norm_list))

    for key in results:
        results[key] = np.array(results[key])

    # ========================================================================
    # DIAGNOSTIC 1: Curvature contamination
    # ========================================================================
    logger.info("=" * 70)
    logger.info("DIAGNOSTIC 1: Curvature Contamination")
    logger.info("=" * 70)
    logger.info("Testing if δ² ~ c₁·h^η + c₂·h⁴ (curvature term)")
    logger.info("")

    # Find bias regime (after minimum)
    min_idx = np.argmin(results['mean_delta2'])
    fit_start = min_idx + 1

    h_bias = results['h_fit'][fit_start:]
    delta2_bias = results['mean_delta2'][fit_start:]

    # Fit 1: Pure power law δ² ~ c₁·h^η
    log_h = np.log10(h_bias)
    log_delta2 = np.log10(delta2_bias)
    eta_pure, intercept_pure = np.polyfit(log_h, log_delta2, 1)

    logger.info(f"Pure power law: δ² ~ h^{eta_pure:.3f}")
    logger.info(f"  Intercept: {intercept_pure:.3f}")

    # Fit 2: With curvature term δ² ~ c₁·h^η + c₂·h⁴
    # Use nonlinear least squares in linear space
    from scipy.optimize import curve_fit
    def model_with_curvature(h, c1, eta, c2):
        return c1 * h**eta + c2 * h**4

    try:
        # Initial guess: c1 from pure fit, η=eta_pure, c2=0
        c1_init = 10**(intercept_pure)
        popt, _ = curve_fit(
            model_with_curvature, h_bias, delta2_bias,
            p0=[c1_init, eta_pure, 0],
            bounds=([0, 2.0, -np.inf], [np.inf, 4.0, np.inf]),
            maxfev=5000
        )
        c1_fit, eta_fit, c2_fit = popt

        # Evaluate contribution of curvature term
        curvature_contrib = c2_fit * h_bias**4
        bias_contrib = c1_fit * h_bias**eta_fit
        frac_curvature = np.abs(curvature_contrib / bias_contrib)

        logger.info(f"")
        logger.info(f"With curvature: δ² ~ {c1_fit:.3e}·h^{eta_fit:.3f} + {c2_fit:.3e}·h⁴")
        logger.info(f"  η changes: {eta_pure:.3f} → {eta_fit:.3f} (Δ = {eta_fit - eta_pure:+.3f})")
        logger.info(f"  Curvature contribution at h={h_bias[-1]:.3f}: {frac_curvature[-1]:.1%}")
        logger.info(f"  Mean curvature fraction: {np.mean(frac_curvature):.1%}")

        if np.abs(c2_fit) > 1e-10 and np.mean(frac_curvature) > 0.1:
            logger.info("  → **Curvature contamination detected!**")
        else:
            logger.info("  → Curvature term negligible")
    except Exception as e:
        logger.warning(f"Curvature fit failed: {e}")

    # ========================================================================
    # DIAGNOSTIC 2: Non-locality analysis
    # ========================================================================
    logger.info("")
    logger.info("=" * 70)
    logger.info("DIAGNOSTIC 2: Non-locality Leakage")
    logger.info("=" * 70)
    logger.info("Comparing η for different locality thresholds")
    logger.info("")

    for r_threshold in [0.5, 0.7, 1.0, 1.02]:
        mask = results['r_eff_over_h'][fit_start:] <= r_threshold
        if mask.sum() < 3:
            logger.info(f"r_eff/h ≤ {r_threshold}: Only {mask.sum()} points, skipping")
            continue

        h_local = h_bias[mask]
        delta2_local = delta2_bias[mask]

        log_h_local = np.log10(h_local)
        log_delta2_local = np.log10(delta2_local)
        eta_local, _ = np.polyfit(log_h_local, log_delta2_local, 1)

        logger.info(f"r_eff/h ≤ {r_threshold:.2f}: η = {eta_local:.3f} ({mask.sum()} points)")

    # ========================================================================
    # DIAGNOSTIC 3: Query heterogeneity
    # ========================================================================
    logger.info("")
    logger.info("=" * 70)
    logger.info("DIAGNOSTIC 3: Query Heterogeneity")
    logger.info("=" * 70)
    logger.info("Per-quartile η to check if drift variation flattens slope")
    logger.info("")

    query_points_orig = query_points * x_std + x_mean
    abs_query_orig = np.abs(query_points_orig.flatten())

    quartiles = [
        (0, 25, "Q1 (smallest |y|)"),
        (25, 50, "Q2"),
        (50, 75, "Q3"),
        (75, 100, "Q4 (largest |y|)"),
    ]

    for p_low, p_high, label in quartiles:
        p_low_val = np.percentile(abs_query_orig, p_low)
        p_high_val = np.percentile(abs_query_orig, p_high)
        bin_mask = (abs_query_orig >= p_low_val) & (abs_query_orig < p_high_val)

        if bin_mask.sum() < 10:
            continue

        bin_queries = query_points[bin_mask]

        # Recompute δ² for this bin
        bin_delta2 = []
        for h_fit_z in h_fit_grid_z:
            delta2_list = []
            for x0 in bin_queries:
                result = cu.local_linear_mean(
                    X_train_z, Y_train_z, x0, h=h_fit_z,
                    ridge=1e-6, weight="gaussian"
                )
                mu_model = result.mu
                x0_orig = x0 * x_std + x_mean
                mu_true = true_drift_fn(x0_orig)
                mu_model_orig = mu_model * y_std + y_mean
                delta2 = (mu_model_orig - mu_true)**2
                delta2_list.append(float(delta2.flatten()[0]))
            bin_delta2.append(np.mean(delta2_list))

        bin_delta2 = np.array(bin_delta2)

        # Fit in bias regime
        bin_delta2_bias = bin_delta2[fit_start:]
        log_delta2_bin = np.log10(bin_delta2_bias)
        eta_bin, _ = np.polyfit(log_h, log_delta2_bin, 1)

        logger.info(f"{label}: |y| ∈ [{p_low_val:.4f}, {p_high_val:.4f}]")
        logger.info(f"  η = {eta_bin:.3f} ({bin_mask.sum()} queries)")

    # ========================================================================
    # DIAGNOSTIC 4: Empirical vs analytic drift check
    # ========================================================================
    logger.info("")
    logger.info("=" * 70)
    logger.info("DIAGNOSTIC 4: True Drift Approximation")
    logger.info("=" * 70)
    logger.info("Checking if f(y) = sign(y)|y|^q matches empirical drift")
    logger.info("")

    # Compute empirical drift using large bandwidth (nearly global)
    h_large = 10.0 * h_star_z
    drift_errors = []

    for x0 in query_points[:20]:  # Check first 20
        result = cu.local_linear_mean(
            X_train_z, Y_train_z, x0, h=h_large,
            ridge=1e-6, weight="gaussian"
        )

        mu_empirical = result.mu  # In z-space
        x0_orig = x0 * x_std + x_mean
        mu_analytic = true_drift_fn(x0_orig)

        # Convert to same units
        mu_empirical_orig = mu_empirical * y_std + y_mean

        error = np.abs(mu_empirical_orig - mu_analytic) / (np.abs(mu_analytic) + 1e-10)
        drift_errors.append(float(error.flatten()[0]))

    logger.info(f"Drift approximation error (h={h_large:.3f}, nearly global):")
    logger.info(f"  Mean relative error: {np.mean(drift_errors):.2%}")
    logger.info(f"  Max relative error: {np.max(drift_errors):.2%}")

    if np.mean(drift_errors) > 0.05:
        logger.info("  → **Significant drift approximation error!**")
    else:
        logger.info("  → Analytic drift accurate")

    # ========================================================================
    # Summary
    # ========================================================================
    logger.info("")
    logger.info("=" * 70)
    logger.info("SUMMARY")
    logger.info("=" * 70)
    logger.info(f"Current η = {eta_pure:.3f} (theory: 3.0, gap: {eta_pure - 3.0:.3f})")
    logger.info("")
    logger.info("Check the diagnostics above to identify the dominant source of the gap.")


def main():
    parser = argparse.ArgumentParser(description="Gap analysis diagnostics")
    parser.add_argument("--q", type=float, default=1.5)
    parser.add_argument("--sigma", type=float, default=0.01)
    parser.add_argument("--n", type=int, default=15000)
    parser.add_argument("--seed", type=int, default=100)

    args = parser.parse_args()

    # Setup logging
    from logging_utils import setup_logger
    log_file = Path(__file__).parent / "logs" / "gap_analysis.log"
    logger = setup_logger("gap_analysis", log_file=log_file, level="INFO")

    # Configure common_utils logger
    cu_logger = __import__('logging').getLogger('common_utils')
    cu_logger.setLevel(__import__('logging').INFO)
    for handler in logger.handlers:
        cu_logger.addHandler(handler)

    diagnose_gap(
        q=args.q,
        sigma=args.sigma,
        n=args.n,
        seed=args.seed,
    )


if __name__ == "__main__":
    main()
