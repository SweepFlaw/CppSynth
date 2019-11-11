#include <bits/stdc++.h>
using namespace std;

int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);

  int tc;
  cin >> tc;
  while (tc--) {
    int n, m, k;
    cin >> n >> m >> k;
    int ar[n];
    for (int i = 0; i < n; i++) {
      cin >> ar[i];
    }

    for (int i = 0; i < n - 1; i++) {
      int x = max(0, ar[i + 1] - k);
      if (ar[i] >= ar[i + 1]) {
        m += ar[i] - k;
      } else if (x - ar[i] <= m) {
        m -= x - ar[i];
      } else {
        m = -1;
        break;
      }
    }

    if (m >= 0) cout << "YES" << '\n';
    else cout << "NO" << '\n';
  }
  return 0;
}