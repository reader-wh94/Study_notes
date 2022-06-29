# https://www.acmicpc.net/problem/2178
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

N, M = map(int, input().split())
graph = [list(map(int, input())) for _ in range(N)]

def bfs(x,y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = graph[x][y] + 1
                    # 현재 좌표값 + 1 를 다음 좌표값으로 갱신
                    queue.append((nx, ny))

    return graph[N-1][M-1]
    # 최종 N,M 위치에서의 graph 값을 반환(즉, 최소 거리)

print(bfs(0, 0))

# 값 입력시 input().split()인지 그냥 input()인지 구분 잘 하기