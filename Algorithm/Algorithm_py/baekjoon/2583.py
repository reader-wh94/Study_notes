# https://www.acmicpc.net/problem/2583
import sys
sys.setrecursionlimit(100000)

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def dfs(y, x):
    global count
    graph[y][x] = 1
    count += 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < M:
            if graph[ny][nx] == 0:
                dfs(ny, nx)

M, N, K = map(int, input().split())
graph = [[0]*N for _ in range(M)]
result = []
count = 0

for _ in range(K):
    x1,y1,x2,y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] = -1

for i in range(M):
    for j in range(N):
        if graph[i][j] == 0:
            count = 0
            dfs(i, j)
            result.append(count)

result.sort()
print(len(result))
for i in result:
    print(i, end=" ")