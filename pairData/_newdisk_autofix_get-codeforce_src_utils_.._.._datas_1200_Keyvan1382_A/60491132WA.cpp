#include <bits/stdc++.h>

using namespace std;

string s;
long long n = 0 , a[10];
int main()
{
	cin >> n >> s;
	for (int i = 0; i < n; i++)
	{
		if (s[i] == 'L')
		{
			for (int j = 0; i < 10; j++)
			{
				if (a[j] == 0)
				{
					a[j] += 1;
					break;
				}
			}
		}
		else if (s[i] == 'R')
		{
			for (int j = 9; j > -1; j--)
			{
				if (a[j] == 0)
				{
					a[j] += 1;
					break;
				}
			}
		}
		else
		{
			a[int(s[i]-'0')] -= 0;
		}
	}
	for (int i = 0; i < 10; i++)
	{
		cout << a[i];
	}
	return 0;
}
