# https://www.acmicpc.net/problem/1620

import sys

n, m = map(int, input().split())
poketmon_id = {}
poketmon_name = {}

for i in range(n):
    x = sys.stdin.readline().strip()
    poketmon_id[i] = x
    poketmon_name[x] = i

for _ in range(m):
    x = sys.stdin.readline().strip()
    if x.isdigit():
        print(poketmon_id[int(x) - 1])
    else:
        print(poketmon_name[x] + 1)