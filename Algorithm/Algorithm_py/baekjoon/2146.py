# https://www.acmicpc.net/problem/2146
from collections import deque
import sys

n = int(input())
map = [list(map(int, input().split())) for _ in range(n)]
ocean = deque()
num = -1

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def numbering(x, y):
    q = deque([(x, y)])
    map[x][y] = num

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if map[nx][ny] == 1:
                    map[nx][ny] = num
                    q.append((nx, ny))
                elif map[nx][ny] == 0 and not (x, y) in ocean:
                    ocean.append((x, y))

def distance():
    loop = 0
    ans = sys.maxsize # 0으로 놓으면 값은 0으로

    while ocean:
        loop += 1
        length = len(ocean)

        for _ in range(length):
            x, y = ocean.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < n and 0 <= ny < n:
                    if map[nx][ny] == 0:
                        map[nx][ny] = map[x][y]
                        ocean.append((nx, ny))
                    elif map[nx][ny] < map[x][y]:
                        ans = min(ans, (loop - 1) * 2)
                    elif map[nx][ny] > map[x][y]:
                        ans = min(ans, loop * 2 - 1)
    return ans

for i in range(n):
    for j in range(n):
        if map[i][j] > 0:
            numbering(i, j)
            num -= 1

print(distance())

# https://vixxcode.tistory.com/30 참고