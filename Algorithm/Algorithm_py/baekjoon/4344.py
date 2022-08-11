# https://www.acmicpc.net/problem/4344

c = int(input())

for _ in range(c):
    lists = list(map(int, input().split()))
    avg = sum(lists[1:]) / lists[0]
    count = 0

    for i in lists[1:]:
        if i > avg:
            count += 1

    rate = count / lists[0] * 100
    print('{0:0.3f}%'.format(rate))