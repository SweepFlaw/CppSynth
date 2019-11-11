// #pragma GCC optimize(3)
#include<bits/stdc++.h>
using namespace std;
#define fi first
#define sc second
#define pb push_back
#define mp make_pair
#define LEN(X) strlen(X)
#define SZ(X) ((int)(X).size())
#define ALL(X) (X).begin(), (X).end()
#define FOR(I, N) for (int I = 0; I < (N); ++I)
#define FORD(I, N) for (int I = N; ~I; --I)
#define REP(I, A, B) for (int I = A; I <= (B); ++I)
#define REPD(I, B, A) for (int I = B; I >= A; --I)
#define FORS(I, S) for (int I = 0; S[I]; ++I)
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> pi;
typedef pair<ll, ll> pl;
const int N = 1e2 + 5;
const int R = 1e6 + 10;
const int MOD = 1e9 + 7;
int n;
int f[N][N];
int P[R];
bool del[R];
char s[N];
int ans[N], tot;
int main(){
    scanf("%d", &n);
    for (int i = 1; i <= n;i++)
    {
        for (int j = 1; j <= n;j++)
        {
            f[i][j] = R;
        }
    }
    for (int i = 1; i <= n;i++)
    {
        f[i][i] = 0;
        scanf(" %s", s + 1);
        int len = strlen(s + 1);
        for (int j = 1; j <= len;j++)
        {
            if (s[j]=='1'){
                f[i][j] = 1;
            }
        }
    }
    for (int k = 1; k <= n;k++)
    {
        for (int i = 1; i <= n;i++)
        {
            if (i==k)
                continue;
            for (int j = 1; j <= n;j++)
            {
                if (i==j || j==k)
                    continue;
                f[i][j] = min(f[i][j], f[i][k] + f[k][j]);
            }
        }
    }
    int m;
    scanf("%d", &m);
    for (int i = 1; i <= m;i++)
    {
        scanf("%d", &P[i]);
    }
    int la = P[1];
    for (int i = 2; i < m;i++)
    {
        int now = P[i];
        int nxt = P[i + 1];
        if (f[la][nxt]>=f[la][now]+f[now][nxt]){
            del[i] = 1;
        }else{
            la = P[i];
        }
    }
    
    for (int i = 1; i <= m;i++)
    {
        if (del[i]) continue;
        ans[++tot] = P[i];
    }
    printf("%d\n", tot);
    for (int i = 1; i <= tot;i++)
    {
        printf("%d%c", ans[i], i == tot ? '\n' : ' ');
    }
    return 0;
}