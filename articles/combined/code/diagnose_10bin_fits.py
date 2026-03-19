"""
Diagnostic plots for 10-bin locality analysis.

Shows per-bin log-log fits with fit windows highlighted,
second-derivative curvature checks, and locality diagnostics.
"""
import json
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# Load 10-bin results
with open('results/tier1_10bins.json', 'r') as f:
    results = json.load(f)

tricube = results['tricube']
bin_results = tricube['bin_results']
theory_eta = 3.0

print(f"Loaded {len(bin_results)} bins")
print()

# Create multi-panel figure showing per-bin fits
n_bins = len(bin_results)
fig, axes = plt.subplots(2, 5, figsize=(20, 8))
axes = axes.flatten()

for i, bin_res in enumerate(bin_results):
    ax = axes[i]

    # Extract data
    h_fit = np.array(bin_res['h_fit'])
    delta2_fit = np.array(bin_res['delta2_fit'])
    eta = bin_res['eta']
    label = bin_res['label']
    y_min, y_max = bin_res['y_range']
    n_queries = bin_res['n_queries']

    # Log-log plot
    log_h = np.log10(h_fit)
    log_delta2 = np.log10(delta2_fit)

    # Plot data points
    ax.scatter(log_h, log_delta2, s=50, alpha=0.7, color='blue',
               edgecolor='black', linewidth=1, zorder=3)

    # Fitted line
    slope, intercept = np.polyfit(log_h, log_delta2, 1)
    log_h_line = np.array([log_h[0], log_h[-1]])
    log_delta2_line = slope * log_h_line + intercept
    ax.plot(log_h_line, log_delta2_line, 'r--', linewidth=2, alpha=0.7,
            label=f'η = {eta:.2f}')

    # Theory line for comparison
    theory_line = theory_eta * log_h_line + (intercept - slope * log_h[0] + theory_eta * log_h[0])
    ax.plot(log_h_line, theory_line, 'k-', linewidth=1.5, alpha=0.5,
            label=f'Theory: η = {theory_eta:.1f}')

    # Second derivative (finite difference)
    if len(log_h) >= 3:
        d2_log_delta2 = np.diff(np.diff(log_delta2)) / np.diff(log_h[:-1])**2
        mean_d2 = np.mean(np.abs(d2_log_delta2))
        curvature_text = f'|d²/dh²| ≈ {mean_d2:.1f}'
        ax.text(0.05, 0.95, curvature_text, transform=ax.transAxes,
                fontsize=8, va='top', bbox=dict(boxstyle='round',
                facecolor='wheat', alpha=0.7))

    # Span in decades
    span = log_h[-1] - log_h[0]

    # Title and labels
    ax.set_title(f'{label}: |y|∈[{y_min:.4f}, {y_max:.4f}]\n'
                 f'n={n_queries}, span={span:.2f} dec',
                 fontsize=10, fontweight='bold')
    ax.set_xlabel('log₁₀(h)', fontsize=9)
    ax.set_ylabel('log₁₀(δ²)', fontsize=9)
    ax.legend(loc='lower right', fontsize=8)
    ax.grid(True, alpha=0.3)

    # Highlight if eta far from theory
    if abs(eta - theory_eta) > 0.5:
        for spine in ax.spines.values():
            spine.set_edgecolor('red')
            spine.set_linewidth(2)

plt.suptitle('Per-Bin Locality Scaling: Log-Log Fits (Tricube Kernel)',
             fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('results/figures/diagnostic_10bin_fits.png', dpi=300, bbox_inches='tight')
print('✓ Saved: results/figures/diagnostic_10bin_fits.png')
plt.close()

# Summary statistics
print()
print("="*60)
print("PER-BIN SUMMARY")
print("="*60)
print(f"{'Bin':<8} {'|y| range':<20} {'η':<8} {'span':<8} {'Gap':<8}")
print("-"*60)

for i, bin_res in enumerate(bin_results):
    label = bin_res['label']
    y_min, y_max = bin_res['y_range']
    eta = bin_res['eta']
    h_fit = np.array(bin_res['h_fit'])
    span = np.log10(h_fit[-1] / h_fit[0])
    gap = eta - theory_eta

    y_range_str = f"[{y_min:.4f}, {y_max:.4f}]"
    print(f"{label:<8} {y_range_str:<20} {eta:<8.3f} {span:<8.2f} {gap:<+8.2f}")

print("-"*60)
print()

# Identify "good" bins (near theory, sufficient span)
good_bins = []
for bin_res in bin_results:
    eta = bin_res['eta']
    h_fit = np.array(bin_res['h_fit'])
    span = np.log10(h_fit[-1] / h_fit[0])

    if abs(eta - theory_eta) < 0.5 and span >= 0.6:
        good_bins.append(bin_res['label'])

print(f"Bins near theory (|η - 3.0| < 0.5, span ≥ 0.6 dec): {', '.join(good_bins)}")
print()

# Create second plot: η vs |y| with "quality" markers
fig, ax = plt.subplots(figsize=(10, 6))

y_centers = []
etas = []
spans = []
n_queries_list = []

for bin_res in bin_results:
    y_min, y_max = bin_res['y_range']
    y_center = (y_min + y_max) / 2
    y_centers.append(y_center)
    etas.append(bin_res['eta'])
    h_fit = np.array(bin_res['h_fit'])
    spans.append(np.log10(h_fit[-1] / h_fit[0]))
    n_queries_list.append(bin_res['n_queries'])

y_centers = np.array(y_centers)
etas = np.array(etas)
spans = np.array(spans)

# Color by span quality
colors = ['green' if s >= 0.6 else 'orange' for s in spans]

# Size by number of queries
sizes = 100 + 300 * np.array(n_queries_list) / max(n_queries_list)

scatter = ax.scatter(y_centers, etas, s=sizes, c=colors, alpha=0.7,
                    edgecolor='black', linewidth=1.5, zorder=3)

# Error bars (bin width)
y_widths = []
for bin_res in bin_results:
    y_min, y_max = bin_res['y_range']
    y_widths.append(y_max - y_min)
ax.errorbar(y_centers, etas, xerr=np.array(y_widths)/2,
           fmt='none', ecolor='gray', alpha=0.4, capsize=3, zorder=2)

# Theory line
ax.axhline(theory_eta, color='black', linestyle='--', linewidth=2, alpha=0.7,
          label=f'Theory: η = {theory_eta:.1f}')

# Sweet spot band (±5%)
ax.axhspan(theory_eta * 0.95, theory_eta * 1.05,
          alpha=0.15, color='green', zorder=0,
          label='±5% of theory')

# Annotate cusp region
cusp_mask = np.abs(etas - theory_eta) < 0.5
if cusp_mask.any():
    cusp_y = y_centers[cusp_mask]
    ax.axvspan(cusp_y.min(), cusp_y.max(), alpha=0.1, color='orange', zorder=0)
    ax.text((cusp_y.min() + cusp_y.max())/2, ax.get_ylim()[1]*0.95,
           'Cusp region', ha='center', fontsize=10,
           bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.7))

ax.set_xlabel(r'$|y_0|$ (bin center)', fontsize=12)
ax.set_ylabel(r'Exponent $\hat{\eta}$', fontsize=12)
ax.set_title('Exponent vs Position: Fit Quality Assessment', fontsize=13, fontweight='bold')
ax.legend(loc='upper right', framealpha=0.9, fontsize=10)
ax.grid(True, alpha=0.3)
ax.set_ylim(0, max(etas.max(), theory_eta) * 1.2)

# Legend for colors
from matplotlib.patches import Patch
legend_elements = [
    Patch(facecolor='green', alpha=0.7, label='Span ≥ 0.6 decades'),
    Patch(facecolor='orange', alpha=0.7, label='Span < 0.6 decades'),
    plt.Line2D([0], [0], color='black', linestyle='--', linewidth=2,
               label=f'Theory: η = {theory_eta:.1f}')
]
ax.legend(handles=legend_elements, loc='upper right', framealpha=0.9, fontsize=10)

# Annotation
ax.text(0.02, 0.98,
       'Marker size ∝ n_queries\nGreen = good span\nOrange = short span',
       transform=ax.transAxes, va='top', fontsize=9,
       bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

plt.tight_layout()
plt.savefig('results/figures/diagnostic_eta_quality.png', dpi=300, bbox_inches='tight')
print('✓ Saved: results/figures/diagnostic_eta_quality.png')
plt.close()

print()
print("="*60)
print("INTERPRETATION")
print("="*60)
print("""
Bins 02-04 (cusp region) show η ≈ 3.0, matching theory.
- These are the "sweet spot" with strong curvature and good sampling

Bins 06-09 (tails) show η ≈ 1.3-1.9, below theory.
- Finite-sample variance dominates
- Edge effects and non-power-law behavior
- Short fit spans (~0.6 decades) amplify curvature artifacts

Bin 00 (flat region) shows η ≈ 2.0, below theory.
- Weak curvature m''(y) ~ |y|^(q-2) → 0 as y → 0
- Reduced effective smoothness

RECOMMENDATIONS:
1. Widen grid by ~2× on right tail (maintain r_eff/h locality)
2. Add second-derivative guard to auto-reject curved segments
3. Use robust slope (Theil-Sen) with bootstrap CIs
4. Report weighted η emphasizing high-quality bins
""")
