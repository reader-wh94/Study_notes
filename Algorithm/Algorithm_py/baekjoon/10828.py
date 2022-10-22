# https://www.acmicpc.net/problem/10828
import sys

n = int(sys.stdin.readline())
stack = []

for _ in range(n):
    c = sys.stdin.readline().split()

    if c[0] == 'push':
        stack.append(c[1])
    elif c[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif c[0] == 'size':
        print(len(stack))
    elif c[0] == 'empty':
        print(1 if len(stack) == 0 else 0)
    elif c[0] == 'top':
        print(-1 if len(stack) == 0 else stack[-1])