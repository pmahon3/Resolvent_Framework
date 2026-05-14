"""
Test and validation utilities for common_utils.py components.

Provides smoke tests and sanity checks for:
- Divergences (JS, MMD)
- IACT estimation
- Bootstrap
- Local linear regression
- Plotting utilities
"""

from __future__ import annotations
import numpy as np
import numpy.typing as npt
from typing import Callable
import logging

Array = npt.NDArray[np.float64]


def test_divergence_symmetry(
    divergence_fn: Callable[[Array, Array], float],
    name: str,
    rng: np.random.Generator,
    logger: logging.Logger,
) -> bool:
    """
    Test that divergence is symmetric for symmetric f-divergences (JS).

    Parameters
    ----------
    divergence_fn : Callable
        Function computing D(P || Q) from samples.
    name : str
        Name for logging.
    rng : np.random.Generator
        RNG for test data.
    logger : logging.Logger
        Logger.

    Returns
    -------
    passed : bool
    """
    logger.info(f"Testing {name} symmetry...")

    # Generate two Gaussians
    x_p = rng.normal(0, 1, size=(500, 2))
    x_q = rng.normal(0.5, 1, size=(500, 2))

    d_pq = divergence_fn(x_p, x_q)
    d_qp = divergence_fn(x_q, x_p)

    # JS should be symmetric; KL is not
    rel_diff = abs(d_pq - d_qp) / (abs(d_pq) + 1e-12)

    passed = rel_diff < 0.01
    if passed:
        logger.info(f"  ✓ {name} symmetry passed: D(P||Q)={d_pq:.4f}, D(Q||P)={d_qp:.4f}, rel_diff={rel_diff:.3e}")
    else:
        logger.warning(f"  ✗ {name} symmetry failed: D(P||Q)={d_pq:.4f}, D(Q||P)={d_qp:.4f}, rel_diff={rel_diff:.3e}")

    return passed


def test_divergence_identical(
    divergence_fn: Callable[[Array, Array], float],
    name: str,
    rng: np.random.Generator,
    logger: logging.Logger,
) -> bool:
    """
    Test that divergence is zero for identical distributions.

    Parameters
    ----------
    divergence_fn : Callable
        Function computing D(P || Q) from samples.
    name : str
        Name for logging.
    rng : np.random.Generator
        RNG for test data.
    logger : logging.Logger
        Logger.

    Returns
    -------
    passed : bool
    """
    logger.info(f"Testing {name} on identical distributions...")

    x = rng.normal(0, 1, size=(500, 2))
    d_xx = divergence_fn(x, x)

    passed = d_xx < 0.01
    if passed:
        logger.info(f"  ✓ {name} identity passed: D(X||X)={d_xx:.4e}")
    else:
        logger.warning(f"  ✗ {name} identity failed: D(X||X)={d_xx:.4e} (should be ~0)")

    return passed


def test_divergence_ordering(
    divergence_fn: Callable[[Array, Array], float],
    name: str,
    rng: np.random.Generator,
    logger: logging.Logger,
) -> bool:
    """
    Test that divergence increases with separation of distributions.

    Parameters
    ----------
    divergence_fn : Callable
        Function computing D(P || Q) from samples.
    name : str
        Name for logging.
    rng : np.random.Generator
        RNG for test data.
    logger : logging.Logger
        Logger.

    Returns
    -------
    passed : bool
    """
    logger.info(f"Testing {name} ordering...")

    x_p = rng.normal(0, 1, size=(500, 2))

    # Q close to P
    x_q1 = rng.normal(0.2, 1, size=(500, 2))
    d1 = divergence_fn(x_p, x_q1)

    # Q far from P
    x_q2 = rng.normal(2.0, 1, size=(500, 2))
    d2 = divergence_fn(x_p, x_q2)

    passed = d2 > d1
    if passed:
        logger.info(f"  ✓ {name} ordering passed: D(P||Q_near)={d1:.4f} < D(P||Q_far)={d2:.4f}")
    else:
        logger.warning(f"  ✗ {name} ordering failed: D(P||Q_near)={d1:.4f} >= D(P||Q_far)={d2:.4f}")

    return passed


def test_iact_ar1(
    iact_fn: Callable[[Array], float],
    logger: logging.Logger,
    rng: np.random.Generator,
) -> bool:
    """
    Test IACT on AR(1) process with known theoretical value.

    For AR(1): y_t = rho * y_{t-1} + eps_t,
    theoretical tau_mix = (1 + rho) / (1 - rho)

    Parameters
    ----------
    iact_fn : Callable
        Function computing IACT from 1D array.
    logger : logging.Logger
        Logger.
    rng : np.random.Generator
        RNG for test data.

    Returns
    -------
    passed : bool
    """
    logger.info("Testing IACT on AR(1)...")

    rho = 0.7
    n = 10000
    tau_theory = (1 + rho) / (1 - rho)  # = 5.67

    # Simulate AR(1)
    y = np.zeros(n)
    eps = rng.normal(0, np.sqrt(1 - rho**2), size=n)
    for t in range(1, n):
        y[t] = rho * y[t-1] + eps[t]

    tau_est = iact_fn(y)

    rel_error = abs(tau_est - tau_theory) / tau_theory

    passed = rel_error < 0.2  # Allow 20% error (finite sample)
    if passed:
        logger.info(f"  ✓ IACT test passed: estimated={tau_est:.2f}, theory={tau_theory:.2f}, rel_error={rel_error:.2%}")
    else:
        logger.warning(f"  ✗ IACT test failed: estimated={tau_est:.2f}, theory={tau_theory:.2f}, rel_error={rel_error:.2%}")

    return passed


def test_local_linear_exact(
    local_linear_fn: Callable,
    logger: logging.Logger,
    rng: np.random.Generator,
) -> bool:
    """
    Test local linear regression on exactly linear data.

    Generate Y = A X + b + noise, fit at x0, check A and b recovery.

    Parameters
    ----------
    local_linear_fn : Callable
        Local linear fit function.
    logger : logging.Logger
        Logger.
    rng : np.random.Generator
        RNG.

    Returns
    -------
    passed : bool
    """
    logger.info("Testing local linear regression on linear data...")

    # True linear model: y = 2x + 3 + noise
    n = 1000
    X = rng.uniform(-1, 1, size=(n, 1))
    A_true = np.array([[2.0]])
    b_true = np.array([3.0])
    noise = rng.normal(0, 0.1, size=(n, 1))
    Y = X @ A_true.T + b_true + noise

    # Fit at x0 = 0 with large bandwidth (should recover global linear fit)
    x0 = np.array([0.0])
    h = 2.0  # Large bandwidth

    result = local_linear_fn(X, Y, x0, h=h, ridge=1e-6)

    # Check A and b
    A_error = np.abs(result.A - A_true).max()
    b_error = np.abs(result.b - b_true).max()

    passed = (A_error < 0.2) and (b_error < 0.3)
    if passed:
        logger.info(f"  ✓ Local linear test passed: A_est={result.A.flatten()}, b_est={result.b}, errors: A={A_error:.3f}, b={b_error:.3f}")
    else:
        logger.warning(f"  ✗ Local linear test failed: A_est={result.A.flatten()}, b_est={result.b}, errors: A={A_error:.3f}, b={b_error:.3f}")

    return passed


def test_bootstrap_coverage(
    bootstrap_fn: Callable,
    logger: logging.Logger,
    rng: np.random.Generator,
) -> bool:
    """
    Test that bootstrap CI has correct coverage on known distribution.

    Generate Gaussian data, bootstrap mean, check if true mean in CI.

    Parameters
    ----------
    bootstrap_fn : Callable
        Bootstrap function.
    logger : logging.Logger
        Logger.
    rng : np.random.Generator
        RNG.

    Returns
    -------
    passed : bool
    """
    logger.info("Testing bootstrap CI coverage...")

    true_mean = 5.0
    data = rng.normal(true_mean, 1.0, size=500)

    def mean_fn(x):
        return np.mean(x)

    result = bootstrap_fn(
        mean_fn,
        data,
        block_length=10,
        n_boot=1000,
        level=0.95,
        rng=rng,
    )

    in_ci = result.ci_low <= true_mean <= result.ci_high

    if in_ci:
        logger.info(f"  ✓ Bootstrap coverage passed: true_mean={true_mean:.3f} in CI=[{result.ci_low:.3f}, {result.ci_high:.3f}]")
    else:
        logger.warning(f"  ✗ Bootstrap coverage failed: true_mean={true_mean:.3f} NOT in CI=[{result.ci_low:.3f}, {result.ci_high:.3f}]")

    return in_ci


def run_all_tests(
    common_utils_module,
    logger: logging.Logger,
    rng: np.random.Generator,
) -> dict[str, bool]:
    """
    Run all validation tests for common_utils.

    Parameters
    ----------
    common_utils_module : module
        Imported common_utils module.
    logger : logging.Logger
        Logger.
    rng : np.random.Generator
        RNG.

    Returns
    -------
    results : dict[str, bool]
        Test results.
    """
    logger.info("=" * 60)
    logger.info("Running validation tests for common_utils")
    logger.info("=" * 60)

    results = {}

    # Test JS divergence
    def js_fn(x, y):
        return common_utils_module.js_divergence(x, y, method="kde")

    results['js_symmetry'] = test_divergence_symmetry(js_fn, "JS", rng, logger)
    results['js_identical'] = test_divergence_identical(js_fn, "JS", rng, logger)
    results['js_ordering'] = test_divergence_ordering(js_fn, "JS", rng, logger)

    # Test MMD
    def mmd_fn(x, y):
        mmd2, _ = common_utils_module.mmd_rbf(x, y, use_median_heuristic=True)
        return mmd2

    results['mmd_identical'] = test_divergence_identical(mmd_fn, "MMD", rng, logger)
    results['mmd_ordering'] = test_divergence_ordering(mmd_fn, "MMD", rng, logger)

    # Test IACT
    results['iact_ar1'] = test_iact_ar1(common_utils_module.iact, logger, rng)

    # Test local linear
    results['local_linear_exact'] = test_local_linear_exact(
        common_utils_module.local_linear_mean, logger, rng
    )

    # Test bootstrap
    results['bootstrap_coverage'] = test_bootstrap_coverage(
        common_utils_module.moving_block_bootstrap, logger, rng
    )

    # Summary
    logger.info("=" * 60)
    logger.info("Test summary:")
    n_passed = sum(results.values())
    n_total = len(results)
    for test_name, passed in results.items():
        status = "✓ PASS" if passed else "✗ FAIL"
        logger.info(f"  {status}: {test_name}")
    logger.info(f"Total: {n_passed}/{n_total} passed")
    logger.info("=" * 60)

    return results
