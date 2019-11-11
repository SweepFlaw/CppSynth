#include <bits/stdc++.h>
using namespace std;

#define ll long long int
#define N 2000000

int main()
{
    string s;
    cin >> s;

    int flag = 0;
    for(int i=s.length()-1; i>=1; i--)
        if(s[i] - '0')
        {
            flag = 1;
            break;
        }

    if(!flag && s.length()%2)
    {
        cout << s.length()/2;
        return 0;
    }

    cout << (s.length() + 1)/2;
    return 0;
} 