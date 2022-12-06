# https://www.acmicpc.net/problem/2629
import sys
input = sys.stdin.readline

n = int(input())
chu = list(map(int, input().split()))
m = int(input())
marbles = list(map(int, input().split()))
dp = [[0] * 15001 for _ in range(n+1)]
possible = []

def dfs(chu, n, now, left, right):
    new = abs(left - right)

    if new not in possible:
        possible.append(new)
    if now == n:
        return 0
    if dp[now][new] == 0:
        dfs(chu, n, now + 1, left + chu[now], right)
        dfs(chu, n, now + 1, left, right + chu[now])
        dfs(chu, n, now + 1, left, right)
        dp[now][new] = 1
dfs(chu, n, 0, 0, 0)
for i in range(0, m):
    if marbles[i] in possible:
        print('Y', end=' ')
    else:
        print('N', end=' ')