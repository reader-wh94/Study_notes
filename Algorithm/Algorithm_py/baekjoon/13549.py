# https://www.acmicpc.net/problem/13549
from collections import deque

n, k = map(int, input().split())
visited = [0] * 100001

def bfs():
    q = deque([n])
    visited[n] = 1

    while q:
        x = q.popleft()

        if x == k:
            print(visited[x] - 1)
            break

        if 0 <= x * 2 < 100001 and visited[x*2] == 0:
            visited[x*2] = visited[x]
            q.appendleft(x*2)
        if 0 <= x - 1 < 100001 and visited[x-1] == 0:
            visited[x-1] = visited[x] + 1
            q.append(x-1)
        if 0 <= x + 1 < 100001 and visited[x+1] == 0:
            visited[x+1] = visited[x] + 1
            q.append(x+1)
bfs()