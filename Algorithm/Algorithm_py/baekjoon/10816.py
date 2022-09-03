# https://www.acmicpc.net/problem/10816
import sys

n = int(input())
cards = list(map(int, sys.stdin.readline().split()))

m = int(input())
s_cards = list(map(int, sys.stdin.readline().split()))

dic = {}

for i in cards:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

for i in s_cards:
    if i in dic:
        print(dic[i], end=' ')
    else:
        print(0, end=' ')