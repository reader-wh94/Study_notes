# https://www.acmicpc.net/problem/1929
import math

m, n = map(int, input().split())

for x in range(m, n+1):
    if x == 1:
        continue
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            break
    else:
        print(x)