n = int(input())
graph = [list(map(int, input())) for _ in range(n)]
res = []

def sol(x, y, n):
    check = graph[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if check != graph[i][j]:
                check = -1
                break
    if check == -1:
        print("(", end='')
        sol(x, y, n//2)
        sol(x, y+n//2, n//2)
        sol(x+n//2, y, n//2)
        sol(x+n//2, y+n//2, n//2)
        print(")", end='')
    elif check == 1:
        print(1, end='')
    elif check == 0:
        print(0, end='')

sol(0, 0, n)