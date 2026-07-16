#!/usr/bin/env python3
"""Bounded actual-event universal-shadow discriminator.

Use the same six sampled mixed leaves per orientation as the coordinate-child
control, but choose a canonical opposite event and represent the true
two-copy relation on the shared-state fibre product.  Simultaneous truth
patterns of the six retained and six opposite events are enumerated exactly
from reduced MDD roots.  Boolean terms are evaluated on the resulting finite
relation quotient.  Their true universal shadow is then composed back into
an exact one-copy MDD and compared with the coordinate-target Boolean
calculus before both old-lower kernels are audited.
"""
import argparse,collections,hashlib,json,os,struct,sys,time
HERE=os.path.dirname(os.path.abspath(__file__));sys.path.insert(0,HERE)
import full_cycle_adjacent_rectangle_intersection as inter
SCHEMA='adjacent-full-cycle-actual-event-universal-shadow-v1'
JOIN=os.path.join(HERE,'adjacent_full_cycle_join_rich_per_a.json')
FACTOR=os.path.join(HERE,'adjacent_full_cycle_union_factor_checkpoint.json')
SAMPLE_A=3;MASKS_PER_A=2;CAP=96;ALL12=(1<<4096)-1

def payload():
 started=time.perf_counter();source=json.load(open(JOIN));factor=json.load(open(FACTOR));selected={}
 assert factor['global_carrier_points']==211897540016 and factor['nonempty_global_macrofibres']==23998
 for rec in source['orientation_records']:
  xs=[x['event_index'] for x in rec['per_a']]
  selected[rec['orientation']]=tuple(xs[(i*(len(xs)-1))//(SAMPLE_A-1)] for i in range(SAMPLE_A))
 base,b=inter.capture_grammar();events=b['all_events'];macros=b['macros'];engines=b['engines'];states=b['states']
 roots={ev:r for r,ev in b['root_to_event'].items()};principal=b['principal'];n=len(events);N=len(states)
 assert (n,N)==(18676,224);upmap={u:i for i,u in enumerate(principal)}
 allold=(1<<n)-1;zero=upmap[allold];nonatomic=0
 for d,u in enumerate(principal):
  if d!=zero:nonatomic|=u&~(1<<d)
 z=allold&~nonatomic&~(1<<zero);atoms=[]
 while z:q=z&-z;atoms.append(q.bit_length()-1);z-=q
 assert len(atoms)==91
 occ=[[[] for _ in range(N)] for _ in range(4)]
 for m,(_,ds) in enumerate(macros):
  for pos in range(4):
   for i,s in enumerate(ds[pos]):occ[pos][s].append((m,i))
 stat={}
 def status(m,r,pos,i):
  k=(m,r,pos,i)
  if k in stat:return stat[k]
  if r<=1:v=r
  else:
   x,ch=engines[m].nodes[r]
   if x==pos:v=status(m,ch[i],pos,i)
   else:a={status(m,t,pos,i) for t in ch};v=a.pop() if len(a)==1 else 2
  stat[k]=v;return v
 def classify(pos):
  out=[]
  for ev in events:
   E=U=0;rr=roots[ev]
   for s,os in enumerate(occ[pos]):
    a=[status(m,rr[m],pos,i) for m,i in os]
    if any(a):E|=1<<s
    if all(x==1 for x in a):U|=1<<s
   out.append((E,U))
  return out
 left=classify(3);right=classify(0)
 def minima(cs):
  g=collections.defaultdict(list)
  for i,(E,U) in enumerate(cs):g[U].append((E,i))
  out={}
  for U,xs in g.items():
   keep=[]
   for E,i in sorted(xs,key=lambda x:(x[0].bit_count(),x[0],x[1])):
    if not any(not K&~E for K,_ in keep):keep.append((E,i))
   out[U]=tuple(keep)
  return out
 def admissible(cs,op):
  fam=[];wit=[]
  for A,(EA,_) in enumerate(cs):
   ws={}
   for U,xs in op.items():
    cand=[(i,E) for E,i in xs if not EA&E]
    if cand:ws[U]=min(cand)
   fam.append(tuple(sorted(ws,key=lambda u:(u.bit_count(),u))));wit.append(ws)
  return fam,wit
 lu,lw=admissible(left,minima(right));ru,rw=admissible(right,minima(left))

 def mddop(kind,x,y):return tuple(engines[m].app(kind,a,c) for m,(a,c) in enumerate(zip(x,y)))
 def mddneg(x):return tuple(engines[m].neg(a) for m,a in enumerate(x))
 def subset(x,y):return all(not engines[m].app(0,a,engines[m].neg(c)) for m,(a,c) in enumerate(zip(x,y)))
 def rhash(x):return hashlib.sha256(b''.join(struct.pack('<I',a) for a in x)).hexdigest()
 def cyl(pos,mask):return tuple(engines[m].varset(pos,{s for s in ds[pos] if mask>>s&1}) for m,(_,ds) in enumerate(macros))
 kcache={};ktests=0
 def kernel(target):
  nonlocal ktests
  h=rhash(target)
  if h in kcache:return kcache[h]
  j=zero;eligible=[]
  for a in atoms:
   ktests+=1
   if subset(roots[events[a]],target):eligible.append(a);j=upmap[principal[j]&principal[a]]
  ed=hashlib.sha256(','.join(map(str,eligible)).encode()).hexdigest()
  good=subset(roots[events[j]],target);kcache[h]=(j,good,len(eligible),ed);return kcache[h]

 # Exact simultaneous value patterns after fixing the shared coordinate.
 pcache={}
 def patterns(m,rs,pos,i):
  key=(m,rs,pos,i)
  if key in pcache:return pcache[key]
  if all(r<=1 for r in rs):ans=frozenset((sum((r&1)<<k for k,r in enumerate(rs)),))
  else:
   vs=[engines[m].nodes[r][0] for r in rs if r>1];v=min(vs)
   if v==pos:
    nxt=tuple(engines[m].nodes[r][1][i] if r>1 and engines[m].nodes[r][0]==v else r for r in rs)
    ans=patterns(m,nxt,pos,i)
   else:
    ans=set()
    for q in range(len(engines[m].domains[v])):
     nxt=tuple(engines[m].nodes[r][1][q] if r>1 and engines[m].nodes[r][0]==v else r for r in rs)
     ans.update(patterns(m,nxt,pos,i))
    ans=frozenset(ans)
  pcache[key]=ans;return ans

 # Compose a state-dependent six-bit truth table back into an exact MDD.
 def compose_all(ev_indices,pos,tables):
  out=[]
  for m,(_,ds) in enumerate(macros):
   memo={}
   def go(rs,s):
    key=(rs,s)
    if key in memo:return memo[key]
    if all(r<=1 for r in rs) and s>=0:
     pat=sum((r&1)<<k for k,r in enumerate(rs));ans=(tables[s]>>pat)&1
    else:
     vs=[engines[m].nodes[r][0] for r in rs if r>1]
     if s<0:vs.append(pos)
     v=min(vs);ch=[]
     for q in range(len(engines[m].domains[v])):
      nxt=tuple(engines[m].nodes[r][1][q] if r>1 and engines[m].nodes[r][0]==v else r for r in rs)
      ns=ds[pos][q] if v==pos and s<0 else s
      ch.append(go(nxt,ns))
     ans=engines[m].node(v,ch)
    memo[key]=ans;return ans
   out.append(go(tuple(roots[events[e]][m] for e in ev_indices),-1))
  return tuple(out)

 def leaf_formula(i):
  ans=0
  for p in range(4096):
   if (p>>i&1) or (p>>(6+i)&1):ans|=1<<p
  return ans
 records=[];global_first=None
 for name,pos,classes,fams,wits,opclasses in (
   ('left_retained_position11',3,left,lu,lw,right),
   ('right_retained_position00',0,right,ru,rw,left)):
  retained=[];opposite=[];leafmeta=[]
  for A in selected[name]:
   for U in [u for u in fams[A] if u][:MASKS_PER_A]:
    B,EB=wits[A][U];retained.append(A);opposite.append(B);leafmeta.append((A,B,U))
  assert len(retained)==6
  # In the opposite copy the shared coordinate position is the other one.
  oppos=0 if pos==3 else 3
  AP=[set() for _ in range(N)];BP=[set() for _ in range(N)]
  for s in range(N):
   for m,i in occ[pos][s]:AP[s].update(patterns(m,tuple(roots[events[e]][m] for e in retained),pos,i))
   for m,i in occ[oppos][s]:BP[s].update(patterns(m,tuple(roots[events[e]][m] for e in opposite),oppos,i))
   assert AP[s] and BP[s]
  allowed=[]
  for s in range(N):
   q=0
   for a in AP[s]:
    for bb in BP[s]:q|=1<<(a|(bb<<6))
   allowed.append(q)
  def vector_hash(xs):return hashlib.sha256(repr(tuple(xs)).encode()).hexdigest()
  ap_hash=vector_hash(tuple(tuple(sorted(x)) for x in AP))
  bp_hash=vector_hash(tuple(tuple(sorted(x)) for x in BP))
  allowed_hash=vector_hash(allowed)
  def signature(F):return tuple(F&q for q in allowed)
  def sighash(sig):return hashlib.sha256(repr(sig).encode()).hexdigest()
  def shadows(F):
   lt=[];rt=[]
   for s in range(N):
    l=0;r=0
    for a in range(64):
     if all(F>>(a|(bb<<6))&1 for bb in BP[s]):l|=1<<a
    for bb in range(64):
     if all(F>>(a|(bb<<6))&1 for a in AP[s]):r|=1<<bb
    lt.append(l);rt.append(r)
   return lt,rt
  terms={}
  for i,(A,B,U) in enumerate(leafmeta):
   F=leaf_formula(i);coord=mddop(1,roots[events[A]],cyl(pos,U))
   terms[signature(F)]={'kind':'Leaf','F':F,'coord':coord,'parents':None}
  leaves=list(terms.values())
  for i,x in enumerate(leaves):
   for y in leaves[i:]:
    F=x['F']&y['F'];sig=signature(F)
    terms.setdefault(sig,{'kind':'And','F':F,'coord':mddop(0,x['coord'],y['coord']),
      'parents':(signature(x['F']),signature(y['F']))})
    if len(terms)>=CAP:break
   if len(terms)>=CAP:break
  base_terms=list(terms.values());candidates=dict(terms);neg_terms=[]
  for x in base_terms:
   F=ALL12^x['F'];sig=signature(F);coord=mddneg(x['coord'])
   neg_terms.append({'kind':'Neg','F':F,'coord':coord,'parents':(signature(x['F']),)})
   # Match the old control: only kernel-good coordinate complements enter OR.
   if kernel(coord)[1]:candidates.setdefault(sig,neg_terms[-1])
  vals=list(candidates.values());or_terms=[]
  for i,x in enumerate(vals):
   for y in vals[i+1:]:
    if any((x['F']&y['F']&q) for q in allowed):continue
    F=x['F']|y['F'];sig=signature(F)
    if sig in terms:continue
    or_terms.append({'kind':'OrthoOr','F':F,'coord':mddop(1,x['coord'],y['coord']),
      'parents':(signature(x['F']),signature(y['F']))})
  tested=list(terms.values())+neg_terms+or_terms
  mismatches=[];actual_bad=coord_bad=0;mismatch_kinds=collections.Counter()
  provenance=[];shadow_table_chain=hashlib.sha256()
  for t in tested:
   LT,RT=shadows(t['F']);tables=LT
   sig=signature(t['F']);sh= sighash(sig)
   ph=[sighash(x) for x in (t.get('parents') or ())]
   provenance.append((t['kind'],sh,tuple(ph)))
   shadow_table_chain.update(f"{t['kind']}|{sh}|{vector_hash(LT)}|{vector_hash(RT)}\n".encode())
   actual=compose_all(retained,pos,tables)
   ak,ag,aec,aed=kernel(actual);ck,cg,cec,ced=kernel(t['coord'])
   same=actual==t['coord'];actual_bad+=not ag;coord_bad+=not cg
   if not same or ag!=cg or ak!=ck:
    mismatch_kinds[t['kind']]+=1
    rec={'kind':t['kind'],'semantic_signature_sha256':sh,
     'parent_signature_sha256':ph,'actual_shadow_sha256':rhash(actual),
     'coordinate_target_sha256':rhash(t['coord']),'shadows_equal':same,
     'actual_kernel_event_index':ak,'actual_kernel_good':ag,
     'actual_eligible_atom_count':aec,'actual_eligible_atom_digest_sha256':aed,
     'coordinate_kernel_event_index':ck,'coordinate_kernel_good':cg}
    rec['coordinate_eligible_atom_count']=cec;rec['coordinate_eligible_atom_digest_sha256']=ced
    mismatches.append(rec)
    if global_first is None:global_first={'orientation':name,**rec}
  assert mismatch_kinds['Leaf']==0 and mismatch_kinds['And']==0
  mismatch_digest=hashlib.sha256('\n'.join(json.dumps(x,sort_keys=True,separators=(',',':')) for x in mismatches).encode()).hexdigest()
  prov_digest=hashlib.sha256('\n'.join(repr(x) for x in provenance).encode()).hexdigest()
  leaf_records=[]
  for A,B,U in leafmeta:
   leaf_records.append({'retained_event_index':A,'opposite_event_index':B,
    'retained_physical_root_sha256':rhash(roots[events[A]]),
    'opposite_physical_root_sha256':rhash(roots[events[B]]),
    'retained_E_hex':hex(classes[A][0]),'retained_U_hex':hex(classes[A][1]),
    'opposite_E_hex':hex(opclasses[B][0]),'opposite_U_hex':hex(opclasses[B][1]),
    'witness_U_hex':hex(U),'disjoint_existential_masks':not bool(classes[A][0]&opclasses[B][0])})
  records.append({'orientation':name,'retained_event_indices':retained,
   'opposite_event_indices':opposite,'leaf_metadata':[{'A':a,'B':bb,'U_hex':hex(u)} for a,bb,u in leafmeta],
   'exact_leaf_witness_records':leaf_records,
   'realized_retained_pattern_vector_sha256':ap_hash,
   'realized_opposite_pattern_vector_sha256':bp_hash,
   'allowed_pair_vector_sha256':allowed_hash,
   'realizable_left_pattern_count_by_state':dict(collections.Counter(map(len,AP))),
   'realizable_right_pattern_count_by_state':dict(collections.Counter(map(len,BP))),
   'leaf_and_term_count':len(terms),'neg_terms_tested':len(neg_terms),
   'distinct_neg_semantic_signatures':len({signature(x['F']) for x in neg_terms}),
   'actual_disjoint_orthoor_count':len(or_terms),
   'distinct_orthoor_semantic_signatures':len({signature(x['F']) for x in or_terms}),
   'terms_tested':len(tested),'universal_shadow_mismatches':len(mismatches),
   'mismatch_kind_histogram':dict(sorted(mismatch_kinds.items())),
   'provenance_chained_digest_sha256':prov_digest,
   'actual_shadow_table_chained_digest_sha256':shadow_table_chain.hexdigest(),
   'full_mismatch_chained_digest_sha256':mismatch_digest,
   'actual_kernel_bad_terms':actual_bad,'coordinate_kernel_bad_terms':coord_bad,
   'first_mismatches':mismatches[:12]})
 out={'schema':SCHEMA,'schema_version':'1.0','base_full_cycle_payload_sha256':base['payload_sha256'],
  'adjacent_factor_checkpoint_payload_sha256':factor['payload_sha256'],
  'source_join_rich_payload_sha256':source['payload_sha256'],
  'sample_rule':'same 3 endpoint-spread retained A/orientation and 2 smallest nonempty U/A; canonical minimum-index opposite witness',
  'old_atom_count':len(atoms),'orientation_records':records,'first_discriminator':global_first,
  'old_atom_target_subset_tests':ktests,'simultaneous_pattern_cache_entries':len(pcache),
  'fibre_product_basis':'The adjacent carrier is the full conditional fibre product over the shared state. Therefore every realized retained-side truth pattern pairs with every realized opposite-side truth pattern at fixed shared state.',
  'scope':'Bounded six-leaf actual two-copy relation quotient with one canonical minimal-E/minimum-index opposite witness per (A,U); exact shared-state pattern enumeration and exact MDD universal shadows. Other exact opposite witnesses in the same (E,U) class, arbitrary old operands, exhaustive mixed closure, latticehood, OML, sigma closure, MBRC, ODBC, and Phi are not covered.',
  'verification_independence':'Single producer; exact MDD grammar and join-rich sample receipt shared with prior controls. No independent verifier.',
  'evidence_classes':['Executable verified bounded evidence'],
  'command':'python3 notes/open_questions/verification/adjacent_full_cycle_actual_event_shadow.py --verify'}
 out['producer_sha256']=hashlib.sha256(open(__file__,'rb').read()).hexdigest()
 out['payload_sha256']=hashlib.sha256(json.dumps(out,sort_keys=True,separators=(',',':')).encode()).hexdigest()
 return out,time.perf_counter()-started
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--emit',action='store_true');ap.add_argument('--verify',action='store_true');a=ap.parse_args()
 out,seconds=payload();path=os.path.join(HERE,'adjacent_full_cycle_actual_event_shadow.json')
 if a.emit:
  with open(path,'w') as f:json.dump(out,f,sort_keys=True,indent=2);f.write('\n')
 else:assert json.load(open(path))==out
 print(json.dumps({'status':'PASS','payload_sha256':out['payload_sha256'],'first_discriminator':out['first_discriminator'],'runtime_seconds':round(seconds,3)},sort_keys=True))
