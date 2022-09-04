# https://www.acmicpc.net/problem/1764
import sys

n, m = map(int, sys.stdin.readline().split())
listen = set()
watch = set()

for _ in range(n):
    listen.add(sys.stdin.readline().strip())

for _ in range(m):
    watch.add(sys.stdin.readline().strip())

member = sorted(list(listen & watch))
print(len(member))

for i in member:
    print(i)