"""
Entry point #1 (infinite extension case) — the L(H) clustering argument.

QUESTION (handoff): does the meet-zero/orthogonal gap produce the same
universal extension failure on L(H), dim H = ∞, as on MO₃? Does
σ-completeness change it?

ANSWER (this script verifies the finite-dimensional core):
NO normal/σ-additive (Gleason) state on L(H) extends to a finitely
additive charge on the full Boolean clopen algebra of S₀(L(H)), and
σ-completeness is IRRELEVANT — extension is a finitary charge condition.

THE CONSTRUCTION (no Gleason needed; pure orthoadditivity):
Fix a 2-dim subspace e ⊂ H. For any line p ⊂ e, the perpendicular line
p' ⊂ e satisfies p ⊥ p' and p ∨ p' = e, so a STATE obeys
    s(p) + s(p') = s(e)                                    (*)
Now pick k DISTINCT lines p_1,…,p_k in e (generic ⟹ the 2k lines
{p_i, p_i'} are pairwise distinct). Distinct lines meet only at 0, so all
2k are PAIRWISE MEET-ZERO. Since h preserves meets, h sends them to 2k
pairwise-DISJOINT clopens in S₀(L(H)). A finitely additive charge μ ≥ 0
with μ(whole)=1, extending μ(h(a)) = s(a), must satisfy
    Σ_i [ s(p_i) + s(p_i') ] ≤ 1.
By (*) the left side is exactly k·s(e). Hence
    k · s(e) ≤ 1   for EVERY k ≥ 1.
If s(e) > 0, choosing k > 1/s(e) violates it. So:

    ANY state with s(e) > 0 for even ONE finite-dim e FAILS extension.

Every normal state s = tr(ρ·) has s(e) > 0 for some 2-dim e (ρ ≠ 0), so
NO normal state extends. The argument uses only orthoadditivity on lines
inside one 2-plane; σ-completeness of the lattice never enters.

THE RESIDUE (open, NOT closed by this argument): a state with s(e) = 0
for EVERY finite-dim e — a singular / purely-finitely-additive
orthoadditive state vanishing on all finite-rank projections (lives "at
infinity", cf. states factoring through the Calkin algebra). For such a
state every line has measure 0, so the clustering bound k·s(e) ≤ 1 is
vacuous. Whether (1) such orthoadditive states exist and (2) whether one
could extend — where the relevant meet-zero families are infinite-dim
subspaces with trivial intersection, and σ-additivity OF THE STATE (not
of the lattice) is what bites — is the open sliver.

So the honest verdict is "no NORMAL state extends (clean, decisive); the
singular case is open", NOT "universal failure."

This script verifies the finite-dim core numerically: it builds k real
lines in R² ⊂ H, checks they are pairwise meet-zero, and confirms the
LP that asks for an extending charge is INFEASIBLE once k·s(e) > 1.
"""

import numpy as np
from scipy.optimize import linprog


def lines_in_plane(k, seed_angles=None):
    """k distinct lines in R^2, given by unit directions; return the lines
    and their perpendiculars as angle pairs in [0, π)."""
    if seed_angles is None:
        # generic distinct angles, avoiding coincidences p_i' = p_j
        seed_angles = [np.pi * (i + 1) / (2 * k + 3) for i in range(k)]
    lines = []
    for a in seed_angles:
        perp = (a + np.pi / 2) % np.pi
        lines.append((a % np.pi, perp))
    return lines


def all_distinct(lines, tol=1e-9):
    """Check the 2k lines {p_i, p_i'} are pairwise distinct (angles mod π)."""
    angles = [a for pair in lines for a in pair]
    for i in range(len(angles)):
        for j in range(i + 1, len(angles)):
            d = abs(angles[i] - angles[j]) % np.pi
            d = min(d, np.pi - d)
            if d < tol:
                return False
    return True


def extension_feasible(k, s_e):
    """LP: 2k pairwise-disjoint h-images carry masses s(p_i), s(p_i') with
    s(p_i)+s(p_i') = s_e and total mass over the whole space = 1, all ≥ 0.
    Feasible iff k·s_e ≤ 1. We solve it as an LP rather than trust the sum.

    Variables: x_1..x_{2k} (mass on the 2k disjoint h-images) + x_0
    (remainder = complement of their union). Constraints:
      x_{2i-1} + x_{2i} = s_e          (the pair sums, from (*))
      Σ all x = 1                       (charge normalisation)
      x ≥ 0
    """
    n = 2 * k + 1                       # x_0 plus 2k pieces
    A_eq, b_eq = [], []
    # pair-sum constraints: for pair i, x_{2i-1}+x_{2i} = s_e
    for i in range(k):
        row = [0] * n
        row[1 + 2 * i] = 1
        row[2 + 2 * i] = 1
        A_eq.append(row)
        b_eq.append(s_e)
    # total mass = 1
    A_eq.append([1] * n)
    b_eq.append(1.0)
    res = linprog(c=[0] * n, A_eq=np.array(A_eq), b_eq=np.array(b_eq),
                  bounds=[(0, None)] * n, method="highs")
    return res.success


def main():
    s_e = 0.3       # any normal state has some 2-plane e with s(e) > 0
    print(f"Fix a 2-dim subspace e with s(e) = {s_e}.")
    print(f"Clustering bound: extension needs k·s(e) ≤ 1, i.e. k ≤ {1/s_e:.3f}.\n")

    threshold = int(np.floor(1.0 / s_e))
    for k in range(1, threshold + 3):
        lines = lines_in_plane(k)
        distinct = all_distinct(lines)
        feasible = extension_feasible(k, s_e)
        predicted = (k * s_e <= 1 + 1e-12)
        flag = "ok" if feasible == predicted else "MISMATCH"
        print(f"  k={k:2d}: 2k distinct lines={distinct}, k·s(e)={k*s_e:.2f}, "
              f"extension feasible={feasible} (predicted {predicted}) [{flag}]")
        assert feasible == predicted, "LP disagrees with k·s(e) ≤ 1"
        assert distinct, "lines not pairwise distinct — pick other angles"

    k_kill = threshold + 1
    print(f"\nAt k={k_kill}, k·s(e)={k_kill*s_e:.2f} > 1: NO extending charge.")
    print("Uses only orthoadditivity on lines in ONE 2-plane; Gleason and")
    print("σ-completeness of the lattice never enter.")
    print("\n=> No normal (Gleason) state on L(H) extends. σ-completeness")
    print("   does NOT change this. Residue: singular states with s(e)=0 on")
    print("   every finite-dim e (clustering bound vacuous) — OPEN.")


if __name__ == "__main__":
    main()
