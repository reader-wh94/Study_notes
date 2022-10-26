# https://www.acmicpc.net/problem/4949

while True:
    s = input()
    stack = []
    flag = 1

    if s == '.':
        break

    for i in s:
        if i == '[' or i == '(':
            stack.append(i)
        elif i == ']':
            if len(stack) and stack[-1] == '[':
                stack.pop()
            else:
                flag = 0
                break
        elif i == ')':
            if len(stack) and stack[-1] == '(':
                stack.pop()
            else:
                flag = 0
                break
    if flag == 1 and len(stack) == 0:
        print('yes')
    else:
        print('no')