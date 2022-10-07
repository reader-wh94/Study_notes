# https://www.acmicpc.net/problem/11047
import sys

n, k = map(int, sys.stdin.readline().split())
coin = []
count = 0

for _ in range(n):
    x = int(sys.stdin.readline())
    coin.append(x)

for i in range(n-1, -1, -1):
    if k == 0:
        break
    if coin[i] > k:
        continue
    count += k // coin[i]
    k %= coin[i]
print(count)