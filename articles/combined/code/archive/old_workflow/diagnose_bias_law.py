"""
Diagnostic: Check pure bias law δ²(y₀; h_fit) ∝ h_fit^(2s)

This script tests the local fit bias directly without divergence computation,
following the user's diagnostic framework to identify remaining sources of
slope flattening.
"""

import numpy as np
import matplotlib.pyplot as plt
import argparse
from pathlib import Path

from src.core import common_utils as cu
from src.simulation.tier1_scalar import simulate_scalar_system


def diagnose_bias_law(
    q: float = 1.5,
    sigma: float = 0.01,
    n: int = 15000,
    seed: int = 100,
    interior_tail_range: tuple = (0.6, 0.8),
    kernel: str = "gaussian",
):
    """
    Comprehensive bias diagnostics following user's 8-point framework.

    Parameters
    ----------
    q : float
        Power in drift (smoothness s ≈ q)
    sigma : float
        Noise level
    n : int
        Sample size
    seed : int
        Random seed
    interior_tail_range : tuple
        (min, max) for |y₀| to avoid both origin and boundary
    """
    logger = cu.logger
    rng = cu.make_rng(seed)

    logger.info("=" * 70)
    logger.info("DIAGNOSTIC: Pure Bias Law δ² ∝ h^(2s)")
    logger.info("=" * 70)
    logger.info(f"Config: q={q}, sigma={sigma}, n={n}, seed={seed}, kernel={kernel}")
    logger.info(f"Interior tail range: |y₀| ∈ {interior_tail_range}")
    logger.info(f"Theory: 2s = {2*q:.1f}")

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

    # DIAGNOSTIC 2: Interior tail queries (avoid boundary)
    logger.info("")
    logger.info("--- Query Selection (Interior Tail) ---")

    # Work in ORIGINAL coordinates (before z-scoring) to match user's specification
    X_test_orig = X_test_z * x_std + x_mean
    abs_x_orig = np.abs(X_test_orig.flatten())

    logger.info(f"Original data range: [{X_test_orig.min():.3f}, {X_test_orig.max():.3f}]")
    logger.info(f"Data std: {x_std:.3f}, mean: {x_mean:.6f}")

    # If data doesn't reach interior_tail_range, use percentile-based selection
    y_min_orig, y_max_orig = interior_tail_range

    if abs_x_orig.max() < y_min_orig:
        # Data doesn't reach the specified range - use top percentiles instead
        logger.warning(f"Data doesn't reach |y| = {y_min_orig:.1f} (max = {abs_x_orig.max():.3f})")
        logger.info("Switching to percentile-based interior tail: [60th, 90th percentile]")

        p60 = np.percentile(abs_x_orig, 60)
        p90 = np.percentile(abs_x_orig, 90)

        interior_mask = (abs_x_orig >= p60) & (abs_x_orig <= p90)
        interior_indices = np.where(interior_mask)[0]

        # Check boundary (top 5%)
        p95 = np.percentile(abs_x_orig, 95)
        boundary_mask = abs_x_orig > p95

        logger.info(f"Interior tail: |y| ∈ [{p60:.4f}, {p90:.4f}] (60-90 percentile)")
        logger.info(f"Boundary: |y| > {p95:.4f} (95 percentile)")
    else:
        # Use specified range
        interior_mask = (abs_x_orig >= y_min_orig) & (abs_x_orig <= y_max_orig)
        interior_indices = np.where(interior_mask)[0]

        # Boundary is near ±1 (clamp limit)
        boundary_mask = abs_x_orig > 0.9

    logger.info(f"Total test points: {len(X_test_z)}")
    logger.info(f"Interior tail (|y| ∈ [{y_min_orig:.1f}, {y_max_orig:.1f}]): {interior_mask.sum()} points ({100*interior_mask.sum()/len(X_test_z):.1f}%)")
    logger.info(f"Near boundary (|y| > 0.9): {boundary_mask.sum()} points ({100*boundary_mask.sum()/len(X_test_z):.1f}%)")

    if len(interior_indices) < 50:
        logger.warning(f"Only {len(interior_indices)} interior points! May need to adjust range.")
        n_queries = len(interior_indices)
    else:
        n_queries = min(100, len(interior_indices))

    query_idx = rng.choice(interior_indices, size=n_queries, replace=False)
    query_points = X_test_z[query_idx]

    # Log query distribution by bins (in original coordinates)
    logger.info("")
    logger.info("--- Query Distribution by |y₀| Bins ---")

    query_points_orig = query_points * x_std + x_mean
    abs_query_orig = np.abs(query_points_orig.flatten())

    # Use quartiles of the actual query distribution
    q25 = np.percentile(abs_query_orig, 25)
    q50 = np.percentile(abs_query_orig, 50)
    q75 = np.percentile(abs_query_orig, 75)
    q100 = abs_query_orig.max()

    bins = [(0, q25), (q25, q50), (q50, q75), (q75, q100)]
    for b_min, b_max in bins:
        mask = (abs_query_orig >= b_min) & (abs_query_orig < b_max)
        logger.info(f"  |y₀| ∈ [{b_min:.4f}, {b_max:.4f}): {mask.sum()} queries ({100*mask.sum()/n_queries:.1f}%)")

    # Bandwidth grid (IN Z-SCORED UNITS)
    # Key fix: h must be in the same units as the fit space (z-scored)
    # Theory: h* ~ n_eff^(-1/(2s+d)) in the space where we measure distances
    # For z-scored data, typical scale is ~1, so we define h* relative to that
    n_eff = n_train / cu.iact(y[:n_train])

    # Compute h* in z-scored space
    # Typical inter-point distance in z-space is ~1 (since std=1 after z-scoring)
    # Use standard rate-optimal bandwidth formula
    h_star_z = n_eff**(-1 / (2*q + 1))  # This gives h* for z-scored space

    # Grid multipliers: dense coverage in bias regime with locality guard
    # Key insight: Need LARGER h for bias regime, but stay local (r_eff/h < 0.7)
    # Dense mid-range points (0.38, 0.46, 0.55, etc.) for wider fit window in bias regime
    h_mult = np.array([0.5, 0.75, 1.0, 1.5, 2.0, 2.5, 3.0, 3.38, 3.76, 4.14, 4.5, 5.0, 5.5, 6.0])
    h_fit_grid_z = h_mult * h_star_z

    logger.info("")
    logger.info(f"--- Bandwidth Grid in Z-scored Units (h*_z = {h_star_z:.4f}) ---")
    logger.info(f"h_fit_z: {h_fit_grid_z}")
    logger.info(f"Grid spans {np.log10(h_fit_grid_z[-1]/h_fit_grid_z[0]):.2f} decades")
    logger.info(f"Note: All distances, weights, and fits computed in z-scored space")

    # Storage for diagnostics
    results = {
        'h_fit': [],
        'mean_delta2': [],
        'median_delta2': [],
        'iqr_delta2': [],
        'n_eff_mean': [],
        'n_eff_std': [],
        'cond_mean': [],
        'A_norm_mean': [],
        'A_norm_std': [],
        'frac_A_small': [],  # Fraction with ||A|| < 1e-6
        'r_eff_mean': [],     # Mean effective radius
        'r_eff_over_h': [],   # Mean r_eff/h ratio (locality metric)
        'sse_ratio_mean': [],  # Mean SSE_lin/SSE_const
    }

    logger.info("")
    logger.info("=" * 70)
    logger.info("DIAGNOSTIC 1: Pure Bias Law (δ² vs h_fit)")
    logger.info("=" * 70)

    for idx_h, h_fit_z in enumerate(h_fit_grid_z):
        logger.info(f"\n--- h_fit_z = {h_fit_z:.4f} ---")

        delta2_list = []
        n_eff_list = []
        cond_list = []
        A_norm_list = []
        r_eff_list = []
        sse_ratio_list = []

        # For first and last h, log extended diagnostics from first query
        log_extended = (idx_h == 0 or idx_h == len(h_fit_grid_z) - 1)

        for i, x0 in enumerate(query_points):
            # Fit local linear model IN Z-SCORED SPACE with h in z-units
            result = cu.local_linear_mean(
                X_train_z, Y_train_z, x0, h=h_fit_z,
                ridge=1e-6, weight=kernel
            )

            # Log extended diagnostics for first query at first/last h
            if log_extended and i == 0:
                logger.info("  --- Extended Weight Diagnostics (first query) ---")
                logger.info(f"    sum_w    = {result.sum_w:.6e}")
                logger.info(f"    sum_w²   = {result.sum_w2:.6e}")
                logger.info(f"    w_p10    = {result.w_p10:.6e}")
                logger.info(f"    w_p50    = {result.w_p50:.6e}")
                logger.info(f"    w_p90    = {result.w_p90:.6e}")
                logger.info(f"    r_eff    = {result.r_eff:.6f}")
                logger.info(f"    r_eff/h  = {result.r_eff/h_fit_z:.6f}")
                logger.info(f"    med_dist = {result.median_dist:.6f}")
                logger.info(f"    cond     = {result.cond:.4e}")
                logger.info(f"    ||A||    = {np.linalg.norm(result.A):.6f}")
                sse_ratio = result.sse_linear / result.sse_const if result.sse_const > 0 else np.nan
                logger.info(f"    SSE_lin/SSE_const = {sse_ratio:.6f}")
                logger.info("")

            # DIAGNOSTIC 3: Effective sample size & conditioning
            # Use the diagnostic field from LocalLinearResult (computed from raw weights)
            n_eff = result.n_eff
            n_eff_list.append(n_eff)

            # Condition number from LocalLinearResult
            cond_num = result.cond
            cond_list.append(cond_num)

            # DIAGNOSTIC 4: Check if fit is actually linear
            A_norm = np.linalg.norm(result.A)
            A_norm_list.append(A_norm)

            # Store locality metrics
            r_eff_list.append(result.r_eff)
            sse_ratio = result.sse_linear / result.sse_const if result.sse_const > 0 else np.nan
            sse_ratio_list.append(sse_ratio)

            # Get model prediction
            mu_model = result.mu

            # Get true prediction
            x0_orig = x0 * x_std + x_mean
            mu_true = true_drift_fn(x0_orig)

            # Convert model prediction to original coordinates
            mu_model_orig = mu_model * y_std + y_mean

            # DIAGNOSTIC 1: Bias δ²
            delta2 = (mu_model_orig - mu_true)**2
            delta2_list.append(float(delta2.flatten()[0]))

        delta2_arr = np.array(delta2_list)
        n_eff_arr = np.array(n_eff_list)
        cond_arr = np.array(cond_list)
        A_norm_arr = np.array(A_norm_list)
        r_eff_arr = np.array(r_eff_list)
        sse_ratio_arr = np.array(sse_ratio_list)

        # Aggregate statistics
        mean_delta2 = np.mean(delta2_arr)
        median_delta2 = np.median(delta2_arr)
        iqr_delta2 = np.percentile(delta2_arr, 75) - np.percentile(delta2_arr, 25)

        n_eff_mean = np.mean(n_eff_arr)
        n_eff_std = np.std(n_eff_arr)

        cond_mean = np.nanmean(cond_arr)

        A_norm_mean = np.mean(A_norm_arr)
        A_norm_std = np.std(A_norm_arr)
        frac_A_small = np.mean(A_norm_arr < 1e-6)

        r_eff_mean = np.mean(r_eff_arr)
        r_eff_over_h = r_eff_mean / h_fit_z
        sse_ratio_mean = np.nanmean(sse_ratio_arr)

        # Store results
        results['h_fit'].append(h_fit_z)
        results['mean_delta2'].append(mean_delta2)
        results['median_delta2'].append(median_delta2)
        results['iqr_delta2'].append(iqr_delta2)
        results['n_eff_mean'].append(n_eff_mean)
        results['n_eff_std'].append(n_eff_std)
        results['cond_mean'].append(cond_mean)
        results['A_norm_mean'].append(A_norm_mean)
        results['A_norm_std'].append(A_norm_std)
        results['frac_A_small'].append(frac_A_small)
        results['r_eff_mean'].append(r_eff_mean)
        results['r_eff_over_h'].append(r_eff_over_h)
        results['sse_ratio_mean'].append(sse_ratio_mean)

        # Log per-h_fit diagnostics
        logger.info(f"  mean(δ²) = {mean_delta2:.6e}, median = {median_delta2:.6e}, IQR = {iqr_delta2:.6e}")
        logger.info(f"  n_eff: mean = {n_eff_mean:.1f}, std = {n_eff_std:.1f}")
        logger.info(f"  r_eff/h = {r_eff_over_h:.3f}, SSE_lin/SSE_const = {sse_ratio_mean:.4f}")
        logger.info(f"  cond(X'WX): mean = {cond_mean:.2e}")
        logger.info(f"  ||A||: mean = {A_norm_mean:.4f}, std = {A_norm_std:.4f}, frac<1e-6 = {frac_A_small:.2%}")

    # Convert to arrays
    for key in results:
        results[key] = np.array(results[key])

    # Fit slope in BIAS REGIME only (where δ² increases with h)
    logger.info("")
    logger.info("=" * 70)
    logger.info("SLOPE FITTING (Bias Regime)")
    logger.info("=" * 70)

    # Find where δ² reaches minimum (transition from variance → bias regime)
    # We need to fit ONLY in the bias regime where δ² ∝ h^(2s)
    min_idx = np.argmin(results['mean_delta2'])

    # Start fitting from the point AFTER the minimum
    # This ensures we're solidly in the bias regime
    fit_start_idx = min_idx + 1

    logger.info(f"δ² minimum at h_fit_z = {results['h_fit'][min_idx]:.4f} (δ² = {results['mean_delta2'][min_idx]:.3e})")
    logger.info(f"Starting fit from h_fit_z = {results['h_fit'][fit_start_idx]:.4f}")

    h_fit_tail = results['h_fit'][fit_start_idx:]
    mean_delta2_tail = results['mean_delta2'][fit_start_idx:]

    # LOCALITY GUARD: Filter out points that violate locality conditions
    # NOTE: SSE guard removed - for this low-noise data (σ=0.01), local drift
    # is nearly constant everywhere, so SSE_lin/SSE_const ≈ 1.0 doesn't indicate
    # non-locality, just that curvature is weak relative to noise floor.
    # 1. r_eff/h ≤ 1.02 (relaxed: effective radius scales with h)
    # 2. n_eff ≥ 50 (sufficient effective sample size)
    # 3. cond < 1e6 (well-conditioned design matrix)
    # 4. δ² is INCREASING consecutively (bias regime, not noise fluctuation)
    delta2_increasing = np.diff(results['mean_delta2'][fit_start_idx:], prepend=results['mean_delta2'][fit_start_idx]) > 0
    locality_mask = (
        (results['r_eff_over_h'][fit_start_idx:] <= 1.02) &
        (results['n_eff_mean'][fit_start_idx:] >= 50) &
        (results['cond_mean'][fit_start_idx:] < 1e6) &
        delta2_increasing
    )

    if locality_mask.sum() >= 2:
        h_fit_fit = h_fit_tail[locality_mask]
        delta2_fit = mean_delta2_tail[locality_mask]

        log_h = np.log10(h_fit_fit)
        log_delta2 = np.log10(delta2_fit)

        eta_delta2, intercept = np.polyfit(log_h, log_delta2, 1)

        logger.info(f"Fit window: h_fit ∈ [{h_fit_fit[0]:.4f}, {h_fit_fit[-1]:.4f}] ({len(h_fit_fit)} points)")
        logger.info(f"Locality guard: r_eff/h ≤ 1.02, n_eff ≥ 50, cond < 1e6, δ² increasing")
        logger.info(f"Points passing locality: {locality_mask.sum()}/{len(locality_mask)}")
        logger.info(f"")
        logger.info(f"*** η_δ² = {eta_delta2:.3f} *** (theory: 2s = {2*q:.1f})")
        logger.info(f"Intercept: {intercept:.3f}")
        logger.info(f"Interpretation: δ² ∝ h^{eta_delta2:.3f}")
    else:
        logger.warning("Not enough valid points for fitting!")
        eta_delta2 = np.nan

    # DIAGNOSTIC 5: Per-|y₀| bin slopes
    logger.info("")
    logger.info("=" * 70)
    logger.info("DIAGNOSTIC 5: Heterogeneous Slopes by |y₀| Bin")
    logger.info("=" * 70)

    # Use quartiles of the actual query distribution
    query_points_orig = query_points * x_std + x_mean
    abs_query_orig = np.abs(query_points_orig.flatten())

    q33 = np.percentile(abs_query_orig, 33)
    q67 = np.percentile(abs_query_orig, 67)
    q_max = abs_query_orig.max()

    bins_to_test = [
        (0, q33, "lower third"),
        (q33, q67, "middle third"),
        (q67, q_max, "upper third"),
    ]

    for b_min, b_max, label in bins_to_test:
        logger.info(f"\n--- Bin: |y₀| ∈ [{b_min:.4f}, {b_max:.4f}) ({label}) ---")

        # Re-run computation for this bin
        bin_mask = (abs_query_orig >= b_min) & (abs_query_orig < b_max)

        if bin_mask.sum() < 10:
            logger.info(f"  Only {bin_mask.sum()} queries in this bin, skipping")
            continue

        bin_query_points = query_points[bin_mask]

        bin_mean_delta2 = []

        for h_fit_z in h_fit_grid_z:
            delta2_list = []
            for x0 in bin_query_points:
                result = cu.local_linear_mean(
                    X_train_z, Y_train_z, x0, h=h_fit_z,
                    ridge=1e-6, weight=kernel
                )

                mu_model = result.mu
                x0_orig = x0 * x_std + x_mean
                mu_true = true_drift_fn(x0_orig)
                mu_model_orig = mu_model * y_std + y_mean
                delta2 = (mu_model_orig - mu_true)**2
                delta2_list.append(float(delta2.flatten()[0]))

            bin_mean_delta2.append(np.mean(delta2_list))

        bin_mean_delta2 = np.array(bin_mean_delta2)

        # Fit slope with same locality mask
        if locality_mask.sum() >= 2:
            delta2_fit_bin = bin_mean_delta2[fit_start_idx:][locality_mask]
            log_delta2_bin = np.log10(delta2_fit_bin)
            eta_bin, _ = np.polyfit(log_h, log_delta2_bin, 1)

            logger.info(f"  η_δ² = {eta_bin:.3f} (theory: {2*q:.1f})")
        else:
            logger.info(f"  Not enough local points for fitting")

    # Summary
    logger.info("")
    logger.info("=" * 70)
    logger.info("SUMMARY")
    logger.info("=" * 70)
    logger.info(f"Overall η_δ² = {eta_delta2:.3f} (theory: {2*q:.1f})")
    logger.info(f"Gap from theory: {eta_delta2 - 2*q:.3f} ({100*(eta_delta2 - 2*q)/(2*q):.1f}%)")
    logger.info("")
    logger.info("Per-h_fit diagnostic table:")
    logger.info(f"{'h_fit':>8s} {'δ²':>10s} {'n_eff':>8s} {'cond':>10s} {'||A||':>8s}")
    for i in range(len(results['h_fit'])):
        logger.info(
            f"{results['h_fit'][i]:8.4f} "
            f"{results['mean_delta2'][i]:10.3e} "
            f"{results['n_eff_mean'][i]:8.1f} "
            f"{results['cond_mean'][i]:10.2e} "
            f"{results['A_norm_mean'][i]:8.4f}"
        )

    return results, eta_delta2


def main():
    parser = argparse.ArgumentParser(description="Diagnose pure bias law")
    parser.add_argument("--q", type=float, default=1.5)
    parser.add_argument("--sigma", type=float, default=0.01)
    parser.add_argument("--n", type=int, default=15000)
    parser.add_argument("--seed", type=int, default=100)
    parser.add_argument("--y_min", type=float, default=0.6, help="Interior tail min |y|")
    parser.add_argument("--y_max", type=float, default=0.8, help="Interior tail max |y|")
    parser.add_argument("--kernel", type=str, default="gaussian", choices=["gaussian", "tricube", "exp"], help="Weighting kernel")

    args = parser.parse_args()

    # Setup logging
    from src.core.logging_utils import setup_logger
    log_file = Path(__file__).parent / "logs" / "diagnose_bias_law.log"
    logger = setup_logger("bias_diag", log_file=log_file, level="INFO")

    # Also configure common_utils logger
    cu_logger = __import__('logging').getLogger('common_utils')
    cu_logger.setLevel(__import__('logging').INFO)
    for handler in logger.handlers:
        cu_logger.addHandler(handler)

    # Run diagnostics
    results, eta = diagnose_bias_law(
        q=args.q,
        sigma=args.sigma,
        n=args.n,
        seed=args.seed,
        interior_tail_range=(args.y_min, args.y_max),
        kernel=args.kernel,
    )


if __name__ == "__main__":
    main()
