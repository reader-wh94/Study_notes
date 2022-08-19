# https://www.acmicpc.net/problem/1978

n = int(input())
numbers = list(map(int, input().split()))
count = 0

for x in numbers:
    if x != 1:
        for i in range(2, x):
            if x % i == 0:
                break
        else:
            count += 1

print(count)