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
      vector<vector<int>>dp(n+1,vector<int>(x+1));
      for(int i=0;i<n;i++){
            dp[i][0]=1;
      }
      for(int i=n-1;i>=0;i--){
            for(int sum=1;sum<=x;sum++){
                  int skipping=dp[i+1][sum];
                  int picking=0;
                  if(a[i]<=sum){
                        picking=dp[i][sum-a[i]];
                  }
                  dp[i][sum]=(picking+skipping)%mod;
            }
      }
      cout<<dp[0][x]<<endl;

      

}