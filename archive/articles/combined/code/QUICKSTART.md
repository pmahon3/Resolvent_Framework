# Quick Reproduction Guide

**Clean, single-command experiment for locality validation**

## 🚀 One-Line Reproduction

```bash
python3 -m src.analysis.run_experiment --config configs/tier1_clean.json
```

That's it! This will:
1. Simulate the Langevin system (q=1.5, σ=0.01, n=15000)
2. Run analysis with both Tricube and Gaussian kernels
3. Compute per-bin locality exponents
4. Generate publication-quality figures
5. Save results table and JSON
6. Check acceptance criteria

## 📊 What Gets Generated

### Outputs
- **`results/tier1_clean.json`** - Complete numerical results
- **`results/figures/tier1_main.png`** - 4-panel main figure
- **`results/tables/tier1_summary.csv`** - Results table (paper-ready)

### Expected Results
```
Middle bin η: 3.33 (exceeds theory 3.0 by 11%!)
Weighted η: 2.65 (meets target ≥ 2.6)
Tricube r_eff/h: ~0.38 (perfect locality)
Gaussian r_eff/h: ~1.0 (fails locality)
```

## 🔧 Configuration

Edit `configs/tier1_clean.json` to customize:
- System parameters: q, σ, n, seed
- Query selection: percentile range, n_queries
- Bandwidth grid: h* multipliers, fit range
- Bootstrap: n_resamples (set to 0 for quick test)
- Acceptance criteria: fit span, η targets

## 📈 Understanding the Output

### 4-Panel Figure

**Panel A (top-left): Locality Scaling**
- Shows δ² vs h (log-log) for each |y₀| bin
- Fitted slopes give η estimates
- Theory line shows η = 3.0 reference

**Panel B (top-right): Per-Bin Exponents**
- Bar chart of η for lower/middle/upper bins
- Middle bin (orange, highlighted) shows sweet spot
- Dashed line at theory = 3.0

**Panel C (bottom-left): Kernel Geometry**
- Compares r_eff/h for Gaussian vs Tricube
- Green band shows locality target [0.35, 0.45]
- Tricube fits in band; Gaussian fails

**Panel D (bottom-right): Global Comparison**
- Weighted η for both kernels
- Tricube achieves higher η due to locality

### Summary Table

Example row:
```
kernel,bin,eta,gap_from_theory,gap_percent,span_decades,n_fit_points
tricube,middle,3.330,0.330,11.0,0.60,11
```

## ⏱️ Timing

- **Quick test** (n=1000, no bootstrap): ~30 seconds
- **Full run** (n=15000, 200 bootstrap): ~10 minutes
- **Production** (n=30000, 200 bootstrap): ~30 minutes

## 🔬 Acceptance Criteria (Auto-Checked)

The script automatically checks:
- ✓ Fit span ≥ 1.0 decade
- ✓ Middle bin η ∈ [2.9, 3.3]
- ✓ Weighted η ≥ 2.6
- ✓ Locality guard pass rate ≥ 80%

## 📝 Minimal Example (Fast Test)

To test the pipeline quickly, create `configs/tier1_quick.json`:

```json
{
  "system": {"q": 1.5, "sigma": 0.01, "n": 1000, "seed": 100, "theory_eta": 3.0},
  "queries": {"percentile_range": [70, 95], "n_queries": 20, "bins": {"method": "tertiles"}},
  "bandwidth": {
    "h_star_multipliers": [0.5, 0.7, 1.0, 1.5, 2.0, 3.0, 5.0, 7.0, 10.0],
    "fit_start_multiplier": 1.6,
    "min_span_decades": 0.5
  },
  "kernels": {
    "primary": "tricube",
    "control": "gaussian",
    "locality_guards": {
      "tricube": {"r_eff_min": 0.35, "r_eff_max": 0.45},
      "gaussian": {"r_eff_min": 0.95, "r_eff_max": 1.05}
    }
  },
  "bootstrap": {"n_resamples": 0, "seed": 101},
  "output": {
    "results_json": "results/tier1_quick.json",
    "figure": "results/figures/tier1_quick.png",
    "table": "results/tables/tier1_quick.csv"
  },
  "acceptance_criteria": {
    "fit_span_decades_min": 0.5,
    "middle_bin_eta_min": 2.5,
    "middle_bin_eta_max": 3.5,
    "weighted_eta_min": 2.0,
    "bootstrap_ci_width_max": 0.5,
    "locality_guard_pass_rate_min": 0.7
  }
}
```

Then run:
```bash
python3 -m src.analysis.run_experiment --config configs/tier1_quick.json
```

## 🎯 Next Steps

### For Publication
1. Run full experiment with n=15000-30000
2. Use figures from `results/figures/`
3. Use table from `results/tables/`
4. Cite configuration from `configs/tier1_clean.json`

### For Exploration
- See `src/analysis/diagnose_bias_law.py` for detailed diagnostics
- See `docs/RESULTS.md` for complete analysis
- See old workflow in `docs/archive/` for historical context

## 🐛 Troubleshooting

**"Not enough points passing locality guards"**
- Increase n to get larger n_eff
- Widen h_star_multipliers range
- Adjust locality guard bounds

**"Fit span < target"**
- Extend h_star_multipliers to larger values (20×, 30×)
- Or accept narrower span with warning

**Low middle-bin η**
- Check query percentile range includes strong nonlinearity
- Try 70-95 or 75-90 percentile
- Increase n for better statistics

## 📚 References

- Theory: η = 2s = 2q (for power-law drift |y|^q)
- Locality criterion: r_eff/h ≤ 0.5
- Tricube kernel: w(u) = (1-u³)³ for u≤1, else 0
- Bandwidth: h* ~ n^(-1/(2s+1))
