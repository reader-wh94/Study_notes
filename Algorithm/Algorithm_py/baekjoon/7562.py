# https://www.acmicpc.net/problem/7562
from collections import deque

dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]

T = int(input())

def bfs(x, y):
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()

        if x == endX and y == endY:
            return graph[endX][endY] - 1
        # 1부터 시작했으므로

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < l and 0 <= ny < l:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = graph[x][y] + 1
                    q.append((nx, ny))

for _ in range(T):
     l = int(input())
     startX, startY = map(int, input().split())
     endX, endY = map(int, input().split())
     graph = [[0] * l for _ in range(l)]

     graph[startX][startY] = 1

     print(bfs(startX, startY))
