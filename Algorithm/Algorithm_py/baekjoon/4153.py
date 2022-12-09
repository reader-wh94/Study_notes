# https://www.acmicpc.net/problem/4153

while True:
    length = list(map(int, input().split()))

    a = max(length)
    length.remove(a)
    c = min(length)
    length.remove(c)
    b = length[0]

    if a == 0 and b == 0 and c == 0:
        break

    if b ** 2 + c ** 2 == a ** 2:
        print("right")
    else:
        print("wrong")