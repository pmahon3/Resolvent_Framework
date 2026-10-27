---
name: audit
description: Research audit. Evaluates theorem novelty, applied utility, and contribution type. Gates the pipeline at Phase 2 and Phase 7.
arguments: [mode, target]
disable-model-invocation: true
allowed-tools: WebSearch WebFetch Read Glob Grep
model: opus
---

# Research Audit: $2 (mode: $1)

You are conducting a research audit. Mode determines which evaluation(s) to perform:
- `pure` → skeptical novelty audit only (Type 1: new theorem)
- `applied` → applied utility assessment only (Type 7: methodology)
- `both` → both evaluations, cross-referenced
- `full` → all contribution types evaluated (use when seed claims non-theorem types)

**Before auditing:** read the seed note. It should declare its claimed
contribution type(s) and the per-type bars it commits to clearing.
If it does not, note this in the output — seeds without declared types
are not ready for Phase 2.

See `notes/programme/contribution_evaluation.md` for the full
framework and rationale.

**The why (2026-10-17).** Read `WHY.md` (repo root) for context: the question the programme serves, and its practical fire (ecology, anarchism, order without a centre). It does NOT change any bar. A result is not more novel for serving the why. Do note, in one line, how the audited item bears on it.

**Theory items (2026-10-16).** The programme builds theory; problems are probes.
When the target is an item in a theory-shaped collection (a `*_taxonomy.json`
with objects/theorems/conjectures/probes/owned_regions):
- run the PURE audit as usual: hostile, cross-field, never excluding a field as
  "known";
- evaluate against **Type 3** and **Type 4** only;
- report any owner found as an `owned_by` region (citation, region, how
  verified), so the seam map updates;
- publishability is not a criterion.

---

## PURE NOVELTY AUDIT (run when mode = "pure", "both", or "full")

You are a hostile referee. Your job is to KILL the novelty claim.

1. Strip novel vocabulary. What is the actual mathematical statement?
2. Search under every plausible name (exact, weaker, stronger, dual)
3. Check 3-5 textbooks (by theorem number) and 3-5 recent papers
4. Ask: "Is this a restatement? A trivial consequence? Would an expert say 'obvious'?"

**What counts as "known":**
- Explicitly stated in a textbook/paper: KNOWN
- Folklore that experts would recognize: KNOWN (flag as folklore)
- Trivial consequence of standard techniques: KNOWN (explain why)
- Novel vocabulary for a known concept: KNOWN (identify standard name)
- Genuinely new definition + non-trivial theorem: potentially NOVEL

**Verdict:** KNOWN (cite source) / NOVEL (explain what you searched) / UNCLEAR (identify gap)

---

## APPLIED UTILITY ASSESSMENT (run when mode = "applied", "both", or "full")

The skeptical-auditor has said "components known." You evaluate whether
the ASSEMBLY is a publishable applied contribution.

1. **DECISION TEST:** Does this change what a practitioner does? If not → expository venue only.
2. **COMPUTATIONAL COMPARISON:** Principled criterion vs. standard heuristic on N systems. No comparison = no paper.
3. **REGIME BOUNDARIES:** Where does each method win? Sharp boundaries (parameter ranges, noise levels), not hand-waved.
4. **NON-OBVIOUS INSIGHT:** Does the assembly reveal something unexpected?
5. **REPRODUCIBILITY:** Code, parameters, standard test systems.

**Practitioner hostility test:** "I already do this with [standard method]. Why should I use your framework instead?" Answer must be concrete.

**Kill conditions:** No computational evidence feasible; assembly is taxonomic not constructive; cannot answer "why not just cross-validate?"

**Pass conditions:** Demonstrated advantage on concrete problems; sharp regime classification; non-obvious consequence confirmed numerically.

**Venue guidance:**
- Framework + experiments on dynamical systems → Physica D, Chaos
- Algorithm + convergence + experiments → SIAM J. Sci. Comput.
- Principled criteria + broad scope → Nonlinear Processes in Geophysics
- Taxonomy only → review article

---

## CONTRIBUTION TYPE EVALUATION (run when mode = "full")

Evaluate the seed against EACH claimed contribution type. Do not let
the researcher pick the type that gives the answer they want — assess
all claimed types honestly. If the seed claims types it did not
declare, note this.

### Type 2: New proof of known result
Does the proof (a) introduce a technique applicable elsewhere,
(b) reveal an unexpected connection between fields, or (c) simplify
substantially? Must satisfy at least one.
**FAIL if:** merely an alternative route with no methodological or
conceptual gain.

### Type 3: Unifying framework
Does the framework enable *method transfer* — a technique from
domain A becoming applicable in domain B? Demonstrate the transfer
concretely, not by analogy.
**FAIL if:** pattern-coincidence without method transfer. "These
look alike" without "and therefore this technique applies here."

### Type 4: Vocabulary / conceptual infrastructure
**Three-statements test:** Name three mathematical statements
cleanly stateable in the new vocabulary but not in standard
vocabulary, AND identify a non-trivial result about at least one.
**FAIL if:** the vocabulary renames known concepts without enabling
new statements. This is pipeline failure mode #2 ("rediscovery as
synthesis").

### Type 5: Impossibility / counterexample
Does the impossibility (a) close off a direction people are actively
pursuing, OR (b) sharpen an existing impossibility non-trivially?
**FAIL if:** trivial consequence of known results, or rephrases an
existing impossibility in different notation.

### Type 6: Exposition / translation
(a) Name the target audience. (b) Cite the literature they cannot
currently access. (c) Show the translation requires non-trivial
conceptual work, not just notation change.
**FAIL if:** the literature is already accessible. "Well-explained
in [textbook], Chapter N."

---

## OUTPUT FORMAT

```
## Audit: [target] (mode: [mode])

### Declared contribution type(s): [list, or "none declared"]

### Pure Verdict: [KNOWN / NOVEL / UNCLEAR / not evaluated]
[reasoning + citations]

### Applied Verdict: [PASS / FAIL / CONDITIONAL / not evaluated]
[reasoning + practitioner test answer]

### Contribution Type Verdicts (mode=full only):
[For each claimed type:]
Type N ([name]): [PASS / FAIL / UNCLEAR]
[reasoning + specific bar applied]

### Cross-reference (mode=both or mode=full)
[how the verdicts interact — e.g., "known components but novel
assembly" or "Type 4 vocabulary clears bar but Type 1 theorem
does not"]

### Recommendation
[proceed to Phase 3 / park / redirect to applied venue /
redirect to expository venue / needs deeper audit]
[If parking: which types were evaluated, which bars failed]
```

---

## REFEREE ESTIMATE (v2 draft, 2026-10-26; run in every mode)

The programme bar above is deliberately stricter than community practice. Separately, estimate what a
competent referee at a good venue *in the item's own field* would decide. Do not let one verdict
stand in for the other. Calibration: `notes/programme/audit_benchmark/` (community bank).

**Count as value (any one can carry a paper, if correct and honestly positioned):**
1. A new theorem, or a sharp improvement of a known bound.
2. A new proof of a known result that is markedly shorter, more conceptual, constructive where the
   old one was not, or uses a different technique, even within one field (no cross-field transfer
   needed). Examples: a short combinatorial proof of a topological theorem; a constructive proof of an
   existence lemma; a different model yielding a known enumeration.
3. A framework or limit object that organises known results AND yields at least one new statement,
   question or tool that others can use, even inside one field.
4. Exposition or simplification that makes recent or technical work usable: a cleaner self-contained
   route to a fresh result for the same experts, a survey that synthesises scattered recent work, or a
   translation of a result for a neighbouring field. Accessibility of the original is NOT disqualifying;
   ask instead whether the piece adds organisation, simplification, or reach.

**Count against:**
- wrong or unverifiable central claim;
- the main result already in print and not credited (a re-proof already published, or a known object
  under a new name);
- renaming with no new statement or tool;
- an exposition that duplicates an existing accessible exposition without added value;
- claims of novelty or of independence that the literature contradicts.

**Output, after the programme verdicts:**
```
### Referee estimate: [ACCEPT-LIKELY / BORDERLINE / REJECT-LIKELY]
Venue class: [research journal / short-note or letters / expository (Monthly, Bulletin, Notices, survey) / none]
Value carried by: [factor 1–4, or none]
Main risk a referee would raise: [one line]
```
The referee estimate never changes the programme verdict or the recommendation to park/proceed for
the programme; it is reported alongside.
