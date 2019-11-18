#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;

#define pb push_back
#define mp(x,y) make_pair(x,y)
#define scd(n) scanf("%d",&n)
#define sclf(n) scanf("%lf",&n)
#define scl(n) scanf("%lld",&n)
#define repi(a,b,c) for(int i=a;i<b;i+=c)
#define repis(a,b,c) for(int i=a-1;i>=b;i-=c)
#define repj(a,b,c) for(int j=a;j<b;j+=c)
#define repjs(a,b,c) for(int j=a-1;j>=b;j-=c)
#define repk(a,b,c) for(int k=a;k<b;k+=c)
#define repks(a,b,c) for(int k=a-1;k>=0;k-=c)
#define fi first
#define se second

/*
 fast I/O

ios::sync_with_stdio(0);
cin.tie();

 freeopen

 freopen("input.txt","r",stdin);
 freopen("output.txt","w",stdout);
 */

typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
const int mx = 2e5+100;
const int md = 1000000007;

priority_queue < int, vector < int >, greater<int> > pq;

bool compare(pii &a, pii &b) {
    return a.fi > b.fi;
}

int main() {
    ll n,m,q,div;
    scanf("%lld %lld %lld",&n,&m,&q);
    div = __gcd(n,m);
    n /= div;
    m /= div;
    while(q--) {
        ll x,y,a,b;
        scanf("%lld %lld %lld %lld",&x,&y,&a,&b);
        y--;
        b--;
        if(x == 1) {
            y /= n;
        } else {
            y /= m;
        }

        if(a == 1) {
            b /= n;
        } else {
            b /= m;
        }
        printf("%s\n",y == b ? "YES" : "NO");
    }
}
