#include <bits/stdc++.h>
#define IOS ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
#define deci fixed<<showpoint<<setprecision //<<deci()<<
#define ll long long
#define mod 1000000007
#define endl "\n"
double pi=acos(-1);
using namespace std;
string s;
int cnt;
int main(){
cin>>s;
int sz=s.length();
bool f=0;
for(int i=0;i<sz-1;i++){
    if(s[i]=='1'){
        f=1;
        break;}
}
if(sz%2 && f)
    cout<<(sz/2) +1;
else
cout<<sz/2;
    return 0;
}
