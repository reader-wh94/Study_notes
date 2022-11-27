# https://www.acmicpc.net/problem/12015
import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
dp = [0]

for i in range(n):
    start = 0
    end = len(dp) - 1
    while start <= end:
        mid = (start + end) // 2
        if dp[mid] < a[i]:
            start = mid + 1
        else:
            end = mid - 1
    if start >= len(dp):
        dp.append(a[i])
    else:
        dp[start] = a[i]
print(len(dp) - 1)