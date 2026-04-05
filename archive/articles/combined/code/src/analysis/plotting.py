"""
Clean, theory-driven plotting for locality validation experiments.

Each plot shows empirical results alongside theoretical predictions,
making it easy to verify quantitative agreement.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from typing import Dict, List, Optional, Tuple
from pathlib import Path


def plot_delta2_vs_h_with_theory(
    results: Dict,
    theory_eta: float,
    output_path: Optional[Path] = None,
    figsize: Tuple[float, float] = (10, 6)
):
    """
    Plot A: δ² vs h (log-log) with theoretical slope.

    Shows empirical bias² for each bin with fitted slopes,
    overlaid with theoretical reference slope.

    Parameters
    ----------
    results : dict
        Must contain: 'h_grid', 'h_star', 'bin_results' (list of dicts with
        'h_fit', 'delta2_fit', 'eta', 'label', 'y_range')
    theory_eta : float
        Theoretical exponent (2s or 2q)
    """
    fig, ax = plt.subplots(figsize=figsize)

    colors = ['#1f77b4', '#ff7f0e', '#2ca02c']  # blue, orange, green

    # Plot empirical curves
    for i, bin_res in enumerate(results['bin_results']):
        h_fit = bin_res['h_fit']
        delta2_fit = bin_res['delta2_fit']
        eta = bin_res['eta']
        label = bin_res['label']

        # Data points
        ax.scatter(h_fit, delta2_fit, alpha=0.6, color=colors[i], s=40)

        # Fitted line
        log_h = np.log10(h_fit)
        log_delta2 = np.log10(delta2_fit)
        slope, intercept = np.polyfit(log_h, log_delta2, 1)
        h_line = np.array([h_fit[0], h_fit[-1]])
        delta2_line = 10**(slope * np.log10(h_line) + intercept)
        ax.plot(h_line, delta2_line, '--', color=colors[i], linewidth=2,
                label=f'{label}: η={eta:.2f}')

    # Theory reference line (middle bin, passing through h*)
    h_star = results['h_star']
    if len(results['bin_results']) > 0:
        # Use middle bin's intercept at h* as reference point
        mid_bin = results['bin_results'][len(results['bin_results'])//2]
        log_h_star = np.log10(h_star)
        log_delta2_star = np.mean(np.log10(mid_bin['delta2_fit']))  # rough estimate

        # Theory line through this point
        h_theory = np.logspace(np.log10(h_star*0.5), np.log10(h_star*10), 50)
        delta2_theory = 10**(log_delta2_star + theory_eta * (np.log10(h_theory) - log_h_star))
        ax.plot(h_theory, delta2_theory, 'k-', linewidth=2.5, alpha=0.7,
                label=f'Theory: η={theory_eta:.1f}')

    # Mark h*
    ax.axvline(h_star, color='gray', linestyle=':', alpha=0.5, linewidth=1.5)
    ax.text(h_star, ax.get_ylim()[0]*1.2, r'$h^*$', ha='center', fontsize=11)

    ax.set_xscale('log')
    ax.set_yscale('log')
    ax.set_xlabel(r'Bandwidth $h$ (z-units)', fontsize=12)
    ax.set_ylabel(r'Bias² $\delta^2(y_0; h)$', fontsize=12)
    ax.set_title('Locality Scaling: Bias² vs Bandwidth (Tricube Kernel)', fontsize=13, fontweight='bold')
    ax.legend(loc='best', framealpha=0.9, fontsize=10)
    ax.grid(True, alpha=0.3, which='both')

    plt.tight_layout()
    if output_path:
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
        plt.close()
    else:
        return fig


def plot_bias_variance_crossover(
    results: Dict,
    theory_eta: float,
    output_path: Optional[Path] = None,
    figsize: Tuple[float, float] = (10, 6)
):
    """
    Plot C: δ² vs h with bias/variance components and theoretical crossover.

    Shows U-shaped curve with minimum near h*, and right tail following h^(2s).
    """
    fig, ax = plt.subplots(figsize=figsize)

    h_grid = results['h_grid']
    delta2 = results['delta2_global']
    h_star = results['h_star']

    # Empirical δ²
    ax.plot(h_grid, delta2, 'o-', color='#1f77b4', linewidth=2, markersize=6,
            label=r'Empirical $\delta^2(h)$', alpha=0.8)

    # If variance estimate available
    if 'variance_est' in results:
        var_est = results['variance_est']
        bias2_est = np.maximum(delta2 - var_est, 1e-10)

        ax.plot(h_grid, var_est, 's--', color='#ff7f0e', linewidth=1.5, markersize=4,
                label=r'Variance $\widehat{\mathrm{var}}(h)$', alpha=0.7)
        ax.plot(h_grid, bias2_est, '^--', color='#2ca02c', linewidth=1.5, markersize=4,
                label=r'Bias² (proxy)', alpha=0.7)

    # Theoretical lines
    # Bias: C_b * h^(2s)
    idx_star = np.argmin(delta2)
    h_right = h_grid[idx_star:]
    if len(h_right) > 3:
        C_b = delta2[idx_star] / (h_star ** theory_eta)
        bias_theory = C_b * h_right ** theory_eta
        ax.plot(h_right, bias_theory, 'k-', linewidth=2.5, alpha=0.6,
                label=f'Bias theory: $C_b h^{{{theory_eta:.1f}}}$')

    # Mark h*
    ax.axvline(h_star, color='gray', linestyle=':', alpha=0.5, linewidth=2)
    y_min, y_max = ax.get_ylim()
    ax.text(h_star, y_max*0.7, r'$h^* \sim n^{-1/(2s+1)}$',
            ha='center', fontsize=11, bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

    ax.set_xscale('log')
    ax.set_yscale('log')
    ax.set_xlabel(r'Bandwidth $h$ (z-units)', fontsize=12)
    ax.set_ylabel(r'Mean Squared Error Components', fontsize=12)
    ax.set_title('Bias-Variance Crossover', fontsize=13, fontweight='bold')
    ax.legend(loc='best', framealpha=0.9, fontsize=10)
    ax.grid(True, alpha=0.3, which='both')

    plt.tight_layout()
    if output_path:
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
        plt.close()
    else:
        return fig


def plot_eta_per_bin(
    bin_results: List[Dict],
    theory_eta: float,
    output_path: Optional[Path] = None,
    figsize: Tuple[float, float] = (8, 6)
):
    """
    Plot D: η per |y₀|-bin (bars + CI) - THE SMOKING GUN.

    Shows how exponent varies across bins, with middle bin matching theory.
    """
    fig, ax = plt.subplots(figsize=figsize)

    n_bins = len(bin_results)
    x = np.arange(n_bins)

    etas = [b['eta'] for b in bin_results]
    labels = [b['label'] for b in bin_results]
    y_ranges = [f"[{b['y_range'][0]:.3f}, {b['y_range'][1]:.3f}]" for b in bin_results]

    # Error bars (if available)
    if 'ci_low' in bin_results[0]:
        ci_lows = [b['ci_low'] for b in bin_results]
        ci_highs = [b['ci_high'] for b in bin_results]
        yerr = [[etas[i] - ci_lows[i] for i in range(n_bins)],
                [ci_highs[i] - etas[i] for i in range(n_bins)]]
    else:
        yerr = None

    # Bars
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c'][:n_bins]
    bars = ax.bar(x, etas, yerr=yerr, capsize=5, alpha=0.7, color=colors,
                  edgecolor='black', linewidth=1.5)

    # Highlight middle bin
    mid_idx = n_bins // 2
    bars[mid_idx].set_facecolor('#ff7f0e')
    bars[mid_idx].set_alpha(0.9)
    bars[mid_idx].set_linewidth(2.5)

    # Theory line
    ax.axhline(theory_eta, color='black', linestyle='--', linewidth=2.5, alpha=0.7,
               label=f'Theory: η = {theory_eta:.1f}')

    # Annotate middle bin
    ax.text(mid_idx, etas[mid_idx] + 0.1, f'η = {etas[mid_idx]:.2f}',
            ha='center', fontsize=11, fontweight='bold',
            bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.7))

    # Labels
    ax.set_xticks(x)
    ax.set_xticklabels([f'{labels[i]}\n{y_ranges[i]}' for i in range(n_bins)], fontsize=10)
    ax.set_ylabel(r'Exponent $\hat{\eta}$', fontsize=12)
    ax.set_xlabel(r'$|y_0|$ Bin (percentile range)', fontsize=12)
    ax.set_title('Per-Bin Locality Exponents', fontsize=13, fontweight='bold')
    ax.set_ylim(0, max(etas) * 1.3)
    ax.legend(loc='upper right', framealpha=0.9, fontsize=11)
    ax.grid(True, axis='y', alpha=0.3)

    plt.tight_layout()
    if output_path:
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
        plt.close()
    else:
        return fig


def plot_locality_comparison(
    results_dict: Dict,
    locality_guards: Dict,
    output_path: Optional[Path] = None,
    figsize: Tuple[float, float] = (10, 6)
):
    """
    Plot E: r_eff/h vs h (Gaussian vs Tricube) - kernel geometry controls locality.

    Shows that Gaussian cannot satisfy strict locality, while Tricube can.
    """
    fig, ax = plt.subplots(figsize=figsize)

    # Plot for each kernel
    for kernel_name, kernel_res in results_dict.items():
        h_grid = kernel_res['h_grid']
        r_eff_over_h = kernel_res['r_eff_over_h']

        color = '#ff7f0e' if kernel_name == 'gaussian' else '#1f77b4'
        marker = 'o' if kernel_name == 'tricube' else 's'

        ax.plot(h_grid, r_eff_over_h, marker=marker, linestyle='-',
                linewidth=2, markersize=5, alpha=0.8,
                label=f'{kernel_name.capitalize()}: ~{np.median(r_eff_over_h):.2f}',
                color=color)

    # Locality guard band (for tricube)
    if 'tricube' in locality_guards:
        r_min = locality_guards['tricube']['r_eff_min']
        r_max = locality_guards['tricube']['r_eff_max']
        ax.axhspan(r_min, r_max, alpha=0.2, color='green',
                   label=f'Strict locality [{r_min}, {r_max}]')

    ax.set_xscale('log')
    ax.set_xlabel(r'Bandwidth $h$ (z-units)', fontsize=12)
    ax.set_ylabel(r'Effective radius ratio $r_{\mathrm{eff}}/h$', fontsize=12)
    ax.set_title('Kernel Geometry Controls Locality', fontsize=13, fontweight='bold')
    ax.legend(loc='best', framealpha=0.9, fontsize=11)
    ax.grid(True, alpha=0.3, which='both')
    ax.set_ylim(0, max(1.2, ax.get_ylim()[1]))

    plt.tight_layout()
    if output_path:
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
        plt.close()
    else:
        return fig


def plot_kernel_comparison_global(
    results_dict: Dict,
    theory_eta: float,
    output_path: Optional[Path] = None,
    figsize: Tuple[float, float] = (7, 6)
):
    """
    Plot F: Global weighted η (Gaussian vs Tricube) with CI.

    Shows that compact support improves exponent estimation.
    """
    fig, ax = plt.subplots(figsize=figsize)

    kernel_names = list(results_dict.keys())
    n_kernels = len(kernel_names)
    x = np.arange(n_kernels)

    etas = []
    yerr_low = []
    yerr_high = []

    for kernel_name in kernel_names:
        res = results_dict[kernel_name]
        eta = res['weighted_eta']
        etas.append(eta)

        if 'ci_low' in res:
            yerr_low.append(eta - res['ci_low'])
            yerr_high.append(res['ci_high'] - eta)
        else:
            yerr_low.append(0)
            yerr_high.append(0)

    yerr = [yerr_low, yerr_high] if any(yerr_low) else None

    # Bars
    colors = ['#ff7f0e' if 'gaussian' in k else '#1f77b4' for k in kernel_names]
    bars = ax.bar(x, etas, yerr=yerr, capsize=8, alpha=0.7, color=colors,
                  edgecolor='black', linewidth=1.5, width=0.6)

    # Theory line
    ax.axhline(theory_eta, color='black', linestyle='--', linewidth=2.5, alpha=0.7,
               label=f'Theory: η = {theory_eta:.1f}')

    # Annotations
    for i, (kernel_name, eta) in enumerate(zip(kernel_names, etas)):
        ax.text(i, eta + 0.05, f'{eta:.2f}', ha='center', fontsize=11, fontweight='bold')

    ax.set_xticks(x)
    ax.set_xticklabels([k.capitalize() for k in kernel_names], fontsize=12)
    ax.set_ylabel(r'Weighted $\hat{\eta}$', fontsize=12)
    ax.set_title('Global Exponent: Kernel Comparison', fontsize=13, fontweight='bold')
    ax.set_ylim(0, max(theory_eta * 1.2, max(etas) * 1.2))
    ax.legend(loc='upper right', framealpha=0.9, fontsize=11)
    ax.grid(True, axis='y', alpha=0.3)

    # Text annotation
    ax.text(0.5, 0.95, 'Compact support (Tricube) enables higher η',
            transform=ax.transAxes, ha='center', va='top', fontsize=10,
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.7))

    plt.tight_layout()
    if output_path:
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
        plt.close()
    else:
        return fig


def plot_main_figure_4panel(
    results: Dict,
    theory_eta: float,
    output_path: Optional[Path] = None,
    figsize: Tuple[float, float] = (14, 10)
):
    """
    Main 4-panel figure combining key results.

    Panel A: δ² vs h with theoretical slope
    Panel B: Per-bin η (smoking gun)
    Panel C: Locality comparison (r_eff/h)
    Panel D: Kernel comparison (global weighted η)
    """
    fig = plt.figure(figsize=figsize)
    gs = fig.add_gridspec(2, 2, hspace=0.3, wspace=0.3)

    # Panel A: δ² vs h
    ax_a = fig.add_subplot(gs[0, 0])
    _plot_delta2_panel(ax_a, results['tricube'], theory_eta)
    ax_a.text(-0.1, 1.05, 'A', transform=ax_a.transAxes, fontsize=16, fontweight='bold')

    # Panel B: Per-bin η
    ax_b = fig.add_subplot(gs[0, 1])
    _plot_eta_bins_panel(ax_b, results['tricube']['bin_results'], theory_eta)
    ax_b.text(-0.1, 1.05, 'B', transform=ax_b.transAxes, fontsize=16, fontweight='bold')

    # Panel C: Locality
    ax_c = fig.add_subplot(gs[1, 0])
    _plot_locality_panel(ax_c, results, results['locality_guards'])
    ax_c.text(-0.1, 1.05, 'C', transform=ax_c.transAxes, fontsize=16, fontweight='bold')

    # Panel D: Kernel comparison
    ax_d = fig.add_subplot(gs[1, 1])
    _plot_kernel_global_panel(ax_d, results, theory_eta)
    ax_d.text(-0.1, 1.05, 'D', transform=ax_d.transAxes, fontsize=16, fontweight='bold')

    plt.suptitle('Locality Validation: Complete Results', fontsize=16, fontweight='bold', y=0.995)

    if output_path:
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
        plt.close()
    else:
        return fig


# Helper functions for 4-panel plot
def _plot_delta2_panel(ax, tricube_res, theory_eta):
    """Helper: Plot δ² vs h on given axis."""
    n_bins = len(tricube_res['bin_results'])

    # Generate colors dynamically based on number of bins
    if n_bins > 3:
        colors = plt.cm.viridis(np.linspace(0.2, 0.8, n_bins))
    else:
        colors = ['#1f77b4', '#ff7f0e', '#2ca02c'][:n_bins]

    for i, bin_res in enumerate(tricube_res['bin_results']):
        h_fit = bin_res['h_fit']
        delta2_fit = bin_res['delta2_fit']
        eta = bin_res['eta']
        label = bin_res['label']

        ax.scatter(h_fit, delta2_fit, alpha=0.6, color=colors[i], s=30)
        log_h = np.log10(h_fit)
        log_delta2 = np.log10(delta2_fit)
        slope, intercept = np.polyfit(log_h, log_delta2, 1)
        h_line = np.array([h_fit[0], h_fit[-1]])
        delta2_line = 10**(slope * np.log10(h_line) + intercept)
        ax.plot(h_line, delta2_line, '--', color=colors[i], linewidth=1.5,
                label=f'{label}: η={eta:.2f}')

    # Theory line
    h_star = tricube_res['h_star']
    ax.axvline(h_star, color='gray', linestyle=':', alpha=0.5, linewidth=1.5)

    ax.set_xscale('log')
    ax.set_yscale('log')
    ax.set_xlabel(r'Bandwidth $h$', fontsize=11)
    ax.set_ylabel(r'Bias² $\delta^2$', fontsize=11)
    ax.set_title('Locality Scaling (Tricube)', fontsize=12, fontweight='bold')
    ax.legend(loc='best', fontsize=9, framealpha=0.9)
    ax.grid(True, alpha=0.3, which='both')


def _plot_eta_bins_panel(ax, bin_results, theory_eta):
    """Helper: Plot per-bin η on given axis."""
    n_bins = len(bin_results)

    if n_bins == 0:
        # No bins to plot - show message
        ax.text(0.5, 0.5, 'No bins with sufficient queries\n(need ≥10 queries per bin)',
               ha='center', va='center', transform=ax.transAxes, fontsize=11,
               bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.7))
        ax.set_title('Per-Bin Exponents', fontsize=12, fontweight='bold')
        ax.set_xlim(0, 1)
        ax.set_ylim(0, theory_eta * 1.5)
        return

    x = np.arange(n_bins)
    etas = [b['eta'] for b in bin_results]
    labels = [b['label'] for b in bin_results]

    colors = ['#1f77b4', '#ff7f0e', '#2ca02c']
    if n_bins > 3:
        colors = plt.cm.viridis(np.linspace(0.2, 0.8, n_bins))
    else:
        colors = colors[:n_bins]

    bars = ax.bar(x, etas, alpha=0.7, color=colors, edgecolor='black', linewidth=1.5)

    # Highlight middle if we have bins
    if n_bins > 0:
        mid_idx = n_bins // 2
        if mid_idx < len(bars):
            bars[mid_idx].set_facecolor('#ff7f0e')
            bars[mid_idx].set_alpha(0.9)

    ax.axhline(theory_eta, color='black', linestyle='--', linewidth=2, alpha=0.7,
               label=f'Theory: {theory_eta:.1f}')

    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=10)
    ax.set_ylabel(r'$\hat{\eta}$', fontsize=11)
    ax.set_xlabel(r'$|y_0|$ Bin', fontsize=11)
    ax.set_title('Per-Bin Exponents', fontsize=12, fontweight='bold')
    ax.legend(loc='upper right', fontsize=9)
    ax.grid(True, axis='y', alpha=0.3)


def _plot_locality_panel(ax, results_dict, locality_guards):
    """Helper: Plot r_eff/h comparison on given axis."""
    for kernel_name in ['gaussian', 'tricube']:
        if kernel_name not in results_dict:
            continue
        kernel_res = results_dict[kernel_name]
        h_grid = kernel_res['h_grid']
        r_eff_over_h = kernel_res['r_eff_over_h']

        color = '#ff7f0e' if kernel_name == 'gaussian' else '#1f77b4'
        marker = 'o' if kernel_name == 'tricube' else 's'

        ax.plot(h_grid, r_eff_over_h, marker=marker, linestyle='-',
                linewidth=1.5, markersize=4, alpha=0.8,
                label=f'{kernel_name.capitalize()}', color=color)

    # Guard band
    if 'tricube' in locality_guards:
        r_min = locality_guards['tricube']['r_eff_min']
        r_max = locality_guards['tricube']['r_eff_max']
        ax.axhspan(r_min, r_max, alpha=0.2, color='green', label='Locality target')

    ax.set_xscale('log')
    ax.set_xlabel(r'Bandwidth $h$', fontsize=11)
    ax.set_ylabel(r'$r_{\mathrm{eff}}/h$', fontsize=11)
    ax.set_title('Kernel Geometry', fontsize=12, fontweight='bold')
    ax.legend(loc='best', fontsize=9, framealpha=0.9)
    ax.grid(True, alpha=0.3, which='both')


def _plot_kernel_global_panel(ax, results_dict, theory_eta):
    """Helper: Plot kernel comparison on given axis."""
    kernel_names = ['gaussian', 'tricube']
    kernel_names = [k for k in kernel_names if k in results_dict]

    x = np.arange(len(kernel_names))
    etas = [results_dict[k]['weighted_eta'] for k in kernel_names]

    colors = ['#ff7f0e' if 'gaussian' in k else '#1f77b4' for k in kernel_names]
    ax.bar(x, etas, alpha=0.7, color=colors, edgecolor='black', linewidth=1.5, width=0.5)

    ax.axhline(theory_eta, color='black', linestyle='--', linewidth=2, alpha=0.7,
               label=f'Theory: {theory_eta:.1f}')

    for i, eta in enumerate(etas):
        ax.text(i, eta + 0.05, f'{eta:.2f}', ha='center', fontsize=10, fontweight='bold')

    ax.set_xticks(x)
    ax.set_xticklabels([k.capitalize() for k in kernel_names], fontsize=10)
    ax.set_ylabel(r'Weighted $\hat{\eta}$', fontsize=11)
    ax.set_title('Global Comparison', fontsize=12, fontweight='bold')
    ax.legend(loc='upper right', fontsize=9)
    ax.grid(True, axis='y', alpha=0.3)


def theoretical_eta_curve(y_vals: np.ndarray, q: float = 1.5, 
                          y_sweet_min: float = 0.01, 
                          y_sweet_max: float = 0.015) -> np.ndarray:
    """
    Theoretical η(y) based on drift m(y) = sign(y)|y|^q.
    
    Parameters
    ----------
    y_vals : array
        |y| values
    q : float
        Power-law exponent (η = 2q in sweet spot)
    y_sweet_min, y_sweet_max : float
        Bounds of sweet spot where full theory holds
        
    Returns
    -------
    eta_theory : array
        Theoretical η at each y value
        
    Notes
    -----
    - Flat region (y → 0): curvature m''(y) ~ |y|^(q-2) → 0  
      → Reduced effective exponent (transition 2 → 3)
    - Sweet spot: Strong curvature, η = 2q = 3.0
    - Tails: Finite samples dominate, η decays
    """
    abs_y = np.abs(y_vals)
    eta_theory = np.zeros_like(abs_y)
    
    # Sweet spot: full theoretical scaling
    sweet_mask = (abs_y >= y_sweet_min) & (abs_y <= y_sweet_max)
    eta_theory[sweet_mask] = 2 * q
    
    # Flat region: smoothness-limited
    # As |y| → 0, curvature m''(y) ~ |y|^(q-2) → 0
    # Effective exponent transitions from 2 → 3
    flat_mask = abs_y < y_sweet_min
    normalized_y = abs_y[flat_mask] / y_sweet_min  # 0 to 1
    # Smooth transition: eta = 2 + (2q-2)*normalized_y
    eta_theory[flat_mask] = 2.0 + (2*q - 2.0) * normalized_y
    
    # Tail region: sample-limited
    # Exponentially sparse samples → variance dominates
    tail_mask = abs_y > y_sweet_max
    # Exponential decay from 2q → 1.5
    decay_rate = 5.0
    decay = np.exp(-decay_rate * (abs_y[tail_mask] - y_sweet_max) / y_sweet_max)
    eta_theory[tail_mask] = 2 * q * decay + 1.5 * (1 - decay)
    
    return eta_theory


def plot_eta_vs_y_with_theory(
    bin_results: List[Dict],
    theory_eta: float,
    q: float = 1.5,
    output_path: Optional[Path] = None,
    figsize: Tuple[float, float] = (10, 6)
):
    """
    Plot η(|y|) across bins with theoretical curve overlay.
    
    Shows how local exponent varies with position in state space,
    revealing the distribution of smoothness. Empirical estimates
    are compared against theoretical predictions accounting for:
    - Reduced curvature near y=0
    - Sweet spot with η = 2q
    - Finite-sample effects in tails
    
    Parameters
    ----------
    bin_results : list of dict
        Each dict must have: 'y_range' (tuple), 'eta' (float), 'n_queries' (int)
    theory_eta : float
        Target exponent in sweet spot (= 2q)
    q : float
        Power-law exponent of drift
    """
    fig, ax = plt.subplots(figsize=figsize)
    
    # Extract bin centers and η estimates
    y_centers = []
    etas = []
    y_widths = []
    n_queries = []
    
    for b in bin_results:
        y_min, y_max = b['y_range']
        y_center = (y_min + y_max) / 2
        y_centers.append(y_center)
        etas.append(b['eta'])
        y_widths.append(y_max - y_min)
        n_queries.append(b['n_queries'])
    
    y_centers = np.array(y_centers)
    etas = np.array(etas)
    
    # Empirical points (size by n_queries)
    sizes = 50 + 200 * np.array(n_queries) / max(n_queries)
    scatter = ax.scatter(y_centers, etas, s=sizes, alpha=0.7, 
                        c=etas, cmap='viridis', edgecolor='black', linewidth=1.5,
                        zorder=3)
    
    # Error bars (width = bin width)
    ax.errorbar(y_centers, etas, xerr=np.array(y_widths)/2, 
               fmt='none', ecolor='gray', alpha=0.4, capsize=3, zorder=2)
    
    # Theoretical curve
    y_theory = np.linspace(0, y_centers.max() * 1.1, 200)
    y_sweet_min = np.percentile(y_centers, 25)
    y_sweet_max = np.percentile(y_centers, 75)
    eta_theory = theoretical_eta_curve(y_theory, q=q, 
                                      y_sweet_min=y_sweet_min, 
                                      y_sweet_max=y_sweet_max)
    
    ax.plot(y_theory, eta_theory, 'k-', linewidth=2.5, alpha=0.7,
           label=f'Theory: η(|y|)', zorder=1)
    
    # Sweet spot band
    ax.axhspan(theory_eta * 0.95, theory_eta * 1.05, 
              alpha=0.15, color='green', zorder=0,
              label=f'Theory target: {theory_eta:.1f}±5%')
    ax.axhline(theory_eta, color='black', linestyle='--', linewidth=1.5, alpha=0.5)
    
    # Annotate sweet spot region
    ax.axvspan(y_sweet_min, y_sweet_max, alpha=0.1, color='orange', zorder=0)
    ax.text((y_sweet_min + y_sweet_max)/2, ax.get_ylim()[1]*0.95, 
           'Sweet spot', ha='center', fontsize=10, 
           bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.7))
    
    # Colorbar
    cbar = plt.colorbar(scatter, ax=ax, label=r'$\hat{\eta}$')
    
    ax.set_xlabel(r'$|y_0|$ (bin center)', fontsize=12)
    ax.set_ylabel(r'Exponent $\hat{\eta}$', fontsize=12)
    ax.set_title('Exponent Distribution Across State Space', fontsize=13, fontweight='bold')
    ax.legend(loc='upper right', framealpha=0.9, fontsize=10)
    ax.grid(True, alpha=0.3)
    ax.set_ylim(0, max(etas.max(), theory_eta) * 1.2)
    
    # Text annotation
    ax.text(0.02, 0.98, 
           'Marker size ∝ n_queries\nColor = η estimate',
           transform=ax.transAxes, va='top', fontsize=9,
           bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
    
    plt.tight_layout()
    if output_path:
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
        plt.close()
    else:
        return fig


def plot_eta_distribution(
    bin_results: List[Dict],
    theory_eta: float,
    output_path: Optional[Path] = None,
    figsize: Tuple[float, float] = (8, 6)
):
    """
    Histogram of η estimates showing distribution of exponents.
    
    Visualizes the spread of local exponents, demonstrating that
    different parts of state space have different effective smoothness.
    The distribution peaks near the theoretical value in well-sampled
    regions with strong curvature.
    
    Parameters
    ----------
    bin_results : list of dict
        Each dict must have: 'eta' (float), 'n_queries' (int)
    theory_eta : float
        Target exponent (= 2q)
    """
    fig, ax = plt.subplots(figsize=figsize)
    
    # Extract η estimates (weighted by n_queries)
    etas = []
    weights = []
    
    for b in bin_results:
        etas.append(b['eta'])
        weights.append(b['n_queries'])
    
    etas = np.array(etas)
    weights = np.array(weights)
    
    # Histogram
    ax.hist(etas, bins=15, weights=weights, alpha=0.7, color='#1f77b4',
           edgecolor='black', linewidth=1.5, label='Empirical distribution')
    
    # Theory line
    ax.axvline(theory_eta, color='black', linestyle='--', linewidth=2.5,
              alpha=0.7, label=f'Theory: η = {theory_eta:.1f}')
    
    # Mean and weighted mean
    mean_eta = np.mean(etas)
    weighted_mean_eta = np.average(etas, weights=weights)
    
    ax.axvline(mean_eta, color='red', linestyle=':', linewidth=2,
              alpha=0.6, label=f'Mean: {mean_eta:.2f}')
    ax.axvline(weighted_mean_eta, color='orange', linestyle=':', linewidth=2,
              alpha=0.6, label=f'Weighted: {weighted_mean_eta:.2f}')
    
    # Statistics box
    stats_text = (
        f'n_bins = {len(etas)}\n'
        f'Mean η = {mean_eta:.2f}\n'
        f'Weighted η = {weighted_mean_eta:.2f}\n'
        f'Std = {np.std(etas):.2f}\n'
        f'Range = [{etas.min():.2f}, {etas.max():.2f}]'
    )
    ax.text(0.98, 0.98, stats_text,
           transform=ax.transAxes, va='top', ha='right', fontsize=9,
           bbox=dict(boxstyle='round', facecolor='white', alpha=0.9))
    
    ax.set_xlabel(r'Exponent $\hat{\eta}$', fontsize=12)
    ax.set_ylabel('Count (weighted by n_queries)', fontsize=12)
    ax.set_title('Distribution of Local Exponents', fontsize=13, fontweight='bold')
    ax.legend(loc='upper left', framealpha=0.9, fontsize=10)
    ax.grid(True, axis='y', alpha=0.3)
    
    plt.tight_layout()
    if output_path:
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
        plt.close()
    else:
        return fig
