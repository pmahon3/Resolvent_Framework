"""
Divergence-based stochastic reconstruction for delay-embedded time series.

Paper III: "Divergence-Based Noise Estimation for Delay-Reconstructed
Dynamical Systems"

Core components:
  - delay_embed: form delay vectors from scalar time series
  - local_pushforward: compute A(z), σ(z), div(z) at a query point
  - map_attractor: sweep local_pushforward over the reconstructed attractor
  - embedding_diagnostic: dimension sweep to find sufficient embedding
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Literal, Optional

import numpy as np
import numpy.typing as npt
from scipy.spatial import KDTree

Array = npt.NDArray[np.float64]


# =========================================================================
# §1. Delay embedding
# =========================================================================

def delay_embed(y: Array, d: int, L: int) -> Array:
    """Form delay vectors from a scalar time series.

    Parameters
    ----------
    y : Array, shape (N,)
        Scalar time series.
    d : int
        Embedding dimension.
    L : int
        Lag (delay step).

    Returns
    -------
    Z : Array, shape (N - (d-1)*L, d)
        Delay vectors z_t = (y_t, y_{t-L}, ..., y_{t-(d-1)*L}).
    """
    N = len(y)
    n = N - (d - 1) * L
    if n <= 0:
        raise ValueError(f"Time series too short: N={N}, d={d}, L={L}")
    Z = np.column_stack([y[(d - 1) * L - k * L: N - k * L] for k in range(d)])
    return Z


# =========================================================================
# §2. Local linear pushforward
# =========================================================================

@dataclass
class LocalPushforward:
    """Result of local linear fit at a query point z."""
    z: Array            # shape (d,) — query point
    A: Array            # shape (d, d) — local Jacobian
    b: Array            # shape (d,) — local intercept
    sigma: float        # scalar — local noise amplitude (RMS residual)
    div: float          # scalar — divergence tr(A)
    Sigma: Array        # shape (d, d) — full residual covariance
    n_eff: float        # effective sample size
    r_eff: float        # effective radius
    cond: float         # condition number of design matrix


def tricube_weights(dists: Array, h: float) -> Array:
    """Tricube kernel: w(u) = (1 - u³)³ for u ≤ 1, else 0."""
    u = dists / h
    return np.where(u <= 1.0, (1.0 - u ** 3) ** 3, 0.0)


def local_pushforward(
    Z: Array,
    Z_next: Array,
    z0: Array,
    *,
    h: float,
    ridge: float = 1e-8,
    min_pts: int = 20,
) -> Optional[LocalPushforward]:
    """Compute the local linearized pushforward at z0.

    Fits z_{t+1} ≈ A · (z_t - z0) + b near z0 using tricube-weighted
    least squares.

    Parameters
    ----------
    Z : Array, shape (n, d)
        Delay vectors at time t.
    Z_next : Array, shape (n, d)
        Delay vectors at time t+1.
    z0 : Array, shape (d,)
        Query point.
    h : float
        Bandwidth (kernel radius).
    ridge : float
        Ridge regularization.
    min_pts : int
        Minimum effective sample size.

    Returns
    -------
    result : LocalPushforward or None
        None if insufficient data in the neighbourhood.
    """
    n, d = Z.shape

    # Centre at z0
    Delta = Z - z0.reshape(1, -1)
    dists = np.linalg.norm(Delta, axis=1)

    # Tricube weights
    w = tricube_weights(dists, h)
    w_sum = w.sum()

    if w_sum < min_pts:
        return None

    # Scale-invariant design: Δ_scaled = Δ / h
    Delta_scaled = Delta / h

    # Weighted least squares: (Δ'WΔ + ridge·I) g = Δ'W Y
    W = np.diag(w)
    DtWD = Delta_scaled.T @ W @ Delta_scaled + ridge * np.eye(d)
    DtWY = Delta_scaled.T @ W @ Z_next

    try:
        g = np.linalg.solve(DtWD, DtWY)  # shape (d, d)
    except np.linalg.LinAlgError:
        return None

    # Intercept
    w_normed = w / w_sum
    b_vec = np.average(Z_next - Delta_scaled @ g, axis=0, weights=w_normed)

    # Jacobian in original coordinates: A = g / h
    A = g.T / h  # shape (d, d)

    # Residuals
    predicted = Delta @ A.T + b_vec.reshape(1, -1)
    residuals = Z_next - predicted

    # Weighted residual covariance
    Sigma = (residuals.T @ W @ residuals) / w_sum

    # Divergence
    div_val = np.trace(A)

    # Noise amplitude: RMS of residuals per dimension
    sigma_val = np.sqrt(np.trace(Sigma) / d)

    # Diagnostics
    n_eff = float(w_sum ** 2 / np.sum(w ** 2))
    r_eff = float(np.sqrt(np.sum(w * dists ** 2) / w_sum))
    cond_val = float(np.linalg.cond(DtWD))

    return LocalPushforward(
        z=z0, A=A, b=b_vec, sigma=sigma_val, div=div_val,
        Sigma=Sigma, n_eff=n_eff, r_eff=r_eff, cond=cond_val,
    )


# =========================================================================
# §3. Attractor mapping
# =========================================================================

def map_attractor(
    Z: Array,
    Z_next: Array,
    *,
    h: float,
    n_query: int = 1000,
    ridge: float = 1e-8,
    min_pts: int = 20,
    seed: Optional[int] = None,
) -> list[LocalPushforward]:
    """Sweep local_pushforward over the reconstructed attractor.

    Parameters
    ----------
    Z : Array, shape (n, d)
        Delay vectors at time t.
    Z_next : Array, shape (n, d)
        Delay vectors at time t+1.
    h : float
        Bandwidth.
    n_query : int
        Number of query points to sample.
    seed : int, optional
        Random seed for reproducibility.

    Returns
    -------
    results : list of LocalPushforward
        One per successful query point.
    """
    rng = np.random.default_rng(seed)
    n = len(Z)
    idx = rng.choice(n, size=min(n_query, n), replace=False)

    results = []
    for i in idx:
        res = local_pushforward(Z, Z_next, Z[i], h=h, ridge=ridge,
                                min_pts=min_pts)
        if res is not None:
            results.append(res)

    return results


# =========================================================================
# §4. Test systems
# =========================================================================

def lorenz63(N: int, dt: float = 0.01, transient: int = 5000,
             sigma: float = 10.0, rho: float = 28.0, beta: float = 8/3,
             noise: float = 0.0, seed: Optional[int] = None) -> Array:
    """Generate Lorenz-63 trajectory.

    Returns shape (N, 3) array after discarding transient.
    """
    rng = np.random.default_rng(seed)
    total = N + transient
    x = np.zeros((total, 3))
    x[0] = [1.0, 1.0, 1.0]

    for t in range(total - 1):
        dx = sigma * (x[t, 1] - x[t, 0])
        dy = x[t, 0] * (rho - x[t, 2]) - x[t, 1]
        dz = x[t, 0] * x[t, 1] - beta * x[t, 2]
        x[t + 1] = x[t] + dt * np.array([dx, dy, dz])
        if noise > 0:
            x[t + 1] += noise * np.sqrt(dt) * rng.standard_normal(3)

    return x[transient:]


def rossler(N: int, dt: float = 0.01, transient: int = 5000,
            a: float = 0.2, b: float = 0.2, c: float = 5.7,
            noise: float = 0.0, seed: Optional[int] = None) -> Array:
    """Generate Rössler trajectory.

    Returns shape (N, 3) array after discarding transient.
    """
    rng = np.random.default_rng(seed)
    total = N + transient
    x = np.zeros((total, 3))
    x[0] = [1.0, 1.0, 1.0]

    for t in range(total - 1):
        dx = -x[t, 1] - x[t, 2]
        dy = x[t, 0] + a * x[t, 1]
        dz = b + x[t, 2] * (x[t, 0] - c)
        x[t + 1] = x[t] + dt * np.array([dx, dy, dz])
        if noise > 0:
            x[t + 1] += noise * np.sqrt(dt) * rng.standard_normal(3)

    return x[transient:]


def logistic_map(N: int, r: float = 3.9, noise: float = 0.0,
                 seed: Optional[int] = None) -> Array:
    """Generate logistic map time series: x_{t+1} = r·x_t·(1-x_t) + noise."""
    rng = np.random.default_rng(seed)
    x = np.zeros(N)
    x[0] = 0.4
    for t in range(N - 1):
        x[t + 1] = r * x[t] * (1 - x[t])
        if noise > 0:
            x[t + 1] += noise * rng.standard_normal()
    return x


# =========================================================================
# §5. Embedding diagnostic: dimension sweep
# =========================================================================

def dimension_sweep(
    y: Array,
    L: int,
    d_range: range,
    h: float,
    n_query: int = 500,
    seed: Optional[int] = None,
) -> dict:
    """Sweep embedding dimension and track σ, div, and their stability.

    Parameters
    ----------
    y : Array, shape (N,)
        Scalar time series.
    L : int
        Lag.
    d_range : range
        Range of embedding dimensions to test.
    h : float
        Bandwidth for local linear fit.
    n_query : int
        Query points per dimension.
    seed : int, optional
        Random seed.

    Returns
    -------
    results : dict with keys 'd', 'mean_sigma', 'std_sigma',
              'mean_div', 'std_div', 'n_success'
    """
    out = {'d': [], 'mean_sigma': [], 'std_sigma': [],
           'mean_div': [], 'std_div': [], 'n_success': []}

    for d in d_range:
        Z = delay_embed(y, d, L)
        Z_t = Z[:-1]
        Z_next = Z[1:]

        results = map_attractor(Z_t, Z_next, h=h, n_query=n_query,
                                seed=seed)

        if len(results) < 10:
            out['d'].append(d)
            out['mean_sigma'].append(np.nan)
            out['std_sigma'].append(np.nan)
            out['mean_div'].append(np.nan)
            out['std_div'].append(np.nan)
            out['n_success'].append(len(results))
            continue

        sigmas = np.array([r.sigma for r in results])
        divs = np.array([r.div for r in results])

        out['d'].append(d)
        out['mean_sigma'].append(np.mean(sigmas))
        out['std_sigma'].append(np.std(sigmas))
        out['mean_div'].append(np.mean(divs))
        out['std_div'].append(np.std(divs))
        out['n_success'].append(len(results))

    return {k: np.array(v) for k, v in out.items()}
