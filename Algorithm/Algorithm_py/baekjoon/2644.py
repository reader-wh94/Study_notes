# https://www.acmicpc.net/problem/2644
from collections import deque

n = int(input())
a, b = map(int, input().split())
m = int(input())

graph = [[] for _ in range(n+1)]
result = [0] * (n+1)

def bfs(v):
    q = deque()
    q.append(v)

    while q:
        v = q.popleft()

        for n in graph[v]:
            if result[n] == 0:
                result[n] = result[v] + 1
                # 가중치
                q.append(n)

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

bfs(a)

print(result[b] if result[b] != 0 else -1)