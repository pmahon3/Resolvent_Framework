## Audit: seed.md, "the universal Urysohn space U is oscillation stable" (mode: full)

Audit date per AS_OF.md: **2004-07-25**. Only sources dated on or before that day are used as prior art.
Sources were consulted 2026-10-26.

**AS_OF compliance note.** One search hit was arXiv:math/0407444 (Pestov, "Oscillation stability of the
Urysohn metric space", v1 dated 26 July 2004, v2 withdrawn). Its abstract matches the seed, so it is the
submission itself, and it is also dated after the audit date. I saw only the abstract page. I did **not**
use it, or its withdrawal, as evidence for anything below. The correctness finding rests only on the
elementary argument in §Correctness. I ignored post-2004 Urysohn-sphere papers (arXiv 0706.1326,
0710.2884, 1203.6024) as prior art. They surfaced in searches only.

### Declared contribution type(s): Type 1 (new theorem)

### Correctness (checked first, because it decides everything else)

**The central claim is false.** Here is a counterexample, using the seed's own definition and checked by hand:

1. *U is geodesic.* Take x, y ∈ U with d(x,y) = D. The one-point extension {x, y, m} with
   d(x,m) = d(m,y) = D/2 is a metric space, so U's extension property realises m in U. A complete metric
   space with midpoints has an isometric segment between any two points: take dyadic midpoints, then pass
   to the completion. So U is path-connected, and so is every isometric copy Y ⊂ U of U.
2. *Every copy is unbounded.* U is unbounded, because extension gives points at any prescribed distance.
   So Y is unbounded too.
3. Fix x₀ ∈ U and put h(x) = d(x₀, x), which is 1-Lipschitz. On Y, h is continuous and Y is connected, so
   h(Y) is an interval. Since d(y,y') ≤ h(y) + h(y'), h is unbounded on Y. Hence h(Y) ⊇ [a, ∞) for some a.
4. Let g(t) = dist(t, 2ℤ). It takes values in [0, 1], is 1-Lipschitz, and reaches both 0 and 1 on every
   half-line. Put **f = g ∘ h**. Then f is bounded and 1-Lipschitz, hence uniformly continuous, and
   **osc(f|Y) = 1 for every isometric copy Y of U**. So the definition fails for every ε < 1.
5. The derived Ramsey statement also fails. Colour x by the parity of ⌊h(x)⌋. For δ < 1/2, the
   δ-neighbourhood of either colour class misses an interval of h-values in every period, and h(Y) covers
   a half-line. So no copy Y lies within δ of a single colour class.

The obstruction is trivial: U is unbounded and connected, so "distance to a point, read modulo 2"
oscillates fully on every copy. The sketched method ("control f on a finite configuration, iterate along an
exhaustion") cannot work as described. The step of iterating along an exhaustion is where a proof has to
break, because finite-configuration control (as in Pestov 2002, Cor. 6.11–6.12) does not stop drift in
d(x₀, ·) across the infinite copy. The seed gives no proof to locate the error more precisely.

The counterexample uses only that U is unbounded. That motivates asking the question for a bounded
Urysohn-type space instead (e.g. the universal space of bounded diameter). That is a different statement,
and the seed does not make it.

### Pure Verdict: not evaluated (novelty moot), CENTRAL CLAIM FALSE
- No source on or before 2004-07-25 states the claimed theorem. Searched: "oscillation stable" with
  Urysohn, distortion, approximate indivisibility, Ramsey with tolerance.
- Nearest prior work:
  - **Pestov, "Ramsey–Milman phenomenon, Urysohn metric spaces, and extremely amenable groups",
    Israel J. Math. 127 (2002) 317–357; arXiv math/0004010 (v1 Apr 2000, rev. Jul 2003; predates).**
    Read level: full text skimmed via ar5iv, targeted at the relevant sections. Owns extreme amenability of
    Iso(U) and the finite Ramsey-with-tolerance results for embeddings of a *finite* F into U
    (Cor. 6.11, 6.12). It contains no oscillation-stability claim and no open question about U in the part
    I read (§7 asks only about links to Euclidean Ramsey theory).
  - **Odell–Schlumprecht, "The distortion problem", Acta Math. 173 (1994)** (predates). Read level:
    citation only. Distortion of the Hilbert sphere, the contrast case.
- Not a novelty failure but a **correctness failure**: the theorem as stated is refuted by a
  3-line argument.

### Applied Verdict: not evaluated (no Type 7 claimed; pure mathematics)

### Contribution Type Verdicts (mode=full):
**Type 1 (new theorem): FAIL.** The bar needs "a previously unknown *true* statement with proof." The
statement is false (counterexample above), and the seed sketches a proof but does not give one.

No other types were declared. For completeness:
- Type 5 would apply only to the *negation*. The negation is trivial (above), so it would fail
  "trivial consequence".
- Type 2 does not apply.

### Cross-reference
Novelty and correctness do not interact here: the claim is new only because it is false. The surviving
ingredients (finite-configuration Ramsey control in U) are owned by Pestov 2002.

### Recommendation
**Park (kill).** Type 1 was evaluated and fails on correctness. A live redirect would be to restate the
question for a bounded Urysohn-type space (e.g. the universal space of bounded diameter) and supply an actual proof.
That would be a new seed needing its own audit.

**Bearing on WHY.md (one line):** a hidden idealisation. "Every copy looks locally the same" is defeated by
one global coordinate (distance to a fixed point) that no local view controls. Local agreement does not add
up to one flat world when the space is unbounded and connected.

### Referee estimate: REJECT-LIKELY
Venue class: none
Value carried by: none (the central claim is wrong)
Main risk a referee would raise: The theorem is false. f(x) = dist(d(x₀,x), 2ℤ) is bounded and 1-Lipschitz,
and has oscillation 1 on every isometric copy of the connected, unbounded space U.
