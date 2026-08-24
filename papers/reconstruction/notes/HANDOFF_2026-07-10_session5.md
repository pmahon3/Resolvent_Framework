# Handoff — reconstruction / universal impossibility (2026-07-10, session 5)

Supersedes `HANDOFF_2026-07-10_session4.md`. This session executed shovel-plan
step 1a and closed both owed debts: the **lock-avoidance lemma is PROVED**
(crossed-cycle branch of L-B closed) and the **hostile prior-art scout ran**
(equivalence + primitive⟹crossed not found; Thomassen citation from memory
was WRONG and is now corrected on record).

## Where the whole thing sits

```
Universal impossibility (tamings complete = no fork)
 ⟸ Joint 1 [pruning lemma, TR_k=LISC_k all k]        CLOSED
 ∧ Joint 2 [parity-only]:
     ⟸ L-A [balance ⟺ safe-on-evens]                 PROVED (s.c. bar-D)
     ∧ L-B [primitive ⟹ G diagonal-or-full]          HALF-CLOSED
          ├─ exclude {(0,0),(1,0)}: crossed cycle     ✅ CLOSED (session 5)
          └─ exclude {(0,0),(0,1)}: bar-D aperiodic   OPEN ← the remaining crux
 ∧ [winding-2 → full-safety bridge]                   spot-checked, not proved
```

## What session 5 PROVED (all ⟦HAND + machine-verified stepwise⟧)

**THEOREM.** Strongly connected G, no crossed cycle ⟹ no loops, all simple
cycles odd and ALL OF ONE LENGTH d = period(G) ≥ 3. Hence **primitive ⟹
crossed**; the census law "no-cross ⟹ odd period ≥ 3" is a theorem.

Via the **LOCK-AVOIDANCE LEMMA**: all-odd U with a shared distinct-length
cycle pair ⟹ some pair of odd cycles of distinct lengths works at laps (1,1)
from a shared base (antipodal-free even closed walk; laps/path-joins never
needed). Proof = minimal-sum pair + minimal-distance ordered kill + hybrid
peeling + the τ-equation endgame (τ(w) = τ(x_t) + δ turns any within-piece
killer into a SHORTER ordered kill of the original pair — contradiction).
Full statement + 9-step proof + refuted intermediates + oracle inventory:
`joint2_wielandt_finding.md` §"LOCK-AVOIDANCE LEMMA PROVED".

Supporting: chain-connectivity of simple cycles in strongly connected
digraphs (kills the disjoint case); kill symmetry; the exact (1,1) lock
analysis as an iff.

**Genuine stall structures exist and are in the record** — (5,15) s=4 and the
(9,27) class-ρ₀ family; they defeat the naive gap-descent and the clean-piece
repair, and are exactly why the endgame has its final form. Refuted
intermediates (M), P(a) documented in the hub — do not resurrect them.

## Prior-art scout (hostile, run 2026-07-10)

- Equivalence: NOT FOUND (closest: Gao–Shao 2009 double-vertex digraphs;
  Fernandes et al. arXiv:2410.20189 — both asynchronous, different objects).
- Primitive ⟹ crossed: with-diagonal layer classical (McAndrew 1963);
  diagonal-avoidance content NOT FOUND. Plausibly new.
- ⚠ **Thomassen correction**: "strongly 2-connected ⟹ even dicycle" is FALSE
  (Seymour's 7-vertex counterexample). Real theorems: Thomassen JAMS 1992
  (min degree ≥ 3 / strongly 3-connected); McCuaig JGT 2000 (unique strongly
  2-connected exception). Foundational structure for our hypothesis class:
  Seymour–Thomassen JCTB 1987. Full citations in the hub.
- OWED: paywalled full-text checks — Gao–Shao 2009; "Multi-agent pathfinding
  on strongly connected digraphs" (2025).

## Oracles (papers/reconstruction/oracles/, all asserts green)

`lock_avoidance_lemma.py` (glued-universe sweep + H1–H3),
`lock_avoidance_probe_M.py` (refutes (M)/P(a)),
`lock_avoidance_probe_descent.py` (sum-descent cases),
`lock_avoidance_probe_endgame.py` (step-9 dichotomy, provenance-aware peel),
`lock_avoidance_rho0_927.py` (exhaustive (9,27) stall territory).
Session-4 oracles unchanged and still ground truth for the equivalence.

## NEXT (per shovel plan §Execution order)

1. Remaining step-1 debt: **Paper II §4 reposition + 2 cites** (Stairs 1983
   Phil Sci 50:578; arXiv:2603.22353).
2. **Theorem 1** — pruning lemma phase-parametrized + theorem-let B.
3. The open crux of Joint 2 is now ONLY the bar-D aperiodic half
   (exclude {(0,0),(0,1)}). Thomassen-1992/McCuaig-2000 structure theory is
   the right imported leverage (correct citations now on record).
4. Optional bank-deepening: Lean formalization of the lock-avoidance chain
   (large; not gating).

## DISCIPLINE

- Advisor not consulted (sessions 3–5); compensated by per-step oracle
  asserts on exhaustive universes + one independent hostile scout.
- The endgame probe caught a real bookkeeping subtlety (D ∩ D' shared arcs ⟹
  provenance must be positional). The assert layer caught it. Keep it.
- SCOPE fence unchanged: winding-2; full-safety bridge spot-checked only.
- Do NOT recall any of this as Lean-certified.
