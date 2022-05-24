# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV5PhcWaAKIDFAUq&categoryId=AV5PhcWaAKIDFAUq&categoryType=CODE&problemTitle=&orderBy=RECOMMEND_COUNT&selectCodeLang=PYTHON&select-1=1&pageSize=10&pageIndex=2

N = int(input())
num = []

for i in range(1, int(N ** (1/2)) + 1):
    if N % i == 0:
        num.append(i)
    if i**2 != N:
        num.append(N // i)

num.sort()

for i in num:
    print(i, end=" ")