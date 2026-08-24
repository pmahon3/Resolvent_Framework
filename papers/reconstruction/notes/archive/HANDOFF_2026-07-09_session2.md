# Handoff — reconstruction / universal impossibility (2026-07-09, session 2)

Supersedes `HANDOFF_2026-07-09.md` (session 1, which took the paper through
Phase-4/5 and opened the UI attack). Working tree CLEAN, 7 commits this session
(`336e51c..404f306`) on branch `oml-descent-sigma-essential-reduction`. Nothing
pushed.

This session did four things: verified the owed Phase-4 backlog, reduced Joint 2 to
one named lemma, reskeletoned the paper, and opened the attack on that lemma's
easier half. Plus two housekeeping requests (reading-direction refs + reorg).

## What happened (7 commits)

1. **Phase-4: all 8 owed HAND proofs VERIFIED** (`336e51c`) — advisor-cross-checked
   on the subtle ones; all hold. 2 editorial fixes applied. Gate lemma verified +
   found VACUOUS for the size-2-window ring. Per-item verdicts in `STATUS.md`.
2. **Joint 2 REDUCED to one named lemma L-B** (`5fac082`) — the parity-only attack.
3. **Blast-radius sync** (`da3f2fa`) — persisted prior-session oracles, fixed stale
   scratchpad pointers.
4. **Paper RESKELETONED** (`2dc5a90`) — 10pp catalogue → 4pp architecture,
   payoff-first, every node status-marked. Old body archived + removed.
5. **Reading-direction note** (`2868fcf`) + **LaTeX conversion & reorg**
   (`39b1ce2`) — 4-field background refs; reading_directions/ now one subfolder
   per topic.
6. **Crossed-cycle exclusion opened** (`404f306`) — L-B's easier half, foundation
   verified.

## The paper right now

`papers/reconstruction/` — the PUBLIC FACE is now the SKELETON
(`reconstruction_skeleton.tex`, 4pp, builds clean). Payoff-first: reconstruction
guarantee = the target; C=R → why-hard → winding criterion → universal impossibility
= the dependency chain beneath it; interim results (parity, PR-box, ten tamings,
Circuit Localization) demoted to "instances of the winding criterion." Every node
STATUS-MARKED [PROVED]/[CLASSICAL]/[OPEN]/[SCOPE]. The proved body is preserved
verbatim in `notes/reconstruction_body_PROVED_ARCHIVE.tex` (578 lines, all 10
proofs); the old `reconstruction_body.tex` removed.

Owed to fill the skeleton to a complete paper (all in skeleton §method):
(i) prove L-B or state it as the open problem; (ii) prove the winding-2→full-safety
bridge applies, or scope every boundary claim to winding-2; (iii) fold the archived
body back in as instances, ordered define-at-first-use.

## The reduction (where the whole thing sits)

```
Universal impossibility (tamings complete = no fork)
 ⟸ Joint 1 [pruning lemma, TR_k=LISC_k all k]        CLOSED
 ∧ Joint 2 [parity-only]:
     ⟸ L-A [balance ⟺ safe-on-evens]                 PROVED (s.c. bar-D)
     ∧ L-B [primitive ⟹ G diagonal-or-full]          OPEN ← the target
          ├─ exclude {(0,0),(1,0)}: crossed cycle     ATTACK OPEN (this session)
          └─ exclude {(0,0),(0,1)}: bar-D aperiodic   OPEN (the hard half)
 ∧ [winding-2 → full-safety bridge]                   spot-checked, not proved
```

**Validated object** (1600 langs 0-mismatch): unsafe at L ⟺ a 2-fold cover of the
layer cycle closes with SWAP MONODROMY after L ⟺ the unordered-pair graph bar-D,
signed by monodromy+1, is UNBALANCED. This is the intrinsic re-derivation of the
parity mechanism (shadow of det(I+P)=1−(−1)^L) — NOT a new taming.

**R1 backbone** (non-circular): A=3 + A=4 FULL enumeration, ~25,700 primitives, 0
counterexamples to primitive + infinite-safe ⟹ safe exactly on evens.

## The live edge — crossed-cycle exclusion (L-B's easier half)

**Target (verified well-posed):** primitive + s.c. ρ ⟹ a crossed cycle exists in
bar-D ⟹ **primitive ⟹ NOT-safe-at-all-L**, turning "no safe-on-odds language
exists" into a theorem. A clean win = HALF of L-B + that corollary.

**Foundation LOCKED (verify-first, all passed):**
- crossed-cycle (D-reachability (a,b)⇝(b,a)) ⟺ NOT-safe-at-all-L: 0 mismatches,
  A=3 FULL. Reframe EXACT.
- Kronecker lever HOLDS: D = ρ⊗ρ off-diagonal; primitive ρ ⟹ ρ⊗ρ strongly connected
  on ALL ordered pairs (0 failures/139, matrix-power verified).

**Retarget (the lever buys this):** (a,b) already reaches (b,a) in the full product;
the ONLY content is that some such path can AVOID THE DIAGONAL. So:
  **primitive + s.c. ⟹ some off-diagonal (a,b) reaches (b,a) by a ρ⊗ρ-path never
  touching a diagonal vertex.**

**NEXT MOVE (the whole proof, probably):** find the ROUTING GADGET on the simplest
witness. "No crossed cycle" = every swap-route forced through the diagonal (threads
must collide to swap) = a rigidity; pure permutations are imprimitive, so
primitivity with ≥2 states already excludes determinism. Primitivity = arcs beyond a
single cycle = a fork/branch that lets one thread detour while the other passes.
Find that fork by hand; that is likely the argument.

## Discipline notes (carry forward — do not lose)

- **Confirmation-bias guard is ON, and cuts BOTH ways.** This session: 3 catches
  where a clean hypothesis dissolved wrongly (bipartite-layered-ring tautology; 2
  closure coding bugs; L-A disconnected-bar-D case), AND 1 REVERSE catch — my first
  crossed-cycle script manufactured a PHANTOM obstruction ("5 tensor failures") from
  a buggy inline reverse-reachability; independent matrix-power re-impl cleared it to
  0. Lesson: a sloppy check fabricates phantom cracks just as easily as phantom
  confirmations. Re-verify load-bearing checks with an INDEPENDENT implementation.
- **Raw-DFS LISC / matrix-power = ground-truth oracles.** Derived detectors
  (signed_balance, G-image) are convenient but have already been wrong; the derived
  ones get validated against the raw ones, never trusted alone.
- **SCOPE fence: everything is winding-2** (lisc2_raw). Full safety needs the
  Joint-1 bridge, spot-checked (kmax=3 on 9 witnesses + golden-mean calibration)
  but NOT proved. Do not claim full-safety parity-only until the bridge is proved.
- **L-A caveat:** proved for STRONGLY-CONNECTED bar-D; the disconnected case is a
  spelled-out per-component obligation, not automatic (caught by verify-by-building).

## Oracles (persisted, notes/unsorted/)

- `parity_only_z2_balance.py` — balance/G-type detector + safe-on-evens oracle
- `parity_only_swap_monodromy.py` — validated winding-2 = swap-monodromy (1600 langs)
- `parity_only_witness_channel.py` — non-circular R1 enumeration
- `joint2_wielandt.py`, `joint2_deep.py`, `joint2_fork_hunt_scale.py` — prior-session
  Wielandt/fork oracles
- `pruning_lemma_fine.py::LISC_windings` — the general-k winding oracle (bridge check)

## NAV

- Attack detail: `notes/unsorted/joint2_wielandt_finding.md` (the hub — L-A proof,
  L-B reduction, crossed-cycle foundation all here)
- Taxonomy: `notes/unsorted/universal_impossibility_taxonomy.json`
  (open_crux.forcing_lemma_LB is the node)
- Parent: `notes/unsorted/commensurability_taxonomy.json`
- Paper: `papers/reconstruction/reconstruction_skeleton.tex` + `notes/STATUS.md`
- Background reading: `notes/reading_directions/reconstruction/` (LaTeX + md)
- Lean env: `export PATH=$HOME/.elan/bin:$PATH; cd formalization/QuerySystem; lake env lean QuerySystem/<file>.lean`

## Blast-radius (verified clean this session)

Git clean, 7 commits. All 12 JSON valid. Skeleton builds 4pp 0-undefined; reading
doc builds 4pp all cites resolve. Lean WindingInjectivity + WindingDichotomy compile
0-sorry standard axioms. Oracles run standalone + golden-mean calibration passes.
Reading-direction reorg: 6 cross-refs fixed, all resolve. Memory hot-path trimmed
(flagship line 2719→2159) + reading-plan pointer updated to new subfolder.
