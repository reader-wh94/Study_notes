# https://www.acmicpc.net/problem/10250

t = int(input())

for _ in range(t):
    h, w, n = map(int, input().split())

    f, ho = 0, 0

    if n % h == 0:
        f = h * 100
        ho = n // h
    else:
        f = (n % h) * 100
        ho = n // h + 1
    print(f + ho)