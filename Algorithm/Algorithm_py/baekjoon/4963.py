# https://www.acmicpc.net/problem/4963
import sys
sys.setrecursionlimit(100000)

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

def dfs(x, y):
  graph[x][y] = -1

  for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]

    if 0 <= nx < h and 0 <= ny < w:
      if graph[nx][ny] == 1:
        graph[nx][ny] = -1
        dfs(nx, ny)

while True:
  w, h = map(int, input().split())
  graph = [list(map(int, input().split())) for _ in range(h)]
  count = 0

  if w == 0 and h == 0:
    break

  for i in range(h):
    for j in range(w):
      if graph[i][j] == 1:
        dfs(i, j)
        count += 1

  print(count)