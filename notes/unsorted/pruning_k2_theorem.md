# Pruning lemma at k=2: TR₂ = LISC₂ is a theorem (unconditional)

**Date:** 2026-07-09. **Status:** proved (⟦HAND⟧, round-trip verified by building
against raw-DFS oracle; layer-order step is a graph property, not instance-luck).
**Scope:** closes the k=2 case of the pruning lemma. Does NOT close the pruning
lemma (k≥3 open) and does NOT close universal impossibility (second joint —
eventual-periodicity ⟹ taming-forced — is separately unestablished).

## What the pruning lemma is (context)

Universal impossibility (the fork does not exist) is intended to reduce, via
eventual periodicity of the unsafe set, to the **pruning lemma**: TR_k = LISC_k
cofinitely, where
- **LISC_k(L)** = ∃ layer-injective simple cycle of winding k on the layered ring
  over ℤ_L (a closed walk of length kL, each layer visited in k *distinct* states,
  all kL vertices distinct).
- **TR_k(L)** = ∃ diagonal-avoiding tuple-rotation walk in the k-fold tensor
  power (the phase-agnostic proxy that admits a clean eventual-periodicity proof).

The seed flagged (2.2z) a "phase gap" in the k=2 reduction: the lockstep-exchange
model demanded an illegal 0→0 step and MISSED real simple cycles.

## The resolution: lockstep-exchange was the wrong proxy; TR₂-as-reachability is right

The k=2 object is **two winding-1 PATHS (not closed configs) that swap endpoints**.
A simple winding-2 cycle W (length 2L) splits at its two visits to layer 0 into
- strand P = W[0..L], a path s₀ → s_L,
- strand Q = W[L..2L], a path s_L → s₀.
Neither closes alone; they close *jointly*. (This is why the earlier probe — which
searched for two disjoint *closed* configs — found none when LISC held: it searched
a set the witnesses were never in.)

**Key structural fact (graph property, not DFS artifact):** the layered graph has
arcs only (i,a)→(i+1,b). So every walk advances its layer by exactly 1 each step;
step k sits on layer (start+k) mod L. Hence steps i and i+L share layer i, and the
two visits to layer i by a winding-2 cycle are exactly W[i], W[i+L].

**TR₂ ⟺ LISC₂, both directions, constructive:**
- **LISC₂ ⟹ TR₂.** From simple W set P[i]=W[i], Q[i]=W[i+L] (i=0..L). Both follow
  rel (W does). Simplicity ⟹ W[i]≠W[i+L] ⟹ P[i]≠Q[i] (off-diagonal is FORCED, not
  assumed). W[2L]=W[0] and W[L] give the swap P[L]=Q[0], Q[L]=P[0]. ⟹ TR₂ witness.
- **TR₂ ⟹ LISC₂.** From strands P,Q concatenate W = P[0..L−1], Q[0..L−1] (closing
  Q[L]=P[0]). Distinct within each strand (distinct layers) and across (P[i]≠Q[i]
  by off-diagonal) ⟹ all 2L vertices distinct ⟹ simple.

**No phase gap at k=2** because the only way to pair two strands is the swap
(P[L]=Q[0], Q[L]=P[0]) — a single transposition, no permutation freedom.

## Verification (by building, raw-DFS = ground truth)

`scratchpad/k2_extraction_test.py`: for targets {adv1, adv5, gm, rho13, full2,
perm3} × L=3..11, extract P,Q from every raw LISC₂ witness (check off-diagonal +
rel + swap) and rebuild W from every TR₂ witness (check genuine simple w2 cycle).
**Round-trip holds on ALL cases, zero failures.** (First run failed on an off-by-one
in my extraction — P[L] must be W[L] not W[0]; fixed, then clean.)

## k ≥ 3 RECONCILED: the pruning lemma holds for ALL k (no permutation gap)

**Result (2026-07-09):** TR_k = LISC_k for every k, by the SAME structural argument
as k=2. The feared "permutation-threading freedom" at k≥3 is a RELABELLING
ARTIFACT, not a real degree of freedom.

**The reconciliation.** A winding-k simple cycle W (length kL) splits into k
strands by wrap: slot j = W[jL .. (j+1)L]. Label strands by TRAVERSAL ORDER around
the single cycle. Then:
- the layer-i tensor tuple τ_i = (W[i], W[L+i], ..., W[(k−1)L+i]) has each slot
  following rel (W is a closed walk, wrap boundaries are rel-arcs);
- off-diagonal at every layer i: simplicity ⟹ the k visits to layer i are distinct
  ⟹ τ_i entries distinct;
- **τ_L = cyclic-rotation of τ_0 BY CONSTRUCTION** of the wrap indexing (slot j ends
  at the start of slot j+1).
So every LISC_k witness IS a diagonal-avoiding *cyclic-rotation* tensor walk. A
"non-cyclic k-cycle threading" is the same simple cycle under a different arbitrary
strand-labelling — no invariant distinction. The cyclic-rotation proxy already
captures all of LISC_k.

**⚠ PRECISION (defect caught + fixed): the proxy is rotation-by-a-GENERATOR, not
"any rotation".** Rotation-by-r with gcd(r,k)=d>1 threads the k slots into d cycles
of winding k/d — that witnesses LISC_{k/d}, NOT LISC_k. So TR_k(any-rotation)
OVERCOUNTS. Only rotation by r with gcd(r,k)=1 (canonically **r=1**) gives LISC_k.
Discriminator (`scratchpad/reconcile_k3.py` rot-check): C4dir at L=2 has LISC₂=T,
LISC₄=F; TR₄(any-rotation) fires (via rot-2), TR₄(rot-1)=F=LISC₄. The theorem is
**TR_k(rot-1) = LISC_k**; "any rotation" is wrong and must not leak into the
eventual-periodicity count.

**Verified by building, both directions** (rot-1 proxy): on {full3, 2c3c, full4,
C4dir, C4+chord, diamond}, k∈{3,4}, L≤6 —
- LISC_k ⟹ TR_k(rot-1): every raw witness gives a valid diagonal-avoiding
  rotation-by-1 tensor walk (rel + off-diagonal + τ_L=rot₁(τ_0)), 0 failures;
- TR_k(rot-1) ⟹ LISC_k: every rot-1 tensor walk concatenates to a genuine simple
  winding-k cycle, 0 failures;
- LISC_k = TR_k(rot-1) on the discriminating targets (LISC₂≠LISC₄ separated).

**⟹ the pruning lemma TR_k(rot-1) = LISC_k is a theorem for all k, unconditional
and exact.** The seed's k=2 "phase gap" and the anticipated k≥3 "permutation gap"
were BOTH artifacts of wrong proxies (lockstep-exchange at k=2; slot-labelling
ambiguity at k≥3). ⟦HAND⟧, raw-DFS oracle = ground truth.

**Completeness of "Joint 1 closed" (three statements the reduction needs):**
1. **k ≤ |A|**: a winding-k simple cycle needs k distinct states per layer. So the
   unsafe set is the FINITE union ∪_{k=2}^{|A|} LISC_k.
2. **TR_k(rot-1) is eventually periodic in L**: standard finite-digraph fact
   (walk-lengths between two nodes of the fixed tensor power = eventually periodic
   union of APs; the "Wielandt-bounded" the seed named). Cited, not re-derived.
3. Finite union of eventually-periodic sets is eventually periodic ⟹ the unsafe set
   is eventually periodic = theorem-let B. **The seed's TR_k must be confirmed = the
   rot-1 object** for "closed" to rest on the matched definition (the seed's proxy
   is diagonal-avoiding tuple-ROTATION; rot-1 is the generator case — consistent,
   but confirm the seed never used a non-generator rotation).

**⟹ Joint 1 (pruning lemma) of universal impossibility is CLOSED** (⟦HAND⟧,
verification-passed). What remains for universal impossibility is Joint 2 (see
`joint2_wielandt_finding.md`): its crux = why non-symmetry forces primitive ⟹
cofinitely-unsafe. That is now the SOLE open core of the conjecture.

## Verification pass (2026-07-09) — the hard check, PASSED

Adversarial scan (`scratchpad`, reconcile_k3 rot-1 version): **4,144
strongly-connected languages (144 at |A|=3, 4000 sampled at |A|=4) × k=2..|A| ×
L=2..7 = 73,728 checks of LISC_k vs TR_k(rot-1 generators). ZERO failures.**
Includes the boundary k=|A| and the discriminating targets (C4dir etc. where
LISC₂≠LISC₄, so rot-1 vs any-rotation is separated). The seed's k=2 proxy
(`tr2_set` target = reach (b,a) = rot-1) confirmed = the rot-1 object, so "closed"
rests on the matched definition. Remaining trust = the constructive proof is
⟦HAND⟧ (not Lean); Lean is the natural durability step (finite, same structure as
the k=2 slated module). Standing counterexample-guard: raw-DFS LISC oracle.

## What remains open (do not overclaim)

1. **Pruning lemma at k≥3** — permutation-threading; TR_k vs LISC_k with the
   pairing freedom explicit. Evidence toward agreement (this probe + seed's L=35),
   no proof.
2. **Eventual-periodicity ⟹ a taming is forced** — the SECOND joint of universal
   impossibility, only "assumed" in the record (seed 2.2t design-lane attack via
   grading/potential/phase-code + Wielandt residue classes). Even a full pruning
   proof does not close the conjecture without this.
