#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <unordered_map>
#include <queue>
#include <deque>
#include <cmath>
#include <math.h>
#include <string>
#include <time.h>
#include <random>
#include <memory.h>
#include <bitset>
using namespace std;

#define FILE0
#define MAGIC0
mt19937 rnd(time(0)); //rnd()

#define ll long long
#define pii pair<int, int>
#define pll pair<ll, ll>
#define mii map<int, int>
#define mll map<ll, ll>
#define msl map<string, ll>
#define mls map<ll, string>
#define MOD (1000000007ll)
#define MOD2 (1000000009ll)
#define BIGMOD (1000000000000000007ll)
#define RMOD int(5e8 + rnd() % (int) 5e8)
#define fast ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);

#ifdef FILE1
ifstream in("input.txt");
ofstream out("output.txt");
#endif
#ifdef MAGIC1
#pragma GCC optimize("Ofast")
#pragma GCC target("sse,sse2,sse3,ssse3,sse4,popcnt,abm,mmx,avx,tune=native")
#pragma GCC optimize("unroll-loops")
#endif

bool isPrime(ll a)
{
	ll i;
	for (i = 2; i*i <= a; i++)
	{
		if (a%i == 0)
		{
			return 0;
		}
	}
	return (a != 1);
}

bool isPalindrom(const string &s, int l, int r)
{
	for (int i = 0; i < (r - l + 1) / 2; i++)
	{
		if (s[l + i] != s[r - i])
		{
			return 0;
		}
	}
	return 1;
}

template <class type1> type1 gcd(type1 a, type1 b)
{
	type1 t;
	while (b)
	{
		t = b;
		b = a%b;
		a = t;
	}
	return a;
}

ll positiveMod(ll v, ll md)
{
	v = v%md;
	if (v < 0)
	{
		v += md;
	}
	return v;
}

//-----------------------------------------------------end--------------------------------------//



int main()
{
	fast;
	
	ll i, j, q, n, m, g, t1, v1, t2, v2, a, b;

	cin >> n >> m >> q;

	g = gcd(n, m);
	a = n / g;
	b = m / g;

	for (i = 0; i < n; i++)
	{
		cin >> t1 >> v1 >> t2 >> v2;

		if (t1 == 2 && t2 == 1)
		{
			swap(t1, t2);
			swap(v1, v2);
		}

		if (t1 == 1 && t2 == 1)
		{
			if ((v1-1) / a == (v2-1) / a)
			{
				cout << "YES\n";
			}
			else
			{
				cout << "NO\n";
			}
		}

		if (t1 == 2 && t2 == 2)
		{
			if ((v1 - 1) / b == (v2 - 1) / b)
			{
				cout << "YES\n";
			}
			else
			{
				cout << "NO\n";
			}
		}

		if (t1 == 1 && t2 == 2)
		{
			if ((v1-1)/a == (v2-1)/b)
			{
				cout << "YES\n";
			}
			else
			{
				cout << "NO\n";
			}
		}
	}


	return 0;
}