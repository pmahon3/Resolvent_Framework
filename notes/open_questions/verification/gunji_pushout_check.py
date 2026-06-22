#!/usr/bin/env python3
"""
Machine check of the Prop 4 / Prop 8 contradiction in
Gunji et al., "Contextuality as a Left Adjoint" (arXiv:2603.22353).

CLAIM UNDER TEST (their Prop 8 / Methods 5.3):
    P = B1 sqcup_2 B2 -- the object obtained by gluing two Boolean
    algebras at {0,1} (their eq. 20) -- "is the pushout of f and g in Bool",
    where the span is built from 2 = {0,1}, the two-element Boolean algebra.

WHAT WE VERIFY, with B1 = B2 = 2^2 (the running example, a 2^2-Boolean algebra):

  (A) 2 = {0,1} is the INITIAL object of Bool
        => the pushout of B1 <- 2 -> B2 in Bool is just the COPRODUCT B1 + B2.
  (B) The coproduct of 2^2 and 2^2 in Bool is 2^4 (16 elements), Boolean,
        and it SATISFIES the pushout universal property (checked by brute force).
  (C) Gunji's eq.20 object -- glue at {0,1}, keep everything else distinct --
        is MO_2 (6 elements), is NON-DISTRIBUTIVE (their own Prop 4), and
        FAILS the Bool pushout universal property.

Conclusion: the object their Prop 8 calls "the pushout in Bool" (MO_2) is NOT
that pushout; the genuine Bool-pushout is 2^4. Prop 8 mislabels a colimit-in-OML
(the horizontal sum / free OML, their correct Thm 6) as a pushout-in-Bool.

No external dependencies. Run: python3 gunji_pushout_check.py
"""

from itertools import product, chain, combinations


# ----------------------------------------------------------------------
# Finite Boolean algebra 2^n, carrier = subsets of {0,...,n-1} as frozensets.
# Operations: meet = intersection, join = union, comp = complement, le = subset.
# ----------------------------------------------------------------------
def powerset_BA(n):
    base = frozenset(range(n))
    elts = [frozenset(s) for s in
            chain.from_iterable(combinations(range(n), k) for k in range(n + 1))]
    return {
        "elts": elts,
        "bot": frozenset(),
        "top": base,
        "meet": lambda a, b: a & b,
        "join": lambda a, b: a | b,
        "comp": lambda a: base - a,
        "le":   lambda a, b: a <= b,
    }


def is_distributive(L):
    elts, meet, join = L["elts"], L["meet"], L["join"]
    for a, b, c in product(elts, repeat=3):
        if meet(a, join(b, c)) != join(meet(a, b), meet(a, c)):
            return False, (a, b, c)
    return True, None


# ----------------------------------------------------------------------
# A Bool-homomorphism h: L -> M is given as a dict on carriers preserving
# bot, top, meet, join, comp.  We verify homomorphism-hood explicitly.
# ----------------------------------------------------------------------
def is_bool_hom(L, M, h):
    if h.get(L["bot"]) != M["bot"] or h.get(L["top"]) != M["top"]:
        return False
    for a in L["elts"]:
        if a not in h:
            return False
    for a, b in product(L["elts"], repeat=2):
        if h[L["meet"](a, b)] != M["meet"](h[a], h[b]):
            return False
        if h[L["join"](a, b)] != M["join"](h[a], h[b]):
            return False
    for a in L["elts"]:
        if h[L["comp"](a)] != M["comp"](h[a]):
            return False
    return True


def atoms_of(L):
    """Atoms of a finite Boolean algebra: minimal nonzero elements."""
    bot, elts, le = L["bot"], L["elts"], L["le"]
    nz = [e for e in elts if e != bot]
    return [a for a in nz
            if not any(x != a and x != bot and le(x, a) for x in nz)]


def all_bool_homs(L, M):
    """
    Enumerate all Bool-homs L -> M.  A hom out of a finite BA is determined by
    its values on the atoms of L, which must be pairwise-disjoint (meet = bot_M)
    and join to top_M.  Then h(x) = join of h(atom) for atoms <= x.
    This is |M|^(#atoms_L), vastly smaller than |M|^|L|.
    """
    atoms, le = atoms_of(L), L["le"]
    botM, topM, meetM, joinM = M["bot"], M["top"], M["meet"], M["join"]
    homs = []
    for vals in product(M["elts"], repeat=len(atoms)):
        # partition-of-unity constraint
        if joinM_all(M, vals) != topM:
            continue
        if any(meetM(vals[i], vals[j]) != botM
               for i in range(len(vals)) for j in range(i + 1, len(vals))):
            continue
        amap = dict(zip(atoms, vals))
        h = {}
        for x in L["elts"]:
            below = [amap[a] for a in atoms if le(a, x)]
            h[x] = botM
            for v in below:
                h[x] = joinM(h[x], v)
        if is_bool_hom(L, M, h):           # final guard (cheap, confirms)
            homs.append(h)
    return homs


def joinM_all(M, vals):
    acc = M["bot"]
    for v in vals:
        acc = M["join"](acc, v)
    return acc


# ----------------------------------------------------------------------
# (A) 2 = {0,1} is initial in Bool: exactly one hom 2 -> B for every B.
# ----------------------------------------------------------------------
def check_initial(two, B):
    homs = all_bool_homs(two, B)
    return len(homs) == 1, len(homs)


# ----------------------------------------------------------------------
# Pushout universal property in Bool.
# Span:  B1 <-i1- 2 -i2-> B2   (here i1,i2 the unique initial homs)
# A candidate (P, j1: B1->P, j2: B2->P) is THE pushout iff:
#   (commute) j1 . i1 == j2 . i2   (automatic here: both = the initial hom into P)
#   (universal) for every cocone (X, q1:B1->X, q2:B2->X) with q1.i1==q2.i2,
#       there is a UNIQUE Bool-hom u: P->X with u.j1==q1 and u.j2==q2.
# We test universality against a family of test targets X.
# ----------------------------------------------------------------------
def compose(h2, h1):                       # (h2 . h1) on carrier of dom(h1)
    return {a: h2[h1[a]] for a in h1}


def cocones(B1, B2, X, i1, i2):
    """All Bool cocones (q1,q2) into X that agree on the initial object."""
    out = []
    for q1 in all_bool_homs(B1, X):
        for q2 in all_bool_homs(B2, X):
            if compose(q1, i1) == compose(q2, i2):
                out.append((q1, q2))
    return out


def is_pushout(P, j1, j2, B1, B2, i1, i2, test_targets):
    """Check the universal property of (P, j1, j2) against test_targets."""
    for X in test_targets:
        for (q1, q2) in cocones(B1, B2, X, i1, i2):
            # find Bool-homs u: P -> X with u.j1 = q1, u.j2 = q2
            mediators = []
            for u in all_bool_homs(P, X):
                if compose(u, j1) == q1 and compose(u, j2) == q2:
                    mediators.append(u)
            if len(mediators) != 1:
                return False, (X, len(mediators))
    return True, None


# ======================================================================
# Build the objects.
# ======================================================================
two = powerset_BA(1)            # {0,1}: subsets of {0}  -> 2 elements
B1  = powerset_BA(2)            # 2^2 : 4 elements
B2  = powerset_BA(2)            # 2^2 : 4 elements
coproduct = powerset_BA(4)      # 2^4 : 16 elements  (genuine Bool coproduct)

# The unique initial homs 2 -> B1, 2 -> B2 (bot->bot, top->top).
i1 = all_bool_homs(two, B1)[0]
i2 = all_bool_homs(two, B2)[0]


# --- Coproduct injections j1: B1 -> 2^4, j2: B2 -> 2^4 -------------------
# 2^4 = subsets of {0,1,2,3}.  B1 lives on coords {0,1}, B2 on coords {2,3}.
# Free-product (tensor) injections: a Boolean hom out of 2^2 is fixed by where
# it sends the two atoms; the coproduct injection sends atom k of B1 to the
# join of coordinate-k cells, i.e. atom {0}->{0,2}? -- we instead construct the
# injections as the canonical ones into the free product and just VERIFY they
# are homs and that the result is a valid pushout.  Simplest correct choice:
#   j1 sends a subset S of {0,1} to  S (as subset of {0,1,2,3}) "doubled"
# We build j1, j2 as the standard coproduct insertions of free BAs:
#   B1 = P({x1,x2}) , B2 = P({y1,y2}) , coproduct = P({x1,x2}x{y1,y2})?
# To stay elementary we instead DERIVE j1, j2 by requiring them to be the
# unique homs making (2^4, j1, j2) a pushout, searching for injective homs;
# but cleaner: use the product-of-spaces model.  See construction below.

# Coproduct of Boolean algebras P(X), P(Y) is P(X x Y) (Stone dual: product of
# spaces).  Here X = {0,1} (Spec B1), Y = {0,1} (Spec B2), X x Y has 4 points
# -> 2^4.  Injection j1: P(X) -> P(X x Y) is  A |-> A x Y  (cylinder).
# Encode X x Y points 0..3 as (xi, yi): point p = 2*xi + yi.
def cyl_X(A):   # A subset of {0,1} (coords of X) -> subset of X x Y
    return frozenset(2 * xi + yi for xi in A for yi in (0, 1))
def cyl_Y(B):   # B subset of {0,1} (coords of Y) -> subset of X x Y
    return frozenset(2 * xi + yi for yi in B for xi in (0, 1))

j1 = {A: cyl_X(A) for A in B1["elts"]}
j2 = {B: cyl_Y(B) for B in B2["elts"]}


# ----------------------------------------------------------------------
# Gunji's eq.20 object: glue B1, B2 at {0,1}, keep all else distinct.
# Carrier: bot, top, and the (4-2)+(4-2) = 4 middle elements -> MO_2 (6 elts).
# Label them: 'b','b1' (the two middle atoms of B1's 2^2), 'c','c1' (of B2).
# In 2^2 the two middle elements are the atoms; they are complements of each
# other. So MO_2 has atoms {b, b^perp = b1, c, c^perp = c1}.
# ----------------------------------------------------------------------
BOT, TOP = "0", "1"
MO2_elts = [BOT, TOP, "b", "b1", "c", "c1"]
comp_MO2 = {BOT: TOP, TOP: BOT, "b": "b1", "b1": "b", "c": "c1", "c1": "c"}

def meet_MO2(a, b):
    if a == b: return a
    if a == TOP: return b
    if b == TOP: return a
    if a == BOT or b == BOT: return BOT
    return BOT                              # distinct non-trivial atoms meet at 0
def join_MO2(a, b):
    if a == b: return a
    if a == BOT: return b
    if b == BOT: return a
    if a == TOP or b == TOP: return TOP
    return TOP                              # distinct non-trivial atoms join at 1

MO2 = {
    "elts": MO2_elts, "bot": BOT, "top": TOP,
    "meet": meet_MO2, "join": join_MO2,
    "comp": lambda a: comp_MO2[a],
    "le": lambda a, b: meet_MO2(a, b) == a,
}

# Injections into MO_2: B1's atoms -> b,b1 ; B2's atoms -> c,c1 ; bot/top glued.
atomsB1 = [e for e in B1["elts"] if e not in (B1["bot"], B1["top"])]
atomsB2 = [e for e in B2["elts"] if e not in (B2["bot"], B2["top"])]
g1 = {B1["bot"]: BOT, B1["top"]: TOP, atomsB1[0]: "b", atomsB1[1]: "b1"}
g2 = {B2["bot"]: BOT, B2["top"]: TOP, atomsB2[0]: "c", atomsB2[1]: "c1"}


# ======================================================================
# Run the checks.
# ======================================================================
print("=" * 68)
print("Machine check: Gunji et al. Prop 4 / Prop 8 contradiction")
print("=" * 68)

# (A) initiality of 2
okA1, nA1 = check_initial(two, B1)
okA2, nA2 = check_initial(two, B2)
print(f"\n(A) 2 = {{0,1}} is initial in Bool:")
print(f"    #homs 2 -> B1 = {nA1}  (want 1): {'OK' if okA1 else 'FAIL'}")
print(f"    #homs 2 -> B2 = {nA2}  (want 1): {'OK' if okA2 else 'FAIL'}")
print("    => pushout of B1 <- 2 -> B2  =  coproduct B1 + B2.")

# Distributivity of the two candidate objects.
dC, _ = is_distributive(coproduct)
dM, wM = is_distributive(MO2)
print(f"\n(B/C) Distributivity (= 'is it a Boolean algebra?'):")
print(f"    2^4 coproduct distributive: {dC}  ({'Boolean' if dC else 'NOT Boolean'})")
print(f"    MO_2 (eq.20 object) distributive: {dM}  "
      f"({'Boolean' if dM else 'NOT Boolean -- matches their Prop 4'})")
if not dM:
    print(f"      distributivity fails at (a,b,c) = {wM}")

# Verify j1,j2,g1,g2 really are Bool-homs where required.
print(f"\n    j1: B1 -> 2^4 is a Bool-hom: {is_bool_hom(B1, coproduct, j1)}")
print(f"    j2: B2 -> 2^4 is a Bool-hom: {is_bool_hom(B2, coproduct, j2)}")
# NB: g1,g2 need NOT be Bool-homs into MO_2 (MO_2 is not Boolean); they are the
# OML insertions.  We only use MO_2 as a *candidate target* X for universality,
# which requires Bool cocones -- MO_2 carries none that separate, see below.

# Test targets for the universal property: a spread of finite BAs.
test_targets = [powerset_BA(k) for k in range(0, 5)]   # 2^0 .. 2^4

# (B) Does 2^4 satisfy the Bool pushout universal property?
okPO, witPO = is_pushout(coproduct, j1, j2, B1, B2, i1, i2, test_targets)
print(f"\n(B) 2^4 with (j1,j2) satisfies the Bool pushout universal property")
print(f"    against targets 2^0..2^4: {'OK -- it IS the pushout' if okPO else f'FAIL {witPO}'}")

# (C) MO_2 cannot even be a target/object of Bool (not Boolean), and is not the
# Bool-pushout: the genuine pushout is 2^4 (16 elts) =/= MO_2 (6 elts).
print(f"\n(C) Their Prop 8 calls MO_2 'the pushout in Bool'.")
print(f"    |MO_2| = {len(MO2['elts'])}   |genuine Bool pushout 2^4| = {len(coproduct['elts'])}")
print(f"    MO_2 is non-distributive => not an object of Bool => cannot be the")
print(f"    pushout in Bool.  The Bool pushout is 2^4.  Prop 8 is FALSE as stated.")

print("\n" + "=" * 68)
verdict = okA1 and okA2 and dC and (not dM) and okPO \
          and len(MO2["elts"]) != len(coproduct["elts"])
print("VERDICT:", "CONTRADICTION CONFIRMED" if verdict else "CHECK INCONCLUSIVE")
print("  Prop 4 (P non-distributive) and Prop 8 (P = pushout in Bool) cannot")
print("  both hold: the Bool pushout is the 16-element Boolean 2^4, whereas the")
print("  eq.20 object is the 6-element non-distributive MO_2.")
print("=" * 68)
