# https://www.acmicpc.net/problem/10830
import sys
input = sys.stdin.readline

def mul(arr, b):
    if b == 1:
        for i in range(n):
            for j in range(n):
                arr[i][j] %= 1000
        return arr

    elif b % 2 == 1:
        arr2 = mul(arr, b-1)
        res = []

        for i in range(n):
            temp = []
            for j in range(n):
                sum = 0
                for k in range(n):
                    sum += arr2[i][k] * arr[k][j]
                temp.append(sum % 1000)
            res.append(temp)
        return res
    else:
        arr2 = mul(arr, b // 2)
        res = []

        for i in range(n):
            temp = []
            for j in range(n):
                sum = 0
                for k in range(n):
                    sum += arr2[i][k] * arr2[k][j]
                temp.append(sum % 1000)
            res.append(temp)
        return res

n, b = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
ans = mul(a, b)

for i in ans:
    print(*i)