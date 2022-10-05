# https://www.acmicpc.net/problem/11660
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
numbers = [list(map(int, input().split())) for _ in range(n)]
sum = [[0] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        sum[i][j] = sum[i-1][j] + sum[i][j-1] - sum[i-1][j-1] + numbers[i-1][j-1]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    print(sum[x2][y2] - sum[x1-1][y2] - sum[x2][y1-1] + sum[x1-1][y1-1])
