# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV13zo1KAAACFAYh&categoryId=AV13zo1KAAACFAYh&categoryType=CODE&problemTitle=&orderBy=RECOMMEND_COUNT&selectCodeLang=PYTHON&select-1=2&pageSize=10&pageIndex=1

t = int(input())

for tc in range(1, t+1):
    tc_num = int(input())
    scores = list(map(int, input().split()))
    num = [0] * 101

    for i in scores:
        num[i] += 1

    max_score = 0

    for i in range(0, len(num)):
        if num[i] >= max_score:
            max_index = i
            max_score = num[i]

    print('#%d %d' % (tc, max_index))