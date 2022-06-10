# https://www.acmicpc.net/problem/2468
import sys
sys.setrecursionlimit(1000000)

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def dfs(x, y, h):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < N:
            if graph[nx][ny] > h and visited[nx][ny] == False:
                visited[nx][ny] = True
                dfs(nx, ny, h)

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
ans = 0

for k in range(max(map(max, graph))):
    visited = [[False]*N for _ in range(N)]
    count = 0

    for i in range(N):
        for j in range(N):
            if graph[i][j] > k and visited[i][j] == False:
                visited[i][j] = True
                count += 1
                dfs(i, j, k)
    ans = max(ans, count)

print(ans)

#python3으로 하면 통과... pypy3은 메모리 초과... why?