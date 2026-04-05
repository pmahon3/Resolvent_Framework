"""
Generate distribution plots from existing results.
"""
import json
import numpy as np
from pathlib import Path
from src.analysis import plotting

# Load existing 3-bin results
print("Loading results from tier1_clean.json...")
with open('results/tier1_clean.json', 'r') as f:
    results = json.load(f)

tricube_results = results['tricube']
bin_results = tricube_results['bin_results']
theory_eta = 3.0
q = 1.5

print(f"Found {len(bin_results)} bins")
print()

# Plot 1: η vs |y| with theory
print("Generating Plot 1: η vs |y| with theoretical curve...")
plotting.plot_eta_vs_y_with_theory(
    bin_results,
    theory_eta,
    q=q,
    output_path=Path('results/figures/eta_vs_y_theory_3bins.png')
)
print("✓ Saved to: results/figures/eta_vs_y_theory_3bins.png")
print()

# Plot 2: η distribution histogram
print("Generating Plot 2: η distribution histogram...")
plotting.plot_eta_distribution(
    bin_results,
    theory_eta,
    output_path=Path('results/figures/eta_distribution_3bins.png')
)
print("✓ Saved to: results/figures/eta_distribution_3bins.png")
print()

print("="*60)
print("✓✓✓ Distribution plots generated successfully!")
print("="*60)
print()
print("View the plots:")
print("  results/figures/eta_vs_y_theory_3bins.png")
print("  results/figures/eta_distribution_3bins.png")
