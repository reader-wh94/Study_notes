# https://www.acmicpc.net/problem/2798
from itertools import combinations

n, m = map(int, input().split())
cards = list(map(int, input().split()))

sum_list = list(combinations(cards, 3))
max_num = 0

for i in sum_list:
    temp = sum(i)

    if max_num < temp <= m:
        max_num = temp

print(max_num)
