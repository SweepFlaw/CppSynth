#include <bits/stdc++.h>

#define memset(x) memset(x,0,sizeof(x))

#define pb push_back

using namespace std;

int n, m;

int a[1000005], cnt[1005], dist[105][105], used[1005];

vector <int> g[1000005], ans;

queue <int> q;

void check () {
    for (int i = 1;i <= n;i ++) {
        q.push (i);
        memset (used);
        used[i] = true;
        while (!q.empty ()) {
            int v = q.front ();
            q.pop ();
            for (auto to : g[v]) {
                if (!used[to]) {
                    used[to] = true;
                    dist[i][to] = dist[i][v] + 1;
                    q.push (to);
                }
            }
        }
    }
}

void solve (int v, int w) {
    if (v == n) {
        ans.pb (a[v]);
        return;
    }
    int res = dist[ans.back ()][a[v + 1]];
    if (res == v - w) {
        solve (v + 1, w);
    }else {
        ans.pb (a[v]);
        solve (v + 1, v - 1);
    }
}

int main () {
    ios_base::sync_with_stdio(0),cin.tie (0), cout.tie (0);
    cin >> m;
    for (int i = 1;i <= m;i ++) {
        for (int j = 1;j <= m;j ++) {
            char c;
            cin >> c;
            if (c == '1')g[i].pb (j);
        }
    }cin >> n;
    for (int i = 1;i <= n;i ++) {
        cin >> a[i];
    }check ();
    ans.pb (a[1]);
    solve (1, 0);
    cout << ans.size () << endl;
    for (auto it : ans) {
        cout << it << ' ';
    }
}
