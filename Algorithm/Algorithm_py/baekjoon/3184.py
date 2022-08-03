# https://www.acmicpc.net/problem/4179
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

r, c = map(int, input().split())
graph = [list(map(str, input().rstrip())) for _ in range(r)]
visited = [[0] * c for _ in range(r)]
wolf, sheep = 0, 0
q = deque()

def bfs(x, y):
    global w, s
    q.append((x, y))
    visited[x][y] = 1

    while q:
        x, y = q[0][0], q[0][1]
        del q[0]

        if graph[x][y] == 'v':
            w += 1
        elif graph[x][y] == 'o':
            s += 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < r and 0 <= ny < c and visited[nx][ny] == 0 and graph[nx][ny] != '#':
                q.append((nx, ny))
                visited[nx][ny] = 1

for i in range(r):
    for j in range(c):
        if not visited[i][j] and graph[i][j] == '#':
            w, s = 0, 0
            bfs(i, j)
            if w >= s:
                s = 0
            else:
                w = 0

            wolf += w
            sheep += s

print(sheep, wolf)