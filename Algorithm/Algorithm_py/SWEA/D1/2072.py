# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&problemLevel=2&problemLevel=3&contestProbId=AV5QSEhaA5sDFAUq&categoryId=AV5QSEhaA5sDFAUq&categoryType=CODE&problemTitle=&orderBy=RECOMMEND_COUNT&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=1&problemLevel=1%2C2%2C3&&&&&&&&&

N = int(input())

for i in range(N):
    num = list(map(int, input().split()))
    sum = 0
    for j in range(10):
        if num[j] % 2 == 1:
            sum += num[j]
    print('#' + str(i + 1) + ' ' + str(sum))