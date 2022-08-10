# https://www.acmicpc.net/problem/15552

import sys

T = int(input())

for _ in range(T):
    a, b = map(int, sys.stdin.readline().split())
    print(a+b)