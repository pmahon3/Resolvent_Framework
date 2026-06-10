# Does L2 (= consistency model, bare product ℕ→MO2) admit a 2-valued HOMOMORPHISM?
# Advisor's argument: the DIAGONAL/constant copy {⊥, c_a, c_a', c_b, c_b', ⊤}
# (c_x(n)=x ∀n) has top = GLOBAL ⊤, so the gap pair THERE forces the contradiction.
# A homomorphism h: L2 -> {0,1} restricted to the diagonal is a homomorphism
# MO2 -> {0,1} (the diagonal is a sub-OML isomorphic to MO2, with the SAME top/bot).
# Since MO2 has no homomorphism, h can't exist. Verify the diagonal really is
# an MO2-sub-OML with global bounds, and meet/ortho computed coordinatewise agree.
BOT,A,Ap,B,Bp,TOP='bot','a','ap','b','bp','top'
def m_meet(x,y):
    if x==BOT or y==BOT: return BOT
    if x==TOP: return y
    if y==TOP: return x
    return x if x==y else BOT
def m_join(x,y):
    if x==TOP or y==TOP: return TOP
    if x==BOT: return y
    if y==BOT: return x
    return x if x==y else TOP
m_compl={BOT:TOP,A:Ap,Ap:A,B:Bp,Bp:B,TOP:BOT}

N=4  # finite check; constant funcs over N blocks
def const(x): return tuple(x for _ in range(N))
diag = {x: const(x) for x in [BOT,A,Ap,B,Bp,TOP]}

# coordinatewise ops on tuples
def t_meet(f,g): return tuple(m_meet(a,b) for a,b in zip(f,g))
def t_join(f,g): return tuple(m_join(a,b) for a,b in zip(f,g))
def t_compl(f): return tuple(m_compl[a] for a in f)
TOPt, BOTt = const(TOP), const(BOT)

# (a) diagonal closed under coordinatewise ops, top/bot are GLOBAL:
vals=list(diag.values())
closed=all(t_meet(f,g) in vals and t_join(f,g) in vals and t_compl(f) in vals
           for f in vals for g in vals)
print(f"diagonal closed under coordinatewise meet/join/compl: {closed}")
print(f"diagonal top = global ⊤? {diag[TOP]==TOPt}   bot = global ⊥? {diag[BOT]==BOTt}")

# (b) the gap survives ON the diagonal: c_a ∧ c_b = c_(a∧b) = c_⊥ = global ⊥,
#     but c_a ⊀ c_b^⊥ : check c_a ≤ c_b' fails coordinatewise.
ca,cb,cbp = diag[A],diag[B],diag[Bp]
def t_leq(f,g): return all(m_meet(a,b)==a for a,b in zip(f,g))  # f≤g iff f∧g=f
print(f"c_a ∧ c_b = global ⊥? {t_meet(ca,cb)==BOTt}")
print(f"c_a ≤ c_b^⊥ (= c_b')? {t_leq(ca,cbp)}  (must be False: gap on diagonal)")

# (c) THEREFORE any hom h:L2->{0,1} restricted to diagonal is an MO2-hom => none.
#  brute: enumerate all {0,1} assignments to the 4 diagonal atoms respecting
#  h(⊥)=0,h(⊤)=1, h(x')=1-h(x), and require h(x∧y)=h(x)∧h(y) & h(x∨y)=h(x)∨h(y).
from itertools import product as prod
atoms=[A,Ap,B,Bp]
def hom_exists():
    for va,vb in prod([0,1],repeat=2):
        h={BOT:0,TOP:1,A:va,Ap:1-va,B:vb,Bp:1-vb}
        ok=True
        for x in [BOT,A,Ap,B,Bp,TOP]:
            for y in [BOT,A,Ap,B,Bp,TOP]:
                if h[m_meet(x,y)]!=min(h[x],h[y]) or h[m_join(x,y)]!=max(h[x],h[y]):
                    ok=False
        if ok: return (va,vb)
    return None
print(f"\n2-valued homomorphism on the diagonal MO2-copy exists? {hom_exists() is not None}")
print("=> diagonal forces NO homomorphism on L2 (global bounds + gap). Clean, decide-able.")
