# Stage 2: (A) mechanically verify the merge certificate for EVERY V01 set on 3x3x3x3: find a coordinate and two values
# a,b whose slice difference depends on one other coordinate j; check {x_i=a, x_j in U+} is contained in F,
# {x_i=a, x_j in U-} is disjoint from F, and that after removing/adding them slice a equals slice b.
# (B) count irreducible sets on 3x3x3x4 (slices along the 4-valued coordinate).
import itertools, time, numpy as np
exec(open('k4_3333_stage1.py').read().split("# --- reducibility test")[0].replace("print('admissible","pass #print('admissible"))
t0=time.time()
def certify(S):                                   # S: (m,n3,3,3,3) int8, axes 1..4 are the four coordinates
    m=len(S); done=np.zeros(m,bool)
    for ax in range(1,5):
        for a,b in itertools.permutations(range(S.shape[ax]),2):
            Fa=np.take(S,a,axis=ax); Fb=np.take(S,b,axis=ax); d=Fa-Fb                # (m,.,.,.)
            for keep in range(1,4):
                ref=d
                for k in (1,2,3):
                    if k!=keep: ref=np.take(ref,[0],axis=k)
                simple=(d==ref).reshape(m,-1).all(1)
                plus=(ref==1); minus=(ref==-1)                                       # U+ and U- as functions of x_keep
                contained=((Fa==1)|~plus).reshape(m,-1).all(1)                       # {x_keep in U+} inside slice a
                disjoint=((Fa==0)|~minus).reshape(m,-1).all(1)                       # {x_keep in U-} misses slice a
                after=np.where(plus,0,np.where(minus,1,Fa)); same=(after==Fb).reshape(m,-1).all(1)
                assert (simple<= (contained&disjoint&same)).all(), 'merge certificate failed'
                done|=simple
    return done
buf=[]; total=0; cert=0
def flush():
    global buf,total,cert
    if buf:
        S=np.array(buf,dtype=np.int8).reshape(-1,3,3,3,3); c=certify(S); total+=len(S); cert+=int(c.sum()); buf=[]
for i,l in enumerate(lists):
    for F1 in l:
        for F2 in l: buf.append(np.concatenate([T[i],F1,F2]))
    if len(buf)>100000: flush()
flush(); print('(A) 3x3x3x3: sets',total,'| merge certificate verified for',cert,'| time %.0fs'%(time.time()-t0),flush=True)
M4=int((cnt.astype(np.int64)**3).sum()); print('(B) 3x3x3x4: |V01| =',M4,flush=True)
buf=[]; total=0; cert=0; irr=[]
def flush4():
    global buf,total,cert
    if buf:
        S=np.array(buf,dtype=np.int8).reshape(-1,4,3,3,3); c=certify(S); total+=len(S); cert+=int(c.sum()); irr.extend(S[~c]); buf=[]
for i,l in enumerate(lists):
    for F1 in l:
        for F2 in l:
            for F3 in l: buf.append(np.concatenate([T[i],F1,F2,F3]))
    if len(buf)>60000: flush4()
flush4(); print('(B) 3x3x3x4: sets',total,'| reducible (certificate verified)',cert,'| irreducible',len(irr),'| time %.0fs'%(time.time()-t0))
