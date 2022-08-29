# https://www.acmicpc.net/problem/11651

n = int(input())
number_list = [list(map(int, input().split())) for _ in range(n)]

number_list.sort(key=lambda x: (x[1], x[0]))

for i, j in number_list:
    print(i, j)