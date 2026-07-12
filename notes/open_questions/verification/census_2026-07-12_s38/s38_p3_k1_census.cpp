#include <array>
#include <cstdint>
#include <cstdio>
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

using U = uint64_t;
using Port = std::array<int,2>;
struct Rel { std::array<U,32> succ{}; };

static std::vector<U> states;
static U ALL, FACE, COMP, IMG[28], W[28*28+1];

static void enumerate_states() {
  bool seen[1<<14]{};
  int blocks[7][3];
  for (int i=0;i<7;i++) { blocks[i][0]=2*i; blocks[i][1]=2*i+1; blocks[i][2]=(2*i+2)%14; }
  for (int code=0;code<2187;code++) {
    int q=code; U x=0;
    for (int i=0;i<7;i++) { x |= U(1)<<blocks[i][q%3]; q/=3; }
    bool ok=true;
    for (auto &b:blocks) if (__builtin_popcountll(x&((U(1)<<b[0])|(U(1)<<b[1])|(U(1)<<b[2])))!=1) ok=false;
    if (ok) seen[x]=true;
  }
  for (int x=0;x<(1<<14);x++) if (seen[x]) states.push_back(x);
  ALL=(U(1)<<states.size())-1;
  for (int a=0;a<14;a++) for (size_t s=0;s<states.size();s++) if (states[s]>>a&1) IMG[a]|=U(1)<<s;
  for (int a=0;a<14;a++) IMG[14+a]=ALL^IMG[a];
  U cluster=(U(1)<<0)|(U(1)<<3)|(U(1)<<11);
  for (size_t s=0;s<states.size();s++) if ((states[s]&cluster)==cluster) FACE|=U(1)<<s;
  COMP=ALL^FACE;
  int n=0;
  for (int a=0;a<28;a++) for (int b=0;b<28;b++) if (IMG[a]&~IMG[b]&ALL) W[n++]=IMG[a]&~IMG[b]&ALL;
  W[n]=0;
}

static Rel relation(Port p) {
  Rel r;
  for (size_t s=0;s<states.size();s++) r.succ[s]=(states[s]>>p[0]&1)?IMG[p[1]]:(ALL^IMG[p[1]]);
  return r;
}
static U image(const Rel&r,U m) { U z=0; while(m){int s=__builtin_ctzll(m);m&=m-1;z|=r.succ[s];} return z; }
static U pre(const Rel&r,U m) { U z=0; for(size_t s=0;s<states.size();s++) if(r.succ[s]&m) z|=U(1)<<s; return z; }
static bool orders(U m) { for(int i=0;W[i];i++) if(!(W[i]&m)) return false; return true; }

// stage: 1=face-free failure, 2=face-nonlive failure,
// 3=live-complement order failure, 4=operative.
struct Result { bool operative=false, root=false; int stage=0; };
static Result screen(const std::array<Rel,3>&r,int target) {
  U l1=IMG[target],l0=ALL^l1;
  U e0[3]={l0,l0,l0};
  for (;;) {
    U n[3]; for(int p=0;p<3;p++) n[p]=l0&pre(r[p],e0[(p+1)%3]);
    if(n[0]==e0[0]&&n[1]==e0[1]&&n[2]==e0[2]) break;
    for(int p=0;p<3;p++) e0[p]=n[p];
  }
  U zr[3]={l0,0,0};
  for (;;) {
    U n[3]={zr[0],zr[1],zr[2]};
    for(int p=0;p<3;p++) n[(p+1)%3]|=image(r[p],zr[p])&l0;
    if(n[0]==zr[0]&&n[1]==zr[1]&&n[2]==zr[2]) break;
    for(int p=0;p<3;p++) zr[p]=n[p];
  }
  for(int p=0;p<3;p++) if(((zr[p]&e0[p]&FACE)!=FACE)) return {false,false,1};
  U e1[3]={0,0,0};
  for (;;) {
    U n[3];
    for(int p=0;p<3;p++) n[p]=e1[p]|(l0&pre(r[p],e1[(p+1)%3]))|(l1&pre(r[p],e0[(p+1)%3]));
    if(n[0]==e1[0]&&n[1]==e1[1]&&n[2]==e1[2]) break;
    for(int p=0;p<3;p++) e1[p]=n[p];
  }
  U q[3][2]={{l0,l1},{0,0},{0,0}};
  for (;;) {
    U n[3][2]; for(int p=0;p<3;p++) for(int k=0;k<2;k++) n[p][k]=q[p][k];
    for(int p=0;p<3;p++) {
      int z=(p+1)%3; U im0=image(r[p],q[p][0]),im1=image(r[p],q[p][1]);
      n[z][0]|=im0&l0; n[z][1]|=(im0&l1)|(im1&l0);
    }
    bool same=true; for(int p=0;p<3;p++) for(int k=0;k<2;k++) same&=n[p][k]==q[p][k];
    if(same) break;
    for(int p=0;p<3;p++) for(int k=0;k<2;k++) q[p][k]=n[p][k];
  }
  for(int p=0;p<3;p++) {
    U live=(q[p][0]&pre(r[p],e1[(p+1)%3]))|(q[p][1]&pre(r[p],e0[(p+1)%3]));
    if(live&FACE) return {false,false,2};
    if(!orders(live&COMP)) return {false,false,3};
  }
  return {true,orders(e1[0]),4};
}

static std::string portstr(Port p) { std::ostringstream s; s<<"["<<p[0]<<","<<p[1]<<"]"; return s.str(); }
int main(int argc,char**argv) {
  enumerate_states();
  if(states.size()!=29) { std::cerr<<"state anchor failure\n"; return 2; }
  std::vector<Port> ps; std::vector<Rel> rs;
  for(int a=0;a<14;a++) for(int b=0;b<14;b++) { ps.push_back({a,b}); rs.push_back(relation({a,b})); }
  long start=0,end=196; std::string path="s38_p3_k1_checkpoint.json";
  for(int i=1;i<argc;i++){std::string a=argv[i];if(a=="--start")start=std::stol(argv[++i]);else if(a=="--end")end=std::stol(argv[++i]);else if(a=="--checkpoint")path=argv[++i];}
  long long triples=0,op[3]={0},root[3]={0},fail[3][3]{}; int targets[3]={1,2,4}; std::vector<std::string> surv;
  auto save=[&](long done){std::string tmp=path+".tmp";std::ofstream f(tmp);f<<"{\n  \"schema\": 1,\n  \"scope\": \"7-loop C={a0,a3,a11}, period 3, k=1\",\n  \"ports\": 196,\n  \"start\": "<<start<<",\n  \"end\": "<<end<<",\n  \"completed_first_ports\": "<<done<<",\n  \"screened_triples\": "<<triples<<",\n  \"targets\": {\n";for(int k=0;k<3;k++)f<<"    \""<<targets[k]<<"\": {\"face_free_fail\": "<<fail[k][0]<<", \"face_nonlive_fail\": "<<fail[k][1]<<", \"complement_order_fail\": "<<fail[k][2]<<", \"operative\": "<<op[k]<<", \"root_order\": "<<root[k]<<"}"<<(k<2?",":"")<<"\n";f<<"  },\n  \"survivors\": [";for(size_t i=0;i<surv.size();i++)f<<(i?",\n    ":"\n    ")<<surv[i];f<<(surv.empty()?"":"\n  ")<<"]\n}\n";f.close();std::rename(tmp.c_str(),path.c_str());};
  for(long i=start;i<end;i++) {
    for(int j=0;j<196;j++) for(int h=0;h<196;h++) {
      triples++;
      std::array<Rel,3> rr{rs[i],rs[j],rs[h]};
      for(int k=0;k<3;k++){auto x=screen(rr,targets[k]);if(!x.operative)fail[k][x.stage-1]++;else{op[k]++;if(x.root){root[k]++;std::ostringstream z;z<<"{\"target\":"<<targets[k]<<",\"p0\":"<<portstr(ps[i])<<",\"p1\":"<<portstr(ps[j])<<",\"p2\":"<<portstr(ps[h])<<"}";surv.push_back(z.str());}}}
    }
    if((i-start+1)%4==0){save(i+1);std::cerr<<"first="<<i+1<<"/"<<end<<" op="<<op[0]<<","<<op[1]<<","<<op[2]<<" root="<<root[0]<<","<<root[1]<<","<<root[2]<<"\n";}
  }
  save(end); return 0;
}
