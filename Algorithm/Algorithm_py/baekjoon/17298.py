# https://www.acmicpc.net/problem/17298
import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
res = [-1] * n
stack = []

for i in range(n):
    while stack and a[stack[-1]] < a[i]:
        res[stack.pop()] = a[i]
    stack.append(i)

print(*res)