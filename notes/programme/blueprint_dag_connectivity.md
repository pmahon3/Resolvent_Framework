# What is missing that would make the blueprint a network

**Written 2026-08-25.** Measurement, not proposal. Answers: which nodes/results
are absent that currently keep the DAG a set of parallel chains rather than a
connected structure.

## AMENDMENT 2026-08-25 (tower): island 1 is closed

The descent-witness ladder is now in the blueprint. Blueprint declarations went
104 -> 115; the four `DescentWitness*` modules moved off the coverage baseline
(26 -> 22 uncovered).

Measured with `scratchpad/dagcheck.py` (a different parser from the one that
produced the numbers below, so compare the deltas, not the absolutes):

| | before | after |
|---|---|---|
| nodes | 98 | 110 |
| edges | 160 | 179 |
| components | 6 | 6 |
| MO2 component | **4** | **16** |

So the MO2 island is no longer a dead end — it is the 4-rung ladder
`def:mo2 -> def:l2n -> thm:star-finite -> def:navara-l2 -> thm:star-infinite`
with the consistency and closure legs hanging off it. What did **not** happen:
the component count is unchanged, and the ladder did not attach to the 28-node
ch4/ch5 body. Growing an island is not the same as connecting one. The
`\uses` edges all run *into* MO2, because that is the real dependency
direction — nothing in the σ-essential lane consumes `star_infinite`.

Two things found on the way in, both recorded because they change what the
nodes mean:

1. **The consistency model did not cover `L2.instOML`.** `DescentWitnessConsistency`
   realized the ten blockwise axioms using a bare `mOrtho` function, and its
   docstring claimed all eleven. But there was no product `OrthomodularLattice`
   instance anywhere in the library, so the eleventh axiom — that `L₂` *is* an
   OML — was unmodelled, and it is the one that gives `⊓`, `≤`, `ᗮ`, `⊥` in the
   other ten their meaning. Fixed by proving `instPiOrthomodularLattice`
   (products of OMLs are OMLs, coordinatewise) and identifying `mOrtho` with
   that structure's orthocomplement definitionally (`mOrtho_eq_ortho`).
   `axioms_consistent` now carries both as conjuncts. This is the standing
   hazard in its usual costume: everything compiled, and the gap was only
   visible by reading what the model did *not* say.

2. **`axiomcheck.sh` grew a citation-keyed allowlist** (`axiom_allowlist.txt`),
   because `star_infinite` rests on Navara's eleven cited axioms and the gate
   was absolute. The allowlist is not a weakening: an unlisted axiom still fails
   hard, an allowlist entry without a citation is a hard error, entries used by
   no node are reported as stale, and cited declarations are counted *separately*
   from closed ones so the number of things actually proved stays visible. The
   gate now reads `115 declarations: 113 closed, 2 cited, 0 uncited`.

Island 2 (the diagonal layer, 4 nodes) is untouched and still the next item.

---

## AMENDMENT 2 — 2026-08-25 (tower): island 2 is closed, and [B] is not what it looked like

### Island 2 (the diagonal layer) — closed

`AJNoExtension.cyl_iInter_empty` now routes through
`Diagonal.pi_inter_diag_eq_empty` instead of re-running the argument.
`grep 'Diagonal\.'` over the library no longer returns nothing.

The carrying map is the content: a coherent family is not a sequence, so
`ASM.toSeq ω : k ↦ (ω_k)_k` reads off the top coordinate at each level. The two
facts `pi_inter_diag_eq_empty` consumes come from different places, which is
what makes the reduction non-trivial rather than a rename — every entry lies in
its own `X k` by the subtype and needs no hypothesis at all, while constancy
needs *both* the coherence (coordinate `0` from level `i` down to level `0`) and
the base cylinders (coordinate `0` across to coordinate `i` at level `i`).

With the Lean routed, the blueprint edge `thm:aj-no-extension → thm:diag-empty`
became *true* and was added. Before the refactor it would have been a lie: the
prose described the argument the diagonal layer proves while the Lean proof did
it again by hand.

| | before | after ladder | after refactor |
|---|---|---|---|
| nodes | 98 | 110 | 110 |
| edges | 160 | 179 | 180 |
| components | 6 | 6 | **5** |
| diagonal island | 4 | 4 | **absorbed into 48** |

`ASM.AJ_no_extension_unconditional` still rests on `propext, Classical.choice,
Quot.sound` only. One edge, because one duplicated argument was removed.

### [B] `ReconstructionTheorem` — the stated rationale does not hold

The claim was that it "imports QuerySystem (covered) AND is imported by
DelayEmbedding (covered)", so a node would land *between* two things already in
the graph. Both ends fail, at the node level rather than the module level:

1. **Nothing is used from `QuerySystem`.** `ReconstructionTheorem.lean` imports
   `QuerySystem.QuerySystem` and references no declaration from it. The import
   is inert; there is no edge to ch0 to be had.
2. **The covered `DelayEmbedding` nodes do not depend on it.** The ten delay
   nodes in the blueprint are all query-system side (`delayQuery`, `delayEval`,
   `delayQuerySystem`, `not_seqUpperDirected`, the fixed-lag chain). The five
   declarations that *do* consume `ReconstructionTheorem` —
   `delayObservableAlgebra`, `delayObservableAlgebra_eq_comap`,
   `delayMap_shift_intertwining`, `delay_reconstruction_iff`,
   `delay_cyclic_implies_reconstruction` — are **none of them blueprint nodes**.

`DelayEmbedding.lean` is really two mathematically disjoint halves sharing a
file: the delay query system over `SensorStream X`, and a "Reconstruction
bridge" section over `(X, h : X → ℝ, T : X → X)`. They share no declaration.
Coverage cannot see this — it asks only that a module have *some* covered
declaration, so a module can be half-blueprinted and read as done.

So adding `ReconstructionTheorem` alone yields a **new sixth island**, which is
what the table below ranks as value "none". A real bridge needs a lemma
identifying the delay query system's `delayEval` with `delayMap` — i.e.
instantiating the sensor stream as an orbit `n ↦ T^[n] x` and the outcome space
as `ℝ` via `h`. That is mathematics and a modelling decision about whether the
query system's `X` is the state space or the observation space, not annotation.
Left for the human.

---

## The measurement

95 nodes, 127 edges, 1.34 edges/node. **Five connected components** (undirected):

| size | chapters | what it is |
|---|---|---|
| 43 | 0,1,2,3 | query systems → extension → Andersen–Jessen → delay |
| 27 | 4,5 | Boolean/orthomodular hinge → σ-essential witness |
| 17 | 6 | pruning / Theorem B |
| 4 | 2 | `def:diag-cylinders`, `lem:diag-inter`, `lem:diag-measurable`, `thm:diag-empty` |
| 4 | 4 | `def:oml`, `def:mo2`, `thm:mo2-oml`, `thm:mo2-gap` |

The two size-4 components are **orphan islands inside chapters that otherwise
connect**. Those are the sharpest signal: they are not separate subjects, they
are results whose consumers are missing.

## Island 1 — MO₂ (ch4). The missing rungs are FORMALIZED and outside.

`grep MO2` over the library: MO₂ is used by four modules, **none in the
blueprint**, forming a clean ladder:

```
OrthomodularMO2          (Rung 1)  ← IN the blueprint, as the island
  └ DescentWitnessFinite    (Rung 2)  115L,  8 decls, 0 axioms
      ├ DescentWitnessInfinite (Rung 3) 160L,  3 decls, 11 cited axioms
      └ DescentWitnessConsistency       110L, 12 decls, 0 axioms
          └ DescentWitnessClosure       113L,  5 decls, 0 axioms
```

Navara's construction (PAMS 115, 1992, p. 428) with MO₂ blocks: finite
truncation `L2N N = Fin N → MO₂`, then the infinite object `L₂`, then a
concrete model proving the Rung-3 axioms consistent, then three closure legs.
Culminates in `star_infinite` — the `(★)` property.

**This is the single highest-value addition.** It is ~500 lines of existing,
axiom-clean-except-cited Lean that would attach the MO₂ island to a real
chain, and it is the (β)-swap descent argument — the thing MO₂ exists to serve.
Adding it turns a 4-node orphan into a 4-rung ladder.

## Island 2 — the diagonal layer (ch2). Genuinely unused.

`grep 'Diagonal\.'` over the library returns **nothing**. `Diagonal.lean` is
consumed by no other module.

Note this is *not* the same as being unproved — the nodes are `\leanok` and the
axiom gate passes. The diagonal cylinders were built for the Andersen–Jessen
refutation, and when that landed (2026-08-24) `AJNoExtension` proved its own
`cyl_iInter_empty` directly rather than going through `Diagonal`.

So the fix here is a *Lean* change, not a blueprint one: either
`AJNoExtension.cyl_iInter_empty` should be refactored to consume
`Diagonal.pi_inter_diag_eq_empty`, or `Diagonal` should be recognised as
superseded. **Refactoring is the better call** — it would create a real
ch2-internal edge and remove a duplicated argument.

## The three big components — why they do not touch

- **43 (ch0–3) vs 27 (ch4–5).** Structural, not an oversight. Checked
  2026-08-24: no OML module imports ch0/ch1. `ConcreteOMLBlocks →
  SigmaEssentialAmended → SigmaEssentialLocalization → Mathlib`;
  `OrthomodularMO2 → Mathlib`. The σ-essential lane genuinely does not use the
  query-system core. A bridge would have to be *written*, not annotated.
- **17 (ch6, pruning).** Its own opening says it: "a separate line of work…
  sharing no definitions and no dependencies". Reconstruction lane. Honest.

## The uncovered modules that would ADD edges, ranked

Of the 26 uncovered modules, those whose imports reach something already in the
blueprint (so adding them yields immediate edges):

| module | imports | value |
|---|---|---|
| `DescentWitness{Finite,Infinite,Consistency,Closure}` | → `OrthomodularMO2` | **highest** — de-orphans MO₂, 4 rungs |
| `SigmaEssentialOpenCore` | → `SigmaEssentialLocalization` | high — Ψ/Φ open core, `TargetA_sharp`, the admissibility work |
| `ConcreteOMLBlocks`, `MarczewskiTransport`, `ConcreteOMLPatterns` | chain from `SigmaEssentialAmended` | high — the block/pattern layer, ~1700L axiom-free |
| `SigmaEssentialBareForm` | → `SigmaEssentialLocalization` | medium |
| `ReconstructionTheorem` | → `QuerySystem` | medium — would attach to ch0 AND is what `DelayEmbedding` imports |
| `EncodingDefectCheck`, `UlamWitnessReceipts` | → covered modules | low — receipts, not results |
| `BandClosure`, `Commensurability`, `FibreProductReflection`, `FiniteAtomFoldKernel`, `UltrafilterCharge`, `WindingInjectivity` | no project imports | none — would be new islands |

## What would actually make it a network

Ranked by edges-per-effort:

1. **The descent-witness ladder** (4 modules, already written). De-orphans MO₂
   and gives ch4 a real internal chain.
2. **`ReconstructionTheorem`.** It imports `QuerySystem` and is imported by
   `DelayEmbedding` — so adding it puts a node *between* two things already in
   the blueprint, converting a gap into a path. Cheapest real bridge.
3. **`SigmaEssentialOpenCore` + the block/pattern layer.** Large, axiom-clean,
   and it is where Φ/`TargetA_sharp` live — the open core the whole lane is
   about.
4. **Refactor `AJNoExtension` onto `Diagonal`.** Lean work, not blueprint;
   removes a duplicated argument and de-orphans island 2.

None of these bridges the 43/27 split — that one needs mathematics, not
annotation, and is the honest shape of the corpus.
