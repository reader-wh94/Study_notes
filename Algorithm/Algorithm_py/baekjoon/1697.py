# https://www.acmicpc.net/problem/1697
from collections import deque

N, K = map(int, input().split())
max = 100001
visited = [0] * 100001

def bfs():
    q = deque()
    q.append(N)

    while q:
        x = q.popleft()

        if x == K:
            print(visited[x])
            break

        for i in (x-1, x+1, x*2):
            if 0 <= i <= max and visited[i] == 0:
                visited[i] = visited[x] + 1
                q.append(i)

bfs()