# Latticehood audit propagation

*2026-08-04. Propagation and terminology hygiene only; no new mathematics,
attack work, finite search, or Lean. Source verdict:
[`latticehood_prior_art.md`](latticehood_prior_art.md). Claim-status entries:
[`latticehood_propagation_ledger.md`](latticehood_propagation_ledger.md).*

## Verdict

The literal three-way latticehood family has been removed from the active
corpus. No source had promoted it to a theorem, but several authoritative
sources advertised it as the completing conjecture. The corpus now states
three different boundaries and one surviving formal theory target:
`latticehood => Phi` at regularity. The existing OML attack record remains
valid because it was already scoped to `Phi`.

## Phase 0 inventory (captured before editing)

The search covered `notes/`, `papers/`, `docs/`, `README.md`, and `CLAUDE.md`
for “latticehood,” “liftability,” “all three transitions,” “three coordinate
systems,” “three obstructions,” “latticehood family,” and co-occurrences of
pasting/regularity/sharpness.

### Actual three-way assertions

| classification | pre-edit location | pre-edit claim |
|---|---|---|
| **Asserted as a result** | none | No source called the latticehood family a theorem or proved result. |
| **Asserted as a conjecture** | [`frontier_map.md`](../notes/programme/frontier_map.md), §1, “The choice,” and “two-front programme” | `latticehood => liftability => tameness` uniformly across all three coordinate systems; the theory-completing target. |
| **Asserted as a conjecture** | [`shovel_plan.md`](../notes/programme/shovel_plan.md), Theorem 2 and “vacant lots” | Regularity as the load-bearing case of a larger three-transition family. |
| **Asserted as a conjecture** | [`taxonomies_index.json`](../notes/taxonomies_index.json), `corpus_spine` | The open bridging conjecture is the latticehood family. |
| **Asserted as a conjecture** | [`spine.tex`](../papers/spine/spine.tex), abstract; [`spine_body.tex`](../papers/spine/spine_body.tex), §4 | The family is the single remaining bridging conjecture. |
| **Historical conjecture record** | [`VERIFICATION_PASS.md`](../papers/spine/notes/VERIFICATION_PASS.md) | The 2026-07-08 verification log records insertion of a “latticehood conjecture”; it does not grade it as proved. |
| **Flagged as heuristic/organising structure** | pre-edit spine “non-distributivity as the discriminator” paragraph | A common tame/wild pattern across the three rows, without a theorem identifying their predicates. |
| **Flagged as heuristic/organising structure** | [`distributivity_and_realism_body.tex`](../papers/paper_ii/distributivity_and_realism_body.tex), filtration section; [`paper_ii_taxonomy.json`](../papers/paper_ii/paper_ii_taxonomy.json) | The three transitions form one organising ladder but are explicitly of different mathematical character. |
| **Flagged as heuristic/organising structure** | [`knowledge_map_body.tex`](../notes/knowledge_map/knowledge_map_body.tex) and [`coherence_structure.md`](../notes/unsorted/coherence_structure.md) | The transition names organise known results; `coherence_structure.md` already says the obstructions live on different axes. |

### Search candidates that were not the family

- [`program_overview.md`](../notes/programme/program_overview.md) already called
  the three transitions mathematically different. Its “Through-Line” and
  “Three Obstructions” sections belonged to a superseded Paper I–III arc, not
  the latticehood claim; their headings nevertheless needed a scope fence.
- [`sigma_essential.tex`](../papers/sigma_essential/sigma_essential.tex) and
  the witness-candidate sources state only the surviving regularity conjecture
  `latticehood => Phi`. Their phrase “three obstructions” means three
  regularity-side carrier mechanisms. No edit was made to the sigma-essential
  paper or dependency path.
- [`program_synthesis.md`](../notes/archive/program_synthesis.md) is an archived,
  superseded three-paper synthesis; it does not assert the latticehood family.
- [`latticehood_prior_art.md`](latticehood_prior_art.md) and its ledger already
  record the refutation. `README.md` and `CLAUDE.md` contain no three-way
  latticehood assertion.

## Phase 1 — authoritative programme documents

| file | before | after |
|---|---|---|
| [`frontier_map.md`](../notes/programme/frontier_map.md) | The family was the deepest theory-completing conjecture; regularity was its load-bearing case. | The family is closed under its literal reading. The three boundaries are listed separately, and `latticehood => Phi` is the whole surviving theory front. The Skeleton A/B, three-front, and T4 history is explicitly preserved. |
| [`program_overview.md`](../notes/programme/program_overview.md) | The filtration used an unqualified `S_df` endpoint, while the historical Through-Line/Three Obstructions could be mistaken for the current theory front. | The endpoint is `S_df^sigma`; standalone VDR is fenced. The historical sections are labelled as superseded, and a current three-boundary table states the single surviving target. |
| [`shovel_plan.md`](../notes/programme/shovel_plan.md) | Theorem 2 was the load-bearing case; the full family was a vacant lot. | Theorem 2 is the whole regularity theory front; the family is no longer a vacant lot. All recorded attack work remains attached to `Phi`. |
| [`taxonomies_index.json`](../notes/taxonomies_index.json) | Registry advertised the family as the open bridge. | Registry records the refutation and points to OML finite-trace sigma-liftability. |

## Phase 2 — paper-level check

No paper source stated the family as a theorem or result. The spine called it a
conjecture in both abstract and body; Paper II offered the filtration as an
organising synthesis and said the transitions were different; the
sigma-essential paper stated only `latticehood => Phi`.

No proved paper theorem required retraction. Two paper sources did require
correctness-level prose/typing maintenance:

- the reference-only spine now retracts the false literal conjecture, gives the
  three distinct boundaries, and states only the regularity question;
- Paper II now distinguishes standalone `VDR` from the sigma-additive
  dispersion-free filtration endpoint.

The reconstruction and Paper II sources also contain reciprocal notices that
their `EA`/`PR` symbols are paper-local. The sigma-essential paper of record and
its dependency path were read only.

## Phase 3 — terminology hygiene

The canonical decisions are collected in
[`coherence_terminology.md`](coherence_terminology.md):

| term | before | after |
|---|---|---|
| Reconstruction `EA`/`PR(R)` versus realism-paper `EA`/`PR` | Same symbols and a common local-to-global motivation invited silent identification. | Both source definitions are recorded; no translation is claimed. Cross-paper uses must be qualified. |
| `VDR` versus filtration | `S_df` was declared a subset of `S_sigma`, while standalone VDR asked only for a dispersion-free state. | Canonical `VDR(A)` means `S_df(A)` is nonempty. The filtration endpoint is `S_df^sigma(A) := S_df(A) intersect S_sigma(A)`. |

The VDR split is propagated through the Paper II body and outline, the spine,
the programme overview, the Paper II taxonomy, and the knowledge map. The
`EA`/`PR` fence appears reciprocally in the reconstruction and Paper II sources
and centrally in the terminology note.

## Phase 4 — theory-front restatement

[`oml_lattice_regularity_attack.md`](../notes/open_questions/oml_attack/oml_lattice_regularity_attack.md)
now records, at its entry and in §33, that `latticehood => Phi` is the entire
surviving theory front. Its earlier word “unified” is scoped to the three
regularity-side meet-destruction mechanisms. The description “needs a genuinely
new idea to unify three arrows” is retired; no theorem-let, reduction, search
receipt, or epistemic grade in the attack changes.

## Phase 5 memo

**Theory front in one sentence.** Determine whether every concrete,
sigma-complete, non-Boolean, essentially irreducible orthomodular lattice
satisfies the finite-trace sigma-liftability predicate `Phi`.

**Status changes.** The family moved from OPEN CONJECTURE/HEURISTIC to
REFUTED-LITERAL and was removed from the frontier map, shovel plan, taxonomy
registry, and spine. `latticehood => Phi` stayed mathematically OPEN but moved
from “load-bearing case” to the whole theory-front target. The filtration/VDR
identification moved from AMBIGUOUS to TYPED-SPLIT. Exact ledger entries are in
[`latticehood_propagation_ledger.md`](latticehood_propagation_ledger.md).

**Paper correctness.** No theorem was false because the family was never stated
as one. The spine nevertheless needed its now-refuted conjecture removed, and
Paper II needed the infinite-carrier sigma-additivity ambiguity made explicit.

**Outside-specialist readiness.** Yes. The surviving problem has a specified
carrier class, quantified finite traces, and a precise conclusion. A
two-paragraph letter statement follows.

> Let `L` be a concrete, sigma-complete, non-Boolean orthomodular lattice,
> viewed as a complement- and countable-disjoint-union-closed family of subsets
> of a set `Omega`, and assume it is essentially irreducible (the quotient by
> the sigma-ideal of countable sets has centre `{0,1}`). For every finite
> orthocomplement-closed suborthoposet `B subset L` and every two-valued state
> `s` on `B`, suppose there is a global finitely additive two-valued state `mu`
> on `L` with `mu|B = s`. Must there be a global sigma-additive two-valued state
> `nu` on `L` with `nu|B = s`? This is the predicate `Phi(L)`.
>
> Equivalently, is the set of sigma-additive two-valued states dense in the
> finitely additive two-valued states for the finite-coordinate product
> topology, throughout that OML class? The analogous orthomodular-poset form
> fails by the corpus's sigma-essential witness, while no OML proof or
> counterexample is known in the audited literature. I would be grateful for a
> reference to any state-extension, normality, or orthomodular-lattice theorem
> that settles this density question, or for a known counterexample under these
> exact hypotheses.
