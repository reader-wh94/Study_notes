# https://www.acmicpc.net/problem/2667

# 1. root의 아래, 좌, 우에 1이 있는지 확인
# -> dx, dy로 방향 이동용 리스트 저장 후 사용
# 2. 0이 있으면 다음 아래에 있는 idx 탐색
# -> True, False로 방문한 visited 리스트 사용
# Q. 1끼리 붙어 있는 단지는 어떻게 구분?
# Q. 단지 내 아파트 개수 따로 카운트

N = int(input())
graph = [list(map(int, input())) for _ in range(N)]
visited = [[False]*N for _ in range(N)]
num = []

#상하좌우 이동
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def dfs(x, y):
  global count
  visited[x][y] = True
  if graph[x][y] == 1:
    count += 1
  
  # 인접 노드 탐색하면서 연결되어 있으면 dfs 재귀호출
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < N and 0 <= ny < N:
      if visited[nx][ny] == False and graph[nx][ny] == 1:
        dfs(nx, ny)

count = 0

# 모든 정점을 확인해서 시작점이 될 수 있는지 확인
# 시작점이 가능하다면 dfs 탐색 시작
for i in range(N):
  for j in range(N):
    if graph[i][j] == 1 and visited[i][j] == False:
      dfs(i, j)
      num.append(count)
      count = 0
      
num.sort()
print(len(num))
for i in num:
  print(i)