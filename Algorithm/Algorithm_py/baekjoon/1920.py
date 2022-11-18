# https://www.acmicpc.net/problem/1920

n = int(input())
a = set(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

for i in b:
    print('1' if i in a else '0')