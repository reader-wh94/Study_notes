# https://www.acmicpc.net/problem/3009

rec = [list(map(int, input().split())) for _ in range(3)]

for i in range(2):
    ans = 0
    if rec[0][i] == rec[1][i]:
        ans = rec[2][i]
    elif rec[0][i] == rec[2][i]:
        ans = rec[1][i]
    elif rec[1][i] == rec[2][i]:
        ans = rec[0][i]
    print(ans, end=' ')
