# https://www.acmicpc.net/problem/1181

n = int(input())
sort_list = []

for _ in range(n):
    s = input()
    sort_list.append(s)

sort = set(sort_list)
sort_list = list(sort)
sort_list.sort()
sort_list.sort(key=len)

for x in sort_list:
    print(x)