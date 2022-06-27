# https://www.acmicpc.net/problem/1260
from collections import deque

N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited_dfs = [0] * (N + 1)
visited_bfs = [0] * (N + 1)

def dfs(v):
    visited_dfs[v] = 1
    print(v, end=" ")

    for i in graph[v]:
        if visited_dfs[i] == 0:
            dfs(i)
            visited_dfs[i] = 1

def bfs(v):
    visited_bfs[v] = 1
    queue = deque()
    queue.append(v)

    while queue:
        num = queue.popleft()
        print(num, end=" ")
        for i in graph[num]:
            if visited_bfs[i] == 0:
                queue.append(i)
                visited_bfs[i] = 1

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(len(graph)):
    graph[i].sort()

dfs(V)
print()
bfs(V)