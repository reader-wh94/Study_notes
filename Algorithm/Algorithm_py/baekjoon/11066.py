# https://www.acmicpc.net/problem/11066
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    k = int(input())
    pages = [0] + list(map(int, input().split()))
    sum_p = [0 for _ in range(k+1)]
    for i in range(1, k+1):
        sum_p[i] = sum_p[i-1] + pages[i]

    dp = [[0 for i in range(k+1)] for _ in range(k+1)]

    for i in range(2, k+1):
        for j in range(1, k+2-i):
            dp[j][j+i-1] = min([dp[j][j+p] + dp[j+p+1][j+i-1] for p in range(i-1)]) + (sum_p[j+i-1] - sum_p[j-1])
    print(dp[1][k])
