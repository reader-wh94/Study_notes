# https://www.acmicpc.net/problem/2589
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

l, w = map(int, input().split())
map = [list(map(str, input())) for _ in range(l)]
result = 0
# l 육지 w 바다

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited = [[0] * w for _ in range(l)]
    # 새로 탐색할 때마다 visited 정보를 초기화
    visited[x][y] = 1
    max_n = 0

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < l and 0 <= ny < w:
                if map[nx][ny] == 'L' and visited[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    max_n = max(max_n, visited[nx][ny])
                    q.append((nx, ny))
    return max_n - 1

for i in range(l):
    for j in range(w):
        if map[i][j] == 'L':
            result = max(result, bfs(i, j))

print(result)