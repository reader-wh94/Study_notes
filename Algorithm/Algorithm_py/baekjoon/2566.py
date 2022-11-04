# https://www.acmicpc.net/problem/2566

graph = [list(map(int, input().split())) for _ in range(9)]
x = max(map(max, graph))
print(x)

for i in range(9):
    for j in range(9):
        if graph[i][j] == x:
            print(i+1, j+1)