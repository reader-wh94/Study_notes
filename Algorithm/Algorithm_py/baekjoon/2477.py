# https://www.acmicpc.net/problem/2477
import sys
input = sys.stdin.readline

k = int(input())
length, small = [], []
x, y = [], []

for i in range(6):
    w, l = map(int, input().split())
    length.append([w, l])
    if length[i][0] == 1 or length[i][0] == 2:
        x.append(length[i][1])
    if length[i][0] == 3 or length[i][0] == 4:
        y.append(length[i][1])

for i in range(6):
    if length[i][0] == length[(i+2)%6][0]:
        small.append(length[(i+1)%6][1])

print(((max(x) * max(y)) - (small[0] * small[1])) * k)
