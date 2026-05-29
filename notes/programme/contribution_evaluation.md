# Contribution Type Evaluation Framework

**Date:** 2026-05-27
**Status:** Active reference document for Phase 2 and Phase 7 audits.

---

## Motivation

The Phase 2 audit gate originally asked: "is this result known?" This
is a theorem-novelty check — necessary but insufficient. Mathematical
contributions come in several types, each with its own standard for
novelty and substance. Paper II (EA/PR/VDR vocabulary) is a Type 4
vocabulary contribution that passed the existing audit; Papers I and
II together are a Type 3 unification. The pipeline already handles
non-theorem work implicitly. This document makes the evaluation
explicit and operational.

**Principle: broader lens, not broader standard.** Each contribution
type has its own honest-park criterion. A seed that clears no type's
bar parks, regardless of how many types it vaguely gestures at.

**This is an upgrade, not a correction.** No item in `covered_leads/`
was wrongly parked under the previous lens. The upgrade ensures future
seeds are evaluated against the full range of recognized contribution
types rather than only theorem novelty.

---

## Primary source

Tao, "What is good mathematics?", *Bulletin of the AMS* 44(4), 2007,
pp. 623--634. Lists 21 dimensions of mathematical quality. Collapsed
here to 7 actionable types with operational bars.

Supporting evidence: editorial policies of Annals of Probability
("importance, interest, and originality — formal novelty and
correctness are not sufficient"), SIAM Review (four explicit
expository tracks), JASA (separate theory/methods and applications
tracks), the Monthly ("great exposition is our raison d'etre").

---

## The 7 contribution types and their bars

### Type 1: New theorem

A previously unknown true statement with proof.

**Bar:** The statement is not known, not folklore, not a trivial
consequence of standard techniques. The proof is non-routine.

**Park if:** Known (cite source), folklore (flag as such), or
trivial consequence (explain the 3-line derivation).

This is the existing `/audit pure` check. Retained as-is.

### Type 2: New proof of known result

A different proof of a known theorem.

**Bar:** The new proof (a) introduces a technique applicable
elsewhere, (b) reveals an unexpected connection between fields,
or (c) simplifies substantially. Must satisfy at least one.

**Park if:** The proof is merely an alternative route with no
methodological, conceptual, or simplification gain. "Different
but not better or more revealing."

### Type 3: Unifying framework

A conceptual structure showing previously unrelated results to be
instances of a single phenomenon.

**Bar:** The unification enables *method transfer* between the
unified domains — a technique from domain A becomes applicable in
domain B via the framework. Pattern-coincidence (noting that two
things look similar) does not clear the bar.

**Park if:** The unification is an analogy that does not enable
transfer. "These look alike" without "and therefore this technique
applies here."

### Type 4: Vocabulary / conceptual infrastructure

Introducing a new concept, definition, or distinction that
organises existing mathematics.

**Bar (three-statements test):** Name three mathematical statements
cleanly stateable in the new vocabulary but not in standard
vocabulary, AND provide a non-trivial result about at least one.

**Park if:** The vocabulary renames known concepts without enabling
new statements. Failure mode #2 in the pipeline ("rediscovery as
synthesis") is a failed Type 4 contribution.

**Calibration:** Paper II (EA/PR/VDR) clears this bar. The parked
seeds (KVP merger, five-traditions, residual_structure_inference)
do not.

### Type 5: Impossibility / counterexample

Demonstrating that something cannot be done, or that a natural
conjecture fails.

**Bar:** The impossibility (a) closes off a direction people are
actively pursuing, OR (b) sharpens an existing impossibility
non-trivially (weaker hypotheses, stronger conclusion, new
structural insight into *why* it fails).

**Park if:** The impossibility is a trivial consequence of known
results, or merely rephrases an existing impossibility in different
notation. "We already knew this couldn't work."

**Calibration:** Arrow's theorem, Shah-Peters (2020), the CE
non-derivability result — these clear the bar. Rephrasing
Bergna/Heckman-Singer in functional-analytic language does not.

### Type 6: Exposition / translation

Making existing mathematics accessible to an audience that
currently lacks access, or translating results from field A into
field B's language.

**Bar:** (a) Name the target audience. (b) Cite the existing
literature they cannot currently access (language barrier,
prerequisite depth, scattered across sources). (c) The translation
requires non-trivial conceptual work (not just notation change).

**Park if:** The existing literature is already accessible to the
target audience. "This is well-explained in [textbook], Chapter N."

**Venue note:** Expository contributions target specific venues
(Monthly, Intelligencer, SIAM Review, Expositiones Mathematicae,
Notices of the AMS). A contribution that is "only expository" is
still a contribution — at the right venue.

### Type 7: Methodology / applied contribution

A new method, algorithm, or computational procedure.

**Bar:** This is the existing `/audit applied` check. Demonstrated
advantage on concrete problems; sharp regime classification;
non-obvious consequence confirmed numerically.

**Park if:** No computational evidence; assembly is taxonomic not
constructive; cannot answer "why not just [standard method]?"

---

## How seeds interact with types

### Phase 1 requirement

Every seed note must declare its claimed contribution type(s):

> **Claimed type(s):** [e.g., Type 4 (vocabulary) + Type 5
> (impossibility)]. The per-type bars I commit to clearing:
> [specific statement of what the seed must demonstrate].

A seed that cannot articulate its claimed type is not ready for
Phase 2 audit. This is the discipline that prevents the broader
lens from becoming a permission slip.

### Phase 2 audit

The audit evaluates the seed against each claimed type's bar.
The verdict is per-type:

```
Type 4 (vocabulary): FAIL — three-statements test not met.
  The vocabulary renames [existing concept] without enabling
  new statements.
Type 5 (impossibility): UNCLEAR — may sharpen [existing result]
  but need to verify [specific gap].
```

A seed that fails all claimed types parks. A seed that clears at
least one type's bar proceeds to Phase 3, scoped to the surviving
type(s).

### Park notes

Park notes must record which types were evaluated and which bars
failed. This prevents drift and enables retrospective audit of
whether the lens was applied uniformly.

---

## Interaction with existing pipeline rules

**"Park honestly" still applies to every type.** The rule is
unchanged; what changes is the range of types against which
honesty is assessed.

**"Don't formalize known results" applies only to Type 1.**
A Type 4 (vocabulary) or Type 6 (exposition) contribution may
legitimately formalize known results if the formalization itself
is the contribution (e.g., making a classical result accessible
via Lean for the first time). But the seed must claim Type 6 and
clear that bar — the formalization must serve an audience that
currently lacks access.

**"One theorem per paper" generalises to "one contribution per
paper."** The publishable unit is one contribution of any type.
A paper that tries to be vocabulary + exposition + new theorem
is trying to be three things at once.

---

## Open questions: a third audit outcome

The Phase 2 gate produces three outcomes, not two:

1. **Proceed** — at least one type's bar cleared. Move to Phase 3.
2. **Park** — no type's bar cleared, and the seed is dead (known,
   mis-stated, or structurally blocked). Move to `covered_leads/`.
3. **Open question** — no type's bar cleared *yet*, but the seed
   formulates a precise, well-posed problem that is (a) genuinely
   open in the literature, (b) not already posed elsewhere, and
   (c) would have named downstream consequences if solved. Move
   to `notes/open_questions/`.

Open questions are not contributions. They are not being worked
(no Phase 4 time invested). They are re-audited when new
literature appears or a new idea surfaces, and re-enter the
pipeline at Phase 2 if circumstances change.

**Criteria for open-question status (all three required):**
- The question is precisely stated (formal definitions, exact
  theorem to prove or disprove).
- The obstruction to answering it is identified (not just "hard").
- Answering it would have named consequences (specific theorems
  that would follow, specific fields that would benefit).

**Distinction from parking:** A parked seed is dead — the
direction itself is blocked or the result is known. An open
question is alive but dormant — the direction is viable but
requires resources (time, collaboration, new technique) not
currently available.

---

## What this framework does NOT do

- It does not retroactively unpark anything. All items in
  `covered_leads/` were parked for substantive reasons.
- It does not soften the audit. Each type has a concrete bar.
- It does not license revisiting recently-parked material.
- It does not change the 8-phase pipeline structure. The phases
  are type-independent; what varies by type is what "Phase 4
  mathematical work" looks like.
