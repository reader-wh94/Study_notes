# https://www.acmicpc.net/problem/1012
from collections import deque

T = int(input())

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs(x, y):
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] == 1:
                    q.append((nx, ny))
                    graph[nx][ny] = 0

for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [[0] * M for _ in range(N)]
    worm = 0

    for _ in range(K):
        x, y = map(int, input().split())
        graph[y][x] = 1

    for i in range(M):
        for j in range(N):
            if graph[j][i] == 1:
                bfs(j, i)
                worm += 1
    print(worm)