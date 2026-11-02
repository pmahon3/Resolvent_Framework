# Prior art for a research decision graph (layers + `rests_on` / `informs` + `cascade.py`)

Scout run 2026-11-02. Shelf-first: `SHELF_INDEX.json` held nothing on this topic (grep for Doyle, de Kleer, AGM,
IBIS, Toulmin, Lakatos, Dung, blueprint, traceability, micropublication, discourse graph: only unrelated
`BLUEPRINT_OML_SURVEY.md` path hits). Two PDFs added to the shelf (de Kleer 1986, Clark et al. 2014), with index entries.

Read levels: **READ** = text of the PDF read in part (sections named); **ABS** = abstract / publisher page / tool
README; **SEC** = secondary summaries from search results only; **MEM** = from standard knowledge, not checked
this session (treat as unverified).

Repo facts that constrain the design (from `notes/TAXONOMY_SCHEMA.md`): entries already carry `id`, `status`,
`uses` (the hand-proof DAG, "mirroring the blueprint's `\uses`"), `scope`, `lean`, `owned_by`; gates are
"record, not propagate" and "reversal = a new gate, not a mutation". Any tool must respect both.

---

## (a) Findings

### 1. Truth maintenance systems
- **Doyle 1979**, "A Truth Maintenance System", AI 12(3):251-272. **SEC + READ via de Kleer's section 3.1.**
  Nodes are IN/OUT; an SL-justification has an *inlist* and an *outlist* (valid iff inlist all IN, outlist all OUT).
  Every IN node needs **well-founded support**: circular supports that satisfy the justifications locally are
  outlawed. Contradiction triggers dependency-directed backtracking: find the *assumptions* (nodes whose support
  has a nonempty outlist) behind it and retract one.
- **de Kleer 1986**, "An assumption-based TMS", AI 28:127-162, PDF on shelf. **READ** (abstract, section 3 on TMS
  limitations, section 4 on environments/labels, via pdftotext). Each node is labelled with a set of
  *environments* (sets of assumptions); labels are kept consistent, sound, complete, minimal. Contradictions record
  *nogood* sets; retraction is avoided and context switching is free. His list of Doyle-TMS defects is directly
  relevant: single state at a time; "overzealous contradiction avoidance" (A, B contradictory should only block
  inferences using both); "the dominance of justifications" (what counts as an assumption changes as support
  changes); well-founded support needs a global computation; "unouting" (rederiving what was retracted).
- Later: Forbus–de Kleer, *Building Problem Solvers* (1993) (**MEM**) is the textbook with JTMS/ATMS/LTMS code.
  Python ports found: `ftl-reasons` (Doyle-style, v0.57, MIT, SQLite `reasons.db`, `retract`/`assert`/`nogood`/
  `check-stale`/`export`; **ABS** from PyPI; pre-1.0, one maintainer; the page does not address cycles);
  `ltms` and `NATMS` are toy/research ports (**SEC**).
- Survey bridging TMS and AGM: Almeida & Casals, "From Doyle to AGM", arXiv:2608.14567 (May 2026). **ABS only**;
  could not confirm it discusses JTMS/ATMS or entrenchment. Worth one read if belief-change depth is wanted.

### 2. Belief revision (AGM)
- Alchourrón–Gärdenfors–Makinson, JSL 50(2):510-530, 1985: partial meet contraction, postulates, representation
  theorem. **SEC.** Entrenchment (Gärdenfors–Makinson, TARK 1988): contraction gives up the least entrenched
  beliefs first. **SEC.** Hansson-style *belief bases* (revise the explicit base, not the deductive closure)
  noted in results; **SEC**. Iterated revision (Darwiche–Pearl 1997) and the recovery-postulate controversy:
  **MEM**.
- What it says for us: (i) when a reversal forces something to go, retract in order of *increasing entrenchment*;
  (ii) revise the **explicit base** (the nodes we wrote), never a closure; (iii) AGM is silent on the order of
  successive revisions, which our dated log supplies. AGM presupposes a logical language and consistency
  checking; our nodes are prose, so only the *ordering idea* transfers.

### 3. Design rationale and argument mapping
- **IBIS**, Kunz & Rittel 1970, Berkeley working paper: three node types (issue, position, argument) with
  attachment rules: issues attach to any node, positions only to issues, arguments only to positions. **SEC.**
  gIBIS (Conklin–Begeman 1988) and DRL (Lee 1991), **MEM**, add tooling/decision-support only.
- **QOC**, MacLean–Young–Bellotti–Moran, HCI 6:201-250, 1991: question, options, criteria; options are assessed
  against criteria. **MEM** (my search returned nothing on it).
- **Toulmin** (*Uses of Argument*, 1958): claim, data, **warrant**, backing, qualifier, rebuttal. **MEM**, but
  Clark et al. (READ, section on argument) cite it and use it. The warrant is the inference step licensing
  data -> claim.
- **ADRs**, Nygard 2011 "Documenting architecture decisions": title, status (proposed/accepted/deprecated/
  superseded), context, decision, consequences; a reversed decision is a *new* record, old one kept and
  marked superseded. MADR adds "superseded by" links. **SEC** (original post not retrieved).

### 4. Requirements traceability and change impact
- Gotel & Finkelstein 1994, "An analysis of the requirements traceability problem", ICRE 94-101; UCL Discovery
  eprint 749 (PDF fetch failed, not shelved). **ABS + SEC.** Finding: >100 practitioners; most traceability
  failures stem from weak **pre-requirements-specification** traceability, i.e. losing track of where a
  requirement came from and which people/rationale produced it, not from missing code links.
- Tools: **Doorstop** (one file per item in VCS, parent-child links, `link` + validation) and **StrictDoc**
  (descended from Doorstop, parent-child links, coverage). **ABS.** The search did not confirm "suspect link"
  behaviour; from memory Doorstop stores a content fingerprint on each link and flags the link suspect when the
  parent text changes (**MEM**, verify before copying). Change impact analysis (Bohner–Arnold 1996): **MEM**.

### 5. Research knowledge graphs
- **Discourse graphs** (Joel Chan; Roam and Obsidian plugins): atomic Question / Claim / Evidence / Source nodes,
  typed relations (supports, opposes, informs), sidebar "discourse context". **SEC** (plugin pages, forum posts;
  no primary paper read). The Obsidian plugin requires Datacore; its lab example states git workflows are
  unobserved.
- **Micropublications**, Clark–Ciccarese–Goble, J Biomed Semantics 5:28 (2014), arXiv:1305.3506, on shelf.
  **ABS + READ of the argument section's headings.** Minimal form = statement + attribution; maximal form =
  statement + all evidence, interpretation, discussion and *challenges*. Typed `supports` / `challenges` edges,
  explicitly linked to Toulmin rebuttal and Dung attack; a corpus of them forms an evidence network.
  Incremental adoption is a stated design goal.
- Nanopublications, ORKG, SEPIO, CiTO: **MEM, not read.** CiTO is a vocabulary for citation intent
  (supports, disputes, extends, usesMethodIn...); useful only as a word list. All are RDF/OWL publishing
  infrastructure.
- **Dung 1995**, AI 77(2):321-357, abstract argumentation: arguments + attack relation; grounded extension =
  least fixed point of the defence function, always exists and is unique; stable extensions may not exist.
  **SEC.** Attack cycles are legal here, unlike justification cycles.

### 6. Mathematics-specific
- **leanblueprint** (Massot; PyPI; plasTeX): dependencies from LaTeX labels; a label counts as a dependency of the
  *statement* if needed to state it, of the *proof* if only needed in the proof; node colours = formalization
  status (not_ready / can_state / stated, plus fully-formalized darker); `checkdecls` verifies Lean names exist
  (CI-checkable). **SEC.** LeanArchitect (Zhu–Monticone–Welleck–Avigad, ITP 2026) infers dependencies from Lean
  code. **SEC.**
- **Lakatos**, *Proofs and Refutations* (1976; thesis 1961): responses to a counterexample = surrender,
  monster-barring (redefine the concept), exception-barring (restrict the conjecture), monster-adjusting,
  **lemma-incorporation** (the counterexample exposes a hidden lemma; put it in the proof and the theorem).
  **SEC.** *Methodology of scientific research programmes* (hard core, protective belt, negative/positive
  heuristic, progressive vs degenerating): **MEM**, search did not retrieve it.
- Polymath wiki/blog practice: **not searched** (MEM only: public log + wiki summary; no formal graph).

### 7. Value of information
- Howard 1966, "Information value theory", IEEE Trans. SSC-2(1):22-34. **ABS + SEC.** Value of perfect
  information is an upper bound on what any experiment is worth; value is zero when no outcome changes the
  action. Chaloner–Verdinelli 1995 (Bayesian experimental design), bandit/portfolio framings: **MEM, not
  searched.**

### 8. Off-the-shelf tools
| Tool | Level | Fit |
|---|---|---|
| `ftl-reasons` (PyPI) | ABS | Doyle TMS CLI; SQLite (binary, not diff-friendly; JSON export exists); no stated cycle handling; pre-1.0 |
| `ltms`, `NATMS` | SEC | toy / research |
| Doorstop, StrictDoc | ABS | git-native requirement items with parent links; one file per item; heavier than needed |
| adr-tools / MADR | SEC | ADR file templates, supersede links |
| Obsidian Discourse Graphs | SEC | needs Datacore + Obsidian vault; node-per-note |
| leanblueprint | SEC | already the model for `uses`; needs a LaTeX blueprint |
| networkx 3.1, PyYAML | local | already installed; enough for cycles/closure |

---

## (b) Mapping table

| Prior art | Our layer / mechanism | Adopt | Lacks for a one-person, theory-first maths repo |
|---|---|---|---|
| Doyle JTMS | `rests_on`; "claim holds unless gate fires" | Well-founded support = acyclic `rests_on`; cycle = alarm. **Outlist** = "holds unless X is established" for open falsifiers. IN/OUT is *computed*, not stored | Auto-flipping statuses violates "record, not propagate"; no prose semantics |
| de Kleer ATMS | assumption sets, nogoods | Per-claim **base**: the minimal sets of unverified leaves it rests on. A **nogood** = a recorded "these cannot all hold" (e.g. the Paper I B2 pair). Alternatives justify a claim (OR groups) | Full label calculus is overkill at hundreds of nodes; closed propositional setting |
| AGM / entrenchment | rank of what to re-examine first | Ordinal entrenchment from layer height and evidence grade; revise the explicit base | No logic language, no postulates |
| IBIS / QOC | probes, "persist or pivot" forks | Question -> options -> criteria for probe choice; issue nodes for forks | Argument-map tooling; no cascade |
| Toulmin | edge annotation | **Warrant on an edge** = the stated reason B supports A. WHY.md's "hidden idealisation" question is a missing warrant | Heavy if required on every edge |
| ADR / MADR | reversal records | Status + context + decision + consequences; supersede, never overwrite; consequences = generated checklist | Per-claim ADRs would be noise |
| Traceability / impact analysis | `cascade.py impact`, `stale` | Forward and backward trace; content-hash on edges to detect suspect links; origin ("pre-RS") links kept for WHY -> aims | Coverage matrices; compliance goals |
| Discourse graphs / micropubs | node kinds Q / Claim / Evidence | Q-C-E typing; typed supports/challenges; minimal-to-maximal adoption; attribution | RDF/OWL, publishing aims, GUI plugin dependencies |
| Dung | contested claims | Only the lesson: an attack cycle is an unresolved dispute to list, not a bug | Extension semantics unnecessary |
| leanblueprint | claims <-> Lean | Statement-uses vs proof-uses split; status colours; CI-checkable names | Needs LaTeX blueprint; no reversal story |
| Lakatos | revision-move vocabulary; layers 0-1 vs 3-5 | Tag each revision with its move; monster-barring is an alarm flag; lemma-incorporation = add node to `rests_on` | Informal, no mechanism |
| Howard VOI | probe choice | Zero-VOI rule (below) | Numeric priors do not exist here |

---

## (c) Design changes suggested for the two-edge + `cascade.py` sketch

1. **Reuse `uses` as `rests_on`; do not migrate.** The schema already has the hand-proof DAG and a validator.
   Extend `uses` entries from strings to optional objects `{id, kind: statement|proof, warrant, checked}`.
   The statement/proof split is the blueprint lesson: a changed *definition* changes the meaning of every
   statement mentioning it (re-read), a changed *proof* only affects provers (re-check).
2. **Two kinds of justification run in opposite directions.** Evidence supports claims bottom-up (epistemic;
   reversal means *retract / re-verify*). WHY and aims authorise probes top-down (motivational; a change means
   *re-prioritise*, not "false"). Keep two edge types but give `informs` a `kind` (`motivates | suggests |
   analogy | surprised-by`) and make `cascade.py` print different verbs for the two. Gotel–Finkelstein says
   the origin links (WHY -> aims -> seams) are the ones that rot, so keep them few and written in words.
3. **Alternatives and OR groups (TMS).** Let a claim list several independent supports
   (`rests_on_any: [[a,b],[c]]`). Impact output then says "loses SOLE support" vs "an alternative remains".
4. **Assumption base (ATMS-lite).** `cascade.py assumptions <id>` returns the leaf set: ⟦HAND⟧ unverified,
   cited-not-read, stance items, `scope` limits. Reversing a leaf then names exactly the claims whose base
   contains it. Add a `nogoods` list (sets of ids that cannot all stand), consulted by `check`.
5. **Status is advisory output, never written.** Respect "record, not propagate": `impact` prints
   "would be OUT / suspect", the human edits `status`. This also sidesteps Doyle's unouting problem: nothing is
   retracted, so nothing needs rederiving.
6. **Entrenchment = layer height + evidence grade.** Grades: `lean` > `hand-verified` > `hand-unverified` >
   `cited-read` > `cited-secondary` / `llm`. Sort suspects with the **least entrenched first**, and show the most
   entrenched suspect last with its warrant (it is the one a reversal should most hesitate to touch).
7. **Hash-based staleness.** Each edge stores `checked: <hash of target's one_line+status+scope at review>`.
   `stale` lists edges whose target changed since; no label grep needed. Plus a date check: dependent
   last-reviewed earlier than a dependency's last status change.
8. **Revision-move tag** on reversal records: `surrender | monster-barring | exception-barring |
   lemma-incorporation`. Monster-barring (changing a definition so the counterexample leaves) prints a warning;
   the programme's own stated risk is rescue by reframing ("Park honestly").
9. **Cycle policy.** `rests_on` cycle -> hard error listing the cycle. `informs` loops -> allowed, must carry a
   date; `check` prints loops of length <= 3 once per run as an FYI, and mutual-attack pairs as "unresolved
   dispute" (Dung).
10. **Layer-direction lint.** A `rests_on` edge from a layer-0/1 node (WHY, stance) onto layer 4-5 (evidence) is
    suspect: aims should not be justified by a single result (circularity alarm); warn.
11. **Undeclared dependents.** `impact` also greps for the id across `notes/`, `papers/`, `docs/`, and lists files
    that mention it with no declared edge, as "add edge or mark `mentions_only`". This is the 2026-10-27 failure
    mode (10 files by grep) turned into a worklist.
12. **Zero-VOI check for probes.** For each gate: for each pre-registered outcome, run `impact` on its `affects`
    ids. If no outcome changes any decision-bearing downstream node (a claim at layer <= 3, a paper statement),
    the probe is decorative; say so. Rank live probes by (number and entrenchment of nodes whose status would
    flip under some outcome) divided by cost. Ordinal only.

---

## (d) Recommended minimal instantiation, and what not to adopt

**Files**
- Nodes = existing taxonomy entries (id, status, uses, scope, lean). No new per-node files.
- `notes/programme/decision_graph.json`: only the nodes that do not live in a taxonomy: layer 0-1 items
  (WHY.md question, aims, stance), each paper, each checkpoint decision; fields
  `{id, layer, title, file, anchor, grade, status, reviewed}`. Cross-file ids written `collection:id`.
- `notes/decisions/YYYY-MM-DD-slug.md`: MADR-lite for **reversals and forks only** (a threshold: >= 3
  dependents or any layer <= 3 node). Template:
  `status (proposed|accepted|superseded-by) / move / trigger / what-changed / impact (pasted from cascade.py,
  checkboxes) / consequences / rests_on / informs`.
- `tools/cascade.py` (networkx + stdlib, ~150-250 lines). Memory budget trivial.

**Script behaviour**
- `check`: dangling ids, `rests_on` cycles (error), layer-direction lint, nogood violations, orphans (no edges).
- `impact <id>`: transitive `rests_on` dependents, "sole support" vs "alternative remains", 1-hop `informs`
  with dates, undeclared mentions by grep; sorted least-entrenched-first; capped at N (default 15) with a count,
  per CLAUDE.md pacing.
- `assumptions <id>`; `stale`; `probes` (zero-VOI check). Read-only. Exit code nonzero only on `check` errors.

**First increment** (a morning's work): `check` + `impact`, plus back-filling `rests_on` for the three 2026-10-27
reversals only. Add the rest when it hurts.

**Do NOT adopt**
- Full ATMS label algebra, Dung extension semantics, AGM postulates or contraction operators (no logical
  language; the nodes are prose).
- RDF/OWL, nanopublications, ORKG, SEPIO (publication infrastructure; the programme states publication is
  not a goal).
- A node file per claim or an Obsidian/Datacore dependency; a vault migration would cost more than the grep it
  replaces.
- `ftl-reasons` as a dependency (binary SQLite, pre-1.0, no cycle handling stated, auto-retraction conflicts
  with "record, not propagate"). Borrow its command vocabulary (`explain`, `trace`, `check-stale`) only.
- Traceability matrices, 100% coverage goals, mandatory warrants, numeric VOI or bandits (no priors exist).
- A requirement that every edge be present before work proceeds: Micropublications' lesson is incremental,
  minimal-to-maximal adoption.

**Honest caveat.** The graph records what the human has written down as depending on what. It cannot see an
unrecorded dependency, and a tidy graph can raise confidence it has not earned; the undeclared-mention grep and the
hostile `/audit` remain the actual checks. Treat `cascade.py` output as a worklist, not a verdict.

## Sources
- Doyle 1979, AI 12(3):251-272. de Kleer 1986, https://www.dekleer.org/Publications/An%20Assumption-Based%20TMS.pdf (shelved)
- Almeida & Casals 2026, https://arxiv.org/abs/2608.14567
- AGM 1985 JSL 50(2):510-530; Gärdenfors–Makinson 1988 (search results via Cambridge Core and others)
- Kunz & Rittel 1970 (Berkeley IURD); Wikipedia "Issue-based information system"; MADR https://adr.github.io/madr
- Gotel & Finkelstein 1994, https://discovery.ucl.ac.uk/749/
- Clark, Ciccarese, Goble 2014, https://arxiv.org/pdf/1305.3506 (shelved)
- Discourse Graphs: https://www.obsidianstats.com/plugins/discourse-graphs ; https://github.com/DiscourseGraphs/obsidian-lab-example
- leanblueprint https://pypi.org/project/leanblueprint/ ; LeanArchitect https://drops.dagstuhl.de/storage/00lipics/lipics-vol382-itp2026/LIPIcs.ITP.2026.25/LIPIcs.ITP.2026.25.pdf
- Dung 1995, AI 77(2):321-357 (search results, e.g. https://core.ac.uk/download/80775633.pdf)
- Howard 1966, IEEE SSC-2(1):22-34
- ftl-reasons https://pypi.org/project/ftl-reasons/ ; ltms https://pypi.org/project/ltms/ ; StrictDoc https://strictdoc.readthedocs.io
