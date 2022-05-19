# https://www.acmicpc.net/problem/10026
import sys
sys.setrecursionlimit(10000)

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x,y):
  visited[y][x] = 1
  
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    
    if (0 <= nx < N) and (0 <= ny < N):
      if visited[ny][nx] == 0 and graph[y][x] == graph[ny][nx]:
        dfs(nx, ny)
        
N = int(input())
graph = [list(map(str, input())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
count1 = 0

for i in range(N):
  for j in range(N):
    if visited[i][j] == 0:
      count1 += 1
      dfs(j, i)
      
for i in range(N):
  for j in range(N):
    if graph[i][j] == 'R':
      graph[i][j] = 'G'

count2 = 0
visited = [[0]*N for _ in range(N)]
for i in range(N):
  for j in range(N):
    if visited[i][j] == 0:
      count2 += 1
      dfs(j, i)

print(count1, count2)