# https://www.acmicpc.net/problem/8958

t = int(input())

for _ in range(t):
    result = list(input())
    a, b = 0, 0

    for i in result:
        if i == 'O':
            b += 1
        else:
            b = 0
        a += b

    print(a)
