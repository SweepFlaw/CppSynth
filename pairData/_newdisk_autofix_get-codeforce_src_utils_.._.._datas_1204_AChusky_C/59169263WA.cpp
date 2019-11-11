#include<bits/stdc++.h>
using namespace std;
const int maxn=100+5;
const int maxm=1e6+5;
const int inf=1e9;
int n,m;
int p[maxn];
int d[maxn][maxn];
vector<int> v;
int main(void){
	// freopen("in.in","r",stdin);
	scanf("%d",&n);
	for(int i=1;i<=n;i++){
		for(int j=1;j<=n;j++){
			scanf("%1d",&d[i][j]);
			if(d[i][j]==0) d[i][j]=inf;
		}
	}
	scanf("%d",&m);
	for(int i=1;i<=m;i++){
		scanf("%d",&p[i]);
	}
	for(int k=1;k<=n;k++){
		for(int i=1;i<=n;i++){
			for(int j=1;j<=n;j++){
				d[i][j]=min(d[i][j],d[i][k]+d[k][j]);
			}
		}
	}
	v.push_back(p[1]);
	int pre=p[1];
	// cout<<d[4][3]+d[3][4]<<' '<<d[4][4]<<endl;
	// cout<<d[3][3]<<' '<<d[3][1]<<' '<<d[1][3]<<endl;
	for(int i=2;i<m;i++){
		// cout<<i<<' '<<pre<<' '<<d[pre][i]+d[i][i+1]<<' '<<d[pre][i+1]<<endl;
		if(d[pre][p[i]]+d[p[i]][p[i+1]]!=d[pre][p[i+1]]||pre==p[i+1]){
			pre=p[i];
			v.push_back(p[i]);
		}
	}
	v.push_back(p[m]);
	int sz=v.size();
	printf("%d\n",sz);
	for(int i=0;i<sz;i++){
		printf("%d%c",v[i]," \n"[i==sz-1]);
	}
	return 0;
}