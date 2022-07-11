# https://www.acmicpc.net/problem/12851
from collections import deque

n, k = map(int, input().split())
visited = [0] * 100001
max = 100001
result = 0

def bfs():
    global result
    q = deque([n])
    visited[n] = 1

    while q:
        x = q.popleft()

        if x == k:
            result += 1
            continue

        for i in (x-1, x+1, 2*x):
            if 0 <= i < max and (visited[i] == visited[x] + 1 or visited[i] == 0):
                visited[i] = visited[x] + 1
                q.append(i)

bfs()

print(visited[k] - 1)
print(result)