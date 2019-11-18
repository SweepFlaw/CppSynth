#include<bits/stdc++.h>

using namespace std;

const long long MAXN = 5005;
const long long INF = 0x7f3f3f3f;
const long long LINF = 0x1f3f3f3f3f3f3f3f;
const long long MOD = 998244353;
const long long OVER_FLOW = 0xffffffff;

long long n, m; /**< n个数,m个操作,以model为模 */
string str[MAXN];
long long dp[MAXN][MAXN];

void add(long long l1, long long r1, long long l2, long long r2) {
    dp[l1][l2]++, dp[l1][r1 + 1]--, dp[r1 + 1][l2]--, dp[r1 + 1][r2 + 1]++;
}

int main() {

#ifndef ONLINE_JUDGE
    freopen("testdata.in", "r+", stdin);
    freopen("testdata.out", "w+", stdout);
#endif // ONLINE_JUDGE

#ifndef ONLINE_JUDGE
    auto start_time = clock();
    cerr << setprecision(3) << fixed;
#endif

/*
写代码时请注意：
    1.是否要开Long Long？数组边界处理好了么？
    2.实数精度
    3.下标能从最小值开始就从最小值开始
    5.排序之前不能取模.
    6.0-1子矩阵子序列:前缀和
    7.模拟题注意代码复用.
    8.单个区间问题考虑前缀和,多个区间左右端点拆开,排序,记录端点极值
思考提醒：
    1.最大值和最小值问题可不可以用二分+贪心？
    2.dp
    3.如果规模小的话还能尝试dfs
    4.如果存在等式.转换关系少可以暴力枚举变量,或者考虑从数据大小入手
*/

    ios::sync_with_stdio(false);
    long long k;
    cin >> n >> k;
    for (long long i = 1; i <= n; i++) {
        cin >> str[i];
    }
    for (long long i = 1; i <= n; i++) {
        long long l = -1, r = -1;
        for (long long j = 1; j <= n; j++) {
            if (str[i][j - 1] == 'B') {
                if (l == -1) l = j;
                r = j;
            }
        }
        if (l == -1) add(1, n, 1, n);
        else if (r - l + 1 <= k) add(max(1ll, i - k + 1), i, max(1ll, r - k + 1), l);
    }
    for (long long i = 1; i <= n; i++) {
        long long l = -1, r = -1;
        for (long long j = 1; j <= n; j++) {
            if (str[j][i - 1] == 'B') {
                if (l == -1) l = j;
                r = j;
            }
        }
        if (l == -1) add(1, n, 1, n);
        else if (r - l + 1 <= k) add(max(1ll, r - k + 1), l, max(1ll, i - k + 1), i);
    }

    for (long long i = 1; i <= n; i++) {
        for (long long j = 1; j <= n; j++) {
            dp[i][j] = dp[i][j] + dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1];
        }
    }

    long long res = 0;
    for (long long i = 1; i <= n; i++) {
        for (long long j = 1; j <= n; j++) {
            res = max(res, dp[i][j]);
        }
    }

    cout << res << endl;

#ifndef ONLINE_JUDGE
    auto end_time = clock();
    cerr << "Execution time: " << (end_time - start_time) * (int) 1e3 / CLOCKS_PER_SEC << " ms\n";
#endif

    return 0;

}