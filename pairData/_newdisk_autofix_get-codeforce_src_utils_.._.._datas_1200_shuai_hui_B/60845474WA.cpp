#include<bits/stdc++.h>
using namespace std;
#define ll long long
ll a[110];
int main(){
    int _;scanf("%d",&_);
    while(_--){
        int n,m;
        ll k;
        scanf("%d%d%lld",&n,&m,&k);
        for(int i=1;i<=n;i++)
            scanf("%lld",&a[i]);
        ll now=m;
        int L=1;
        bool fa=1;
        for(int i=1;i<n;i++){
            now+=a[i];
            now-=max(a[i+1]-k,1ll*0);
            if(m<0){
                fa=0;break;
            }
        }
        if(fa) puts("YES");
        else puts("NO");
    }
    return 0;
}
