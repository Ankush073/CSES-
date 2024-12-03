mod=10**9+7
def tab(n):
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
          for j in range(1, 7):
               if(i-j>=0):
                  dp[i] = (dp[i]+dp[i - j])%mod

    return dp[n]
def solve(n,lookup={}):
      if(n<0):
            return 0
      if(n==0):
            return 1
      if n not in lookup:
            lookup[n]= (
                  solve(n-1)+
                  solve(n-2)+
                  solve(n-3)+
                  solve(n-4)+
                  solve(n-5)+
                  solve(n-6)
            )
      return lookup[n]
def main():
      n=int(input())
      # ans= solve(n,{})
      # print(ans%mod)
      ans=tab(n)
      print(ans%mod)
if __name__=="__main__":
      main()


