# https://www.acmicpc.net/problem/1010
from math import factorial

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    ans = factorial(m) // (factorial(n) * factorial(m - n))
    print(ans)