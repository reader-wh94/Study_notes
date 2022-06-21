# https://www.acmicpc.net/problem/1707

from collections import deque

K = int(input())

def bfs(v):
    visited[v] = 1
    queue = deque()
    queue.append(v)

    while queue:
        num = queue.popleft()
        for i in graph[num]:
            if visited[i] == 0:
                visited[i] = -visited[num]
                queue.append(i)
            else:
                if visited[i] == visited[num]:
                    return False
    return True

for _ in range(K):
    V, E = map(int, input().split())
    result = True
    graph = [[] for _ in range(V + 1)]
    visited = [1] + [0] * (V + 1)

    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    for i in range(1, V+1):
        if visited[i] == 0:
            if bfs(i) == False:
                result = False
                break

    print("YES" if result else "NO")
