#!/usr/bin/env python3
"""Local-envelope audit for the first missing adjacent-cycle cylinder hull.

The predecessor receipt finds that, for z equal to pulled right event 18, the
exact set-theoretic left-coordinate cylinder hull C is absent.  This audit
recomputes C and compares it with every one of the 18,676 old left events.  It
finds the sharp old-event bracket 0x404 < C < 0x505.  Only 0x505 is relevant
to z itself: it is z's least left-old upper envelope.  The 0x404 event is the
greatest old event contained in C; it is not z's lower shadow, which is 0
because the opposite universal mask U_B is empty.  No mixed closure is built.
"""
import argparse,hashlib,json,os,struct,sys,time

HERE=os.path.dirname(os.path.abspath(__file__));sys.path.insert(0,HERE)
import full_cycle_adjacent_rectangle_intersection as inter

SCHEMA='adjacent-full-cycle-missing-hull-envelope-v1'
SOURCE='adjacent_full_cycle_exact_old_shadow.json'

def payload():
 start=time.perf_counter();src=json.load(open(os.path.join(HERE,SOURCE)))
 witness=src['first_missing_exact_old_shadow'];assert witness and witness['kind']=='least_left_set_hull'
 base,b=inter.capture_grammar();events=b['all_events'];macros=b['macros'];engines=b['engines'];states=b['states'];N=len(states)
 roots={ev:r for r,ev in b['root_to_event'].items()};gle=b['gle'];principal=b['principal']
 assert len(events)==len(principal)==18676
 bi=witness['opposite_class_representative_event_index'];broot=roots[events[bi]];pos=0

 # Exact existential shared-state mask of the serialized opposite event.
 cache={}
 def nonempty(m,root,i):
  key=(m,root,i)
  if key in cache:return cache[key]
  if root<=1:z=bool(root)
  else:
   v,ch=engines[m].nodes[root]
   z=nonempty(m,ch[i],i) if v==pos else any(nonempty(m,x,i) for x in ch)
  cache[key]=z;return z
 seen=[False]*N;possible=[False]*N
 for m,(_,ds) in enumerate(macros):
  for i,s in enumerate(ds[pos]):seen[s]=True;possible[s]|=nonempty(m,broot[m],i)
 assert all(seen);mask=sum(1<<s for s,v in enumerate(possible) if v)
 def mhash(x):return hashlib.sha256(x.to_bytes(28,'little')).hexdigest()
 assert mhash(mask)==witness['opposite_E_sha256'] and mask.bit_count()==witness['piecewise_full_state_count']==71
 candidate=tuple(engines[m].varset(3,{s for s in ds[3] if mask>>s&1}) for m,(_,ds) in enumerate(macros))
 def rhash(x):return hashlib.sha256(b''.join(struct.pack('<I',z) for z in x)).hexdigest()
 assert rhash(candidate)==witness['candidate_root_tuple_sha256'] and candidate not in roots.values()

 uppers=[i for i,r in enumerate(roots[ev] for ev in events) if gle(candidate,r)]
 lowers=[i for i,r in enumerate(roots[ev] for ev in events) if gle(r,candidate)]
 U=sum(1<<i for i in uppers);L=sum(1<<i for i in lowers)
 # An upper u is nonminimal iff another upper v is strictly below it.
 upper_has_strict_lower=0
 for v in uppers:upper_has_strict_lower|=(principal[v]&U)&~(1<<v)
 minimal_upper_bits=U&~upper_has_strict_lower
 minimal_uppers=[i for i in uppers if minimal_upper_bits>>i&1]
 least_uppers=[i for i in minimal_uppers if U&~principal[i]==0]
 # A lower v is nonmaximal iff its principal upset contains another lower.
 maximal_lowers=[v for v in lowers if not ((principal[v]&L)&~(1<<v))]
 common_upper=(1<<len(events))-1
 for v in lowers:common_upper&=principal[v]
 greatest_lowers=[i for i in maximal_lowers if common_upper>>i&1]
 def erec(i):
  p,f=events[i];return {'event_index':i,'full17_hex':hex(f),'partial_root_tuple_sha256':rhash(p),'partial_component_is_zero':all(x==0 for x in p),'physical_root_tuple_sha256':rhash(roots[events[i]])}
 out={'schema':SCHEMA,'schema_version':'1.0','source_exact_shadow_payload_sha256':src['payload_sha256'],'base_full_cycle_payload_sha256':base['payload_sha256'],
  'candidate_kind':'least left-coordinate cylinder hull C for retained empty event and opposite event 18','candidate_shared_state_count':mask.bit_count(),
  'retained_event_record':witness['retained_event_record'],'opposite_event_record':witness['opposite_event_record'],
  'candidate_shared_state_mask_sha256':mhash(mask),'candidate_root_tuple_sha256':rhash(candidate),'candidate_is_old_event':candidate in roots.values(),
  'old_events_tested':len(events),'old_upper_bounds':len(uppers),'inclusion_minimal_old_upper_bounds':len(minimal_uppers),
  'least_old_upper_envelopes':len(least_uppers),'minimal_old_upper_records':[erec(i) for i in minimal_uppers[:32]],
  'old_lower_bounds':len(lowers),'inclusion_maximal_old_lower_bounds':len(maximal_lowers),'greatest_old_lower_envelopes':len(greatest_lowers),
  'maximal_old_lower_records':[erec(i) for i in maximal_lowers[:32]],
  'opposite_universal_mask_is_empty':witness['opposite_U_sha256']==mhash(0),'original_z_greatest_left_old_lower_is_zero':witness['opposite_U_sha256']==mhash(0),
  'sharp_coordinate_cylinder_bracket':{'greatest_old_event_below_C_full17_hex':hex(events[greatest_lowers[0]][1]) if len(greatest_lowers)==1 else None,
                                       'least_old_event_above_C_full17_hex':hex(events[least_uppers[0]][1]) if len(least_uppers)==1 else None},
  'upper_leastness_method':'All 18,676 physical roots are tested for candidate subset. An upper u is least iff its certified principal upset contains the complete upper-bound bitset.',
  'lower_greatestness_method':'All roots are tested for subset of candidate; maximal elements use the certified principal upsets, and a greatest element lies in every lower bound principal upset.',
  'interpretation':('The missing coordinate cylinder C has a unique least old local upper envelope; this is also z actual least left-old upper. The greatest old event inside C is not z lower shadow (which is 0 because U_B is empty).' if len(least_uppers)==1 else
                    'The missing exact cylinder has no least old local upper envelope; its serialized incomparable minimal old upper bounds are an exact first-round conservativity obstruction.' if len(least_uppers)==0 and len(minimal_uppers)>1 else
                    'Unexpected envelope multiplicity; inspect the serialized bound records.'),
  'scope':'Exact old-copy envelope poset for one serialized 71-state cylinder only. No closure of the adjacent union, no assertion about other mixed pairs, and no lattice/OML/direct-limit claim.',
  'runtime_reporting':'Wall-clock time is printed by the command but excluded from the deterministic payload.','evidence_class':'executable verified symbolic reduced-MDD subset census',
  'command':'python3 notes/open_questions/verification/adjacent_full_cycle_missing_hull_envelope.py --verify'}
 out['producer_sha256']=hashlib.sha256(open(__file__,'rb').read()).hexdigest();out['payload_sha256']=hashlib.sha256(json.dumps(out,sort_keys=True,separators=(',',':')).encode()).hexdigest()
 return out,time.perf_counter()-start

if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--emit',action='store_true');ap.add_argument('--verify',action='store_true');a=ap.parse_args();out,seconds=payload();path=os.path.join(HERE,'adjacent_full_cycle_missing_hull_envelope.json')
 if a.emit:
  with open(path,'w') as f:json.dump(out,f,sort_keys=True,indent=2);f.write('\n')
 else:assert json.load(open(path))==out
 print(json.dumps({'status':'PASS','payload_sha256':out['payload_sha256'],'old_upper_bounds':out['old_upper_bounds'],'minimal_uppers':out['inclusion_minimal_old_upper_bounds'],'least_envelopes':out['least_old_upper_envelopes'],'runtime_seconds':round(seconds,3)},sort_keys=True))
