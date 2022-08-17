# https://www.acmicpc.net/problem/10870

n = int(input())

def fibonacci(x):
    if x <= 1:
        return x
    return fibonacci(x-1) + fibonacci(x - 2)

print(fibonacci(n))