# https://www.acmicpc.net/problem/1004
import sys
import math
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    x1, y1, x2, y2 = map(int, input().split())
    p = int(input())
    count = 0
    for _ in range(p):
        cx, cy, cr = map(int, input().split())
        dis1 = math.sqrt((x1 - cx) ** 2 + (y1 - cy) ** 2)
        dis2 = math.sqrt((x2 - cx) ** 2 + (y2 - cy) ** 2)

        if cr > dis1 and cr > dis2:
            pass
        elif cr > dis1:
            count += 1
        elif cr > dis2:
            count += 1
    print(count)