"""
PRESSURE TEST: do separating sigma-additive states survive the finite->limit
passage on L2, and where do they put mass on the infinite witness p = \/_n b|C_n ?

L2 = constancy-sublogic of prod_{n} MO2 (singleton blocks C_n = {n}).
A STATE s: L2 -> [0,1], s(1)=1, additive on ORTHOGONAL pairs.

MO2 atoms: a, a', b, b'  with a^perp=a', b^perp=b'; a&b=0 but a not<= b'.
2-valued states on MO2 (Gudder): assign 1 to exactly one atom per complementary
pair? NO -- a state must respect a+a'=1 (orthogonal) and b+b'=1. A {0,1}-state
picks one of {a,a'} to be 1 and one of {b,b'} to be 1, BUT consistency:
if s(a)=1 then s(a')=0; independently s(b)=1 or s(b')=1. So 4 two-valued states.
Check: is s(a)=s(b)=1 consistent? a&b=0 so we'd want... meet=0 doesn't force
s(a&b)=0 to relate to s(a),s(b) since a,b NOT orthogonal (no additivity demanded).
So yes, all 4 sign-choices give valid 2-valued states. MO2 is concrete (separating).
"""
from itertools import product

# MO2 elements
BOT,A,Ap,B,Bp,TOP = 'bot','a','ap','b','bp','top'
ATOMS=[A,Ap,B,Bp]
ortho={BOT:TOP,TOP:BOT,A:Ap,Ap:A,B:Bp,Bp:B}

# The 4 two-valued states on MO2: choose value of a (1=>a, 0=>a'), value of b.
def mo2_states():
    states=[]
    for va,vb in product([0,1],repeat=2):
        s={BOT:0,TOP:1}
        s[A]=va; s[Ap]=1-va
        s[B]=vb; s[Bp]=1-vb
        states.append(s)
    return states

MO2S=mo2_states()
print(f"MO2 has {len(MO2S)} two-valued states (separating => concrete). OK")

# Finite truncation L2^(N): functions Fin N -> MO2 with coordinatewise ops.
# A PRODUCT state on L2^(N): pick a MO2-state per coordinate, s(f)=? 
# But a state on the PRODUCT LATTICE is NOT just coordinatewise eval -- a state
# must be additive on orthogonal pairs of the WHOLE product. The natural family:
# evaluation-at-coordinate-n composed with an MO2-state. s_n,sigma(f) = sigma(f(n)).
# These are states (additivity on ortho pairs reduces to coordinate n). 
# Do they SEPARATE L2^(N)? Two functions differ at some coord n in some atom;
# pick sigma distinguishing those MO2 values -> s separates. YES separating.

print("\nProduct/evaluation states s_{n,sigma}(f)=sigma(f(n)) separate L2^(N).")

# THE KEY: the infinite witness p = b on every block; family a_n = a at n, bot else.
# sigma-additivity test on the orthogonal family {a_n}: are the a_n pairwise ortho? 
# yes (verified in Lean). sigma-additive state demands  s(\/_n a_n) = sum_n s(a_n).
# Let q = \/_n a_n  (exists by sigma-orthocompleteness; = 'a on every block').
# For evaluation state s_{m,sigma}: s(a_n) = sigma(a_n(m)) = sigma(a) if n=m else sigma(bot)=0.
#   so sum_n s(a_n) = sigma(a).   And s(q)=sigma(q(m))=sigma(a). MATCH. sigma-additive OK.
# Now the WITNESS p = b on every block. Is p orthogonal to the family? NO (that's star).
#   p is NOT in the orthogonal family, so sigma-additivity says nothing forcing about p directly.
# The real question (Q1): does p get a definite {0,1} value, i.e. concentrate on a point?

# A 2-valued state that is sigma-additive: take s_{m,sigma}. s(p)=sigma(p(m))=sigma(b)=vb in {0,1}.
# So EACH evaluation state DOES give p a definite value. p is NOT dispersion-free-forced-off.
# => point-concentration is AVAILABLE via evaluation states. Let's verify these are sigma-additive
# on ALL orthogonal families, not just {a_n}.

def eval_state(m, sigma):
    return lambda f: sigma[f[m]]   # f a dict n->MO2 value

# Test sigma-additivity of an evaluation state on a generic disjoint-support ortho family.
# Build family g_k = (some atom) at block k, bot elsewhere, k=0..K. join = that atom on each block.
def test_sigma_add(m,sigma,K=6):
    # family g_k: put atom 'b' at block k
    def gk(k):
        return {n:(B if n==k else BOT) for n in range(K)}
    join = {n:B for n in range(K)}  # \/_k g_k = b on every block 0..K-1
    s=eval_state(m,sigma)
    lhs=s(join)
    rhs=sum(s(gk(k)) for k in range(K))
    return lhs,rhs

for m in range(2):
    for sigma in MO2S:
        lhs,rhs=test_sigma_add(m,sigma)
        tag="OK" if lhs==rhs else "FAIL-sigma-add"
        print(f" eval state block={m} sigma(a,b)=({sigma[A]},{sigma[B]}): s(\\/g)={lhs} sum={rhs} {tag}")
