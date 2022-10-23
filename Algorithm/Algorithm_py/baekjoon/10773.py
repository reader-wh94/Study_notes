# https://www.acmicpc.net/problem/10773

k = int(input())
money = []

for _ in range(k):
    x = int(input())

    if x != 0:
        money.append(x)
    else:
        money.pop()
print(sum(money))