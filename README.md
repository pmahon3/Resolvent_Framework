# Structure from Observation

## Status (2026-07-10)

**Active flagship: reconstruction/commensurability** (`papers/reconstruction/`)
— EA/PR(𝓡) structure theory proved; universal-impossibility attack live.
**σ-essential** (`papers/sigma_essential/`) — the OMP form is a
machine-checked ZFC theorem (0-sorry Lean witness); paper dissemination-ready.

Authoritative state: `notes/programme/program_overview.md`.
Open-problem map: `notes/programme/frontier_map.md`.
Work plan: `notes/programme/shovel_plan.md` (four theorems + vacant lots).
Zoom-out navigation: `notes/taxonomies_index.json` (load FIRST).

### Papers

- **reconstruction** — ACTIVE flagship; skeleton public face, Type-6 bridge.
- **sigma_essential** — Ψ machine-checked; dissemination-ready.
- **spine** — corpus-level umbrella (reference-only, reads the three
  transitions as one classification).
- **Paper I** — audited, fixed honest, PARKED (no submission).
- **Paper II** — audited, revised: the survivor (Type-6 clears).
- **Paper III / fibre mixing** — withdrawn/dead, in `papers/archive/`.

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
