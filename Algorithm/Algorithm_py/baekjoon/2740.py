# https://www.acmicpc.net/problem/2740
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

m2, k = map(int, input().split())
b = [list(map(int, input().split())) for _ in range(m)]

res = [[0] * k for _ in range(n)]

for i in range(n):
    for j in range(k):
        for l in range(m):
            res[i][j] += a[i][l] * b[l][j]

for i in res:
    print(*i)