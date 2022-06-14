# https://www.acmicpc.net/problem/1743
import sys
sys.setrecursionlimit(1000000)

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

N, M, K = map(int, input().split())
graph = [[0] * M for _ in range(N)]
visited = [[False] * M for _ in range(N)]
count = 0

def dfs(x, y):
    global count
    visited[x][y] = True

    if graph[x][y] == 1:
        count += 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if graph[nx][ny] == 1 and visited[nx][ny] == False:
                dfs(nx, ny)

for _ in range(K):
    r, c = map(int, input().split())
    graph[r-1][c-1] = 1

res = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1 and visited[i][j] == False:
            count = 0
            dfs(i, j)
            res = max(res, count)
print(res)