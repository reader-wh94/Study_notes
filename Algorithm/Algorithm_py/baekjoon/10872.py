# https://www.acmicpc.net/problem/10872

n = int(input())

def factorial(x):
    result = 1
    if x > 0:
        result = x * factorial(x-1)
    return result

print(factorial(n))