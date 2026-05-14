"""Quick test of JS divergence fix"""
import numpy as np
import common_utils as cu
from logging_utils import setup_logger
import logging

logger = setup_logger("js_test", level=logging.INFO, console=True)

# Test JS divergence on simple Gaussians
rng = cu.make_rng(42)

# Two nearby Gaussians
x_p = rng.normal(0.0, 1.0, size=(500, 1))
x_q = rng.normal(0.2, 1.0, size=(500, 1))

# Compute JS divergence with both methods
js_kde = cu.js_divergence(x_p, x_q, method="kde")
js_hist = cu.js_divergence(x_p, x_q, method="hist", bins=32)

print(f"\nJS divergence (KDE): {js_kde:.6f}")
print(f"JS divergence (hist): {js_hist:.6f}")

# Test identical distribution
x_same = rng.normal(0.0, 1.0, size=(500, 1))
js_same_kde = cu.js_divergence(x_same, x_same, method="kde")
js_same_hist = cu.js_divergence(x_same, x_same, method="hist", bins=32)

print(f"\nJS divergence on identical (KDE): {js_same_kde:.6f}")
print(f"JS divergence on identical (hist): {js_same_hist:.6f}")

# Test far apart Gaussians
x_far = rng.normal(3.0, 1.0, size=(500, 1))
js_far_kde = cu.js_divergence(x_p, x_far, method="kde")
js_far_hist = cu.js_divergence(x_p, x_far, method="hist", bins=32)

print(f"\nJS divergence far (KDE): {js_far_kde:.6f}")
print(f"JS divergence far (hist): {js_far_hist:.6f}")

print("\n✓ All JS divergences should be non-negative!")
print(f"✓ Ordering: near({js_kde:.4f}) < far({js_far_kde:.4f}): {js_kde < js_far_kde}")
