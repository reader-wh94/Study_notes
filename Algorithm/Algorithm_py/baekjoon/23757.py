# https://www.acmicpc.net/problem/23757
import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input().split())
c = list(map(int, input().split()))
w = list(map(int, input().split()))
res = []

for i in c:
    heapq.heappush(res, -i)

for j in w:
    a = -heapq.heappop(res)
    if a > j:
        heapq.heappush(res, -(a - j))
    elif a == j:
        continue
    else:
        print(0)
        exit()
print(1)