#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <vector>
using namespace std;

static bool graphical(vector<int> x) {
    const int m=(int)x.size();
    long long sum=accumulate(x.begin(),x.end(),0LL);
    if(sum&1) return false;
    sort(x.begin(),x.end(),greater<int>());
    for(int d:x) if(d<0||d>=m) return false;
    long long pref=0;
    for(int k=1;k<=m;k++){
        pref+=x[k-1];
        long long rhs=1LL*k*(k-1);
        for(int i=k;i<m;i++) rhs+=min(k,x[i]);
        if(pref>rhs) return false;
    }
    return true;
}

static long long deficit(const vector<int>& w,const vector<int>& S,int k){
    vector<char> sel(w.size(),0); for(int i:S)sel[i]=1;
    long long d=1LL*k*(k-1);
    for(int i=0;i<(int)w.size();i++) d+=sel[i]?-w[i]:min(k,w[i]);
    return d;
}

static bool source_star(int n,const vector<pair<int,int>>& E,const array<int,7>& deg){
    vector<int>a;for(int v=0;v<n;v++)if(deg[v])a.push_back(v);
    if(a.size()<2||E.size()!=a.size()-1)return false;
    vector<int> ds;for(int v:a)ds.push_back(deg[v]);
    sort(ds.begin(),ds.end(),greater<int>());
    if(ds[0]!=(int)a.size()-1)return false;
    for(size_t i=1;i<ds.size();i++)if(ds[i]!=1)return false;
    return true;
}

static bool subdivided_case(int n,const vector<pair<int,int>>& E,const array<int,7>& deg,const vector<int>&S,int k){
    vector<int>a;for(int v=0;v<n;v++)if(deg[v])a.push_back(v);
    if((int)a.size()!=k+3||(int)E.size()!=k+2)return false;
    int c=-1,m=-1;vector<int> leaves;
    for(int v:a){if(deg[v]==k+1){if(c!=-1)return false;c=v;}else if(deg[v]==2){if(m!=-1)return false;m=v;}else if(deg[v]==1)leaves.push_back(v);else return false;}
    if(c<0||m<0||(int)leaves.size()!=k+1)return false;
    auto has=[&](int x,int y){if(x>y)swap(x,y);return find(E.begin(),E.end(),make_pair(x,y))!=E.end();};
    if(!has(c,m))return false;
    int midleaf=0;vector<int> direct_idx;
    for(int x:leaves){if(has(m,x))midleaf++;if(has(c,x)){for(int i=0;i<(int)E.size();i++){auto [u,v]=E[i];if((u==min(c,x)&&v==max(c,x)))direct_idx.push_back(i);}}}
    if(midleaf!=1||(int)direct_idx.size()!=k)return false;
    vector<int>T=S,D=direct_idx;sort(T.begin(),T.end());sort(D.begin(),D.end());return T==D;
}

int main(){
    constexpr int n=7;vector<pair<int,int>> pairs;
    for(int u=0;u<n;u++)for(int v=u+1;v<n;v++)pairs.push_back({u,v});
    uint64_t total=1ULL<<pairs.size();
    uint64_t li=0,one=0,threshold_sets=0,equalities=0,r0=0;
    long long minD=1LL<<60;
    for(uint64_t mask=0;mask<total;mask++){
        array<int,7> deg{};vector<pair<int,int>> E;E.reserve(21);
        for(int i=0;i<21;i++)if(mask>>i&1ULL){auto [u,v]=pairs[i];deg[u]++;deg[v]++;E.push_back({u,v});}
        vector<int>w;w.reserve(E.size());int zeros=0;
        for(auto [u,v]:E){int x=abs(deg[u]-deg[v]);w.push_back(x);zeros+=x==0;}
        if(zeros<=1){one++;if(!graphical(w)){cerr<<"ONE_ZERO_FAIL mask="<<mask<<"\n";return 2;}if(zeros==1&&E.size()==1){if(w[0]!=0){return 3;}r0++;}}
        if(zeros!=0||E.empty())continue;
        li++;
        if(!graphical(w)){cerr<<"FINAL_FAIL mask="<<mask<<"\n";return 4;}
        for(int k=1;k<=(int)E.size();k++){
            vector<int> elig;for(int i=0;i<(int)w.size();i++)if(w[i]>=k)elig.push_back(i);
            if((int)elig.size()<k)continue;
            vector<int>S;
            auto rec=[&](auto&&self,int pos,int need)->bool{
                if(need==0){threshold_sets++;long long D=deficit(w,S,k);minD=min(minD,D);if(D<0){cerr<<"THRESHOLD_FAIL mask="<<mask<<" k="<<k<<" D="<<D<<"\n";return false;}if(D==0){equalities++;bool ok=(k==1?source_star(n,E,deg):(source_star(n,E,deg)||subdivided_case(n,E,deg,S,k)));if(!ok){cerr<<"EQUALITY_FAIL mask="<<mask<<" k="<<k<<"\n";return false;}}return true;}
                if((int)elig.size()-pos<need)return true;
                S.push_back(elig[pos]);if(!self(self,pos+1,need-1))return false;S.pop_back();
                if(!self(self,pos+1,need)) return false;
                return true;
            };
            if(!rec(rec,0,k))return 5;
        }
    }
    cout<<"ALL_N7_CHECKS_PASS\n";
    cout<<"graphs "<<total<<" locally_irregular_nonempty "<<li<<" at_most_one_zero "<<one
        <<" threshold_sets "<<threshold_sets<<" equality_sets "<<equalities
        <<" r0_repairs "<<r0<<" min_threshold_deficit "<<minD<<"\n";
}
