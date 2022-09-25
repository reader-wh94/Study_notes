# https://www.acmicpc.net/problem/11053

n = int(input())
numbers = list(map(int, input().split()))
dp = [0 for i in range(n)]

for i in range(n):
    for j in range(n):
        if numbers[i] > numbers[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1

print(max(dp))