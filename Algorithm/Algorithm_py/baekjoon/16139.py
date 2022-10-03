# https://www.acmicpc.net/problem/16139

# S = list(map(str, input()))
# q = int(input())
#
# for _ in range(q):
#     s, a, b = map(str, input().split())
#     a = int(a)
#     b = int(b)
#
#     ss = S[a:b+1]
#     print(ss.count(s))
# 50점

import sys
input = sys.stdin.readline

s = list(input())
q = int(input())
count = []
alp = [0] * 26

for c in s:
    if 97 <= ord(c) <= 122:
        alp[ord(c) - 97] += 1
        count.append(alp[:])

for _ in range(q):
    c, s, e = input().split()
    ans = alp[int(e)][ord(c) - 97]

    if s != '0':
        ans -= alp[int(s) - 1][ord(c) - 97]
    print(ans)