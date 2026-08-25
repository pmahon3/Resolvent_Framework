# What is missing that would make the blueprint a network

**Written 2026-08-25.** Measurement, not proposal. Answers: which nodes/results
are absent that currently keep the DAG a set of parallel chains rather than a
connected structure.

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
