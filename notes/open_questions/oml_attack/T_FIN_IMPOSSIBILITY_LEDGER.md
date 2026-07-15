# T-FIN impossibility ledger

*Campaign 19 parallel theorem track, opened 2026-07-15. This ledger does not
assume T-FIN and does not replace the constructive quotient computation.*

## The theorem under attack

**T-FIN.** Every terminal concrete OML on the current full conditional
`K_{2,2}` carrier extending the four-cell root satisfies at least one of:

- **Gate A:** `Bool(q0,q1)` or `Bool(r0,r1)` is reconstructed;
- **Gate B:** there is a nonzero event contained in a row activation cylinder.

The present one- and two-cell marginal OMLs are not terminals on the full
carrier and therefore do not refute T-FIN. They are exact countermodels to
weaker implications that omit transverse/full-grid coupling.

## Current constructive controls

| Control | Exact result | Evidence | T-FIN scope missing |
|---|---|---|---|
| node-6 formal split | 17 points, 18432 events, `B_9 x MO2^2`, defect and both boundary gaps persist | **Executable verified**; product **Hand proved** | all physical cells, activation, trivial centre |
| node-6 + cell 00 | 892 points, 18496 events, centre-free OML, defect persists, row-0 Gate B absent, Gate A absent | **Executable verified**, payload `e65582f3...` | cells 01/10/11, row-1 activation, full carrier |
| node-6 + same-row cells 00/01 | 9928 points, 18554 events, centre-free OML, defect persists, row-0 Gate B absent, Gate A absent | **Executable verified**, payload `2764d647...` | transverse cells 10/11, row-1 activation, full carrier |

Both finite OMLs are `Phi`-tame: on a finite OML every orthogonal family has
only finitely many nonzero members, so finite additivity equals sigma
additivity. **Hand proved.** Their role is architectural, not negative.

## Failure ledger

| Candidate implication | Status | Evidence | Smallest countermodel or obstruction | Revised theorem |
|---|---|---|---|---|
| profile-only proper splitter in a terminal OML implies Gate A | **Refuted** | **Executable verified** | 17-point node-6 terminal, `B_9 x MO2^2` | add physical coupling and/or essential irreducibility |
| essential irreducibility plus one restored conditional cell implies Gate A or row-0 Gate B | **Refuted** | **Executable verified** | 892-point centre-free one-cell OML | require at least a second incidence direction |
| two faithful cells sharing activation and `q`, plus the common node-6 defect, imply Gate A or row-0 Gate B | **Refuted** | **Executable verified** | 9928-point centre-free same-row OML | require transverse `r` coupling and the second activation pattern |
| restoring an adjacent same-row cell repairs the first PJH hull or extracts its residue | **Refuted** | **Executable verified** | same-row OML: hull/residue absent, same join least | propagation theorem must use transverse provenance or a strict defect rank not constant on this control |
| coupling that destroys the formal product centre must repair the defect | **Refuted** | **Executable verified** | one-cell OML has centre `{0,1}` and persistent defect | centre destruction and PJH repair are independent; add block-incidence or transverse hypotheses |
| a proper non-profile splitter makes point states fail order separation | **Refuted** | **Hand proved** from concreteness; **Executable verified** construction | one-cell OML (already point reduced) | state route must concern all fa states, sigma interpolation, or an infinite-limit event invisible to sigma states |
| two bare four-residue squares with event rows/columns/total force a residue event | **Refuted** | **Hand proved** | four-point six-event `MO2` control | require explicit shared edge/PJH/provenance incidence |
| same-row coupling forces monotone growth of the fattened same-side meet | **Open** | no transported meet certificate yet | current quotient receipts do not serialize the meet | compute the exact meet and residue in the same-row OML; then state the missing transverse growth hypothesis |
| every centre-free gate-avoiding binary defect violates cross-cut extremality | **Refuted** at one- and same-row levels | **Executable verified** all new-event pairs | 892- and 9928-point OMLs | restrict to transverse/full `K_{2,2}` coupling |
| transverse cell 10 forces hull repair, Gate B, centrality, or nonlatticehood | **Open** | none | next exact quotient | construct cells-00/10 quotient and audit both activations |
| full four-cell terminal fires Gate A or B | **Open** | T-FIN | no full terminal or proof | retain as fixed-carrier target |

## Route I — coupled residue squares

The exact same-row control refutes every lemma whose coupling hypotheses are
only: two faithful conditional cells, shared activation, shared `q`, common
node-6 first defect, centre-freeness, and absence of Gate A/B. A valid
two-square obstruction must mention at least one datum absent here:

1. a transverse cell sharing `r0` or `r1`;
2. the second row activation and its conditional premise;
3. cross-row maximal-block incidence;
4. two provenance-fattened meets coupled through one column; or
5. a state-compatibility condition involving both rows.

**Level-1 theorem (proved).** Same-row two-cell coupling does not force Gate A
or Gate B. **Executable verified.** A Level-2 transverse-coupling theorem is
**Open**.

## Route II — first-PJH-defect propagation

The node-6 defect does not change type after adding cell 00 or cell 01: its
profile word, witness pair, designated join, missing hull, and missing residue
are unchanged. **Executable verified.** Hence “number of restored same-row
cells” is not a well-founded defect rank.

The smallest live rank must detect transverse information. Candidate state:

`(atlas node, entered profile, split-source cell, restored row set,
restored column set, activation rows represented, hull/residue eventhood,
cross-cut status)`.

The next transition `cells {00,01} -> add 10` is discriminating: it introduces
both a new row activation and a shared-column constraint. Coverage beyond this
transition is **Open**.

## Route III — fattened-meet incompatibility

No growth theorem is currently proved. The same-row receipt does not yet
serialize the lattice meet `q0^c meet q1`, its provenance core, or its proper
residue. Therefore no claim is made that the meet persists unchanged. The
first required test is an exact meet certificate inside the 18554-event OML.
If it is proper and stable, it is the requested explicit locally stable meet
type refuting same-row growth. If it grows, the increment must be classified
before proposing a transverse induction. **Open.**

## Route IV — maximal blocks and centre

Centre forcing at the one-cell and same-row levels is refuted: both OMLs have
centre `{0,1}`. **Executable verified** using the generator-commutant lemma
(**Hand proved**). Full maximal-block classifications are not yet available.
The smallest useful block problem is not all blocks; it is the incidence of
blocks containing the node-6 join, the two restored edge algebras, and the
first transverse cell events. This begins only after cell 10 is restored.

## Route V — state separation

Point evaluations order-separate both quotient OMLs by concreteness.
Therefore point separation cannot prove T-FIN. Since both controls are finite,
they are automatically `Phi`-tame, but this says nothing about the intended
uncountable assembly. The live state theorem must address one of:

- classification/extension of all finitely additive two-valued states across
  transverse repairs;
- compatible sigma-state interpolation over the actual maximal-block atlas;
- an infinite-limit event missed by every sigma state; or
- finite-trace replacement after the coupled quotient family is scaled.

All are **Open**.

## Theorem hierarchy status

| Level | Status |
|---|---|
| 1 — exact same-row quotient | **Proved/executable verified:** gate-avoiding centre-free OML exists |
| 2 — transverse coupling type | **Open** |
| 3 — fixed-carrier T-FIN | **Open** |
| 4 — representation-independent rectangle impossibility | **Open** |
| 5 — normalization of arbitrary `Phi` failure | **Open** |

## Decision and next action

The evidence now favours a gate-avoiding *finite marginal architecture*, not
yet a full gate-avoiding terminal. T-FIN remains genuinely uncertain. The
single most discriminating next computation is the exact cells-00/10
transverse quotient using the same node-6 split, with both activation
cylinders and full lattice/centre gates audited. In parallel, serialize the
same-row fattened meet so that Route III has a precise stable or growing
witness.
