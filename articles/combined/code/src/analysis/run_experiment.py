"""
Clean experiment runner for locality validation.

Single entry point: loads config, runs experiment, saves results.
No debugging noise - only key milestones logged.
"""

import json
import csv
import numpy as np
from pathlib import Path
from typing import Dict, List, Tuple
import argparse
import time

from src.core import common_utils as cu
from src.simulation.tier1_scalar import simulate_scalar_system
from src.analysis import plotting
from src.analysis import robust_fitting as rf
from src.analysis.json_utils import sanitize_for_json
from src.analysis.plot_eta_overlay import plot_eta_u_overlay


def load_config(config_path: Path) -> Dict:
    """Load experiment configuration from JSON."""
    with open(config_path, 'r') as f:
        config = json.load(f)
    return config


def simulate_and_prepare(config: Dict, rng) -> Tuple:
    """
    Simulate system and prepare train/test split with z-scoring.

    Returns
    -------
    X_train_z, Y_train_z, X_test_z, query_points, x_std, y_std, x_mean, y_mean, n_eff, h_star
    """
    # Simulate
    q = config['system']['q']
    sigma = config['system']['sigma']
    n = config['system']['n']

    y = simulate_scalar_system(n, q, sigma, rng=rng)
    X = y[:-1].reshape(-1, 1)
    Y = y[1:].reshape(-1, 1)

    # Z-score
    X_z, x_mean, x_std = cu.zscore(X, axis=0)
    Y_z, y_mean, y_std = cu.zscore(Y, axis=0)

    # Train/test split
    n_train = int(0.6 * len(X_z))
    X_train_z = X_z[:n_train]
    Y_train_z = Y_z[:n_train]
    X_test_z = X_z[n_train:]

    # Select queries from percentile range
    X_test_orig = X_test_z * x_std + x_mean
    abs_x_orig = np.abs(X_test_orig.flatten())
    p_low, p_high = config['queries']['percentile_range']
    p_low_val = np.percentile(abs_x_orig, p_low)
    p_high_val = np.percentile(abs_x_orig, p_high)

    interior_mask = (abs_x_orig >= p_low_val) & (abs_x_orig <= p_high_val)
    interior_indices = np.where(interior_mask)[0]

    n_queries = min(config['queries']['n_queries'], len(interior_indices))
    query_idx = rng.choice(interior_indices, size=n_queries, replace=False)
    query_points = X_test_z[query_idx]

    # Compute effective sample size and h*
    n_eff = n_train / cu.iact(y[:n_train])
    h_star = n_eff ** (-1 / (2*q + 1))

    return (X_train_z, Y_train_z, X_test_z, query_points,
            x_std, y_std, x_mean, y_mean, n_eff, h_star)


def compute_delta2_grid(
    X_train_z, Y_train_z, query_points, h_grid, x_std, y_std, x_mean, y_mean,
    kernel: str, q: float
) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """
    Compute δ² and diagnostics over bandwidth grid.

    Returns
    -------
    delta2_mean, r_eff_over_h_mean, n_eff_mean, u_mean
    """
    def true_drift_fn(y_val):
        return np.sign(y_val) * np.abs(y_val)**q

    results = {'delta2': [], 'r_eff_over_h': [], 'n_eff': [], 'u': []}

    print(f"Computing global δ² grid: {len(query_points)} queries × {len(h_grid)} bandwidths = {len(query_points) * len(h_grid)} local fits...", flush=True)
    start_time = time.time()

    for h_idx, h_z in enumerate(h_grid, 1):
        h_start = time.time()
        delta2_list = []
        r_eff_list = []
        neff_list = []
        u_list = []

        for q_idx, x0 in enumerate(query_points, 1):
            result = cu.local_linear_mean(
                X_train_z, Y_train_z, x0, h=h_z,
                ridge=1e-6, weight=kernel
            )

            # Compute bias
            mu_model = result.mu
            x0_orig = x0 * x_std + x_mean
            mu_true = true_drift_fn(x0_orig)
            mu_model_orig = mu_model * y_std + y_mean
            delta2 = (mu_model_orig - mu_true)**2
            delta2_list.append(float(delta2.flatten()[0]))

            # Diagnostics
            r_eff_list.append(result.r_eff / h_z)
            neff_list.append(result.n_eff)

            # Scaled distance u = |y₀|/h (in z-space)
            u_list.append(float(np.abs(x0.flatten()[0]) / h_z))

        results['delta2'].append(np.median(delta2_list))
        results['r_eff_over_h'].append(np.median(r_eff_list))
        results['n_eff'].append(np.median(neff_list))
        results['u'].append(np.median(u_list))

        h_time = time.time() - h_start
        elapsed = time.time() - start_time
        rate = h_idx / elapsed
        eta_mins = (len(h_grid) - h_idx) / rate / 60 if rate > 0 else 0
        print(f"  [{h_idx}/{len(h_grid)}] h={h_z:.4f}: {h_time:.1f}s/bandwidth, {elapsed/60:.1f}min elapsed, ETA {eta_mins:.1f}min", flush=True)

    return (np.array(results['delta2']),
            np.array(results['r_eff_over_h']),
            np.array(results['n_eff']),
            np.array(results['u']))


def fit_eta_right_tail(
    h_grid, delta2, h_star, fit_start_mult, locality_guard, min_span_decades,
    config: Dict
) -> Tuple:
    """
    Fit η on right tail with locality guards and robust fitting.

    Returns
    -------
    h_fit, delta2_fit, eta, span_decades, pass_rate, ci_low, ci_high, diagnostics
    """
    # Build full locality mask
    r_eff_over_h = locality_guard['r_eff_over_h']
    r_min = locality_guard['r_min']
    r_max = locality_guard['r_max']
    n_eff = locality_guard['n_eff']

    locality_mask = (
        (r_eff_over_h >= r_min) &
        (r_eff_over_h <= r_max) &
        (n_eff >= 50)
    )

    # Get robust fitting config
    use_robust = config['bandwidth'].get('use_robust_slope', False)
    curvature_threshold = config['bandwidth'].get('curvature_guard_threshold', 2.0)
    bootstrap_n = config['bootstrap'].get('n_resamples', 0)
    bootstrap_seed = config['bootstrap'].get('seed', None)

    # Use robust fitting module
    fit_results = rf.fit_with_diagnostics(
        h_grid, delta2, h_star, fit_start_mult, locality_mask,
        use_robust=use_robust,
        curvature_threshold=curvature_threshold,
        min_span_decades=min_span_decades,
        bootstrap_n=bootstrap_n,
        bootstrap_seed=bootstrap_seed
    )

    h_fit = fit_results['h_fit']
    delta2_fit = fit_results['delta2_fit']
    eta = fit_results['eta']
    ci_low = fit_results['ci_low']
    ci_high = fit_results['ci_high']
    diagnostics = fit_results['diagnostics']

    # Compute pass rate (from original locality mask in selected window)
    min_idx = np.argmin(delta2)
    fit_start_idx = np.searchsorted(h_grid, h_star * fit_start_mult)
    fit_start_idx = max(fit_start_idx, min_idx + 1)

    if len(locality_mask[fit_start_idx:]) > 0:
        pass_rate = locality_mask[fit_start_idx:].sum() / len(locality_mask[fit_start_idx:])
    else:
        pass_rate = 0.0

    span_decades = diagnostics['span_decades']

    # Print warnings/info
    if span_decades < min_span_decades:
        print(f"Warning: fit span {span_decades:.2f} < target {min_span_decades:.2f} decades")

    if diagnostics['quality'] != 'good':
        print(f"Warning: fit quality = {diagnostics['quality']}")

    return h_fit, delta2_fit, eta, span_decades, pass_rate, ci_low, ci_high, diagnostics


def compute_per_bin_eta(
    X_train_z, Y_train_z, query_points, h_fit, h_grid, u_med_grid,
    x_std, y_std, x_mean, y_mean,
    kernel: str, q: float, bin_method: str
) -> List[Dict]:
    """
    Compute η for each |y₀| bin with representative u.

    Returns
    -------
    List of dicts with keys: label, y_range, eta, h_fit, delta2_fit, u_rep
    """
    def true_drift_fn(y_val):
        return np.sign(y_val) * np.abs(y_val)**q

    query_points_orig = query_points * x_std + x_mean
    abs_query_orig = np.abs(query_points_orig.flatten())

    # Define bins
    if bin_method == "tertiles":
        q33 = np.percentile(abs_query_orig, 33)
        q67 = np.percentile(abs_query_orig, 67)
        bins = [
            (0, q33, "lower"),
            (q33, q67, "middle"),
            (q67, abs_query_orig.max(), "upper"),
        ]
    elif bin_method.startswith("quantiles"):
        # Extract n_bins from "quantiles_N" format
        n_bins = int(bin_method.split("_")[1]) if "_" in bin_method else 10
        percentiles = np.linspace(0, 100, n_bins + 1)
        bin_edges = np.percentile(abs_query_orig, percentiles)
        bins = [
            (bin_edges[i], bin_edges[i+1], f"bin_{i:02d}")
            for i in range(n_bins)
        ]
    else:
        raise ValueError(f"Unknown bin_method: {bin_method}")

    bin_results = []

    # Check if we have valid fit points
    if len(h_fit) == 0:
        print("Warning: No valid bandwidth points for per-bin fitting (empty h_fit)")
        return bin_results

    import sys
    print(f"\nPer-bin analysis: {len(bins)} bins", flush=True)
    bin_start_time = time.time()

    for bin_idx, (b_min, b_max, label) in enumerate(bins, 1):
        bin_mask = (abs_query_orig >= b_min) & (abs_query_orig < b_max)

        # Minimum 10 queries per bin (enough for stable η estimates)
        if bin_mask.sum() < 10:
            print(f"Warning: {label} bin has only {bin_mask.sum()} queries, skipping", flush=True)
            continue

        bin_queries = query_points[bin_mask]
        n_fits = len(bin_queries) * len(h_fit)
        print(f"  [{bin_idx}/{len(bins)}] {label}: {len(bin_queries)}q × {len(h_fit)}h = {n_fits} fits...", end='', flush=True)

        fit_start = time.time()

        # Compute δ² and u for this bin at fit points
        bin_delta2 = []
        bin_u = []
        for h_z in h_fit:
            d2_list = []
            u_list = []
            for x0 in bin_queries:
                result = cu.local_linear_mean(
                    X_train_z, Y_train_z, x0, h=h_z,
                    ridge=1e-6, weight=kernel
                )
                mu_model = result.mu
                x0_orig = x0 * x_std + x_mean
                mu_true = true_drift_fn(x0_orig)
                mu_model_orig = mu_model * y_std + y_mean
                delta2 = (mu_model_orig - mu_true)**2
                d2_list.append(float(delta2.flatten()[0]))

                # Compute u = |y₀|/h for this query (in z-space)
                u_list.append(float(np.abs(x0.flatten()[0]) / h_z))

            bin_delta2.append(np.mean(d2_list))
            bin_u.append(np.median(u_list))  # Median u at this h across bin queries

        bin_delta2 = np.array(bin_delta2)
        bin_u = np.array(bin_u)
        log_h = np.log10(h_fit)
        log_bin_delta2 = np.log10(bin_delta2)
        eta_bin, _ = np.polyfit(log_h, log_bin_delta2, 1)

        # Compute representative u for this bin (median over fitted h window)
        u_rep = float(np.median(bin_u))

        fit_time = time.time() - fit_start
        elapsed = time.time() - bin_start_time
        rate = bin_idx / elapsed if elapsed > 0 else 0
        eta_mins = (len(bins) - bin_idx) / rate / 60 if rate > 0 else 0
        print(f" {fit_time:.1f}s. η={eta_bin:.3f}, u={u_rep:.3f}. Bin ETA {eta_mins:.1f}min", flush=True)

        bin_results.append({
            'label': label,
            'y_range': (b_min, b_max),
            'eta': eta_bin,
            'n_queries': bin_mask.sum(),
            'h_fit': h_fit,
            'delta2_fit': bin_delta2,
            'u_rep': u_rep
        })

    return bin_results


def run_kernel_analysis(
    X_train_z, Y_train_z, X_test_z, query_points, h_grid, h_star,
    x_std, y_std, x_mean, y_mean, kernel: str, config: Dict
) -> Dict:
    """
    Run full analysis for one kernel.

    Returns
    -------
    results : dict with keys:
        h_grid, h_star, delta2_global, r_eff_over_h, n_eff_global,
        h_fit, delta2_fit, eta_global, span_decades,
        bin_results, weighted_eta
    """
    q = config['system']['q']

    print(f"\n{'='*60}")
    print(f"Kernel: {kernel.upper()}")
    print(f"{'='*60}")

    # Compute δ² over grid
    delta2, r_eff_over_h, n_eff, u_med = compute_delta2_grid(
        X_train_z, Y_train_z, query_points, h_grid,
        x_std, y_std, x_mean, y_mean, kernel, q
    )

    print(f"Computed δ² over {len(h_grid)} bandwidth values")
    print(f"r_eff/h range: [{r_eff_over_h.min():.3f}, {r_eff_over_h.max():.3f}]")
    print(f"u = |y₀|/h range: [{u_med.min():.3f}, {u_med.max():.3f}]")

    # Fit global η
    locality_guards = config['kernels']['locality_guards'][kernel]
    locality_guard = {
        'r_eff_over_h': r_eff_over_h,
        'n_eff': n_eff,
        'r_min': locality_guards['r_eff_min'],
        'r_max': locality_guards['r_eff_max']
    }

    # EARLY DIAGNOSTIC: Check locality guard status before expensive fitting
    print(f"\n🔍 Locality Guard Diagnostic:")
    print(f"  Target range: r_eff/h ∈ [{locality_guard['r_min']:.3f}, {locality_guard['r_max']:.3f}]")
    locality_mask_all = (
        (r_eff_over_h >= locality_guard['r_min']) &
        (r_eff_over_h <= locality_guard['r_max']) &
        (n_eff >= 50)
    )
    print(f"  Overall pass rate: {locality_mask_all.sum()}/{len(r_eff_over_h)} = {locality_mask_all.sum()/len(r_eff_over_h):.1%}")

    # Check fit window specifically
    min_idx = np.argmin(delta2)
    fit_start_mult = config['bandwidth']['fit_start_multiplier']
    fit_start_idx = np.searchsorted(h_grid, h_star * fit_start_mult)
    fit_start_idx = max(fit_start_idx, min_idx + 1)

    if fit_start_idx < len(h_grid):
        fit_window_mask = locality_mask_all[fit_start_idx:]
        print(f"  Fit window (h ≥ {fit_start_mult:.1f}×h*): {fit_window_mask.sum()}/{len(fit_window_mask)} pass = {fit_window_mask.sum()/len(fit_window_mask):.1%}")
        print(f"  r_eff/h in fit window: [{r_eff_over_h[fit_start_idx:].min():.3f}, {r_eff_over_h[fit_start_idx:].max():.3f}]")

        if fit_window_mask.sum() == 0:
            print(f"  ⚠️  WARNING: ZERO points pass locality guard in fit window!")
            print(f"  ⚠️  This will result in empty h_fit and failed experiment.")
            print(f"  Suggestions:")
            print(f"    - Relax r_eff_min from {locality_guard['r_min']:.3f} to {r_eff_over_h[fit_start_idx:].min():.3f}")
            print(f"    - Or reduce fit_start_multiplier from {fit_start_mult:.1f}")
        elif fit_window_mask.sum() < 5:
            print(f"  ⚠️  WARNING: Only {fit_window_mask.sum()} points in fit window - may be insufficient!")
    print()

    (h_fit, delta2_fit, eta_global, span_decades, pass_rate,
     ci_low_global, ci_high_global, global_diagnostics) = fit_eta_right_tail(
        h_grid, delta2, h_star,
        config['bandwidth']['fit_start_multiplier'],
        locality_guard,
        config['bandwidth']['min_span_decades'],
        config
    )

    print(f"\nGlobal fit:")
    theory_eta = config['system'].get('theory_eta', 2 * config['system']['q'])
    print(f"  η = {eta_global:.3f} (theory: {theory_eta:.1f})")
    if not np.isnan(ci_low_global):
        print(f"  95% CI: [{ci_low_global:.3f}, {ci_high_global:.3f}]")
    print(f"  Fit span: {span_decades:.2f} decades ({len(h_fit)} points)")
    print(f"  Fit quality: {global_diagnostics['quality']}")
    print(f"  Locality guard pass rate: {pass_rate:.1%}")

    # Per-bin analysis
    bin_results = compute_per_bin_eta(
        X_train_z, Y_train_z, query_points, h_fit, h_grid, u_med,
        x_std, y_std, x_mean, y_mean, kernel, q,
        config['queries']['bins']['method']
    )

    # Weighted average
    if len(bin_results) > 0:
        bin_weights = np.array([b['n_queries'] for b in bin_results])
        bin_etas = np.array([b['eta'] for b in bin_results])
        weighted_eta = np.average(bin_etas, weights=bin_weights)

        print(f"\nPer-bin results:")
        for b in bin_results:
            print(f"  {b['label']:8s}: η = {b['eta']:.3f} ({b['n_queries']} queries)")
        print(f"  Weighted: η = {weighted_eta:.3f}")
    else:
        weighted_eta = np.nan

    return {
        'h_grid': h_grid,
        'h_star': h_star,
        'delta2_global': delta2,
        'r_eff_over_h': r_eff_over_h,
        'n_eff_global': n_eff,
        'h_fit': h_fit,
        'delta2_fit': delta2_fit,
        'eta_global': eta_global,
        'ci_low_global': ci_low_global,
        'ci_high_global': ci_high_global,
        'global_diagnostics': global_diagnostics,
        'span_decades': span_decades,
        'pass_rate': pass_rate,
        'bin_results': bin_results,
        'weighted_eta': weighted_eta
    }


def save_results(results: Dict, config: Dict):
    """Save results to JSON, CSV table, and generate figures."""
    output_dir = Path(config['output']['results_json']).parent
    output_dir.mkdir(parents=True, exist_ok=True)

    # 1. Save JSON (using sanitize_for_json to handle numpy types)
    json_path = Path(config['output']['results_json'])

    with open(json_path, 'w') as f:
        json.dump(sanitize_for_json(results), f, indent=2)
    print(f"\nSaved results to {json_path}")

    # 2. Generate table
    table_path = Path(config['output']['table'])
    table_path.parent.mkdir(parents=True, exist_ok=True)
    generate_summary_table(results, config, table_path)

    # 3. Generate main figure
    fig_path = Path(config['output']['figure'])
    fig_path.parent.mkdir(parents=True, exist_ok=True)
    theory_eta = config['system'].get('theory_eta', 2 * config['system']['q'])

    plotting.plot_main_figure_4panel(results, theory_eta, output_path=fig_path)
    print(f"Saved main figure to {fig_path}")

    # 4. Generate η(u) overlay plot (if bin results exist)
    if 'tricube' in results and 'bin_results' in results['tricube']:
        overlay_path = Path(config['output'].get('figure_overlay', 'results/figures/eta_u_overlay.png'))
        overlay_path.parent.mkdir(parents=True, exist_ok=True)

        q = config['system']['q']
        p = config.get('theory', {}).get('transition_sharpness_p', 2.0)

        plot_eta_u_overlay(
            bin_results=results['tricube']['bin_results'],
            q=q,
            p=p,
            output_path=overlay_path
        )
        print(f"Saved η(u) overlay to {overlay_path}")


def generate_summary_table(results: Dict, config: Dict, output_path: Path):
    """Generate CSV summary table."""
    theory_eta = config['system'].get('theory_eta', 2 * config['system']['q'])

    rows = []

    # Global results
    for kernel in ['tricube', 'gaussian']:
        if kernel not in results or kernel in ['config', 'locality_guards']:
            continue
        res = results[kernel]
        rows.append({
            'kernel': kernel,
            'bin': 'global',
            'eta': f"{res['eta_global']:.4f}",
            'gap_from_theory': f"{res['eta_global'] - theory_eta:.4f}",
            'gap_percent': f"{100 * (res['eta_global'] - theory_eta) / theory_eta:.1f}",
            'span_decades': f"{res['span_decades']:.2f}",
            'n_fit_points': str(len(res['h_fit'])),
            'r_eff_over_h_median': f"{np.median(res['r_eff_over_h']):.3f}",
            'locality_pass_rate': f"{res['pass_rate']:.2f}"
        })

    # Per-bin results (tricube only)
    if 'tricube' in results and 'bin_results' in results['tricube']:
        for b in results['tricube']['bin_results']:
            rows.append({
                'kernel': 'tricube',
                'bin': b['label'],
                'eta': f"{b['eta']:.4f}",
                'gap_from_theory': f"{b['eta'] - theory_eta:.4f}",
                'gap_percent': f"{100 * (b['eta'] - theory_eta) / theory_eta:.1f}",
                'n_queries': str(b['n_queries']),
                'y_range_min': f"{b['y_range'][0]:.4f}",
                'y_range_max': f"{b['y_range'][1]:.4f}"
            })

    # Weighted results
    for kernel in ['tricube', 'gaussian']:
        if kernel in results and 'weighted_eta' in results[kernel]:
            weighted_eta = results[kernel]['weighted_eta']
            if not np.isnan(weighted_eta):
                rows.append({
                    'kernel': kernel,
                    'bin': 'weighted',
                    'eta': f"{weighted_eta:.4f}",
                    'gap_from_theory': f"{weighted_eta - theory_eta:.4f}",
                    'gap_percent': f"{100 * (weighted_eta - theory_eta) / theory_eta:.1f}"
                })

    # Write CSV manually
    if rows:
        # Get all unique keys
        all_keys = set()
        for row in rows:
            all_keys.update(row.keys())
        fieldnames = sorted(all_keys)

        with open(output_path, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)

    print(f"Saved summary table to {output_path}")


def check_acceptance_criteria(results: Dict, config: Dict) -> bool:
    """Check if results meet acceptance criteria."""
    criteria = config['acceptance_criteria']
    tricube = results.get('tricube', {})

    print(f"\n{'='*60}")
    print("ACCEPTANCE CRITERIA CHECK")
    print(f"{'='*60}")

    checks = []

    # Fit span
    span = tricube.get('span_decades', 0)
    span_ok = span >= criteria['fit_span_decades_min']
    checks.append(span_ok)
    status = "✓" if span_ok else "✗"
    print(f"{status} Fit span: {span:.2f} ≥ {criteria['fit_span_decades_min']:.1f} decades")

    # Middle bin eta
    bin_results = tricube.get('bin_results', [])
    if len(bin_results) >= 2:
        mid_eta = bin_results[len(bin_results)//2]['eta']
        mid_ok = (criteria['middle_bin_eta_min'] <= mid_eta <= criteria['middle_bin_eta_max'])
        checks.append(mid_ok)
        status = "✓" if mid_ok else "✗"
        print(f"{status} Middle bin η: {mid_eta:.2f} ∈ [{criteria['middle_bin_eta_min']:.1f}, {criteria['middle_bin_eta_max']:.1f}]")

    # Weighted eta
    weighted_eta = tricube.get('weighted_eta', np.nan)
    if not np.isnan(weighted_eta):
        weighted_ok = weighted_eta >= criteria['weighted_eta_min']
        checks.append(weighted_ok)
        status = "✓" if weighted_ok else "✗"
        print(f"{status} Weighted η: {weighted_eta:.2f} ≥ {criteria['weighted_eta_min']:.1f}")

    # Locality pass rate
    pass_rate = tricube.get('pass_rate', 0)
    pass_ok = pass_rate >= criteria['locality_guard_pass_rate_min']
    checks.append(pass_ok)
    status = "✓" if pass_ok else "✗"
    print(f"{status} Locality pass rate: {pass_rate:.1%} ≥ {criteria['locality_guard_pass_rate_min']:.0%}")

    all_passed = all(checks)
    print(f"\n{'='*60}")
    if all_passed:
        print("✓✓✓ ALL CRITERIA MET ✓✓✓")
    else:
        print("⚠️  Some criteria not met")
    print(f"{'='*60}\n")

    return all_passed


def main():
    parser = argparse.ArgumentParser(description="Run clean locality experiment")
    parser.add_argument("--config", type=str, default="configs/tier1_clean.json",
                        help="Path to config JSON")
    args = parser.parse_args()

    # Load config
    config_path = Path(args.config)
    config = load_config(config_path)

    print(f"\n{'='*60}")
    print(f"LOCALITY VALIDATION EXPERIMENT")
    print(f"Config: {config_path}")
    print(f"{'='*60}\n")

    # Setup RNG
    rng = cu.make_rng(config['system']['seed'])

    # Simulate and prepare data
    print("Simulating system...")
    (X_train_z, Y_train_z, X_test_z, query_points,
     x_std, y_std, x_mean, y_mean, n_eff, h_star) = simulate_and_prepare(config, rng)

    print(f"n_train: {len(X_train_z)}, n_eff: {n_eff:.1f}, h*: {h_star:.4f}")
    print(f"n_queries: {len(query_points)}")

    # Bandwidth grid
    h_mult = np.array(config['bandwidth']['h_star_multipliers'])
    h_grid = h_mult * h_star
    print(f"Bandwidth grid: {len(h_grid)} points, [{h_mult[0]:.1f}×h*, {h_mult[-1]:.1f}×h*]")

    # Run analysis for each kernel
    results = {}
    results['locality_guards'] = config['kernels']['locality_guards']

    for kernel in [config['kernels']['primary'], config['kernels']['control']]:
        results[kernel] = run_kernel_analysis(
            X_train_z, Y_train_z, X_test_z, query_points, h_grid, h_star,
            x_std, y_std, x_mean, y_mean, kernel, config
        )

    # Save results
    save_results(results, config)

    # Check acceptance criteria
    check_acceptance_criteria(results, config)

    print("\n✓ Experiment complete!")


if __name__ == "__main__":
    main()
