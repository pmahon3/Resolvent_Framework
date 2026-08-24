#!/usr/bin/env python3
"""Bounded per-state restricted-root class census for atomic horns.

This is a representation prototype, not a horn-atlas search.  In the old
18,676-event full-cycle OML it first enumerates atomic extensions (P,a,P join
a) and retains exactly those for which the old lattice join strictly exceeds
the literal set union.  It then records the event indices occurring as P, a,
or P join a in such horns.

For a selected shared state s and an orientation position, the exact local
trace of an event is the ordered tuple of reduced-MDD roots obtained by
restricting every macrofibre occurrence of s at that position.  The occurrence
order is fixed, so equality of tuples is exact even though root identifiers are
local to their macrofibre engines.  Classes are interned independently for each
(orientation,s).  No cross-class containment matrix and no mixed kernel atlas
is constructed.
"""
import argparse, functools, hashlib, json, os, struct, sys, time

HERE=os.path.dirname(os.path.abspath(__file__));sys.path.insert(0,HERE)
import full_cycle_adjacent_rectangle_intersection as inter

SCHEMA='adjacent-full-cycle-restricted-trace-classes-v1'

def payload(state_count=12):
 if not 8 <= state_count <= 16:
  raise ValueError('state_count must lie in [8,16]')
 started=time.perf_counter();base,b=inter.capture_grammar()
 events=b['all_events'];macros=b['macros'];engines=b['engines'];states=b['states']
 roots={ev:r for r,ev in b['root_to_event'].items()};principal=b['principal']
 n=len(events);assert n==18676 and len(principal)==n and len(states)==224
 upmap={u:i for i,u in enumerate(principal)};assert len(upmap)==n
 allold=(1<<n)-1;zero=upmap[allold]
 nonatomic=0
 for d,u in enumerate(principal):
  if d!=zero:nonatomic|=u&~(1<<d)
 atom_bits=allold&~nonatomic&~(1<<zero);atoms=[]
 while atom_bits:
  z=atom_bits&-atom_bits;atoms.append(z.bit_length()-1);atom_bits-=z
 assert len(atoms)==91

 # On atom-support macros literal union requires OR(P_m,a_m)=J_m.  Off the
 # atom support it requires P_m=J_m.  The latter checks are load-bearing:
 # nondistributive lattice join can overshoot the literal union away from the
 # atom's set support.  Thus the test below is exact on all 842 macrofibres,
 # while MDD OR is needed only on the atom support.
 atom_support={a:tuple(m for m,r in enumerate(roots[events[a]]) if r) for a in atoms}
 atom_support_sets={a:frozenset(atom_support[a]) for a in atoms}
 roleP=set();roleA=set();roleJ=set();strict_horns=0;extensions=0
 for p in range(n):
  pp=principal[p];pr=roots[events[p]]
  for a in atoms:
   if principal[a]>>p&1: # a <= p, so this is not a genuine extension
    continue
   extensions+=1;j=upmap[pp&principal[a]];jr=roots[events[j]];ar=roots[events[a]]
   literal=True;support=atom_support_sets[a]
   for m in atom_support[a]:
    if engines[m].app(1,pr[m],ar[m])!=jr[m]:
     literal=False;break
   if literal:
    for m in range(len(macros)):
     if m not in support and pr[m]!=jr[m]:
      literal=False;break
   if not literal:
    strict_horns+=1;roleP.add(p);roleA.add(a);roleJ.add(j)
 roles=sorted(roleP|roleA|roleJ)

 # Regression supplied by hostile review: this join overshoots only away
 # from the atom support, so both order direction and full-macro equality are
 # exercised.  Event indices are stable under the banked grammar receipt.
 rp,ra,rj=1,18451,18431
 assert ra in atoms and not (principal[ra]>>rp&1)
 assert upmap[principal[rp]&principal[ra]]==rj
 rrP=roots[events[rp]];rrA=roots[events[ra]];rrJ=roots[events[rj]]
 regression_on=sum(engines[m].app(1,rrP[m],rrA[m])!=rrJ[m] for m in atom_support[ra])
 regression_off=sum(rrP[m]!=rrJ[m] for m in range(len(macros)) if m not in atom_support_sets[ra])
 assert regression_on==0 and regression_off==432

 # Evenly spaced deterministic shared states, including both endpoints.
 selected=tuple((i*(len(states)-1))//(state_count-1) for i in range(state_count))
 assert len(set(selected))==state_count
 occurrences={}
 for pos in (3,0):
  per=[[] for _ in states]
  for m,(_,ds) in enumerate(macros):
   for i,s in enumerate(ds[pos]):per[s].append((m,i))
  occurrences[pos]=per

 @functools.lru_cache(None)
 def restrict(m,root,pos,i):
  if root<=1:return root
  v,ch=engines[m].nodes[root]
  if v==pos:return ch[i]
  return engines[m].node(v,[restrict(m,z,pos,i) for z in ch])

 orientation_records=[];total_raw=total_unique=total_packed=0
 for name,pos in (('left_retained_position_11',3),('right_retained_position_00',0)):
  for s in selected:
   occ=occurrences[pos][s];classes={};multiplicities={}
   role_class_sets={'P':set(),'atom':set(),'join':set()}
   for ev_i in roles:
    rr=roots[events[ev_i]]
    key=tuple(restrict(m,rr[m],pos,i) for m,i in occ)
    cid=classes.setdefault(key,len(classes));multiplicities[cid]=multiplicities.get(cid,0)+1
    if ev_i in roleP:role_class_sets['P'].add(cid)
    if ev_i in roleA:role_class_sets['atom'].add(cid)
    if ev_i in roleJ:role_class_sets['join'].add(cid)
   unique=len(classes);raw=len(roles);packed=sum(4*len(k) for k in classes)
   # Re-intern in reverse event order as a collision-free implementation
   # self-check: the partition multiplicity multiset must be identical.
   reverse={};rm={}
   for ev_i in reversed(roles):
    rr=roots[events[ev_i]];key=tuple(restrict(m,rr[m],pos,i) for m,i in occ)
    cid=reverse.setdefault(key,len(reverse));rm[cid]=rm.get(cid,0)+1
   assert len(reverse)==unique and sorted(rm.values())==sorted(multiplicities.values())
   record={'orientation':name,'position':pos,'shared_state_index':s,
    'macrofibre_occurrences':len(occ),
    'horn_role_events':raw,'distinct_exact_trace_classes':unique,
    'compression_ratio_raw_events_per_class':raw/unique,
    'largest_class_multiplicity':max(multiplicities.values()),
    'singleton_class_count':sum(v==1 for v in multiplicities.values()),
    'P_role_class_count':len(role_class_sets['P']),
    'atom_role_class_count':len(role_class_sets['atom']),
    'join_role_class_count':len(role_class_sets['join']),
    'canonical_unique_root_words_packed_bytes':packed,
    'multiplicity_histogram':{str(k):list(multiplicities.values()).count(k) for k in sorted(set(multiplicities.values()))}}
   orientation_records.append(record);total_raw+=raw;total_unique+=unique;total_packed+=packed

 out={'schema':SCHEMA,'schema_version':'1.0','base_full_cycle_payload_sha256':base['payload_sha256'],
  'completed_events':n,'old_atom_count':len(atoms),'genuine_atomic_extensions':extensions,
  'strict_atomic_join_overshoot_horns':strict_horns,
  'off_support_regression':{'P_event_index':rp,'atom_event_index':ra,'join_event_index':rj,
   'overshoot_macros_on_atom_support':regression_on,'overshoot_macros_off_atom_support':regression_off},
  'distinct_P_role_events':len(roleP),'distinct_atom_role_events':len(roleA),
  'distinct_join_role_events':len(roleJ),'distinct_union_horn_role_events':len(roles),
  'selected_shared_state_count':state_count,'selected_shared_state_indices':list(selected),
  'per_state_orientation_records':orientation_records,
  'aggregate_raw_event_trace_words':total_raw,'aggregate_distinct_trace_classes':total_unique,
  'aggregate_compression_ratio':total_raw/total_unique,
  'aggregate_canonical_unique_root_words_packed_bytes':total_packed,
  'restriction_cache_entries':restrict.cache_info().currsize,
  'representation_result':'Exact restricted-root class interning is measured independently per selected shared state and orientation, only for events occurring in strict atomic-extension horns.',
  'quantifier_scope':'All old P and all 91 old atoms are exhaustively tested for strict literal-union overshoot. Trace classes are measured only on the deterministic selected 8-16 shared states; no claim covers the other states.',
  'scope_not_covered':'No containment matrix, bad-mask atlas, kernel verdict, mixed closure, latticehood, OML, direct limit, sigma closure, MBRC, ODBC, or Phi conclusion.',
  'verification_independence':'Single producer. Reverse-order reinterning independently checks each class partition multiplicity multiset; it shares the same restriction primitive and is not an independent verifier.',
  'evidence_classes':['Executable verified'],
  'runtime_reporting':'Wall time is printed but excluded from the deterministic payload.',
  'command':f'python3 notes/open_questions/verification/adjacent_full_cycle_restricted_trace_classes.py --verify --state-count {state_count}'}
 out['producer_sha256']=hashlib.sha256(open(__file__,'rb').read()).hexdigest()
 out['payload_sha256']=hashlib.sha256(json.dumps(out,sort_keys=True,separators=(',',':')).encode()).hexdigest()
 return out,time.perf_counter()-started

if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--emit',action='store_true');ap.add_argument('--verify',action='store_true');ap.add_argument('--state-count',type=int,default=12);a=ap.parse_args()
 out,seconds=payload(a.state_count)
 path=os.path.join(HERE,f'adjacent_full_cycle_restricted_trace_classes_s{a.state_count}.json')
 if a.emit:
  with open(path,'w') as f:json.dump(out,f,sort_keys=True,indent=2);f.write('\n')
 else:assert json.load(open(path))==out
 print(json.dumps({'status':'PASS','payload_sha256':out['payload_sha256'],'strict_horns':out['strict_atomic_join_overshoot_horns'],'role_events':out['distinct_union_horn_role_events'],'trace_classes':out['aggregate_distinct_trace_classes'],'packed_bytes':out['aggregate_canonical_unique_root_words_packed_bytes'],'runtime_seconds':round(seconds,3)},sort_keys=True))
