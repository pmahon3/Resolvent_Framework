"""
Robust slope estimation with quality guards for locality validation.

Implements:
- Theil-Sen robust slope estimation
- Second-derivative curvature guard
- Monotonicity check
- Per-bin fit window auto-selection
- Bootstrap confidence intervals
"""
import numpy as np
from typing import Tuple, Optional, Dict
from scipy import stats


def theil_sen_slope(x: np.ndarray, y: np.ndarray) -> Tuple[float, float]:
    """
    Compute Theil-Sen robust slope estimate.

    Parameters
    ----------
    x, y : arrays
        Data in log-log space (log10(h), log10(δ²))

    Returns
    -------
    slope, intercept : floats
        Robust linear fit parameters
    """
    # Use scipy's theilslopes (equivalent to Theil-Sen for simple regression)
    result = stats.theilslopes(y, x)
    slope = result.slope
    intercept = result.intercept

    return slope, intercept


def check_monotonicity(y: np.ndarray, min_violations: int = 2) -> bool:
    """
    Check if y is monotonically increasing (allowing small violations).

    Parameters
    ----------
    y : array
        Data to check (log10(δ²))
    min_violations : int
        Maximum allowed violations

    Returns
    -------
    is_monotone : bool
    """
    diffs = np.diff(y)
    violations = np.sum(diffs < 0)
    return violations <= min_violations


def compute_curvature(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    """
    Compute second derivative (curvature) using finite differences.

    Parameters
    ----------
    x, y : arrays
        Data in log-log space

    Returns
    -------
    curvature : array
        |d²y/dx²| at interior points
    """
    if len(x) < 3:
        return np.array([])

    # Second derivative: d²y/dx² ≈ (y[i+1] - 2*y[i] + y[i-1]) / dx²
    dx = np.diff(x)
    d2y = np.diff(np.diff(y))
    dx_mid = dx[:-1]  # Use left spacing

    curvature = np.abs(d2y / dx_mid**2)

    return curvature


def select_fit_window(
    h_grid: np.ndarray,
    delta2: np.ndarray,
    h_star: float,
    fit_start_mult: float,
    locality_mask: np.ndarray,
    curvature_threshold: float = 0.08,
    min_span_decades: float = 1.0
) -> Tuple[np.ndarray, np.ndarray, Dict]:
    """
    Auto-select fit window with quality guards.

    Applies:
    1. Locality guard (r_eff/h constraints)
    2. Monotonicity check
    3. Curvature guard (second derivative)
    4. Minimum span requirement

    Parameters
    ----------
    h_grid : array
        Bandwidth values
    delta2 : array
        Bias² values
    h_star : float
        Optimal bandwidth
    fit_start_mult : float
        Start fit at h_star × fit_start_mult
    locality_mask : array (bool)
        Pre-computed locality constraint
    curvature_threshold : float
        Max allowed |d²/dh²|
    min_span_decades : float
        Minimum span in decades

    Returns
    -------
    h_fit, delta2_fit : arrays
        Selected window
    diagnostics : dict
        Quality metrics
    """
    # Start from h_star × fit_start_mult
    min_idx = np.argmin(delta2)
    fit_start_idx = np.searchsorted(h_grid, h_star * fit_start_mult)
    fit_start_idx = max(fit_start_idx, min_idx + 1)

    # Apply locality mask
    h_cand = h_grid[fit_start_idx:]
    delta2_cand = delta2[fit_start_idx:]
    loc_mask_tail = locality_mask[fit_start_idx:]

    h_cand = h_cand[loc_mask_tail]
    delta2_cand = delta2_cand[loc_mask_tail]

    if len(h_cand) < 3:
        # Not enough points
        return h_cand, delta2_cand, {
            'monotone': False,
            'mean_curvature': np.nan,
            'span_decades': 0.0,
            'n_points': len(h_cand),
            'quality': 'insufficient_points'
        }

    # Check monotonicity
    log_h = np.log10(h_cand)
    log_delta2 = np.log10(delta2_cand)
    is_monotone = check_monotonicity(log_delta2, min_violations=2)

    # Compute curvature
    curvature = compute_curvature(log_h, log_delta2)
    mean_curvature = np.mean(curvature) if len(curvature) > 0 else np.nan

    # Apply curvature guard: find longest segment with low curvature
    if len(curvature) > 0 and not np.all(curvature <= curvature_threshold):
        # Find segments with low curvature
        low_curve_mask = np.concatenate([[True], curvature <= curvature_threshold, [True]])

        # Find longest contiguous segment
        changes = np.diff(low_curve_mask.astype(int))
        starts = np.where(changes == 1)[0]
        ends = np.where(changes == -1)[0]

        if len(starts) > 0 and len(ends) > 0:
            segment_lengths = ends - starts
            longest_idx = np.argmax(segment_lengths)
            start_idx = starts[longest_idx]
            end_idx = ends[longest_idx]

            h_cand = h_cand[start_idx:end_idx]
            delta2_cand = delta2_cand[start_idx:end_idx]
            log_h = np.log10(h_cand)
            log_delta2 = np.log10(delta2_cand)

            # Recompute curvature for selected segment
            curvature = compute_curvature(log_h, log_delta2)
            mean_curvature = np.mean(curvature) if len(curvature) > 0 else np.nan

    # Check span
    if len(h_cand) < 2:
        span_decades = 0.0
    else:
        span_decades = np.log10(h_cand[-1] / h_cand[0])

    # Quality assessment
    if len(h_cand) < 3:
        quality = 'insufficient_points'
    elif span_decades < min_span_decades:
        quality = 'short_span'
    elif not is_monotone:
        quality = 'non_monotone'
    elif mean_curvature > curvature_threshold:
        quality = 'high_curvature'
    else:
        quality = 'good'

    diagnostics = {
        'monotone': is_monotone,
        'mean_curvature': mean_curvature,
        'span_decades': span_decades,
        'n_points': len(h_cand),
        'quality': quality
    }

    return h_cand, delta2_cand, diagnostics


def bootstrap_slope_ci(
    x: np.ndarray,
    y: np.ndarray,
    n_resamples: int = 1000,
    confidence_level: float = 0.95,
    use_robust: bool = True,
    seed: Optional[int] = None
) -> Tuple[float, float, float]:
    """
    Bootstrap confidence intervals for slope.

    Parameters
    ----------
    x, y : arrays
        Data in log-log space
    n_resamples : int
        Number of bootstrap samples
    confidence_level : float
        CI level (e.g., 0.95 for 95%)
    use_robust : bool
        Use Theil-Sen (True) or OLS (False)
    seed : int, optional
        Random seed

    Returns
    -------
    slope, ci_low, ci_high : floats
    """
    if seed is not None:
        np.random.seed(seed)

    n = len(x)
    slopes = []

    for _ in range(n_resamples):
        # Resample with replacement
        indices = np.random.choice(n, size=n, replace=True)
        x_boot = x[indices]
        y_boot = y[indices]

        # Fit slope
        if use_robust:
            slope_boot, _ = theil_sen_slope(x_boot, y_boot)
        else:
            slope_boot, _ = np.polyfit(x_boot, y_boot, 1)

        slopes.append(slope_boot)

    slopes = np.array(slopes)

    # Compute percentiles
    alpha = 1 - confidence_level
    ci_low = np.percentile(slopes, 100 * alpha / 2)
    ci_high = np.percentile(slopes, 100 * (1 - alpha / 2))
    slope = np.median(slopes)

    return slope, ci_low, ci_high


def fit_with_diagnostics(
    h_grid: np.ndarray,
    delta2: np.ndarray,
    h_star: float,
    fit_start_mult: float,
    locality_mask: np.ndarray,
    use_robust: bool = True,
    curvature_threshold: float = 0.08,
    min_span_decades: float = 1.0,
    bootstrap_n: int = 0,
    bootstrap_seed: Optional[int] = None
) -> Dict:
    """
    Complete fitting pipeline with all guards and diagnostics.

    Parameters
    ----------
    h_grid, delta2 : arrays
        Bandwidth and bias² data
    h_star : float
        Optimal bandwidth
    fit_start_mult : float
        Start fit at h_star × fit_start_mult
    locality_mask : array (bool)
        Pre-computed locality constraint
    use_robust : bool
        Use Theil-Sen (True) or OLS (False)
    curvature_threshold : float
        Max allowed |d²/dh²|
    min_span_decades : float
        Minimum span in decades
    bootstrap_n : int
        Number of bootstrap samples (0 = skip)
    bootstrap_seed : int, optional
        Random seed for bootstrap

    Returns
    -------
    results : dict
        Contains: h_fit, delta2_fit, eta, ci_low, ci_high, diagnostics
    """
    # Auto-select fit window
    h_fit, delta2_fit, diagnostics = select_fit_window(
        h_grid, delta2, h_star, fit_start_mult, locality_mask,
        curvature_threshold, min_span_decades
    )

    if len(h_fit) < 2:
        # Failed to find valid window
        return {
            'h_fit': h_fit,
            'delta2_fit': delta2_fit,
            'eta': np.nan,
            'ci_low': np.nan,
            'ci_high': np.nan,
            'diagnostics': diagnostics
        }

    # Fit slope
    log_h = np.log10(h_fit)
    log_delta2 = np.log10(delta2_fit)

    if use_robust:
        eta, intercept = theil_sen_slope(log_h, log_delta2)
    else:
        eta, intercept = np.polyfit(log_h, log_delta2, 1)

    # Bootstrap CIs if requested
    if bootstrap_n > 0:
        eta_boot, ci_low, ci_high = bootstrap_slope_ci(
            log_h, log_delta2, n_resamples=bootstrap_n,
            use_robust=use_robust, seed=bootstrap_seed
        )
        # Use bootstrap median as eta
        eta = eta_boot
    else:
        ci_low = np.nan
        ci_high = np.nan

    return {
        'h_fit': h_fit,
        'delta2_fit': delta2_fit,
        'eta': eta,
        'ci_low': ci_low,
        'ci_high': ci_high,
        'intercept': intercept,
        'diagnostics': diagnostics
    }
