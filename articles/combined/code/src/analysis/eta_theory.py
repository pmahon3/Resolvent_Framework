"""
Theoretical η(u) transition curve for locality-scaling analysis.

The curve captures the transition from cusp-dominated (η=2q) to
interior-dominated (η=4) smoothness as a function of scaled distance u = |y₀|/h.
"""
import numpy as np
from typing import Dict, Tuple


def eta_theory_curve(u: np.ndarray, q: float, p: float = 2.0) -> np.ndarray:
    """
    Theoretical η(u) transition curve.

    η_theory(u) = 2q + (4 - 2q) * u^p / (1 + u^p)

    Parameters
    ----------
    u : array
        Scaled distance |y₀|/h
    q : float
        Drift exponent (m(y) = sign(y)|y|^q)
    p : float
        Transition sharpness parameter (default: 2.0)
        p ∈ [1.5, 3] controls steepness of cusp→interior transition

    Returns
    -------
    eta : array
        Theoretical exponent values
    """
    eta_cusp = 2 * q  # Near cusp: smoothness s = q
    eta_interior = 4.0  # Interior: smoothness s = 2

    transition = u**p / (1 + u**p)
    eta = eta_cusp + (eta_interior - eta_cusp) * transition

    return eta


def get_theory_bands(q: float) -> Dict[str, Tuple[float, float, float, float]]:
    """
    Get acceptance bands for cusp and interior regions.

    Parameters
    ----------
    q : float
        Drift exponent

    Returns
    -------
    bands : dict
        'cusp': (u_min, u_max, eta_min, eta_max) for cusp region
        'interior': (u_min, u_max, eta_min, eta_max) for interior region
    """
    eta_cusp = 2 * q
    tolerance = 0.3

    bands = {
        'cusp': {
            'u_range': (0.0, 0.7),
            'eta_range': (eta_cusp - tolerance, eta_cusp + tolerance)
        },
        'interior': {
            'u_range': (2.0, np.inf),
            'eta_range': (3.4, 4.0)
        }
    }

    return bands


def plot_theory_curve_with_bands(ax, q: float, p: float = 2.0,
                                  u_max: float = 5.0, n_points: int = 200):
    """
    Plot theoretical η(u) curve with acceptance bands on given axis.

    Parameters
    ----------
    ax : matplotlib axis
        Axis to plot on
    q : float
        Drift exponent
    p : float
        Transition sharpness
    u_max : float
        Maximum u value for plotting
    n_points : int
        Number of points for smooth curve
    """
    import matplotlib.pyplot as plt

    # Generate smooth curve
    u_dense = np.linspace(0, u_max, n_points)
    eta_dense = eta_theory_curve(u_dense, q, p)

    # Plot theory curve
    ax.plot(u_dense, eta_dense, 'k-', linewidth=2, label='Theory: η(u)', zorder=10)

    # Get bands
    bands = get_theory_bands(q)

    # Cusp band (u ≤ 0.7)
    cusp_u = bands['cusp']['u_range']
    cusp_eta = bands['cusp']['eta_range']
    ax.axvspan(cusp_u[0], cusp_u[1],
               ymin=(cusp_eta[0] - 1.5) / (5.5 - 1.5),
               ymax=(cusp_eta[1] - 1.5) / (5.5 - 1.5),
               alpha=0.15, color='blue', label='Cusp band')
    ax.hlines([cusp_eta[0], cusp_eta[1]], cusp_u[0], cusp_u[1],
              colors='blue', linestyles='dashed', alpha=0.5, linewidth=1)

    # Interior band (u ≥ 2.0)
    interior_u = bands['interior']['u_range']
    interior_eta = bands['interior']['eta_range']
    ax.axvspan(interior_u[0], u_max,
               ymin=(interior_eta[0] - 1.5) / (5.5 - 1.5),
               ymax=(interior_eta[1] - 1.5) / (5.5 - 1.5),
               alpha=0.15, color='green', label='Interior band')
    ax.hlines([interior_eta[0], interior_eta[1]], interior_u[0], u_max,
              colors='green', linestyles='dashed', alpha=0.5, linewidth=1)

    # Formatting
    ax.set_xlabel('u = |y₀|/h (scaled distance to cusp)', fontsize=11)
    ax.set_ylabel('η (bias-scaling exponent)', fontsize=11)
    ax.set_xlim(0, u_max)
    ax.set_ylim(1.5, 5.5)
    ax.grid(True, alpha=0.3)
    ax.legend(loc='upper left', fontsize=9)

    return ax
