"""
Tier 1: One-dimensional controlled dynamics

System: y_{t+1} = sign(y_t)|y_t|^q + noise, clamped to [-1, 1]

Goal: Verify locality exponent η ≈ 2s and learning exponent ζ ≈ 2s/(2s+1)
      where s ≈ q is the smoothness.
"""

from __future__ import annotations
import argparse
import json
import time
from pathlib import Path
from typing import Optional

import numpy as np
import matplotlib.pyplot as plt

# Local imports
from src.core import common_utils as cu
from src.core.logging_utils import setup_logger, Checkpoint, validate_array, log_summary_stats
from src.tests.test_utils import run_all_tests


def simulate_scalar_system(
    n: int,
    q: float,
    sigma: float,
    *,
    burn_in: int = 5000,
    rng: np.random.Generator,
) -> np.ndarray:
    """
    Simulate scalar system: y_{t+1} = sign(y_t)|y_t|^q + noise, clamp to [-1, 1].

    Parameters
    ----------
    n : int
        Number of steps (after burn-in).
    q : float
        Power in drift term (controls smoothness).
    sigma : float
        Noise standard deviation.
    burn_in : int
        Burn-in steps to discard.
    rng : np.random.Generator
        RNG.

    Returns
    -------
    y : ndarray
        Time series of shape (n,).
    """
    logger = cu.logger

    total_steps = n + burn_in
    y = np.zeros(total_steps)

    # Initialize
    y[0] = rng.uniform(-1, 1)

    for t in range(total_steps - 1):
        drift = np.sign(y[t]) * np.abs(y[t])**q
        noise = rng.normal(0, sigma)
        y[t+1] = np.clip(drift + noise, -1, 1)

    # Discard burn-in
    y = y[burn_in:]

    logger.info(f"Simulated scalar system: n={n}, q={q}, sigma={sigma}, burn_in={burn_in}")
    log_summary_stats(y, "time series y", logger)

    return y


def compute_edge_divergence(
    y: np.ndarray,
    h_fit: float,
    *,
    h_eval: Optional[float] = None,
    train_frac: float = 0.6,
    val_frac: float = 0.2,
    ridge: float = 1e-6,
    divergence: str = "js",
    weight: str = "exp",
    use_oracle: bool = False,
    true_drift_fn: Optional[callable] = None,
    true_sigma: Optional[float] = None,
    rng: np.random.Generator,
) -> dict:
    """
    Compute edge divergence between data and model conditionals.

    Parameters
    ----------
    y : ndarray
        Time series (n,).
    h_fit : float
        Bandwidth for model fitting (local linear regression).
    h_eval : float, optional
        Bandwidth for empirical conditional estimation. If None, use small fixed value
        based on median pairwise distance.
    train_frac, val_frac : float
        Train/val split fractions (test = 1 - train - val).
    ridge : float
        Ridge regularization for local linear fit.
    divergence : {"js", "mmd"}
        Divergence measure.
    weight : {"exp", "gaussian"}
        Weighting kernel for local linear fit.
    use_oracle : bool
        If True, use oracle (true dynamics) as target instead of empirical conditional.
    true_drift_fn : callable, optional
        True drift function m(y) for oracle. Required if use_oracle=True.
    true_sigma : float, optional
        True noise std for oracle. Required if use_oracle=True.
    rng : np.random.Generator
        RNG.

    Returns
    -------
    result : dict
        Contains edge_action, tau_mix, and intermediate arrays.
    """
    logger = cu.logger

    n = len(y)
    n_train = int(n * train_frac)
    n_val = int(n * val_frac)

    y_train = y[:n_train]
    y_val = y[n_train:n_train + n_val]
    y_test = y[n_train + n_val:]

    logger.info(f"Split: train={len(y_train)}, val={len(y_val)}, test={len(y_test)}")

    # Estimate IACT on training data
    tau_mix = cu.iact(y_train)
    logger.info(f"Estimated tau_mix = {tau_mix:.2f}")

    # Prepare edge pairs
    X_train = y_train[:-1].reshape(-1, 1)
    Y_train = y_train[1:].reshape(-1, 1)

    X_test = y_test[:-1].reshape(-1, 1)
    Y_test = y_test[1:].reshape(-1, 1)

    # Z-score on training data
    X_train_z, x_mean, x_std = cu.zscore(X_train, axis=0)
    Y_train_z, y_mean, y_std = cu.zscore(Y_train, axis=0)

    X_test_z = (X_test - x_mean) / x_std
    Y_test_z = (Y_test - y_mean) / y_std

    # Set h_eval if not provided (use small fixed value based on median distance)
    if h_eval is None:
        from scipy.spatial.distance import pdist
        dists = pdist(X_test_z)
        h_eval = float(np.percentile(dists, 15))  # 15th percentile - small and fixed
        logger.info(f"Auto h_eval (15th percentile): {h_eval:.4f}")

    # Fit local linear model at each test point
    # IMPORTANT: Sample from TAIL regions (large |x|) where nonlinearity is strongest!
    # At x≈0, drift m(x)≈0 is linear → all h_fit work equally well → flat locality curve
    n_test = len(X_test_z)
    n_queries = min(n_test, 50)  # Subsample for speed

    # Sample from tail: points with |x| > 75th percentile (top 25%)
    # This ensures we test where nonlinearity is strong
    abs_x = np.abs(X_test_z.flatten())
    tail_threshold = np.percentile(abs_x, 75)  # Top quartile
    tail_mask = abs_x > tail_threshold
    tail_indices = np.where(tail_mask)[0]

    if len(tail_indices) >= n_queries:
        # Sample from tail only
        query_idx = rng.choice(tail_indices, size=n_queries, replace=False)
        logger.info(f"Sampling {n_queries} query points from tail (|x| > {tail_threshold:.3f})")
    else:
        # Fall back to random sampling if not enough tail points
        query_idx = rng.choice(n_test, size=n_queries, replace=False)
        logger.warning(f"Only {len(tail_indices)} tail points, using random sampling")

    divergences = []

    for i, idx in enumerate(query_idx):
        x0 = X_test_z[idx]

        # Fit local linear mean on training data using h_fit
        result_train = cu.local_linear_mean(
            X_train_z, Y_train_z, x0, h=h_fit, ridge=ridge, weight=weight
        )

        # Model conditional: Gaussian with mean = mu, std = sqrt(Sigma)
        mu_model = result_train.mu
        sigma_model = np.sqrt(result_train.Sigma) if result_train.Sigma > 0 else 0.1

        # Sample from model conditional
        y_model = rng.normal(mu_model, sigma_model, size=100)

        if use_oracle:
            # Oracle conditional: use true dynamics
            if true_drift_fn is None or true_sigma is None:
                raise ValueError("use_oracle=True requires true_drift_fn and true_sigma")

            # Get true state in original coordinates
            x0_orig = x0 * x_std + x_mean
            mu_true = true_drift_fn(x0_orig)

            # Convert model prediction to original coordinates
            mu_model_orig = mu_model * y_std + y_mean

            # ANALYTIC JS DIVERGENCE for Gaussians with equal variance!
            # For N(μ₁, σ²) vs N(μ₂, σ²), JS = (1/8) * (μ₁ - μ₂)² / σ²
            # This is the CRITICAL FIX for getting η ≈ 2s
            delta = mu_model_orig - mu_true  # Mean error
            div = (1.0 / 8.0) * (delta ** 2) / (true_sigma ** 2)
            div = float(div.flatten()[0])  # Extract scalar

            logger.debug(f"    Oracle analytic JS: δ={delta[0]:.6f}, JS={div:.6f}")
        else:
            # Empirical conditional: neighbors of x0 in test data using h_eval
            dists = np.linalg.norm(X_test_z - x0.reshape(1, -1), axis=1)
            weights = np.exp(-dists / h_eval)  # Use h_eval, not h_fit!
            weights /= weights.sum()

            # Subsample empirical neighbors (weighted)
            n_neighbors = min(100, n_test)
            neighbor_idx = rng.choice(n_test, size=n_neighbors, replace=True, p=weights)
            y_data = Y_test_z[neighbor_idx].flatten()

            # Sample from model conditional
            y_model = rng.normal(mu_model, sigma_model, size=100)

            # Compute divergence via sampling (KDE/histogram)
            if divergence == "js":
                div = cu.js_divergence(y_data, y_model, method="hist", bins=32)
            elif divergence == "mmd":
                div, _ = cu.mmd_rbf(y_data, y_model, use_median_heuristic=True)
            else:
                raise ValueError(f"Unknown divergence: {divergence}")

        divergences.append(div)

        if (i + 1) % 50 == 0:
            logger.debug(f"  Query {i+1}/{n_queries}: div={div:.4f}")

    edge_action = float(np.mean(divergences))

    logger.info(f"Edge action (h_fit={h_fit:.4f}, h_eval={h_eval:.4f}): {edge_action:.6f}")

    return {
        "edge_action": edge_action,
        "tau_mix": tau_mix,
        "divergences": np.array(divergences),
        "n_queries": n_queries,
        "h_eval": h_eval,
    }


def run_learning_curve(
    config: dict,
    rng: np.random.Generator,
) -> dict:
    """
    Run learning curve experiment: vary sample size n.

    Parameters
    ----------
    config : dict
        Configuration parameters.
    rng : np.random.Generator
        RNG.

    Returns
    -------
    results : dict
        Learning curve results.
    """
    logger = cu.logger
    logger.info("=" * 60)
    logger.info("Running learning curve experiment")
    logger.info("=" * 60)

    q = config["q"]
    sigma = config["sigma"]
    n_max = config["n_max"]
    h = config["h_default"]

    # Sample size grid
    n_grid = np.array([1000, 2000, 5000, 10000, 20000, 50000, 100000])
    n_grid = n_grid[n_grid <= n_max]

    logger.info(f"Sample sizes: {n_grid}")

    A_n = []
    tau_mix_list = []

    for n in n_grid:
        logger.info(f"--- Processing n = {n} ---")

        # Simulate
        y = simulate_scalar_system(n, q, sigma, rng=rng)

        # Compute edge divergence (use fixed h_fit for learning curve)
        result = compute_edge_divergence(y, h, rng=rng, use_oracle=False)

        edge_action = result["edge_action"]
        tau_mix = result["tau_mix"]

        logger.info(f"  Edge action A(n={n}) = {edge_action:.6f}")
        logger.info(f"  tau_mix = {tau_mix:.2f}")

        A_n.append(edge_action)
        tau_mix_list.append(tau_mix)

    A_n = np.array(A_n)
    tau_mix_list = np.array(tau_mix_list)

    # Fit learning curve
    n_eff = n_grid / np.mean(tau_mix_list)
    curve = cu.fit_learning_curve(n_grid, A_n, n_eff=n_eff)

    zeta_est = -curve.slope
    A_inf = A_n.min()

    logger.info(f"Learning curve: zeta_est = {zeta_est:.3f}, A_inf = {A_inf:.4e}")
    logger.info(f"Theoretical zeta = 2s/(2s+1) ≈ {2*q/(2*q+1):.3f} (with s≈q={q})")

    return {
        "n_grid": n_grid,
        "A_n": A_n,
        "tau_mix_list": tau_mix_list,
        "n_eff": n_eff,
        "curve": curve,
        "zeta_est": zeta_est,
        "A_inf": A_inf,
    }


def run_locality_curve(
    config: dict,
    rng: np.random.Generator,
) -> dict:
    """
    Run locality curve experiment: vary bandwidth h_fit while keeping h_eval fixed.

    Parameters
    ----------
    config : dict
        Configuration parameters.
    rng : np.random.Generator
        RNG.

    Returns
    -------
    results : dict
        Locality curve results (both empirical and oracle if use_oracle=True).
    """
    logger = cu.logger
    logger.info("=" * 60)
    logger.info("Running locality curve experiment")
    logger.info("=" * 60)

    q = config["q"]
    sigma = config["sigma"]
    n = config["n_max"]
    use_oracle = config.get("use_oracle", True)  # Default to oracle for Tier 1

    # Simulate once with large n
    y = simulate_scalar_system(n, q, sigma, rng=rng)

    # Estimate effective sample size scale
    n_eff = n / cu.iact(y[:int(0.6 * n)])
    h_star = n_eff**(-1 / (2*q + 1))

    logger.info(f"Estimated optimal h* ≈ {h_star:.4f}")

    # Extended bandwidth grid for bias-variance U-shape
    # Go wider: 0.25, 0.5, 1, 2, 4, 8 * h_star
    h_mult = np.array([0.25, 0.5, 0.75, 1.0, 1.5, 2.0, 4.0, 8.0])
    h_fit_grid = h_mult * h_star

    logger.info(f"h_fit grid: {h_fit_grid}")

    # True drift function for oracle
    def true_drift_fn(y_val):
        return np.sign(y_val) * np.abs(y_val)**q

    A_h_empirical = []
    A_h_oracle = [] if use_oracle else None
    h_eval_used = None

    for h_fit in h_fit_grid:
        logger.info(f"--- Processing h_fit = {h_fit:.4f} ---")

        # Compute empirical edge divergence (using Gaussian weights)
        result_emp = compute_edge_divergence(
            y, h_fit,
            h_eval=h_eval_used,  # Will be auto-set on first iteration and reused
            rng=rng,
            weight="gaussian",  # Use Gaussian for clearer bias behavior
            use_oracle=False
        )
        edge_action_emp = result_emp["edge_action"]
        if h_eval_used is None:
            h_eval_used = result_emp["h_eval"]  # Save for consistency
            logger.info(f"Fixed h_eval = {h_eval_used:.4f} for all h_fit")

        logger.info(f"  Edge action (empirical) A(h_fit={h_fit:.4f}) = {edge_action_emp:.6f}")
        A_h_empirical.append(edge_action_emp)

        if use_oracle:
            # Compute oracle edge divergence
            result_oracle = compute_edge_divergence(
                y, h_fit,
                rng=rng,
                weight="gaussian",
                use_oracle=True,
                true_drift_fn=true_drift_fn,
                true_sigma=sigma
            )
            edge_action_oracle = result_oracle["edge_action"]
            logger.info(f"  Edge action (oracle) A(h_fit={h_fit:.4f}) = {edge_action_oracle:.6f}")
            A_h_oracle.append(edge_action_oracle)

    A_h_empirical = np.array(A_h_empirical)
    if use_oracle:
        A_h_oracle = np.array(A_h_oracle)

    # Fit locality curve on right tail (large h_fit where bias dominates)
    # Use the largest 50% of h values for fitting
    fit_start_idx = len(h_fit_grid) // 2
    fit_range = (h_fit_grid[fit_start_idx], h_fit_grid[-1])

    logger.info(f"Fitting eta on right tail: h_fit in [{fit_range[0]:.4f}, {fit_range[1]:.4f}]")

    # Fit empirical curve
    curve_emp = cu.fit_locality_curve(h_fit_grid, A_h_empirical, fit_range=fit_range)
    eta_est_emp = curve_emp.slope
    A_0_emp = A_h_empirical.min()

    logger.info(f"Empirical locality curve: eta_est = {eta_est_emp:.3f}, A_0 = {A_0_emp:.4e}")

    results = {
        "h_fit_grid": h_fit_grid,
        "h_eval": h_eval_used,
        "A_h_empirical": A_h_empirical,
        "curve_empirical": curve_emp,
        "eta_est_empirical": eta_est_emp,
        "A_0_empirical": A_0_emp,
    }

    if use_oracle:
        # Fit oracle curve
        curve_oracle = cu.fit_locality_curve(h_fit_grid, A_h_oracle, fit_range=fit_range)
        eta_est_oracle = curve_oracle.slope
        A_0_oracle = A_h_oracle.min()

        logger.info(f"Oracle locality curve: eta_est = {eta_est_oracle:.3f}, A_0 = {A_0_oracle:.4e}")

        results.update({
            "A_h_oracle": A_h_oracle,
            "curve_oracle": curve_oracle,
            "eta_est_oracle": eta_est_oracle,
            "A_0_oracle": A_0_oracle,
        })

        # Use oracle for primary eta estimate
        eta_est = eta_est_oracle
        A_0 = A_0_oracle
    else:
        eta_est = eta_est_emp
        A_0 = A_0_emp

    logger.info(f"Theoretical eta = 2s ≈ {2*q:.3f} (with s≈q={q})")

    # Add legacy keys for compatibility
    results.update({
        "h_grid": h_fit_grid,  # Legacy name
        "A_h": A_h_oracle if use_oracle else A_h_empirical,  # Legacy name
        "curve": curve_oracle if use_oracle else curve_emp,
        "eta_est": eta_est,
        "A_0": A_0,
    })

    return results


def plot_results(learning_results: dict, locality_results: dict, config: dict, output_dir: Path):
    """
    Generate and save figures.

    Parameters
    ----------
    learning_results : dict
        Learning curve results.
    locality_results : dict
        Locality curve results.
    config : dict
        Configuration.
    output_dir : Path
        Output directory.
    """
    logger = cu.logger

    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    # Learning curve
    ax = axes[0]
    n_grid = learning_results["n_grid"]
    A_n = learning_results["A_n"]
    curve = learning_results["curve"]

    cu.plot_loglog_with_fit(ax, n_grid, A_n, label="Data")
    ax.set_title(f"Learning Curve (q={config['q']}, σ={config['sigma']})")
    ax.set_xlabel("Sample size n")
    ax.set_ylabel("Edge action A(n)")

    # Locality curve
    ax = axes[1]
    h_grid = locality_results["h_grid"]
    A_h = locality_results["A_h"]
    curve = locality_results["curve"]

    cu.plot_loglog_with_fit(ax, h_grid, A_h, label="Data")
    ax.set_title(f"Locality Curve (q={config['q']}, σ={config['sigma']})")
    ax.set_xlabel("Bandwidth h")
    ax.set_ylabel("Edge action A(h)")

    plt.tight_layout()

    output_path = output_dir / f"tier1_q{config['q']}_s{config['sigma']}.png"
    cu.savefig(fig, str(output_path))

    logger.info(f"Saved figure: {output_path}")


def main():
    parser = argparse.ArgumentParser(description="Tier 1: Scalar controlled dynamics")
    parser.add_argument("--q", type=float, default=1.5, help="Power q (smoothness)")
    parser.add_argument("--sigma", type=float, default=0.01, help="Noise level")
    parser.add_argument("--n_max", type=int, default=100000, help="Max sample size")
    parser.add_argument("--seed", type=int, default=42, help="Random seed")
    parser.add_argument("--output_dir", type=str, default="figures", help="Output directory")
    parser.add_argument("--run_tests", action="store_true", help="Run validation tests first")
    parser.add_argument("--verbose", action="store_true", help="Verbose logging")

    args = parser.parse_args()

    # Setup
    output_dir = Path(__file__).parent / args.output_dir
    log_file = Path(__file__).parent / "logs" / f"tier1_q{args.q}_s{args.sigma}.log"

    log_level = "DEBUG" if args.verbose else "INFO"
    logger = setup_logger("tier1", log_file=log_file, level=getattr(__import__('logging'), log_level))

    # Also configure common_utils logger to use the same handlers
    cu_logger = __import__('logging').getLogger('common_utils')
    cu_logger.setLevel(getattr(__import__('logging'), log_level))
    for handler in logger.handlers:
        cu_logger.addHandler(handler)

    logger.info("=" * 60)
    logger.info("Tier 1: One-dimensional controlled dynamics")
    logger.info("=" * 60)

    rng = cu.make_rng(args.seed)

    # Configuration
    config = {
        "q": args.q,
        "sigma": args.sigma,
        "n_max": args.n_max,
        "seed": args.seed,
        "h_default": 0.5,  # Default bandwidth for learning curve
        "use_oracle": True,  # Use oracle conditional for locality curves (Tier 1)
    }

    logger.info(f"Configuration: {json.dumps(config, indent=2)}")

    # Run validation tests if requested
    if args.run_tests:
        logger.info("Running validation tests...")
        test_results = run_all_tests(cu, logger, rng)
        if not all(test_results.values()):
            logger.error("Some tests failed! Proceed with caution.")

    # Run experiments
    start_time = time.time()

    learning_results = run_learning_curve(config, rng)
    locality_results = run_locality_curve(config, rng)

    elapsed = time.time() - start_time
    logger.info(f"Total runtime: {elapsed:.1f} seconds")

    # Plot
    plot_results(learning_results, locality_results, config, output_dir)

    # Save checkpoint
    checkpoint_dir = Path(__file__).parent / "configs"
    cp = Checkpoint(checkpoint_dir, f"tier1_q{args.q}_s{args.sigma}")

    arrays = {
        "learning_n_grid": learning_results["n_grid"],
        "learning_A_n": learning_results["A_n"],
        "locality_h_grid": locality_results["h_grid"],
        "locality_A_h": locality_results["A_h"],
    }

    metadata = {
        "runtime_seconds": elapsed,
        "zeta_est": learning_results["zeta_est"],
        "eta_est": locality_results["eta_est"],
    }

    cp.save(config, arrays, metadata)

    logger.info("=" * 60)
    logger.info(f"Results summary:")
    logger.info(f"  Learning exponent ζ_est = {learning_results['zeta_est']:.3f} (theory: {2*args.q/(2*args.q+1):.3f})")
    logger.info(f"  Locality exponent η_est = {locality_results['eta_est']:.3f} (theory: {2*args.q:.3f})")
    logger.info(f"  A_inf = {learning_results['A_inf']:.4e}")
    logger.info(f"  A_0 = {locality_results['A_0']:.4e}")
    logger.info("=" * 60)


if __name__ == "__main__":
    main()
