# https://www.acmicpc.net/problem/1676

n = int(input())
count = 0

while n != 0:
    n //= 5
    count += n

print(count)