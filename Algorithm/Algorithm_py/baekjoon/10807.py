# https://www.acmicpc.net/problem/10807

n = int(input())
numbers = list(map(int, input().split()))
x = int(input())
cnt = 0

for i in numbers:
    if i == x:
        cnt += 1
print(cnt)