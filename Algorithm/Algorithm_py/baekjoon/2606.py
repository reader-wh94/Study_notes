# https://www.acmicpc.net/problem/2606
from collections import deque

def bfs(v):
    global count
    queue = deque([v])

    while queue:
        pop = queue.popleft()
        visited[pop] = 1

        for i in graph[pop]:
            if visited[i] == 0:
                visited[i] = 1
                queue.append(i)
                count += 1

def dfs(v):
    global count
    visited[v] = 1

    for i in graph[v]:
        if visited[i] == 0:
            visited[i] = 1
            dfs(i)
            count += 1

N = int(input())
E = int(input())
graph = [[] for _ in range(N + 1)]
visited = [0 for _ in range(N + 1)]
count = 0

for i in range(E):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

bfs(1)
# dfs(1)
print(count)