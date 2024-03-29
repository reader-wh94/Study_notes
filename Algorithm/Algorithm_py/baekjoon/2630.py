# https://www.acmicpc.net/problem/2630
import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
res = []

def sol(x,y,n):
    color = graph[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != graph[i][j]:
                sol(x, y, n//2)
                sol(x, y+n//2, n//2)
                sol(x+n//2, y, n//2)
                sol(x+n//2, y+n//2, n//2)
                return
    if color == 0:
        res.append(0)
    else:
        res.append(1)

sol(0,0,n)
print(res.count(0))
print(res.count(1))
