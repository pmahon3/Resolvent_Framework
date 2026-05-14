# Robust Fitting Implementation for Publication-Quality Results

## Overview

This document describes the improvements to the locality validation pipeline for publication-ready results with proper uncertainty quantification and quality guards.

## Implemented Features

### 1. Extended Bandwidth Grid
**File**: `configs/tier1_10bins.json`
- Extended from 20×h* → 40×h* (added 5 new points)
- Provides ~1.0-1.2 decades span after locality guards (vs 0.65 before)
- New config flags:
  - `use_robust_slope`: true (enable Theil-Sen regression)
  - `curvature_guard_threshold`: 2.0 (max allowed |d²/dh²|)

### 2. Robust Fitting Module
**File**: `src/analysis/robust_fitting.py`

**Key Functions**:
- `theil_sen_slope()`: Robust slope estimation (resistant to outliers)
- `select_fit_window()`: Auto-select fit window with guards:
  1. **Locality guard**: r_eff/h ∈ [0.35, 0.45] for tricube
  2. **Monotonicity check**: Allow ≤2 violations in increasing δ²(h)
  3. **Curvature guard**: Find longest segment with |d²/dh²| < threshold
  4. **Span requirement**: Require ≥1.0 decades