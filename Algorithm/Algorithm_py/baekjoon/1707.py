# https://www.acmicpc.net/problem/1707
"""import sys
sys.setrecursionlimit(10**6)

K = int(input())

def dfs(v, group):
    visited[v] = group

    for i in graph[v]:
        if visited[i] == 0:
            if not dfs(i, -group):
                return False
        elif visited[i] == visited[v]:
                return False
    return True

for _ in range(K):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]
    visited = [0] * (V + 1)

    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    result = True

    for i in range(1, V + 1):
        if visited[i] == 0:
            result = dfs(i, 1)
            if not result:
                break

    print("YES" if result else "NO")"""
#dfs는 시간초과 or 메모리 초과

from collections import deque

K = int(input())

def bfs(v):
    visited[v] = 1
    queue = deque()
    queue.append(v)

    while queue:
        a = queue.popleft()
        for i in graph[a]:
            if visited[i] == 0:
                visited[i] = -visited[a]
                queue.append(i)
            else:
                if visited[i] == visited[a]:
                    return False
    return True

for _ in range(K):
    V, E = map(int, input().split())
    result = True
    graph = [[] for _ in range(V + 1)]
    visited = [0] * (V + 1)

    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    for i in range(1, V + 1):
        if visited[i] == 0:
            if not bfs(i):
                result = False
                break
    print("YES" if result else "NO")
