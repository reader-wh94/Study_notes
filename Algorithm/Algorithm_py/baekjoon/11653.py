# https://www.acmicpc.net/problem/11653

n = int(input())
x = 2
while n != 1:
    if n % x == 0:
        print(x)
        n = n / x
    else:
        x += 1