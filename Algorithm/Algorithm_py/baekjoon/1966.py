# https://www.acmicpc.net/problem/1966
from collections import deque

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    q = deque(list(map(int, input().split())))
    cnt = 0

    while q:
        max_num = max(q)
        front = q.popleft()
        m -= 1

        if max_num == front:
            cnt += 1
            if m < 0:
                print(cnt)
                break
        else:
            q.append(front)
            if m < 0:
                m = len(q) - 1