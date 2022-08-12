# https://www.acmicpc.net/problem/4673

def d(n):
    n = n + sum(map(int, str(n)))
    return n

non = set()

for i in range(1, 10001):
    non.add(d(i))

for i in range(1, 10001):
    if i not in non:
        print(i)