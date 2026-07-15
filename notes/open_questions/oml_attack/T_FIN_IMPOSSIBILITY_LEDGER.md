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
| node-6 + same-row cells 00/01 | 9928 points, 18554 events, centre-free OML, defect persists, row-0 Gate B absent, Gate A absent; `q0^c meet q1` stays at 2130 points with 352-point nonevent residue | **Executable verified**, payload `2367e72c...` | transverse cells 10/11, row-1 activation, full carrier |
| node-6 + transverse cells 00/10 | 49730 points, 18560 events, centre-free OML, defect persists, both Gate-B cylinders absent, Gate A absent; `q0^c meet q1` stays `0x70` with whole `0111` residue absent | **Executable verified**, payload `75f69aab...` | cells 01/11, three-cell corner, full carrier |
| node-6 + corner cells 00/01/10 | 553648 points, 18618 events, centre-free OML; defect, both boundary gaps, both activation escapes, and unchanged `0x70` meet persist | **Executable verified**, payload `0957dde3...` | actual cell-11 event algebra and full-grid terminal |

All finite controls are `Phi`-tame: on a finite OML every orthogonal family has
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
| same-row coupling forces strict advance of the node-6 same-side meet toward its literal cylinder | **Refuted** | **Executable verified** exact meet certificate | 9928-point same-row OML: 2130-point `0x70` meet persists, whole `0111` 352-point residue remains a nonevent, increment zero | require transverse coupling or the three-cell corner; weak nondecreasing monotonicity remains true |
| every centre-free gate-avoiding binary defect violates cross-cut extremality | **Refuted** at one- and same-row levels | **Executable verified** all new-event pairs | 892- and 9928-point OMLs | restrict to transverse/full `K_{2,2}` coupling |
| transverse cell 10 forces hull repair, Gate B, centrality, or nonlatticehood | **Refuted** | **Executable verified** | 49730-point centre-free transverse OML | require a three-cell corner or full four-cycle |
| transverse cell 10 forces strict advance of the node-6 same-side meet | **Refuted** | **Executable verified** exact meet certificate | transverse OML: `0x70` meet has 8560 points, increment zero; whole `0111` residue has 2880 points and remains a nonevent | require simultaneous complete-row/complete-column incidence in the three-cell corner |
| three-cell corner `{00,01,10}` forces Gate A/B or nonlatticehood | **Refuted** | **Executable verified** exact normal-form audit | 553648-point centre-free 18618-event corner OML | require actual cell-11 events/full four-cycle |
| complete row plus complete column forces strict advance of the node-6 meet | **Refuted** | **Executable verified** | corner OML: 103180-point `0x70` meet, zero increment, whole 25344-point `0111` nonevent residue | require cell 11/full-cycle closure or another node/split |
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

**Level-1 theorems (proved).** Neither same-row nor transverse two-cell
coupling forces Gate A or Gate B. **Executable verified.** A Level-2 theorem
must now require at least a three-cell corner or the full four-cycle.

## Route II — first-PJH-defect propagation

The node-6 defect does not change type after adding cell 00 or cell 01: its
profile word, witness pair, designated join, missing hull, and missing residue
are unchanged. **Executable verified.** Hence “number of restored same-row
cells” is not a well-founded defect rank.

The smallest live rank must detect transverse information. Candidate state:

`(atlas node, entered profile, split-source cell, restored row set,
restored column set, activation rows represented, hull/residue eventhood,
cross-cut status)`.

The two-cell transverse state `{00,10}` preserves the identical defect, and
the three-cell corner `{00,01,10}` does too despite containing a complete row
and a complete column. Thus neither restored-cell count, represented
activation rows, nor row/column completion is a strict defect rank. The first
untested transition is the actual fourth cell completing the cycle.
**Executable verified** through the corner; full cycle **Open**.

## Route III — fattened-meet incompatibility

The exact same-row certificate refutes *forced strict advance* from a second
cell sharing activation and `q`. The lattice meet `q0^c meet q1` has `2130`
points and equals the transported node-6 formal-terminal meet on this carrier:
profile mask `0x70`, words `{0100,0101,0110}`. Its literal intersection has
`2482` points and the missing `352` points are exactly the whole `0111`
profile fibre, still a nonevent. The meet increment is empty. **Executable
verified**, payload `2367e72c...`, meet hash `e93f6776...`.

This is an explicit locally stable proper-meet type for this selected split.
It is not the stage-558 `336404`-point fine-fibre fattened meet on the full
carrier. It does not refute weak monotonicity and does not prove stability
under transverse or three-cell restoration. The corner test now shows that
even shared `r0`, the second activation premise, and simultaneous completion
of a row and column do not suffice: its meet remains `0x70` with zero
increment. A valid strict-growth lemma must use cell 11/full-cycle incidence,
an alternative split, or another defect node. **Executable verified** for
this corner; general coverage **Open**.

The transverse control supplies the same negative test: cell 10 leaves the
`0x70` meet unchanged and its whole `0111` residue absent. Thus neither merely
sharing the activation/`q` direction nor merely adding the second activation
through `r0` forces strict advance. The live hypothesis must use their joint
presence, first realized by `{00,01,10}`. That joint presence also fails: the
corner leaves the meet unchanged. **Executable verified**. The full cycle is
the remaining finite hypothesis.

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
| 2 — coupling type through three cells | **Refuted as an impossibility route; full four-cycle open** |
| 3 — fixed-carrier T-FIN | **Open** |
| 4 — representation-independent rectangle impossibility | **Open** |
| 5 — normalization of arbitrary `Phi` failure | **Open** |

## Decision and next action

The evidence now favours a gate-avoiding *finite marginal architecture*, not
yet a full gate-avoiding terminal. T-FIN remains genuinely uncertain. The
single most discriminating next computation is restoration of the actual
cell-11 event algebra on the full compatible carrier using the same node-6
split. Audit full-cycle closure, both gates, PJH defect, meet residue,
latticehood, centre, and state separation before any arbitrary-base claim.
