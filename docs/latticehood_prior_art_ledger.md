# Prior-art ledger: latticehood leads

*Opened and closed 2026-08-04. Literature-only gate. The exact statements,
source links, and synthesis are in
[`latticehood_prior_art.md`](latticehood_prior_art.md). “Not located” is a
bounded search verdict, not a proof that no source exists.*

## Entry LPA-LIFT-1 — lifting and completeness analogues

**Question under test.** Is the corpus's finite-trace sigma-liftability `Phi`
an instance of classical measure-algebra lifting; failing that, does an existing
completeness theorem in AW*/W* theory, continuous geometry, pre-Hilbert quantum
logic, or domain theory imply the corpus's latticehood-to-tameness step?

**Best-outcome criterion.** A theorem translating `Phi` to a known lifting
property, or a completeness theorem whose hypotheses are met by a concrete,
sigma-complete OML and whose conclusion supplies `Phi`.

**Outcome.** The names collide but the maps do not. A classical lifting is a
Boolean right inverse to `Sigma -> Sigma/N` for a fixed countably additive
measure; `Phi` asks for a sigma-additive two-valued state matching the finite
trace of some finitely additive state. The lifting theorem's “complete” means
null-complete measure space, not OML latticehood. AW* theory supplies the closest
analogue, but in the negative direction: arbitrary completeness of the
projection lattice (together with annihilator axioms) still does not supply the
predual/normal-measure structure of a W*-algebra. Kaplansky additionally assumes
modularity and obtains lattice-operation continuity, not state regularity.
Amemiya--Araki's lattice is complete on both sides of their dichotomy;
orthomodularity, not lattice completeness, detects metric completeness. Domain
theory likewise has complete lattices which are not continuous.

**Falsifier/search check.** No source among the named primary texts states a
finite-trace finitely-additive-to-sigma-additive density theorem for concrete
OMLs. Existing exact-vocabulary and adjacent-state-extension searches did not
produce one; the repo's earlier Czech-school audit remains the relevant broader
record.

**Status.** **CLOSED — UNRELATED HOMONYM PLUS NEGATIVE ANALOGUES; NO CORPUS
IMPLICATION LOCATED.**

**Evidence grade.** **PRIMARY-SOURCE LITERATURE VERDICT.** Definitions and
hypotheses checked in Fremlin 341A/341K, Heunen--Reyes Definition 2.1, Saito's
explicit non-W* AW* examples, Pavlov, Kaplansky, the local Amemiya--Araki PDF,
and Abramsky--Jung. No new theorem, formalization, or computation.

**Disposition.** Do not invoke the classical lifting theorem as a technique for
`Phi`. AW*/W* is useful as a warning and vocabulary comparison only.

## Entry LPA-BOHR-1 — Bohrification/presheaf collapse

**Question under test.** Do pasting, regularity, and sharpness become one
section/gluing problem for the spectral presheaf over Boolean or commutative
contexts, with latticehood becoming one recognized condition on that presheaf?

**Best-outcome criterion.** A common presheaf and one condition equivalent to
all three transition predicates, or an established theorem reducing the
corpus's completing target to translation.

**Outcome.** Two transitions have classical section formulations, but not on
one presheaf. Kochen--Specker sharpness is exactly nonexistence of a global
element of the spectral presheaf. Pasting is exactly extendability/global
section for the event/distribution presheaf of Abramsky--Brandenburger, with the
acyclic universal-extension case already owned by Vorob'ev. Regularity is
translated by Döring as local sigma-additivity of a measure on clopen subobjects
(equivalently normality in the stated von Neumann scope); restriction
naturality holds on both the finitely additive and normal sides and therefore
does not distinguish them. HLS valuations live on an internally distributive
locale. No source turns binary OML latticehood into one presheaf condition
forcing the three conclusions.

**Decisive negative check.** Projection lattices of von Neumann algebras are
complete OMLs, while the Kochen--Specker spectral presheaf can have no global
elements. Thus literal latticehood-to-sharpness is false in the flagship
presheaf example.

**Status.** **CLOSED — PARTIALLY OWNED TRANSLATION; NO SINGLE-PRESHEAF
COLLAPSE; `Phi` UNCHANGED.**

**Evidence grade.** **PRIMARY-SOURCE LITERATURE VERDICT, CORROBORATED BY A
PRIOR FULL-TEXT REPO AUDIT.** Checked against Isham--Butterfield, Döring's
generalized Kochen--Specker theorem and measure paper, Döring--Isham II, HLS,
Abramsky--Brandenburger, and Vorob'ev; reconciled with
[`topos_route_read_2026-06-19.md`](../notes/open_questions/verification/topos_route_read_2026-06-19.md).

**Disposition.** Cite the sharpness and pasting translations as owned. Use the
topos machinery to locate the regularity wall, not as a solution of `Phi`.
