#include <bits/stdc++.h>
using namespace std;

#define ll long long

ll gcd(ll a, ll b) {
	ll r, s = min(a,b), g = max(a,b);
	r = g%s;
	while(r > 0) {
		g = s; s = r; r = g%s;
	}
	return s;
}

int main() {
	ios_base::sync_with_stdio(false);

	ll n, m, q; cin >> n >> m >> q;
	ll g = gcd(n, m);
	while(q--) {
		ll a1,a2,b1,b2; cin >> a1 >> a2 >> b1 >> b2;
		ll sec1, sec2;
		
		if(a1 == 1) {
			sec1 = a2/(n/g);
			if(a2%(n/g) == 0) sec1--;
		} else {
			sec1 = a2/(m/g);
			if(a2%(n/g) == 0) sec1--;
		}
		if(b1 == 1) {
			sec2 = b2/(n/g);
			if(b2%(n/g) == 0) sec2--;
		} else {
			sec2 = b2/(m/g);
			if(b2%(m/g) == 0) sec2--;
		}
		if(sec1 == sec2) cout << "YES\n";
		else cout << "NO\n";
	}
}