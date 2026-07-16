#!/usr/bin/env python3
"""Exact first-round old-cylinder lower-kernel scan for adjacent full cycles.

For z=A_L disjoint-union B_R, physical disjointness is E_A cap E_B=empty.
The greatest possible left-coordinate cylinder contained in z has section
  A_s when B_s is not full, and X_s when B_s is full,
so its exact root is A union cylinder(U_B).  This script retains every actual
partial root of A and quotients only the opposite event by its (E_B,U_B)
class.  For fixed U_B, only inclusion-minimal E_B masks are retained: physical
admissibility is the existential condition E_A cap E_B=empty, and a larger
E_B with the same U_B never admits a pair that a contained E_B does not.

For a core C, let L(C) be the old events below C.  The old family is a
certified finite OML, hence atomistic: if the join y of all atoms below x were
strictly below x, orthomodularity would make x meet y-complement nonzero; a
minimal nonzero element below that residual would be an atom below x but not
below y, a contradiction.  Therefore the join of L(C) is exactly the join of
the old atoms contained in C.  The scan tests only those atoms.  C has a
greatest old lower bound iff their old join J(C) is still below C, in which
case J(C) is that bound.  Joins are folded using the certified identity

  Up(x join y) = Up(x) cap Up(y).

It starts at retained A, which already contains every old atom below A.  Atoms
already below the accumulator are skipped by one principal-upset bit test.  If
another contained atom D makes the join escape C, the pair (accumulator,D)
certifies nonexistence: any greatest lower would have to contain their old
join.  If the fold finishes, its final old event remains below C and contains
every old atom below C, hence dominates every old lower by atomisticity.  This replaces
the former disk-backed exact-root table and maximal-lower enumeration.  It
does not use root digests for equality.  Duplicate symbolic kernels may be
retested without weakening the universal quantifier.  The right direction is
symmetric, and the scan stops at the first cumulative-join escape.

No further quotient comes from replacing U by U union U_A: admissibility gives
U subset E_B, U_A subset E_A, and E_A cap E_B=empty, hence U cap U_A=empty;
the replacement is injective on the admissible U masks (although the two cores
are of course equal after adjoining the already-full U_A fibres).

Default mode is unbounded.  --max-kernels N is diagnostic only; a bounded stop
is explicitly nonexhaustive and cannot support the positive theorem.
"""
import argparse,hashlib,json,os,struct,sys,time

HERE=os.path.dirname(os.path.abspath(__file__));sys.path.insert(0,HERE)
import full_cycle_adjacent_rectangle_intersection as inter

SCHEMA='adjacent-full-cycle-exact-lower-kernel-scan-v3'

def payload(max_kernels=0):
 start=time.perf_counter();base,b=inter.capture_grammar()
 events=b['all_events'];macros=b['macros'];engines=b['engines'];states=b['states'];N=len(states)
 roots={ev:r for r,ev in b['root_to_event'].items()};root_index={roots[ev]:i for i,ev in enumerate(events)}
 principal=b['principal'];assert len(events)==len(principal)==len(root_index)==18676
 upmap={u:i for i,u in enumerate(principal)};assert len(upmap)==len(events)
 allold=(1<<len(events))-1;zero=upmap[allold]
 # An element is non-atomic exactly when it has a nonzero strict lower.  Mark
 # all strict uppers of every nonzero d by OR-ing its certified principal
 # upset; the remaining nonzero indices are precisely the atoms.
 nonatomic=0
 for d,u in enumerate(principal):
  if d!=zero:nonatomic|=u&~(1<<d)
 atom_mask=allold&~nonatomic&~(1<<zero)
 atoms=[];z=atom_mask
 while z:
  bit=z&-z;atoms.append(bit.bit_length()-1);z-=bit
 assert atoms and all(sum(1 for d,u in enumerate(principal) if u>>a&1)==2 for a in atoms)

 def shadows(pos):
  cache={}
  def cls(m,root,i):
   key=(m,root,i)
   if key in cache:return cache[key]
   if root<=1:z=root
   else:
    v,ch=engines[m].nodes[root]
    if v==pos:z=cls(m,ch[i],i)
    else:
     vals={cls(m,x,i) for x in ch};z=vals.pop() if len(vals)==1 else 2
   cache[key]=z;return z
  ans=[]
  for ev in events:
   E=[False]*N;U=[True]*N;seen=[False]*N
   for m,(_,ds) in enumerate(macros):
    root=roots[ev][m]
    for i,s in enumerate(ds[pos]):
     z=cls(m,root,i);seen[s]=True;E[s]|=z!=0;U[s]&=z==1
   assert all(seen)
   e=sum(1<<s for s,v in enumerate(E) if v);u=sum(1<<s for s,v in enumerate(U) if v);assert not u&~e
   ans.append((e,u))
  return ans,len(cache)
 left,cacheL=shadows(3);right,cacheR=shadows(0)
 leftclasses={x:i for i,x in enumerate(left)};rightclasses={x:i for i,x in enumerate(right)}
 def minimal_existentials(classes):
  """Exact same-U admissibility quotient by inclusion-minimal E masks."""
  groups={}
  for (E,U),i in classes.items():groups.setdefault(U,[]).append((E,i))
  ans={};discarded=0
  for U,xs in groups.items():
   keep=[]
   for E,i in sorted(xs,key=lambda z:(z[0].bit_count(),z[0],z[1])):
    if any((K&~E)==0 for K,_ in keep):discarded+=1;continue
    keep.append((E,i))
   ans[U]=tuple(keep)
  return ans,discarded
 left_by_u,left_dominated=minimal_existentials(leftclasses)
 right_by_u,right_dominated=minimal_existentials(rightclasses)
 cylcache={}
 def cylinder(pos,mask):
  key=(pos,mask)
  if key not in cylcache:cylcache[key]=tuple(engines[m].varset(pos,{s for s in ds[pos] if mask>>s&1}) for m,(_,ds) in enumerate(macros))
  return cylcache[key]
 def gor(x,y):return tuple(engines[m].app(1,x[m],y[m]) for m in range(len(macros)))
 def rle(x,y):
  # Macrofibres are disjoint, so componentwise MDD inclusion is exact.
  for m,(a,c) in enumerate(zip(x,y)):
   if engines[m].app(0,a,engines[m].neg(c)):return False
  return True
 def rhash(x):return hashlib.sha256(b''.join(struct.pack('<I',z) for z in x)).hexdigest()
 def mhash(x):return hashlib.sha256(x.to_bytes(28,'little')).hexdigest()
 def erec(i):
  p,f=events[i];return {'event_index':i,'full17_hex':hex(f),'partial_root_tuple_sha256':rhash(p),'physical_root_tuple_sha256':rhash(roots[events[i]])}

 fold_order=atoms
 pairs=0;realized=0;absent=0;subset_tests=0;join_folds=0;failure=None;bounded=False
 absent_with_unique_greatest=0;maximum_fold_length=0
 def inspect(direction,retained_i,opposite_i,retained_shadow,opposite_shadow,pos):
  nonlocal pairs,realized,absent,subset_tests,join_folds,failure,bounded,absent_with_unique_greatest,maximum_fold_length
  if max_kernels and pairs>=max_kernels:bounded=True;return
  pairs+=1;core=gor(roots[events[retained_i]],cylinder(pos,opposite_shadow[1]))
  if core in root_index:
   realized+=1;return
  absent+=1;j=retained_i;folds=0
  for d in fold_order:
   # Atom d <= j iff the old principal upset of d contains j.
   if principal[d]>>j&1:continue
   subset_tests+=1
   if not rle(roots[events[d]],core):continue
   oldj=j;j=upmap[principal[j]&principal[d]];join_folds+=1;folds+=1
   if not rle(roots[events[j]],core):
    failure={'direction':direction,'retained_event_record':erec(retained_i),'opposite_class_representative_event_record':erec(opposite_i),
     'retained_E_sha256':mhash(retained_shadow[0]),'retained_U_sha256':mhash(retained_shadow[1]),
     'opposite_E_sha256':mhash(opposite_shadow[0]),'opposite_U_sha256':mhash(opposite_shadow[1]),
     'opposite_universal_state_count':opposite_shadow[1].bit_count(),'core_root_tuple_sha256':rhash(core),
     'prior_accumulated_old_lower_record':erec(oldj),'new_contained_old_atom_record':erec(d),'escaping_old_join_record':erec(j),
     'prior_accumulator_subset_core':rle(roots[events[oldj]],core),'new_lower_subset_core':rle(roots[events[d]],core),
     'escaping_join_subset_core':False,'principal_upset_intersection_is_join':principal[oldj]&principal[d]==principal[j],
     'folds_before_escape':folds}
    maximum_fold_length=max(maximum_fold_length,folds);return
  maximum_fold_length=max(maximum_fold_length,folds);absent_with_unique_greatest+=1

 # Deterministic left scan: retain every local-position-11 descriptor; quotient
 # the opposite position-00 copy only by distinct (E,U), then deduplicate U.
 for ai,A in enumerate(left):
  choices=[]
  for U,xs in right_by_u.items():
   eligible=next(((E,bi) for E,bi in xs if not A[0]&E),None)
   if eligible is not None:choices.append((U,(eligible[0],U),eligible[1]))
  for _,B,bi in sorted(choices):
   inspect('left_old_copy',ai,bi,A,B,3)
   if failure or bounded:break
  if failure or bounded:break
 if not failure and not bounded:
  for bi,B in enumerate(right):
   choices=[]
   for U,xs in left_by_u.items():
    eligible=next(((E,ai) for E,ai in xs if not B[0]&E),None)
    if eligible is not None:choices.append((U,(eligible[0],U),eligible[1]))
   for _,A,ai in sorted(choices):
    inspect('right_old_copy',bi,ai,B,A,0)
    if failure or bounded:break
   if failure or bounded:break
 completed=not failure and not bounded
 out={'schema':SCHEMA,'schema_version':'3.0','base_full_cycle_payload_sha256':base['payload_sha256'],'completed_events_each':len(events),'shared_states':N,
  'old_zero_event_index':zero,'old_atom_count':len(atoms),
  'old_atom_indices_sha256':hashlib.sha256(b''.join(struct.pack('<I',a) for a in atoms)).hexdigest(),
  'left_distinct_EU_classes':len(leftclasses),'right_distinct_EU_classes':len(rightclasses),'left_classification_cache_entries':cacheL,'right_classification_cache_entries':cacheR,
  'left_distinct_universal_masks':len(left_by_u),'right_distinct_universal_masks':len(right_by_u),
  'left_same_U_dominated_existential_classes_discarded':left_dominated,'right_same_U_dominated_existential_classes_discarded':right_dominated,
  'max_kernels':max_kernels,'bounded_stop':bounded,'scan_completed_exhaustively':completed,'stopped_at_first_failure':failure is not None,
  'symbolic_retained_event_by_admissible_opposite_universal_kernels_visited':pairs,
  'cores_already_old_events':realized,'absent_exact_cores':absent,'absent_cores_with_unique_greatest_old_lower':absent_with_unique_greatest,
  'exact_old_atom_subset_tests':subset_tests,'old_lattice_join_folds':join_folds,'maximum_join_fold_length_seen':maximum_fold_length,
  'first_cumulative_join_escape':failure,
  'quantifiers':('Every actual retained descriptor in each orientation; every opposite universal mask U for which some realized same-U existential mask E is physically disjoint. Inclusion-nonminimal same-U E masks are discarded by the proved existential-admissibility quotient. Duplicate exact cores across different symbolic kernels may be retested; no root digest is used for deduplication.'),
  'universal_mask_normalization':('U -> U union U_A gives the same core, but is not a quotient on admissible kernels: U subset E_B and U_A subset E_A with E_A intersection E_B empty, so U and U_A are disjoint and adjoining fixed U_A is injective.'),
  'finite_OML_atomisticity_theorem':('Every finite OML is atomistic. If the join y of all atoms below x were below x strictly, orthomodularity makes x meet y-complement nonzero; a minimal nonzero element below that residual is an atom below x but not below y, contradiction.'),
  'join_fold_decision_theorem':('For core C, atomisticity identifies the join of all old events below C with the join of all old atoms contained in C. This join is below C iff C has a greatest old lower, and is then that greatest lower. Each escaping fold serializes an accumulated old lower and a contained old atom whose certified old join is not below C, an exact nonexistence certificate.'),
  'positive_theorem_status':('exhaustive: every first-round exact left/right coordinate lower core has a unique greatest old local lower bound' if completed else 'not established: bounded diagnostic stop' if bounded else 'refuted by the serialized first failing core'),
  'scope':'Exact first-round lower-kernel scan only. No upper-envelope theorem, no mixed closure, no preservation after later repairs, and no lattice/OML/direct-limit claim.',
  'runtime_reporting':'Wall-clock time is printed but excluded from the deterministic payload. Counts above are deterministic complexity receipts.',
  'evidence_classes':['Hand proved','Executable verified'],
  'verification_independence':'Producer replay only; no independent verifier for this scanner.',
  'command':('python3 notes/open_questions/verification/adjacent_full_cycle_exact_lower_kernel_scan.py --verify'+(' --max-kernels '+str(max_kernels) if max_kernels else ''))}
 out['producer_sha256']=hashlib.sha256(open(__file__,'rb').read()).hexdigest();out['payload_sha256']=hashlib.sha256(json.dumps(out,sort_keys=True,separators=(',',':')).encode()).hexdigest()
 return out,time.perf_counter()-start

if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--emit',action='store_true');ap.add_argument('--verify',action='store_true');ap.add_argument('--max-kernels',type=int,default=0);a=ap.parse_args();out,seconds=payload(a.max_kernels)
 suffix=('_bounded_kernels_'+str(a.max_kernels) if a.max_kernels else '')
 path=os.path.join(HERE,'adjacent_full_cycle_exact_lower_kernel_scan'+suffix+'.json')
 if a.emit:
  with open(path,'w') as f:json.dump(out,f,sort_keys=True,indent=2);f.write('\n')
 else:assert json.load(open(path))==out
 print(json.dumps({'status':'PASS','payload_sha256':out['payload_sha256'],'exhaustive':out['scan_completed_exhaustively'],'failure':out['first_cumulative_join_escape'],'kernels':out['symbolic_retained_event_by_admissible_opposite_universal_kernels_visited'],'runtime_seconds':round(seconds,3)},sort_keys=True))
