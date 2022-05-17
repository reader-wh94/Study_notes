# https://www.acmicpc.net/problem/1012
import sys
sys.setrecursionlimit(10000)

def dfs(x, y):
  dx = [1,-1,0,0]
  dy = [0,0,1,-1]
  
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    
    if (0 <= nx < M) and (0 <= ny < N):
      if graph[ny][nx] == 1:
        graph[ny][nx] = -1
        dfs(nx, ny)
    
T = int(input())

for _ in range(T):
  M, N, K = map(int, input().split())
  graph = [[0]*M for _ in range(N)]
  count = 0
  
  for i in range(K):
    X, Y = map(int, input().split())
    graph[Y][X] = 1
    

  for i in range(M):
    for j in range(N):
      if graph[j][i] == 1:
        dfs(i, j)
        count += 1
      
  print(count)