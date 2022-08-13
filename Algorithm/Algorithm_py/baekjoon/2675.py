# https://www.acmicpc.net/problem/2675

t = int(input())

for _ in range(t):
    x, s = input().split()
    text = ""

    for i in s:
        text += int(x) * i
    print(text)