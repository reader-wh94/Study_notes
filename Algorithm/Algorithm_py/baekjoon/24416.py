# https://www.acmicpc.net/problem/24416

n = int(input())
f = [0 for _ in range(41)]
count_re = 0
count_dp = 0

def fib(x):
    global count_re

    count_re += 1
    if x == 1 or x == 2:
        count_re -= 1
        return 1
    else:
        return fib(x-1) + fib(x-2)

def fibonacci(x):
    global count_dp
    f[1], f[2] = 1, 1

    for i in range(3, x+1):
        count_dp += 1
        f[i] = f[i-1] + f[i-2]
    return f[x]

fib(n)
fibonacci(n)
print(count_re+1, count_dp)
