# Implementation Gap Analysis

## What exists (archive/articles/combined/code/)

### Core: `src/core/common_utils.py`

`local_linear_mean(X, Y, x0, h, weight, ridge, min_pts)`

Already implements:
- ✅ Weighted local linear regression: Y ≈ A·(X-x₀) + b
- ✅ Jacobian A = g/h (the local linearized pushforward)
- ✅ Residual covariance Σ = (residuals^T W residuals) / w_sum
- ✅ Tricube kernel: w(u) = (1-u³)³ for |u| ≤ 1
- ✅ Also: Gaussian, exponential kernels
- ✅ Ridge regularization
- ✅ Effective sample size n_eff
- ✅ Effective radius r_eff
- ✅ Condition number of design matrix
- ✅ Returns LocalLinearResult with A, b, mu, Sigma, diagnostics

### Simulation: `src/simulation/tier1_scalar.py`

- ✅ Scalar Langevin dynamics: y_{t+1} = sign(y)|y|^q + noise
- ✅ Configurable noise amplitude
- ✅ Time series generation

### Analysis: `src/analysis/`

- ✅ Robust fitting (robust_fitting.py)
- ✅ Per-bin analysis (eta_theory.py)
- ✅ Plotting infrastructure

## What's missing

### 1. Delay embedding (trivial)

```python
def delay_embed(y, d, L):
    """Form delay vectors from scalar time series."""
    N = len(y) - (d-1)*L
    return np.array([y[t + np.arange(d)*L] for t in range(N)])
```

~5 lines. Not implemented but trivial.

### 2. Divergence computation (one line)

```python
div_F = np.trace(A)  # A is d×d Jacobian from local_linear_mean
```

Already have A from the local linear fit. Just take the trace.

### 3. Attractor-wide mapping

Need: loop over query points, compute (A(z), σ(z), div(z)) at
each, store as arrays.

```python
def map_attractor(Z, Z_next, h, n_query=1000):
    """Map A, sigma, div over the reconstructed attractor."""
    query_idx = np.random.choice(len(Z), n_query, replace=False)
    results = []
    for i in query_idx:
        res = local_linear_mean(Z, Z_next, Z[i], h=h, weight="tricube")
        div_i = np.trace(res.A)
        sigma_i = np.sqrt(np.trace(res.Sigma) / Z.shape[1])
        results.append({'z': Z[i], 'A': res.A, 'div': div_i,
                       'sigma': sigma_i, 'n_eff': res.n_eff})
    return results
```

~20 lines. Straightforward extension of existing code.

### 4. Test systems (moderate effort)

Need generators for:
- Lorenz-63: standard, many implementations available
- Rössler: standard
- Logistic map: trivial
- Irrational rotation (from fibre mixing notes): trivial

Plus: ground-truth Lyapunov exponents for comparison.
Lorenz: λ₁ ≈ 0.91, λ₂ ≈ 0, λ₃ ≈ -14.57 → sum ≈ -13.66
Rössler: λ₁ ≈ 0.07, λ₂ ≈ 0, λ₃ ≈ -5.4 → sum ≈ -5.33

### 5. Embedding dimension sweep

Run the pipeline at d = 1, 2, 3, 4, 5, ... and track:
- How σ(z) decreases with d
- How div(z) converges to the true Lyapunov sum
- The point where both stabilize = sufficient embedding dimension

This is the key experiment: it demonstrates the diagnostic.

### 6. Comparison with FNN

Implement false nearest neighbours (standard algorithm) and show
correlation with our residual-based diagnostic.

### 7. Bandwidth selection

The existing code has h as a parameter. Need an adaptive method:
- Cross-validation on prediction error
- Or: residual-based (choose h to minimize structured residuals)

## Effort estimate

| Component | Lines of code | Time |
|-----------|--------------|------|
| Delay embedding | ~10 | 30 min |
| Divergence + attractor mapping | ~50 | 2 hours |
| Lorenz/Rössler generators | ~50 | 2 hours |
| Dimension sweep experiment | ~100 | 1 day |
| FNN comparison | ~80 | 1 day |
| Bandwidth selection | ~100 | 2 days |
| Plotting / figures | ~200 | 2 days |
| **Total new code** | **~600** | **~1 week** |

The existing `local_linear_mean` is the heavy lifting — already
done and tested. The new code is all glue and experiments.

## Key risk

The main risk is **bandwidth sensitivity**: if σ(z) and div(z)
depend strongly on h (the kernel bandwidth), the diagnostic is
unreliable. Mitigation: show stability across a range of h, or
develop the adaptive bandwidth selection before running
experiments.
