#!/usr/bin/env python3
"""Sparse exact restricted-section containment census for atomic kernels.

For 64 endpoint-spread retained events in each adjacent orientation, this
replays every admissible-U atomic fold far enough to enumerate exactly the
bad(D,A) queries made by the grouped kernel engine.  Each assigned section is
canonicalized in a separate immutable DAG (the banked MDDs are never mutated).
Containment is cached only for restricted trace-class pairs that are actually
queried.  Every compressed bad mask is compared with a direct read-only MDD
oracle.  No global class matrix is built.
"""
import argparse,collections,hashlib,json,os,resource,signal,sys,time

HERE=os.path.dirname(os.path.abspath(__file__));sys.path.insert(0,HERE)
import full_cycle_adjacent_rectangle_intersection as inter

SCHEMA='adjacent-full-cycle-sparse-containment-pairs-v1'
SPREAD=64

def payload():
 start=time.perf_counter();base,b=inter.capture_grammar()
 events=b['all_events'];macros=b['macros'];engines=b['engines'];states=b['states']
 roots={ev:r for r,ev in b['root_to_event'].items()};principal=b['principal']
 n=len(events);N=len(states);assert (n,N)==(18676,224)
 upmap={u:i for i,u in enumerate(principal)};assert len(upmap)==n
 allold=(1<<n)-1;zero=upmap[allold];nonatomic=0
 for d,u in enumerate(principal):
  if d!=zero:nonatomic|=u&~(1<<d)
 atom_bits=allold&~nonatomic&~(1<<zero);atoms=[]
 while atom_bits:
  z=atom_bits&-atom_bits;atoms.append(z.bit_length()-1);atom_bits-=z
 assert len(atoms)==91

 occurrences=[[[] for _ in range(N)] for _ in range(4)]
 for m,(_,ds) in enumerate(macros):
  for pos in range(4):
   for i,s in enumerate(ds[pos]):occurrences[pos][s].append((m,i))

 # Classification is copied from the committed exact streaming oracle.  Its
 # status recursion is read-only and only distinguishes empty/full/partial.
 status_cache={}
 def status(m,r,pos,i):
  key=(m,r,pos,i)
  if key in status_cache:return status_cache[key]
  if r<=1:z=r
  else:
   v,ch=engines[m].nodes[r]
   if v==pos:z=status(m,ch[i],pos,i)
   else:
    vals={status(m,x,pos,i) for x in ch};z=vals.pop() if len(vals)==1 else 2
  status_cache[key]=z;return z
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
  fam=[]
  for EA,_ in classes:
   us=[U for U,xs in op.items() if any(not EA&E for E,_ in xs)]
   fam.append(tuple(sorted(us,key=lambda u:(u.bit_count(),u))))
  return fam
 left_us=admissible(left,minima(right));right_us=admissible(right,minima(left))
 assert (sum(map(len,left_us)),sum(map(len,right_us)))==(28023,27699)
 def sample(fams):
  active=[i for i,u in enumerate(fams) if u]
  return tuple(active[(t*(len(active)-1))//(SPREAD-1)] for t in range(SPREAD))

 # Immutable canonical assigned-section DAGs.  IDs are local to each
 # (orientation, macrofibre), terminals are 0/1, and reduction is exact.
 class Factory:
  __slots__=('pos','m','nodes','intern','cache','subset_cache')
  def __init__(self,pos,m):
   self.pos=pos;self.m=m;self.nodes=[None,None];self.intern={};self.cache={};self.subset_cache={}
  def node(self,v,ch):
   if all(x==ch[0] for x in ch):return ch[0]
   k=(v,tuple(ch));z=self.intern.get(k)
   if z is None:z=len(self.nodes);self.intern[k]=z;self.nodes.append(k)
   return z
  def restrict(self,r,i):
   k=(r,i);z=self.cache.get(k)
   if z is not None:return z
   if r<=1:z=r
   else:
    v,ch=engines[self.m].nodes[r]
    if v==self.pos:z=self.restrict(ch[i],i)
    else:z=self.node(v,[self.restrict(x,i) for x in ch])
   self.cache[k]=z;return z
  def subset(self,a,c):
   if not a or c==1 or a==c:return True
   k=(a,c);z=self.subset_cache.get(k)
   if z is not None:return z
   if a<=1 and c<=1:z=bool((not a) or c)
   else:
    va,ca=self.nodes[a] if a>1 else (10**9,None)
    vc,cc=self.nodes[c] if c>1 else (10**9,None);v=min(va,vc)
    aa=ca if va==v else (a,)*len(engines[self.m].domains[v])
    cy=cc if vc==v else (c,)*len(engines[self.m].domains[v])
    z=all(self.subset(x,y) for x,y in zip(aa,cy))
   self.subset_cache[k]=z;return z

 # Independent direct oracle on original MDD nodes, after assignment, with
 # no engine.node/app/neg calls.
 oracle_calls=oracle_nodes=0
 def oracle_subset(m,x,y,pos,i):
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
    if v==pos:
     aa=ca[i] if va==v else a;cy=cc[i] if vc==v else c;z=go(aa,cy)
    else:
     aa=ca if va==v else (a,)*len(engines[m].domains[v])
     cy=cc if vc==v else (c,)*len(engines[m].domains[v])
     z=all(go(a0,c0) for a0,c0 in zip(aa,cy))
   memo[k]=z;return z
  return go(x,y)

 baseline=(sum(len(e.nodes) for e in engines),sum(len(e.acache) for e in engines),sum(len(e.ncache) for e in engines))
 records=[];digest=hashlib.sha256();total_bad_queries=total_raw=total_pair_lookups=0
 def run(name,pos,classes,fams):
  nonlocal total_bad_queries,total_raw,total_pair_lookups
  chosen=sample(fams);factories=[Factory(pos,m) for m in range(len(macros))]
  class_maps=[{} for _ in range(N)];class_words=[[] for _ in range(N)]
  pair_cache=[{} for _ in range(N)];state_raw=[0]*N;state_lookups=[0]*N
  event_class_cache={}
  def cid(ev,s):
   k=(ev,s)
   if k in event_class_cache:return event_class_cache[k]
   rr=roots[events[ev]]
   word=tuple(factories[m].restrict(rr[m],i) for m,i in occurrences[pos][s])
   z=class_maps[s].get(word)
   if z is None:z=len(class_words[s]);class_maps[s][word]=z;class_words[s].append(word)
   event_class_cache[k]=z;return z
  def compressed_subset(D,A,s):
   nonlocal total_pair_lookups
   x=cid(D,s);y=cid(A,s);k=(x,y);state_lookups[s]+=1;total_pair_lookups+=1
   if k not in pair_cache[s]:
    wx=class_words[s][x];wy=class_words[s][y]
    pair_cache[s][k]=all(factories[m].subset(a,c) for (m,_),a,c in zip(occurrences[pos][s],wx,wy))
   return pair_cache[s][k]
  def bad_pair(D,A):
   nonlocal total_bad_queries,total_raw
   EA,UA=classes[A];ED,_=classes[D];cand=ED&~UA;oracle=compressed=0
   dr=roots[events[D]];ar=roots[events[A]]
   while cand:
    bit=cand&-cand;s=bit.bit_length()-1;cand-=bit
    oz=True
    for m,i in occurrences[pos][s]:
     state_raw[s]+=1;total_raw+=1
     if not oracle_subset(m,dr[m],ar[m],pos,i):oz=False;break
    cz=compressed_subset(D,A,s)
    assert oz==cz,(name,D,A,s,oz,cz)
    if not oz:oracle|=bit
    if not cz:compressed|=bit
   assert oracle==compressed,(name,D,A,oracle,compressed)
   total_bad_queries+=1;digest.update(f'{name},{D},{A},{oracle:x}\n'.encode())
   return oracle
  kernel_count=transition_count=failing_kernels=0;orientation_bad_start=total_bad_queries
  for A in chosen:
   us=fams[A];kernel_count+=len(us);full=(1<<len(us))-1
   groups={A:full};cache={}
   def bad(D):
    if D not in cache:cache[D]=bad_pair(D,A)
    return cache[D]
   atom_bad={a:bad(a) for a in atoms}
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
     J=upmap[principal[P]&principal[a]];Q=bad(J);transition_count+=1
     passed=0;z=eligible
     while z:
      bit=z&-z;ui=bit.bit_length()-1;z-=bit
      if not Q&~us[ui]:passed|=bit
      else:failing_kernels+=1
     if passed:nxt[J]|=passed
    groups=dict(nxt)
  per_state=[]
  for s in range(N):
   per_state.append({'state_index':s,'classes':len(class_words[s]),
    'assigned_oracle_occurrence_comparisons':state_raw[s],
    'class_pair_lookups':state_lookups[s],'distinct_class_pair_queries':len(pair_cache[s])})
  word_roots=sum(sum(len(w) for w in ws) for ws in class_words)
  records.append({'orientation':name,'position':pos,'selected_retained_events':len(chosen),
   'selected_event_indices_sha256':hashlib.sha256(','.join(map(str,chosen)).encode()).hexdigest(),
   'admissible_kernels':kernel_count,'group_join_transitions':transition_count,
   'failing_kernels':failing_kernels,'passing_kernels':kernel_count-failing_kernels,
   'bad_event_pair_queries':total_bad_queries-orientation_bad_start,
   'interned_event_state_assignments':len(event_class_cache),
   'total_classes':sum(len(x) for x in class_words),
   'total_distinct_class_pair_queries':sum(len(x) for x in pair_cache),
   'total_class_pair_lookups':sum(state_lookups),
   'total_assigned_oracle_occurrence_comparisons':sum(state_raw),
   'per_state':per_state,
   'immutable_restricted_dag_nodes':sum(len(f.nodes)-2 for f in factories),
   'immutable_subset_cache_entries':sum(len(f.subset_cache) for f in factories),
   'canonical_trace_word_root_ids':word_roots,
   'deterministic_uint32_payload_lower_bound_bytes':4*(word_roots+2*sum(len(x) for x in pair_cache))})
 run('left_retained_position11',3,left,left_us)
 run('right_retained_position00',0,right,right_us)
 final=(sum(len(e.nodes) for e in engines),sum(len(e.acache) for e in engines),sum(len(e.ncache) for e in engines))
 assert final==baseline,(baseline,final)
 peak=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
 sampled_kernels=sum(r['admissible_kernels'] for r in records)
 distinct_pairs=sum(r['total_distinct_class_pair_queries'] for r in records)
 linear_projection=(distinct_pairs*55722+sampled_kernels-1)//sampled_kernels
 out={'schema':SCHEMA,'schema_version':'1.0','base_full_cycle_payload_sha256':base['payload_sha256'],
  'completed_events_each':n,'shared_states':N,'old_atom_count':len(atoms),
  'sample':'64 endpoint-spread retained events with a live admissible U in each orientation',
  'orientation_records':records,'bad_event_pair_queries':total_bad_queries,
  'raw_assigned_occurrence_comparisons':total_raw,'class_pair_lookups':total_pair_lookups,
  'distinct_class_pair_queries':distinct_pairs,
  'bad_mask_digest_sha256':digest.hexdigest(),'oracle_calls':oracle_calls,'oracle_recursive_nodes':oracle_nodes,
  'mdd_snapshot_before_sparse_queries':list(baseline),'mdd_snapshot_after_sparse_queries':list(final),
  'deterministic_memory_accounting':{
   'canonical_trace_word_root_ids':sum(r['canonical_trace_word_root_ids'] for r in records),
   'immutable_restricted_dag_nodes':sum(r['immutable_restricted_dag_nodes'] for r in records),
   'immutable_subset_cache_entries':sum(r['immutable_subset_cache_entries'] for r in records),
   'distinct_class_pair_entries':distinct_pairs,
   'uint32_payload_lower_bound_bytes':sum(r['deterministic_uint32_payload_lower_bound_bytes'] for r in records)},
  'linear_distinct_pair_projection_at_55722_kernels':linear_projection,
  'complete_scan_assessment':('Not supported by retaining sample-global Python class/pair caches: the sampled demand linearly projects to tens of millions of distinct pairs. The measurements support a per-retained-A eviction design, not this accumulating-cache design, for a complete 55,722-kernel scan.'),
  'comparison_unit_semantics':('A raw assigned occurrence comparison is one direct original-MDD containment test at one macrofibre occurrence, with short-circuit on the first failure. A class-pair lookup tests or reuses containment of one complete assigned-state trace word across all of that state\'s occurrences.'),
  'quantifier_scope':'Every admissible U and every atomic transition reached for exactly 64 endpoint-spread retained A in each orientation.',
  'scope_not_covered':'The other retained events, complete 55,722 kernels, later mixed closure, latticehood, OML, sigma closure, MBRC, ODBC, and Phi.',
  'verification_independence':'Compressed immutable-DAG containment and the direct original-MDD oracle use separate recursion implementations but share capture_grammar and classification. No independent verifier.',
  'evidence_classes':['Executable verified'],
  'command':'python3 notes/open_questions/verification/adjacent_full_cycle_sparse_containment_pairs.py --verify'}
 out['producer_sha256']=hashlib.sha256(open(__file__,'rb').read()).hexdigest()
 out['payload_sha256']=hashlib.sha256(json.dumps(out,sort_keys=True,separators=(',',':')).encode()).hexdigest()
 return out,time.perf_counter()-start,peak

if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--emit',action='store_true');ap.add_argument('--verify',action='store_true');a=ap.parse_args()
 def alarm(_s,_f):raise TimeoutError('sparse containment census exceeded 720 seconds')
 prior=signal.getsignal(signal.SIGALRM);signal.signal(signal.SIGALRM,alarm);signal.alarm(720)
 try:out,seconds,peak=payload()
 finally:signal.alarm(0);signal.signal(signal.SIGALRM,prior)
 path=os.path.join(HERE,'adjacent_full_cycle_sparse_containment_pairs.json')
 if a.emit:
  with open(path,'w') as f:json.dump(out,f,sort_keys=True,indent=2);f.write('\n')
 else:assert json.load(open(path))==out
 print(json.dumps({'status':'PASS','payload_sha256':out['payload_sha256'],
  'bad_queries':out['bad_event_pair_queries'],'raw_comparisons':out['raw_assigned_occurrence_comparisons'],
  'distinct_class_pairs':out['distinct_class_pair_queries'],'peak_rss_platform_units_console_only':peak,
  'runtime_seconds':round(seconds,3)},sort_keys=True))
