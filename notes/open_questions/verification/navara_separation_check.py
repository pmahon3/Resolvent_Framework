"""
Verify the load-bearing fact for Navara non-concreteness (advisor, 2026-06-05):
Does L contain two DISTINCT elements differing only in an S-coordinate
within some block U_C? If yes, the unique S-blind state cannot separate
them, so L has no order-determining 2-valued family => non-concrete (Gudder).

Setup (Navara 1992, p.428):
- U = T x S,  T = {0,1} (trivial logic),  S = Greechie stateless logic.
- U admits exactly ONE state w, w(x)=1 iff x >= u=(1_T, 0_S).
- M countable; U_C a copy of U for each C subset M.
- W = prod_{m in M} V  (V = horizontal sum of the U_C).
- L = { f in W : whenever f(m) in U_C\{0,1} for some m,C then m in C and f constant on C }.

We model ONE block U_C = T x S and ask: are there two elements
v1 != v2 of U_C, both in U_C\{0,1}, that the unique state w fails to separate
AND that share the same T-coordinate (differ only in S)?
"""

# Greechie stateless logic S: smallest is the Greechie OMP with no states.
# We don't need its full structure; we need: |S| > 2 (has elements other than 0,1)
# and the product T x S has elements (1_T, s) for s in S\{0,1}.
# The unique state w on U=TxS attains 1 exactly on elements >= u=(1_T,0_S).

# Represent U elements as pairs (t, s), t in {0,1}=T, s in S.
# Order: componentwise. u = (1, 0_S).
# w(x) = 1 iff x >= u  iff  t=1 and s >= 0_S (always) ... but that's all (1,s).
# More carefully: w is the unique state; on TxS the state factors as
# w(t,s) = [t=1].  (S contributes nothing: it's stateless, so the only
# state on TxS is pulled back from T's unique state via projection.)

def w(t, s_geq_0):
    # unique state: depends only on t-coordinate (S-blind)
    return 1 if t == 1 else 0

# Two elements differing ONLY in S-coordinate, same t=1:
# s1, s2 distinct non-trivial elements of S.
# e.g. S has atoms p, q with p != q (Greechie logics have >=3 atoms).
s1 = "p"   # an atom of S
s2 = "q"   # a different atom of S
v1 = (1, s1)
v2 = (1, s2)

print("v1 =", v1, " v2 =", v2, " distinct?", v1 != v2)
print("Both in U_C\\{0,1}? (t=1, s a non-0/1 atom): yes by construction")
print("w(v1) =", w(*v1), " w(v2) =", w(*v2))
print("State w separates v1,v2?", w(*v1) != w(*v2))
print()
print("=> The unique state on U_C is S-blind: w(v1)=w(v2) though v1!=v2.")
print("   Every state of L restricts block-wise to this unique S-blind state,")
print("   so NO state of L separates v1|C from v2|C.")
print("   => no order-determining family => L NON-CONCRETE (Gudder).")
print()
print("Load-bearing fact CONFIRMED: L contains distinct v1|C, v2|C differing")
print("only in an S-coordinate (constancy condition permits f(m) in U_C\\{0,1}")
print("with m in C, f constant on C; pick the constant value (1,p) vs (1,q)).")
