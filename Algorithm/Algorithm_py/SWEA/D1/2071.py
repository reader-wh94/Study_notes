# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV5QRnJqA5cDFAUq&categoryId=AV5QRnJqA5cDFAUq&categoryType=CODE&problemTitle=&orderBy=RECOMMEND_COUNT&selectCodeLang=PYTHON&select-1=1&pageSize=10&pageIndex=1

N = int(input())

for i in range(N):
    num = list(map(int, input().split()))
    avg = round(sum(num) / 10)
    print('#' + str(i + 1) + ' ' + str(avg))
