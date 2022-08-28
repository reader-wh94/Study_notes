# https://www.acmicpc.net/problem/2108
from collections import Counter

n = int(input())
nums = []

for _ in range(n):
    x = int(input())
    nums.append(x)

avg = round(sum(nums) / n)
print(avg)

nums.sort()
print(nums[n // 2])

counts = Counter(nums).most_common(2)
if len(counts) > 1:
    if counts[0][1] == counts[1][1]:
        print(counts[1][0])
    else:
        print(counts[0][0])
else:
    print(counts[0][0])

print(nums[n-1] - nums[0])