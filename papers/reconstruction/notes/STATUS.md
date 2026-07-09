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

## PRIOR-ART VERDICT (2026-07-08, hostile scout — see PRIOR_ART_VERDICT.md)

**Headline: the polyhedral core is KNOWN; novelty is the observational/dynamical
layer + winding criterion + Circuit-Localization assembly. Contribution TYPE 6
(bridge/translation), clearing TYPE 3 only if parity/winding are unobtainable
without the EA/PR framework.** Must state this verdict IN the paper.

Per-result: R1 framework = Wainwright–Jordan LOCAL/MARG + Abramsky–Brandenburger
(known translation). 2a acyclic⟹tame = **Vorob'ev 1962** (drop "free theorem"
framing; do NOT cite Kellerer for the iff). 2c universality = De Loera–Onn +
**Průša–Werner 2013/2015** (exact-object universality, was OFF-SHELF). Parity =
Nemhauser–Trotter + Chvátal + Hoffman–Kruskal/König (mechanism classical; only
the golden-mean/recurrence dressing new). Tamings = TU/König/perfect-graph
renamed. R5 Circuit Localization = NOVEL assembly + winding criterion, but must
differentiate from **Thapper–Živný** (BLP-tight iff fractional symmetric
polymorphism — the tamings are plausibly its shadows), not just Barto–Kozik.

**Owed before drafting proofs (per-step cite-vs-prove now RESOLVED):**
- CITE-CLASSICAL (short reduction + citation, do NOT write original proofs):
  acyclic (Vorob'ev/BFMY), 2c universality (De Loera–Onn/Průša–Werner/Pitowsky),
  parity mechanism (Nemhauser–Trotter/Chvátal/Hoffman–Kruskal/König), signable
  (Hoffman–Gale-appendix/Ghouila-Houri/König), cliques+holes (SPGT/CCLSV/CSW).
- WRITE-ORIGINAL (genuinely ours): the EA/PR framing, the reduction lemmas
  (golden-mean homs⟺independent sets; marginal-determination affine lift), the
  **winding/primitive-orbit criterion + covering-space proof**, the
  Circuit-Localization assembly.
- MANDATORY CITATION FIXES: add Průša–Werner, Thapper–Živný, Leggett–Garg+NSIT,
  Vorob'ev, BFMY, Abramsky 2012, Nemhauser–Trotter, Chvátal, Hoffman–Kruskal,
  Ghouila-Houri, König, SPGT, CCLSV, Fine 1982. **Attribution landmine:
  signability⇒TU is the Hoffman–GALE APPENDIX to Heller–Tompkins 1956, NOT the
  main text — cite correctly or it gets caught.**
- SHELF GAPS to close: (1) Leggett–Garg/NSIT is the nearest competitor
  (temporal contextuality) — differentiate the cyclic-time/subshift-orbit
  reading explicitly. (2) Průša–Werner (exact-object universality).
- CONTRIBUTION-TYPE SELF-TEST to run: are parity + winding re-derivable directly
  in stable-set / graphical-models language? If yes → Type 6; if no → Type 3.
  Answer decides the paper's positioning.
