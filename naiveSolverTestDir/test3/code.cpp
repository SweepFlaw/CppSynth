/* author Dc-HITMAN */
    		#pragma GCC optimize ("Ofast")
    		//#pragma GCC target ("sse,sse2,sse3,ssse3,sse4,popcnt,abm,mmx,avx,tune=native")
    		#pragma GCC optimize("unroll-loops")
    	/*#pragma warning(disable:4996)
    		#pragma comment(linker, "/stack:200000000")*/
    		#pragma GCC optimize ("-ffloat-store")
    	
    		#include<iostream>
    		#include<bits/stdc++.h>
    		#include<stdio.h>
    		using namespace std;
    			//#define TRACE
    	
    			//#ifdef TRACE
    		/*	#define trace(...) __f(#__VA_ARGS__, __VA_ARGS__)
    			template <typename Arg1>
    			void __f(const char* name, Arg1&& arg1){
    				cerr << name << " : " << arg1 << std::endl;
    			}
    			template <typename Arg1, typename... Args>
    			void __f(const char* names, Arg1&& arg1, Args&&... args){
    				const char* comma = strchr(names + 1, ',');cerr.write(names, comma - names) << " : " << arg1<<" | ";__f(comma+1, args...);
    			}
    			//#else
    			//#define trace(...)
    		//	#endif*/
    	
    			#define rep(i, n)    for(int i = 0; i < (n); ++i)
    			#define repA(i, a, n)  for(int i = a; i <= (n); ++i)
    			#define repD(i, a, n)  for(int i = a; i >= (n); --i)
    			#define trav(a, x) for(auto& a : x)
    			#define all(x) x.begin(), x.end()
    			#define sz(x) (int)(x).size()
    			#define fill(a)  memset(a, 0, sizeof (a))
    			#define fst first
    			#define snd second
    			#define mp make_pair
    			#define pb push_back
    			typedef long long ld;
    			typedef long long int ll;
    			typedef pair<int, int> pii;
    			typedef vector<int> vi;
    	
    		
   	struct UF {
					vi e;
					UF(int n) : e(n, -1) {}
					bool same_set(int a, int b) { return find(a) == find(b); }
					int size(int x) { return -e[find(x)]; }
					int find(int x) { return e[x] < 0 ? x : e[x] = find(e[x]); }
					void join(int a, int b) {
						a = find(a), b = find(b);
						if (a == b) return;
						if (e[a] > e[b]) swap(a, b);
						e[a] += e[b]; e[b] = a;
					}
			};
            //int st[1000000][24];
   
    int main() {
    	ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
        int n,k;
        cin>>n>>k;
        string s;
        vector<string> arr;
        rep(i,n){cin>>s;arr.pb(s);}
        int dp[n][n];
        fill(dp);
        int dp1[n][n];
        fill(dp1);
        for(int i=0;i<n;i++){
            if(arr[i][0]=='B')dp[i][0]=1;
            for(int j=1;j<n;j++){
                if(arr[i][j]=='B')dp[i][j]=dp[i][j-1]+1;
                else dp[i][j]=dp[i][j-1];
            }
        }
        for(int j=0;j<n;j++){
            if(arr[0][j]=='B')dp1[0][j]=1;
            for(int i=1;i<n;i++){
                if(arr[i][j]=='B')dp1[i][j]=dp1[i-1][j]+1;
                else dp1[i][j]=dp1[i-1][j];
            }
        }
        int col[n];
        fill(col);
        int row[n];
        fill(row);
        for(int i=0;i<n;i++){
            int a=0;
            for(int j=0;j<n;j++){
                if(arr[i][j]=='W')a++;
            }
            if(a==n)row[i]=1;
            if(i!=0)row[i]+=row[i-1];
        }
        for(int i=0;i<n;i++){
            int a=0;
            for(int j=0;j<n;j++){
                if(arr[j][i]=='W')a++;
            }
            if(a==n)col[i]=1;
            if(i!=0)col[i]+=col[i-1];
        }
      //  cout<<row[n-1]<<" "<<col[n-1]<<endl;
     // rep(i,n){rep(j,n)cout<<dp[i][j]<<" ";cout<<endl;}
   //  rep(i,n)cout<<row[i]<<" ";cout<<endl;
        int ans[n][n][2];
        fill(ans);
        int ans1=row[n-1]+col[n-1];
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                int a=0,b=0,c=0,d=0;
                if(j+k>n || i+k>n )continue;
                if(i==0 || j==0){
                    if(i==0){
                        a=row[n-1]-row[k-1];
                    }
                    else {a=row[n-1]-row[i+k-1]+row[i-1];}
                    if(j==0){
                        b=col[n-1]-col[k-1];
                    }
                    else{b=col[n-1]+col[j-1]-col[j+k-1];}
                    for(int l=i;l<i+k;l++){
                        c=dp[l][n-1];
                        if(j==0)d=dp[l][j+k-1];
                        else d=dp[l][j+k-1]-dp[l][j-1];
                        if(c==d)ans[i][j][0]++;
                    }
                    for(int l=j;l<j+k;l++){
                        c=dp1[n-1][l];
                        if(i==0)d=dp1[i+k-1][l];
                        else d=dp1[i+k-1][l]-dp1[i-1][l];
                        if(c==d)ans[i][j][1]++;
                    }
                    ans1=max(ans1,a+b+ans[i][j][0]+ans[i][j][1]);
                }
                else if(i+k>n || j+k>n)continue;
                else{
                    a=ans[i-1][j][0];
                    c=dp[i-1][n-1];
                    d=dp[i-1][j+k-1]-dp[i-1][j-1];
                    if(c==d)a--;
                    c=dp[i+k-1][n-1];
                    d=dp[i+k-1][j+k-1]-dp[i+k-1][j-1];
                    if(c==d)a++;
                    ans[i][j][0]=a;


                    a=ans[i][j-1][1];
                    c=dp1[n-1][j-1];
                    d=dp1[i+k-1][j-1]-dp1[i-1][j-1];
                    if(c==d)a--;
                    c=dp1[n-1][j+k-1];
                    d=dp1[i+k-1][j+k-1]-dp1[i-1][j+k-1];
                    if(c==d)a++;
                    ans[i][j][1]=a;
                    
                    a=row[i-1]+row[n-1]-row[i+k-1];
                    b=col[j-1]+col[n-1]-col[j+k-1];
                    ans1=max(ans1,a+b+ans[i][j][0]+ans[i][j][1]);
                }
              //  cout<<i<<" "<<j<<" "<<ans[i][j][0]<<" "<<ans[i][j][1]<<ans1<<endl;
            }
        }
        cout<<ans1<<endl;
    }	