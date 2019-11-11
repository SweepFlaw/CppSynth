#include <bits/stdc++.h>
using namespace std;

using ll=long long;

int main()
{
    int t;
    cin>>t;
    
    while(t--)
    {
        ll n,m,k;
        cin>>n>>m>>k;
        
        vector<ll> h;
        
        for(int i=0; i<n; i++)
        {
            ll h1;
            cin>>h1;
            h.push_back(h1);
        }
        
        bool w=1;
        
        for(int i=1; i<n; i++)
        {
            if(h[i]>h[i-1])
            {
                m -= max(0LL, h[i] - (h[i-1]+k));
            }
            
            else
            {
                m += h[i-1] - max(0LL,h[i]-k);
            }
            
            if(m<0) w=0;
        }
        
        cout << (w ? "YES" : "NO") << endl;
    }
}