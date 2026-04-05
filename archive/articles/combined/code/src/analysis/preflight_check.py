"""
Quick pre-flight check for locality guards.

Tests a few representative bandwidths to verify guards will pass
before committing to a full 2.5 hour run.
"""

import json
import numpy as np
from pathlib import Path
import sys

from src.core import common_utils as cu
from src.simulation.tier1_scalar import simulate_scalar_system


def preflight_check(config_path: Path):
    """
    Quick test with 5 bandwidths to check if locality guards will work.

    Takes ~1-2 minutes instead of 2.5 hours.
    """
    print(f"\n{'='*60}")
    print("PRE-FLIGHT LOCALITY GUARD CHECK")
    print(f"Config: {config_path}")
    print(f"{'='*60}\n")

    # Load config
    with open(config_path, 'r') as f:
        config = json.load(f)

    # Simulate system (same as full run)
    q = config['system']['q']
    sigma = config['system']['sigma']
    n = config['system']['n']
    seed = config['system']['seed']

    rng = cu.make_rng(seed)
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

    # Select queries (same as full run)
    X_test_orig = X_test_z * x_std + x_mean
    abs_x_orig = np.abs(X_test_orig.flatten())
    p_low, p_high = config['queries']['percentile_range']
    p_low_val = np.percentile(abs_x_orig, p_low)
    p_high_val = np.percentile(abs_x_orig, p_high)

    interior_mask = (abs_x_orig >= p_low_val) & (abs_x_orig <= p_high_val)
    interior_indices = np.where(interior_mask)[0]

    # Use just 20 queries for quick test
    n_queries_test = min(20, len(interior_indices))
    query_idx = rng.choice(interior_indices, size=n_queries_test, replace=False)
    query_points = X_test_z[query_idx]

    # Compute h*
    n_eff = n_train / cu.iact(y[:n_train])
    h_star = n_eff ** (-1 / (2*q + 1))

    print(f"System: q={q}, σ={sigma}, n={n}, seed={seed}")
    print(f"n_train: {n_train}, n_eff: {n_eff:.1f}, h*: {h_star:.4f}")
    print(f"Test queries: {n_queries_test} (instead of {config['queries']['n_queries']})\n")

    # Test bandwidths: min, start of fit window, middle, end of fit window, max
    h_mults = config['bandwidth']['h_star_multipliers']
    fit_start_mult = config['bandwidth']['fit_start_multiplier']

    # Pick 5 representative bandwidths
    test_mults = [
        h_mults[0],                          # Minimum
        fit_start_mult,                      # Start of fit window
        h_mults[len(h_mults)//3],           # Lower third
        h_mults[2*len(h_mults)//3],         # Upper third
        h_mults[-1]                          # Maximum
    ]

    print(f"Testing {len(test_mults)} representative bandwidths (instead of {len(h_mults)}):")
    print(f"  Multipliers: {[f'{m:.1f}' for m in test_mults]}")
    print(f"  Fit window starts at: {fit_start_mult:.1f}×h*\n")

    # Test each kernel
    for kernel in [config['kernels']['primary'], config['kernels']['control']]:
        guards = config['kernels']['locality_guards'][kernel]
        r_min = guards['r_eff_min']
        r_max = guards['r_eff_max']

        print(f"{'='*60}")
        print(f"Kernel: {kernel.upper()}")
        print(f"Locality guard: r_eff/h ∈ [{r_min:.3f}, {r_max:.3f}]")
        print(f"{'='*60}\n")

        results = []

        for mult in test_mults:
            h_z = mult * h_star
            r_eff_list = []
            n_eff_list = []

            # Test with sample queries
            for x0 in query_points:
                result = cu.local_linear_mean(
                    X_train_z, Y_train_z, x0, h=h_z,
                    ridge=1e-6, weight=kernel
                )
                r_eff_list.append(result.r_eff / h_z)
                n_eff_list.append(result.n_eff)

            r_eff_over_h = np.median(r_eff_list)
            n_eff_val = np.median(n_eff_list)

            # Check if passes guard
            passes_r_min = r_eff_over_h >= r_min
            passes_r_max = r_eff_over_h <= r_max
            passes_neff = n_eff_val >= 50
            passes_all = passes_r_min and passes_r_max and passes_neff

            in_fit_window = mult >= fit_start_mult

            status = "✓" if passes_all else "✗"
            window_marker = " [FIT]" if in_fit_window else ""

            print(f"{status} h={mult:5.1f}×h* = {h_z:.4f}{window_marker}")
            print(f"    r_eff/h = {r_eff_over_h:.3f}  ", end='')

            if not passes_r_min:
                print(f"FAIL: < {r_min:.3f}")
            elif not passes_r_max:
                print(f"FAIL: > {r_max:.3f}")
            else:
                print(f"PASS")

            if not passes_neff:
                print(f"    n_eff = {n_eff_val:.1f}  FAIL: < 50")

            results.append({
                'mult': mult,
                'in_fit': in_fit_window,
                'passes': passes_all,
                'r_eff_over_h': r_eff_over_h
            })

        # Summary
        print(f"\n{'-'*60}")
        all_results = [r for r in results]
        fit_results = [r for r in results if r['in_fit']]

        all_pass = sum(1 for r in all_results if r['passes'])
        fit_pass = sum(1 for r in fit_results if r['passes'])

        print(f"Summary for {kernel}:")
        print(f"  All bandwidths: {all_pass}/{len(all_results)} pass ({100*all_pass/len(all_results):.0f}%)")
        print(f"  Fit window:     {fit_pass}/{len(fit_results)} pass ({100*fit_pass/len(fit_results):.0f}%)")

        r_eff_range = [r['r_eff_over_h'] for r in results]
        print(f"  r_eff/h range:  [{min(r_eff_range):.3f}, {max(r_eff_range):.3f}]")
        print(f"  Guard range:    [{r_min:.3f}, {r_max:.3f}]")

        if fit_pass == 0:
            print(f"\n  ⚠️  CRITICAL: ZERO fit window points pass!")
            print(f"  ⚠️  Full experiment will FAIL")
            print(f"  Suggestion: Relax r_eff_min from {r_min:.3f} to {min(r_eff_range):.3f}")
        elif fit_pass < len(fit_results) * 0.5:
            print(f"\n  ⚠️  WARNING: < 50% of fit window passes")
            print(f"  ⚠️  May have insufficient points for robust fit")
        else:
            print(f"\n  ✓ PASS: Sufficient points in fit window")
            print(f"  ✓ Full experiment should succeed")

        print()

    print(f"{'='*60}")
    print("Pre-flight check complete!")
    print(f"{'='*60}\n")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python -m src.analysis.preflight_check <config.json>")
        sys.exit(1)

    config_path = Path(sys.argv[1])
    preflight_check(config_path)
