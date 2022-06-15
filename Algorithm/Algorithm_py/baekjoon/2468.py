# https://www.acmicpc.net/problem/2468
import sys
sys.setrecursionlimit(1000000)

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def dfs(x, y, h):
    visited[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < N:
            if visited[nx][ny] == False and graph[nx][ny] > h:
                dfs(nx, ny, h)

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
area = 0

for k in range(max(map(max, graph))):
    visited = [[False] * N for _ in range(N)]
    count = 0

    for i in range(N):
        for j in range(N):
            if visited[i][j] == False and graph[i][j] > k:
                count += 1
                dfs(i, j, k)

    area = max(area, count)

print(area)