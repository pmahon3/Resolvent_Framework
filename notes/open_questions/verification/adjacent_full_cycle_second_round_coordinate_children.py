#!/usr/bin/env python3
"""Bounded exact-root second-round coordinate-kernel discriminator.

This producer deliberately works with the exact one-coordinate targets

  C_L(A,U) = A union cylinder(U)

that determine greatest old lower shadows of first-round adjacent mixed
events.  It does *not* identify these targets with the full two-copy mixed
events.  Consequently the AND/NEG/bridge calculations below audit the
coordinate shadow calculus only, not closure or latticehood of the adjacent
event family.

The retained-event sample is read from the committed join-rich receipt before
any target calculation.  For each of three endpoint-spread retained events in
each orientation, the two smallest nonempty admissible U masks are used.
Every old-kernel calculation exhausts the certified 91 old atoms.
"""
import argparse,collections,hashlib,json,os,struct,sys,time

HERE=os.path.dirname(os.path.abspath(__file__));sys.path.insert(0,HERE)
import full_cycle_adjacent_rectangle_intersection as inter

SCHEMA='adjacent-full-cycle-second-round-coordinate-children-v1'
JOIN_RICH=os.path.join(HERE,'adjacent_full_cycle_join_rich_per_a.json')
SAMPLE_A=3
MASKS_PER_A=2
CHILD_CAP=96

def payload():
 started=time.perf_counter()
 source=json.load(open(JOIN_RICH))
 source_payload=source['payload_sha256']
 selected={}
 for rec in source['orientation_records']:
  xs=[x['event_index'] for x in rec['per_a']]
  chosen=tuple(xs[(i*(len(xs)-1))//(SAMPLE_A-1)] for i in range(SAMPLE_A))
  selected[rec['orientation']]=chosen

 base,b=inter.capture_grammar()
 events=b['all_events'];macros=b['macros'];engines=b['engines'];states=b['states']
 roots={ev:r for r,ev in b['root_to_event'].items()};principal=b['principal']
 n=len(events);N=len(states);assert (n,N)==(18676,224)
 root_index={roots[e]:i for i,e in enumerate(events)}
 upmap={u:i for i,u in enumerate(principal)};assert len(upmap)==n
 allold=(1<<n)-1;zero=upmap[allold];nonatomic=0
 for d,u in enumerate(principal):
  if d!=zero:nonatomic|=u&~(1<<d)
 z=allold&~nonatomic&~(1<<zero);atoms=[]
 while z:
  bit=z&-z;atoms.append(bit.bit_length()-1);z-=bit
 assert len(atoms)==91

 occurrences=[[[] for _ in range(N)] for _ in range(4)]
 for m,(_,ds) in enumerate(macros):
  for pos in range(4):
   for i,s in enumerate(ds[pos]):occurrences[pos][s].append((m,i))
 status_cache={}
 def status(m,r,pos,i):
  k=(m,r,pos,i)
  if k in status_cache:return status_cache[k]
  if r<=1:q=r
  else:
   v,ch=engines[m].nodes[r]
   if v==pos:q=status(m,ch[i],pos,i)
   else:
    vals={status(m,x,pos,i) for x in ch};q=vals.pop() if len(vals)==1 else 2
  status_cache[k]=q;return q
 def classify(pos):
  out=[]
  for ev in events:
   E=U=0;rr=roots[ev]
   for s,occ in enumerate(occurrences[pos]):
    vals=[status(m,rr[m],pos,i) for m,i in occ]
    if any(vals):E|=1<<s
    if all(x==1 for x in vals):U|=1<<s
   out.append((E,U))
  return out
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
  return [tuple(sorted((U for U,xs in op.items()
    if any(not EA&E for E,_ in xs)),key=lambda u:(u.bit_count(),u)))
    for EA,_ in classes]
 left_us=admissible(left,minima(right));right_us=admissible(right,minima(left))

 def cyl(pos,mask):
  return tuple(engines[m].varset(pos,{s for s in ds[pos] if mask>>s&1})
    for m,(_,ds) in enumerate(macros))
 def op(kind,x,y):
  return tuple(engines[m].app(kind,a,c) for m,(a,c) in enumerate(zip(x,y)))
 def neg(x):return tuple(engines[m].neg(a) for m,a in enumerate(x))
 def subset(x,y):
  return all(not engines[m].app(0,a,engines[m].neg(c))
    for m,(a,c) in enumerate(zip(x,y)))
 def rhash(x):return hashlib.sha256(b''.join(struct.pack('<I',a) for a in x)).hexdigest()
 def old_join(x,y):return upmap[principal[x]&principal[y]]
 comp={i:root_index[neg(roots[e])] for i,e in enumerate(events)}
 def old_meet(x,y):return comp[old_join(comp[x],comp[y])]

 kernel_cache={}
 kernel_tests=0
 def kernel(target):
  nonlocal kernel_tests
  key=rhash(target)
  if key in kernel_cache:return kernel_cache[key]
  j=zero;eligible=[]
  for a in atoms:
   kernel_tests+=1
   if subset(roots[events[a]],target):
    eligible.append(a);j=old_join(j,a)
  good=subset(roots[events[j]],target)
  ans=(j,tuple(eligible),good);kernel_cache[key]=ans;return ans

 def coarse_shadow(target,pos):
  E=U=0
  for s,occ in enumerate(occurrences[pos]):
   vals=[status(m,target[m],pos,i) for m,i in occ]
   if any(vals):E|=1<<s
   if all(x==1 for x in vals):U|=1<<s
  return E,U

 records=[];first_failure=None;shadow_bridges=collections.defaultdict(dict)
 def old_record(i):
  p,f=events[i]
  return {'full17_hex':hex(f),'partial_root_tuple_sha256':rhash(p),
   'physical_root_tuple_sha256':rhash(roots[events[i]])}
 def child_record(x):
  return {'kind':x['kind'],'root_sha256':rhash(x['root']),'kernel':old_record(x['kernel']),
   'A':x.get('A'),'U_hex':None if 'U' not in x else hex(x['U']),
   'parents':x.get('parents'),'parent':x.get('parent')}
 for name,pos,classes,fams in (
   ('left_retained_position11',3,left,left_us),
   ('right_retained_position00',0,right,right_us)):
  leaves=[]
  for A in selected[name]:
   us=[u for u in fams[A] if u][:MASKS_PER_A]
   assert len(us)==MASKS_PER_A
   for U in us:
    target=op(1,roots[events[A]],cyl(pos,U))
    k,eligible,good=kernel(target)
    if not good and first_failure is None:
     first_failure={'phase':'leaf','orientation':name,'A':A,'U_hex':hex(U)}
    leaves.append({'kind':'Leaf','root':target,'kernel':k,'A':A,'U':U})
  leaves.sort(key=lambda x:rhash(x['root']))
  children={rhash(x['root']):x for x in leaves}
  and_tested=and_dedup=and_pass=0
  for i,x in enumerate(leaves):
   for y in leaves[i:]:
    and_tested+=1;t=op(0,x['root'],y['root']);h=rhash(t)
    k,eligible,good=kernel(t);expected=old_meet(x['kernel'],y['kernel'])
    ok=good and k==expected
    if ok:and_pass+=1
    elif first_failure is None:
     first_failure={'phase':'AND','orientation':name,'left':rhash(x['root']),
       'right':rhash(y['root']),'computed_kernel':k,'expected_meet':expected,'good':good}
    if h in children:continue
    and_dedup+=1
    children[h]={'kind':'And','root':t,'kernel':k,'parents':(rhash(x['root']),rhash(y['root']))}
    if len(children)>=CHILD_CAP:break
   if len(children)>=CHILD_CAP:break

  neg_tested=neg_good=0;first_missing_upper=None;union_candidates=dict(children)
  for h,x in sorted(children.items()):
   neg_tested+=1;t=neg(x['root']);k,eligible,good=kernel(t)
   if good:
    neg_good+=1
    union_candidates.setdefault(rhash(t),{'kind':'Neg','root':t,'kernel':k,'parent':h})
   elif first_missing_upper is None:
    first_missing_upper={'parent_root_sha256':h,'parent_kind':x['kind'],
      'complement_root_sha256':rhash(t),'maximal_lower_fold':old_record(k)}

  vals=[x for _,x in sorted(union_candidates.items())]
  disjoint=bridge_pass=0;bridge_hist=collections.Counter()
  for i,x in enumerate(vals):
   for y in vals[i+1:]:
    if op(0,x['root'],y['root'])!=tuple(0 for _ in macros):continue
    disjoint+=1;union=op(1,x['root'],y['root'])
    bridges=tuple(a for a in atoms if subset(roots[events[a]],union)
      and not subset(roots[events[a]],x['root'])
      and not subset(roots[events[a]],y['root']))
    bridge_records=tuple(sorted((old_record(a) for a in bridges),
      key=lambda r:(r['full17_hex'],r['physical_root_tuple_sha256'])))
    basej=old_join(x['kernel'],y['kernel']);j=basej;first_escape=None
    if not subset(roots[events[j]],union):
     first_escape={'stage':'base_kernel_join','prior':old_record(x['kernel']),
      'adjoined':old_record(y['kernel']),'escaping_join':old_record(j)}
    for a in bridges:
     oldj=j;j=old_join(j,a)
     if first_escape is None and not subset(roots[events[j]],union):
      first_escape={'stage':'bridge_atom','prior':old_record(oldj),
       'adjoined':old_record(a),'escaping_join':old_record(j)}
    fullk,_,good=kernel(union);ok=good and j==fullk and subset(roots[events[j]],union)
    bridge_pass+=ok;sig=hashlib.sha256(json.dumps(bridge_records,sort_keys=True,
      separators=(',',':')).encode()).hexdigest()
    bridge_hist[len(bridges)]+=1
    shadow=tuple(sorted((coarse_shadow(x['root'],pos),coarse_shadow(y['root'],pos))))
    shadow_bridges[(name,shadow)].setdefault(sig,
      {'left':rhash(x['root']),'right':rhash(y['root']),'bridge_count':len(bridges)})
    if not ok and first_failure is None:
     first_failure={'phase':'ORTHO_OR','orientation':name,
       'left_child':child_record(x),'right_child':child_record(y),
       'union_root_sha256':rhash(union),'bridge_atoms':list(bridge_records),
       'base_kernel_join':old_record(basej),'first_escaping_extension':first_escape,
       'fold':old_record(j),'full_atom_fold':old_record(fullk),
       'full_atom_fold_inside_union':good}
  records.append({'orientation':name,'selected_A':list(selected[name]),
    'leaf_count':len(leaves),'distinct_leaf_and_child_roots':len(children),
    'and_pairs_tested':and_tested,'new_and_roots':and_dedup,
    'and_kernel_meet_passes':and_pass,'neg_children_tested':neg_tested,
    'neg_children_with_greatest_old_lower':neg_good,
    'kernel_good_union_candidates_including_complements':len(union_candidates),
    'first_complement_without_greatest_old_lower':first_missing_upper,
    'exact_disjoint_child_pairs':disjoint,'bridge_union_fold_passes':bridge_pass,
    'bridge_count_histogram':dict(sorted(bridge_hist.items()))})

 ambiguity=[]
 for (name,shadow),sigs in shadow_bridges.items():
  if len(sigs)>1:
   ambiguity.append({'orientation':name,
    'shadow_sha256':hashlib.sha256(repr(shadow).encode()).hexdigest(),
    'distinct_bridge_signatures':len(sigs),
    'examples_by_signature':dict(sorted(sigs.items()))})
 out={'schema':SCHEMA,'schema_version':'1.0',
  'base_full_cycle_payload_sha256':base['payload_sha256'],
  'source_join_rich_payload_sha256':source_payload,
  'sample_rule':f'{SAMPLE_A} endpoint-spread retained A per orientation; {MASKS_PER_A} smallest nonempty admissible U per A',
  'old_atom_count':len(atoms),'child_cap_per_orientation':CHILD_CAP,
  'orientation_records':records,'old_atom_target_subset_tests':kernel_tests,
  'first_kernel_or_transition_failure':first_failure,
  'equal_coarse_shadow_pairs_with_different_bridge_signatures':ambiguity,
  'scope':('Bounded exact reduced-MDD coordinate-target calculus only. Leaves are the exact '
   'one-coordinate cores A union cylinder(U) controlling old shadows of adjacent mixed '
   'events; they are not the full two-copy events. No exhaustive first-round, full mixed '
   'closure, lattice, OML, direct-limit, MBRC, ODBC, or Phi claim.'),
  'verification_independence':('Single producer using the certified full-cycle MDD grammar; '
   'sample indices only are imported from the committed join-rich receipt. No shard artifact is read.'),
  'determinism_scope':('On this final source, PYTHONHASHSEED=0 emit and verify and '
   'PYTHONHASHSEED=12345 whole-payload replay all pass. Earlier replay failures were '
   'source-version skew and in-memory tuple/integer-key versus JSON list/string-key type skew, '
   'not differing mathematical payloads.'),
  'evidence_classes':['Executable verified bounded evidence'],
  'command':'PYTHONHASHSEED=0 python3 notes/open_questions/verification/adjacent_full_cycle_second_round_coordinate_children.py --verify'}
 out['producer_sha256']=hashlib.sha256(open(__file__,'rb').read()).hexdigest()
 out['payload_sha256']=hashlib.sha256(json.dumps(out,sort_keys=True,separators=(',',':')).encode()).hexdigest()
 return out,time.perf_counter()-started

if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--emit',action='store_true');ap.add_argument('--verify',action='store_true')
 ap.add_argument('--diagnose',action='store_true');a=ap.parse_args()
 out,seconds=payload();path=os.path.join(HERE,'adjacent_full_cycle_second_round_coordinate_children.json')
 if a.emit:
  with open(path,'w') as f:json.dump(out,f,sort_keys=True,indent=2);f.write('\n')
 elif a.diagnose:
  old=json.load(open(path))
  print(json.dumps({k:{'old':old.get(k),'new':out.get(k)} for k in sorted(set(old)|set(out))
    if old.get(k)!=out.get(k)},sort_keys=True,indent=2))
 else:assert json.load(open(path))==json.loads(json.dumps(out,sort_keys=True))
 print(json.dumps({'status':'PASS','payload_sha256':out['payload_sha256'],
  'first_failure':out['first_kernel_or_transition_failure'],
  'runtime_seconds':round(seconds,3)},sort_keys=True))
