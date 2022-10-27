# https://www.acmicpc.net/problem/1874

n = int(input())
stack = []
op = []
cnt = 1
temp = True

for i in range(n):
    num = int(input())
    while cnt <= num:
        stack.append(cnt)
        op.append('+')
        cnt += 1
    if stack[-1] == num:
        stack.pop()
        op.append('-')
    else:
        temp = False
if temp:
    for i in op:
        print(i)
else:
    print('NO')