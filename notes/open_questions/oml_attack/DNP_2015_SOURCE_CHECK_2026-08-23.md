# DNP 2015 — primary-source check: UNRESOLVED, full text required

**Date:** 2026-08-23
**Queue:** relaxed-gate, from `NEXT_CAMPAIGN_HANDOFF.md` item 7.
**Gate:** promote-to-seed **iff** it exhibits a sigma-complete **LATTICE**
carrying a **non-extendable** state. All three conjuncts required.

## Identification (confirmed)

De Simone, A., Navara, M., Ptak, P., *States on systems of sets that are closed
under symmetric difference*, Mathematische Nachrichten **288** (17-18),
1995-2000 (2015). DOI `10.1002/mana.201500029`.

## Abstract (verbatim)

> We consider extensions of certain states. The states are defined on the
> systems of sets that are closed under the formation of the symmetric
> difference (concrete quantum logics). These systems can be viewed as certain
> set-representable quantum logics enriched with the symmetric difference. We
> first show how the compactness argument allows us to extend states on Boolean
> algebras over such systems of sets. We then observe that the extensions are
> sometimes possible even for non-Boolean situations. On the other hand, a
> difference-closed system can be constructed such that even two-valued states
> do not allow for extensions. Finally, we consider these questions in a
> sigma-complete setup and find a large class of such systems with rather
> interesting state properties.

## VERDICT: UNRESOLVED. Do NOT record as "does not promote".

On the abstract alone the gate reads negative on two of three conjuncts:

- the non-extendable two-valued example is presented in a movement SEPARATE
  from the sigma-complete one, and is not there described as sigma-complete;
- the objects throughout are "systems of sets" / "concrete quantum logics",
  i.e. set-representable orthomodular POSETS -- lattice is never claimed.

**That reading is not admissible as a verdict here.** The EPV check
(`EPV_2025_PRIMARY_SOURCE_RECEIPT_2026-07-19.md`) established the precedent
directly: its load-bearing claim sat in the body, not the abstract, and the
abstract-level read was recorded as wrong -- "chat right / repo abstract-fetch
blind". An abstract that separates two movements is exactly the shape that
misled once already. The final section is the one that matters and it is
summarized in a single sentence naming no properties.

## What the full text has to settle

1. In the sigma-complete section: is any member of the "large class" a
   **lattice**, or are they all only sigma-complete OMPs? SDC lattices do
   exist (see adjacent, below), so this is not answerable a priori.
2. Does any sigma-complete member carry a **non-extendable** state, or are the
   "interesting state properties" something else (statelessness, unique state,
   no two-valued states)? Statelessness would NOT satisfy the gate -- with no
   states there is no state to fail to extend.
3. If the non-extendable example of the third movement is in fact sigma-complete
   and a lattice, the gate fires and E5 clause (b) must be rewritten.

## Why this blocks E5

E5's clause (b), the second-inclusion localization, is E4's banked payoff and
rests on "the candidate screen found NO confirmed sigma-complete LATTICE
non-extendable carrier". DNP 2015 is the queued candidate for precisely that
description. Writing Stage-0 `SIGMA_LAYER_TARGET.md` before this is settled
risks building the target document on a premise this paper may negate.

## Access

No open preprint located (arXiv, ResearchGate, author pages). Wiley paywall.
Needs institutional access; drop the PDF in
`notes/literature_review/literature/` and this can be closed in one read.

## Adjacent, unverified, possibly relevant to Q1

"A Symmetric-Difference-Closed Orthomodular Lattice That Is Stateless",
*Order* (2022), DOI `10.1007/s11083-022-09621-7`. Surfaced in the same search;
NOT checked against primary source. If the title is accurate then SDC + lattice
is consistent, which removes one possible a-priori reason the DNP class could
not contain lattices. It is also stateless, so it does not itself satisfy the
gate. Flagged only so Q1 is not answered by assumption.
