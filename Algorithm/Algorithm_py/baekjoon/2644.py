# https://www.acmicpc.net/problem/2644
from collections import deque

def bfs(start):
    q = deque()
    q.append(start)
    visit = [0 for _ in range(N + 1)]
    visit[start] = 1

    while q:
        d = q.popleft()
        for i in graph[d]:
            if visit[i] == 0:
                visit[i] = 1
                result[i] = result[d] + 1
                q.append(i)

N = int(input())
a, b = map(int, input().split())
m = int(input())
graph = [[] for _ in range(N + 1)]
result = [0 for _ in range(N + 1)]

for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

bfs(a)
print(result[b] if result[b] != 0 else -1)


