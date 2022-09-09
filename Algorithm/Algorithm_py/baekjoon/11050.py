# https://www.acmicpc.net/problem/11050

n, k = map(int, input().split())

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

print(factorial(n) // (factorial(k) * factorial(n - k)))