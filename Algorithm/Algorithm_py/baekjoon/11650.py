# https://www.acmicpc.net/problem/11650

n = int(input())
number_list = [list(map(int, input().split())) for _ in range(n)]

number_list.sort()

for i, j in number_list:
    print(i, j)