# https://www.acmicpc.net/problem/5014
from collections import deque

f, s, g, u, d = map(int, input().split())
# f는 전체 층, g는 회사가 있는 층, s는 현재 위치, u는 위로 u층, d는 아래로 d층
visited = [0] * (f + 1)

def bfs():
    q = deque()
    q.append(s)
    visited[s] = 1

    while q:
        x = q.popleft()

        if x == g:
            print(visited[x] - 1)
            return

        for i in (x+u, x-d):
            if 0 < i <= f and visited[i] == 0:
                visited[i] = visited[x] + 1
                q.append(i)
    else:
        print("use the stairs")
        return

bfs()