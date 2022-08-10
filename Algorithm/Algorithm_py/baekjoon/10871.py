# https://www.acmicpc.net/problem/10871

n, x = map(int, input().split())
number = list(map(int, input().split()))

for i in number:
    if i < x:
        print(i)