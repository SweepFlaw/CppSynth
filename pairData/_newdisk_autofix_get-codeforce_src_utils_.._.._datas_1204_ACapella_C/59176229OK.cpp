#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

ll rPow(ll n, ll k) {
    if (k <= 0) return 1;
    return n * rPow(n, --k);
}

int dp[110][110];
char a[110][110];
int inf = 110;
int p[1000100];

int main() {
  //  freopen("in.txt", "r", stdin);
    //freopen("outt.txt", "w  ", stdout);
    ios::sync_with_stdio(0);
    cin.tie();
    cout.tie();

    int n;
    cin>>n;
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            cin >> a[i][j];
        }
    }
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            if (a[i][j] == '0') {
                dp[i][j] = inf;
            } else {
                dp[i][j] = 1;
            }
            if (i == j) dp[i][j] = 1;
        }
    }
    int m;
    cin>>m;
    for (int i = 0; i < m; i++)
        cin >> p[i];

    for (int k = 1; k <= n; k++) {
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j]);
                if (dp[i][j] > inf) dp[i][j] = inf;
            }
        }
    }
    int j = 1;
    vector <int> ans;
    ans.push_back(p[0]);
    bool ok = 1;
    for (int i = 0; i < m; i++) {
        while (dp[p[i]][p[j]] == j - i) {
            j++;
            if (j == m) {
                ok = 0;
                break;
            }
        }
        if (ok) {
            ans.push_back(p[j - 1]);
            i = j - 2;
        }
    }
    ans.push_back(p[m - 1]);
    cout << ans.size() << endl;
    for (int i = 0; i < ans.size(); i++) {
        cout << ans[i] << " ";
    }
    cout << endl;



    return 0;
}