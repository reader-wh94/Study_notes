# https://www.acmicpc.net/problem/15649
from itertools import permutations

n, m = map(int, input().split())
# numbers = []
#
# for i in range(1, n+1):
#     numbers.append(i)
#
# perm = list(permutations(numbers, m))
#
# for x in perm:
#     print(*x)

s = []

def dfs():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return

    for i in range(1, n+1):
        if i in s:
            continue
        s.append(i)
        dfs()
        s.pop()

dfs()