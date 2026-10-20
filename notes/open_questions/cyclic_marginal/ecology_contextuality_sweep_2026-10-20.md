# Ecology sweep: locally consistent, globally impossible field data (2026-10-20)

reviewed: false. One sonnet scout, about 24 searches. Verification level is given per item. CbD and
the contextuality papers already on the shelf were excluded.

## Verdicts

| Lead | Verdict | Verified |
|---|---|---|
| Aerts, Broekaert, Czachor, Kuna, Sinervo, Sozzo, "Quantum structure in competing lizard communities", *Ecol. Model.* 281 (2014) 38–51, arXiv:1212.0109 | **NEIGHBOUR, the only direct hit** | scout: full text; me: arXiv abstract |
| Ecology's own versions (co-occurrence null models, JSDMs, integrated SDMs, Simpson's paradox) | NOTHING FOUND that asks whether a joint *exists*. These build a joint in (JSDM, Hammersley–Clifford) or down-weight conflict | snippets |
| Ecological inference (Duncan–Davis 1953, Goodman 1953, King 1997) | NEIGHBOUR in mathematics (the marginal problem with bounds); a lens for data merging | snippets |
| Hajian-Forooshani, Perfecto, Irizarry, Vandermeer, *Ecol. Lett.* 2026, DOI 10.1111/ele.70415 | LENS: pairwise competition from two years of ant data fails to reproduce the community | abstract |
| Barendregt–Thomas, *J. Math. Biol.* 2023, arXiv:2111.05902 | **OWNS the finite-population cutoff for case 1b**, in words | scout: most of the full text |
| Stone–Holmes, *SIAM J. Appl. Math.* 50 (1990) 726–743 | OWNS the noise cutoff (finite mean recurrence time) | abstract/secondary |

## The lizard paper: what it does and the honest distance

- **What it does.** It uses the same side-blotched lizards as our note §9, with field data from
  Bleay–Comendant–Sinervo, *Proc. R. Soc. B* 274 (2007). It computes pairwise win/lose joint
  probabilities for morph pairs, reports a CHSH violation and a violated marginal law, and builds a
  Hilbert-space model with "entangled" competition states.
- **Caveats** (scout's reading, consistent with the abstract):
  - The joints are model-derived, and the paper says they "cannot be measured directly".
  - The scenario is compound two-lizard entities, not a loop of overlapping views.
  - A violated marginal law is what Contextuality-by-Default calls *direct influence*, not
    contextuality.
  - No n-cycle or LP existence test is run.
- **For us:**
  - **Part II must cite it.** Our lizard section reads the cycle as "coherent answers with no
    single world". Aerts et al. made a nearby claim with data in 2014.
  - The honest open move is a **proper test**: a contextuality-by-default or n-cycle LP
    feasibility test on the Bleay et al. data, if the data are available. That would be a new case
    in our sense. Data availability is unconfirmed.

## Case 1b

- **Barendregt–Thomas.** Each species "becomes closer to zero with each cycle". Discrete
  populations "will eventually drop to exactly zero". Different stochastic formulations give
  different long-run outcomes.
- **So "unbounded depth = the continuum idealisation" is owned in words.** The log-depth phrasing
  and the use of depth types as two-valued queries are ours to supply. Neither is a claim yet.

## Gap that survives

No one has run a marginal-feasibility (Vorob'ev / n-cycle / contextuality-by-default) test on a
cyclic ecological dataset. Coverage: US web search, so non-English and paywalled ecology is
under-covered. The chance a paper was missed is moderate, because ecologists would file such work
under "co-occurrence", "network" or "scale".

## Follow-up (a), 2026-10-20: finding data for a joint-existence test

- **Bleay–Comendant–Sinervo 2007** (PMC2275174) has no tables, no deposited data and no pairwise
  morph × morph counts. Its values exist only in figures.
- **Open data:** Corl et al., Dryad doi:10.5061/dryad.4qrfj6qq7 (2025). `Uta_field_data_on_morphs.csv`
  is 3.7 KB: per outcrop ("World") per year, counts of oo/ob/yo/bb/by/yy throats and morph
  frequencies (Friedman et al. 2017). Not downloaded.
- **Pushback from the data: the lizard cycle is a loop of *relations*, not a loop of *views*.**
  - Site-year morph counts are one joint table per population: one observer, so a world always
    exists (case 1, F2).
  - Building pairwise "views" from them would repeat the Aerts move of manufacturing the scenario.
- **The honest finite test for a dominance cycle** uses pairwise *win rates* P(i beats j). Ask
  whether some random ranking produces them, i.e. the linear ordering polytope. For three items the
  only non-trivial condition is P(1>2) + P(2>3) + P(3>1) ≤ 2 (memory: Block–Marschak 1960;
  Fishburn 1992; to verify). That is owned mathematics (random utility theory), and it is the right
  shape for contest data. It needs morph-vs-morph contest or siring-competition win rates, which
  are not in the Dryad file. They are possibly in Sinervo's papers (paywalled; the user offered
  SFU access).
