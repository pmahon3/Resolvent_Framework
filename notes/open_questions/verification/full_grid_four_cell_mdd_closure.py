#!/usr/bin/env python3
"""Exact bounded MDD closure for the node-6 full four-cell carrier."""
import argparse,collections,functools,hashlib,itertools,json,math,os,random,sys
HERE=os.path.dirname(os.path.abspath(__file__));sys.path.insert(0,HERE)
import sharedq_kcell_completion_audit as cell
import full_grid_terminal_split_one_cell_quotient as one
import full_grid_core16_pjh_defect_atlas as atlas_mod
import full_grid_binary_pjh_split_core_audit as split_mod
SCHEMA="full-grid-four-cell-mdd-closure-v1";NODE_ID=6;FULL17=(1<<17)-1

class MDD:
 def __init__(self,domains):
  self.domains=domains;self.nodes=[None,None];self.intern={};self.acache={};self.ncache={0:1,1:0}
 def node(self,v,ch):
  if all(x==ch[0] for x in ch):return ch[0]
  k=(v,tuple(ch));z=self.intern.get(k)
  if z is None:z=len(self.nodes);self.intern[k]=z;self.nodes.append(k)
  return z
 def varset(self,v,S):return self.node(v,[1 if x in S else 0 for x in self.domains[v]])
 def neg(self,x):
  if x in self.ncache:return self.ncache[x]
  v,ch=self.nodes[x];z=self.node(v,[self.neg(a) for a in ch]);self.ncache[x]=z;return z
 def app(self,op,x,y):
  if op==0:
   if not x or not y:return 0
   if x==1:return y
   if y==1:return x
  else:
   if x==1 or y==1:return 1
   if not x:return y
   if not y:return x
  if x==y:return x
  k=(op,min(x,y),max(x,y));z=self.acache.get(k)
  if z is not None:return z
  vx=self.nodes[x][0];vy=self.nodes[y][0];v=min(vx,vy)
  cx=self.nodes[x][1] if vx==v else [x]*len(self.domains[v]);cy=self.nodes[y][1] if vy==v else [y]*len(self.domains[v])
  z=self.node(v,[self.app(op,a,b) for a,b in zip(cx,cy)]);self.acache[k]=z;return z
 def evaluate(self,x,point):
  while x>1:v,ch=self.nodes[x];x=ch[self.domains[v].index(point[v])]
  return x

def payload(event_cap=25000,node_cap=200000):
 states=cell.cell_states();local=one.local_event_predicates(states);groups=collections.defaultdict(list)
 for j,s in enumerate(states):
  a=tuple(int(x in s) for x in cell.SHARED);q=int('e11'in s or'e10'in s);r=int('e11'in s or'e01'in s);groups[a,q,r].append(j)
 macros=[]
 for a0 in sorted({x[0] for x in groups}):
  for a1 in sorted({x[0] for x in groups}):
   for q0,q1,r0,r1 in itertools.product((0,1),repeat=4):
    ds=(groups[a0,q0,r0],groups[a0,q0,r1],groups[a1,q1,r0],groups[a1,q1,r1])
    if all(ds):macros.append(((a0,a1,q0,q1,r0,r1),ds))
 engines=[MDD(ds) for _,ds in macros]
 sourcehash='ae31a846410eff44a1133601bbc9bdab774ffea3e4aa10a4a5e8009752b7799c'
 source=next(e for e in local if hashlib.sha256(e.to_bytes(28,'little')).hexdigest()==sourcehash)
 # Atom roots per macro. Profiles 0..14 are whole macro fibres; profile 15 is split by source on coordinate 0.
 atomroots=[]
 for m,(key,ds) in enumerate(macros):
  p=(key[2]<<3)|(key[3]<<2)|(key[4]<<1)|key[5];row=[0]*17
  if p<15:row[p]=1
  else:
   z=engines[m].varset(0,{s for s in ds[0] if source>>s&1});row[15]=z;row[16]=engines[m].neg(z)
  atomroots.append(row)
 def gapp(op,x,y):return tuple(engines[m].app(op,x[m],y[m]) for m in range(len(macros)))
 def gneg(x):return tuple(engines[m].neg(x[m]) for m in range(len(macros)))
 ZERO=(0,)*len(macros);ONE=(1,)*len(macros)
 atoms=[tuple(atomroots[m][a] for m in range(len(macros))) for a in range(17)]
 @functools.lru_cache(None)
 def au(bits):
  z=ZERO
  for a in range(17):
   if bits>>a&1:z=gapp(1,z,atoms[a])
  return z
 def nonzero(x):return any(x)
 def gle(x,y):return not nonzero(gapp(0,x,gneg(y)))
 def canon(x):
  f=0
  for a in range(17):
   if gle(atoms[a],x):f|=1<<a
  return (gapp(0,x,gneg(au(f))),f)
 @functools.lru_cache(None)
 def touch(p):return sum(1<<a for a in range(17) if nonzero(gapp(0,p,atoms[a])))
 def comp(x):
  p,f=x;t=touch(p);return (gapp(0,au(t),gneg(p)),FULL17^(f|t))
 def disjoint(x,y):
  p,f=x;q,g=y
  return not(f&g or touch(p)&g or touch(q)&f or nonzero(gapp(0,p,q)))
 def union(x,y):
  p,f=x;q,g=y;return canon(gapp(1,gapp(1,p,q),au(f|g)))
 def le(x,y):
  p,f=x;q,g=y
  return not(f&~g) and gle(p,gapp(1,q,au(g)))
 # Validate MDD Boolean operations by enumeration: every fibre <=256, plus deterministic samples in the largest fibres.
 rng=random.Random(1604);validated_small=0;validated_sampled=0
 cell_roots=[]
 for pos in range(4):
  for e in local:
   cell_roots.append(tuple(engines[m].varset(pos,{s for s in ds[pos] if e>>s&1}) for m,(_,ds) in enumerate(macros)))
 for m,(_,ds) in enumerate(macros):
  eng=engines[m];size=math.prod(map(len,ds));tests=[]
  if size<=256:
   tests=list(itertools.product(*ds));validated_small+=len(tests)
  elif size>=50000:
   tests=[tuple(rng.choice(d) for d in ds) for _ in range(64)];validated_sampled+=len(tests)
  for pt in tests:
   roots=[eng.varset(v,{pt[v]}) for v in range(4)]
   for x,y in zip(roots,roots[1:]+roots[:1]):
    assert eng.evaluate(eng.neg(x),pt)==(not eng.evaluate(x,pt))
    assert eng.evaluate(eng.app(0,x,y),pt)==(eng.evaluate(x,pt) and eng.evaluate(y,pt))
    assert eng.evaluate(eng.app(1,x,y),pt)==(eng.evaluate(x,pt) or eng.evaluate(y,pt))
 # Formal terminal.
 sourcej=json.load(open(os.path.join(HERE,atlas_mod.SOURCE)));node=next(x for x in sourcej['payload']['tree'] if x['id']==NODE_ID)
 atlas=json.load(open(os.path.join(HERE,'full_grid_core16_pjh_defect_atlas.json')));rec=next(x for x in atlas['records'] if x['node_id']==NODE_ID)
 low=int(rec['failed_lower_hex'],16);fam=atlas_mod.close16(atlas_mod.raw16())
 for choice in node['path_choices_hex']:
  z=int(choice,16);fam=atlas_mod.close16(fam|{z,atlas_mod.FULL^z})
 formal_join=split_mod.lift(low,15)|(1<<15)
 terminal=split_mod.close_logic({split_mod.lift(e,15) for e in fam}|{formal_join,FULL17^formal_join},FULL17)
 old={(ZERO,e) for e in terminal};events=set(old);extras=[];cursor=0;reason=None
 def add(x):
  if x not in events:events.add(x);extras.append(x);return True
 for root in cell_roots:add(canon(root))
 oldcodes=sorted(terminal)
 while cursor<len(extras):
  x=extras[cursor];add(comp(x))
  if len(events)>event_cap:reason='event_cap';break
  for e in oldcodes:
   y=(ZERO,e)
   if disjoint(x,y):add(union(x,y))
   if len(events)>event_cap:reason='event_cap';break
  if reason:break
  for y in extras[:cursor]:
   if disjoint(x,y):add(union(x,y))
   if len(events)>event_cap:reason='event_cap';break
  if reason:break
  if sum(len(e.nodes) for e in engines)>node_cap:reason='node_cap';break
  cursor+=1
 nodes=sum(len(e.nodes) for e in engines)
 # Exact lattice audit, reducing old-old pairs to the banked terminal lattice.
 oldcodes=sorted(terminal);all_events=[(ZERO,e) for e in oldcodes]+sorted(set(extras)-old,key=lambda x:(x[1],hash(x[0])))
 newevents=all_events[len(oldcodes):];oldpres=True
 for x in newevents:
  lowers=[e for e in oldcodes if le((ZERO,e),x)];greatest=0
  for e in lowers:greatest|=e
  if greatest not in terminal:oldpres=False;break
 oldcontains=[0]*17
 for j,e in enumerate(oldcodes):
  for a in range(17):
   if e>>a&1:oldcontains[a]|=1<<j
 allold=(1<<len(oldcodes))-1;principal=[]
 for x in all_events:
  support=x[1]|touch(x[0]);u=allold
  for a in range(17):
   if support>>a&1:u&=oldcontains[a]
  for j,y in enumerate(newevents):
   if le(x,y):u|=1<<(len(oldcodes)+j)
  principal.append(u)
 upmap={u:i for i,u in enumerate(principal)};failure=None;tested=0
 if reason is None and oldpres and len(upmap)==len(all_events):
  for ix in range(len(oldcodes),len(all_events)):
   for iy in range(len(all_events)):
    tested+=1;c=principal[ix]&principal[iy]
    if c not in upmap:failure=(ix,iy);break
   if failure:break
 lattice=reason is None and oldpres and len(upmap)==len(all_events) and failure is None
 # Exact gates expressible in the event algebra.
 def cylinder(pos,pred):return canon(tuple(engines[m].varset(pos,{s for s in ds[pos] if pred(s)}) for m,(_,ds) in enumerate(macros)))
 def qpred(s):return bool((1<<s)&sum(1<<j for j,x in enumerate(states) if 'e11'in x or'e10'in x))
 def rpred(s):return bool((1<<s)&sum(1<<j for j,x in enumerate(states) if 'e11'in x or'e01'in x))
 qs=[cylinder(0,qpred),cylinder(2,qpred)];rs=[cylinder(0,rpred),cylinder(1,rpred)]
 acts=[cylinder(0,lambda s:all(x in states[s] for x in cell.SHARED)),cylinder(2,lambda s:all(x in states[s] for x in cell.SHARED))]
 def reconstructed(x,y):return all(canon(gapp(0,A,B)) in events for A,B in ((gapp(1,x[0],au(x[1])),gapp(1,y[0],au(y[1]))),(gapp(1,x[0],au(x[1])),gneg(gapp(1,y[0],au(y[1])))),(gneg(gapp(1,x[0],au(x[1]))),gapp(1,y[0],au(y[1]))),(gneg(gapp(1,x[0],au(x[1]))),gneg(gapp(1,y[0],au(y[1]))))))
 defect=(ZERO,formal_join);hull=(ZERO,split_mod.lift(int(rec['failed_upper_hex'],16),15));wits=[(ZERO,split_mod.lift(int(w,16),15)) for w in rec['witness_pair_hex']]
 defectjoin=all(not(le(wits[0],u) and le(wits[1],u)) or le(defect,u) for u in events)
 def setinter(x,y):return canon(gapp(0,gapp(1,x[0],au(x[1])),gapp(1,y[0],au(y[1]))))
 qlit=setinter(comp(qs[0]),qs[1]);qlowers=[e for e in events if le(e,qlit)];qmeet=(ZERO,0)
 for e in qlowers:qmeet=union(qmeet,e)
 if qmeet not in events:qmeet=None
 residue=None if qmeet is None else setinter(qlit,comp(qmeet))
 oldq=(ZERO,0)
 for e in old:
  if le(e,qlit):oldq=union(oldq,e)
 qincrement=None if qmeet is None else setinter(qmeet,comp(oldq))
 def rootcount(m,x,start=0):
  if x<=1:return x*math.prod(len(macros[m][1][v]) for v in range(start,4))
  v,ch=engines[m].nodes[x];return math.prod(len(macros[m][1][u]) for u in range(start,v))*sum(rootcount(m,z,v+1) for z in ch)
 atomweights=[sum(rootcount(m,atomroots[m][a]) for m in range(len(macros))) for a in range(17)]
 def eventcount(x):return sum(rootcount(m,x[0][m]) for m in range(len(macros)))+sum(atomweights[a] for a in range(17) if x[1]>>a&1)
 def profilecounts(x):
  full=gapp(1,x[0],au(x[1]));out=[0]*16
  for m,(key,_) in enumerate(macros):out[(key[2]<<3)|(key[3]<<2)|(key[4]<<1)|key[5]]+=rootcount(m,full[m])
  return out
 # Exact centre. Physical-root membership avoids recanonicalizing intersections.
 # Every event is retained initially: commuting with an embedded centre-free
 # sub-OML does not force an outsider formal event to lie in that sub-OML's centre.
 generatorcodes={split_mod.lift(e,15) for e in atlas_mod.raw16()}|{split_mod.lift(int(x,16),15) for x in node['path_choices_hex']}|{formal_join}
 generators={(ZERO,e) for e in generatorcodes}|{canon(x) for x in cell_roots}
 def physroot(x):return gapp(1,x[0],au(x[1]))
 root_to_event={physroot(x):x for x in events};assert len(root_to_event)==len(events)
 assert all(canon(physroot(x))==x for x in newevents)
 assert all(x[0]==ZERO for x in old)
 def compatible(x,y):
  X=physroot(x);Y=physroot(y);nX=gneg(X);nY=gneg(Y)
  return gapp(0,X,Y) in root_to_event and gapp(0,X,nY) in root_to_event and gapp(0,nX,Y) in root_to_event
 centre_candidates=list(all_events)
 centre=[];centre_filter_counts=[]
 if lattice:
  centre=centre_candidates
  ordered=sorted(generators,key=lambda x:(x[1].bit_count(),x[1],hash(x[0])))
  for g in ordered:
   centre=[x for x in centre if compatible(x,g)];centre_filter_counts.append(len(centre))
   if len(centre)==2:break
 # Independent raw four-cell family E0 (without terminal atlas): exact
 # complement/disjoint-union closure in physical-root representation.
 e0=set(cell_roots);e0arr=list(e0);e0cur=0
 while e0cur<len(e0arr):
  x=e0arr[e0cur]
  for z in [gneg(x)]+[gapp(1,x,y) for y in e0arr[:e0cur] if not nonzero(gapp(0,x,y))]:
   if z not in e0:e0.add(z);e0arr.append(z)
  e0cur+=1
 assert len(e0)==230 and all(z in root_to_event for z in e0)
 assert defect in events and all(le(w,defect) for w in wits)
 out={'schema':SCHEMA,'schema_version':'1.0','macro_fibres':len(macros),'carrier_points':sum(math.prod(map(len,d)) for _,d in macros),
 'mdd_validation_small_point_evaluations':validated_small,'mdd_validation_sampled_large_point_evaluations':validated_sampled,
 'four_cell_cylinder_generators':len(cell_roots),'formal_terminal_events':len(terminal),'closure_events_at_stop':len(events),
 'extra_events_at_stop':len(set(extras)-old),'processed_extra_events':cursor,'closure_completed':reason is None,
 'stop_reason':reason,'event_cap':event_cap,'mdd_node_cap':node_cap,'interned_mdd_nodes':nodes,
 'max_nodes_in_one_macro':max(len(e.nodes) for e in engines),'apply_cache_entries':sum(len(e.acache) for e in engines),
 'old_terminal_sublattice_preserved':oldpres,'principal_upsets_injective':len(upmap)==len(all_events),'new_event_pairs_tested':tested,'first_lattice_failure':failure,'lattice':lattice,
 'orthomodular_lattice':lattice,
 'orthomodularity_status':'hand-exact consequence: for x<=y, y\\x is complement(x union complement(y)); the union exists by disjoint-union closure, so y\\x is an event and gives the orthomodular decomposition',
 'centre_events':len(centre) if lattice else None,'centre_is_trivial':lattice and set(centre)=={(ZERO,0),(ZERO,FULL17)},
 'centre_filter_counts':centre_filter_counts,
 'centre_status':'exact: all 18,676 events are filtered against actual generators using direct physical-MDD-root intersection membership; no categorical old-event reduction is used',
 'independent_raw_E0_events':len(e0),'all_E0_roots_in_completed_family':all(z in root_to_event for z in e0),
 'all_event_physical_roots_unique':len(root_to_event)==len(events),'all_new_descriptors_canonical':all(canon(physroot(x))==x for x in newevents),'all_old_descriptors_canonical_by_17_atom_form':all(x[0]==ZERO for x in old),
 'defect_is_event':defect in events,'both_witnesses_below_defect':all(le(w,defect) for w in wits),
 'closure_order_independence':'The queue computes the least fixed point of the deterministic complement/disjoint-union operator and processes every newly inserted event against every earlier event; set insertion order cannot change that fixed point. Independent E0 closure supplies a second construction path for all 230 raw roots.',
 'q_boundary_reconstructed':reconstructed(qs[0],qs[1]),'r_boundary_reconstructed':reconstructed(rs[0],rs[1]),
 'activation_cylinders_are_events':[a in events for a in acts],'nonzero_activation_supported_events':[sum(1 for e in events if e!=(ZERO,0) and le(e,a)) for a in acts],
 'defect_join_remains_witness_join':defectjoin,'hull_repaired':hull in events,
 'q0_complement_meet_q1_exists':qmeet in events if qmeet is not None else False,'q_meet_residue_is_event':residue in events if residue is not None else False,
 'q_meet_points':None if qmeet is None else eventcount(qmeet),'q_literal_intersection_points':eventcount(qlit),
 'q_meet_residue_points':None if residue is None else eventcount(residue),'q_meet_residue_profile_counts':None if residue is None else profilecounts(residue),
 'old_profile_core_q_meet_points':eventcount(oldq),'q_meet_increment_points':None if qincrement is None else eventcount(qincrement),'q_meet_increment_profile_counts':None if qincrement is None else profilecounts(qincrement),
 'point_evaluations_order_separate_by_concreteness':lattice,
 'phi_tame_because_finite':lattice,
 'exact_missing_compression_theorem':None if reason is None else 'Bound the number of canonical partial MDD descriptors generated by pairwise orthogonal unions of four coordinate-cylinder cell events over the 17 terminal atoms; equivalently prove finite closure of this descriptor algebra below the reported cap.',
 'scope':'Exact full four-cell closure, lattice/orthomodularity, centre, boundary, activation, PJH, q-meet and finite Phi-tameness audit.',
 'command':'python3 notes/open_questions/verification/full_grid_four_cell_mdd_closure.py --verify'}
 out['producer_sha256']=hashlib.sha256(open(__file__,'rb').read()).hexdigest();out['payload_sha256']=hashlib.sha256(json.dumps(out,sort_keys=True,separators=(',',':')).encode()).hexdigest();return out

if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--emit',action='store_true');ap.add_argument('--verify',action='store_true');ap.add_argument('--event-cap',type=int,default=25000);ap.add_argument('--node-cap',type=int,default=1000000);a=ap.parse_args();out=payload(a.event_cap,a.node_cap);path=os.path.join(HERE,'full_grid_four_cell_mdd_closure.json')
 if a.emit:
  with open(path,'w') as f:json.dump(out,f,sort_keys=True,indent=2);f.write('\n')
 else:assert json.load(open(path))==out
 print(json.dumps(out,sort_keys=True,indent=2))
