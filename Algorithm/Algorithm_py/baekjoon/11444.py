# https://www.acmicpc.net/problem/11444

n = int(input())
p = 1000000007

def mul(a, b):
    n = len(a)
    res = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            temp = 0
            for k in range(n):
                temp += a[i][k] * b[k][j]
            res[i][j] = temp % p

def square(a, k):
    if k == 1:
        for i in range(len(a)):
            for j in range(len(a)):
                a[i][j] %= p
        return a

    temp = square(a, k // 2)
    if k % 2:
        return mul(mul(temp, temp), a)
    else:
        return mul(temp, temp)

graph = [[1, 1], [1, 0]]
print(square(graph, n)[0][1])