# https://www.acmicpc.net/problem/11403

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [0 for _ in range(N)]

def dfs(x):
    for i in range(N):
        if graph[x][i] == 1 and visited[i] == 0:
            visited[i] = 1
            dfs(i)

for i in range(N):
    dfs(i)
    for j in range(N):
        if visited[j] == 1:
            print(1, end=" ")
        else:
            print(0, end=" ")
    print()
    visited = [0 for _ in range(N)]