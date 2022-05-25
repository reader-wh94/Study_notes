# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5LrsUaDxcDFAXc&categoryId=AV5LrsUaDxcDFAXc&categoryType=CODE&problemTitle=&orderBy=RECOMMEND_COUNT&selectCodeLang=PYTHON&select-1=2&pageSize=10&pageIndex=1&&&&&&&&&&

t = int(input())

for tc in range(1, t + 1) :
    n = int(input())
    num = list(map(int, input().split()))
    last = num[-1]
    result = 0

    for i in range(n-2, -1, -1) :
        if num[i] >= last :
            last = num[i]
        else :
            result += last - num[i]

    print('#%d %d' % (tc, result))