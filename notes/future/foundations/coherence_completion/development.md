# Development Log: Coherence and Completion

Working log for the philosophy-math iteration on coherence, consistency,
failure modes, and admissibility.  Entries are chronological.  Material
graduates to the stable files when it stops changing.

---

## 2026-05-03 — Initial state and overlap diagnosis

The cluster currently has three files with significant overlap:

- `conceptual_schema.md` — the seed note (2026-04-13).  Contains the
  three-component schema, the conceptual grammar (consistency / coherence /
  admissibility), the forcing vs permitting distinction, the failure-mode
  taxonomy, and the CE worked example.  Also contains objecthood-as-open-horizon
  and valuation-of-refinement — both philosophical in register.

- `paper_sketch.md` — the exposition plan (2026-05-02).  Walks through most of
  the same material: the schema, the grammar, the CE witness, objecthood, the
  taxonomy table, and the staging options (Version A / Version B).

- `mathematical_language.md` — the formal file (2026-05-02).  1370 lines.
  Contains the abstract schema, the probability instance as seed example
  throughout, and the institution/completion-descent generalization.  Now has a
  three-zone table of contents.

The overlap arose because `conceptual_schema.md` was the original working
surface where both philosophical and mathematical ideas were developed together.
When `paper_sketch.md` was created for the exposition plan, it needed the same
material as context, so it re-walked it.

### What needs to happen

1. Thin `conceptual_schema.md` to its proper role: the vocabulary and taxonomy
   that define the conceptual space.  Remove narrative, staging, and worked
   examples that now live better in `paper_sketch.md` or
   `mathematical_language.md`.

2. Make `paper_sketch.md` the sole home for: exposition plan, staging options,
   abstract draft, section outline, and the table comparing all five layers.

3. Keep `mathematical_language.md` as-is (with the new zone structure).

4. Future iteration on the concepts goes here in `development.md`, not into the
   stable files until it settles.

### Pending conceptual questions

These are the open edges where philosophy and math are still entangled:

- **Compactness as distinguishing consistency**: is contradiction the unique
  compact failure mode?  This is philosophically motivated (consistency as
  species of coherence) but needs a mathematical answer.  Currently stated as
  open question 3 in `conceptual_schema.md` and as Target 2 in
  `paper_sketch.md`.

- **Forcing vs permitting**: the distinction is clear for CE (CE forces, not
  merely permits).  Is this always the case for admissibility conditions?  Or
  can there be admissibility that permits without forcing?  This affects whether
  the schema has two levels (coherence / admissibility) or three (coherence /
  permitting / forcing).

- **Horizon plurality and valuation**: the zeta example suggests multiple
  horizons for one object.  The mathematical language file has a "Horizon
  Plurality" section but it is still philosophical.  The question is whether
  horizon comparison is a formal object (functors between completion-descent
  data?) or just a naming convention.

- **Fibre mixing as second worked example**: blocked on the derivability
  question.  If fibre mixing turns out to be irreducible (like CE), then the
  two-example Version B becomes natural.  If derivable, it's still an example
  but a less interesting one for the coherence paper.

### First formal steps (from original conceptual_schema.md seed)

1. Write a provisional formal definition of a "coherence notion" within the
   three-part schema (local data / global realization / failure mode).
2. Define what it means for such a notion to be *compact*: every instance of
   the failure mode is detectable by a finite sub-instance.
3. Verify that consistency/contradiction is the canonical compact case under
   this definition.
4. Test whether CE or any non-extension coherence notion can also be compact
   in a nontrivial way — or prove it cannot.

Step 4 is the priority theorem target.  A positive answer (another compact
coherence notion exists) would force a richer taxonomy; a negative answer
(compactness singles out contradiction-type failure) would give a formal sense
in which consistency is the unique compact coherence notion.
