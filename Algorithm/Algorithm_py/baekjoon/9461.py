# https://www.acmicpc.net/problem/9461

n = int(input())
dp = [0] * 100000
dp[1], dp[2], dp[3] = 1, 1, 1

for _ in range(n):
    x = int(input())

    for i in range(4, x+1):
        dp[i] = dp[i-2] + dp[i-3]
    print(dp[x])