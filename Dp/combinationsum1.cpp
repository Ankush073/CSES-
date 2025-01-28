#include<bits/stdc++.h>
using namespace std;
const int mod = 1e9 + 7;
int main(){ 
#ifndef ONLINE_JUDGE
      freopen("input.txt", "r", stdin);
      freopen("output.txt", "w", stdout);
#endif
      ios_base::sync_with_stdio(0);
      cin.tie(0);
      int n,x;
      cin>>n>>x;
      vector<int>a(n);
      for(int i=0;i<n;i++){
            cin>>a[i];
      }
      vector<int>dp(x+1);
      dp[0]=1;
      for(int i=1;i<=x;i++){
            for(int j=0;j<n;j++){
                  if(a[j]<=i) dp[i]=(dp[i]+dp[i-a[j]])%mod;
            }
      }
      cout<<dp[x]<<endl;

      

}