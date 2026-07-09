# reconstruction paper — status

Created 2026-07-08. The formal write-up of the reconstruction / commensurability
structure theory (successor programme to the σ-essential witness).

## Scope (skeleton + proved core drafted)
- **Proved core, drafted at LaTeX quality:** framework + C=R geometry (§1);
  trichotomy (§2, free/acyclic + product + De Loera–Onn universality);
  parity theorem (§3, with PR-box corollary); taming catalogue + signable
  theorem + forest-counting + **symmetric Circuit Localization** (§4);
  winding characterisation + **Lean-certified layer-injectivity discriminant**
  (§5).
- **Fenced as conjecture (NOT claimed proved):** universal impossibility
  conjecture + pruning lemma + the named k=2 phase gap (§6).
- **Consequences:** reconstruction guarantee, scoped to the tame classes;
  one-phenomenon-three-faces tie to Paper II + σ-essential (§7).
- **Method note:** verdict-grade discipline + Lean certification (§8).

## Provenance
All statements extracted faithfully from
`notes/unsorted/commensurability_classification_seed.md` (§§1, 2.2f, 2.2s,
2.2t, 2.2x–2.2z, 3) and the taxonomy
`notes/unsorted/commensurability_taxonomy.json`. Lemma 2 =
`formalization/QuerySystem/QuerySystem/WindingInjectivity.lean`.

## NOT YET DONE (owed before any submission)
- **Full proofs.** §§2–5 carry proof *sketches*; the complete proofs live in the
  seed rounds and must be written out and audited (Phase-2 `/audit full`).
- **Prior-art compare step.** The derive-then-compare shelf (§3 of the seed:
  Vorob'ev, Kellerer, junction trees/GYO, CSW, SPGT, Bulatov–Zhuk, etc.) is
  only partially cited; a hostile prior-art pass is owed, especially on the
  trichotomy (marginal-problem folklore) and the tamings (TU / König / perfect
  graphs).
- **The k=2 pruning residual** stays open; §6 must not harden into a proof
  until it is settled structurally.
