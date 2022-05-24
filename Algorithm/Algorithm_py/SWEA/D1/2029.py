# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV5QGNvKAtEDFAUq&categoryId=AV5QGNvKAtEDFAUq&categoryType=CODE&problemTitle=&orderBy=RECOMMEND_COUNT&selectCodeLang=PYTHON&select-1=1&pageSize=10&pageIndex=2

N = int(input())

for i in range(N):
    x, y = map(int, input().split())
    print(f"#{i + 1} {x // y} {x % y}")