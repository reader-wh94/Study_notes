# https://www.acmicpc.net/problem/11724

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]
count = 0

def dfs(v):
    visited[v] = 1

    for i in graph[v]:
        if visited[i] == 0:
            dfs(i)

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, N+1):
    if visited[i] == 0:
        dfs(i)
        count += 1

print(count)