#include<bits/stdc++.h>
using namespace std;
int mincost(int cost[4][4],int n,int p,int mask,int dp[1<<4]){
      if(p>=n){
            return 0;
      }
      if(dp[mask]!=INT_MAX){
            return dp[mask];
      }
      int minimum=INT_MAX;
      for(int j=0;j<n;j++){
            if(!(mask&(1<<j))){
                  int ans=mincost(cost,n,p+1,mask|(1<<j),dp)+cost[p][j];
                  minimum=min(minimum,ans);
            }
      }
      return dp[mask]=minimum;
}
int main(){
      int cost[4][4]={{10,2,6,5},{1,15,12,8},{7,8,9,3},{15,13,4,10}};
      int dp[1<<4];
      for(int i=0;i<(1<<4);i++){
            dp[i]=INT_MAX;
      }
      cout<<mincost(cost,4,0,0,dp)<<endl;
}