/***************************************************************************************************************************
****************************************************************************************************************************
****************************************************************************************************************************
CODE BY:-
		
		BLACKHATGEEK
		Student @ NIT KURUKSHETRA
		
		" BREAK THE CONSTRAINTS :P "
		
*****************************************************************************************************************************
*****************************************************************************************************************************
*****************************************************************************************************************************/
#include<bits/stdc++.h>
using namespace std;
#define ll long long int
#define pb push_back
#define mp make_pair
#define F first
#define S second
#define r0 return 0;
#define f(k,i,n,j) for(ll k=i;k<=n;k=k+j)
#define cin(a) cin>>a;
#define loop while(t--)
#define vi vector<int>
#define vii vector<long long int>
#define SORT(v) sort(v.begin(),v.end());
ll diff(ll x,ll y)
{
	if(x>y)
	{
		return x-y;
	}
	else
	{
		return y-x;
	}
}
bool prime[10];
void SieveOfEratosthenes(int n) 
{ 
    
    memset(prime, true, sizeof(prime)); 
  
    for (int p=2; p*p<=n; p++) 
    { 
      
        if (prime[p] == true) 
        { 
            
            for (int i=p*p; i<=n; i += p) 
                prime[i] = false; 
        } 
    } 
}
bool isvowel(char c)
{
	if(c=='a'||c=='A'||c=='E'||c=='e'||c=='I'||c=='i'||c=='O'||c=='o'||c=='U'||c=='u')
	{
		return true;
	}
	else
	{
		return false;
	}
}
int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	ll n,l,r;
	cin>>n>>l>>r;
	ll lsum=0;
	ll rsum=0;
	lsum=(1<<l)-1+(n-l);
	rsum=(1<<r)-1+(n-r)*(1<<(r-1));
	cout<<lsum<<" "<<rsum;
	r0
	
	
}
