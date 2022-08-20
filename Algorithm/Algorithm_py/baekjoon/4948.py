# https://www.acmicpc.net/problem/4948

num = []

for x in range(2, 246913):
    count = 0

    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            count += 1
            break

    if count == 0:
        num.append(x)

while True:
    n = int(input())
    res = 0

    if n == 0:
        break

    for i in num:
        if n < i <= 2*n:
            res += 1

    print(res)