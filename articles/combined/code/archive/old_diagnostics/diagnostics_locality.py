#!/usr/bin/env python3
"""
Diagnostic tests for locality curve implementation.
Based on user's prescribed diagnostic framework.
"""

import numpy as np
import matplotlib.pyplot as plt
import argparse
from pathlib import Path

import common_utils as cu
from tier1_scalar import simulate_scalar_system, compute_edge_divergence

def setup_logging():
    """Setup logging to console."""
    import logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s | %(levelname)-8s | %(name)-16s | %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    return logging.getLogger('diagnostics')

def diag1_decoupling_sanity(config: dict, logger):
    """
    Diag 1: Test that varying h_eval doesn't change the curve shape.
    Plot A_empirical(h_fit) for two different h_eval values.
    They should be nearly identical (decoupling works).
    """
    logger.info("="*60)
    logger.info("Diag 1: Decoupling Sanity Check")
    logger.info("="*60)

    q = config["q"]
    sigma = config["sigma"]
    n_max = config["n_max"]
    seed = config["seed"]

    rng = np.random.default_rng(seed)

    # Generate data
    y = simulate_scalar_system(n_max, q=q, sigma=sigma, rng=rng)

    # Compute optimal bandwidth
    iact_val = cu.iact(y, max_lag=200)
    n_eff = len(y) / max(iact_val, 1.0)
    s = q  # Smoothness
    h_star = n_eff ** (-1.0 / (2 * s + 1))

    # h_fit grid
    h_mult = np.array([0.25, 0.5, 0.75, 1.0, 1.5, 2.0, 4.0, 8.0])
    h_fit_grid = h_mult * h_star

    # Two different h_eval values (small vs even smaller)
    from scipy.spatial.distance import pdist
    y_2d = y.reshape(-1, 1)  # Make 2D for pdist
    dists = pdist(y_2d[:-1])
    h_eval_1 = float(np.percentile(dists, 15))  # Default
    h_eval_2 = float(np.percentile(dists, 10))  # Even smaller

    logger.info(f"h_star = {h_star:.4f}, n_eff = {n_eff:.1f}")
    logger.info(f"h_eval_1 (15th pct) = {h_eval_1:.4f}")
    logger.info(f"h_eval_2 (10th pct) = {h_eval_2:.4f}")

    A_h_1 = []
    A_h_2 = []

    for h_fit in h_fit_grid:
        # With h_eval_1
        result_1 = compute_edge_divergence(
            y, h_fit,
            h_eval=h_eval_1,
            divergence="js",
            weight="gaussian",
            use_oracle=False,
            rng=rng
        )
        A_h_1.append(result_1["edge_action"])

        # With h_eval_2
        result_2 = compute_edge_divergence(
            y, h_fit,
            h_eval=h_eval_2,
            divergence="js",
            weight="gaussian",
            use_oracle=False,
            rng=rng
        )
        A_h_2.append(result_2["edge_action"])

        logger.info(f"h_fit={h_fit:.4f}: A(h_eval_1)={result_1['edge_action']:.4f}, A(h_eval_2)={result_2['edge_action']:.4f}")

    A_h_1 = np.array(A_h_1)
    A_h_2 = np.array(A_h_2)

    # Plot
    fig, ax = plt.subplots(1, 1, figsize=(8, 6))
    ax.loglog(h_fit_grid, A_h_1, 'o-', label=f'h_eval={h_eval_1:.3f} (15th pct)', markersize=8)
    ax.loglog(h_fit_grid, A_h_2, 's-', label=f'h_eval={h_eval_2:.3f} (10th pct)', markersize=8)
    ax.set_xlabel('Model bandwidth h_fit', fontsize=12)
    ax.set_ylabel('Edge divergence A(h)', fontsize=12)
    ax.set_title('Diag 1: Decoupling Sanity (vary h_eval)', fontsize=14)
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3)

    fig_path = Path("figures") / "diag1_decoupling.png"
    fig_path.parent.mkdir(exist_ok=True)
    fig.savefig(fig_path, dpi=150, bbox_inches='tight')
    logger.info(f"Saved figure: {fig_path}")

    # Assess similarity
    rel_diff = np.abs(A_h_1 - A_h_2) / (A_h_1 + 1e-10)
    max_rel_diff = rel_diff.max()
    mean_rel_diff = rel_diff.mean()

    logger.info(f"Max relative difference: {max_rel_diff:.2%}")
    logger.info(f"Mean relative difference: {mean_rel_diff:.2%}")

    if mean_rel_diff < 0.20:
        logger.info("✓ PASS: Curves are similar (decoupling works)")
    else:
        logger.warning(f"✗ FAIL: Curves differ by {mean_rel_diff:.1%} on average")

    return {"h_fit_grid": h_fit_grid, "A_h_1": A_h_1, "A_h_2": A_h_2}


def diag2_oracle_vs_empirical(config: dict, logger):
    """
    Diag 2: Compare oracle vs empirical locality curves.
    They should share the same slope at large h_fit (both see model bias).
    """
    logger.info("="*60)
    logger.info("Diag 2: Oracle vs Empirical Comparison")
    logger.info("="*60)

    q = config["q"]
    sigma = config["sigma"]
    n_max = config["n_max"]
    seed = config["seed"]

    rng = np.random.default_rng(seed)

    # Generate data
    y = simulate_scalar_system(n_max, q=q, sigma=sigma, rng=rng)

    # Compute optimal bandwidth
    iact_val = cu.iact(y, max_lag=200)
    n_eff = len(y) / max(iact_val, 1.0)
    s = q
    h_star = n_eff ** (-1.0 / (2 * s + 1))

    # h_fit grid
    h_mult = np.array([0.25, 0.5, 0.75, 1.0, 1.5, 2.0, 4.0, 8.0])
    h_fit_grid = h_mult * h_star

    # Fixed h_eval
    from scipy.spatial.distance import pdist
    y_2d = y.reshape(-1, 1)
    dists = pdist(y_2d[:-1])  # Pairwise distances for X (states, not transitions)
    h_eval = float(np.percentile(dists, 15))

    logger.info(f"h_star = {h_star:.4f}, n_eff = {n_eff:.1f}, h_eval = {h_eval:.4f}")

    # True drift function
    def true_drift_fn(y_val):
        return np.sign(y_val) * np.abs(y_val)**q

    A_oracle = []
    A_empirical = []

    for h_fit in h_fit_grid:
        # Oracle
        result_oracle = compute_edge_divergence(
            y, h_fit,
            divergence="js",
            weight="gaussian",
            use_oracle=True,
            true_drift_fn=true_drift_fn,
            true_sigma=sigma,
            rng=rng
        )
        A_oracle.append(result_oracle["edge_action"])

        # Empirical
        result_emp = compute_edge_divergence(
            y, h_fit,
            h_eval=h_eval,
            divergence="js",
            weight="gaussian",
            use_oracle=False,
            rng=rng
        )
        A_empirical.append(result_emp["edge_action"])

        logger.info(f"h_fit={h_fit:.4f}: Oracle={result_oracle['edge_action']:.4f}, Empirical={result_emp['edge_action']:.4f}")

    A_oracle = np.array(A_oracle)
    A_empirical = np.array(A_empirical)

    # Fit slopes on right tail (largest 50%)
    fit_start = len(h_fit_grid) // 2
    h_fit_tail = h_fit_grid[fit_start:]
    A_oracle_tail = A_oracle[fit_start:]
    A_emp_tail = A_empirical[fit_start:]

    # Fit log-log: log(A) = log(A_0) + eta * log(h)
    log_h = np.log10(h_fit_tail)
    log_A_oracle = np.log10(A_oracle_tail)
    log_A_emp = np.log10(A_emp_tail)

    eta_oracle = np.polyfit(log_h, log_A_oracle, 1)[0]
    eta_emp = np.polyfit(log_h, log_A_emp, 1)[0]

    logger.info(f"Oracle slope (right tail): η = {eta_oracle:.3f}")
    logger.info(f"Empirical slope (right tail): η = {eta_emp:.3f}")
    logger.info(f"Theory: η = 2s ≈ {2*s:.3f}")

    # Plot
    fig, ax = plt.subplots(1, 1, figsize=(8, 6))
    ax.loglog(h_fit_grid, A_oracle, 'o-', label=f'Oracle (η={eta_oracle:.2f})', markersize=8, linewidth=2)
    ax.loglog(h_fit_grid, A_empirical, 's-', label=f'Empirical (η={eta_emp:.2f})', markersize=8, linewidth=2)
    ax.axvline(h_fit_tail[0], color='gray', linestyle='--', alpha=0.5, label='Fit region start')
    ax.set_xlabel('Model bandwidth h_fit', fontsize=12)
    ax.set_ylabel('Edge divergence A(h)', fontsize=12)
    ax.set_title(f'Diag 2: Oracle vs Empirical (theory η={2*s:.1f})', fontsize=14)
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3)

    fig_path = Path("figures") / "diag2_oracle_vs_empirical.png"
    fig.savefig(fig_path, dpi=150, bbox_inches='tight')
    logger.info(f"Saved figure: {fig_path}")

    return {
        "h_fit_grid": h_fit_grid,
        "A_oracle": A_oracle,
        "A_empirical": A_empirical,
        "eta_oracle": eta_oracle,
        "eta_emp": eta_emp
    }


def diag3_bias_variance_ushape(config: dict, logger):
    """
    Diag 3: Check for bias-variance U-shape in empirical curve.
    With wide h_fit range, should see:
    - Small h: high variance (empirical conditional noisy) → A increases
    - Large h: high bias (model smooth) → A increases
    - Sweet spot in middle
    """
    logger.info("="*60)
    logger.info("Diag 3: Bias-Variance U-Shape")
    logger.info("="*60)

    q = config["q"]
    sigma = config["sigma"]
    n_max = config["n_max"]
    seed = config["seed"]

    rng = np.random.default_rng(seed)

    # Generate data
    y = simulate_scalar_system(n_max, q=q, sigma=sigma, rng=rng)

    # Compute optimal bandwidth
    iact_val = cu.iact(y, max_lag=200)
    n_eff = len(y) / max(iact_val, 1.0)
    s = q
    h_star = n_eff ** (-1.0 / (2 * s + 1))

    # EXTRA WIDE h_fit grid to see U-shape
    h_mult = np.array([0.1, 0.25, 0.5, 0.75, 1.0, 1.5, 2.0, 4.0, 8.0, 16.0])
    h_fit_grid = h_mult * h_star

    # Fixed h_eval
    from scipy.spatial.distance import pdist
    y_2d = y.reshape(-1, 1)
    dists = pdist(y_2d[:-1])  # Pairwise distances for X (states, not transitions)
    h_eval = float(np.percentile(dists, 15))

    logger.info(f"h_star = {h_star:.4f}, n_eff = {n_eff:.1f}, h_eval = {h_eval:.4f}")
    logger.info(f"h_fit range: [{h_fit_grid[0]:.4f}, {h_fit_grid[-1]:.4f}]")

    A_empirical = []

    for h_fit in h_fit_grid:
        result = compute_edge_divergence(
            y, h_fit,
            h_eval=h_eval,
            divergence="js",
            weight="gaussian",
            use_oracle=False,
            rng=rng
        )
        A_empirical.append(result["edge_action"])
        logger.info(f"h_fit={h_fit:.4f}: A={result['edge_action']:.4f}")

    A_empirical = np.array(A_empirical)

    # Check for U-shape: find minimum
    min_idx = np.argmin(A_empirical)
    min_h = h_fit_grid[min_idx]
    min_A = A_empirical[min_idx]

    logger.info(f"Minimum at h_fit = {min_h:.4f} (A = {min_A:.4f})")
    logger.info(f"Minimum index: {min_idx}/{len(h_fit_grid)-1}")

    # Check if minimum is interior (not at edges)
    if 0 < min_idx < len(h_fit_grid) - 1:
        logger.info("✓ PASS: U-shape detected (interior minimum)")
    else:
        logger.warning("✗ No clear U-shape (minimum at boundary)")

    # Plot
    fig, ax = plt.subplots(1, 1, figsize=(8, 6))
    ax.loglog(h_fit_grid, A_empirical, 'o-', markersize=8, linewidth=2, label='Empirical')
    ax.loglog(min_h, min_A, 'r*', markersize=20, label=f'Min at h={min_h:.3f}')
    ax.axvline(h_star, color='gray', linestyle='--', alpha=0.5, label=f'h* (optimal)')
    ax.set_xlabel('Model bandwidth h_fit', fontsize=12)
    ax.set_ylabel('Edge divergence A(h)', fontsize=12)
    ax.set_title('Diag 3: Bias-Variance U-Shape', fontsize=14)
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3)

    fig_path = Path("figures") / "diag3_ushape.png"
    fig.savefig(fig_path, dpi=150, bbox_inches='tight')
    logger.info(f"Saved figure: {fig_path}")

    return {"h_fit_grid": h_fit_grid, "A_empirical": A_empirical, "min_idx": min_idx}


def diag4_weight_kernel(config: dict, logger):
    """
    Diag 4: Compare exponential vs Gaussian weighting kernels.
    Check if kernel choice affects slope estimation.
    """
    logger.info("="*60)
    logger.info("Diag 4: Weighting Kernel Comparison")
    logger.info("="*60)

    q = config["q"]
    sigma = config["sigma"]
    n_max = config["n_max"]
    seed = config["seed"]

    rng = np.random.default_rng(seed)

    # Generate data
    y = simulate_scalar_system(n_max, q=q, sigma=sigma, rng=rng)

    # Compute optimal bandwidth
    iact_val = cu.iact(y, max_lag=200)
    n_eff = len(y) / max(iact_val, 1.0)
    s = q
    h_star = n_eff ** (-1.0 / (2 * s + 1))

    # h_fit grid
    h_mult = np.array([0.25, 0.5, 0.75, 1.0, 1.5, 2.0, 4.0, 8.0])
    h_fit_grid = h_mult * h_star

    # True drift function
    def true_drift_fn(y_val):
        return np.sign(y_val) * np.abs(y_val)**q

    logger.info(f"h_star = {h_star:.4f}, n_eff = {n_eff:.1f}")

    A_exp = []
    A_gauss = []

    for h_fit in h_fit_grid:
        # Exponential weights
        result_exp = compute_edge_divergence(
            y, h_fit,
            divergence="js",
            weight="exp",
            use_oracle=True,
            true_drift_fn=true_drift_fn,
            true_sigma=sigma,
            rng=rng
        )
        A_exp.append(result_exp["edge_action"])

        # Gaussian weights
        result_gauss = compute_edge_divergence(
            y, h_fit,
            divergence="js",
            weight="gaussian",
            use_oracle=True,
            true_drift_fn=true_drift_fn,
            true_sigma=sigma,
            rng=rng
        )
        A_gauss.append(result_gauss["edge_action"])

        logger.info(f"h_fit={h_fit:.4f}: Exp={result_exp['edge_action']:.4f}, Gauss={result_gauss['edge_action']:.4f}")

    A_exp = np.array(A_exp)
    A_gauss = np.array(A_gauss)

    # Fit slopes on right tail
    fit_start = len(h_fit_grid) // 2
    log_h = np.log10(h_fit_grid[fit_start:])
    eta_exp = np.polyfit(log_h, np.log10(A_exp[fit_start:]), 1)[0]
    eta_gauss = np.polyfit(log_h, np.log10(A_gauss[fit_start:]), 1)[0]

    logger.info(f"Exponential weights: η = {eta_exp:.3f}")
    logger.info(f"Gaussian weights: η = {eta_gauss:.3f}")
    logger.info(f"Theory: η = 2s ≈ {2*s:.3f}")

    # Plot
    fig, ax = plt.subplots(1, 1, figsize=(8, 6))
    ax.loglog(h_fit_grid, A_exp, 'o-', label=f'Exponential (η={eta_exp:.2f})', markersize=8, linewidth=2)
    ax.loglog(h_fit_grid, A_gauss, 's-', label=f'Gaussian (η={eta_gauss:.2f})', markersize=8, linewidth=2)
    ax.set_xlabel('Model bandwidth h_fit', fontsize=12)
    ax.set_ylabel('Edge divergence A(h)', fontsize=12)
    ax.set_title(f'Diag 4: Weight Kernel (theory η={2*s:.1f})', fontsize=14)
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3)

    fig_path = Path("figures") / "diag4_kernels.png"
    fig.savefig(fig_path, dpi=150, bbox_inches='tight')
    logger.info(f"Saved figure: {fig_path}")

    return {
        "h_fit_grid": h_fit_grid,
        "A_exp": A_exp,
        "A_gauss": A_gauss,
        "eta_exp": eta_exp,
        "eta_gauss": eta_gauss
    }


def main():
    parser = argparse.ArgumentParser(description="Locality curve diagnostics")
    parser.add_argument("--q", type=float, default=1.5, help="Drift exponent")
    parser.add_argument("--sigma", type=float, default=0.01, help="Noise strength")
    parser.add_argument("--n_max", type=int, default=10000, help="Trajectory length")
    parser.add_argument("--seed", type=int, default=55, help="Random seed")
    parser.add_argument("--diag", type=str, default="all",
                        choices=["all", "1", "2", "3", "4"],
                        help="Which diagnostic to run")

    args = parser.parse_args()
    logger = setup_logging()

    config = {
        "q": args.q,
        "sigma": args.sigma,
        "n_max": args.n_max,
        "seed": args.seed,
    }

    logger.info("="*60)
    logger.info("Locality Curve Diagnostics")
    logger.info("="*60)
    logger.info(f"Configuration: q={args.q}, sigma={args.sigma}, n={args.n_max}, seed={args.seed}")

    results = {}

    if args.diag in ["all", "1"]:
        results["diag1"] = diag1_decoupling_sanity(config, logger)

    if args.diag in ["all", "2"]:
        results["diag2"] = diag2_oracle_vs_empirical(config, logger)

    if args.diag in ["all", "3"]:
        results["diag3"] = diag3_bias_variance_ushape(config, logger)

    if args.diag in ["all", "4"]:
        results["diag4"] = diag4_weight_kernel(config, logger)

    logger.info("="*60)
    logger.info("Diagnostics complete!")
    logger.info("="*60)

    return results


if __name__ == "__main__":
    main()
