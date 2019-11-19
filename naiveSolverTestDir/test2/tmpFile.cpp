#include <bits/stdc++.h>
using namespace std;
long long n,m,sum,x,y,z;
bool ok;
int main ()
{
	cin >> n;
	string s;
	int a[10];
	for(int i = 0;i < 10;++i){
		a[i] = 0;
	}
	cin >> s;
	for(int i = 0;i < s.size();++i){
		if(s[i] == 'L'){
			for(int j = 0;j < 10;++j){
				if(a[j] == 0){
					a[j] = 1;
					break;
				}
			}
		}
		else if(s[i] == 'R'){
			for(int j = 9;j >= 0;--j){
				if(a[j] == 0){
					a[j] = 1;
					break;
				}
			}
		}
		else{
			x = s[i] - '0';
			a[x] = 0;
		}
	}
	for(int i = 0;i < 10;++i){
		cout << a[i];
	}
}