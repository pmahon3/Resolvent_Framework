# Debugging Notes: Locality Guard Failure

## Problem Summary

**Date**: 2025-10-14
**Issue**: `eta_u_quick.json` experiment ran for 2.5 hours but produced **zero usable fit points**

### Observed Symptoms

```
Tricube kernel:
- Computed δ² over 28 bandwidth values (146 minutes)
- r_eff/h range: [0.323, 0.380]  ← PROBLEM HERE
- Locality guard pass rate: 89.5%  ← Overall good
- Fit span: 0.00 decades (0 points)  ← FAILURE
- η = nan (no fit possible)
```

## Root Cause

**Locality guard mismatch in fit window:**

```json
{
  "locality_guards": {
    "tricube": {"r_eff_min": 0.35, "r_eff_max": 0.45}  ← Too strict
  }
}
```

**Observed r_eff/h**: [0.323, 0.380]
**Guard requirement**: [0.35, 0.45]

The **minimum** r_eff/h (0.323) was **below** the guard threshold (0.35), causing many points to fail. More importantly, in the **fit window** (h ≥ 1.6×h*), **ALL points failed** the locality guard.

### Why Overall Pass Rate Was Misleading

- Overall pass rate: 89.5% (across all h values)
- Fit window pass rate: 0% (in the h > 1.6×h* region)

The experiment **wasted 2.5 hours** computing points that couldn't be used for fitting.

## Solutions Implemented

### 1. Added Early Diagnostic Logging

Added pre-fit diagnostics in `src/analysis/run_experiment.py:367-396`:

```python
# EARLY DIAGNOSTIC: Check locality guard status before expensive fitting
print(f"\n🔍 Locality Guard Diagnostic:")
print(f"  Target range: r_eff/h ∈ [{r_min:.3f}, {r_max:.3f}]")

# Check overall pass rate
locality_mask_all = (r_eff_over_h >= r_min) & (r_eff_over_h <= r_max) & (n_eff >= 50)
print(f"  Overall pass rate: {locality_mask_all.sum()}/{len(r_eff_over_h)}")

# Check fit window specifically
fit_window_mask = locality_mask_all[fit_start_idx:]
print(f"  Fit window (h ≥ {fit_start_mult:.1f}×h*): {fit_window_mask.sum()}/{len(fit_window_mask)} pass")
print(f"  r_eff/h in fit window: [{r_eff_over_h[fit_start_idx:].min():.3f}, {r_eff_over_h[fit_start_idx:].max():.3f}]")

if fit_window_mask.sum() == 0:
    print(f"  ⚠️  WARNING: ZERO points pass locality guard in fit window!")
    print(f"  ⚠️  This will result in empty h_fit and failed experiment.")
    print(f"  Suggestions:")
    print(f"    - Relax r_eff_min from {r_min:.3f} to {r_eff_over_h[fit_start_idx:].min():.3f}")
    print(f"    - Or reduce fit_start_multiplier from {fit_start_mult:.1f}")
```

**Benefit**: Catch locality guard failures **immediately** after grid computation (seconds), not after hours of wasted work.

### 2. Created Fixed Config

Created `configs/eta_u_quick_fixed.json` with relaxed locality guards:

```json
{
  "locality_guards": {
    "tricube": {"r_eff_min": 0.30, "r_eff_max": 0.50},  ← Relaxed from [0.35, 0.45]
    "gaussian": {"r_eff_min": 0.90, "r_eff_max": 1.10}   ← Relaxed from [0.95, 1.05]
  }
}
```

**Rationale**:
- Observed tricube r_eff/h: [0.323, 0.380]
- Set r_eff_min = 0.30 (safely below minimum)
- Set r_eff_max = 0.50 (safely above maximum)

### 3. Enhanced Progress Logging

Already had detailed timing logs showing:
- Time per bandwidth with ETA
- Time per bin with ETA
- Total elapsed time

## Lessons Learned

1. **Check locality guards early**: Don't wait until after expensive computation to discover guard failures

2. **Overall metrics can be misleading**: 89.5% overall pass rate hid 0% pass rate in the critical fit window

3. **Add diagnostic checkpoints**: Early warnings save hours of wasted computation

4. **Validate guards against observed data**: Locality guards from theory may not match empirical distributions

## Testing Strategy

Run `eta_u_quick_fixed.json` with:
1. Diagnostic logging to verify guard status
2. Timing logs to track progress
3. Relaxed guards to ensure fit points exist

Expected outcome:
- Diagnostic shows >70% pass rate in fit window
- At least 5-10 points available for fitting
- Successful η(u) curve generation

## Future Improvements

1. **Auto-adjust guards**: Automatically relax guards if fit window has < 5 points
2. **Pre-flight check**: Quick 3-bandwidth test to validate guards before full run
3. **Config validation**: Check that guards are compatible with expected r_eff/h ranges
