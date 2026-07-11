# Hostile prior-art search: Czech/Slovak school vs. the σ-essential cell

**Date:** 2026-06-19. **Target cell:** concrete (set-representable), σ-complete,
non-Boolean OML with a σ-additive state w that is contextual globally but
non-contextual on every finite sub-OML (σ-essential contextuality).

**Discriminator applied to every hit:** (a) σ-additive (not merely
finitely-additive) AND (b) finite-restriction-is-classical (contextuality
finitely witnessed ⟹ Wright-type near-miss, does NOT close).

**Verdict: NO killer paper found. The cell is open.** The Czech school work
clusters around adjacent-but-distinct objects (two-valued = dispersion-free
measures; Gudder's integral-additivity problem; full/finitely-additive state
spaces). The one solved-positive risk (realization theorems) misses on the
σ-complete + concrete conjunction.

---

## The precondition error to avoid

"Two-valued state" = **dispersion-free** ({0,1}-valued). A two-valued state is a
**vertex** of the dispersion-free hull, hence **non-contextual by definition**.
So any paper whose contextuality-relevant object is a two-valued state cannot
witness the cell — the contextuality precondition (a non-dispersion-free pure /
extreme state that two-valued states fail to span) never engages. "Concentrated"
(= Dirac δ_x at a point of Q) ≠ "two-valued": a state can be two-valued without
being concentrated, and it is still dispersion-free.

---

## Closest papers, with (a)/(b) status

### 1. Navara–Pták, "Two-valued measures on σ-classes," Čas. Pěst. Mat. 108 (1983) 225–229. [dml.cz/118163, full text read]
**MOST DANGEROUS-LOOKING, but does NOT close — rejected at the precondition.**
- σ-class (Def. 1) = exactly a σ-complete concrete logic (closed under
  complement + countable disjoint union). (a) ✓ — Def. 3 is genuine countable
  additivity.
- Central object: **two-valued (= dispersion-free) σ-additive measures**, and
  Gudder's question of whether ∫(f+g) = ∫f + ∫g. Theorem 1: additivity fails iff
  the measure on the finitely-generated sub-σ-class A_{f,g} is **not concentrated
  at a point**. The famous Example (Q = ℚ∩(0,1) squared; m supported on B,C,D
  with B∩C∩D=∅) is a two-valued σ-additive measure that is non-concentrated.
- Why it fails: non-concentrated ≠ contextual. The Example's measure is still
  two-valued = dispersion-free, hence non-contextual. The contextuality
  precondition never engages. (b) is moot.
- The Wright-type near-miss IS embedded here: the closing example (Q = {1..6},
  A = even-cardinality subsets, the **pure non-two-valued** measure m{a,b}=1/2)
  exhibits a pure state that two-valued states do NOT span ⟹ genuine
  non-spanning. But it is **finite** ⟹ fails (b). Wright-type.

### 2. de Simone–Navara–Pták, "States on systems of sets closed under symmetric difference," Math. Nachr. 288 (2015). + EQL line (arXiv 2401.13651, 2401.13798).
- Studies enriched quantum logics (Δ-closed = MO_n-type concrete logics). Has a
  σ-complete sub-strand ("interesting state properties"). BUT the state-space
  results in this line are **simplex** results and the contextuality-relevant
  examples (non-extending two-valued states; non-two-valued extreme states) are
  **finite** (Xeven, card X ≥ 6). Fails (b). The "simplex" framing further means
  spanning typically holds. Wright-type / non-witness.

### 3. de Simone–Navara–Pták, "Extending states on finite concrete logics," math-ph/0311012. [full text read]
- Explicitly **finite** (Xeven). Notes "extreme states on Xeven not two-valued"
  ⟹ non-spanning, but finite. Fails (b). Wright-type.

### 4. Müller, "Jauch–Piron states on concrete quantum logics," IJTP 32 (1993) 433–442.
- Non-Boolean concrete logic with all states Jauch–Piron. About JP property, not
  about σ-essential contextuality. Finite-flavored; no σ-additive contextual
  spanning-failure claim. Does not close.

### 5. Tkadlec; Svozil–Tkadlec (Greechie / KS-type, non-unital two-valued state sets).
- All **finite** Greechie diagrams. Finite ⟹ automatic fail of (b). Wright-type
  by construction (this is the generic case the cell is designed to exclude).

---

## The two real unclosed threats (neither is a two-valued-state paper)

### NEGATIVE direction (would close empty):
- **Navara–Rüttimann, "A characterization of σ-state spaces of OMLs," Expo. Math.
  9 (1991) 275–284.** Prime candidate for a theorem forcing σ-state spaces to be
  simplexes with dispersion-free vertices (⟹ no σ-additive contextuality ⟹ cell
  empty for σ-complete). **RESOLVED — does NOT close, on the verbatim theorem.**
  zbMATH review (Zbl 0742.03027), written by Pták himself: "Let P be an
  orthomodular poset and let S(P) (resp. S_σ(P)) denote the space of all states
  (resp. σ-additive states). The authors find an interesting convexity-theoretic
  characterization of S_σ(P) in S(P) (S_σ(P) is exactly an s-semi-exposed face in
  S(P))." So the result places S_σ(P) as a **semi-exposed face** of the full
  state space — a relative-position theorem. It does NOT force S_σ(P) to be a
  simplex and says nothing about dispersion-free vertices (a face of a non-simplex
  set is generally not a simplex). Negative-closure reading is killed on the
  theorem content, not on inference. Cell stays open.

### POSITIVE direction (solved-positive risk — outranks everything above):
- **Realization theorems:** "every compact convex set is affinely homeomorphic
  to the (full, finitely-additive) state space of an OML" — Navara–Rogalewicz
  (Demonstratio Math. 1988); Harding–Navara (Order 17, 2000, with prescribed
  center/automorphism group too). These realize **non-simplex** (hence
  contextual) state spaces.
- Why they do NOT (yet) close the cell — the two discriminators bite:
  (i) **σ-complete?** The constructions are finite-pasting / Greechie-diagram
      based. They are generically NOT σ-complete, and the realized state space is
      the **full = finitely-additive** state space. Whether the non-simplex
      survives restriction to σ-additive states is exactly the unaddressed point.
  (ii) **concrete?** Not guaranteed; pasting OMLs are typically not
      set-representable (Mayet–Navara 1995 give concreteness only for special
      K(L) forms).
  (iii) Even granting realization, finite-pasting ⟹ contextuality finitely
      witnessed ⟹ fails (b) unless the construction is genuinely infinitary.
- **No located paper realizes a non-simplex state space on an OML that is
  simultaneously concrete AND σ-complete.** That conjunction gap is precisely
  what keeps the cell open.

---

## Single most dangerous paper

**Navara–Rüttimann 1991, "A characterization of σ-state spaces of orthomodular
lattices" (Expo. Math. 9, 275–284)** — it directly characterizes the space of
σ-additive states, so it was the one paper that could close the cell NEGATIVELY.
**Now neutralized via the verbatim zbMATH review (Zbl 0742.03027, reviewed by
Pták):** the theorem only places S_σ(P) as a *semi-exposed face* of S(P); it does
not force a simplex or dispersion-free vertices. Does not close.

With that resolved, the **single largest remaining risk is the POSITIVE side**:
the Harding–Navara / Navara–Rogalewicz realization theorems. They realize
non-simplex (contextual) state spaces, but on the **finitely-additive** state
space of **finite-pasting/Greechie** OMLs — generically neither σ-complete nor
known-concrete, and the realized non-simplex may not survive restriction to
σ-additive states. The conclusion "does not close" rests on the known
pasting ⟹ not-σ-complete fact (fetches were blocked), not on the paper text;
the prior is strong and points the safe way, but is not theorem-verified here.
