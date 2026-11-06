#!/usr/bin/env python3
"""Power curves (POWER_CURVES.md)."""
import math, importlib.util
from pathlib import Path
import numpy as np
from scipy.linalg import eigh
sp = importlib.util.spec_from_file_location("ab", Path(__file__).with_name("assumption_breakers.py")); ab = importlib.util.module_from_spec(sp); sp.loader.exec_module(ab)
K = 10


def base(kind, n, rng):
    if kind == "independent": return rng.standard_normal((n, K))
    S = rng.standard_normal((n, K)); return np.column_stack([(S[:, (i - 1) % K] + S[:, i]) / math.sqrt(2) for i in range(K)])


def world(kind, r, lam2, n, rng):
    F = rng.standard_normal((n, K)); f = rng.standard_normal(n); F[:, :r] = f[:, None]
    return math.sqrt(1 - lam2) * base(kind, n, rng) + math.sqrt(lam2) * F


def pop_vg(kind, r, lam2):
    B = np.eye(K) if kind == "independent" else np.eye(K) + 0.5 * (np.eye(K, k=1) + np.eye(K, k=-1) + np.eye(K, k=K-1) + np.eye(K, k=-(K-1)))
    Fc = np.eye(K); Fc[:r, :r] = 1; R = (1 - lam2) * B + lam2 * Fc
    return float(np.max(np.abs(np.linalg.eigvalsh(np.abs(R - np.eye(K)))))) - 1


def main():
    rng = np.random.default_rng(18)
    for kind in ("boundary", "independent"):
        print(f"\n== base: {kind}")
        print("reach lam2  popVG   " + "  ".join(f"n={n:<4d}" for n in (30, 53, 100)))
        for r in (3, 5, 10):
            for lam2 in (0.05, 0.1, 0.2, 0.3, 0.5):
                pw = [np.mean([ab.test(ab.jit(world(kind, r, lam2, n, rng), rng), False, rng) for _ in range(100)]) for n in (30, 53, 100)]
                print(f"{r:5d} {lam2:4.2f} {pop_vg(kind, r, lam2):+6.2f}   " + "  ".join(f"{p:6.2f}" for p in pw), flush=True)


if __name__ == "__main__":
    main()
