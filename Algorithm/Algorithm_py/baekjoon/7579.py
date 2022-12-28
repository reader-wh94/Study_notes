# https://www.acmicpc.net/problem/7579
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
memory = [0] + list(map(int, input().split()))
cost = [0] + list(map(int, input().split()))
dp = [[0 for _ in range(sum(cost) + 1)] for _ in range(n+1)]
res = sum(cost)

for i in range(1, n+1):
    b = memory[i]
    c = cost[i]

    for j in range(1, sum(cost) + 1):
        if j < c:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(b + dp[i-1][j-c], dp[i-1][j])
        if dp[i][j] >= m:
            res = min(res, j)

if m != 0:
    print(res)
else:
    print(0)