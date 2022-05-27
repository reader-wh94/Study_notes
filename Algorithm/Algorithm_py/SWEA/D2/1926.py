# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&problemLevel=3&contestProbId=AV5PTeo6AHUDFAUq&categoryId=AV5PTeo6AHUDFAUq&categoryType=CODE&problemTitle=&orderBy=RECOMMEND_COUNT&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=1

N = int(input())

for i in range(1, N + 1):
    s = str(i)
    count = 0

    for ss in s:
        if ss == '3' or ss == '6' or ss == '9':
            count += 1

    if count == 0:
        print(s, end=' ')
    else:
        print(count*'-', end=' ')