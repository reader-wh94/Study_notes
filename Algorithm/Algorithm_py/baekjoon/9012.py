import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    s = input().strip()
    stack = []

    for i in s:
        if i == '(':
            stack.append(i)
        else:
            if len(stack):
                stack.pop()
            else:
                print('NO')
                break
    else:
        if stack:
            print('NO')
        else:
            print('YES')