# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV5QQhbqA4QDFAUq&categoryId=AV5QQhbqA4QDFAUq&categoryType=CODE&problemTitle=&orderBy=RECOMMEND_COUNT&selectCodeLang=PYTHON&select-1=1&pageSize=10&pageIndex=1

N = int(input())

for i in range(N):
    num = list(map(int, input().split()))
    print('#' + str(i + 1) + ' ' + str(max(num)))