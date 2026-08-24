# Handoff — reconstruction / universal impossibility (2026-07-10, session 4)

Supersedes `HANDOFF_2026-07-10.md` (session 3, same day). This session took the
crossed-cycle attack from "mechanism pinned" to "**equivalence proved + gap
narrowed to one finite lemma**", via a third route that supersedes both options
(A) grading-construction and (B) same-grade-Kronecker that session 3 left open.

## Where the whole thing sits

```
Universal impossibility (tamings complete = no fork)
 ⟸ Joint 1 [pruning lemma, TR_k=LISC_k all k]        CLOSED
 ∧ Joint 2 [parity-only]:
     ⟸ L-A [balance ⟺ safe-on-evens]                 PROVED (s.c. bar-D)
     ∧ L-B [primitive ⟹ G diagonal-or-full]          OPEN ← the target
          ├─ exclude {(0,0),(1,0)}: crossed cycle     ← REDUCED to lock-avoidance lemma
          └─ exclude {(0,0),(0,1)}: bar-D aperiodic   OPEN (the hard half)
 ∧ [winding-2 → full-safety bridge]                   spot-checked, not proved
```

## What this session ESTABLISHED (all ⟦HAND⟧ + machine-verified)

**1. MASTER LEMMA + CONVERSE = EQUIVALENCE.** Crossed cycle exists ⟺ G has an
**antipodal-free even closed walk** (closed W, length 2m, W(t) ≠ W(t+m) ∀t).
Forward: ride W with two tokens offset m. Converse: concatenate the two halves
of the pair walk. The exclusion problem is now INTRINSIC to G — no pair digraph.
Machine-checked both directions (explicit D-path certificates + converse
construction asserted on every crossed lang, A=3 FULL + 4000 A=4).

**2. Corollaries: no-cross ⟹ no loops AND no even simple cycles** (so all simple
cycles odd ⟹ period odd). **The census law "no-cross ⟹ odd period ≥3" reduces
to the primitive case.** Predictions held on every no-cross lang: A=3 (2),
A=4 FULL (12), A=5 sample (4), n=6 period-3 hunt (124, first size with teeth:
6-cycles fit period-3 grading; 235/235 with an even cycle were crossed).

**3. Candidate-walk family explains 100% of primitives at A≤5** (A=4 FULL
25,575/25,575). Breakdown: even simple cycle ≈99.3%; shared-base two-odd-cycle
walk covers ALL the rest; **disjoint-cycles case NEVER needed**. Minimal hard
case C5+chord (cycles {3,5}, even-cycle-free) works at every base, laps (1,1).

## THE OPEN GAP (one finite lemma)

**Lock-avoidance lemma:** primitive (⟹ ∃ odd cycles of distinct lengths p≠q,
gcd 1, no loops, no even simple cycles under no-cross) ⟹ some shared-base walk
C_p^a·C_q^b is antipodal-free. For a=b=1, q>p, base x, the ONLY failure mode is
an index-locked shared vertex: C₂-index = C₁-index + (q−p)/2 exactly. Freedom:
base choice (shifts all index pairs), order, laps. p=q provably never works —
distinct lengths essential. Disjoint case likely unnecessary (never fired A≤5);
if needed, path-joined walks are in the oracle already.

Also available leverage: Thomassen even-dicycle theorem (strongly 2-connected ⟹
even dicycle ⟦from memory — VERIFY⟧) + Cor 1 ⟹ no-cross ⟹ not strongly
2-connected.

## OWED

- **HOSTILE prior-art scout before the paper touches this**: the equivalence is
  elementary and may be known (automata / symbolic dynamics / even-dicycle
  literature — Thomassen, McCuaig, Robertson–Seymour–Thomas territory).
- The lock-avoidance lemma itself (next session's target).

## DISCIPLINE (carried + earned)

- Advisor not consulted (down in session 3); all ⟦HAND⟧ claims machine-verified
  by an independent fresh implementation (`crossed_cycle_master_lemma.py` does
  not import the old oracle). Counts cross-validate session 3's census exactly.
- The certificate-checking assertions (`verify_swap_path`, `check_equivalence`)
  caught two real bugs during development. Never search without them.
- SCOPE fence unchanged: winding-2; full-safety bridge spot-checked, not proved.

## NAV

- Attack hub: `papers/reconstruction/notes/joint2_wielandt_finding.md` — "MASTER LEMMA"
  section at the end (proofs + oracle results + gap statement).
- New oracle: `papers/reconstruction/oracles/crossed_cycle_master_lemma.py` (run: `python3
  crossed_cycle_master_lemma.py all` — sweeps 3,4,5,6 + equivalence).
- Prior oracles: `papers/reconstruction/oracles/crossed_cycle_*.py` (ground truth unchanged).
- Taxonomy: `papers/reconstruction/notes/universal_impossibility_taxonomy.json`
  (`open_crux.forcing_lemma_LB`).
- Paper: `papers/reconstruction/reconstruction_skeleton.tex` + `notes/STATUS.md`.
- Lean env: `export PATH=$HOME/.elan/bin:$PATH; cd formalization/QuerySystem; lake env lean QuerySystem/<file>.lean`
