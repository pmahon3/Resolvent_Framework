## Audit: `notes/covered_leads/distributed_sensor_contextuality.md` (mode: full, skill v2.1)

*Re-audit 2026-10-26. reviewed: false. Claude (opus), forked audit. The verdict below was formed from
the seed's own claims (lines 1–123) before reading its 2026-06-06 park verdict (lines 124–180). The
comparison is at the end.*

### Declared contribution type(s)
Type 1 (new theorem), *conditional* on building a non-co-realizable multi-sensor family with a
load-bearing non-distributive context logic. Type 3 (unifying framework) as fallback: a
reconstruction/prediction statement provable via the OML dual that is false or unstateable on every
classical joining. Types 4 and 6 are explicitly not claimed. The declaration is well formed.

**Status of the seed: no construction was ever built.** Steps 1–3 of its "Open / next" are all
unexecuted. The audit therefore assesses (i) whether the *target* statement is owned, and (ii) for the
referee estimate, the best-case write-up: a 2-sensor non-co-realizable example, its MO₂ context
logic, and the Paper II forcing applied to it.

### Shelf-first record (CLAUDE.md rule)
I grepped `SHELF_INDEX.json` before searching the web. Hits used here: Abramsky–Brandenburger 2011
(entry 3); Morton 2017 (entry 83); Atserias–Kolaitis 2020 (entry 119, Vorob'ev and BFMY);
Dzhafarov–Kujala CbD (entries 38 and others, `by_question/asynchrony`); Kalmbach 1983 (the Greechie
loop lemma); Shultz 1974; Minguzzi 2005 (`by_question/asynchrony`); Abramsky–Barbosa partial Boolean
algebra duality (entry 1). Every PDF already on the shelf. No new lead was announced that the shelf
already held.

**Read levels:**
- Morton 2017: abstract and introduction, pp. 1–3 (**beyond abstract**).
- Abramsky–Brandenburger 2011: table-of-contents and keyword grep of the shelf PDF only.
- Atserias–Kolaitis 2020: abstract and introduction (grep, shelf PDF).
- Abramsky, "Relational databases and Bell's theorem", arXiv:1208.6416: abstract only (web).
- Gunji et al. 2026, arXiv:2603.22353: abstract only (web, arXiv abs page).
- Robinson, "Sheaves are the canonical datastructure for sensor integration", arXiv:1603.01446:
  search snippet only.
- Kalmbach 1983 (Greechie pasting and loop lemma), Shultz 1974, Minguzzi 2005: shelf-index
  `what_it_proves` entries only.
- Gleason / Kochen–Specker: standard results, from memory.

### Pure Verdict: KNOWN

Strip the vocabulary first. The seed fuses two claims that come apart.

**(A) "The context logic of a sensor family is non-distributive (contains MO₂)."** This is cheap and
it says nothing about the data. Take any two binary settings that are never co-deployed. Their event
algebras paste along {0,1} into MO₂. That logic exists *whether or not* the data admit a joint law.
It is a fact about which questions can be asked together, not about the answers.
- Owner: Greechie pasting of Boolean blocks (Kalmbach 1983, shelf; loop lemma, Sec. 4 Lemma 9), and
  the Kochen–Specker partial Boolean algebra (Abramsky–Barbosa duality, shelf entry 1).
- Recent categorical restatement: Gunji, Ohzawa, Tokuyama, Huang, Nakamura, arXiv:2603.22353 (2026).
  It obtains the non-distributive OML as a pushout of Boolean contexts along {0,1}, left adjoint to
  the Boolean-subalgebra functor, and links non-Booleanity to absence of global sections.
- So the seed's stress test ("is the non-distributivity load-bearing or imported?") answers itself:
  for a pasting, it is always imported from the choice of co-deployability, never forced by the
  dynamics.

**(B) "There is provably no probability space carrying all the sensors' data."** This is the actual
content, as the seed itself says ("That is the whole technical content"). It is owned three times
over.
- **Morton 2017**, arXiv:1708.03264, read beyond the abstract. Contextuality "formally identical to …
  Bell's Theorem" arises from purely classical distributed data collection. One mechanism is missing
  data (§2). Another is write skew under snapshot isolation in low-latency distributed databases
  (§3), with "spatially separated" agents, "speed-of-light constraints", interval time and clock
  divergence from a common reference (§4), all in the Abramsky sheaf framework (§6). **This is the
  seed's "no common dynamical clock" mechanism, already in print, in a distributed setting.**
- **Abramsky 2013** (arXiv:1208.6416): local hidden-variable realizability ⟺ the database admits a
  universal relation. Classical relational data can be contextual.
- **Vorob'ev 1962 / Beeri–Fagin–Maier–Yannakakis 1983** (via Atserias–Kolaitis 2020, shelf):
  pairwise-consistent local laws always glue iff the schema is acyclic (Vorob'ev-regular). Cyclic
  schemas give consistent-but-unglueable instances. This answers "when is a sensor family
  non-co-realizable" at the level of the overlap pattern.
- **Contextuality-by-Default** (Dzhafarov–Kujala, shelf): the systematic treatment of "no joint
  distribution across contexts" for real, classical, inconsistently connected data. It also
  separates real contextuality from disturbance, which is exactly the trap a stale-clock sensor model
  falls into.
- The seed's own "Kolmogorov obstruction" is the standard dichotomy. Sensors are either draws on one
  space, and then they co-realize, or their data violate a consistency or Vorob'ev condition, and
  then the case is (B) above. No third, dynamical route is suggested.

**The asynchrony mechanism, checked separately.** Minguzzi 2005 (shelf, `by_question/asynchrony`)
shows that non-synchronizability of clocks around a loop is a *holonomy* of the simultaneity
connection. That is a classical gauge twist. A gauge twist alone does not give non-co-realizable
statistics: a rotating frame's clocks still sit on one spacetime and one probability space. So "no
common clock" yields contextuality only through the data-versioning route Morton already gives. The
mechanism is owned or empty, not a new door. ⟦HAND — scoping, not a theorem⟧

Verdict: **KNOWN.** (B) is owned by Morton 2017, Abramsky 2013, Vorob'ev/BFMY and CbD. (A) is owned by
Greechie/Kalmbach, and recently by Gunji et al. 2026. No residual statement survives.

### Applied Verdict: FAIL
- **Decision test:** nothing changes for a practitioner. Sheaf-based sensor fusion (Robinson,
  arXiv:1603.01446, snippet only) already treats "can these sensor readings be assembled into one
  consistent state?" as a global-section problem, with a quantitative consistency radius.
- **Practitioner hostility test:** "I already compute a consistency radius / run a CbD or Vorob'ev
  check. What does the OML add?" The seed has no answer.
- No computational comparison exists, and none is proposed.

### Contribution Type Verdicts

**Type 1 (new theorem): FAIL.** This fails twice.
1. *Structurally, before prior art:* the bar asks for a non-distributive logic "not removable by a
   common joining". Part (A) is free and independent of joinability. Part (B) is the only content,
   and it is the classical marginal / no-global-section problem.
2. *Prior art:* (B) in a distributed classical setting is Morton 2017. The general case is Abramsky
   2013, AB 2011 and Vorob'ev 1962.

**Type 3 (unifying framework): FAIL.** This fails independently of any owner: the transfer has no
engine.
- The seed's transfer runs through "the OML dual (McDonald–Bimbó, Gleason descent)". Gleason needs
  L(H) with dim H ≥ 3.
- A sensor-generated logic is a finite (or blockwise) Greechie pasting, not L(H). Its states are
  exactly the block-compatible families of block measures: the no-disturbance polytope that AB 2011
  already describe as compatible families on the presheaf.
- Shultz 1974 (shelf): every rational polytope is the state space of a finite OML. The OML state
  space is therefore an arbitrary polytope carrying no extra structure for a prediction statement.
- So any "prediction provable via the OML dual" is a statement about the no-disturbance polytope
  versus the local polytope. That is stateable, and stated, in standard contextuality vocabulary, so
  the bar "false or unstateable on any classical joining" cannot be met by the OML route itself.
- Paper II's forcing (non-distributive ⟹ VDR blocked) applied to such a pasting is the identity
  "no global section ⟹ no single classical joining". That is a restatement, not a transfer.
  ⟦HAND⟧

Types 2, 4, 5, 6, 7: not claimed. Unprompted, a Type 5 reading ("time-series sensors cannot force
non-Booleanity beyond the marginal problem") would rephrase Kolmogorov/Vorob'ev, so it also fails.

### Cross-reference
The components are known, and there is no assembly, because the seed never built its object. Both of
its fallbacks collapse onto one owned region: the classical marginal problem / absence of global
sections (Vorob'ev → BFMY → Abramsky–Brandenburger → Morton → CbD). The OML layer is decorative here,
in the same sense as the five earlier "decorative-σ/OML" deaths: pasting supplies the
non-distributivity, and states on pastings carry no Gleason-type rigidity.

**Seam-map update (`owned_by` regions, for whoever next edits a taxonomy; not edited here):**
- *Classical distributed-data contextuality (no common clock / versioning / missing data):*
  owned_by Morton 2017, arXiv:1708.03264, §§2–4, 6. Verified: shelf PDF, introduction read.
- *Non-distributive logic generated by gluing Boolean contexts:* owned_by Greechie pasting (Kalmbach
  1983) and Gunji–Ohzawa–Tokuyama–Huang–Nakamura 2026 (arXiv:2603.22353). Verified: Gunji abstract
  only.

**Citation error found (not fixed; edit scope = this file only).**
`notes/literature_review/references.bib` (lines ~122–127) lists the authors of arXiv:2603.22353 as
"Gunji, Haruna, Uragami". The arXiv abs page lists **Gunji, Ohzawa, Tokuyama, Huang, Nakamura**, and
the full title is "Contextuality as a Left Adjoint: A Categorical Generation of Orthomodular
Structure". The same entry probably recurs in `notes/knowledge_map/references.bib` and
`papers/paper_ii/references.bib`, which also cite it. Paper II must be fixed before any submission.

### WHY bearing (one line)
This is the "do local views add up to one world?" question for sensors, and the answer was already in
print: views glue on trees and can fail on loops of overlap. The loop lives in the data's overlap
pattern (Vorob'ev), not in any quantum-logic layer.

### Recommendation
**Park stands.** Types evaluated: 1 and 3 (claimed), 7 (applied, run in full mode). Bars failed:
- Type 1: structurally, because part (A) is free and part (B) is the marginal problem, and on prior
  art (Morton 2017; Abramsky 2013; Vorob'ev).
- Type 3: no transfer engine, since Gleason is unavailable on pastings and the state space is the
  no-disturbance polytope.
- Type 7: no decision change versus sheaf fusion or CbD.

The open-question exit fails criterion (a), because the question is owned.

Do not re-parent this seed into `glued_carriers_taxonomy.json` as a rescue. The finite
merging/marginal version of the question already lives there, and WHY.md (2026-10-26 correction)
records its threshold as owned (Sullivant 2006). One cross-reference line is enough.

### Referee estimate: REJECT-LIKELY
Venue class: none
Value carried by: none
Main risk a referee would raise: classical distributed-data contextuality (no common clock,
versioning) is Morton 2017 and Abramsky 2013 (databases), and is not credited. The OML/MO₂ layer is a
Greechie pasting that adds no statement beyond the no-disturbance versus local polytope.

*Caps applied:*
- Pure is KNOWN, not UNCLEAR, so cap 1 does not bind.
- Cap 3 binds: the owner of the main result (Morton 2017) is in print and uncredited, and no
  substantial residual remains.
- Cap 2 is moot. Even so, the nearest owner was read beyond the abstract.
- The best-case write-up (a 2-sensor example plus MO₂ plus the Paper II forcing) would at most be a
  re-instance of Morton §3.
- For an expository venue (factor 4), it would duplicate Morton and Abramsky's accessible
  expositions without added organisation.

---

## Comparison with prior audit (2026-06-06 park verdict, seed lines 124–180)

*Read after the verdict above was written.*

**Agreement.** Both audits reach the same verdict: Pure KNOWN, Type 1 FAIL, Type 3 FAIL, PARK. Both
locate the kill at the seed's own pre-registered test ("load-bearing or imported?"). Both find that
non-distributivity on a sensor family is *imposed* through the choice of incompatible contexts,
never forced by the dynamics. Gunji et al. 2026 appears in both.

**What the prior audit had and this one did not find independently:**
- **Evangelou-Oost, Bannister, Hayes, "Contextuality in distributed systems", arXiv:2210.09476.**
  I checked it after reading the prior verdict, abstract only. It covers contextuality for
  distributed programs modelled by relative execution traces with *no global clock*, failure of a
  sequential-consistency-type criterion, in the Abramsky framework, Isabelle-verified. This is a
  second owner of the "no common clock" engine, independent of Morton 2017. It strengthens cap 3.
  It is **not on the shelf.** Per the shelf rule, it should get a PDF and an index entry if it is
  ever cited.
- **Fine 1982** (joint distribution ⟺ factorizability) is named as the theorem behind the
  Kolmogorov obstruction. I stated the same dichotomy without naming Fine.
- **Foulis–Randall test spaces** as the operational-logic owner of (A). This is the same region as my
  Greechie/Kalmbach citation, from the empirical-logic side.

**What this audit adds:**
- **Morton 2017 (arXiv:1708.03264), on the shelf and read beyond the abstract,** is absent from the
  prior verdict. It is the closest owner for the *sensor/data* reading: classical, spatially
  distributed data agents, versioning and snapshot isolation, clock divergence. With 2210.09476 it
  makes the "no common clock" route doubly owned.
- **The Type 3 kill without any owner:**
  - Gleason is unavailable on Greechie pastings.
  - Shultz 1974 gives every rational polytope as a finite-OML state space.
  - So the "OML dual" can only restate the no-disturbance versus local polytope.
  The prior audit killed Type 3 by inhabitation, meaning the transfer was already built by Gunji
  et al. This audit also shows that the transfer could not have delivered the seed's bar
  ("unstateable on any classical joining") even if it had been unbuilt.
- **Minguzzi 2005 (shelf):** clock non-synchronizability around a loop is a classical holonomy, a
  gauge twist. On its own it gives no non-co-realizable statistics.
- **Citation error:** the repo bib lists the authors of 2603.22353 as "Gunji, Haruna, Uragami". arXiv
  lists Gunji, Ohzawa, Tokuyama, Huang, Nakamura. The prior verdict avoided authors, but the bib
  feeds Paper II.
- **The referee estimate**, which the prior audit predates (v2.1 caps).

**Where the prior audit is slightly overstated.**
- "Non-co-realizable family → no global joint IS the definition of contextuality" is right in
  substance. The seed, however, asked for a *dynamical* mechanism, and the precise owner of that is
  Morton / Evangelou-Oost et al., not AB 2011 alone.
- "Every level … already built" holds, but the Gunji pushout is an existence/adjunction statement
  (abstract only, in both audits). Calling it "Paper II §7 … as a general theorem" is a reading
  neither audit has verified from the full text. It does not affect the verdict, since Type 3 fails
  regardless.

**Prior "cashable fallback" (Paper II §3 scope caveat).** Still correct and still owed, as far as this
audit can see; I did not check whether it was applied. Suggested addition to that caveat: cite Morton
2017 and arXiv:2210.09476 as the places where distributed-systems contextuality is actually worked
out.

**Should the park change? No.**
- The programme verdict is unchanged.
- The referee estimate is REJECT-LIKELY with venue none. Owners are in print (Morton 2017;
  Evangelou-Oost et al. 2022; Abramsky 2013), and the best-case write-up leaves no residual.
- The v2.1 caps, applied strictly, agree with the programme bar here. This is not a case where
  community practice is more lenient than the programme.
