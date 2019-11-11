#include <bits/stdc++.h>
using namespace std;

int main(){
    string s;
    cin>>s;
    int yi=0;
    for(int i=0;i<(int)s.size();i++){
        if(s[i]=='1')yi++;
    }
    if(yi==1&&s.size()%2==1){
        cout<<(s.size()-1)/2-1<<endl;
    }
    else if(yi==0)cout<<0<<endl; 
    else cout<<(s.size()-1)/2<<endl;
    return 0;
}