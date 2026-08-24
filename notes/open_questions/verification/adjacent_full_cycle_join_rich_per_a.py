#!/usr/bin/env python3
"""Join-rich per-A eviction audit for adjacent atomic lower kernels.

The sample is selected before any restricted-trace containment work.  Among
retained events having a nonempty admissible universal mask, rank by

  (# nonempty admissible U) * (# distinct proper atomic join targets),

then by the two factors and event index.  The top 128 in each orientation are
audited.  U=empty kernels are discharged algebraically: A itself is an
eligible old lower and therefore the greatest old lower.

For every selected A, immutable restricted-section DAGs, trace classes, and
containment pairs are created afresh and discarded before the next A.  Every
compressed bad(D,A) mask is compared with a separate read-only recursion on
the original MDDs.  No global containment matrix or cross-A cache is built.
"""
import argparse,collections,hashlib,json,os,resource,signal,sys,time

HERE=os.path.dirname(os.path.abspath(__file__));sys.path.insert(0,HERE)
import full_cycle_adjacent_rectangle_intersection as inter

SCHEMA='adjacent-full-cycle-join-rich-per-a-v1'
SAMPLE=128

def payload():
 started=time.perf_counter();base,b=inter.capture_grammar()
 events=b['all_events'];macros=b['macros'];engines=b['engines'];states=b['states']
 roots={ev:r for r,ev in b['root_to_event'].items()};principal=b['principal']
 n=len(events);N=len(states);assert (n,N)==(18676,224)
 upmap={u:i for i,u in enumerate(principal)};assert len(upmap)==n
 allold=(1<<n)-1;zero=upmap[allold];nonatomic=0
 for d,u in enumerate(principal):
  if d!=zero:nonatomic|=u&~(1<<d)
 bits=allold&~nonatomic&~(1<<zero);atoms=[]
 while bits:
  z=bits&-bits;atoms.append(z.bit_length()-1);bits-=z
 assert len(atoms)==91

 occurrences=[[[] for _ in range(N)] for _ in range(4)]
 for m,(_,ds) in enumerate(macros):
  for pos in range(4):
   for i,s in enumerate(ds[pos]):occurrences[pos][s].append((m,i))

 status_cache={}
 def status(m,r,pos,i):
  k=(m,r,pos,i)
  if k in status_cache:return status_cache[k]
  if r<=1:z=r
  else:
   v,ch=engines[m].nodes[r]
   if v==pos:z=status(m,ch[i],pos,i)
   else:
    q={status(m,x,pos,i) for x in ch};z=q.pop() if len(q)==1 else 2
  status_cache[k]=z;return z
 def classify(pos):
  ans=[]
  for ev in events:
   E=U=0;rr=roots[ev]
   for s,occ in enumerate(occurrences[pos]):
    vals=[status(m,rr[m],pos,i) for m,i in occ]
    if any(vals):E|=1<<s
    if all(x==1 for x in vals):U|=1<<s
   ans.append((E,U))
  return ans
 left=classify(3);right=classify(0)
 def minima(classes):
  groups=collections.defaultdict(list)
  for i,(E,U) in enumerate(classes):groups[U].append((E,i))
  out={}
  for U,xs in groups.items():
   keep=[]
   for E,i in sorted(xs,key=lambda x:(x[0].bit_count(),x[0],x[1])):
    if not any(not K&~E for K,_ in keep):keep.append((E,i))
   out[U]=tuple(keep)
  return out
 def admissible(classes,op):
  out=[]
  for EA,_ in classes:
   out.append(tuple(sorted((U for U,xs in op.items()
    if any(not EA&E for E,_ in xs)),key=lambda u:(u.bit_count(),u))))
  return out
 left_us=admissible(left,minima(right));right_us=admissible(right,minima(left))
 assert (sum(map(len,left_us)),sum(map(len,right_us)))==(28023,27699)

 # Algebraic selection descriptor: no restricted roots or containment queries.
 join_targets={}
 def joins(A):
  z=join_targets.get(A)
  if z is None:
   z=len({upmap[principal[A]&principal[a]] for a in atoms
    if not (principal[a]>>A&1)})
   join_targets[A]=z
  return z
 def select(fams):
  ranked=[]
  for A,us0 in enumerate(fams):
   us=tuple(u for u in us0 if u)
   if us:
    j=joins(A);ranked.append((-(len(us)*j),-j,-len(us),A))
  ranked.sort()
  return tuple(x[3] for x in ranked[:SAMPLE]),ranked

 class Factory:
  __slots__=('pos','m','nodes','intern','restrict_cache','subset_cache')
  def __init__(self,pos,m):
   self.pos=pos;self.m=m;self.nodes=[None,None];self.intern={}
   self.restrict_cache={};self.subset_cache={}
  def node(self,v,ch):
   if all(x==ch[0] for x in ch):return ch[0]
   k=(v,tuple(ch));z=self.intern.get(k)
   if z is None:z=len(self.nodes);self.intern[k]=z;self.nodes.append(k)
   return z
  def restrict(self,r,i):
   k=(r,i)
   if k in self.restrict_cache:return self.restrict_cache[k]
   if r<=1:z=r
   else:
    v,ch=engines[self.m].nodes[r]
    z=self.restrict(ch[i],i) if v==self.pos else self.node(v,[self.restrict(x,i) for x in ch])
   self.restrict_cache[k]=z;return z
  def subset(self,a,c):
   if not a or c==1 or a==c:return True
   k=(a,c)
   if k in self.subset_cache:return self.subset_cache[k]
   if a<=1 and c<=1:z=bool((not a) or c)
   else:
    va,ca=self.nodes[a] if a>1 else (10**9,None)
    vc,cc=self.nodes[c] if c>1 else (10**9,None);v=min(va,vc)
    aa=ca if va==v else (a,)*len(engines[self.m].domains[v])
    cc2=cc if vc==v else (c,)*len(engines[self.m].domains[v])
    z=all(self.subset(x,y) for x,y in zip(aa,cc2))
   self.subset_cache[k]=z;return z

 oracle_calls=oracle_nodes=0
 def oracle(m,x,y,pos,i):
  nonlocal oracle_calls,oracle_nodes
  oracle_calls+=1;memo={}
  def go(a,c):
   nonlocal oracle_nodes
   if not a or c==1 or a==c:return True
   k=(a,c)
   if k in memo:return memo[k]
   oracle_nodes+=1
   if a<=1 and c<=1:z=bool((not a) or c)
   else:
    va,ca=engines[m].nodes[a] if a>1 else (10**9,None)
    vc,cc=engines[m].nodes[c] if c>1 else (10**9,None);v=min(va,vc)
    if v==pos:z=go(ca[i] if va==v else a,cc[i] if vc==v else c)
    else:
     aa=ca if va==v else (a,)*len(engines[m].domains[v])
     yy=cc if vc==v else (c,)*len(engines[m].domains[v])
     z=all(go(p,q) for p,q in zip(aa,yy))
   memo[k]=z;return z
  return go(x,y)

 baseline=(sum(len(e.nodes) for e in engines),sum(len(e.acache) for e in engines),sum(len(e.ncache) for e in engines))
 digest=hashlib.sha256();records=[];global_raw=global_lookups=global_distinct=global_bad=0
 def orientation(name,pos,classes,fams):
  nonlocal global_raw,global_lookups,global_distinct,global_bad
  chosen,ranked=select(fams);per_a=[];failures=transitions=kernels=0
  tautologies=sum(0 in us for us in fams)
  nontrivial_global=sum(sum(bool(u) for u in us) for us in fams)
  for A in chosen:
   us=tuple(u for u in fams[A] if u);assert us
   kernels+=len(us);factories=[Factory(pos,m) for m in range(len(macros))]
   maps=[{} for _ in range(N)];words=[[] for _ in range(N)];pairs=[{} for _ in range(N)]
   event_classes={};raw=lookups=bad_queries=0
   def cid(D,s):
    k=(D,s)
    if k in event_classes:return event_classes[k]
    rr=roots[events[D]]
    w=tuple(factories[m].restrict(rr[m],i) for m,i in occurrences[pos][s])
    z=maps[s].get(w)
    if z is None:z=len(words[s]);maps[s][w]=z;words[s].append(w)
    event_classes[k]=z;return z
   def compressed(D,s):
    nonlocal lookups
    x=cid(D,s);y=cid(A,s);k=(x,y);lookups+=1
    if k not in pairs[s]:
     wx=words[s][x];wy=words[s][y]
     pairs[s][k]=all(factories[m].subset(p,q)
      for (m,_),p,q in zip(occurrences[pos][s],wx,wy))
    return pairs[s][k]
   bad_cache={}
   def bad(D):
    nonlocal raw,bad_queries
    if D in bad_cache:return bad_cache[D]
    EA,UA=classes[A];ED,_=classes[D];cand=ED&~UA;direct=packed=0
    dr=roots[events[D]];ar=roots[events[A]]
    while cand:
     bit=cand&-cand;s=bit.bit_length()-1;cand-=bit;ok=True
     for m,i in occurrences[pos][s]:
      raw+=1
      if not oracle(m,dr[m],ar[m],pos,i):ok=False;break
     ck=compressed(D,s);assert ck==ok,(name,A,D,s,ck,ok)
     if not ok:direct|=bit
     if not ck:packed|=bit
    assert direct==packed
    bad_cache[D]=direct;bad_queries+=1
    digest.update(f'{name},{A},{D},{direct:x}\n'.encode());return direct
   full=(1<<len(us))-1;groups={A:full};atom_bad={a:bad(a) for a in atoms}
   for a in atoms:
    ba=atom_bad[a];nxt=collections.defaultdict(int)
    for P,ubits in sorted(groups.items()):
     eligible=0;z=ubits
     while z:
      bit=z&-z;ui=bit.bit_length()-1;z-=bit
      if not ba&~us[ui]:eligible|=bit
     if ubits&~eligible:nxt[P]|=ubits&~eligible
     if not eligible:continue
     if principal[a]>>P&1:nxt[P]|=eligible;continue
     J=upmap[principal[P]&principal[a]];Q=bad(J);transitions+=1
     passed=0;z=eligible
     while z:
      bit=z&-z;ui=bit.bit_length()-1;z-=bit
      if Q&~us[ui]:failures+=1
      else:passed|=bit
     if passed:nxt[J]|=passed
    groups=dict(nxt)
   distinct=sum(len(x) for x in pairs)
   root_ids=sum(sum(len(w) for w in ws) for ws in words)
   per_a.append({'event_index':A,'nonempty_admissible_kernels':len(us),
    'distinct_proper_atomic_join_targets':joins(A),'selection_score':len(us)*joins(A),
    'bad_event_pair_queries':bad_queries,'raw_short_circuit_occurrence_comparisons':raw,
    'whole_state_class_pair_lookups':lookups,'distinct_whole_state_class_pairs':distinct,
    'interned_trace_classes':sum(len(x) for x in words),
    'canonical_trace_word_root_ids':root_ids,
    'immutable_restricted_dag_nodes':sum(len(f.nodes)-2 for f in factories),
    'immutable_subset_cache_entries':sum(len(f.subset_cache) for f in factories),
    'uint32_payload_lower_bound_bytes':4*(root_ids+2*distinct)})
   global_raw+=raw;global_lookups+=lookups;global_distinct+=distinct;global_bad+=bad_queries
   # All per-A structures become unreachable here; the next loop allocates new.
  keys=['bad_event_pair_queries','raw_short_circuit_occurrence_comparisons',
   'whole_state_class_pair_lookups','distinct_whole_state_class_pairs',
   'interned_trace_classes','canonical_trace_word_root_ids',
   'immutable_restricted_dag_nodes','immutable_subset_cache_entries',
   'uint32_payload_lower_bound_bytes']
  agg={k:sum(x[k] for x in per_a) for k in keys}
  peaks={k:max(x[k] for x in per_a) for k in keys}
  records.append({'orientation':name,'position':pos,'selected_retained_events':len(chosen),
   'selected_event_indices':list(chosen),
   'selected_event_indices_sha256':hashlib.sha256(','.join(map(str,chosen)).encode()).hexdigest(),
   'selection_rule':'descending (# nonempty admissible U)*(# distinct proper atomic join targets), then both factors descending, then event index ascending',
   'selection_cutoff_score':per_a[-1]['selection_score'],
   'global_u_empty_tautological_kernels':tautologies,
   'global_nonempty_admissible_kernels':nontrivial_global,
   'sample_nonempty_admissible_kernels':kernels,'sample_failures':failures,
   'sample_passes':kernels-failures,'group_join_transitions':transitions,
   'aggregate_per_a_counters':agg,'peak_single_a_counters':peaks,'per_a':per_a})
 orientation('left_retained_position11',3,left,left_us)
 orientation('right_retained_position00',0,right,right_us)
 final=(sum(len(e.nodes) for e in engines),sum(len(e.acache) for e in engines),sum(len(e.ncache) for e in engines))
 assert final==baseline
 out={'schema':SCHEMA,'schema_version':'1.0','base_full_cycle_payload_sha256':base['payload_sha256'],
  'completed_events_each':n,'shared_states':N,'old_atom_count':len(atoms),
  'u_empty_discharge':('Hand proved: if U is empty, the retained event A is itself an eligible old lower and dominates every eligible lower, so the kernel is A without trace work.'),
  'complete_kernel_counts':{'left_all':28023,'right_all':27699,'all':55722,
   'u_empty_tautological':sum(r['global_u_empty_tautological_kernels'] for r in records),
   'nonempty':sum(r['global_nonempty_admissible_kernels'] for r in records)},
  'orientation_records':records,'sample_nonempty_kernels':sum(r['sample_nonempty_admissible_kernels'] for r in records),
  'sample_failures':sum(r['sample_failures'] for r in records),
  'bad_event_pair_queries':global_bad,'raw_short_circuit_occurrence_comparisons':global_raw,
  'whole_state_class_pair_lookups':global_lookups,'sum_per_a_distinct_class_pairs':global_distinct,
  'bad_mask_digest_sha256':digest.hexdigest(),'oracle_calls':oracle_calls,'oracle_recursive_nodes':oracle_nodes,
  'mdd_snapshot_before':list(baseline),'mdd_snapshot_after':list(final),
  'eviction_discipline':'All restricted DAGs, event classes, and class-pair caches are allocated inside one retained-A iteration and discarded before the next A.',
  'comparison_unit_semantics':'Raw comparisons are direct original-MDD tests at one occurrence with short circuit; one class-pair lookup covers the complete assigned-state trace word.',
  'quantifier_scope':'All nonempty admissible U and reached atomic transitions for the deterministic top 128 algebraically join-rich retained events in each orientation.',
  'scope_not_covered':'Unselected retained events, complete 18,370 nontrivial kernels, later mixed closure, latticehood, OML, sigma closure, MBRC, ODBC, and Phi.',
  'verification_independence':'Every compressed containment result is checked against a separate read-only recursion on original MDD roots. Classification and the underlying grammar are shared; there is no independent producer.',
  'evidence_classes':['Hand proved','Executable verified'],
  'command':'python3 notes/open_questions/verification/adjacent_full_cycle_join_rich_per_a.py --verify'}
 out['producer_sha256']=hashlib.sha256(open(__file__,'rb').read()).hexdigest()
 out['payload_sha256']=hashlib.sha256(json.dumps(out,sort_keys=True,separators=(',',':')).encode()).hexdigest()
 return out,time.perf_counter()-started,resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--emit',action='store_true');ap.add_argument('--verify',action='store_true');a=ap.parse_args()
 def timeout(_s,_f):raise TimeoutError('join-rich per-A audit exceeded 720 seconds')
 prior=signal.getsignal(signal.SIGALRM);signal.signal(signal.SIGALRM,timeout);signal.alarm(720)
 try:out,seconds,peak=payload()
 finally:signal.alarm(0);signal.signal(signal.SIGALRM,prior)
 path=os.path.join(HERE,'adjacent_full_cycle_join_rich_per_a.json')
 if a.emit:
  with open(path,'w') as f:json.dump(out,f,sort_keys=True,indent=2);f.write('\n')
 else:assert json.load(open(path))==out
 print(json.dumps({'status':'PASS','payload_sha256':out['payload_sha256'],
  'nonempty_kernels':out['sample_nonempty_kernels'],'failures':out['sample_failures'],
  'distinct_pairs':out['sum_per_a_distinct_class_pairs'],
  'peak_rss_platform_units_console_only':peak,'runtime_seconds':round(seconds,3)},sort_keys=True))
