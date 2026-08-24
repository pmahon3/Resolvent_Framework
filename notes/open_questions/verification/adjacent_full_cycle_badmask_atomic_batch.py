#!/usr/bin/env python3
"""Bad-mask atomic batching prototype for adjacent full-cycle kernels.

This replaces construction of an 842-component physical core for each
symbolic kernel by exact conditional-trace masks.  For retained event A put

  Bad_A(D) = {s : trace_s(D) is not contained in trace_s(A)}.

For an admissible opposite universal mask U, D is below the mixed core iff
Bad_A(D) is contained in U.  The finite old OML is atomistic, so the kernel
exists iff folding all eligible old atoms by old joins never produces an
accumulator whose bad mask escapes U.

The default is a feasibility prototype, not an exhaustive atlas.  It builds
the complete admissible-U families, then tests a deterministic stratified
sample in both orientations.  --legacy-prefix 100 additionally replays the
banked order-biased prefix for an exact five-field aggregate comparison
(kernels, passing, failures, join folds, and maximum folds).  No 842-component
mixed cores are constructed by the batched decision procedure.
"""
import argparse,collections,functools,hashlib,json,os,struct,sys,time

HERE=os.path.dirname(os.path.abspath(__file__));sys.path.insert(0,HERE)
import full_cycle_adjacent_rectangle_intersection as inter

SCHEMA='adjacent-full-cycle-badmask-atomic-batch-v1'

def payload(sample_per_orientation=64,legacy_prefix=100,descriptor_sample=128):
 start=time.perf_counter();phase_times={};t=time.perf_counter();base,b=inter.capture_grammar();phase_times['capture_grammar']=time.perf_counter()-t
 events=b['all_events'];macros=b['macros'];engines=b['engines'];states=b['states'];N=len(states)
 roots={ev:r for r,ev in b['root_to_event'].items()}
 principal=b['principal'];nold=len(events);assert nold==18676 and len(principal)==nold
 upmap={u:i for i,u in enumerate(principal)};assert len(upmap)==nold
 allold=(1<<nold)-1;zero=upmap[allold]
 nonatomic=0
 for d,u in enumerate(principal):
  if d!=zero:nonatomic|=u&~(1<<d)
 atom_bits=allold&~nonatomic&~(1<<zero);atoms=[]
 while atom_bits:
  z=atom_bits&-atom_bits;atoms.append(z.bit_length()-1);atom_bits-=z
 assert len(atoms)==91

 # Exact empty/universal masks and cached restrictions.  The restriction is an
 # MDD in the remaining coordinates, not the coarse 0/partial/1 shadow.
 @functools.lru_cache(None)
 def restrict(m,root,pos,i):
  if root<=1:return root
  v,ch=engines[m].nodes[root]
  if v==pos:return ch[i]
  return engines[m].node(v,[restrict(m,z,pos,i) for z in ch])
 occurrences=[[[] for _ in range(N)] for _ in range(4)]
 for m,(_,ds) in enumerate(macros):
  for pos in range(4):
   for i,s in enumerate(ds[pos]):occurrences[pos][s].append((m,i))

 def classify(pos):
  ans=[]
  for ev in events:
   E=U=0;rr=roots[ev]
   for s,occ in enumerate(occurrences[pos]):
    vals=[restrict(m,rr[m],pos,i) for m,i in occ]
    if any(vals):E|=1<<s
    if all(z==1 for z in vals):U|=1<<s
   ans.append((E,U))
  return ans
 t=time.perf_counter();left=classify(3);right=classify(0);phase_times['exact_trace_classification']=time.perf_counter()-t

 def minimal_existentials(classes):
  groups=collections.defaultdict(list)
  for i,(E,U) in enumerate(classes):groups[U].append((E,i))
  out={};discarded=0
  for U,xs in groups.items():
   keep=[]
   for E,i in sorted(xs,key=lambda z:(z[0].bit_count(),z[0],z[1])):
    if any(not K&~E for K,_ in keep):discarded+=1
    else:keep.append((E,i))
   out[U]=tuple(keep)
  return out,discarded
 left_by_u,left_discard=minimal_existentials(left)
 right_by_u,right_discard=minimal_existentials(right)

 # Inclusion of conditional traces.  Empty and universal masks discharge most
 # states; only genuinely partial intersections reach an MDD subset test.
 bad_cache={}
 partial_state_tests=0;mdd_subset_tests=0
 def bad(pos,Ai,Di,classes):
  nonlocal partial_state_tests,mdd_subset_tests
  key=(pos,Ai,Di)
  if key in bad_cache:return bad_cache[key]
  EA,UA=classes[Ai];ED,UD=classes[Di];cand=ED&~UA;ans=0
  ar=roots[events[Ai]];dr=roots[events[Di]]
  while cand:
   bit=cand&-cand;s=bit.bit_length()-1;cand-=bit;partial_state_tests+=1
   ok=True
   for m,i in occurrences[pos][s]:
    x=restrict(m,dr[m],pos,i);y=restrict(m,ar[m],pos,i);mdd_subset_tests+=1
    if engines[m].app(0,x,engines[m].neg(y)):
     ok=False;break
   if not ok:ans|=bit
  bad_cache[key]=ans;return ans

 # Complete admissible U family.  Same-U existential representatives only
 # witness physical disjointness; the batch subsequently depends on U alone.
 def admissible(classes,op_by_u):
  fam=[];total=0
  for A,(EA,UA) in enumerate(classes):
   us=[]
   for U,xs in op_by_u.items():
    if any(not EA&E for E,_ in xs):us.append(U)
   us=tuple(sorted(us,key=lambda u:(u.bit_count(),u)))
   fam.append(us);total+=len(us)
  return fam,total
 t=time.perf_counter();left_us,left_ceiling=admissible(left,right_by_u)
 right_us,right_ceiling=admissible(right,left_by_u);phase_times['complete_admissible_U_families']=time.perf_counter()-t

 # An exact atomic fold without constructing the mixed core.
 stats=collections.Counter();first_failure=None
 def inspect(direction,A,U,pos,classes,phase):
  nonlocal first_failure
  stats['kernels']+=1;j=A;folds=eligible=0
  phase['kernels']+=1
  for a in atoms:
   ba=bad(pos,A,a,classes)
   if ba&~U:continue
   eligible+=1
   if principal[a]>>j&1:continue
   old=j;j=upmap[principal[j]&principal[a]];folds+=1
   bj=bad(pos,A,j,classes)
   if bj&~U:
    stats['failures']+=1;phase['failures']+=1
    if first_failure is None:
     first_failure={'direction':direction,'retained_event_index':A,
      'universal_mask_sha256':hashlib.sha256(U.to_bytes(28,'little')).hexdigest(),
      'universal_state_count':U.bit_count(),'prior_accumulator_event_index':old,
      'new_atom_event_index':a,'escaping_join_event_index':j,
      'atom_bad_mask_sha256':hashlib.sha256(ba.to_bytes(28,'little')).hexdigest(),
      'escaping_bad_mask_sha256':hashlib.sha256(bj.to_bytes(28,'little')).hexdigest(),
      'escaping_states_outside_U':(bj&~U).bit_count(),'folds_before_escape':folds}
    break
  else:stats['passing']+=1;phase['passing']+=1
  stats['eligible_atoms']+=eligible;stats['join_folds']+=folds
  stats['maximum_folds']=max(stats['maximum_folds'],folds)
  phase['eligible_atoms']+=eligible;phase['join_folds']+=folds
  phase['maximum_folds']=max(phase['maximum_folds'],folds)
  return j

 # Legacy prefix: exactly the scanner's retained-event then sorted-U order.
 legacy_stats=collections.Counter()
 legacy=[]
 t=time.perf_counter()
 if legacy_prefix:
  for A,us in enumerate(left_us):
   # The banked v3 scanner orders its (U,...) choice tuples numerically by U.
   for U in sorted(us):
    legacy.append((A,U))
    if len(legacy)>=legacy_prefix:break
   if len(legacy)>=legacy_prefix:break
  for A,U in legacy:inspect('legacy_left_prefix',A,U,3,left,legacy_stats)
 legacy_delta=dict(legacy_stats)
 phase_times['legacy_prefix_fold']=time.perf_counter()-t

 # Deterministic stratification across retained-event ranks and U ranks.  This
 # is deliberately not a prefix.  Duplicate (A,U) cells are removed exactly.
 def stratified(fams,n):
  nonempty=[i for i,x in enumerate(fams) if x]
  if not nonempty or not n:return []
  picks=[]
  for t in range(n):
   ai=nonempty[(t*len(nonempty))//n]
   us=fams[ai];ui=(t*104729+t*t*17)%len(us);picks.append((ai,us[ui]))
  # Fill rare duplicate loss with a second coprime walk.
  out=[];seen=set()
  for x in picks:
   if x not in seen:seen.add(x);out.append(x)
  cursor=0
  while len(out)<min(n,sum(map(len,fams))):
   ai=nonempty[(cursor*8191)%len(nonempty)];us=fams[ai]
   x=(ai,us[(cursor*131071)%len(us)]);cursor+=1
   if x not in seen:seen.add(x);out.append(x)
  return out
 t=time.perf_counter();stratL=stratified(left_us,sample_per_orientation);stratR=stratified(right_us,sample_per_orientation)
 strat_stats=collections.Counter()
 for A,U in stratL:inspect('stratified_left',A,U,3,left,strat_stats)
 for A,U in stratR:inspect('stratified_right',A,U,0,right,strat_stats)
 strat_delta=dict(strat_stats)
 phase_times['stratified_kernel_folds']=time.perf_counter()-t

 # Exact batching descriptors: A-events with identical E and all 91 atomic bad
 # masks have identical eligible-atom sets for every admissible U.  This does
 # not quotient later accumulator checks, so it is a feasibility count only.
 def descriptors(pos,classes,fams,n):
  groups=collections.Counter();pairfamilies=set()
  chosen=stratified(fams,n)
  # Descriptor selection depends only on A, not on the sampled U cell.
  ais=sorted({A for A,_ in chosen})
  for A in ais:
   us=fams[A]
   avec=tuple(bad(pos,A,a,classes) for a in atoms)
   key=(classes[A][0],avec);groups[key]+=1
   pairfamilies.add((key,us))
  return groups,pairfamilies,len(ais)
 t=time.perf_counter();gL,pfL,nDL=descriptors(3,left,left_us,descriptor_sample);gR,pfR,nDR=descriptors(0,right,right_us,descriptor_sample)
 phase_times['sampled_descriptor_census']=time.perf_counter()-t

 # Banked prefix equivalence has fixed expected aggregate.  This is stronger
 # than merely observing no failure in another 100 kernels.
 legacy_expected={'kernels':100,'passing':100,'failures':0,'join_folds':137,'maximum_folds':10}
 legacy_match=all(legacy_delta.get(k,0)==v for k,v in legacy_expected.items())
 out={'schema':SCHEMA,'schema_version':'1.0','base_full_cycle_payload_sha256':base['payload_sha256'],
  'completed_events_each':nold,'shared_states':N,'old_atom_count':len(atoms),
  'left_distinct_universal_masks':len(left_by_u),'right_distinct_universal_masks':len(right_by_u),
  'left_same_U_dominated_existential_classes_discarded':left_discard,
  'right_same_U_dominated_existential_classes_discarded':right_discard,
  'complete_left_admissible_A_U_kernel_count':left_ceiling,
  'complete_right_admissible_A_U_kernel_count':right_ceiling,
  'complete_both_orientation_kernel_count':left_ceiling+right_ceiling,
  'descriptor_sample_requested_per_orientation':descriptor_sample,
  'left_retained_events_in_descriptor_sample':nDL,'right_retained_events_in_descriptor_sample':nDR,
  'left_distinct_E_plus_atomic_badmask_descriptors_in_sample':len(gL),
  'right_distinct_E_plus_atomic_badmask_descriptors_in_sample':len(gR),
  'left_distinct_descriptor_U_families_in_sample':len(pfL),'right_distinct_descriptor_U_families_in_sample':len(pfR),
  'largest_left_descriptor_multiplicity_in_sample':max(gL.values(),default=0),'largest_right_descriptor_multiplicity_in_sample':max(gR.values(),default=0),
  'legacy_prefix_requested':legacy_prefix,'legacy_prefix_aggregate':legacy_delta,
  'legacy_prefix_expected_aggregate':legacy_expected,'legacy_prefix_matches_banked_100_kernel_receipt':legacy_match,
  'stratified_sample_per_orientation_requested':sample_per_orientation,
  'stratified_left_distinct_kernels':len(stratL),'stratified_right_distinct_kernels':len(stratR),
  'stratified_aggregate':strat_delta,'first_atomic_badmask_escape_in_tested_samples':first_failure,
  'exact_badmask_pairs_computed':len(bad_cache),'conditional_partial_state_tests':partial_state_tests,
  'conditional_mdd_subset_tests':mdd_subset_tests,
  'eager_complete_A_by_atom_descriptor_query_count':2*nold*len(atoms),
  'uncached_reachable_fold_bad_call_ceiling':(left_ceiling+right_ceiling)*2*len(atoms),
  'aborted_complete_descriptor_feasibility_run':{'evidence_status':'operational observation, not receipt-recomputed','source_sha256':'e43ba1ae15bea60274115f68a214db603b2fb1b00ba45fed89679ae9f1088adc','wall_time_cap_seconds':720,'peak_observed_rss_bytes':1060368*1024,'receipt_emitted':False,'bottleneck':'eager complete retained-event by 91-atom restricted-root bad-mask descriptor census'},
  'feasibility_status':('prototype only; the eager complete descriptor table crossed the 12-minute/roughly-1GiB stop. Use lazy horn/transition inversion rather than launch the complete atlas in this representation.'),
  'atomic_batch_theorem':('For retained A and admissible U, the mixed core has a greatest old lower iff the old join of all atoms a with Bad_A(a) subset U has Bad_A(join) subset U. A first escaping atomic extension is an exact failure certificate.'),
  'quantifier_scope':'Complete admissible-U family counts in both orientations; exact legacy prefix, deterministic stratified kernel samples, and sampled descriptor deduplication only. The complete atomic atlas is not run.',
  'scope':'First-round lower kernels on the fixed adjacent two-copy factor only; no upper theorem except complement conjugacy, no later repair closure, lattice, OML, direct-limit, MBRC, ODBC, or Phi claim.',
  'verification_independence':'Single producer implementation; legacy aggregate is checked against fixed counts from the separately banked v3 scalar-core receipt.',
  'evidence_classes':['Hand proved','Executable verified'],
  'command':f'python3 notes/open_questions/verification/adjacent_full_cycle_badmask_atomic_batch.py --verify --sample-per-orientation {sample_per_orientation} --legacy-prefix {legacy_prefix} --descriptor-sample {descriptor_sample}'}
 out['producer_sha256']=hashlib.sha256(open(__file__,'rb').read()).hexdigest()
 out['payload_sha256']=hashlib.sha256(json.dumps(out,sort_keys=True,separators=(',',':')).encode()).hexdigest()
 return out,time.perf_counter()-start,phase_times

if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--emit',action='store_true');ap.add_argument('--verify',action='store_true')
 ap.add_argument('--sample-per-orientation',type=int,default=64);ap.add_argument('--legacy-prefix',type=int,default=100);ap.add_argument('--descriptor-sample',type=int,default=128);a=ap.parse_args()
 if a.sample_per_orientation<0 or a.legacy_prefix<0 or a.descriptor_sample<0:
  ap.error('all count arguments must be nonnegative')
 out,seconds,phase_times=payload(a.sample_per_orientation,a.legacy_prefix,a.descriptor_sample)
 path=os.path.join(HERE,'adjacent_full_cycle_badmask_atomic_batch.json')
 if a.emit:
  with open(path,'w') as f:json.dump(out,f,sort_keys=True,indent=2);f.write('\n')
 else:assert json.load(open(path))==out
 print(json.dumps({'status':'PASS','payload_sha256':out['payload_sha256'],'legacy_match':out['legacy_prefix_matches_banked_100_kernel_receipt'],'kernels_tested':out['legacy_prefix_aggregate'].get('kernels',0)+out['stratified_aggregate'].get('kernels',0),'failure':out['first_atomic_badmask_escape_in_tested_samples'],'phase_runtime_seconds':{k:round(v,6) for k,v in phase_times.items()},'runtime_seconds':round(seconds,3)},sort_keys=True))
