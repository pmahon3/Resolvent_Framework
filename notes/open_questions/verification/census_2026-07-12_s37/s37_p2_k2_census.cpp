#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <tuple>
#include <vector>

using U = uint64_t;
using Port = std::array<int,4>; // old0,new0,old1,new1
static std::vector<U> states;
static U ALL, FACE, COMP, IMG[28], W[28*28];

static void enumerate_states() {
  std::set<U> out;
  int blocks[7][3];
  for(int i=0;i<7;i++){ blocks[i][0]=2*i; blocks[i][1]=2*i+1; blocks[i][2]=(2*i+2)%14; }
  for(int code=0;code<2187;code++){
    int q=code; U x=0; for(int i=0;i<7;i++){ x|=U(1)<<blocks[i][q%3]; q/=3; }
    bool ok=true; for(auto &b:blocks) if(__builtin_popcountll(x & ((U(1)<<b[0])|(U(1)<<b[1])|(U(1)<<b[2])))!=1) ok=false;
    if(ok) out.insert(x);
  }
  states.assign(out.begin(),out.end());
  ALL=(U(1)<<states.size())-1;
  for(int a=0;a<14;a++) for(size_t s=0;s<states.size();s++) if(states[s]>>a&1) IMG[a]|=U(1)<<s;
  for(int a=0;a<14;a++) IMG[14+a]=ALL^IMG[a];
  FACE=0; for(size_t s=0;s<states.size();s++) if((states[s]&((U(1)<<0)|(U(1)<<3)|(U(1)<<11)))==((U(1)<<0)|(U(1)<<3)|(U(1)<<11))) FACE|=U(1)<<s;
  COMP=ALL^FACE;
  int n=0; for(int a=0;a<28;a++) for(int b=0;b<28;b++) if(IMG[a]&~IMG[b]&ALL) W[n++]=IMG[a]&~IMG[b]&ALL;
  W[n]=0;
}

struct Rel { std::array<U,32> succ{}; };
static Rel relation(const Port&p){ Rel r; for(size_t s=0;s<states.size();s++){ U z=ALL; for(int j=0;j<2;j++){int a=p[2*j],b=p[2*j+1]; U wanted=(states[s]>>a)&1; U m=IMG[b]; z &= wanted?m:(ALL^m);} r.succ[s]=z;} return r; }
static U image(const Rel&r,U m){U z=0; while(m){int s=__builtin_ctzll(m);m&=m-1;z|=r.succ[s];}return z;}
static U pre(const Rel&r,U m){U z=0;for(size_t s=0;s<states.size();s++)if(r.succ[s]&m)z|=U(1)<<s;return z;}

// Exact two-cell girth validity was independently established as 9,408 ports.
// For width two it is equivalent to requiring distinct endpoints and no pair
// of source/target atoms to lie together in a block (the table is checked at startup).
static bool two_cell_ok(const Port&p){
  int par[28];std::iota(par,par+28,0);auto root=[&](int x){while(par[x]!=x){par[x]=par[par[x]];x=par[x];}return x;};
  for(int j=0;j<2;j++){int x=root(p[2*j]),y=root(14+p[2*j+1]);if(x!=y)par[x]=y;}
  std::array<std::array<int,3>,14> bs;for(int cell=0;cell<2;cell++)for(int i=0;i<7;i++){bs[7*cell+i]={root(14*cell+2*i),root(14*cell+2*i+1),root(14*cell+(2*i+2)%14)};auto q=bs[7*cell+i];if(q[0]==q[1]||q[0]==q[2]||q[1]==q[2])return false;}
  // BFS in the atom/block incidence graph; incidence cycles of length <10
  // are exactly Berge cycles of length <5.
  for(int a=0;a<28;a++)if(root(a)==a){std::array<int,42>d,pa;d.fill(-1);pa.fill(-1);d[a]=0;std::vector<int>q{a};for(size_t h=0;h<q.size();h++){int v=q[h];std::vector<int> nb;if(v<28){for(int b=0;b<14;b++)if(bs[b][0]==v||bs[b][1]==v||bs[b][2]==v)nb.push_back(28+b);}else for(int x:bs[v-28])nb.push_back(x);for(int w:nb){if(w==pa[v])continue;if(d[w]>=0){if(d[v]+d[w]+1<10)return false;}else{d[w]=d[v]+1;pa[w]=v;q.push_back(w);}}}}
  return true;
}
static std::vector<Port> ports(){std::vector<Port> v;for(int a=0;a<14;a++)for(int b=a+1;b<14;b++)for(int c=0;c<14;c++)for(int d=c+1;d<14;d++)for(int sw=0;sw<2;sw++){Port p{a,sw?d:c,b,sw?c:d};if(two_cell_ok(p))v.push_back(p);}return v;}

struct Result {bool operative=false, root=false; U live0=0,live1=0,e10=0,e11=0,free0=0,free1=0;};
static bool orders(U m){for(int i=0;W[i];i++)if(!(W[i]&m))return false;return true;}
static Result screen(const Rel&r0,const Rel&r1,int target){
  U l1=IMG[target],l0=ALL^l1,e0[2]={l0,l0};
  for(;;){U a=l0&pre(r0,e0[1]),b=l0&pre(r1,e0[0]);if(a==e0[0]&&b==e0[1])break;e0[0]=a;e0[1]=b;}
  U zr[2]={l0,0}; for(;;){U a=zr[0]|(image(r1,zr[1])&l0),b=zr[1]|(image(r0,zr[0])&l0);if(a==zr[0]&&b==zr[1])break;zr[0]=a;zr[1]=b;}
  Result o;o.free0=zr[0]&e0[0];o.free1=zr[1]&e0[1];if((o.free0&FACE)!=FACE||(o.free1&FACE)!=FACE)return o;
  U e1[2]={0,0};for(;;){U a=(l0&pre(r0,e1[1]))|(l1&pre(r0,e0[1]));U b=(l0&pre(r1,e1[0]))|(l1&pre(r1,e0[0]));a|=e1[0];b|=e1[1];if(a==e1[0]&&b==e1[1])break;e1[0]=a;e1[1]=b;}
  o.e10=e1[0];o.e11=e1[1];
  // Rooted reachability by phase and number of ones so far.
  U q[2][2]={{l0,l1},{0,0}};for(;;){U n00=q[0][0]|(image(r1,q[1][0])&l0);U n01=q[0][1]|(image(r1,q[1][0])&l1)|(image(r1,q[1][1])&l0);U n10=q[1][0]|(image(r0,q[0][0])&l0);U n11=q[1][1]|(image(r0,q[0][0])&l1)|(image(r0,q[0][1])&l0);if(n00==q[0][0]&&n01==q[0][1]&&n10==q[1][0]&&n11==q[1][1])break;q[0][0]=n00;q[0][1]=n01;q[1][0]=n10;q[1][1]=n11;}
  o.live0=(q[0][0]&pre(r0,e1[1]))|(q[0][1]&pre(r0,e0[1]));o.live1=(q[1][0]&pre(r1,e1[0]))|(q[1][1]&pre(r1,e0[0]));
  o.operative=!(o.live0&FACE)&&!(o.live1&FACE)&&orders(o.live0&COMP)&&orders(o.live1&COMP);
  o.root=orders(e1[0]); return o;
}

static std::string portstr(const Port&p){std::ostringstream s;s<<"[["<<p[0]<<","<<p[1]<<"],["<<p[2]<<","<<p[3]<<"]]";return s.str();}
int main(int argc,char**argv){
  enumerate_states(); auto ps=ports(); if(states.size()!=29||ps.size()!=9408){std::cerr<<"anchor failure states="<<states.size()<<" ports="<<ps.size()<<"\n";return 2;}
  std::vector<Rel> rs;rs.reserve(ps.size());for(auto&p:ps)rs.push_back(relation(p));
  long start=0,end=ps.size();std::string path="s37_p2_k2_checkpoint.json";for(int i=1;i<argc;i++){std::string a=argv[i];if(a=="--start")start=std::stol(argv[++i]);else if(a=="--end")end=std::stol(argv[++i]);else if(a=="--checkpoint")path=argv[++i];}
  long long screened=0,op[3]={0},root[3]={0};std::vector<std::string> surv;int targets[3]={1,2,4};
  auto save=[&](long done){std::string tmp=path+".tmp";std::ofstream f(tmp);f<<"{\n  \"schema\": 1,\n  \"scope\": \"7-loop C={a0,a3,a11}, period 2, k=2\",\n  \"ports\": 9408,\n  \"start\": "<<start<<",\n  \"end\": "<<end<<",\n  \"completed_first_ports\": "<<done<<",\n  \"screened_pairs\": "<<screened<<",\n  \"targets\": {\n";for(int k=0;k<3;k++)f<<"    \""<<targets[k]<<"\": {\"operative\": "<<op[k]<<", \"root_order\": "<<root[k]<<"}"<<(k<2?",":"")<<"\n";f<<"  },\n  \"survivors\": [";for(size_t i=0;i<surv.size();i++)f<<(i?",\n    ":"\n    ")<<surv[i];f<<(surv.empty()?"":"\n  ")<<"]\n}\n";f.close();std::rename(tmp.c_str(),path.c_str());};
  for(long i=start;i<end;i++){for(size_t j=0;j<ps.size();j++){screened++;for(int k=0;k<3;k++){auto x=screen(rs[i],rs[j],targets[k]);if(x.operative){op[k]++;if(x.root)root[k]++;std::ostringstream z;z<<"{\"target\":"<<targets[k]<<",\"p0\":"<<portstr(ps[i])<<",\"p1\":"<<portstr(ps[j])<<",\"root_order\":"<<(x.root?"true":"false")<<"}";surv.push_back(z.str());}}}if((i-start+1)%8==0){save(i+1);std::cerr<<"first="<<i+1<<"/"<<end<<" op="<<op[0]<<","<<op[1]<<","<<op[2]<<"\n";}}
  save(end);return 0;
}
