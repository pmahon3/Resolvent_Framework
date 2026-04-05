"""
Plot η(u) overlay: empirical estimates vs theoretical transition curve.
"""
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from typing import List, Dict, Optional

from src.analysis.eta_theory import eta_theory_curve, get_theory_bands


def plot_eta_u_overlay(
    bin_results: List[Dict],
    q: float,
    p: float = 2.0,
    u_max: float = 5.0,
    output_path: Optional[Path] = None,
    show: bool = False
):
    """
    Plot empirical η̂(u) vs theoretical η_theory(u) curve.

    Parameters
    ----------
    bin_results : list of dicts
        Per-bin results with keys: u_rep, eta, eta_ci (optional), passed_guards
    q : float
        Drift exponent
    p : float
        Theory transition sharpness (default: 2.0)
    u_max : float
        Maximum u for plotting
    output_path : Path, optional
        Where to save figure
    show : bool
        Whether to show figure interactively
    """
    fig, ax = plt.subplots(figsize=(8, 5))

    # 1. Theory curve
    u_grid = np.linspace(0, u_max, 500)
    eta_theory = eta_theory_curve(u_grid, q, p)
    ax.plot(u_grid, eta_theory, 'k-', linewidth=2.5, label=r'$\eta_{\mathrm{theory}}(u)$', zorder=10)

    # 2. Theory bands
    bands = get_theory_bands(q)
    cusp_band = bands['cusp']
    interior_band = bands['interior']

    # Cusp region (u ≤ 0.7)
    ax.axvspan(cusp_band['u_range'][0], cusp_band['u_range'][1],
               alpha=0.12, color='blue', label='Cusp band', zorder=1)
    ax.axhline(cusp_band['eta_range'][0], color='blue', linestyle=':', alpha=0.4, linewidth=1)
    ax.axhline(cusp_band['eta_range'][1], color='blue', linestyle=':', alpha=0.4, linewidth=1)

    # Interior region (u ≥ 2.0)
    ax.axvspan(interior_band['u_range'][0], u_max,
               alpha=0.12, color='green', label='Interior band', zorder=1)
    ax.axhline(interior_band['eta_range'][0], color='green', linestyle=':', alpha=0.4, linewidth=1)
    ax.axhline(interior_band['eta_range'][1], color='green', linestyle=':', alpha=0.4, linewidth=1)

    # Crossover marker
    ax.axvline(1.0, color='gray', linestyle='--', alpha=0.5, linewidth=1, label=r'$u=1$ (crossover)')

    # 3. Empirical points
    eta_values = []
    for b in bin_results:
        if 'u_rep' not in b or 'eta' not in b:
            continue

        u_rep = b['u_rep']
        eta_hat = b['eta']
        passed = b.get('passed_guards', True)
        eta_values.append(eta_hat)

        # Style based on guard status
        marker = 'o' if passed else 's'
        facecolor = 'C3' if passed else 'none'
        edgecolor = 'C3' if passed else 'C1'
        markersize = 50 if passed else 40
        label_str = 'Empirical (passed)' if passed else 'Empirical (failed guards)'

        ax.scatter(u_rep, eta_hat, s=markersize, marker=marker,
                  facecolors=facecolor, edgecolors=edgecolor,
                  linewidths=1.5, zorder=20, alpha=0.9)

        # CIs if available
        ci = b.get('eta_ci')
        if ci and 'lo' in ci and 'hi' in ci:
            ax.vlines(u_rep, ci['lo'], ci['hi'], colors=edgecolor, linewidth=2, alpha=0.7, zorder=15)

    # 4. Formatting
    ax.set_xlabel(r'$u = |y_0|/h$ (scaled distance to cusp)', fontsize=12, fontweight='bold')
    ax.set_ylabel(r'$\eta$ (bias-scaling exponent)', fontsize=12, fontweight='bold')
    ax.set_title(r'Locality-scaling transition: $\hat\eta(u)$ vs theory', fontsize=13, fontweight='bold')
    ax.set_xlim(0, u_max)

    # Adaptive y-axis: include all empirical data plus theory curve
    if eta_values:
        y_min = min(min(eta_values) - 0.5, 1.5)
        y_max = max(max(eta_values) + 0.5, 5.0)
    else:
        y_min, y_max = 1.5, 5.0
    ax.set_ylim(y_min, y_max)
    ax.grid(True, alpha=0.3, linestyle=':')

    # Legend (avoid duplicates)
    handles, labels = ax.get_legend_handles_labels()
    by_label = dict(zip(labels, handles))
    ax.legend(by_label.values(), by_label.keys(), loc='lower right', fontsize=9, framealpha=0.95)

    plt.tight_layout()

    if output_path:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        fig.savefig(output_path, dpi=150, bbox_inches='tight')
        print(f"Saved η(u) overlay to {output_path}")

    if show:
        plt.show()
    else:
        plt.close(fig)

    return fig, ax
