# https://www.acmicpc.net/problem/14889
import sys
input = sys.stdin.readline

def dfs(depth, idx):
    global res

    if depth == n // 2:
        s_res, l_res = 0, 0
        for i in range(n):
            for j in range(i+1, n):
                if visited[i] and visited[j]:
                    s_res += arr[i][j] + arr[j][i]
                elif not visited[i] and not visited[j]:
                    l_res += arr[i][j] + arr[j][i]
        res = min(res, abs(s_res - l_res))

    for i in range(idx, n):
        if not visited[i]:
            visited[i] = True
            dfs(depth + 1, i + 1)
            visited[i] = False

n = int(input())
arr = []
visited = [False] * (n+1)
for i in range(n):
    arr.append(list(map(int, input().split())))

res = int(1e9)
dfs(0, 0)
print(res)