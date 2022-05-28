# https://www.acmicpc.net/problem/4963
import sys
sys.setrecursionlimit(10000)

dx=[-1,0,1,0,-1,-1,1,1]
dy=[0,1,0,-1,-1,1,-1,1]

def dfs(x, y):
  for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]
    
    if (0 <= nx < h) and (0 <= ny < w):
      if graph[nx][ny] == 1:
        graph[nx][ny] = 0
        dfs(nx, ny)

while True:
  w, h = map(int, input().split())
  if w == 0 and h == 0:
    break
  
  graph = []
  for _ in range(h):
    graph.append(list(map(int, input().split())))
  
  count = 0
  
  for i in range(h):
    for j in range(w):
      if graph[i][j] == 1:
        count += 1
        graph[i][j] == 0
        dfs(i, j)
  
  print(count)