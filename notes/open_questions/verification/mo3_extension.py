"""
Independent verification: does ANY state on MO_3 extend to a finitely
additive charge on the FULL Boolean algebra of clopens of the
McDonald-Bimbo dual S_0(MO_3)?

MO_3 = horizontal sum of three 2x2 Boolean blocks ("Chinese lantern"):
  - bottom 0, top 1
  - three orthogonal pairs of atoms: (p,p'), (q,q'), (r,r')
  - within each pair: p' = p^perp, p ∨ p' = 1, p ∧ p' = 0
  - ACROSS pairs: any two atoms from different blocks meet to 0,
    join to 1, but are NOT orthogonal (p^perp = p', NOT q).

Elements of MO_3: 0, 1, and the six atoms p,p',q,q',r,r'.  (8 elements.)
Order: 0 < each atom < 1.  No atom below another.

A STATE s: assigns s(0)=0, s(1)=1, and s(atom)+s(complement)=1 for each
of the three complementary pairs (orthoadditivity on p ⊥ p').
So states are parametrized by (s(p), s(q), s(r)) in [0,1]^3, with
s(p')=1-s(p), etc.

THE KEY STRUCTURAL FACT (to verify from McDonald-Bimbo):
h preserves MEETS: h(a) ∩ h(b) = h(a ∧ b).
So a ∧ b = 0  ==>  h(a), h(b) are disjoint as sets (modulo the null
improper-filter point ω).

In MO_3, which pairs of atoms have meet 0?
  - p ∧ p' = 0  (complementary, same block)
  - p ∧ q  = 0  (different blocks)   -- and ALL cross-block pairs
So EVERY pair of distinct atoms has meet 0.  All six atoms are
pairwise meet-0  ==>  h(atom) are pairwise disjoint sets.

A finitely additive charge μ on the Boolean algebra, with μ ≥ 0 and
μ(whole)=1, must satisfy: for pairwise-disjoint sets,
  Σ μ(h(atom_i)) ≤ μ(whole) = 1.
And μ(h(atom)) = s(atom) by definition of the extension.
So extension requires:  s(p)+s(p')+s(q)+s(q')+s(r)+s(r') ≤ 1.
But orthoadditivity forces s(p)+s(p') = 1, etc., so the LHS = 3.
3 ≤ 1 is false.  => NO state extends.

Below we verify this as an explicit LP feasibility over the atoms of
the generated Boolean algebra, rather than trusting the hand argument.
"""

import itertools
import numpy as np
from scipy.optimize import linprog

# --- MO_3 elements ---
atoms = ['p', "p'", 'q', "q'", 'r', "r'"]
compl_pairs = [('p', "p'"), ('q', "q'"), ('r', "r'")]

# meet table on atoms: meet(a,b) = a if a==b else 0  (no atom below another)
def meet_atoms(a, b):
    return a if a == b else '0'

# Verify: all distinct atom pairs meet to 0
all_cross_zero = all(
    meet_atoms(a, b) == '0'
    for a, b in itertools.combinations(atoms, 2)
)
print("All distinct atom pairs meet to 0:", all_cross_zero)

# --- The h-images as subsets of the dual space ---
# We do NOT need the full filter space.  The ONLY structural input that
# constrains the charge is the meet-preservation: h(a)∩h(b)=h(a∧b).
# meet-0 atoms => pairwise-disjoint h-images.  We model the Boolean
# algebra abstractly via an LP on the "regions" (atoms of the generated
# field).  Because the six h(atom) are pairwise disjoint, the generated
# field's relevant atoms include the six disjoint pieces R1..R6 = h(atom_i)
# plus a remainder R0 = complement of their union.  A charge assigns
# nonneg mass x0..x6 summing to 1, with μ(h(atom_i)) = x_i.

# Extension constraint: μ(h(atom_i)) = s(atom_i).
# Orthoadditivity (state condition): s(p)+s(p')=1, s(q)+s(q')=1, s(r)+s(r')=1.

def state_extends(s_vals):
    """s_vals: dict atom->value satisfying the state constraints.
    Returns True iff a nonneg charge on the Boolean algebra exists with
    the six disjoint regions carrying exactly s(atom_i) and total 1."""
    # variables: x0 (remainder), x1..x6 (the six disjoint h-images)
    # equalities: x_i = s(atom_i) for i=1..6 ; sum x = 1 ; x>=0
    c = [0]*7
    A_eq = []
    b_eq = []
    # x_i = s(atom_i)
    for i, a in enumerate(atoms, start=1):
        row = [0]*7
        row[i] = 1
        A_eq.append(row); b_eq.append(s_vals[a])
    # total mass = 1
    A_eq.append([1]*7); b_eq.append(1.0)
    res = linprog(c, A_eq=np.array(A_eq), b_eq=np.array(b_eq),
                  bounds=[(0, None)]*7, method='highs')
    return res.success

# Test a grid of states (s(p),s(q),s(r)) in [0,1]^3
import numpy as np
grid = np.linspace(0, 1, 6)
any_extends = False
checked = 0
for sp in grid:
    for sq in grid:
        for sr in grid:
            s = {'p': sp, "p'": 1-sp, 'q': sq, "q'": 1-sq, 'r': sr, "r'": 1-sr}
            checked += 1
            if state_extends(s):
                any_extends = True
                print("  EXTENDS:", (sp, sq, sr))
print(f"Checked {checked} states. Any extends: {any_extends}")

# Also check the maximally-mixed state explicitly (s=1/2 everywhere)
s_mix = {a: 0.5 for a in atoms}
print("Maximally mixed state extends:", state_extends(s_mix))

# Print the decisive inequality
print("\nSum of s over all 6 atoms (always = 3 by orthoadditivity):",
      "s(p)+s(p')+s(q)+s(q')+s(r)+s(r') = (s(p)+s(p')) + ... = 1+1+1 = 3")
print("Charge requires this sum <= 1 (pairwise-disjoint). 3 <= 1 is FALSE.")
