# Paper −1: Proof / Lean Gap Assessment
**Assessed:** 2026-03-22
**Status:** All blocking gaps resolved (2026-03-22). One non-blocking proof gap remains.

---

## Result-by-result status

### §2 (Setup): Definitions only

Not formalized as standalone Lean definitions. Content is implicit in `QuerySystem`,
`CompatibleContents`, and the SP1 theorem. No gap.

---

### §3 (Negative result)

| Result | Paper | Lean | Status |
|---|---|---|---|
| Exhaustiveness trivial | Informal proof | Not formalized | No action needed |
| Extension criterion | Cited (Halmos) | `AddContent.measure` / `measure_eq` | No gap |
| The regress | Informal | Not formalized | Conceptual; no Lean target |
| No finitary condition suffices | Corollary | `fcContent_not_sigmaSubadditive` | **Lean stronger than paper; fine** |

---

### §4 (Necessity of incompleteness)

| Result | Paper | Lean | Status |
|---|---|---|---|
| Nontrivial refinement (def) | Defined informally | Not formalized | No action needed |
| Theorem 4.2 (incompleteness) | **Proof has a gap** | Not formalized | **Task A in plan.md** |

**The gap:** The proof of Theorem 4.2 asserts at lines ~282–283 that "the sequence of
such distinctions generates events in σ(E_Q) that are not in E_Q" without constructing
them. This predates SP1 and is the only mathematically incomplete claim in the paper.
Does not affect the SP1 results.

---

### §5 (SP1 resolution) — **resolved 2026-03-22**

| Result | Paper | Lean | Status |
|---|---|---|---|
| Prop: independence (C1 refuted) | `prop:independence` (proved) | `fcContent_not_sigmaSubadditive` | ✓ Complete |
| Def: collectively exhaustive | `def:collective-exhaustion` | `CollectivelyExhaustive` | ✓ Complete |
| Theorem SP1 | `thm:sp1` (proved both directions) | `sp1_iff` (zero sorrys) | ✓ Complete |
| Remark: dissolution | `rem:dissolution` | Layer separation in Lean docstrings | ✓ Complete |

**Former gaps (now closed):**
- ~~Witnessing def had syntactic ∩ condition~~ → replaced by purely valuation-layer def
- ~~Conjecture 5.1~~ → replaced by Theorem `thm:sp1`
- ~~Remark describing obstacle~~ → replaced by dissolution remark

**Remaining Lean gap (non-blocking):** `counterexampleNCC` not bundled as
`NormalizedCompatibleContents` instance (type mismatch: `finCofinSets ℚ` vs
`{s | MeasurableSet s}`). C1 refutation complete via `fcContent_not_sigmaSubadditive`.
See Task B in `plan.md`.

---

### §6 (Foundational conclusions) — **resolved 2026-03-22**

| Result | Paper | Status |
|---|---|---|
| σ-algebra as commitment | Updated | ✓ |
| SUD as faith (§6.2) | Updated: SUD for SP2, not SP1 | ✓ |
| What remains open (§6.3) | Updated: completed chain + SP2 as next question | ✓ |

---

## Summary

| Gap | Blocking? | Status |
|---|---|---|
| §5: witnessing def (syntactic condition) | Yes | ✓ Resolved |
| §5: Conjecture 5.1 | Yes | ✓ Resolved (SP1 theorem) |
| §5: Remark (obstacle framing) | Yes | ✓ Resolved (dissolution remark) |
| Abstract/intro: conjecture framing | Yes | ✓ Resolved |
| §6.3: open question pointing to Conj 5.1 | Yes | ✓ Resolved |
| §6.2: SUD attributed to SP1 | Yes | ✓ Resolved |
| §4: Theorem 4.2 proof gap | No | **Open (Task A)** |
| Lean: counterexampleNCC type mismatch | No | **Open (Task B)** |
