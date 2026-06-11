"""
Path B (2026-06-10): finite-truncation hinge check for the (beta) MO2-swap.

GOAL. Independently test Claim 3 of `beta_swap_worksheet.{md,tex}` at finite
stages, where the lattice order is UNAMBIGUOUS (no completion subtlety). Path A
(reading Navara p.428) concluded L's order is coordinatewise/sub-product, not a
completion; if that is right, the finite truncations already settle the hinge
and the N->infinity limit changes nothing. This script is the falsifier.

CONSTRUCTION (beta), finite truncation L2^(N):
  - Block U := MO2 = {0, a, a', b, b', 1}  (a'=a^perp, b'=b^perp).
      complementary pairs {a,a'}, {b,b'}; a & b = 0 but a NOT<= b'  (a !perp b).
  - N disjoint blocks C_1,...,C_N.  An element of L2^(N) assigns to each block
    C_i a value in MO2 (the "constant value on C_i"); the constancy condition is
    automatically satisfied because we collapse each block to one coordinate.
      (This is the faithful finite model: Navara's f is constant on each C, so
       its content per block is exactly one MO2 element.)
  - So L2^(N)  ==  MO2^N  with COORDINATEWISE order/meet/join/orthocomplement,
    EXCEPT we must respect that join/meet of two MO2 elements may not exist
    inside MO2 (MO2 is a lattice: it does, with 0 and 1 as the non-trivial lubs)
    -- here MO2 IS a lattice so coordinatewise ops are well-defined.

  NOTE on faithfulness: representing L2^(N) as MO2^N (product) is EXACTLY the
  sub-product-of-W picture Path A read off Navara. If instead L were a
  completion, this model would be wrong -- which is why Path A had to be settled
  first. This script tests the consequence of Path A's reading.

WITNESS DATA (the (star) test):
  a_i := "a on block i, 0 elsewhere"   (i = 1..N)        -- infinite orth family
  p   := "b on block 1, b on block 2, ..., b on block N" -- the single element
                                                            spread over all blocks
  (star) asks:  p & a_i = 0  for all i   AND   p NOT<= a_i^perp  for all i.

If (star) holds at every finite N -> segregation, if real, is purely infinitary
(it would have to switch on only at N=infinity). If (star) FAILS at some finite
N -> Claim 3 is wrong and segregation is already finite.
"""

# ---- MO2 as an explicit lattice ----------------------------------------
# elements
O, A, Ap, B, Bp, I = "0", "a", "a'", "b", "b'", "1"
ELS = [O, A, Ap, B, Bp, I]

# order relation x <= y on MO2.
# Atoms a,a',b,b' are pairwise incomparable; 0 below all; 1 above all.
def leq_mo2(x, y):
    if x == O or y == I:
        return True
    if x == y:
        return True
    # atoms below nothing but 1, above nothing but 0
    return False

# orthocomplement on MO2
PERP = {O: I, I: O, A: Ap, Ap: A, B: Bp, Bp: B}

# meet (greatest lower bound) on MO2
def meet_mo2(x, y):
    if leq_mo2(x, y):
        return x
    if leq_mo2(y, x):
        return y
    # incomparable atoms -> only common lower bound is 0
    return O

# join (least upper bound) on MO2
def join_mo2(x, y):
    if leq_mo2(x, y):
        return y
    if leq_mo2(y, x):
        return x
    # incomparable atoms -> only common upper bound is 1
    return I

# ---- sanity: MO2 has the defining gap -----------------------------------
assert meet_mo2(A, B) == O,        "MO2: a & b should be 0"
assert not leq_mo2(A, PERP[B]),    "MO2: a <= b' should be FALSE (a !perp b)"
assert not leq_mo2(B, PERP[A]),    "MO2: b <= a' should be FALSE"
assert leq_mo2(A, PERP[A]) is False and meet_mo2(A, PERP[A]) == O
# orthogonality x perp y  iff  x <= y^perp
def perp_mo2(x, y):
    return leq_mo2(x, PERP[y])
assert perp_mo2(A, Ap) and not perp_mo2(A, B), "a perp a', a NOT perp b"

# ---- L2^(N) = MO2^N, coordinatewise -------------------------------------
def leq(f, g):           # f,g are tuples of length N
    return all(leq_mo2(fi, gi) for fi, gi in zip(f, g))

def meet(f, g):
    return tuple(meet_mo2(fi, gi) for fi, gi in zip(f, g))

def perp(f):             # coordinatewise orthocomplement
    return tuple(PERP[fi] for fi in f)

def is_perp(f, g):       # f perp g  iff  f <= g^perp
    return leq(f, perp(g))

def zero(N): return tuple(O for _ in range(N))

# ---- the hinge test at truncation N -------------------------------------
def hinge_at_N(N, verbose=False):
    # a_i := a on block i, 0 elsewhere
    def a_block(i):
        return tuple(A if k == i else O for k in range(N))
    # p := b on every block
    p = tuple(B for _ in range(N))

    results = []
    for i in range(N):
        ai = a_block(i)
        m = meet(p, ai)                 # want 0
        ai_perp = perp(ai)              # a_i^perp = (a' on block i, 1 elsewhere)
        p_leq_aiperp = leq(p, ai_perp)  # want FALSE (p NOT perp a_i)
        fact1 = (m == zero(N))          # p & a_i = 0  ?
        fact2 = (not p_leq_aiperp)      # p NOT<= a_i^perp ?
        star_i = fact1 and fact2
        results.append((i, fact1, fact2, star_i, m, ai_perp))
        if verbose:
            print(f"  block i={i}: a_i^perp={ai_perp}")
            print(f"             p & a_i = {m}   (=0? {fact1})")
            print(f"             p <= a_i^perp? {p_leq_aiperp}   "
                  f"(so p NOT perp a_i? {fact2})")
            print(f"             (star) at i: {star_i}")
    star_holds = all(r[3] for r in results)
    return star_holds, results

# ---- run N = 2,3,4 (and a few more for the pattern) ---------------------
if __name__ == "__main__":
    print("=" * 66)
    print("Path B: finite-truncation hinge for the (beta) MO2-swap")
    print("L2^(N) = MO2^N, coordinatewise (per Path A reading of Navara p.428)")
    print("=" * 66)
    print(f"\nWITNESS: a_i = a on block i; p = b on ALL blocks.")
    print(f"(star) needs, for every i:  p&a_i=0  AND  p NOT<= a_i^perp.\n")

    overall = {}
    for N in [2, 3, 4, 5, 8]:
        star, res = hinge_at_N(N, verbose=(N == 2))
        overall[N] = star
        print(f"\nN = {N}:  (star) holds at every block i?  --> {star}")
        if N == 2:
            print("   (verbose trace above)")

    print("\n" + "=" * 66)
    print("VERDICT")
    print("=" * 66)
    if all(overall.values()):
        print("(star) HOLDS at every finite truncation N tested.")
        print("=> Under Path A's coordinatewise reading, the witness p exhibits")
        print("   the element-vs-family gap at every finite stage. If Navara's")
        print("   order is coordinatewise (Path A), nothing changes at N=inf,")
        print("   so the HINGE RESOLVES YES and Claim 3 stands.")
        print("   The notes' 'segregation/leans-NO' would then require the order")
        print("   to be a COMPLETION order (NOT coordinatewise) -- which Path A")
        print("   read OUT of the paper. So: re-examine Path A's reading, OR")
        print("   accept hinge=YES.  THE TENSION IS NOW SHARP AND BINARY.")
    else:
        bad = [N for N, s in overall.items() if not s]
        print(f"(star) FAILS at finite N in {bad}.")
        print("=> Claim 3 is WRONG already at finite stage; segregation is")
        print("   finite, not infinitary. Notes' 'leans NO' vindicated.")
    print()
    print("CAVEAT: this tests the CONSEQUENCE of Path A (coordinatewise order).")
    print("It does NOT independently verify that Navara's L has that order.")
    print("If L is a completion, MO2^N is the wrong model and this is moot.")
