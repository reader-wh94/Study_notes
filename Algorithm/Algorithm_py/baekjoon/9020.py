# https://www.acmicpc.net/problem/9020

def is_Prime(x):
    if x == 1:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

t = int(input())

for _ in range(t):
    n = int(input())
    a, b = n//2, n//2

    while a > 0:
        if is_Prime(a) and is_Prime(b):
            print(a, b)
            break
        else:
            a -= 1
            b += 1