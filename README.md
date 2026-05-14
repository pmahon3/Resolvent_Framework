# Structure from Observation

## Status after novelty audit (2026-05-13)

Rigorous skeptical audits of all papers and artifacts revealed:

- **Paper I** — known theorems with useful synthesis (not novel)
- **Paper II** — incremental, publishable at a philosophy venue if
  honestly framed (EA/PR/VDR vocabulary is novel; mathematics is not)
- **Paper III** — withdrawn (rediscovery)
- **Old Papers II+III** — withdrawn (classical results throughout)

Two active leads survive: the entropy characterization of
reconstruction and the fibre mixing condition.

## Active leads

1. **Entropy characterization:** δ(L) → 0 iff H₂(ν_L) → ∞ bridges
   Rokhlin distance to Rényi-2 entropy in delay reconstruction.
   See `notes/active_leads/entropy_characterization.md`

2. **Fibre mixing:** novel spatial non-degeneracy condition on fibres
   of delay maps, with open derivability question.
   See `notes/active_leads/fibre_mixing.md`

## Repository structure

```
Resolvent_Framework/
├── papers/
│   ├── paper_i/          ← Paper I (synthesis, ready but not novel)
│   ├── paper_ii/         ← Paper II (EA/PR/VDR, drafting)
│   └── archive/          ← all withdrawn/canned papers
├── formalization/
│   └── QuerySystem/      ← Lean 4 / Mathlib (1 sorry total)
└── notes/
    ├── active_leads/     ← 2 leads: entropy characterization, fibre mixing
    ├── covered_leads/    ← well-expressed known results (reference)
    ├── unsorted/         ← Tier 3 pile (needs individual assessment)
    ├── archive/          ← dead ends and superseded notes
    └── future/           ← fibre mixing source material
```

## Lean formalization

| File | Status |
|------|--------|
| QuerySystem.lean | ✅ 0 sorry |
| DiscriminabilityFoundations.lean | ✅ 0 sorry |
| StoneDualityExtension.lean | 1 sorry (Yosida-Hewitt) |
| UltrafilterCharge.lean | ✅ 0 sorry |
| Commensurability.lean | ✅ 0 sorry (1 axiom: KS) |
