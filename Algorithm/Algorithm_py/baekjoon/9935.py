# https://www.acmicpc.net/problem/9935
import sys
input = sys.stdin.readline

s = list(input().rstrip())
bomb = list(input().rstrip())
stack = []

for c in s:
    stack.append(c)

    if stack[-1] == bomb[-1] and len(stack) >= len(bomb):
        if stack[-len(bomb):] == bomb:
            for i in range(len(bomb)):
                stack.pop()
if stack:
    print("".join(stack))
else:
    print("FRULA")