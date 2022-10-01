# https://www.acmicpc.net/problem/11659
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
# numbers = [0] + list(map(int, input().split()))

# for _ in range(m):
#     i, j = map(int, input().split())
#     sum = 0
#
#     for x in range(i, j+1):
#         sum += numbers[x]
#     print(sum)

numbers = list(map(int, input().split()))
preSum = [0]
sum = 0

for i in range(n):
    sum += numbers[i]
    preSum.append(sum)

for i in range(m):
    a, b = map(int, input().split())
    print(preSum[b] - preSum[a-1])

    #sys 미사용시 시간초과가 있다....!!!