# https://www.acmicpc.net/problem/10026

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

N = int(input())
graph = [list(map(str, input())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
count1 = 0

def dfs(x, y):
  visited[y][x] = 1

  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    if 0 <= nx < N and 0 <= ny < N:
      if visited[ny][nx] == 0 and graph[ny][nx] == graph[y][x]:
        dfs(nx, ny)

for i in range(N): # 적록색맹 아닌 경우
  for j in range(N):
    if visited[i][j] == 0:
      count1 += 1
      dfs(j, i)

for i in range(N): # 적록색맹인 경우 R을 G로 변경
  for j in range(N):
    if graph[i][j] == 'R':
      graph[i][j] = 'G'

count2 = 0
visited = [[0]*N for _ in range(N)]

for i in range(N): # 적록색맹인 경우 dfs 재시작
  for j in range(N):
    if visited[i][j] == 0:
      count2 += 1
      dfs(j, i)

print(count1, count2)