# https://www.acmicpc.net/problem/14226
from collections import deque

n = int(input())
q = deque()
graph = [[-1] * (n+1) for _ in range(n+1)]

q.append((1, 0)) # 화면 이모티콘, 클립 보드 이모티콘
graph[1][0] = 0

while q:
    x, y = q.popleft()

    if x == n:
        print(graph[x][y])
        break

    if graph[x][x] == -1:
        graph[x][x] = graph[x][y] + 1
        q.append((x, x))
    if x+y <= n and graph[x+y][y] == -1:
        graph[x+y][y] = graph[x][y] + 1
        q.append((x+y, y))
    if x-1 >= 0 and graph[x-1][y] == -1:
        graph[x-1][y] = graph[x][y] + 1
        q.append((x-1, y))