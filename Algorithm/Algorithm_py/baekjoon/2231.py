# https://www.acmicpc.net/problem/2231

n = int(input())
res = 0

for i in range(1, n+1):
    x = list(map(int, str(i)))
    s = i + sum(x)

    if s == n:
        res = i
        break

print(res)