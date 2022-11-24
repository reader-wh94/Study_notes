# https://www.acmicpc.net/problem/2110
import sys
input = sys.stdin.readline

n, c = map(int, input().split())
house = []

for _ in range(n):
    house.append(int(input()))

house.sort()

start, end = 1, house[-1] - house[0]
line = 0

while start <= end:
    mid = (start + end) // 2
    count = 1
    current = house[0]

    for i in range(1, n):
        if house[i] >= current + mid:
            current = house[i]
            count += 1
    if count >= c:
        start = mid + 1
        line = mid
    else:
        end = mid - 1
print(line)