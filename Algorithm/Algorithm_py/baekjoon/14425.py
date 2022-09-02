# https://www.acmicpc.net/problem/14425
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
s = set([input() for _ in range(n)])
count = 0

for _ in range(m):
    t = input()
    if t in s:
        count += 1

print(count)