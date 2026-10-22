# Structure and Observation

## Status (2026-10-16)

**Aim: build new mathematical theory.** Problems are probes placed at seams
between existing theories. This theory-first orientation replaces the earlier
problem-first one.

**Theory in construction: pointless coherence on glued carriers.** When can
locally coherent views, glued around a loop, form a whole with no points, not
even ideal ones?
- Note: `notes/open_questions/cyclic_marginal/pointless_coherence.pdf` (opens
  with the window puzzle).
- Index: `notes/open_questions/cyclic_marginal/glued_carriers_taxonomy.json`.

**Two sides of the seam:**
- **Cycle side** (`papers/reconstruction/`): the fixed-length winding criterion is
  prior art (Kharoof–Ipek–Okay 2024) and is cited; the open core is the reach
  lemma.
- **Infinity side** (`papers/sigma_essential/`): the ZFC witness is
  machine-checked. A countable witness on every ring L ≥ 4 is Lean-checked, with
  no owner found after three prior-art passes.

Authoritative state: `notes/programme/program_overview.md` (2026-10-16
addendum). Zoom-out navigation: `notes/taxonomies_index.json` (load FIRST).
`frontier_map.md` and `shovel_plan.md` are stale (August 2026).

### Papers

- **reconstruction**: cycle side. Skeleton (5pp), with the fixed-L criterion
  cited. Claimed open core: the reach lemma.
- **sigma_essential**: Ψ machine-checked; dissemination-ready.
- **spine**: corpus-level umbrella (reference-only).
- **Paper I**: audited, fixed honest, PARKED.
- **Paper II**: audited, revised: the survivor (Type-6 clears).
- **Paper III / fibre mixing**: withdrawn/dead, in `papers/archive/`.

## Repository structure

```
Resolvent_Framework/
├── .claude/
│   ├── agents/           ← 6 custom agents
│   └── skills/           ← /audit skill
├── papers/
│   ├── reconstruction/   ← ACTIVE flagship (+ notes/ hubs, oracles/)
│   ├── sigma_essential/  ← Ψ witness paper (+ witness_candidate/ records)
│   ├── spine/            ← corpus umbrella (reference-only)
│   ├── paper_i/          ← synthesis (parked)
│   ├── paper_ii/         ← EA/PR/VDR (survivor)
│   └── archive/          ← withdrawn/canned/dead papers
├── formalization/
│   └── QuerySystem/      ← Lean 4 / Mathlib
└── notes/
    ├── taxonomies_index.json ← zoom-out registry (load FIRST)
    ├── open_questions/   ← precise, open, dormant
    ├── covered_leads/    ← known results + dead leads (reference)
    ├── unsorted/         ← Tier-3 pile (needs assessment)
    ├── knowledge_map/    ← research control panel
    ├── reading_directions/ ← guided reading with questions
    ├── literature_review/ ← lit review + PDF library
    ├── conceptual_sketches/ ← informal sketches
    ├── programme/        ← program_overview + frontier_map + shovel_plan
    └── archive/          ← dead ends and superseded
```

## Lean formalization

`formalization/QuerySystem/` — source of truth is `#print axioms` on each
certificate. Key certified results: `psi_ZFC` (σ-essential, 0-sorry), `WindingInjectivity` + `WindingDichotomy` (reconstruction,
0-sorry, classical flow-decomposition axiomatized). Paper-I
`StoneDualityExtension` carries 1 sorry (Yosida–Hewitt).
