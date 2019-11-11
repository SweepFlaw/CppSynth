#include <bits/stdc++.h>
using namespace std;

#define ll long long int
#define N 2000000

ll a[N];

int main()
{
    string s;
    cin >> s;

    int power = 0, val = 0;
    for(int i=s.length()-1; i>=0; i--)
    {
        if(s[i] == '1')
            val += pow(2,power);

        power++;
    }

    double ans = log(val) / log(4);
    cout << ceil(ans);
    return 0;
}