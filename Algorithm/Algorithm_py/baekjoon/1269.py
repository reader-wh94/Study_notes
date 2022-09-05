# https://www.acmicpc.net/problem/1269
import sys

a, b = map(int, input().split())
a_list = set(map(int, sys.stdin.readline().split()))
b_list = set(map(int, sys.stdin.readline().split()))

count = len(a_list - b_list) + len(b_list - a_list)
print(count)