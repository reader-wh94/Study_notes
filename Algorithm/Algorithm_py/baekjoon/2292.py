# https://www.acmicpc.net/problem/2292

n = int(input())
room = 1
count = 1

while n > room:
    room = room + (6 * count)
    count += 1

print(count)
