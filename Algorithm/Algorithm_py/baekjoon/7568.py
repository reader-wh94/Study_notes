# https://www.acmicpc.net/problem/7568

n = int(input())
member = [list(map(int, input().split())) for _ in range(n)]

for i in member:
    rank = 1
    for j in member:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end=' ')