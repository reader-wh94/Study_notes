# https://www.acmicpc.net/problem/2805
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().split()))
start, end = 1, max(trees)

while start <= end:
    mid = (start + end) // 2
    height = 0

    for i in trees:
        if i >= mid:
            height += i - mid

    if height >= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)