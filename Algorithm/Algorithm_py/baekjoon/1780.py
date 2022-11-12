# https://www.acmicpc.net/problem/1780
import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
ans = [0, 0, 0]
def sol(x, y, n):
    count = graph[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if count != graph[i][j]:
                for k in range(3):
                    for l in range(3):
                        sol(x + k * n // 3, y + l * n // 3, n // 3)
                return
    if count == -1:
        ans[0] += 1
    elif count == 0:
        ans[1] += 1
    elif count == 1:
        ans[2] += 1

sol(0, 0, n)

for i in ans:
    print(i)