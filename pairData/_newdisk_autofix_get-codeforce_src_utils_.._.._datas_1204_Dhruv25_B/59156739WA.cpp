#include<bits/stdc++.h>
using namespace std;
int main()
{
	long long int n,l,r;
	cin>>n>>l>>r;
	long long int y=pow(2,l-1);
	long long int s=pow(2,r-1);
	long long int q=n-l;
	long long int x=q;
	for(long long int i=0;i<l;++i)
	{
		x+=pow(2,i);
	}
	cout<<x<<" ";
	x=0;
	long long int a=n-r;
	x=a*y;
	for(long long int i=0;i<r;++i)
	{
		x+=pow(2,i);
	}
	cout<<x;
	
	
	
	
	
	
}