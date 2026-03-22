# Paper −1 Plan
**Branch:** `paper-minus-one`
**As of:** 2026-03-22

---

## Status

**Paper update: complete.** All blocking tasks executed (2026-03-22).
The paper now states and proves SP1 as a theorem. Abstract, intro, §5, §6 all updated.

**Remaining before submission:** one non-blocking proof to tighten (§4 Theorem 4.2),
one optional Lean architectural gap.

---

## What is done

### Mathematics
- Layer separation proved independent: index layer vs valuation layer.
- C1 refuted: explicit counterexample (finite-cofinite algebra on ℚ, WithTop ℕ index).
- SP1 theorem proved: collective exhaustion ↔ σ-additive extensibility at every level.
- Tetralemma dissolved: C4 closed by SP1 theorem.

### Lean
`formalization/QuerySystem/QuerySystem/DiscriminabilityFoundations.lean` — zero sorrys.
Key theorems: `fcContent_not_sigmaSubadditive`, `sp1_extension`, `sp1_necessity`, `sp1_iff`.

### Paper
All sections updated. See `gap_assessment.md` for the full result-by-result record.

---

## Remaining tasks

### Task A: Tighten §4 incompleteness proof (non-blocking)

**Location:** `discriminability_foundations_body.tex`, Theorem 4.2 proof, lines ~274–284.

**Issue:** The key step ("the sequence of such distinctions generates events in σ(E_Q)
that are not in E_Q") is asserted rather than constructed. This is the only result in
the paper without a tight proof.

**Decision required first:** Choose one of:
- Option 1: Add singleton measurability as a standing assumption in §2. Then the proof
  constructs: given π(x) = π(y) with x ≠ y in E_{Q'}, the event {x} ∈ E_{Q'} but no
  event in E_Q separates x from y, so countable intersections of E_Q events that
  converge to {x} are in σ(E_Q) \ E_Q.
- Option 2: Reformulate Theorem 4.2 with an explicit hypothesis on E_{Q'} (e.g.,
  "E_{Q'} separates points of O_{Q'}") that makes the proof work without a global
  standing assumption.

Option 1 is simpler. Option 2 is more precise about what the theorem actually needs.

### Task B: Close counterexampleNCC Lean gap (optional)

**Issue:** `fcContent` lives on `finCofinSets ℚ`; `NormalizedCompatibleContents.ν`
expects `AddContent ℝ≥0∞ {s | MeasurableSet s}`. The C1 refutation is complete via
`fcContent_not_sigmaSubadditive`. Closing this formally requires one of:

- Option A: Extend `fcContent` to all measurable sets via Carathéodory (the extension
  is not σ-additive — that requires proof).
- Option B: Parameterize `CompatibleContents`, `CollectivelyExhaustive`, and
  `NormalizedCompatibleContents` by a set semiring `C`. Cleaner long-term; also
  needed if the counterexample is used in SP2 arguments.

Not blocking submission.

---

## Open questions post-SP1

1. **SP2.** Does collective exhaustion + SUD give the global extension to Ω without
   topological assumptions? The index-layer condition re-enters here.

2. **Stone space connection.** σ(E_Q) as σ-closure of E_Q — likely the right lens for
   both the incompleteness theorem and SP2.

3. **Formal layer independence.** Model-theoretic independence of index and valuation
   layers — a precise version of the SP1 dissolution.
