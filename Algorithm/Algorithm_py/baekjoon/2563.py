# https://www.acmicpc.net/problem/2563

n = int(input())
white = [[0 for _ in range(101)] for _ in range(101)]

for _ in range(n):
    x, y = map(int, input().split())

    for i in range(x, x+10):
        for j in range(y, y+10):
            white[i][j] = 1

ans = 0
for r in white:
    ans += r.count(1)
print(ans)