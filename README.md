# Structure from Observation

## Status (2026-05-14)

**No active standalone leads.** All previous leads closed by audit.
Papers I and II are synthesis/positioning, not novel research.
Paper II (EA/PR/VDR, van Fraassen-to-duality) is the strongest
novelty zone.

### Papers

- **Paper I** — known theorems with useful synthesis (not novel).
  Expositiones target.
- **Paper II** — EA/PR/VDR vocabulary novel; math classical.
  Synthese target. Core thesis: "the realism/empiricism boundary
  is algebraic."
- **Paper III** — withdrawn (rediscovery)
- **Fibre mixing paper** — dead (bridge theorem false, disintegration
  error). Archived.

### Closed leads

- **Entropy characterization** — depended on bridge theorem (false).
  See `notes/covered_leads/entropy_characterization.md`
- **Fibre mixing** — bridge theorem false; replacement observation
  (geometric ≠ algebraic reconstruction) is known/obvious.
  See `notes/covered_leads/fibre_mixing.md`

### Seeds (unaudited, in notes/unsorted/)

- Excess Fisher curvature — likely known, needs Phase 2 audit
- CE as sheaf condition — stalled, needs fresh approach

## Repository structure

```
Resolvent_Framework/
├── .claude/
│   └── agents/           ← 7 custom agents (auditor, advisor, etc.)
├── papers/
│   ├── paper_i/          ← Paper I (synthesis, expository)
│   ├── paper_ii/         ← Paper II (EA/PR/VDR, strongest contribution)
│   └── archive/          ← all withdrawn/canned/dead papers
├── formalization/
│   └── QuerySystem/      ← Lean 4 / Mathlib (1 sorry total)
└── notes/
    ├── active_leads/     ← currently empty
    ├── covered_leads/    ← known results + dead leads (reference)
    ├── unsorted/         ← seeds + unassessed material
    ├── knowledge_map/    ← research control panel
    ├── reading_directions/ ← guided reading with questions
    ├── programme/        ← programme-level docs
    ├── archive/          ← dead ends and superseded
    └── literature/       ← literature reviews by topic
```

## Lean formalization

| File | Status |
|------|--------|
| QuerySystem.lean | 0 sorry |
| DiscriminabilityFoundations.lean | 0 sorry |
| StoneDualityExtension.lean | 1 sorry (Yosida-Hewitt) |
| UltrafilterCharge.lean | 0 sorry |
| Commensurability.lean | 0 sorry (1 axiom: KS) |
