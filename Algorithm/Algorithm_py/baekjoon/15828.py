# https://www.acmicpc.net/problem/15828
import sys
from collections import deque
input = sys.stdin.readline

buffer = int(input())
q = deque([])

while True:
    r = int(input())

    if r == -1:
        break
    elif r == 0:
        q.popleft()
    else:
        q.append(r)

if len(q) == 0:
    print('empty')
else:
    print(*q)