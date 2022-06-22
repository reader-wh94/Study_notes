# https://www.acmicpc.net/problem/10451

T = int(input())

def dfs(x):
    visited[x] = 1
    num = graph[x]
    if visited[num] == 0:
        dfs(num)

for _ in range(T):
    N = int(input())
    graph = [0] + list(map(int, input().split()))
    visited = [1] + [0] * N
    result = 0

    for i in range(1, N+1):
        if visited[i] == 0:
            dfs(i)
            result += 1
    print(result)