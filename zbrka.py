n, c = [int(x) for x in input().split()]

MOD = 10**9 + 7

dp = [[0 for _ in range(c + 1)] for _ in range(n + 1)]

for j in range(c + 1):
    dp[0][j] = 0

dp[1][0] = 1

for i in range(2, n + 1):
    for j in range(c + 1):
        if j >= i:
            dp[i][j] = (dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - i]) % MOD
        else:
            dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % MOD

print(dp[-1][-1])