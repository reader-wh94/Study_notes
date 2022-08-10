# https://www.acmicpc.net/problem/25304

x = int(input())
n = int(input())
product = [list(map(int, input().split())) for _ in range(n)]
sum = 0

for i in range(n):
    sum += product[i][0] * product[i][1]

if sum == x:
    print("Yes")
else:
    print("No")