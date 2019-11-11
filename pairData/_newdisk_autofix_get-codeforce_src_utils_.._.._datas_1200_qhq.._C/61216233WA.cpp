#include<bits/stdc++.h>
#define ll long long
using namespace std;
const int maxn=2e5+5;
ll gcd(ll x,ll y)
{
    return y==0?x:gcd(y,x%y);
}
int main()
{
    ll n,m,q;
    scanf("%lld%lld%lld",&n,&m,&q);
    ll gd=gcd(n,m);
    ll a1=n/gd;
    ll b1=m/gd;
    while(q--)
    {
        ll x1,x2,y1,y2;
        ll z1,z2;
        scanf("%lld%lld%lld%lld",&x1,&y1,&x2,&y2);
        y1--;y2--;
        if(x1==1){
            z1=y1/a1;
        }
        else{
            z1=y2/b1;
        }
        if(x2==1){
            z2=y2/a1;
        }
        else{
            z2=y2/b1;
        }
        if(z1==z2){
            cout<<"YES"<<endl;
        }
        else{
            cout<<"NO"<<endl;
        }
    }
    return 0;
}
