#include<bits/stdc++.h>
using namespace std;
int main() {
	long long n,m;
	int q;
	scanf("%lld %lld %d",&n,&m,&q);
	long long gkd=__gcd(n,m);
	long long ngkd=n/gkd;
	long long mgkd=m/gkd;
	while(q--){
		long long ex,ey,sx,sy;
		scanf("%lld %lld %lld %lld",&sx,&sy,&ex,&ey);
		if(sx==1){
			sy=(sy-1)/ngkd;
		}
		else{
			sy=(sy-1)/mgkd;
		}
		if(ey==1){
			ey=(ey-1)/ngkd;
		}
		else{
			ey=(ey-1)/mgkd;
		}
		if(sy==ey){
			printf("YES\n");
		}
		else{
			printf("NO\n");
		}
	}
	return 0;
}