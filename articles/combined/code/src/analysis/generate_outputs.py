"""
Generate CSV table and plots from existing JSON results.
Avoids rerunning expensive experiments when only outputs need regeneration.
"""
import json
import sys
from pathlib import Path
import numpy as np

from src.analysis.plot_eta_overlay import plot_eta_u_overlay


def generate_summary_table(results: dict, config: dict, output_path: Path):
    """Generate CSV summary table from results."""
    output_path.parent.mkdir(parents=True, exist_ok=True)

    theory_eta = config['system'].get('theory_eta', 2 * config['system']['q'])

    with open(output_path, 'w') as f:
        # Header
        f.write("kernel,bin,u_rep,eta_hat,eta_theory,delta,ci_lo,ci_hi,n_queries,passed\n")

        # Per-kernel, per-bin rows
        for kernel_name in ['tricube', 'gaussian']:
            if kernel_name not in results:
                continue

            kernel_res = results[kernel_name]
            bin_results = kernel_res.get('bin_results', [])

            for b in bin_results:
                label = b['label']
                u_rep = b.get('u_rep', np.nan)
                eta_hat = b['eta']
                delta = eta_hat - theory_eta
                n_q = b.get('n_queries', 0)
                passed = b.get('passed_guards', True)

                # CI if bootstrap was run
                ci_lo = ci_hi = np.nan
                if 'bootstrap' in kernel_res and kernel_res['bootstrap'].get('ci_per_bin'):
                    ci_dict = kernel_res['bootstrap']['ci_per_bin'].get(label, {})
                    ci_lo = ci_dict.get('lo', np.nan)
                    ci_hi = ci_dict.get('hi', np.nan)

                f.write(f"{kernel_name},{label},{u_rep:.3f},{eta_hat:.3f},{theory_eta:.3f},"
                       f"{delta:+.3f},{ci_lo:.3f},{ci_hi:.3f},{n_q},{passed}\n")


def main():
    if len(sys.argv) != 3:
        print("Usage: python -m src.analysis.generate_outputs <results.json> <config.json>")
        sys.exit(1)

    results_path = Path(sys.argv[1])
    config_path = Path(sys.argv[2])

    # Load results and config
    with open(results_path, 'r') as f:
        results = json.load(f)

    with open(config_path, 'r') as f:
        config = json.load(f)

    print(f"Loaded results from: {results_path}")
    print(f"Loaded config from: {config_path}")

    # 1. Generate CSV table
    table_path = Path(config['output']['table'])
    generate_summary_table(results, config, table_path)
    print(f"\n✓ Generated table: {table_path}")

    # 2. Generate η(u) overlay plot
    if 'tricube' in results and 'bin_results' in results['tricube']:
        overlay_path = Path(config['output'].get('figure_overlay',
                                                  'results/figures/eta_u_overlay.png'))
        overlay_path.parent.mkdir(parents=True, exist_ok=True)

        q = config['system']['q']
        p = config.get('theory', {}).get('transition_sharpness_p', 2.0)

        plot_eta_u_overlay(
            bin_results=results['tricube']['bin_results'],
            q=q,
            p=p,
            output_path=overlay_path
        )
        print(f"✓ Generated overlay plot: {overlay_path}")

    print("\nAll outputs generated successfully!")


if __name__ == '__main__':
    main()
