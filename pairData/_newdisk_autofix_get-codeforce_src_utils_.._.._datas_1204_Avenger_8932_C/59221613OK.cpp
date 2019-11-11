#include <bits/stdc++.h>
using namespace std;


int n;
int a[101][101];


void floyd_warshall()
{
    for ( int k = 0 ; k<= n-1; k++)
        for ( int i = 0; i<= n-1; i++)
            for ( int j = 0; j <= n-1; j++)
        {
            if ( a[i][j] > a[i][k] + a[k][j])
                a[i][j] = a[i][k] + a[k][j];
        }
}

int main()
{
    /*ifstream mf;
    //ofstream o ;
    mf.open("katryoshka.in");
    //o.open("holes.out",ios::out);
    streambuf* stream_buffer = mf.rdbuf();
    //streambuf* stream_buffer_file = o.rdbuf();
    //cout.rdbuf(stream_buffer_file);
    cin.rdbuf(stream_buffer);*/

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cin>>n;
    string s;
    for ( int i = 0; i<= n-1; i++)
    {
        cin>>s;
        for ( int j = 0; j<= n-1; j++)
        {
            a[i][j] = s[j] - '0';
        }

    }
    for ( int i = 0; i<= n-1; i++)
        for ( int j = 0; j<= n-1; j++)
    {
        if ( a[i][j] == 0 && i != j)
            a[i][j] = 9999;
    }
    floyd_warshall();
    int m;
    cin>>m;
    int b[m];
    for ( int i =0 ; i<= m-1; i++)
    {
        cin>>b[i];
        b[i]--;
    }


    vector<int> ans;
    ans.push_back(b[0]);
    int j = 0;
    for ( int i = 1; i<= m-1; i++)
    {   long long int dist = 0;
        for ( int k = j; k<= i-1; k++)
        {
            dist+= a[b[k]][b[k+1]];
        }
        if ( a[ans.back()][b[i]] < dist )
        {
            ans.push_back(b[i-1]);
            j = i-1;
        }
    }
    ans.push_back(b[m-1]);
    cout<<ans.size()<<'\n';
    for ( int i = 0; i< ans.size(); i++)
    {
        cout<<ans[i]+1<<' ';
    }
    return 0;
}
