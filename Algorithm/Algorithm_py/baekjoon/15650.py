# https://www.acmicpc.net/problem/15650

n, m = map(int, input().split())
s = []
visited = [False] * (n+1)

def dfs(x):
    if len(s) == m:
        print(*s)
        return

    for i in range(x+1, n+1):
        if not visited[i]:
            visited[i] = True
            s.append(i)
            dfs(i)
            s.pop()
            visited[i] = False

dfs(0)
