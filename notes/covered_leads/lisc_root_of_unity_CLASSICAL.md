# LISC as a root of unity — PARKED, the mechanism is classical

**Date:** 2026-08-26.
**Question:** Is `LISC_k(L)` the symbolic shadow of a k-th root of unity, and is
the pruning theory worth generalizing from a finite alphabet to the reals?
**Verdict:** **KNOWN.** The reading is correct and the direction it closes is
real, but every load-bearing step is a classical fact. Claimed as Type 5
(impossibility); fails that type's explicit park condition — *trivial
consequence of known results*. Parked rather than reframed.

## The reading, and why it is right

Traversing a simple cycle of length `m`, the layer-`i` states in the layered
ring `R_L` are `{i + jL mod m}`, so the walk closes with winding

```
k = m / gcd(m, L)        -- the order of L in Z_m
```

giving `LISC_k(L)`, with `k ≥ 2` exactly when `m ∤ L`. Verified sound against
the lane's own oracle over 828 relations (0 unsound). And `TR_k^{(1)}(L)` reads
as: an injective k-tuple reaches its own cyclic rotation in `L` steps — a
periodic point of the k-point configuration dynamics whose lag-`L` map acts as a
k-cycle. Verified per-k, 0 mismatches over 648 relations.

## Why it is classical

1. **The layered ring is the categorical product `D × C_L`.**
2. **`C_m × C_L ≅ gcd(m,L) · C_lcm(m,L)`** — the standard component count for a
   direct product of directed cycles. Its winding is `lcm(m,L)/L = m/gcd(m,L)`,
   which is the "single-cycle lemma" verbatim. Checked for all `m, L ≤ 12`.
3. **Functional ρ ⟹ every closed walk is a repeated cycle** (a functional graph
   is rho-shaped: one cycle per component), so only single cycles contribute and
   the configuration story collapses onto one orbit. Elementary.
4. The resulting data — `gcd` of cycle lengths, cyclic classes — is the
   **period / index of imprimitivity** of Perron–Frobenius theory.

Separately, **Theorem B's eventual periodicity is the Boolean-matrix
index/period fact**: the Boolean matrix semigroup is finite, so `A^µ = A^{µ+λ}`
for some minimal `µ, λ`, hence `{L : TR_k^{(1)}(L)}` is eventually periodic and
the `k`-capped finite union is too. `pruning_theorem_and_B.md` already records
that its Lean proof "is the Boolean-matrix argument of §3(2) with the monoid
packaging removed."

## What this still settles (kept, as a record)

- **The reals direction is closed for deterministic dynamics.** For a map, the
  configuration story reduces to the point spectrum — Halmos–von Neumann.
  Generalizing pruning to ℝ *for a map* rediscovers textbook ergodic theory.
  The closure is real; it is just not a contribution.
- **It explains why determinism trivialises pruning.** Recorded in
  `RelationalDelay.lean` as an observation; the reason is (3) above — determinism
  collapses the configuration space onto a single orbit. Content lives in the
  nondeterministic case because branching is what lets strands sit on different
  orbits.
- **Theorem B dies over an infinite alphabet**, independently of the above: both
  pigeonholes are load-bearing (`le_card_of_isLISC`'s k-cap; the finite tuple
  digraph behind `isEvPeriodic_isTR`), and `ρ =` disjoint cycles of lengths
  `{2ⁿ}` over `A = ℕ` gives `Unsafe = {powers of 2}` — unbounded gaps, so not
  eventually periodic.

## What is NOT covered by this verdict

**Theorem P is untouched.** `LISC_k(L) ⟺ TR_k^{(r)}(L)` is about the digraph of
**injective** k-tuples, which is not a product of cycles — the injectivity
restriction is exactly what takes it outside the classical product formula. This
note kills the *spectral reading* as a contribution; it says nothing about the
pruning equivalence itself, whose prior-art standing is recorded separately in
`papers/reconstruction/notes/`.

Likewise the surviving live object — the twisted product on the configuration
space of a **relation** rather than a map — is not addressed here. It was not
searched, because the deterministic collapse made it moot for the reals question
that prompted this.

## Search record

Confirmed classical: `T^n`-ergodicity / root-of-unity criterion;
Halmos–von Neumann discrete spectrum; cyclic decomposition of `L²`; Boolean
matrix semigroup index and period; direct products of directed cycles
(`gcd` components of length `lcm`); Perron–Frobenius period / cyclic classes.

Adjacent, not run down: synchronizing- and completely-reachable-automata theory
(pair/power automata, distinguishability) is the nearest home for the
injective-tuple digraph. If Theorem P's novelty is ever pressed, that is where
to look first.

## Reproduction

`papers/reconstruction/oracles/lisc_configuration_check.py` — C1 soundness,
C2 configuration-space equivalence, C3 the deterministic collapse, all against
`raw_lisc_windings` lifted verbatim from `safe_rho_instrument.py`. Last run
2026-08-26: C1 unsound 0/828, C2 mismatches 0/648, C3 exact on 287/287
functional ρ.
