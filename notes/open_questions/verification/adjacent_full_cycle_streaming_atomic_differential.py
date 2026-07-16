#!/usr/bin/env python3
"""Bounded differential audit of streaming adjacent-kernel atomic folds.

This is deliberately not the complete 55,722-kernel scan.  In each
orientation it selects the first 64 retained events with a live admissible
universal mask and 64 deterministically spread retained events, then checks
*every* admissible universal mask for those retained events twice:

* simultaneously, grouping masks by their current old-lattice accumulator;
* independently at the transition level, one scalar kernel at a time.

Conditional MDD containment is read-only.  It neither constructs residual
nodes nor calls MDD.node/app/neg, so query caches can be evicted after each A.
"""
import argparse,collections,functools,hashlib,json,os,sys,time

HERE=os.path.dirname(os.path.abspath(__file__));sys.path.insert(0,HERE)
import full_cycle_adjacent_rectangle_intersection as inter

SCHEMA='adjacent-full-cycle-streaming-atomic-differential-v1'
LIMIT_SECONDS=720

def payload(prefix=64,spread=64):
 start=time.perf_counter();base,b=inter.capture_grammar()
 events=b['all_events'];macros=b['macros'];engines=b['engines'];states=b['states']
 roots={ev:r for r,ev in b['root_to_event'].items()};principal=b['principal']
 nold=len(events);N=len(states);assert nold==18676 and N==224
 upmap={u:i for i,u in enumerate(principal)};assert len(upmap)==nold
 allold=(1<<nold)-1;zero=upmap[allold];nonatomic=0
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

 # Read-only section status under one assigned coordinate: 0 empty, 1 full,
 # 2 genuinely partial in the remaining coordinates.
 status_cache={};status_calls=status_hits=0
 def section_status(m,root,pos,i):
  nonlocal status_calls,status_hits
  key=(m,root,pos,i)
  if key in status_cache:status_hits+=1;return status_cache[key]
  status_calls+=1
  if root<=1:z=root
  else:
   v,ch=engines[m].nodes[root]
   if v==pos:z=section_status(m,ch[i],pos,i)
   else:
    vals={section_status(m,x,pos,i) for x in ch}
    z=vals.pop() if len(vals)==1 else 2
  status_cache[key]=z;return z

 def classify(pos):
  ans=[]
  for ev in events:
   if time.perf_counter()-start>LIMIT_SECONDS:raise TimeoutError('classification exceeded 12-minute cap')
   E=U=0;rr=roots[ev]
   for s,occ in enumerate(occurrences[pos]):
    vals=[section_status(m,rr[m],pos,i) for m,i in occ]
    if any(vals):E|=1<<s
    if all(x==1 for x in vals):U|=1<<s
   ans.append((E,U))
  return ans
 left=classify(3);right=classify(0)

 def minimal_existentials(classes):
  groups=collections.defaultdict(list)
  for i,(E,U) in enumerate(classes):groups[U].append((E,i))
  out={}
  for U,xs in groups.items():
   keep=[]
   for E,i in sorted(xs,key=lambda x:(x[0].bit_count(),x[0],x[1])):
    if not any(not K&~E for K,_ in keep):keep.append((E,i))
   out[U]=tuple(keep)
  return out
 left_by_u=minimal_existentials(left);right_by_u=minimal_existentials(right)

 # Preserve a canonical opposite event witness for every live (A,U), so a
 # failure receipt certifies physical admissibility rather than only a mask.
 def admissible(classes,op_by_u):
  fam=[];witness=[]
  for A,(EA,_) in enumerate(classes):
   ws={}
   for U,xs in op_by_u.items():
    cand=[(i,E) for E,i in xs if not EA&E]
    if cand:ws[U]=min(cand)
   us=tuple(sorted(ws,key=lambda u:(u.bit_count(),u)))
   fam.append(us);witness.append(ws)
  return fam,witness,sum(map(len,fam))
 left_us,left_w,left_total=admissible(left,right_by_u)
 right_us,right_w,right_total=admissible(right,left_by_u)
 assert (left_total,right_total)==(28023,27699)

 def selected(fams):
  active=[i for i,us in enumerate(fams) if us]
  pre=active[:prefix]
  spr=[]
  if spread==1:spr=[active[len(active)//2]]
  elif spread>1:spr=[active[(t*(len(active)-1))//(spread-1)] for t in range(spread)]
  return tuple(sorted(set(pre+spr))),len(pre),len(set(spr)),len(set(pre)&set(spr))

 read_subset_calls=read_subset_nodes=read_subset_memo_hits=0
 def assigned_subset(m,x,y,pos,i):
  """Whether x|pos=i is contained in y|pos=i, without MDD mutation."""
  nonlocal read_subset_calls,read_subset_nodes,read_subset_memo_hits
  read_subset_calls+=1;memo={}
  def go(a,c):
   nonlocal read_subset_nodes,read_subset_memo_hits
   if not a or c==1 or a==c:return True
   k=(a,c)
   if k in memo:read_subset_memo_hits+=1;return memo[k]
   read_subset_nodes+=1
   # A terminal/nonterminal disagreement cannot be decided until a possible
   # occurrence of the assigned variable has been eliminated.  Treat a
   # terminal as having variable +infinity and recurse through the other DAG.
   if a<=1 and c<=1:return bool((not a) or c)
   va,ca=engines[m].nodes[a] if a>1 else (10**9,None)
   vc,cc=engines[m].nodes[c] if c>1 else (10**9,None);v=min(va,vc)
   if v==pos:
    aa=ca[i] if va==v else a;cy=cc[i] if vc==v else c
    z=go(aa,cy)
   else:
    aa=ca if va==v else (a,)*len(engines[m].domains[v])
    cy=cc if vc==v else (c,)*len(engines[m].domains[v])
    z=all(go(p,q) for p,q in zip(aa,cy))
   memo[k]=z;return z
  return go(x,y)

 # Regression oracle: compare the read-only recursion against the prior exact
 # residual construction plus intersection test on bounded deterministic root
 # pairs.  These reference calls may mutate MDD caches, so the no-mutation
 # baseline is taken only after this regression finishes.
 @functools.lru_cache(None)
 def mut_restrict(m,root,pos,i):
  if root<=1:return root
  v,ch=engines[m].nodes[root]
  if v==pos:return ch[i]
  return engines[m].node(v,[mut_restrict(m,z,pos,i) for z in ch])
 regression=[]
 probe_events=tuple(dict.fromkeys(([0,1,nold-1]+atoms[::7]+list(range(0,nold,max(1,nold//19))))))[:32]
 for pos in (3,0):
  for t in range(64):
   D=probe_events[t%len(probe_events)];A=probe_events[(t*11+5)%len(probe_events)]
   s=(t*37+13)%N;m,i=occurrences[pos][s][t%len(occurrences[pos][s])]
   x=mut_restrict(m,roots[events[D]][m],pos,i);y=mut_restrict(m,roots[events[A]][m],pos,i)
   ref=not engines[m].app(0,x,engines[m].neg(y));got=assigned_subset(m,roots[events[D]][m],roots[events[A]][m],pos,i)
   assert got==ref,(pos,t,m,i,D,A,got,ref);regression.append((pos,m,i,D,A,int(got)))
 # Target the exact former bug: a terminal on one side while the other root
 # selects to the same terminal at `pos`.
 targeted=[]
 for pos in (3,0):
  full_case=empty_case=None
  for D in range(nold):
   if full_case is not None and empty_case is not None:break
   rr=roots[events[D]]
   for s,occ in enumerate(occurrences[pos]):
    if full_case is not None and empty_case is not None:break
    for m,i in occ:
     if rr[m]<=1:continue
     residual=mut_restrict(m,rr[m],pos,i)
     if residual==1 and full_case is None:
      assert assigned_subset(m,1,rr[m],pos,i)
      full_case=('terminal_one_vs_selected_full',pos,m,i,D,s)
     if residual==0 and empty_case is None:
      assert assigned_subset(m,rr[m],0,pos,i)
      empty_case=('selected_empty_vs_terminal_zero',pos,m,i,D,s)
  assert full_case is not None and empty_case is not None,(pos,full_case,empty_case)
  targeted.extend((full_case,empty_case))
 regression.extend(targeted)
 regression_digest=hashlib.sha256(repr(regression).encode()).hexdigest()
 mutation_baseline=(sum(len(e.nodes) for e in engines),sum(len(e.acache) for e in engines),sum(len(e.ncache) for e in engines))

 def maskhex(x):return hex(x)
 def maskhash(x):return hashlib.sha256(x.to_bytes(28,'little')).hexdigest()
 def eventhash(i):
  p,f=events[i];raw=','.join(map(str,p)).encode()+b'|'+str(f).encode()
  return hashlib.sha256(raw).hexdigest()

 summaries=[];all_failures=[];global_peaks=collections.Counter()
 def orientation(name,pos,classes,op_classes,fams,witness):
  chosen,np,ns,no=selected(fams);kernel_count=sum(len(fams[A]) for A in chosen)
  result_digest=hashlib.sha256();transition_digest=hashlib.sha256()
  orient_fail=[];total_transitions=total_bad=0;peak_bad=peak_groups=peak_q=0
  for ordinal,A in enumerate(chosen):
   if time.perf_counter()-start>LIMIT_SECONDS:
    raise TimeoutError('bounded differential audit exceeded 12-minute cap')
   us=fams[A];uindex={u:i for i,u in enumerate(us)};full=(1<<len(us))-1
   bad_cache={}
   def bad(D):
    nonlocal total_bad,peak_bad
    if D in bad_cache:return bad_cache[D]
    EA,UA=classes[A];ED,_=classes[D];cand=ED&~UA;ans=0
    dr=roots[events[D]];ar=roots[events[A]]
    while cand:
     bit=cand&-cand;s=bit.bit_length()-1;cand-=bit
     if any(not assigned_subset(m,dr[m],ar[m],pos,i) for m,i in occurrences[pos][s]):ans|=bit
    bad_cache[D]=ans;total_bad+=1;peak_bad=max(peak_bad,len(bad_cache));return ans
   atom_bad={a:bad(a) for a in atoms}

   # Grouped transition machine.
   groups={A:full};gresult=[None]*len(us);gfail=[None]*len(us)
   for ao,a in enumerate(atoms):
    if time.perf_counter()-start>LIMIT_SECONDS:raise TimeoutError('grouped scan exceeded 12-minute cap')
    qcache={};nxt=collections.defaultdict(int)
    ba=atom_bad[a]
    for P,ubits in sorted(groups.items()):
     eligible=0
     z=ubits
     while z:
      bit=z&-z;ui=bit.bit_length()-1;z-=bit
      if not ba&~us[ui]:eligible|=bit
     stay=ubits&~eligible
     if stay:nxt[P]|=stay
     if not eligible:continue
     if principal[a]>>P&1:nxt[P]|=eligible;continue
     J=upmap[principal[P]&principal[a]]
     if J not in qcache:qcache[J]=bad(J)
     Q=qcache[J];total_transitions+=1
     transition_digest.update(f'{name},{A},{ao},{P},{a},{J},{Q:x}\n'.encode())
     passbits=0;z=eligible
     while z:
      bit=z&-z;ui=bit.bit_length()-1;z-=bit;U=us[ui]
      if Q&~U:gfail[ui]=(ao,P,a,J,Q,Q&~U)
      else:passbits|=bit
     if passbits:nxt[J]|=passbits
    groups=dict(nxt);peak_groups=max(peak_groups,len(groups));peak_q=max(peak_q,len(qcache))
   for P,bits in groups.items():
    while bits:
     bit=bits&-bits;ui=bit.bit_length()-1;bits-=bit;gresult[ui]=P

   # Independent scalar state transition (shared exact bad-mask oracle only).
   for ui,U in enumerate(us):
    if time.perf_counter()-start>LIMIT_SECONDS:raise TimeoutError('scalar replay exceeded 12-minute cap')
    P=A;sf=None
    for ao,a in enumerate(atoms):
     ba=atom_bad[a]
     if ba&~U or principal[a]>>P&1:continue
     J=upmap[principal[P]&principal[a]];Q=bad(J)
     if Q&~U:sf=(ao,P,a,J,Q,Q&~U);break
     P=J
    sr=None if sf else P
    assert (sf,sr)==(gfail[ui],gresult[ui]),(name,A,ui,sf,sr,gfail[ui],gresult[ui])
    verdict=('F',)+sf if sf else ('P',sr)
    result_digest.update(f'{name},{A},{U:x},{verdict}\n'.encode())
    if sf:
     ao,prior,a,J,Q,escape=sf;opp_i,opp_E=witness[A][U]
     assert not classes[A][0]&opp_E
     assert op_classes[opp_i]==(opp_E,U)
     assert not bad(prior)&~U and not atom_bad[a]&~U and Q&~U
     assert not (principal[a]>>prior&1)
     assert J==upmap[principal[prior]&principal[a]]
     rec={'orientation':name,'retained_event_index':A,'retained_event_sha256':eventhash(A),
      'opposite_witness_event_index':opp_i,'opposite_witness_event_sha256':eventhash(opp_i),
      'retained_existential_mask_hex':maskhex(classes[A][0]),
      'opposite_existential_mask_hex':maskhex(opp_E),'universal_mask_hex':maskhex(U),
      'universal_mask_sha256':maskhash(U),'atom_ordinal':ao,'prior_accumulator_event_index':prior,
      'new_atom_event_index':a,'escaping_join_event_index':J,'prior_bad_mask_hex':maskhex(bad(prior)),
      'atom_bad_mask_hex':maskhex(atom_bad[a]),'required_union_mask_hex':maskhex(bad(prior)|atom_bad[a]),
      'escaping_bad_mask_hex':maskhex(Q),'escaping_outside_U_hex':maskhex(escape),
      'escaping_state_indices':[s for s in range(N) if escape>>s&1]}
     orient_fail.append(rec);all_failures.append(rec)
  summaries.append({'orientation':name,'selected_retained_events':len(chosen),
    'prefix_selected_before_dedup':np,'spread_selected_distinct':ns,'prefix_spread_overlap':no,
    'selected_event_indices_sha256':hashlib.sha256(','.join(map(str,chosen)).encode()).hexdigest(),
    'all_admissible_kernels_for_selected_events':kernel_count,'failures':len(orient_fail),
    'bad_masks_computed':total_bad,'group_join_transition_attempts':total_transitions,
    'peak_per_A_bad_mask_cache_entries':peak_bad,'peak_group_count':peak_groups,
    'peak_per_atom_join_bad_cache_entries':peak_q,
    'scalar_grouped_verdict_digest_sha256':result_digest.hexdigest(),
    'grouped_transition_digest_sha256':transition_digest.hexdigest()})
  global_peaks.update({'selected_A':len(chosen),'kernels':kernel_count,'failures':len(orient_fail)})

 orientation('left_retained_position11',3,left,right,left_us,left_w)
 orientation('right_retained_position00',0,right,left,right_us,right_w)
 mutation_final=(sum(len(e.nodes) for e in engines),sum(len(e.acache) for e in engines),sum(len(e.ncache) for e in engines))
 assert mutation_final==mutation_baseline,(mutation_baseline,mutation_final)
 out={'schema':SCHEMA,'schema_version':'1.0','base_full_cycle_payload_sha256':base['payload_sha256'],
  'completed_events_each':nold,'shared_states':N,'old_atom_count':len(atoms),
  'atom_order_event_indices':atoms,'atom_order_sha256':hashlib.sha256(','.join(map(str,atoms)).encode()).hexdigest(),
  'complete_live_kernel_counts':{'left':left_total,'right':right_total,'both':left_total+right_total},
  'selection_parameters':{'prefix':prefix,'spread':spread},'orientation_summaries':summaries,
  'tested_kernel_count':global_peaks['kernels'],'failure_count':len(all_failures),
  'first_failure':all_failures[0] if all_failures else None,
  'read_only_query_counters':{'section_status_cache_entries':len(status_cache),'section_status_calls':status_calls,
   'section_status_cache_hits':status_hits,'assigned_subset_calls':read_subset_calls,
   'assigned_subset_recursive_nodes':read_subset_nodes,'assigned_subset_memo_hits':read_subset_memo_hits},
  'bounded_reference_regression':{'cases':len(regression),'digest_sha256':regression_digest,
   'targeted_former_terminal_shortcut_cases':len(targeted),
   'method':'mutating residual restriction plus exact MDD intersection, including explicit terminal-versus-selected-full/empty cases, run before the mutation baseline'},
  'mdd_cache_snapshot_after_reference_regression':mutation_baseline,
  'mdd_cache_snapshot_after_streaming_scan':mutation_final,
  'differential_verification':('Every selected (A,U) was processed by both the simultaneous-U grouped transition machine and an independent scalar transition loop; exact first failure or terminal accumulator agreed.'),
  'mdd_mutation_discipline':('The bounded reference regression may mutate MDD caches before the recorded baseline. Section status and assigned containment recurse read-only; the measured streaming scan never calls engine.node, engine.app, or engine.neg, and its final MDD snapshot must equal that baseline.'),
  'deadline_discipline':('Cooperative 12-minute checks occur during classification and between retained-event, atom, and scalar-kernel loop units; capture_grammar and one indivisible recursive query cannot be preempted internally.'),
  'quantifier_scope':('All admissible U masks for the union of the first prefix and deterministically spread retained-A samples in both orientations. This is bounded differential algorithm evidence, not the complete 55722-kernel theorem.'),
  'theorem_scope':('First-round lower kernels on the fixed adjacent two-copy factor only. A failure is an exact atomic join-horn certificate. Passing does not prove later mixed closure, latticehood, NF, MBRC, ODBC, or Phi.'),
  'verification_independence':('Grouped and scalar transition implementations are distinct but share capture_grammar, exact classification, admissibility construction, and the read-only bad-mask oracle. No independent producer.'),
  'evidence_classes':['Executable verified'],
  'command':f'python3 notes/open_questions/verification/adjacent_full_cycle_streaming_atomic_differential.py --verify --prefix {prefix} --spread {spread}'}
 out['producer_sha256']=hashlib.sha256(open(__file__,'rb').read()).hexdigest()
 out['payload_sha256']=hashlib.sha256(json.dumps(out,sort_keys=True,separators=(',',':')).encode()).hexdigest()
 return out,time.perf_counter()-start

if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--emit',action='store_true');ap.add_argument('--verify',action='store_true')
 ap.add_argument('--prefix',type=int,default=64);ap.add_argument('--spread',type=int,default=64);a=ap.parse_args()
 if a.prefix<0 or a.spread<0:ap.error('sample sizes must be nonnegative')
 out,seconds=payload(a.prefix,a.spread);path=os.path.join(HERE,'adjacent_full_cycle_streaming_atomic_differential.json')
 if a.emit:
  with open(path,'w') as f:json.dump(out,f,sort_keys=True,indent=2);f.write('\n')
 else:assert json.load(open(path))==out
 print(json.dumps({'status':'PASS','payload_sha256':out['payload_sha256'],'tested_kernels':out['tested_kernel_count'],'failures':out['failure_count'],'runtime_seconds':round(seconds,3)},sort_keys=True))
