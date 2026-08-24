#!/usr/bin/env python3
"""Exact first-round old-cylinder shadow test for adjacent full cycles.

For every actual descriptor A in one completed copy and every distinct
existential/universal shadow class (E_B,U_B) occurring in the other copy for
which E_A cap E_B is empty, test the exact old-cylinder bounds of the mixed
disjoint union z=A_L union B_R.  On the left carrier these are

  greatest set-theoretic lower core: A union cylinder(U_B),
  least set-theoretic upper hull:    A union cylinder(E_B).

The symmetric right tests retain the full partial MDD of B and quotient only
the opposite A by (E_A,U_A).  Membership means equality with an actual event
of the corresponding 18,676-event completed copy.  The search stops at the
first missing exact core/hull.  It does not close the two-copy union and makes
no lattice, OML, or arbitrary-depth claim.
"""
import argparse,hashlib,json,math,os,struct,sys,time

HERE=os.path.dirname(os.path.abspath(__file__));sys.path.insert(0,HERE)
import full_cycle_adjacent_rectangle_intersection as inter

SCHEMA='adjacent-full-cycle-exact-old-shadow-v1'

def payload():
 start=time.perf_counter()
 base,b=inter.capture_grammar();events=b['all_events'];macros=b['macros'];engines=b['engines'];states=b['states']
 roots={ev:r for r,ev in b['root_to_event'].items()};rootset=set(roots.values());N=len(states)

 # Classify the section at one shared-coordinate value as empty/full/partial.
 # The cache is discarded between orientations to keep peak memory bounded.
 def event_shadows(pos):
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
   possible=[False]*N;universal=[True]*N;seen=[False]*N
   for m,(_,ds) in enumerate(macros):
    root=roots[ev][m]
    for i,s in enumerate(ds[pos]):
     z=cls(m,root,i);seen[s]=True;possible[s]|=z!=0;universal[s]&=z==1
   assert all(seen)
   E=sum(1<<s for s,v in enumerate(possible) if v)
   U=sum(1<<s for s,v in enumerate(universal) if v)
   assert not U&~E
   ans.append((E,U))
  return ans,len(cache)

 left,cacheL=event_shadows(3)
 right,cacheR=event_shadows(0)
 leftclasses={x:i for i,x in enumerate(left)}
 rightclasses={x:i for i,x in enumerate(right)}

 cylinder_cache={}
 def cylinder(pos,mask):
  key=(pos,mask)
  if key not in cylinder_cache:
   cylinder_cache[key]=tuple(engines[m].varset(pos,{s for s in ds[pos] if mask>>s&1}) for m,(_,ds) in enumerate(macros))
  return cylinder_cache[key]
 def gor(x,y):return tuple(engines[m].app(1,x[m],y[m]) for m in range(len(macros)))
 def rhash(x):return hashlib.sha256(b''.join(struct.pack('<I',z) for z in x)).hexdigest()
 def mhash(x):return hashlib.sha256(x.to_bytes(28,'little')).hexdigest()
 def erec(i):
  p,f=events[i]
  return {'event_index':i,'full17_hex':hex(f),'partial_root_tuple_sha256':rhash(p),'physical_root_tuple_sha256':rhash(roots[events[i]])}

 tested_pairs=0;tested_roots=0;witness=None
 # R is the left rectangle, whose shared global cell is local position 11=3.
 for ai,A in enumerate(left):
  EA,UA=A;aroot=roots[events[ai]]
  for B,bi in sorted(rightclasses.items()):
   EB,UB=B
   if EA&EB:continue
   tested_pairs+=1
   for kind,mask in (('greatest_left_lower_core',UB),('least_left_set_hull',EB)):
    candidate=gor(aroot,cylinder(3,mask));tested_roots+=1
    if candidate not in rootset:
     witness={'direction':'left_old_copy','kind':kind,'retained_event_index':ai,'opposite_class_representative_event_index':bi,
      'retained_event_record':erec(ai),'opposite_event_record':erec(bi),
      'retained_E_sha256':mhash(EA),'retained_U_sha256':mhash(UA),'opposite_E_sha256':mhash(EB),'opposite_U_sha256':mhash(UB),
      'piecewise_full_state_mask_sha256':mhash(mask),'piecewise_full_state_count':mask.bit_count(),'candidate_root_tuple_sha256':rhash(candidate)}
     break
   if witness:break
  if witness:break
 # S is the right rectangle, whose shared global cell is local position 00=0.
 if witness is None:
  for bi,B in enumerate(right):
   EB,UB=B;broot=roots[events[bi]]
   for A,ai in sorted(leftclasses.items()):
    EA,UA=A
    if EA&EB:continue
    tested_pairs+=1
    for kind,mask in (('greatest_right_lower_core',UA),('least_right_set_hull',EA)):
     candidate=gor(broot,cylinder(0,mask));tested_roots+=1
     if candidate not in rootset:
      witness={'direction':'right_old_copy','kind':kind,'retained_event_index':bi,'opposite_class_representative_event_index':ai,
       'retained_event_record':erec(bi),'opposite_event_record':erec(ai),
       'retained_E_sha256':mhash(EB),'retained_U_sha256':mhash(UB),'opposite_E_sha256':mhash(EA),'opposite_U_sha256':mhash(UA),
       'piecewise_full_state_mask_sha256':mhash(mask),'piecewise_full_state_count':mask.bit_count(),'candidate_root_tuple_sha256':rhash(candidate)}
      break
    if witness:break
   if witness:break

 out={'schema':SCHEMA,'schema_version':'1.0','base_full_cycle_payload_sha256':base['payload_sha256'],
  'completed_events_each':len(events),'shared_states':N,'left_actual_descriptors':len(left),'right_actual_descriptors':len(right),
  'left_distinct_EU_classes':len(leftclasses),'right_distinct_EU_classes':len(rightclasses),
  'left_classification_cache_entries':cacheL,'right_classification_cache_entries':cacheR,
  'actual_descriptor_by_opposite_class_pairs_tested_before_stop':tested_pairs,'exact_piecewise_roots_tested_before_stop':tested_roots,
  'all_first_round_exact_old_cylinder_cores_and_hulls_realized':witness is None,'first_missing_exact_old_shadow':witness,
  'quantifiers':('Left: every one of 18,676 actual local-position-11 descriptors A against every distinct local-position-00 (E_B,U_B) class with E_A intersection E_B empty. '
                 'Right: every one of 18,676 actual local-position-00 descriptors B against every distinct local-position-11 (E_A,U_A) class with E_A intersection E_B empty. '
                 'Only the opposite descriptor is quotiented by (E,U); the retained descriptor contributes its exact partial MDD roots.'),
  'disjointness_justification':'On the full surjective fibre product, two pulled cylinders are disjoint iff their existential shared-state masks have empty intersection.',
  'formula':{'left_lower':'A union cylinder(U_B)','left_upper':'A union cylinder(E_B)','right_lower':'B union cylinder(U_A)','right_upper':'B union cylinder(E_A)'},
  'interpretation':('Every exact first-round greatest-old-cylinder lower core and least-old-cylinder set hull is an actual event of the corresponding completed copy.' if witness is None else
                    'The serialized candidate is the first exact first-round old-cylinder core/hull absent from the corresponding completed copy; coarse (E,U) realization did not detect it.'),
  'scope':'Exact first-round old-cylinder core/hull membership only. No assertion that a mixed union is local, no closure of the two-copy union, no preservation after later mixed repairs, and no lattice/OML/direct-limit claim.',
  'runtime_reporting':'Wall-clock time is printed by the command but excluded from the deterministic payload; operation and cache counts above are deterministic runtime receipts.',
  'evidence_class':'executable verified symbolic reduced-MDD root equality','command':'python3 notes/open_questions/verification/adjacent_full_cycle_exact_old_shadow.py --verify'}
 out['producer_sha256']=hashlib.sha256(open(__file__,'rb').read()).hexdigest();out['payload_sha256']=hashlib.sha256(json.dumps(out,sort_keys=True,separators=(',',':')).encode()).hexdigest()
 return out,time.perf_counter()-start

if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--emit',action='store_true');ap.add_argument('--verify',action='store_true');a=ap.parse_args();out,seconds=payload();path=os.path.join(HERE,'adjacent_full_cycle_exact_old_shadow.json')
 if a.emit:
  with open(path,'w') as f:json.dump(out,f,sort_keys=True,indent=2);f.write('\n')
 else:assert json.load(open(path))==out
 print(json.dumps({'status':'PASS','payload_sha256':out['payload_sha256'],'first_missing':out['first_missing_exact_old_shadow'],'runtime_seconds':round(seconds,3)},sort_keys=True))
