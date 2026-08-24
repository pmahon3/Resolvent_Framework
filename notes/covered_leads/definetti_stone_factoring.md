# Stone Spatialization of the Yosida-Hewitt Decomposition

> **✎2026-08-22.** This note is not a dead end after all — it describes the
> decomposition that underlies the settled picture. Mass on principal
> ultrafilters is the σ-additive part; mass on non-principal ultrafilters is the
> purely finitely additive part. What was resolved is which side you are
> entitled to: with completed countable queries the free part vanishes and you
> get `stone_observational_extension`; without them the free part is genuinely
> there and the right theorem is `stone_measure_exists`, the finitely additive
> one. Neither hypothesis is dispensable — Andersen–Jessen kills the
> valuation-layer condition alone, `counterexampleQS_no_finitary_condition`
> kills the index-layer condition alone, and `ce_independence` shows the two are
> independent. See the blueprint, `rmk:extension-repaired`.

## Summary

The Stone construction spatializes the Yosida-Hewitt decomposition.
For a shift-invariant finitely additive charge on a cylinder algebra,
the Stone measure μ̂ on St(C) decomposes into mass on principal
ultrafilters (the σ-additive part) and mass on non-principal
ultrafilters (the purely finitely additive part).  Each piece is
known; the combination is an observation, not a theorem.

## The exchangeable case (dead end)

Exchangeable charges on {0,1}^ℕ are automatically σ-additive by
the Hausdorff moment problem.  The mixing measure λ on [0,1] gives:

  ℓ(E) = ∫₀¹ Ber(p)(E) dλ(p)

Each Ber(p) is σ-additive; dominated convergence gives σ-additivity
of ℓ.  The Stone factoring reproduces classical de Finetti trivially.

**Exchangeability is too strong.  No exotic part exists.**

## The stationary case (observation, not theorem)

Shift-invariant charges can be purely finitely additive.  Banach
limits are the classical example.  The Doeblin condition for Markov
chains is equivalent to the absence of purely finitely additive
invariant measures (Zhdanok 2018, 2023).

The Yosida-Hewitt decomposition commutes with the shift:
- ℓ = ℓ_c + ℓ_p, both shift-invariant (Yosida-Hewitt 1952)
- On St(C): μ̂ = μ̂_c + μ̂_p
  - μ̂_c supported on pure(Ω) — classical stationary measure
  - μ̂_p supported on non-principal ultrafilters — the exotic part
- Both are shift-invariant on St(C)

This is the Stone representation of the Y-H decomposition applied to
the shift action.  Each ingredient is standard; the spatialization
is implicit in anyone who knows both Y-H and Stone duality.

## The real open question

What are the extreme points of the purely finitely additive
shift-invariant charges?

The σ-additive extreme points are ergodic measures — classical.
The purely finitely additive extreme points are... what?

This connects to the structure of the space of Banach limits (known
to be enormous — non-separable in norm), but its ergodic-theoretic
interpretation is genuinely unexplored.

**Question:** Is there a "purely finitely additive ergodic theorem"?
What does ergodic decomposition look like for the exotic part of μ̂?

## Assessment

| Component | Status |
|-----------|--------|
| Exchangeable case | Dead end (σ-additivity forced) |
| Y-H + Stone spatialization | Observation, not theorem |
| Doeblin ⟺ no exotic invariant measures | Known (Zhdanok) |
| Ergodic theory of purely f.a. part | Open, genuinely unexplored |

**Verdict:** The spatialization observation is worth a remark in a
future paper, not a paper in itself.  The ergodic theory of the
purely finitely additive part is a genuine open question but requires
substantial new ideas — not currently in reach.

## References

- Yosida & Hewitt 1952 (canonical decomposition)
- Zhdanok 2018 (arXiv:1804.02787), 2023 (MDPI Mathematics)
- Banach limits: Sucheston 1967, Lorentz 1948
