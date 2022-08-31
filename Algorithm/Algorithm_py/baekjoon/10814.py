# https://www.acmicpc.net/problem/10814

n = int(input())
members = []

for _ in range(n):
    a, b = map(str, input().split())
    members.append((int(a), b))

members.sort(key=lambda x: x[0])

for i in members:
    print(*i, sep=' ')