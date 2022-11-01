# https://www.acmicpc.net/problem/2164
from collections import deque

n = int(input())
nums = deque([i for i in range(1, n+1)])

while len(nums) != 1:
    nums.popleft()
    x = nums.popleft()
    nums.append(x)

print(*nums)