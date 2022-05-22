# https://www.acmicpc.net/problem/2583
import sys
sys.setrecursionlimit(10000)

N, M, K = map(int, input().split())
graph = [[0]*N for _ in range(M)]
result = []
count=0

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def dfs(y, x):
    global count
    graph[y][x] = 1
    count += 1
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if(0 <= ny < M and 0 <= nx < N and graph[ny][nx] == 0):
            dfs(ny, nx)

for _ in range(K):
    y1, x1, y2, x2 = map(int, input().split())
    for j in range(y1, y2):
        for i in range(x1, x2):
            graph[j][i] = -1


for j in range(M):
    for i in range(N):
        if(graph[j][i] == 0):
            count=0
            dfs(j, i)
            result.append(count)

result.sort()
print(len(result))
for i in result:
    print(i, end=" ")