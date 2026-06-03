"""
Middle-way check, step 1: is PR_dual INHABITED in a non-distributive case?

Context. The proposed subsumption stratifies "PR" into two grades:
  PR_lattice(s): a sigma-additive measure on the lattice A agreeing with s
                 (for L(H): Gleason's Born measure — always, for sigma-add s).
  PR_dual(s):    a (sigma-additive Borel) measure mu_hat on S_0(A) with
                 mu_hat(h(a)) = s(a) AND concentrating on P(A).
Claim of the middle way: PR_dual ⊊ PR_lattice, equiv under distributivity,
strictly separated by non-distributivity, with L(H) the witness (#1 = the
strict gap).

BEFORE proving the containment, the advisor's gate: is PR_dual even
NON-EMPTY for a non-distributive OML? If PR_dual holds only in the Boolean
case, the refinement collapses to "s is Boolean-like" and does no OML work —
the middle way would be a relabeling, not a theorem.

This script works the FINITE case, where there is no countable-join
subtlety: every filter is principal, F(A) is finite, P(A) = F(A) minus the
improper filter, "concentration on P(A)" = "no mass on the improper point",
and a Borel measure on the (finite, discrete) S_0(A) is just a weight vector
on filters. PR_dual then = a nonneg weight w on proper filters with, for
every a, sum_{x: a in x} w(x) = s(a), and total mass 1.

We test MO_2 (smallest non-distributive OML) and a state s, and ask the LP:
does such a w exist? This is the FINITE shadow of PR_dual. If YES for some
non-distributive (A, s), PR_dual is inhabited beyond Boolean and the middle
way has a chance. If NO for all states (as on MO_3, cf. mo3_extension.py),
the finite non-distributive case is already empty and we learn the gap is
even wider than thought.

NOTE on what this does and does NOT settle:
  - Finite ⟹ every filter principal ⟹ the h(.) cover the space and the
    "defect set D" (the live worry in the infinite case) is EMPTY here.
    So a YES here does NOT establish the infinite containment; it only
    tells us PR_dual is not vacuously Boolean-only at the finite level.
  - The real subtlety (mu_hat(D) = 0, D containing limit principal filters)
    is purely infinite-dimensional and is the NEXT step, not this one.

RESULT (2026-06-03): PR_dual is EMPTY on MO_2 for EVERY state, AND the
concentration constraint w(omega)=0 turned out VACUOUS — h(0)=s(0)=0 already
forces w(omega)=0, so dropping concentration gives the identical infeasible
LP. CONCLUSION: in finite dimensions "descent/concentration" has NO content
(the only non-principal point is omega, already killed by s(0)=0), so this
LP tested PURE EXTENSION (#3) and failed for the meet-zero reason
(4 pairwise-meet-zero atoms, Sum s = 2 > 1). It re-derives MO_3, and says
NOTHING about descent.

STRUCTURAL VERDICT (why the finite test cannot decide the middle way):
PR_dual = extension (#3/#1) + descent (#2). The descent component only has
content in INFINITE dimensions, where free (non-principal proper) filters
exist that can carry mass without being forced null (the OML analogue of
free ultrafilters). But that regime is exactly where #2 bites: descent is
not rigorously STATABLE for infinite OMLs (MB duality finitary, no
sigma-Loomis-Sikorski). So PR_dual has no regime where it is BOTH
well-defined AND distinct from the extension axis:
  - finite  ⟹ descent vacuous ⟹ PR_dual ≡ extension;
  - infinite ⟹ descent not statable (#2);
  - L(H) normal states ⟹ fails at the extension step (#1) before descent.
Hence PR_lattice/PR_dual is HONEST BOOKKEEPING (lets one assert both (a)
Gleason-on-the-lattice and (b) dual-space-failure without suppressing
either), but NOT a new theorem: PR_dual repackages the two-axis split in
EA/PR/VDR vocabulary; it clears the "new vocabulary" bar only if some
non-distributive OML+state EXTENDS but fails to CONCENTRATE — a case #2 says
cannot yet even be stated. The only candidate is the singular-state sliver
from #1, which runs into the #2 statability wall. Conjecture, not theorem.
"""

import itertools
import numpy as np
from scipy.optimize import linprog


# ---- MO_2 as a finite OML: 0, 1, and atoms p,p',q,q' ----
# Order: 0 < each atom < 1. Complementary pairs (p,p'), (q,q').
# Orthogonality: p ⊥ p', q ⊥ q' ONLY (cross pairs meet to 0 but are NOT ⊥).
ELEMENTS = ['0', 'p', "p'", 'q', "q'", '1']
ATOMS = ['p', "p'", 'q', "q'"]
COMP = {'p': "p'", "p'": 'p', 'q': "q'", "q'": 'q', '0': '1', '1': '0'}


def leq(a, b):
    """Partial order on MO_2."""
    if a == '0' or b == '1':
        return True
    if a == b:
        return True
    return False


# ---- Filters on MO_2 ----
# A filter: nonempty, upward closed, closed under meet, proper-or-not.
# On MO_2 the proper filters are exactly the principal up-sets of each
# nonzero element: ↑1, ↑p, ↑p', ↑q, ↑q'  (↑atom = {atom, 1}), plus the
# improper filter = all of A (the ω point / contains 0).
def up(a):
    return frozenset(e for e in ELEMENTS if leq(a, e))


PROPER_FILTERS = {a: up(a) for a in ['1', 'p', "p'", 'q', "q'"]}   # principal, proper
IMPROPER = frozenset(ELEMENTS)                                      # contains 0
ALL_FILTERS = dict(PROPER_FILTERS)
ALL_FILTERS['omega'] = IMPROPER

# h(a) = { filter x : a in x }, over ALL filters (incl. improper).
def h(a):
    return [name for name, x in ALL_FILTERS.items() if a in x]


def pr_dual_feasible(s):
    """LP: weights w on ALL filters, w>=0, sum=1, mu_hat(h(a))=s(a) for all
    a in A, AND concentration: w(omega)=0 (no mass off P(A))."""
    names = list(ALL_FILTERS.keys())
    idx = {n: i for i, n in enumerate(names)}
    n = len(names)
    A_eq, b_eq = [], []
    # mu_hat(h(a)) = s(a) for every element a (0 and 1 included)
    for a in ELEMENTS:
        row = [0] * n
        for fn in h(a):
            row[idx[fn]] = 1
        A_eq.append(row)
        b_eq.append(s[a])
    # total mass 1
    A_eq.append([1] * n); b_eq.append(1.0)
    # concentration on P(A): no mass on the improper filter
    row = [0] * n; row[idx['omega']] = 1
    A_eq.append(row); b_eq.append(0.0)
    res = linprog(c=[0] * n, A_eq=np.array(A_eq), b_eq=np.array(b_eq),
                  bounds=[(0, None)] * n, method='highs')
    return res.success, names, (res.x if res.success else None)


def make_state(sp, sq):
    """State on MO_2: s(0)=0, s(1)=1, s(p)+s(p')=1, s(q)+s(q')=1."""
    return {'0': 0.0, '1': 1.0,
            'p': sp, "p'": 1 - sp, 'q': sq, "q'": 1 - sq}


def main():
    print("MO_2 filters (proper, principal):", list(PROPER_FILTERS.keys()))
    print("h(a) for each atom:")
    for a in ATOMS:
        print(f"  h({a}) = {h(a)}")
    print()

    found = []
    grid = np.linspace(0, 1, 11)
    for sp in grid:
        for sq in grid:
            s = make_state(sp, sq)
            ok, names, w = pr_dual_feasible(s)
            if ok:
                found.append((round(sp, 2), round(sq, 2)))
    print(f"PR_dual feasible for {len(found)} / {len(grid)**2} states on MO_2.")
    if found:
        print("  e.g. states (s(p), s(q)):", found[:8], "..." if len(found) > 8 else "")
        # show a witness explicitly
        s = make_state(*[v for v in found[len(found)//2]])
        ok, names, w = pr_dual_feasible(s)
        print(f"\n  Witness state s(p)={s['p']}, s(q)={s['q']}:")
        for nm, wv in zip(names, w):
            if wv > 1e-9:
                print(f"    w({nm}) = {wv:.3f}")
        print("  -> PR_dual is INHABITED on MO_2 (non-distributive). Not Boolean-only.")
    else:
        print("  PR_dual EMPTY on MO_2 — the gap is wider than thought.")

    # Contrast: the deterministic/extreme state s(p)=1, s(q)=1
    print()
    s = make_state(1.0, 1.0)
    ok, _, w = pr_dual_feasible(s)
    print(f"Extreme state s(p)=s(q)=1: PR_dual feasible = {ok}")
    # Contrast: maximally mixed s(p)=s(q)=1/2
    s = make_state(0.5, 0.5)
    ok, _, w = pr_dual_feasible(s)
    print(f"Maximally mixed s(p)=s(q)=1/2: PR_dual feasible = {ok}")


if __name__ == "__main__":
    main()
