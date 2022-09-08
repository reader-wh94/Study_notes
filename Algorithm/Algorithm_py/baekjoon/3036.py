# https://www.acmicpc.net/problem/3036
import sys
from math import gcd

n = int(sys.stdin.readline())
ring = list(map(int, sys.stdin.readline().split()))

standard = ring[0]

for i in range(1, n):
    x = gcd(standard, ring[i])

    print('{0}/{1}'.format(standard // x, ring[i] // x))