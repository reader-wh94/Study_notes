# https://www.acmicpc.net/problem/9375
from collections import Counter
import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    clothes = []

    for i in range(n):
        a, b = map(str, sys.stdin.readline().split())
        clothes.append(b)

    ans = Counter(clothes)

    num = 1

    for j in ans:
        num *= (ans[j] + 1)

    print(num - 1)