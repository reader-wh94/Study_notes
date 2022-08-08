# https://www.acmicpc.net/problem/2588

a = int(input())
b = int(input())
list_b = list(map(int, str(b)))
list_b.reverse()

for i in list_b:
    print(a * i)
print(a*b)
