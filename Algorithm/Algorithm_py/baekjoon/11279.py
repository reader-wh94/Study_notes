# https://www.acmicpc.net/problem/11279
# import sys
# input = sys.stdin.readline
#
# n = int(input())
# nums = []
# count_z = 0
#
# for _ in range(n):
#     x = int(input())
#
#     if x == 0:
#         if len(nums) == 0:
#             print(0)
#             continue
#         max_n = max(nums)
#         nums.remove(max_n)
#         print(max_n)
#     else:
#         nums.append(x)

import sys
import heapq as hq
input = sys.stdin.readline

n = int(input())
heap = []

for _ in range(n):
    x = int(input())

    if x == 0:
        if len(heap) == 0:
            print(0)
        else:
            print((-1) * hq.heappop(heap))
    else:
        hq.heappush(heap, (-1) * x)