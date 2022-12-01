# https://www.acmicpc.net/problem/1655

import sys
import heapq
input = sys.stdin.readline

n = int(input())
l_heap = []
r_heap = []
res = []

for _ in range(n):
    x = int(input())

    if len(l_heap) == len(r_heap):
        heapq.heappush(l_heap, (-x, x))
    else:
        heapq.heappush(r_heap, (x, x))

    if r_heap and l_heap[0][1] > r_heap[0][0]:
        min_num = heapq.heappop(r_heap)[0]
        max_num = heapq.heappop(l_heap)[1]
        heapq.heappush(l_heap, (-min_num, min_num))
        heapq.heappush(r_heap, (max_num, max_num))

    res.append(l_heap[0][1])

for i in res:
    print(i)