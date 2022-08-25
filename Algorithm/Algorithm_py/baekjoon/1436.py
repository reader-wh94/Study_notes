# https://www.acmicpc.net/problem/1436

n = int(input())
arr = [str(i) for i in range(666, 3000000)]
count = 0

for i in arr:
    if '666' in i:
        count += 1
    if count == n:
        print(i)
        break