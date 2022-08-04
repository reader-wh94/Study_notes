# https://www.acmicpc.net/problem/2665
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


n = int(input())
graph = [list(map(int, input())) for _ in range(n)]
visited = [[-1] * n for _ in range(n)]

def bfs():
    q = deque()
    q.append((0, 0))

    visited[0][0] = 0

    while q:
        x, y = q.popleft()

        if x == n-1 and y == n-1:
            return visited[x][y]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == -1:
                if graph[nx][ny] == 1:
                    q.appendleft((nx, ny))
                    visited[nx][ny] = visited[x][y]
                else:
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1

print(bfs())