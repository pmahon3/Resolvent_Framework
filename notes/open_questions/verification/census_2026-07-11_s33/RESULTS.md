# Session 33 census — results (2026-07-11)

> **s34 resolution of the late s33 alarm.** There is no bug in
> `relay_core.analyze.live` under the stated one-sided, any-position
> convention.  The proposed period-collapse and rotation tests silently
> replace the rooted chain by a two-sided/translation-invariant one, so
> their failure is expected.  The independent graph oracle
> `s34_liveness_oracle.py` agrees with `analyze.live` on all 4,150
> period-1 one/two-port maps and 600 sampled period-1/2/3 relays.  The
> alternative `live_fix.live_any` computes the different two-sided
> convention.  Therefore the liveness-dependent results below stand.

Corrected three-condition screen (attack §26 / HANDOFF s32) extended to
the next finite architectures. All numbers machine-produced; scripts in
this directory. `relay_core.py` reproduces every s32 number exactly
(`s33_reproduce_s32.py`) before any new census ran.

## Screen (recap)

For removable cluster state `s_*` (= pentagon all-odd state, support
`{a1,a3,a5,a7,a9}`) and target `D = a_0`, a relay must:
1. `s_*` has an all-zero-`D` infinite path (free state);
2. `s_*` is not σ-live (no exactly-one-`D` path through it);
3. the σ-live states order-determine the pentagon (0 false non-orders).
Survivors then face global (periodic) girth ≥5 and master-cycle girth ≥5.

## Reproduction of s32 (validation)

`4050 → 1000 valid → 275 s_*-self-loop → 45 non-live → 0 order-determining`,
exact. Live-size dist `{0:5,4:2,5:4,6:30,9:4}`; false-nonorder dist
`{4:4,55:30,65:2,71:2,102:2,350:5}`; root-only convention also 0. M* map
`{a1↔a5, a7↔a3}` gap distances `4,5,8,9,12,13` (g=1..6) — matches §25.

**Correction to the s32 "7 of 45 meet master-cycle girth" line.** No
single clean definition of master-cycle girth yields 7. Gap-distance
profiles over the 45: `(1,1,1,1,1,1)×5, (2,2,2,2,2,2)×34, (2,4,4,4,4,4)×2,
(3,2,3,2,3,2)×2, (4,2,4,2,4,2)×2`. Counts: `d_1≥4` → 2; `d_1≥3` → 4;
`some g d_g≥4` → 4; `min_g d_g≥3` → 0; `min_g d_g≥4` → 0. The "7" was a
loose/miscounted diagnostic; it was never load-bearing (all 45 already
fail condition 3 locally). Corrected figure: **0** meet `min_g d_g ≥ 4`
(the correct requirement, since gap distances are non-monotonic so the
shortest master Berge cycle is `min_g d_g + 1`).

## Route (a): two-cell gluings, k ≥ 3 identifications

Filter order per HANDOFF. Coverage is COMPLETE for two-cell route:

| k | maps | valid (girth≥5) | s_* free | non-live | order-det. survivors |
|---|------|-----------------|----------|----------|----------------------|
| 3 | 86,400 | 500 | 338 | 242 | **4** |
| 4 | 1,058,400 | 50 | 50 | 50 | 0 (all live-set empty) |
| 5 | 7,620,480 | 10 | 10 | 10 | 0 (all live-set empty) |
| ≥6 | — | **0** | — | — | — (no girth-valid map: 6 atoms force a co-block pair whose images exceed pentagon diameter) |

k=4,5 die AT the screen: s_* preservation forces the σ-live set empty
(dist `{0:50}`, `{0:10}`; false-nonorders 350). k≥6 is vacuous
(prefilter alone kills all maps, verified k=6..10).

**The four k=3 survivors pass the local screen but all die downstream**
(`s33_verify_survivors.py`; liveness independently cross-checked by
explicit lasso construction — automaton and lasso live-sets agree on all
four, all give σ-live set = the 10 non-`s_*` states, 0 false non-orders):

| survivor | global girth | shortest master cycle | verdict |
|----------|-------------|----------------------|---------|
| `(1,7),(3,1),(7,5)` | fails at window 3 | 4 | KILLED (girth) |
| `(1,7),(5,5),(9,1)` | passes (→ w12) | **3** | KILLED (master) |
| `(1,9),(5,5),(9,3)` | passes (→ w12) | **3** | KILLED (master) |
| `(3,5),(7,9),(9,3)` | fails at window 3 | 4 | KILLED (girth) |

Survivors 1&4: periodic chain grows a Berge 3/4-cycle by the third cell
(2-cell window girth is too local — the s24 global-girth lesson).
Survivors 2&3: `min_g d_g = 2`, so attaching the target-collecting master
block makes a Berge triangle; escape needs a spaced/multi-master, exactly
the s26 route killed in s27.

**Route (a) verdict: EXIT B.** Unlike k=2 (which died AT the screen),
k=3 admits screen-survivors — but none reaches a witness: two die at
global girth, two at master geometry. k=4/5 die at the screen; k≥6 empty.

## Route (b): three-pentagon period-3 relays

- **One-port relays: UNCONDITIONAL no-go.** Full product of all 100 valid
  1-port interfaces, 1,000,000 triples, no self-map cut: **0** phase-0
  survivors (hence 0 all-phase survivors). `s33_census_3cell.py`.
- **Two-port relays: design-class no-go** (full 1000³ = 10⁹ infeasible).
  Censused within the s32 removable-state design class (interfaces
  preserving `s_*`; the free non-live cluster state must survive): 275
  s_*-preserving interfaces, 275³ = 2.08×10⁷ triples. Result: **0
  survivors** at every phase (no-go within the design class).

Route (b) verdict: EXIT B for 1-port (unconditional); 2-port scoped to
the design class.

## Co-equal route (Exit C): removable FACE census on larger Greechie OMLs

`s33_face_census.py`. A removable FACE = a pairwise-incompatible atom
cluster `C` whose face `F(C) = {states with s(c)=1 ∀c∈C}` has **|F| ≥ 2**
and whose complement `Ω∖F(C)` still order-determines. Anchor verified:
pentagon = 11 states, odd-cluster isolates the unique removable `s_*`,
every other single state indispensable, **0 faces with |F|≥2** (the
pentagon is the degenerate zero-slack case).

Richer removable faces EXIST, abundantly, from the 6-loop up:

| OML | states | full-set OD | removable singletons | face-hits (|F|≥2) |
|-----|--------|-------------|----------------------|-------------------|
| 5-loop (pentagon) | 11 | yes | 11 | **0** |
| 6-loop | 18 | yes | 86 | 18 |
| 7-loop | 29 | yes | 210 | 154 |
| 8-loop | 47 | yes | 436 | 556 |
| 9-loop | 76 | yes | 837 | 1623 |
| pentagon+pendant block | 19 | yes | 82 | 41 |
| two pentagons sharing 1 atom | 128 | yes | 1242 | 4825 (faces up to |F|=10) |

Clean exemplar (7-loop, cluster `(0,3,11)`, |F|=3, supports
`{0,3,5,7,9,11}, {0,3,5,8,11}, {0,3,6,9,11}`): complement
order-determines, AND each face state is *individually* dispensable
(removing any one alone still order-determines), and no non-order is
witnessed only within the face. This is the "slack" the pentagon lacks.

**Exit C status: PRECONDITION ESTABLISHED, operative question OPEN.**
The face census answers "does a richer removable face exist?" (yes). It
does NOT answer the question the co-equal route is *for*: does the richer
face avoid the pentagon's liveness/separation tradeoff? That tradeoff is
dynamic (σ-liveness of an infinite relay), and the relay is unbuilt for
these OMLs. Individual dispensability is a *static* property; it is
suggestive, not probative. The discriminator to run next session:
generalize `relay_core`'s `succ`/`analyze` to the chosen OML, put the
whole face `F` in `s_*`'s role, define inter-cell ports, and run the
three-condition screen; the tradeoff is avoided iff some port makes
*every* face state non-σ-live while the complement stays σ-live and
order-determining.

## Files

- `relay_core.py` — pentagon + period-p relay automaton, girth, master gaps.
- `s33_reproduce_s32.py` — exact s32 reproduction (validation).
- `s33_census_k3plus.py` — route (a) k=3,4,5 census.
- `s33_verify_survivors.py` — adversarial kill of the 4 k=3 survivors
  (independent lasso liveness cross-check).
- `s33_census_3cell.py` — route (b) 1-port unconditional + 2-port design-class.
- `s33_face_census.py` — Exit C removable-face census.
- `s34_liveness_oracle.py` — independent finite-graph validation of the
  one-sided any-position liveness semantics.
