n, x = map(int, input().strip().split())
a = list(map(int, input().strip().split()))[:n]

def minc():
    dp = [1e9] * (x + 1)
    dp[0] = 0  # Base case: no coins needed to make sum 0
    
    for coin in a:  # Iterate through each coin
        for i in range(coin, x + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    
    return dp[x] if dp[x] != 1e9 else -1

def main():
    ans = minc()
    print(ans)

if __name__ == "__main__":
    main()
