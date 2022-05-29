# https://www.acmicpc.net/problem/2667

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

N = int(input())
graph = [list(map(int, input())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
name = []
count = 0

def dfs(x,y):
  global count
  visited[x][y] = True
  if graph[x][y] == 1:
    count += 1

  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    if 0 <= nx < N and 0 <= ny < N:
      if graph[nx][ny] == 1 and visited[nx][ny] == False:
        dfs(nx, ny)

for i in range(N):
  for j in range(N):
    if visited[i][j] == False and graph[i][j] == 1:
      dfs(i, j)
      name.append(count)
      count = 0

name.sort()
print(len(name))
for i in name:
  print(i)

