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

        for i in (x*2, x+1, x-1):
            if 0 <= i < 100001 and visited[i] == 0:
                if i == x*2:
                    visited[i] = visited[x]
                    q.appendleft(i)
                else:
                    visited[i] = visited[x] + 1
                    q.append(i)

bfs()