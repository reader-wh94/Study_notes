# https://www.acmicpc.net/problem/2565

n = int(input())
lines = []
dp = [1] * n

for i in range(n):
    a, b = map(int, input().split())
    lines.append([a, b])

lines.sort()

sort_b = list(map(lambda x: x[1], lines))

for i in range(1, n):
    for j in range(i):
        if sort_b[i] > sort_b[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))