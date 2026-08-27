# LISC as a root of unity on the k-point configuration space

**Seeded 2026-08-26.**

**Claimed type(s):** Type 5 (impossibility). **Bar:** must close off an active
direction or sharpen it non-trivially — here, the proposal to generalize the
pruning theory to an infinite alphabet / the reals. Secondary: Type 3 (unifying
framework). **Bar:** must enable method transfer, not analogy — the LISC ↔
spectral reading has to let a statement move between the pruning lane and
ergodic theory, not merely rhyme with it.

## The question this came from

Is `LISC_k(L)` the symbolic shadow of a k-th root of unity in the Koopman
spectrum, and if so, is it worth generalizing pruning from a finite alphabet to
the reals?

## Three findings, in order of confidence

### 1. The single-cycle lemma (proved by hand, anchored computationally)

Traverse a simple cycle of length `m` in `D = (A, ρ)`. In the layered ring
`R_L`, the layer-`i` states are `{i + jL mod m}`, so by CRT the walk is simple
and closes after `lcm(m, L)` steps with winding

```
k = m / gcd(m, L)          -- the order of L in Z_m
```

So a cycle of length `m` certifies `LISC_k(L)` with that `k`, and `k ≥ 2`
exactly when **m ∤ L**. This *is* the root-of-unity statement: the lag-`L` map
on a period-`m` orbit has order `m/gcd(m,L)`.

Anchored against the repo's own trusted oracle (`raw_lisc_windings`, the
`safe_rho_instrument.py` lineage, extracted verbatim — the instrument itself is
POSIX-only): **0 unsound cases** over all 16 relations at |A|=2, all 512 at
|A|=3, and 300 sampled at |A|=4.

### 2. It is NOT an iff, and the failure is exactly nondeterminism

The converse fails often — exact in 340/512 at |A|=3, 201/300 at |A|=4. Minimal
counterexample:

```
ρ = {(0,0), (0,1), (1,0), (1,1)}      simple cycle lengths {1, 2}
single-cycle prediction   {1, 3, 5, 7}
actual Unsafe             {1,…,8}
unexplained               {2, 4, 6, 8}     all with winding exactly 2
```

At `L = 2` no single cycle has `m ∤ L`, yet winding 2 exists: the layered-ring
cycle puts one strand on the 0-loop and another on the 1-loop. They stay
distinct because they are *different orbits*, not because one orbit fails to
close.

### 3. The unification, and the dichotomy that follows

`TR_k^{(1)}(L)` says some injective k-tuple `u` has a length-`L` walk in `T_k`
to `σ(u)`. So `u` is a periodic point of the **k-point configuration dynamics**
whose lag-`L` map acts as a k-cycle — the same root-of-unity statement, one
level up. Confirmed per-k (not merely on the union) against the oracle: **0
mismatches** over 16 + 512 + 120 relations.

Now compute. Let `S = T^L` and `F = σ^{-1} ∘ S^{×k}`. A fixed point satisfies

```
u_j = S u_{j+1}
```

**If ρ is a function**, that forces `u_j = S^{-(j-1)} u_1`: every strand lies on
one orbit, and the condition collapses to `m/gcd(m,L) ≥ k` — finding 1.
**If ρ is a relation**, branching lets the strands sit on different orbits and
nothing collapses.

Checked: single-cycle prediction is **exact on 287/287 functional ρ**
(|A| = 2, 3, 4 exhaustively) and incomplete on 173 non-functional ones.

## What this closes

**The reals question, for deterministic dynamics, is closed.** For a map `T`
the configuration story provably reduces to the point spectrum of `T`, i.e. to
Halmos–von Neumann: `T^L` fails to be ergodic exactly when `T` has a nontrivial
`L`-th root of unity as an eigenvalue, and the space splits into `d | L`
cyclically permuted pieces. Generalizing pruning to ℝ *for a map* would
rediscover that. Not worth doing.

This also explains, rather than merely records, the earlier observation
(`RelationalDelay.lean` docstring) that specialising pruning to a deterministic
ρ trivialises it. Determinism is not incidentally unhelpful; it collapses the
configuration space onto a single orbit.

**Theorem B separately dies over an infinite alphabet** and that finding stands
independently: both pigeonholes are load-bearing (`le_card_of_isLISC`'s k-cap,
and the finite tuple digraph behind `isEvPeriodic_isTR`), and
`ρ =` disjoint cycles of lengths `{2ⁿ}` over `A = ℕ` gives
`Unsafe = {powers of 2}`, which has unbounded gaps and so is not eventually
periodic.

## What survives as a live direction

The genuinely non-classical object is the twisted product on the k-point
configuration space of a **relation**, not a map — set-valued / nondeterministic
dynamics. The continuum version of that is a closed relation on a compact space
(a correspondence), which is subshift/correspondence territory rather than
single-operator spectral theory. Whether *that* has content is the open
question; this seed does not settle it.

## Literature status — INCOMPLETE, do not name anything yet

Checked and confirmed classical: the `T^n`-ergodicity / root-of-unity criterion,
Halmos–von Neumann discrete-spectrum theory, cyclic decomposition of `L²`.
Searched without a direct hit: the injective-k-tuple tensor-power digraph with a
rotation endpoint; nearby literature exists in synchronizing-automata and
completely-reachable-automata work, which was not run down.

`papers/reconstruction/notes/PRIOR_ART_VERDICT.md` covers the polytope /
commensurability side and the winding criterion; it does **not** cover this
framing, so nothing here duplicates its record — but nothing here has had a
real prior-art pass either. The k-tuple-digraph object in particular smells like
it is known under another name.

## What would clear the bars

- **Type 5**: the deterministic collapse is the closure, and it is a two-line
  computation once the twisted product is written down. It needs a written proof
  and, if it is to be claimed, a check that the collapse is not itself folklore.
- **Type 3**: transfer would mean using the configuration-space reading to move
  a *theorem*, not a vocabulary — e.g. deriving Theorem B's eventual periodicity
  from a spectral finiteness statement, or conversely getting a symbolic
  statement out of a joining-theoretic one. Not attempted.

## Reproduction

`papers/reconstruction/oracles/lisc_configuration_check.py` — one runnable
file, all three checks (C1 soundness, C2 configuration-space equivalence, C3
the deterministic collapse). It lifts `raw_lisc_windings` verbatim from
`safe_rho_instrument.py` at import time rather than re-deriving it, so no claim
here rests on a second LISC implementation. (`safe_rho_instrument.py` itself
cannot simply be imported on Windows: it installs a SIGALRM handler at import.)

Last run 2026-08-26: C1 unsound 0/828, C2 mismatches 0/648, C3 exact on
287/287 functional rho.
