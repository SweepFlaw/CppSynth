#include <bits/stdc++.h>
typedef unsigned long long ull;

using namespace std;

int main(){
	ull in,out,n,g,l,b1,b2,sx,sy,ex,ey;
	cin >> in >> out >> n;
	g = __gcd(in,out);
	if(g == 1){
		for(int i = 0 ; i < n ; i ++){
			cout << "YES" << endl;
		}
		return 0;
	}
	b1 = in / g;
	b2 = out / g;
	for(int i = 0 ; i < n ; i ++){
		cin >> sx >> sy >> ex >> ey;
		if(sx == 1){
			sx = (sy-1) / b1;
		}
		else{
			sx = (sy-1) / b2;
		}
		if(sx == 1){
			ex = (ey-1) / b1;
		}
		else{
			ex = (ey-1) / b2;
		}
		if(sx == ex)
			cout << "YES" << endl;
		else
			cout << "NO" << endl;
	}

	return 0;
}