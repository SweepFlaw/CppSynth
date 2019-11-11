#include <bits/stdc++.h>
using namespace std;

const int N = 1e2 + 7, M = 1e6 + 7;;
int n, m;
int S[N][N], dp[M], arr[M], pref[M], lastSeen[N], from[M];
vector<int> seq;

int main() {
  ios::sync_with_stdio(0);
  cin.tie(0); cout.tie(0);

  cin >> n;
  for (int i = 0; i < n; ++i) {
    string str;
    cin >> str;
    for (int j = 0; j < n; ++j) {
      if (str[j] == '1') {
        S[i][j] = 1;
      }
      else if (i == j) {
        S[i][j] = 0;
      }
      else {
        S[i][j] = INT_MAX;
      }
    }
  }
  for (int i = 0; i < n; ++i) {
    for (int j = 0; j < n; ++j) {
      for (int k = 0; k < n; ++k) {
        if (S[j][i] == INT_MAX || S[i][k] == INT_MAX) {
          continue;
        }
        S[j][k] = min(S[j][k], S[j][i] + S[i][k]);
      }
    }
  }
  cin >> m;
  for (int i = 0; i < m; ++i) {
    cin >> arr[i];
    arr[i]--;
  }
  dp[0] = 1;
  from[0] = -1;
  fill(lastSeen, lastSeen + n, -1);
  lastSeen[arr[0]] = 0;
  for (int i = 1; i < m; ++i) {
    dp[i] = INT_MAX;
    for (int j = 0; j < n; ++j) {
      if (arr[i] == j) {
        continue;
      }
      if (lastSeen[j] == -1 || i - lastSeen[j] != S[j][arr[i]]) {
        continue;
      }
      if (dp[lastSeen[j]] + 1 < dp[i]) {
        dp[i] = dp[lastSeen[j]] + 1;
        from[i] = lastSeen[j];
      }
    }
    lastSeen[arr[i]] = i;
  }
  int act = m - 1;
  while (act != -1) {
    seq.push_back(act);
    act = from[act];
  }
  reverse(seq.begin(), seq.end());
  cout << seq.size() << "\n";
  for (auto i : seq) {
    cout << arr[i] + 1 << " ";
  }
  cout << "\n";

  return 0;
}
