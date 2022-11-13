# https://www.acmicpc.net/problem/1629
a, b, c = map(int, input().split())

def sol(a, b):
    if b == 1:
        return a % c
    else:
        temp = sol(a, b//2)
        if b % 2 == 0:
            return (temp * temp) % c
        else:
            return (temp * temp * a) % c
print(sol(a, b))