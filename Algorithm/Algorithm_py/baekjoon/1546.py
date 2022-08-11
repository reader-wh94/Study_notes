# https://www.acmicpc.net/problem/1546

n = int(input())

score = list(map(int, input().split()))
max = max(score)
new_score = []
sum = 0

for i in score:
    x = i / max * 100
    new_score.append(x)
    sum += x

print(sum / n)
