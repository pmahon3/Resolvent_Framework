# common_utils.py

from __future__ import annotations
from dataclasses import dataclass
from typing import Callable, Literal, Optional, Tuple, Sequence, Dict

import numpy as np
import numpy.typing as npt
from scipy import stats
from scipy.spatial.distance import pdist, squareform
import matplotlib.pyplot as plt
import logging

Array = npt.NDArray[np.float64]

# Get logger for this module
logger = logging.getLogger(__name__)


# ----------------------------- RNG & Config -----------------------------

def make_rng(seed: Optional[int] = None) -> np.random.Generator:
    """
    Create a NumPy Generator with an optional seed.

    Parameters
    ----------
    seed : Optional[int]
        If provided, the RNG is reproducible.

    Returns
    -------
    rng : np.random.Generator
    """
    rng = np.random.default_rng(seed)
    if seed is not None:
        logger.debug(f"Created RNG with seed={seed}")
    else:
        logger.debug("Created RNG with random seed")
    return rng


# ----------------------------- Divergences ------------------------------

def js_divergence(
    x_p: Array,
    x_q: Array,
    *,
    method: Literal["kde", "hist"] = "kde",
    bandwidth: Optional[float] = None,
    bins: Optional[int] = None,
    clip: float = 1e-12,
) -> float:
    """
    Jensen–Shannon divergence (JS) between two distributions given samples.

    Design choices
    --------------
    - Works directly with samples (no analytic densities).
    - method="kde" (default): Gaussian KDE with shared bandwidth (scalar) across dims.
      - If `bandwidth` is None, use Scott's rule per-dimension and average.
    - method="hist": shared histogram bins (same edges for P and Q); good for 1D/2D.

    Parameters
    ----------
    x_p, x_q : Array
        Samples from P and Q shaped (n_p, d) and (n_q, d).
    method : {"kde","hist"}
        Density estimator. "kde" recommended for d<=4; "hist" stable for d<=2.
    bandwidth : Optional[float]
        KDE bandwidth (in data units). If None and method="kde", auto-estimate.
    bins : Optional[int]
        If method="hist", number of bins per dimension (1D/2D). If None, use 64.
    clip : float
        Floor to avoid log(0).

    Returns
    -------
    js : float
        JS divergence in nats.
    """
    logger.debug(f"Computing JS divergence: method={method}, n_p={len(x_p)}, n_q={len(x_q)}")

    # Ensure 2D
    if x_p.ndim == 1:
        x_p = x_p.reshape(-1, 1)
    if x_q.ndim == 1:
        x_q = x_q.reshape(-1, 1)

    n_p, d_p = x_p.shape
    n_q, d_q = x_q.shape

    if d_p != d_q:
        raise ValueError(f"Dimension mismatch: x_p has {d_p} dims, x_q has {d_q} dims")

    d = d_p

    if method == "kde":
        return _js_kde(x_p, x_q, bandwidth, clip, d)
    elif method == "hist":
        if d > 2:
            logger.warning(f"hist method with d={d} may be unstable; consider kde")
        if bins is None:
            bins = 64
        return _js_hist(x_p, x_q, bins, clip, d)
    else:
        raise ValueError(f"Unknown method: {method}")


def _js_kde(x_p: Array, x_q: Array, bandwidth: Optional[float], clip: float, d: int) -> float:
    """KDE-based JS divergence."""
    from scipy.stats import gaussian_kde

    # Estimate bandwidth using Scott's rule if not provided
    if bandwidth is None:
        # Scott's rule: h = n^(-1/(d+4)) * sigma
        bw_p = np.mean([np.std(x_p[:, i]) * len(x_p)**(-1/(d+4)) for i in range(d)])
        bw_q = np.mean([np.std(x_q[:, i]) * len(x_q)**(-1/(d+4)) for i in range(d)])
        bandwidth = (bw_p + bw_q) / 2
        logger.debug(f"Auto bandwidth: {bandwidth:.4f}")

    # Fit KDEs
    kde_p = gaussian_kde(x_p.T, bw_method=bandwidth / np.std(x_p))
    kde_q = gaussian_kde(x_q.T, bw_method=bandwidth / np.std(x_q))

    # Evaluate densities on respective samples
    # KL(P||M) ≈ E_P[log(p/m)] ≈ (1/n_p) Σ log(p(x_i)/m(x_i)) where x_i ~ P
    # KL(Q||M) ≈ E_Q[log(q/m)] ≈ (1/n_q) Σ log(q(y_j)/m(y_j)) where y_j ~ Q
    p_at_p = np.clip(kde_p(x_p.T), clip, None)
    q_at_p = np.clip(kde_q(x_p.T), clip, None)
    m_at_p = (p_at_p + q_at_p) / 2

    p_at_q = np.clip(kde_p(x_q.T), clip, None)
    q_at_q = np.clip(kde_q(x_q.T), clip, None)
    m_at_q = (p_at_q + q_at_q) / 2

    # JS = 0.5 * KL(P||M) + 0.5 * KL(Q||M)
    kl_pm = np.mean(np.log(p_at_p / m_at_p))
    kl_qm = np.mean(np.log(q_at_q / m_at_q))
    js = 0.5 * kl_pm + 0.5 * kl_qm

    logger.debug(f"JS(KDE) = {js:.6f}")
    return float(js)


def _js_hist(x_p: Array, x_q: Array, bins: int, clip: float, d: int) -> float:
    """Histogram-based JS divergence (1D or 2D only)."""
    if d == 1:
        # 1D histogram
        x_p_flat = x_p.flatten()
        x_q_flat = x_q.flatten()

        # Shared edges
        edges = shared_bin_edges_1d(x_p_flat, x_q_flat, bins=bins)

        # Compute histograms
        hist_p, _ = np.histogram(x_p_flat, bins=edges, density=True)
        hist_q, _ = np.histogram(x_q_flat, bins=edges, density=True)

        # Normalize to probabilities
        hist_p = hist_p / hist_p.sum()
        hist_q = hist_q / hist_q.sum()

    elif d == 2:
        # 2D histogram
        edges_0 = shared_bin_edges_1d(x_p[:, 0], x_q[:, 0], bins=bins)
        edges_1 = shared_bin_edges_1d(x_p[:, 1], x_q[:, 1], bins=bins)

        hist_p, _, _ = np.histogram2d(x_p[:, 0], x_p[:, 1], bins=[edges_0, edges_1], density=True)
        hist_q, _, _ = np.histogram2d(x_q[:, 0], x_q[:, 1], bins=[edges_0, edges_1], density=True)

        hist_p = hist_p.flatten() / hist_p.sum()
        hist_q = hist_q.flatten() / hist_q.sum()
    else:
        raise ValueError(f"hist method only supports d=1 or d=2, got d={d}")

    # Clip and compute JS
    hist_p = np.clip(hist_p, clip, None)
    hist_q = np.clip(hist_q, clip, None)
    hist_m = (hist_p + hist_q) / 2

    kl_pm = np.sum(hist_p * np.log(hist_p / hist_m))
    kl_qm = np.sum(hist_q * np.log(hist_q / hist_m))
    js = 0.5 * kl_pm + 0.5 * kl_qm

    logger.debug(f"JS(hist) = {js:.6f}")
    return float(js)


def mmd_rbf(
    x_p: Array,
    x_q: Array,
    *,
    bandwidth: Optional[float] = None,
    use_median_heuristic: bool = True,
    return_decomposed: bool = False,
) -> Tuple[float, Optional[Dict[str, float]]]:
    """
    Squared MMD with RBF kernel (unbiased estimator).

    Parameters
    ----------
    x_p, x_q : Array
        Samples from P and Q shaped (n_p, d) and (n_q, d).
    bandwidth : Optional[float]
        RBF kernel lengthscale; if None and `use_median_heuristic`, auto-compute.
    use_median_heuristic : bool
        If True and bandwidth is None, set bandwidth to median pairwise distance.
    return_decomposed : bool
        If True, also return parts {"pp":..., "qq":..., "pq":...}.

    Returns
    -------
    mmd2 : float
        Estimated MMD^2.
    parts : Optional[dict]
        Decomposition components if requested.
    """
    logger.debug(f"Computing MMD: n_p={len(x_p)}, n_q={len(x_q)}")

    # Ensure 2D
    if x_p.ndim == 1:
        x_p = x_p.reshape(-1, 1)
    if x_q.ndim == 1:
        x_q = x_q.reshape(-1, 1)

    # Auto bandwidth
    if bandwidth is None and use_median_heuristic:
        bandwidth = median_heuristic_bandwidth(x_p, x_q)
        logger.debug(f"Auto bandwidth (median heuristic): {bandwidth:.4f}")

    n_p = len(x_p)
    n_q = len(x_q)

    # Compute kernel matrices
    K_pp = rbf_kernel_matrix(x_p, x_p, bandwidth)
    K_qq = rbf_kernel_matrix(x_q, x_q, bandwidth)
    K_pq = rbf_kernel_matrix(x_p, x_q, bandwidth)

    # Unbiased estimator (exclude diagonal for pp and qq)
    term_pp = (K_pp.sum() - np.trace(K_pp)) / (n_p * (n_p - 1))
    term_qq = (K_qq.sum() - np.trace(K_qq)) / (n_q * (n_q - 1))
    term_pq = K_pq.sum() / (n_p * n_q)

    mmd2 = term_pp + term_qq - 2 * term_pq

    logger.debug(f"MMD^2 = {mmd2:.6f} (pp={term_pp:.6f}, qq={term_qq:.6f}, pq={term_pq:.6f})")

    if return_decomposed:
        parts = {"pp": float(term_pp), "qq": float(term_qq), "pq": float(term_pq)}
        return float(mmd2), parts
    else:
        return float(mmd2), None


def rbf_kernel_matrix(x: Array, y: Array, bandwidth: float) -> Array:
    """
    Compute RBF kernel matrix K_ij = exp(-||x_i - y_j||^2 / (2*bandwidth^2)).

    Parameters
    ----------
    x, y : Array
        Arrays of shape (n_x, d) and (n_y, d).
    bandwidth : float
        RBF lengthscale.

    Returns
    -------
    K : Array
        Kernel matrix of shape (n_x, n_y).
    """
    # Compute pairwise squared distances
    # ||x_i - y_j||^2 = ||x_i||^2 + ||y_j||^2 - 2 x_i . y_j
    x_sq = np.sum(x**2, axis=1, keepdims=True)  # (n_x, 1)
    y_sq = np.sum(y**2, axis=1, keepdims=True)  # (n_y, 1)
    sq_dists = x_sq + y_sq.T - 2 * x @ y.T      # (n_x, n_y)

    K = np.exp(-sq_dists / (2 * bandwidth**2))
    return K


def median_heuristic_bandwidth(x: Array, y: Optional[Array] = None) -> float:
    """
    Median pairwise Euclidean distance heuristic.

    Parameters
    ----------
    x : Array
        Samples shape (n_x, d).
    y : Optional[Array]
        If provided, compute median over pairwise distances of x∪y; else just x.

    Returns
    -------
    h : float
        Suggested RBF bandwidth.
    """
    if y is not None:
        z = np.vstack([x, y])
    else:
        z = x

    # Compute pairwise distances
    dists = pdist(z, metric='euclidean')
    h = float(np.median(dists))

    return h


# ------------------------ Autocorrelation / IACT ------------------------

def autocorrelation(
    x: Array,
    *,
    max_lag: Optional[int] = None,
    demean: bool = True,
) -> Array:
    """
    Univariate or multivariate (column-wise) autocorrelation.

    Parameters
    ----------
    x : Array
        Shape (n,) or (n, d). If 2D, compute ACF per column.
    max_lag : Optional[int]
        If None, use floor(n/4).
    demean : bool
        If True, subtract mean before ACF.

    Returns
    -------
    acf : Array
        Autocorrelation(s) shape (L+1,) or (L+1, d), where L = max_lag.
    """
    if x.ndim == 1:
        x = x.reshape(-1, 1)

    n, d = x.shape

    if max_lag is None:
        max_lag = n // 4

    if demean:
        x = x - x.mean(axis=0, keepdims=True)

    acf = np.zeros((max_lag + 1, d))

    for dim in range(d):
        x_dim = x[:, dim]
        var = np.var(x_dim)

        if var < 1e-12:
            logger.warning(f"Near-zero variance in dimension {dim}, ACF may be unreliable")
            acf[:, dim] = 0
            continue

        for lag in range(max_lag + 1):
            if lag == 0:
                acf[lag, dim] = 1.0
            else:
                acf[lag, dim] = np.mean(x_dim[:-lag] * x_dim[lag:]) / var

    if d == 1:
        acf = acf.flatten()

    return acf


def iact(
    x: Array,
    *,
    max_lag: Optional[int] = None,
    cutoff: Literal["first_zero", "stat_threshold"] = "stat_threshold",
) -> float:
    """
    Integrated autocorrelation time (IACT) estimator.

    Parameters
    ----------
    x : Array
        1D array of length n (choose observable like first coordinate).
    max_lag : Optional[int]
        Upper bound for summation; if None, use floor(n/4).
    cutoff : {"first_zero","stat_threshold"}
        - "first_zero": stop sum at first nonpositive acf.
        - "stat_threshold": stop when acf < 2/sqrt(n) (default).

    Returns
    -------
    tau_mix : float
        1 + 2 * sum_{t=1..T*} acf[t].
    """
    if x.ndim != 1:
        raise ValueError("iact expects 1D array")

    n = len(x)
    acf = autocorrelation(x, max_lag=max_lag, demean=True)

    # Determine cutoff point
    if cutoff == "first_zero":
        cutoff_idx = np.where(acf[1:] <= 0)[0]
        if len(cutoff_idx) > 0:
            T_star = cutoff_idx[0] + 1
        else:
            T_star = len(acf) - 1
    elif cutoff == "stat_threshold":
        threshold = 2.0 / np.sqrt(n)
        cutoff_idx = np.where(np.abs(acf[1:]) < threshold)[0]
        if len(cutoff_idx) > 0:
            T_star = cutoff_idx[0] + 1
        else:
            T_star = len(acf) - 1
    else:
        raise ValueError(f"Unknown cutoff: {cutoff}")

    tau_mix = 1.0 + 2.0 * np.sum(acf[1:T_star+1])

    logger.debug(f"IACT: tau_mix={tau_mix:.2f}, cutoff at lag {T_star}")

    return float(tau_mix)


# ------------------------ Bootstrap & Confidence ------------------------

@dataclass
class BootstrapResult:
    stat: float
    ci_low: float
    ci_high: float
    samples: Array  # shape (B,)
    level: float


def moving_block_bootstrap(
    stat_fn: Callable[[Array], float],
    data: Array,
    *,
    block_length: int,
    n_boot: int = 500,
    level: float = 0.95,
    rng: Optional[np.random.Generator] = None,
) -> BootstrapResult:
    """
    Moving-block bootstrap for dependent series.

    Parameters
    ----------
    stat_fn : Callable[[Array], float]
        Function mapping a (resampled) 1D series to a scalar statistic.
    data : Array
        1D array (n,).
    block_length : int
        Block length; typically ~ 5 * tau_mix.
    n_boot : int
        Number of bootstrap replicates.
    level : float
        Confidence level for (ci_low, ci_high).
    rng : Optional[np.random.Generator]
        RNG for reproducibility.

    Returns
    -------
    result : BootstrapResult
        Statistic and CI from bootstrap distribution.
    """
    if rng is None:
        rng = make_rng()

    if data.ndim != 1:
        raise ValueError("moving_block_bootstrap expects 1D data")

    n = len(data)
    n_blocks = int(np.ceil(n / block_length))

    logger.debug(f"Bootstrap: n={n}, block_length={block_length}, n_blocks={n_blocks}, n_boot={n_boot}")

    boot_stats = np.zeros(n_boot)

    for b in range(n_boot):
        # Sample blocks with replacement
        block_starts = rng.integers(0, n - block_length + 1, size=n_blocks)
        resampled = []

        for start in block_starts:
            resampled.append(data[start:start + block_length])

        resampled = np.concatenate(resampled)[:n]  # Trim to original length

        boot_stats[b] = stat_fn(resampled)

    # Compute statistic on original data
    stat = stat_fn(data)

    # Compute CI
    alpha = 1 - level
    ci_low = float(np.percentile(boot_stats, 100 * alpha / 2))
    ci_high = float(np.percentile(boot_stats, 100 * (1 - alpha / 2)))

    logger.debug(f"Bootstrap: stat={stat:.4f}, CI=[{ci_low:.4f}, {ci_high:.4f}]")

    return BootstrapResult(
        stat=float(stat),
        ci_low=ci_low,
        ci_high=ci_high,
        samples=boot_stats,
        level=level,
    )


# ---------------------- Local Linear Conditional Mean -------------------

@dataclass
class LocalLinearResult:
    A: Array          # shape (m, d)  (Jacobian / local linear map)
    b: Array          # shape (m,)    (intercept)
    mu: Array         # shape (m,)    (predicted mean at x0)
    Sigma: Array      # shape (m, m)  (local residual covariance)
    weights: Array    # shape (n,)    (normalized weights used)
    residuals: Array  # shape (n, m)  (weighted residuals y - (Ax+b))
    # Diagnostic fields for locality guard
    n_eff: float      # Effective sample size: (Σwᵢ)² / Σwᵢ²
    r_eff: float      # Effective radius: sqrt(Σwᵢ||Xᵢ-x₀||² / Σwᵢ)
    cond: float       # Condition number of design matrix
    # Extended diagnostics for weight debugging
    sum_w: float      # Sum of raw weights: Σwᵢ
    sum_w2: float     # Sum of squared raw weights: Σwᵢ²
    w_p10: float      # 10th percentile of raw weights
    w_p50: float      # 50th percentile (median) of raw weights
    w_p90: float      # 90th percentile of raw weights
    median_dist: float  # Median distance to x₀
    sse_const: float  # SSE for constant-only fit (no slope)
    sse_linear: float # SSE for local-linear fit (with slope)


def local_linear_mean(
    X: Array,
    Y: Array,
    x0: Array,
    *,
    h: float,
    weight: Literal["exp", "gaussian", "tricube"] = "exp",
    ridge: float = 0.0,
    min_pts: int = 20,
) -> LocalLinearResult:
    """
    Weighted local linear regression: Y ≈ A(X - x0) + b near x0.

    SCALE-INVARIANT DESIGN:
    -----------------------
    The local fit uses normalized coordinates Δ = (X - x0)/h to avoid kernel flattening
    at large h. We solve:
        min_{b, g} Σᵢ wᵢ(Yᵢ - b - gᵀΔᵢ)²
    where Δᵢ = (Xᵢ - x0)/h.

    Then return:
        - Predicted mean at x0: μ = b
        - Jacobian wrt original X: A = g/h

    This ensures ||A|| remains stable across h and δ² ∝ h^(2s) as theory predicts.

    Design choices
    --------------
    - `X` are covariates at time t (shape (n, d)), `Y` are responses at t+1 (shape (n, m)).
    - We center and scale by h to maintain scale invariance.
    - Weights:
        * "exp": w_i = exp(-||X_i - x0|| / h)
        * "gaussian": w_i = exp(-||X_i - x0||^2 / (2 h^2))
        * "tricube": w_i = (1 - (||X_i - x0||/h)^3)^3 for ||X_i - x0|| ≤ h, else 0
    - Ridge regularization stabilizes small neighborhoods.

    Parameters
    ----------
    X : Array
        Shape (n, d).
    Y : Array
        Shape (n, m).
    x0 : Array
        Shape (d,). Query point.
    h : float
        Locality scale / bandwidth.
    weight : {"exp","gaussian","tricube"}
        Weighting kernel. "tricube" has compact support (r_eff/h ~ 0.7-0.9).
    ridge : float
        Ridge term added to (Δ'WΔ).
    min_pts : int
        Require at least this many effective points (sum of weights) to fit.

    Returns
    -------
    res : LocalLinearResult
        Local linear map and summary statistics at x0.
        Note: A is the Jacobian wrt ORIGINAL coordinates X (not scaled Δ).
    """
    if Y.ndim == 1:
        Y = Y.reshape(-1, 1)

    n, d = X.shape
    m = Y.shape[1]

    # Center at x0
    X_centered = X - x0.reshape(1, -1)

    # SCALE-INVARIANT DESIGN: Use Δ = (X - x0)/h
    Delta = X_centered / h

    # Compute weights based on distances in ORIGINAL coordinates
    dists = np.linalg.norm(X_centered, axis=1)

    if weight == "exp":
        w = np.exp(-dists / h)
    elif weight == "gaussian":
        w = np.exp(-dists**2 / (2 * h**2))
    elif weight == "tricube":
        # Tricube kernel: w(u) = (1 - |u|^3)^3 for |u| ≤ 1, else 0
        # where u = ||X_i - x0|| / h
        u = dists / h
        w = np.where(u <= 1.0, (1 - u**3)**3, 0.0)
    else:
        raise ValueError(f"Unknown weight: {weight}")

    # Check effective sample size (raw weights)
    w_sum = w.sum()
    if w_sum < min_pts:
        logger.warning(f"Effective sample size (raw) {w_sum:.1f} < min_pts {min_pts}")

    # DO NOT NORMALIZE - use raw weights for WLS!
    # Normalization destroys h-dependence and causes ||A|| collapse

    # Weighted least squares: solve (Δ'WΔ + ridge*I) g = Δ'W Y
    # Use RAW weights (not normalized)
    W = np.diag(w)
    DtWD = Delta.T @ W @ Delta + ridge * np.eye(d)
    DtWY = Delta.T @ W @ Y

    try:
        g = np.linalg.solve(DtWD, DtWY)  # shape (d, m)
    except np.linalg.LinAlgError:
        logger.error("Singular matrix in local linear regression")
        g = np.zeros((d, m))

    # Intercept: b = weighted mean of (Y - gᵀΔ)
    # Normalize only for computing the mean
    w_normed = w / w_sum
    b = np.average(Y - Delta @ g, axis=0, weights=w_normed)  # shape (m,)

    # Predicted mean at x0 (where Δ = 0)
    mu = b

    # JACOBIAN WRT ORIGINAL X: A = g/h
    # Since Y ≈ b + gᵀΔ = b + gᵀ(X-x0)/h, we have ∂Y/∂X = g/h
    A = g / h

    # Residuals (using original formula with A and X_centered)
    residuals = Y - (X_centered @ A + b.reshape(1, -1))  # shape (n, m)

    # Weighted residual covariance (using raw weights)
    Sigma = (residuals.T @ W @ residuals) / w_sum + ridge * np.eye(m)

    # DIAGNOSTIC METRICS for locality guard
    # Use RAW weights (not normalized) for diagnostics
    # Effective sample size: n_eff = (Σwᵢ)² / Σwᵢ²
    n_eff = float(w_sum**2 / np.sum(w**2))

    # Effective radius: r_eff = sqrt(Σwᵢ||Xᵢ-x₀||² / Σwᵢ)
    r_eff = float(np.sqrt(np.sum(w * dists**2) / w_sum))

    # Condition number of design matrix
    cond = float(np.linalg.cond(DtWD))

    # EXTENDED DIAGNOSTICS for weight debugging
    sum_w = float(w_sum)
    sum_w2 = float(np.sum(w**2))
    w_p10 = float(np.percentile(w, 10))
    w_p50 = float(np.percentile(w, 50))
    w_p90 = float(np.percentile(w, 90))
    median_dist = float(np.median(dists))

    # SSE comparison: constant vs linear fit
    # Constant-only fit: Y ≈ b_const (weighted mean)
    b_const = np.average(Y, axis=0, weights=w_normed)
    resid_const = Y - b_const.reshape(1, -1)
    sse_const = float(np.sum(w[:, None] * resid_const**2))

    # Linear fit: Y ≈ A(X-x₀) + b (already computed)
    sse_linear = float(np.sum(w[:, None] * residuals**2))

    if m == 1:
        A = A.flatten()
        b = b.flatten()
        mu = mu.flatten()
        Sigma = Sigma.flatten()
        residuals = residuals.flatten()

    return LocalLinearResult(
        A=A,
        b=b,
        mu=mu,
        Sigma=Sigma,
        weights=w_normed,  # Return normalized weights for backward compatibility
        residuals=residuals,
        n_eff=n_eff,
        r_eff=r_eff,
        cond=cond,
        sum_w=sum_w,
        sum_w2=sum_w2,
        w_p10=w_p10,
        w_p50=w_p50,
        w_p90=w_p90,
        median_dist=median_dist,
        sse_const=sse_const,
        sse_linear=sse_linear,
    )


# ----------------------------- Plot Helpers -----------------------------

def plot_loglog_with_fit(
    ax,
    x: Array,
    y: Array,
    *,
    fit_range: Optional[Tuple[float, float]] = None,
    label: Optional[str] = None,
    ci: Optional[Tuple[Array, Array]] = None,
) -> Tuple[float, float]:
    """
    Log–log plot with a fitted slope (y ≈ c * x^s). Optionally overlay CI band.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        Target axes.
    x, y : Array
        Positive arrays of the same shape (n,).
    fit_range : Optional[Tuple[float,float]]
        Fit only within [xmin, xmax] in x (on original scale).
    label : Optional[str]
        Line label.
    ci : Optional[Tuple[Array, Array]]
        Lower/upper envelopes for y to draw as a band (same shape as y).

    Returns
    -------
    slope, intercept : float
        Least-squares slope and intercept in log10 space.
    """
    # Filter fit range
    if fit_range is not None:
        mask = (x >= fit_range[0]) & (x <= fit_range[1])
        x_fit = x[mask]
        y_fit = y[mask]
    else:
        x_fit = x
        y_fit = y

    # Log-log fit
    log_x = np.log10(x_fit)
    log_y = np.log10(y_fit)

    slope, intercept = np.polyfit(log_x, log_y, 1)

    # Plot data
    ax.loglog(x, y, 'o', markersize=4, alpha=0.7, label=label)

    # Plot fit line
    ax.loglog(x, 10**(intercept + slope * np.log10(x)), '--', linewidth=2,
              label=f'slope={slope:.2f}')

    # Plot CI band
    if ci is not None:
        ci_low, ci_high = ci
        ax.fill_between(x, ci_low, ci_high, alpha=0.2)

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.legend()
    ax.grid(True, alpha=0.3)

    return float(slope), float(intercept)


def plot_semilog_decay_with_fit(
    ax,
    t: Array,
    dvals: Array,
    *,
    fit_range: Optional[Tuple[int, int]] = None,
    label: Optional[str] = None,
) -> Tuple[float, float]:
    """
    Semi-log plot for divergence decay D(t) ≈ C * exp(-gamma * t).

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        Target axes.
    t : Array
        Time steps (n,).
    dvals : Array
        Divergence values (n,), positive.
    fit_range : Optional[Tuple[int,int]]
        Use t indices [i_start, i_end) to fit the slope.
    label : Optional[str]
        Line label.

    Returns
    -------
    slope, intercept : float
        Least-squares slope and intercept in ln space (slope ≈ -gamma).
    """
    # Filter fit range
    if fit_range is not None:
        t_fit = t[fit_range[0]:fit_range[1]]
        d_fit = dvals[fit_range[0]:fit_range[1]]
    else:
        t_fit = t
        d_fit = dvals

    # ln(D) vs t
    log_d = np.log(d_fit)

    slope, intercept = np.polyfit(t_fit, log_d, 1)

    # Plot data
    ax.semilogy(t, dvals, 'o', markersize=4, alpha=0.7, label=label)

    # Plot fit line
    ax.semilogy(t, np.exp(intercept + slope * t), '--', linewidth=2,
                label=f'decay rate={-slope:.4f}')

    ax.set_xlabel('Time t')
    ax.set_ylabel('Divergence D(t)')
    ax.legend()
    ax.grid(True, alpha=0.3)

    return float(slope), float(intercept)


# --------------------------- Misc Utilities -----------------------------

def zscore(x: Array, axis: int = 0, eps: float = 1e-12) -> Tuple[Array, Array, Array]:
    """
    Z-score normalize.

    Parameters
    ----------
    x : Array
        Data array.
    axis : int
        Axis along which to compute mean/std.
    eps : float
        Numerical floor to avoid division by zero.

    Returns
    -------
    xz : Array
        Z-scored data.
    mean : Array
        Means along axis.
    std : Array
        Stds along axis.
    """
    mean = x.mean(axis=axis, keepdims=True)
    std = x.std(axis=axis, keepdims=True) + eps

    xz = (x - mean) / std

    return xz, mean.squeeze(), std.squeeze()


def shared_bin_edges_1d(
    x: Array,
    y: Array,
    *,
    bins: int = 64,
    margin: float = 1e-9,
) -> Array:
    """
    Shared 1D histogram edges covering both x and y.

    Parameters
    ----------
    x, y : Array
        1D arrays.
    bins : int
        Number of bins.
    margin : float
        Small padding beyond min/max.

    Returns
    -------
    edges : Array
        Bin edges shape (bins+1,).
    """
    vmin = min(x.min(), y.min()) - margin
    vmax = max(x.max(), y.max()) + margin

    edges = np.linspace(vmin, vmax, bins + 1)
    return edges


def savefig(fig, path: str, dpi: int = 200, bbox_inches: str = "tight") -> None:
    """
    Save a matplotlib figure with standard settings.

    Parameters
    ----------
    fig : matplotlib.figure.Figure
    path : str
        Output path (e.g., "figures/tier1_learning.png").
    dpi : int
        Resolution.
    bbox_inches : str
        Matplotlib bbox_inches option.
    """
    from pathlib import Path
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(path, dpi=dpi, bbox_inches=bbox_inches)
    logger.info(f"Saved figure: {path}")


# ------------------------ Contracts for Tiers ---------------------------

@dataclass
class DivergenceCurve:
    x: Array       # grid values (e.g., n or h or t)
    y: Array       # divergence values
    slope: float   # fitted slope (log-log or semi-log)
    intercept: float


def fit_learning_curve(
    n_grid: Array,
    A_n: Array,
    *,
    n_eff: Optional[Array] = None,
    fit_range: Optional[Tuple[float, float]] = None,
) -> DivergenceCurve:
    """
    Fit learning curve slope on log–log scale:
        A(n) ≈ A_inf + C * n_eff^{-zeta}
    Here we fit the tail (A(n) - A_inf) versus n_eff to get slope ~ -zeta.

    Parameters
    ----------
    n_grid : Array
        Sample sizes tested.
    A_n : Array
        Divergence values per n (same length as n_grid).
    n_eff : Optional[Array]
        Effective sample sizes (n / tau_mix). If None, use n_grid.
    fit_range : Optional[Tuple[float,float]]
        Restrict fit to n in [nmin, nmax].

    Returns
    -------
    curve : DivergenceCurve
        With slope ≈ -zeta.
    """
    logger.info("=== Fitting learning curve ===")
    logger.info(f"n_grid: {n_grid}")
    logger.info(f"A_n: {A_n}")

    if n_eff is None:
        n_eff = n_grid
    logger.info(f"n_eff: {n_eff}")

    # Estimate A_inf as lower envelope of largest 2-3 n values
    # Use median of smallest 2-3 A_n values for stability
    n_for_envelope = min(3, len(A_n))
    smallest_indices = np.argsort(A_n)[:n_for_envelope]
    A_inf = np.median(A_n[smallest_indices])
    logger.info(f"A_inf (lower envelope of {n_for_envelope} smallest values): {A_inf:.6f}")
    logger.info(f"  (values used: {A_n[smallest_indices]})")

    # Residual with epsilon clipping to avoid log(0)
    epsilon = 1e-8  # Floor for numerical stability
    A_residual = np.maximum(A_n - A_inf, epsilon)
    logger.info(f"A_residual (clipped at {epsilon:.1e}): {A_residual}")

    # Filter out points where A_residual is too close to epsilon (would break log)
    # Keep only points where A_residual > 10 * epsilon (well above floor)
    valid_mask = A_residual > 10 * epsilon
    logger.info(f"Valid points (A_residual > {10 * epsilon:.2e}): {valid_mask.sum()}/{len(valid_mask)}")

    # Further filter by fit_range if specified
    if fit_range is not None:
        range_mask = (n_grid >= fit_range[0]) & (n_grid <= fit_range[1])
        mask = valid_mask & range_mask
        logger.info(f"Applying fit_range {fit_range}: {mask.sum()} points")
    else:
        mask = valid_mask
        logger.info(f"Using {mask.sum()} points for fit")

    n_fit = n_eff[mask]
    A_fit = A_residual[mask]

    # Log-log fit (A_fit already clipped at epsilon)
    log_n = np.log10(n_fit)
    log_A = np.log10(A_fit)

    logger.info(f"log10(n_eff): {log_n}")
    logger.info(f"log10(A_residual): {log_A}")

    slope, intercept = np.polyfit(log_n, log_A, 1)

    logger.info(f"Fitted slope (in log-log): {slope:.6f}")
    logger.info(f"Fitted intercept (in log-log): {intercept:.6f}")
    logger.info(f"Interpretation: A_residual ~ n_eff^{slope:.3f}")
    logger.info(f"Therefore: zeta ≈ {-slope:.3f} (negative of slope)")
    logger.info("=== End learning curve fit ===")

    return DivergenceCurve(
        x=n_grid,
        y=A_n,
        slope=slope,
        intercept=intercept,
    )


def fit_locality_curve(
    h_grid: Array,
    A_h: Array,
    *,
    fit_range: Optional[Tuple[float, float]] = None,
) -> DivergenceCurve:
    """
    Fit locality curve slope on log–log scale:
        A(h) ≈ A_0 + C * h^{eta}
    Here we fit the tail (A(h) - A_0) versus h to get slope ~ eta.

    Parameters
    ----------
    h_grid : Array
        Bandwidths tested.
    A_h : Array
        Divergence values per h.

    Returns
    -------
    curve : DivergenceCurve
        With slope ≈ eta.
    """
    logger.info("=== Fitting locality curve ===")
    logger.info(f"h_grid: {h_grid}")
    logger.info(f"A_h: {A_h}")

    # Estimate A_0 as lower envelope of smallest 2-3 A_h values
    # Use median for stability (avoids single outlier affecting fit)
    n_for_envelope = min(3, len(A_h))
    smallest_indices = np.argsort(A_h)[:n_for_envelope]
    A_0 = np.median(A_h[smallest_indices])
    logger.info(f"A_0 (lower envelope of {n_for_envelope} smallest values): {A_0:.6f}")
    logger.info(f"  (values used: {A_h[smallest_indices]})")

    # Residual with epsilon clipping to avoid log(0)
    epsilon = 1e-8  # Floor for numerical stability
    A_residual = np.maximum(A_h - A_0, epsilon)
    logger.info(f"A_residual (clipped at {epsilon:.1e}): {A_residual}")

    # Filter out points where A_residual is too close to epsilon (would break log)
    # Keep only points where A_residual > 10 * epsilon (well above floor)
    valid_mask = A_residual > 10 * epsilon
    logger.info(f"Valid points (A_residual > {10 * epsilon:.2e}): {valid_mask.sum()}/{len(valid_mask)}")

    # Further filter by fit_range if specified
    if fit_range is not None:
        range_mask = (h_grid >= fit_range[0]) & (h_grid <= fit_range[1])
        mask = valid_mask & range_mask
        logger.info(f"Applying fit_range {fit_range}: {mask.sum()} points")
    else:
        mask = valid_mask
        logger.info(f"Using {mask.sum()} points for fit")

    h_fit = h_grid[mask]
    A_fit = A_residual[mask]

    # Log-log fit (A_fit already clipped at epsilon)
    log_h = np.log10(h_fit)
    log_A = np.log10(A_fit)

    logger.info(f"log10(h_grid): {log_h}")
    logger.info(f"log10(A_residual): {log_A}")

    slope, intercept = np.polyfit(log_h, log_A, 1)

    logger.info(f"Fitted slope (in log-log): {slope:.6f}")
    logger.info(f"Fitted intercept (in log-log): {intercept:.6f}")
    logger.info(f"Interpretation: A_residual ~ h^{slope:.3f}")
    logger.info(f"Therefore: eta ≈ {slope:.3f}")
    logger.info("=== End locality curve fit ===")

    return DivergenceCurve(
        x=h_grid,
        y=A_h,
        slope=slope,
        intercept=intercept,
    )

