# https://www.acmicpc.net/problem/1260
from collections import deque

N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited_dfs = [0] * (N + 1)
visited_bfs = [0] * (N + 1)

def dfs(x):
    visited_dfs[x] = 1
    print(x, end=" ")

    for i in graph[x]:
        if visited_dfs[i] == 0:
            dfs(i)
            visited_dfs[i] = 1

def bfs(x):
    visited_bfs[x] = 1

    q = deque()
    q.append(x)

    while q:
        x = q.popleft()
        print(x, end=" ")

        for i in graph[x]:
            if visited_bfs[i] == 0:
                visited_bfs[i] = 1
                q.append(i)

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(len(graph)):
    graph[i].sort()

dfs(V)
print()
bfs(V)