#include<bits/stdc++.h>
using namespace std;
int main(){
	int n,l,r;
	cin>>n>>l>>r;
//	int k=1;
//	long long s=0;
//	int kk=1;
//	for(int i=1;i<=n;i++){
//		s+=k;
//		if(kk<r)kk++,k<<=1;
//	}
	cout<<pow(2,l)-1+n-l<<' '<<pow(2,r-1)*(n-r+2)-1<<endl;
}