# https://www.acmicpc.net/problem/2581

a = int(input())
b = int(input())
number = []

for x in range(a, b+1):
    for i in range(2, x + 1):
        if x == i:
            number.append(x)
        if x % i == 0:
            break


if len(number) == 0:
    print(-1)
else:
    print(sum(number))
    print(number[0])