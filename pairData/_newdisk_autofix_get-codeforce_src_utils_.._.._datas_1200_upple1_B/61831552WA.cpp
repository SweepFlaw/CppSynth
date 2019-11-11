#include <bits/stdc++.h>
#pragma GCC optimize ("Ofast")
#pragma GCC optimize ("unroll-loops")
#define rep(i, a, b) for(int i=a; i<=b; i++)
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef tuple<int, int, int> tiii;
const int INF=0x3f3f3f3f;
const ll INFL=0x3f3f3f3f3f3f3f3fLL;
const int dy[]={0, 1, 0, -1};
const int dx[]={1, 0, -1, 0};
const int MOD=1e9+7;
int GCD(int a, int b) {int t=b;while(a){b=a; a=t%a; t=b;} return b;}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int t;
    cin>>t;
    while(t--)
    {
        int n, m, k;
        cin>>n>>m>>k;

        int a;
        cin>>a;

        bool chk=true;
        for(int i=1; i<n; i++)
        {
            int b;
            cin>>b;
            if(b-k>a)
            {
                int x=b-k-a;
                if(x>m) 
                {
                    chk=false;
                }
                m-=x;
            }
            else
            {
                int x=max(a, a-b+k);
                m+=x;
            }
            
            a=b;
        }

        if(chk) 
        {
            cout<<"YES\n";
        }
        else cout<<"NO\n";
    }
}